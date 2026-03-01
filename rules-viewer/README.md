# Finnish Law Business Rules Viewer

Interactive Streamlit app to visualize Finnish law business rules (DMN format).

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Copy your rules YAML file to this folder (e.g., `work_accident_rules.yaml`)

3. Run the app:
```bash
streamlit run rules_viewer.py
```

## Features

- **Decision Browser**: Navigate through all decisions in the rules file
- **Inputs/Outputs**: View each decision's input and output variables
- **Rules Table**: Search and filter decision rules
- **Decision Tree**: View rules in table format with conditions and results
- **Legal References**: Each rule includes legal basis citations

## Requirements

- streamlit
- pyyaml
