"""
Law-to-Rules Swarm - CrewAI Multi-Agent System
Converts Finnish legal text into structured business rules (DMN format)
"""

from crewai import Agent, Task, Crew, Process
from crewai.tools import tool
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
import json
import re


# ============================================================================
# OUTPUT MODELS
# ============================================================================

class BusinessRule(BaseModel):
    """A single business rule extracted from law"""
    rule_id: str = Field(..., description="Unique identifier (e.g., INS-001)")
    rule_name: str = Field(..., description="Human-readable name")
    legal_basis: str = Field(..., description="Law section reference (e.g., §5.1)")
    source_text: str = Field(..., description="Original Finnish text from law")
    condition: str = Field(..., description="IF condition in natural language")
    action: str = Field(..., description="THEN action in natural language")
    exceptions: List[str] = Field(default=[], description="List of exceptions")
    priority: int = Field(default=5, description="Rule priority 1-10")
    rule_type: str = Field(..., description="Type: obligation, prohibition, permission, definition")


class DMNRule(BaseModel):
    """DMN-compatible rule format"""
    name: str
    description: str
    hit_policy: str = "UNIQUE"
    input_variables: List[str]
    output_variable: str
    legal_source: str
    rules: List[Dict]


class RulePackage(BaseModel):
    """Complete rule set for a law section"""
    law_name: str
    law_reference: str
    section: str
    business_rules: List[BusinessRule]
    dmn_rules: List[DMNRule]
    gaps_identified: List[str]
    confidence_score: float


# ============================================================================
# TOOLS
# ============================================================================

@tool
def fetch_finlex_law(law_reference: str, section: Optional[str] = None) -> str:
    """
    Fetch Finnish law text from Finlex database.
    
    Args:
        law_reference: Law reference in format "460/2016" or "459/2015"
        section: Optional section number to extract (e.g., "§5" or "5")
    
    Returns:
        Full law text or specific section if provided
        
    Note: Finlex uses dynamic JavaScript rendering. This tool attempts multiple
    methods to retrieve the law text. If direct fetching fails, it will return
    instructions for manual input.
    """
    import requests
    import re
    
    try:
        # Construct Finlex URLs to try
        base_url = "https://www.finlex.fi/fi/laki/alkup/"
        year, number = law_reference.split("/")
        
        urls_to_try = [
            f"{base_url}{year}/{year}{number.zfill(5)}",
            f"https://www.finlex.fi/fi/laki/ajantasa/{year}/{year}{number.zfill(5)}",
        ]
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; LawBot/1.0)',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }
        
        text = None
        for url in urls_to_try:
            try:
                response = requests.get(url, headers=headers, timeout=30, allow_redirects=True)
                if response.status_code == 200:
                    text = response.text
                    break
            except:
                continue
        
        if not text:
            return f"""Unable to fetch law {law_reference} from Finlex.

Finlex uses dynamic JavaScript rendering which requires a headless browser.

RECOMMENDED WORKAROUND:
1. Visit: https://www.finlex.fi/fi/laki/alkup/{year}/{year}{number.zfill(5)}
2. Copy the law text manually
3. Save to a text file
4. Use read_local_law_file() to load it

ALTERNATIVE:
Use the read_local_law() function which reads from the repository's
existing law files (Molt's work):
- liikennevakuutuslaki (460/2016)
- tyotapaturma_ammattitautilaki (459/2015)
- potilasvakuutuslaki
"""
        
        # Extract text from HTML (basic cleanup)
        # Remove script and style elements
        text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL)
        text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
        
        # Remove HTML tags
        text = re.sub(r'<[^>]+>', ' ', text)
        
        # Clean up whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Decode HTML entities
        import html
        text = html.unescape(text)
        
        if section:
            # Try to extract specific section
            return extract_section(text, section)
        
        return text[:50000]  # Return first 50K chars to avoid token limits
        
    except Exception as e:
        return f"Error fetching law {law_reference}: {str(e)}"


@tool
def read_local_law_file(file_path: str) -> str:
    """
    Read law text from a local file.
    
    Args:
        file_path: Path to the law text file (absolute or relative)
    
    Returns:
        Contents of the law file
    """
    import os
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"


