"""
Example usage of Law-to-Rules Swarm
Demonstrates processing Finnish traffic insurance law sections
"""

from swarm import (
    process_law_section,
    process_full_law,
    create_rule_extraction_crew,
    BusinessRule,
    DMNRule
)
import json


# Example: Section 5 of Liikennevakuutuslaki
SECTION_5 = """
5 § Vakuutettava ajoneuvo

Ajoneuvosta, joka on liikenteessä tai liikennettä varten rekisteröity 
Suomessa, on otettava liikennevakuutus tämän lain mukaisesti.

Mitä 1 momentissa säädetään, ei koske:
1) ajoneuvoa, joka on merkitty rekisteristä poistetuksi;
2) ajoneuvoa, jonka käyttövoimana on vain ihmisvoima tai eläinvoima;
3) ajoneuvoa, jonka rakenteellinen nopeus on enintään 6 km/h;
4) työkoneena käytettävää ajoneuvoa, jos se ei ole muutenkaan 
   rekisteröintivelvollinen.
"""


def example_single_section():
    """Process just section 5"""
    print("=" * 60)
    print("Example 1: Processing Section 5")
    print("=" * 60)
    
    result = process_law_section(SECTION_5, "§5")
    
    print(f"\nLaw: {result.law_name}")
    print(f"Section: {result.section}")
    print(f"Confidence: {result.confidence_score}")
    
    print("\n--- Business Rules ---")
    for rule in result.business_rules:
        print(f"\n{rule.rule_id}: {rule.rule_name}")
        print(f"  IF: {rule.condition}")
        print(f"  THEN: {rule.action}")
        if rule.exceptions:
            print(f"  EXCEPT: {', '.join(rule.exceptions)}")
    
    print("\n--- DMN Rules ---")
    for dmn in result.dmn_rules:
        print(f"\n{dmn.name} ({dmn.hit_policy})")
        print(f"  Inputs: {', '.join(dmn.input_variables)}")
        print(f"  Output: {dmn.output_variable}")


def example_manual_crew():
    """Manually configure and run crew"""
    print("\n" + "=" * 60)
    print("Example 2: Manual Crew Configuration")
    print("=" * 60)
    
    crew = create_rule_extraction_crew(SECTION_5, "§5")
    
    # Show agent configuration
    print("\nCrew Configuration:")
    for agent in crew.agents:
        print(f"  - {agent.role}: {agent.goal[:50]}...")
    
    print("\nTask Flow:")
    for i, task in enumerate(crew.tasks, 1):
        print(f"  {i}. {task.agent.role}: {task.description[:50]}...")


def example_full_law():
    """Process full law (abbreviated example)"""
    print("\n" + "=" * 60)
    print("Example 3: Full Law Processing (abbreviated)")
    print("=" * 60)
    
    # Abbreviated Liikennevakuutuslaki
    law_text = """
1 § Lain tarkoitus
Tämän lain tarkoituksena on vahingonkärsijän turvaaminen.

2 § Soveltamisala
Tätä lakia sovelletaan Suomessa rekisteröityihin ajoneuvoihin.

5 § Vakuutettava ajoneuvo
Ajoneuvosta... on otettava liikennevakuutus.

31 § Korvaus ilman huolimattomuuden arviointia
Liikennevakuutuksesta korvataan henkilövahingot.
"""
    
    result = process_full_law(
        law_text=law_text,
        law_name="Liikennevakuutuslaki",
        law_reference="460/2016"
    )
    
    print(f"\nProcessed: {result.law_name} ({result.law_reference})")
    print(f"Total Rules: {len(result.business_rules)}")
    print(f"DMN Tables: {len(result.dmn_rules)}")
    print(f"Gaps Found: {len(result.gaps_identified)}")


def example_expected_output():
    """Show expected output format"""
    print("\n" + "=" * 60)
    print("Example 4: Expected Output Format")
    print("=" * 60)
    
    rule = BusinessRule(
        rule_id="INS-001",
        rule_name="Vakuutusvelvollisuus",
        legal_basis="§5.1",
        source_text="Ajoneuvosta... on otettava liikennevakuutus",
        condition="Ajoneuvo on liikenteessä TAI rekisteröity Suomessa",
        action="Liikennevakuutus on otettava",
        exceptions=[
            "Ajoneuvo merkitty rekisteristä poistetuksi",
            "Käyttövoima vain ihmis-/eläinvoima",
            "Rakenteellinen nopeus ≤ 6 km/h",
            "Työkone, ei rekisteröintivelvollinen"
        ],
        priority=5,
        rule_type="obligation"
    )
    
    print("\nBusiness Rule:")
    print(json.dumps(rule.dict(), indent=2, ensure_ascii=False))
    
    dmn = DMNRule(
        name="InsuranceObligation",
        description="Determines if vehicle requires insurance",
        hit_policy="FIRST",
        input_variables=["vehicle.in_traffic", "vehicle.registered"],
        output_variable="insurance_required",
        legal_source="§5",
        rules=[
            {
                "inputs": ["true", "-"],
                "output": "Mandatory",
                "legal_basis": "§5.1"
            },
            {
                "inputs": ["-", "true"],
                "output": "Mandatory",
                "legal_basis": "§5.1"
            },
            {
                "inputs": ["false", "false"],
                "output": "Not Required",
                "legal_basis": "§5"
            }
        ]
    )
    
    print("\nDMN Rule:")
    print(json.dumps(dmn.dict(), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    print("Law-to-Rules Swarm - Examples")
    print("=" * 60)
    
    # Run examples
    example_single_section()
    example_manual_crew()
    example_full_law()
    example_expected_output()
    
    print("\n" + "=" * 60)
    print("Examples completed!")
    print("=" * 60)
