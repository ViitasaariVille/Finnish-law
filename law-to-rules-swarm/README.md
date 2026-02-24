# Law-to-Rules Swarm

A CrewAI-based multi-agent system for converting Finnish legal text into structured business rules (DMN format).

**Multi-Model Support**: Use **Kimi K2 + MiniMax M2.5** (recommended) or add Claude for ensemble validation.

## Project Structure

```
law-to-rules-swarm/
├── src/                      # Source code
│   ├── swarm.py             # Core swarm implementation
│   ├── direct_extract.py    # Direct LLM extraction
│   ├── extract_rules.py     # CrewAI-based extraction
│   ├── run_analysis.py      # Full law analysis
│   ├── routers/             # Model routing
│   │   ├── kimi_minimax_router.py
│   │   └── multi_model_router.py
│   └── tools/               # Utilities
│       └── parse_finlex_xml.py
├── tests/                   # Tests
│   ├── test_swarm.py
│   └── test_keys.py
├── examples/                # Usage examples
│   ├── examples.py
│   └── examples_kimi_minimax.py
├── output/                  # Generated outputs
├── docs/                    # Documentation
├── main.py                  # Entry point
├── requirements.txt
└── .env                     # API keys
```

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Copy and edit config
cp .env.example .env
# Edit .env and add your API keys

# 3. Test API keys
python main.py test-keys

# 4. Extract business rules
python main.py extract

# 5. Run full analysis
python main.py analyze
```

## Architecture

The swarm consists of 6 specialized agents:

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
| **Law Reader** | Kimi K2 | Long context, Finnish language |
| **Legal Analyst** | Kimi K2 | Legal reasoning |
| **Rule Extractor** | MiniMax M2.5 | Fast, cost-efficient |
| **Validator** | Kimi K2 | High accuracy |
| **DMN Formatter** | MiniMax M2.5 | Structured output |
| **Gap Analyzer** | Kimi K2 | Full law comparison |

## Usage

### Import from src

```python
from src.swarm import process_law_section, fetch_finlex_law

# Fetch law from Finlex
law_text = fetch_finlex_law("460/2016", "§5")

# Extract rules
result = process_law_section(law_text, "§5")
print(result.business_rules)
```

### Direct LLM Extraction

```python
from src.direct_extract import extract_rules_from_section

rules = extract_rules_from_section(section_text, "§8", "Liikennevakuutuslaki")
```

## Configuration

```bash
# .env file
MOONSHOT_API_KEY=your_moonshot_key
MINIMAX_API_KEY=your_minimax_key
```

## API Keys

| Model | Provider | URL |
|-------|----------|-----|
| Kimi K2 | Moonshot AI | https://platform.moonshot.cn/ |
| MiniMax M2.5 | MiniMax | https://www.minimaxi.com/ |

## License

MIT
