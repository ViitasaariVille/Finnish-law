# Law-to-Rules Swarm

A CrewAI-based multi-agent system for converting Finnish legal text into structured business rules (DMN format).

## Architecture

The swarm consists of 6 specialized agents working in sequence:

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│ Law Reader  │────▶│Legal Analyst │────▶│ Rule Extractor  │
└─────────────┘     └──────────────┘     └─────────────────┘
                                                    │
┌─────────────┐     ┌──────────────┐               │
│   Output    │◀────│ DMN Formatter│◀──────────────┘
│ Formatter   │     └──────────────┘
└─────────────┘            ▲
                           │
                    ┌──────────────┐
                    │  Validator   │
                    └──────────────┘
```

## Agents

### 1. Law Reader
- **Role**: Extracts and segments legal text
- **Tools**: `extract_section`, `parse_definitions`
- **Output**: Structured list of sections and definitions

### 2. Legal Analyst
- **Role**: Analyzes legal meaning and identifies rule types
- **Expertise**: Finnish administrative and insurance law
- **Identifies**: Velvollisuus (obligation), Kielto (prohibition), Lupa (permission), Määritelmä (definition)

### 3. Business Rule Extractor
- **Role**: Converts provisions to IF-THEN rules
- **Output**: BusinessRule objects with conditions, actions, exceptions
- **Handles**: Implicit conditions, complex sentences

### 4. Rule Validator
- **Role**: QA for extracted rules
- **Checks**: Completeness, accuracy, exception handling
- **Output**: Validation report with issues

### 5. DMN Formatter
- **Role**: Converts rules to DMN 1.3 format
- **Output**: DMN-compatible JSON decision tables
- **Handles**: Hit policies, input/output variables

### 6. Gap Analyzer
- **Role**: Identifies missing coverage
- **Reports**: Uncovered sections, incomplete provisions
- **Output**: Prioritized gap list

## Usage

### Process a Single Section

```python
from swarm import process_law_section

law_text = """
5 § Vakuutettava ajoneuvo
Ajoneuvosta, joka on liikenteessä tai liikennettä varten 
rekisteröity Suomessa, on otettava liikennevakuutus.
"""

result = process_law_section(law_text, "§5")
print(result.business_rules)
print(result.dmn_rules)
```

### Process Full Law

```python
from swarm import process_full_law

with open("liikennevakuutuslaki.txt") as f:
    law_text = f.read()

result = process_full_law(
    law_text=law_text,
    law_name="Liikennevakuutuslaki",
    law_reference="460/2016"
)

# Save results
with open("rules.json", "w") as f:
    json.dump(result.dict(), f, indent=2, ensure_ascii=False)
```

## Output Format

### Business Rule
```json
{
  "rule_id": "INS-001",
  "rule_name": "Vakuutusvelvollisuus",
  "legal_basis": "§5.1",
  "source_text": "Ajoneuvosta... on otettava liikennevakuutus",
  "condition": "Ajoneuvo on liikenteessä TAI rekisteröity Suomessa",
  "action": "Liikennevakuutus on otettava",
  "exceptions": [],
  "priority": 5,
  "rule_type": "obligation"
}
```

### DMN Rule
```json
{
  "name": "InsuranceObligation",
  "description": "Determines if vehicle requires insurance",
  "hit_policy": "UNIQUE",
  "input_variables": ["vehicle.in_traffic", "vehicle.registered"],
  "output_variable": "insurance_required",
  "legal_source": "§5",
  "rules": [
    {
      "inputs": ["true", "true"],
      "output": "Mandatory",
      "legal_basis": "§5.1"
    }
  ]
}
```

## Installation

```bash
pip install crewai pydantic
```

## Configuration

Set environment variables for LLM:
```bash
export OPENAI_API_KEY=your_key
# or
export ANTHROPIC_API_KEY=your_key
```

## Testing

```bash
python -m pytest tests/
```

## License

MIT
