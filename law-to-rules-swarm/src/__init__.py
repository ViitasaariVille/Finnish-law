"""
Law-to-Rules Swarm - CrewAI Multi-Agent System
Converts Finnish legal text into structured business rules (DMN format)
"""

from .swarm import (
    fetch_finlex_law,
    process_law_section,
    create_rule_extraction_crew,
    BusinessRule,
    DMNRule,
    RulePackage,
)

__version__ = "1.0.0"
__all__ = [
    "fetch_finlex_law",
    "process_law_section",
    "create_rule_extraction_crew",
    "BusinessRule",
    "DMNRule",
    "RulePackage",
]
