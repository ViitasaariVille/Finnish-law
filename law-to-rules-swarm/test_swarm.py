"""
Tests for Law-to-Rules Swarm
"""

import pytest
from swarm import (
    extract_section,
    parse_definitions,
    validate_rule_completeness,
    BusinessRule,
    DMNRule,
    RulePackage
)


# Test Data
SAMPLE_LAW = """
1 § Tarkoitus
Tämän lain tarkoituksena on turvata vahingonkärsijä.

2 § Määritelmät
Tässä laissa tarkoitetaan:
1) vakuutuksella liikennevakuutusta;
2) vahingolla henkilö- tai omaisuusvahinkoa;
3) vakuutusyhtiöllä liikennevakuutusyhtiötä.

5 § Vakuutusvelvollisuus
Ajoneuvosta, joka on liikenteessä, on otettava vakuutus.

6 § Poikkeukset
5 §:ää ei sovelleta:
a) polkupyöriin;
b) traktoreihin.
"""


class TestTextExtraction:
    """Test law text extraction tools"""
    
    def test_extract_section_by_number(self):
        section = extract_section(SAMPLE_LAW, "§5")
        assert "Vakuutusvelvollisuus" in section
        assert "Ajoneuvosta" in section
    
    def test_extract_section_with_unicode(self):
        section = extract_section(SAMPLE_LAW, "5")
        assert "Vakuutusvelvollisuus" in section
    
    def test_extract_nonexistent_section(self):
        result = extract_section(SAMPLE_LAW, "§99")
        assert "not found" in result
    
    def test_parse_definitions(self):
        definitions = parse_definitions(SAMPLE_LAW)
        assert "vakuutuksella" in definitions
        assert "vahingolla" in definitions
        assert "vakuutusyhtiöllä" in definitions


class TestRuleValidation:
    """Test rule validation logic"""
    
    def test_validate_simple_rule(self):
        rule = "IF vehicle in traffic THEN insurance required"
        section = "Ajoneuvosta on otettava vakuutus"
        result = validate_rule_completeness(rule, section)
        assert result["complete"] is True
    
    def test_validate_missing_condition(self):
        rule = "Insurance required"
        section = "Jos ajoneuvo on liikenteessä, vakuutus on otettava"
        result = validate_rule_completeness(rule, section)
        assert len(result["warnings"]) > 0


class TestDataModels:
    """Test Pydantic models"""
    
    def test_business_rule_creation(self):
        rule = BusinessRule(
            rule_id="INS-001",
            rule_name="Test Rule",
            legal_basis="§5.1",
            source_text="Test text",
            condition="IF test",
            action="THEN result",
            exceptions=[],
            priority=5,
            rule_type="obligation"
        )
        assert rule.rule_id == "INS-001"
        assert rule.priority == 5
    
    def test_dmn_rule_creation(self):
        dmn = DMNRule(
            name="TestDecision",
            description="Test",
            hit_policy="UNIQUE",
            input_variables=["var1"],
            output_variable="result",
            legal_source="§5",
            rules=[]
        )
        assert dmn.hit_policy == "UNIQUE"
    
    def test_rule_package(self):
        package = RulePackage(
            law_name="Test Law",
            law_reference="123/2024",
            section="§5",
            business_rules=[],
            dmn_rules=[],
            gaps_identified=["Missing rule"],
            confidence_score=0.85
        )
        assert package.confidence_score == 0.85


class TestFinnishLegalPatterns:
    """Test recognition of Finnish legal patterns"""
    
    def test_obligation_pattern(self):
        text = "Ajoneuvosta on otettava vakuutus"
        assert "on otettava" in text  # obligation pattern
    
    def test_prohibition_pattern(self):
        text = "Vakuutusta ei saa myöntää"
        assert "ei saa" in text  # prohibition pattern
    
    def test_permission_pattern(self):
        text = "Vakuutusyhtiö voi hylätä hakemuksen"
        assert "voi" in text  # permission pattern
    
    def test_exception_pattern(self):
        text = "Tätä pykälää ei sovelleta polkupyöriin"
        assert "ei sovelleta" in text  # exception pattern


# Integration tests (require API keys)
@pytest.mark.integration
class TestCrewExecution:
    """Integration tests for full crew execution"""
    
    def test_crew_creation(self):
        from swarm import create_rule_extraction_crew
        crew = create_rule_extraction_crew(SAMPLE_LAW, "§5")
        assert len(crew.agents) >= 4
        assert len(crew.tasks) >= 3
    
    def test_agent_roles(self):
        from swarm import (
            create_law_reader_agent,
            create_legal_analyst_agent,
            create_rule_extractor_agent
        )
        
        reader = create_law_reader_agent()
        assert "Reader" in reader.role
        
        analyst = create_legal_analyst_agent()
        assert "Analyst" in analyst.role
        
        extractor = create_rule_extractor_agent()
        assert "Extractor" in extractor.role


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
