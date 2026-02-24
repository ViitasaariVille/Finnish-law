# Law-to-Rules Swarm

A CrewAI-based multi-agent system for converting Finnish legal text into structured business rules (DMN format).

**Multi-Model Support**: Use **Kimi K2 + MiniMax M2.5** (recommended) or add Claude for ensemble validation.

## Quick Start - Kimi + MiniMax Only

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Copy and edit config
cp .env.example .env
# Edit .env and add your API keys:
# MOONSHOT_API_KEY=your_key
# MINIMAX_API_KEY=your_key

# 3. Run swarm
python -c "from kimiminimax_router import *; print('Ready!')"
```

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

## Model Assignment (Kimi + MiniMax)

| Agent | Model | Why |
|-------|-------|-----|
| **Law Reader** | Kimi K2 | Long context, Finnish language expertise |
| **Legal Analyst** | Kimi K2 | Legal reasoning, nuanced analysis |
| **Rule Extractor** | MiniMax M2.5 | Fast pattern matching, cost-efficient |
| **Validator** | Kimi K2 | High accuracy validation |
| **DMN Formatter** | MiniMax M2.5 | Structured output, fast formatting |
| **Gap Analyzer** | Kimi K2 | Long context for full law comparison |

## Why Kimi + MiniMax?

**✅ Cost Effective**: ~75% cheaper than using Claude
- Kimi K2: ~$2/1M tokens
- MiniMax M2.5: ~$1/1M tokens
- Claude: ~$8/1M tokens

**✅ Good Coverage**:
- Kimi handles complex legal reasoning and Finnish language
- MiniMax handles fast extraction and formatting

**✅ Simpler Setup**: Only 2 API keys needed

## Alternative: Add Claude

If you want maximum accuracy with ensemble validation:

```python
# Use multi-model router with all 3 models
from multi_model_router import ModelRouter

router = ModelRouter()  # Uses all 3 models
```

See [multi_model_router.py](multi_model_router.py) for 3-model configuration.

## Usage

### Kimi + MiniMax Only

```python
from kimiminimax_router import (
    ModelRouter,
    create_legal_analyst_agent_multi,
    create_rule_extractor_agent_multi
)

# Initialize router with only Kimi and MiniMax
router = ModelRouter(available_models=["kimi-k2", "minimax-m2.5"])

# Create agents
analyst, model_used = create_legal_analyst_agent_multi(router)
print(f"Legal Analyst using: {model_used}")  # kimik2

extractor, model_used = create_rule_extractor_agent_multi(router)
print(f"Rule Extractor using: {model_used}")  # minimaxm2.5
```

### Process a Law Section

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

## Configuration

### Option 1: Kimi + MiniMax Only (Recommended)

```bash
# .env file
MOONSHOT_API_KEY=your_moonshot_key
MINIMAX_API_KEY=your_minimax_key
SWARM_MODE=kimi-minimax
```

### Option 2: All 3 Models

```bash
# .env file
ANTHROPIC_API_KEY=your_anthropic_key
MOONSHOT_API_KEY=your_moonshot_key
MINIMAX_API_KEY=your_minimax_key
SWARM_MODE=multi
```

## API Keys

| Model | Provider | Get Key |
|-------|----------|---------|
| Kimi K2 | Moonshot AI | https://platform.moonshot.cn/ |
| MiniMax M2.5 | MiniMax | https://www.minimaxi.com/ |
| Claude (optional) | Anthropic | https://console.anthropic.com/ |

## Features

### Cost Optimization
```python
from kimiminimax_router import CostOptimizer, ModelRouter

router = ModelRouter(available_models=["kimi-k2", "minimax-m2.5"])
optimizer = CostOptimizer(router)

cost = optimizer.estimate_cost("kimi-k2", 4000, 2000)
print(f"Cost: ${cost:.4f}")  # ~$0.012 for 6K tokens
```

### Fallback Chain
If Kimi fails, automatically falls back to MiniMax.

### Ensemble Validation (with both models)
```python
from kimiminimax_router import EnsembleValidator

validator = EnsembleValidator(router)
result = validator.validate_rule(rule, section_text)
# Gets consensus from both Kimi and MiniMax
```

## Installation

```bash
pip install crewai pydantic langchain langchain-openai
```

## Testing

```bash
python -m pytest test_swarm.py
```

## Files

| File | Description |
|------|-------------|
| `swarm.py` | Core swarm implementation |
| `kimiminimax_router.py` | Kimi + MiniMax router (recommended) |
| `multi_model_router.py` | Multi-model router (Claude + Kimi + MiniMax) |
| `examples.py` | Usage examples |
| `test_swarm.py` | Unit tests |

## License

MIT