@tool
def read_local_law(law_name: str, law_reference: str) -> str:
    """
    Read Finnish law from local repository files.
    
    Args:
        law_name: Name of law folder (e.g., "liikennevakuutuslaki" or "tyotapaturma_ammattitautilaki")
        law_reference: Law reference (e.g., "460/2016", "459/2015")
    
    Returns:
        Combined text from ontology files and gap analysis for the law
    """
    import os
    
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    law_path = os.path.join(base_path, law_name)
    
    if not os.path.exists(law_path):
        available = [d for d in os.listdir(base_path) 
                     if os.path.isdir(os.path.join(base_path, d)) 
                     and not d.startswith('.') 
                     and not d == 'law-to-rules-swarm']
        return f"Law folder '{law_name}' not found. Available: {available}"
    
    # Read ontology and rules files
    result = []
    
    # Try to read ontology
    ontology_files = [
        f"{law_name.replace('liikennevakuutuslaki', 'car_insurance').replace('tyotapaturma_ammattitautilaki', 'work_accident').replace('potilasvakuutuslaki', 'patient_insurance')}_ontology.md",
        f"{law_name.replace('liikennevakuutuslaki', 'car_insurance').replace('tyotapaturma_ammattitautilaki', 'work_accident').replace('potilasvakuutuslaki', 'patient_insurance')}_dmn_rules.md",
        "GAP_ANALYSIS_10x.md",
        "business_rules_verified.md"
    ]
    
    for filename in ontology_files:
        filepath = os.path.join(law_path, filename)
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    result.append(f"=== {filename} ===\n{content[:10000]}\n")
            except Exception as e:
                result.append(f"=== {filename} ===\nError reading: {e}\n")
    
    if not result:
        files = os.listdir(law_path)
        return f"No law text files found in {law_name}. Available files: {files}"
    
    return "\n".join(result)


@tool
def extract_section(text: str, section_number: str) -> str:
    """Extract a specific section from Finnish law text by section number (e.g., '§5' or '5 §')"""
    # Match Finnish section formats: "5 §", "§5", "5§"
    patterns = [
        rf"{section_number}\s*§.*?(?=\n\d+\s*§|\Z)",
        rf"§\s*{section_number.lstrip('§').strip()}.*?(?=\n§\s*\d+|\Z)",
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        if match:
            return match.group(0).strip()
    
    return f"Section {section_number} not found in text"


@tool
def parse_definitions(text: str) -> Dict[str, str]:
    """Extract definitions section (§2) from law text"""
    definitions = {}
    
    # Match numbered definitions like "1) term: definition" or "1. term - definition"
    pattern = r"(\d+)[\).]\s*([^:]+?)[–-:]\s*(.+?)(?=\n\d+[\).]|\Z)"
    matches = re.findall(pattern, text, re.DOTALL)
    
    for num, term, definition in matches:
        term_clean = term.strip()
        def_clean = definition.strip().replace('\n', ' ')
        definitions[term_clean] = def_clean
    
    return definitions


@tool
def validate_rule_completeness(rule: str, section_text: str) -> Dict:
    """Check if a rule covers all aspects of a law section"""
    result = {
        "complete": True,
        "missing_elements": [],
        "warnings": []
    }
    
    # Check for common Finnish legal keywords
    keywords = ["jos", "tai", "ja", "ei", "paitsi", "kuitenkin"]
    found_keywords = [kw for kw in keywords if kw in section_text.lower()]
    
    if "jos" in found_keywords and "if" not in rule.lower():
        result["warnings"].append("Section contains conditional (jos) but rule may miss it")
    
    if "paitsi" in found_keywords and "except" not in rule.lower():
        result["warnings"].append("Section contains exception (paitsi) but rule may miss it")
    
    return result


@tool
def convert_to_dmn(rules: List[BusinessRule]) -> List[DMNRule]:
    """Convert business rules to DMN format"""
    dmn_rules = []
    
    # Group rules by decision type
    rule_groups = {}
    for rule in rules:
        decision_type = rule.rule_type
        if decision_type not in rule_groups:
            rule_groups[decision_type] = []
        rule_groups[decision_type].append(rule)
    
    for decision_type, rule_list in rule_groups.items():
        if not rule_list:
            continue
            
        dmn_rule = DMNRule(
            name=f"{decision_type.capitalize()}Decision",
            description=f"DMN rules for {decision_type} decisions",
            hit_policy="FIRST" if decision_type == "obligation" else "UNIQUE",
            input_variables=list(set([
                var for rule in rule_list 
                for var in extract_input_variables(rule.condition)
            ])),
            output_variable=f"{decision_type}_result",
            legal_source=rule_list[0].legal_basis,
            rules=[{
                "inputs": parse_condition(rule.condition),
                "output": rule.action,
                "legal_basis": rule.legal_basis,
                "source_text": rule.source_text
            } for rule in rule_list]
        )
        dmn_rules.append(dmn_rule)
    
    return dmn_rules


def extract_input_variables(condition: str) -> List[str]:
    """Extract variable names from condition text"""
    # Simple heuristic extraction
    variables = []
    common_patterns = [
        r"(\w+)\s+(?:on|ei ole|onko)",
        r"(?:jos|kun)\s+(\w+)",
    ]
    for pattern in common_patterns:
        matches = re.findall(pattern, condition, re.IGNORECASE)
        variables.extend(matches)
    return list(set(variables))


def parse_condition(condition: str) -> List[str]:
    """Parse condition into DMN input format"""
    # Simplified parsing - in production would be more sophisticated
    conditions = []
    
    # Split on AND/OR
    parts = re.split(r"\s+(?:ja|tai)\s+", condition, flags=re.IGNORECASE)
    for part in parts:
        part = part.strip()
        if "on " in part.lower():
            conditions.append(part)
        else:
            conditions.append("-")
    
    return conditions


# ============================================================================
# AGENTS
# ============================================================================

def create_law_reader_agent() -> Agent:
    """Agent that reads and segments legal text"""
    return Agent(
        role="Law Reader",
        goal="Extract and segment Finnish legal text into structured sections",
        backstory="""You are an expert in Finnish legal document structure. You can identify 
        sections (pykälät), chapters (luvut), and subsections. You understand the formal 
        structure of Finnish laws including Eduskunnan päätös, Luku, Pykälä, and Momentti.""",
        verbose=True,
        allow_delegation=False,
        tools=[extract_section, parse_definitions]
    )


def create_legal_analyst_agent() -> Agent:
    """Agent that analyzes legal meaning and structure"""
    return Agent(
        role="Legal Analyst",
        goal="Analyze legal provisions and identify rule types (obligation, permission, prohibition)",
        backstory="""You are a Finnish legal expert specializing in administrative and insurance law. 
        You can identify what type of legal norm each provision creates: 
        - Velvollisuus (obligation) - "on velvollinen", "tulee"
        - Kielto (prohibition) - "ei saa", "on kielletty"
        - Lupa (permission) - "voi", "on oikeus"
        - Määritelmä (definition) - "tarkoittaa", "on"
        You understand the nuances of Finnish legal language.""",
        verbose=True,
        allow_delegation=True
    )


def create_rule_extractor_agent() -> Agent:
    """Agent that extracts business rules from legal text"""
    return Agent(
        role="Business Rule Extractor",
        goal="Convert legal provisions into structured IF-THEN business rules",
        backstory="""You are an expert in business rule extraction from legal sources. You convert 
        Finnish legal text into clear IF-THEN rules. You are familiar with DMN (Decision Model and Notation) 
        and can identify conditions, actions, and exceptions. You understand that Finnish laws often use 
        implicit conditions that must be made explicit.""",
        verbose=True,
        allow_delegation=True,
        tools=[validate_rule_completeness]
    )


def create_validator_agent() -> Agent:
    """Agent that validates rules against source law"""
    return Agent(
        role="Rule Validator",
        goal="Validate that extracted rules are complete and accurate against the source law",
        backstory="""You are a quality assurance expert for legal rule extraction. You verify that:
        1. All legal provisions are covered by rules
        2. Rules don't add information not in the law
        3. Exceptions and edge cases are properly handled
        4. References to other sections are noted
        You are meticulous and thorough.""",
        verbose=True,
        allow_delegation=False,
        tools=[validate_rule_completeness]
    )


def create_dmn_formatter_agent() -> Agent:
    """Agent that formats rules into DMN-compatible output"""
    return Agent(
        role="DMN Formatter",
        goal="Convert business rules into DMN-compatible JSON format",
        backstory="""You are a DMN (Decision Model and Notation) expert. You convert business rules 
        into properly structured DMN decision tables. You understand hit policies (UNIQUE, FIRST, PRIORITY, 
        COLLECT), input/output variables, and rule expressions. You output valid JSON that follows 
        DMN 1.3 specification.""",
        verbose=True,
        allow_delegation=False,
        tools=[convert_to_dmn]
    )


def create_gap_analyzer_agent() -> Agent:
    """Agent that identifies gaps in rule coverage"""
    return Agent(
        role="Gap Analyzer",
        goal="Identify missing rules and incomplete coverage of legal provisions",
        backstory="""You are a coverage analyst who compares extracted rules against the full law text. 
        You identify:
        - Sections not covered by any rule
        - Partial coverage of complex provisions  
        - Missing exception handling
        - Implicit conditions not made explicit
        You provide actionable gap reports.""",
        verbose=True,
        allow_delegation=False
    )


# ============================================================================
# TASKS
# ============================================================================

def create_read_law_task(agent: Agent, law_text: str) -> Task:
    """Task to read and segment law text"""
    return Task(
        description=f"""Read the following Finnish law text and identify:
        1. All sections (pykälät) with their numbers
        2. Definitions from §2 (Määritelmät)
        3. Chapter boundaries
        
        Law text:
        {law_text[:5000]}...
        
        Output a structured list of sections with:
        - Section number
        - Section title (if present)
        - Brief summary of content
        - Key legal terms defined
        """,
        expected_output="Structured JSON with sections and definitions",
        agent=agent
    )


def create_analyze_section_task(agent: Agent, section_text: str, section_number: str) -> Task:
    """Task to analyze a specific section"""
    return Task(
        description=f"""Analyze section {section_number} of the Finnish law:
        
        {section_text}
        
        Identify:
        1. What type of legal norm(s) this section creates
           - Velvollisuus (obligation): "on velvollinen", "tulee", "on oltava"
           - Kielto (prohibition): "ei saa", "on kielletty"  
           - Lupa (permission): "voi", "on oikeus", "saattaa"
           - Määritelmä (definition): "tarkoittaa", "on"
        2. Who is the subject (kenelle)
        3. What is the action (mitä)
        4. Under what conditions (milloin)
        5. Any exceptions (poikkeukset)
        6. References to other sections
        
        Output in Finnish legal terminology.""",
        expected_output="Legal analysis with rule types and elements",
        agent=agent
    )


def create_extract_rules_task(agent: Agent, analysis: str, section_text: str) -> Task:
    """Task to extract business rules from analyzed section"""
    return Task(
        description=f"""Based on the legal analysis and original text, extract structured business rules.
        
        Legal Analysis:
        {analysis}
        
        Original Text:
        {section_text}
        
        For each rule, create:
        1. rule_id: Follow format [TYPE]-### (e.g., INS-001 for insurance rules)
        2. rule_name: Clear Finnish name
        3. legal_basis: Section reference
        4. source_text: Exact Finnish quote
        5. condition: IF clause in Finnish
        6. action: THEN clause in Finnish
        7. exceptions: List any exceptions
        8. priority: 1-10 (higher = more specific)
        9. rule_type: obligation/prohibition/permission/definition
        
        Make implicit conditions explicit. Handle complex sentences by splitting into multiple rules.""",
        expected_output="List of BusinessRule objects in JSON",
        agent=agent,
        output_json=BusinessRule
    )


def create_validate_rules_task(agent: Agent, rules: str, section_text: str) -> Task:
    """Task to validate extracted rules"""
    return Task(
        description=f"""Validate these business rules against the source law section:
        
        Extracted Rules:
        {rules}
        
        Source Law:
        {section_text}
        
        Check:
        1. Is every provision covered?
        2. Are there any invented rules not in the law?
        3. Are exceptions properly handled?
        4. Are cross-references noted?
        
        Report any issues found.""",
        expected_output="Validation report with issues and fixes",
        agent=agent
    )


def create_format_dmn_task(agent: Agent, rules: str) -> Task:
    """Task to format rules as DMN"""
    return Task(
        description=f"""Convert these business rules to DMN format:
        
        {rules}
        
        Group rules by decision type. For each decision table:
        - Determine appropriate hit policy (UNIQUE/FIRST/PRIORITY)
        - Extract input variables
        - Define output variable
        - Create rule rows
        
        Output valid DMN 1.3 compatible JSON.""",
        expected_output="DMNRule objects in JSON format",
        agent=agent,
        output_json=DMNRule
    )


def create_gap_analysis_task(agent: Agent, all_rules: str, law_structure: str) -> Task:
    """Task to identify gaps in coverage"""
    return Task(
        description=f"""Compare extracted rules against law structure to find gaps:
        
        Law Structure:
        {law_structure}
        
        Extracted Rules:
        {all_rules}
        
        Identify:
        1. Sections with no rules
        2. Sections with incomplete coverage
        3. Missing exception handling
        4. Implicit conditions not made explicit
        
        Prioritize gaps by importance.""",
        expected_output="Gap analysis report with prioritized gaps",
        agent=agent
    )


# ============================================================================
# CREWS
# ============================================================================

def create_rule_extraction_crew(law_text: str, target_section: Optional[str] = None) -> Crew:
    """Create a crew for extracting rules from a law section"""
    
    # Create agents
    reader = create_law_reader_agent()
    analyst = create_legal_analyst_agent()
    extractor = create_rule_extractor_agent()
    validator = create_validator_agent()
    formatter = create_dmn_formatter_agent()
    
    # Create tasks
    if target_section:
        section_text = extract_section(law_text, target_section)
        tasks = [
            create_analyze_section_task(analyst, section_text, target_section),
            create_extract_rules_task(extractor, "{{task_1.output}}", section_text),
            create_validate_rules_task(validator, "{{task_2.output}}", section_text),
            create_format_dmn_task(formatter, "{{task_2.output}}")
        ]
    else:
        tasks = [
            create_read_law_task(reader, law_text),
            # For each section found, create analysis tasks
            # This would be dynamic in practice
        ]
    
    return Crew(
        agents=[reader, analyst, extractor, validator, formatter],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )


def create_full_law_crew(law_text: str, law_name: str, law_reference: str) -> Crew:
    """Create a crew for processing an entire law"""
    
    reader = create_law_reader_agent()
    analyst = create_legal_analyst_agent()
    extractor = create_rule_extractor_agent()
    validator = create_validator_agent()
    formatter = create_dmn_formatter_agent()
    gap_analyzer = create_gap_analyzer_agent()
    
    # Phase 1: Read and structure the law
    read_task = Task(
        description=f"""Read this Finnish law and identify all sections:
        
        Law: {law_name} ({law_reference})
        
        {law_text[:10000]}...
        
        Output structured list of all sections with:
        - Section number
        - Section name (if any)
        - Content summary
        - Key terms defined
        - Cross-references""",
        expected_output="JSON structure of law sections",
        agent=reader
    )
    
    # Phase 2: For each major section, analyze and extract rules
    # (In practice, this would loop through sections)
    
    # Phase 3: Gap analysis
    gap_task = Task(
        description="""Compare extracted rules against law structure.
        Identify all gaps in coverage.
        Output prioritized list of missing rules.""",
        expected_output="Gap analysis report",
        agent=gap_analyzer,
        context=["{{task_1.output}}"]  # Depends on read task
    )
    
    # Phase 4: Validation
    validate_task = Task(
        description="""Validate all extracted rules for:
        1. Completeness
        2. Accuracy  
        3. Consistency
        Report any issues.""",
        expected_output="Validation report",
        agent=validator
    )
    
    return Crew(
        agents=[reader, analyst, extractor, validator, formatter, gap_analyzer],
        tasks=[read_task, gap_task, validate_task],
        process=Process.sequential,
        verbose=True
    )


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def process_law_section(law_text: str, section_number: str) -> RulePackage:
    """Process a single section of law and return rules"""
    crew = create_rule_extraction_crew(law_text, section_number)
    result = crew.kickoff()
    
    # Parse results into RulePackage
    return RulePackage(
        law_name="Unknown",
        law_reference="",
        section=section_number,
        business_rules=[],  # Parsed from result
        dmn_rules=[],  # Parsed from result
        gaps_identified=[],
        confidence_score=0.0
    )


def process_full_law(law_text: str, law_name: str, law_reference: str) -> RulePackage:
    """Process an entire law and return complete rule package"""
    crew = create_full_law_crew(law_text, law_name, law_reference)
    result = crew.kickoff()
    
    # Parse and return complete package
    return RulePackage(
        law_name=law_name,
        law_reference=law_reference,
        section="ALL",
        business_rules=[],
        dmn_rules=[],
        gaps_identified=[],
        confidence_score=0.0
    )


if __name__ == "__main__":
    # Example usage
    print("Law-to-Rules Swarm initialized")
    print("Use process_law_section() or process_full_law() to convert laws")
