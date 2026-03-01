# Finnish Law Knowledge Graph

Integrated knowledge graph visualization combining:
- **Ontology**: Entity classes and relationships from `work_accident_ontology.yaml`
- **Rules**: Business decision rules from `work_accident_rules.yaml`

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Copy the ontology and rules files to this folder:
   - `work_accident_ontology.yaml`
   - `work_accident_rules.yaml`

3. Run the app:
```bash
streamlit run knowledge_graph.py
```

## Features

### Integrated Knowledge Graph
- **Ontology classes** (teal boxes): Entity classes from the ontology
- **Decisions** (red ellipses): Business decision points
- **Rules** (yellow diamonds): Individual decision rules
- **Edges**: 
  - Gray: Ontology relationships
  - Purple: Entity → Decision (input)
  - Green: Decision → Entity (output)

### Entity-Decision Mapping
Shows which ontology entities feed into which decisions and vice versa.

### Filtering
- Filter by node type (class/decision/rule)
- Toggle ontology relationships
- Toggle rule connections

### Decision Browser
Explore individual decisions with their rules and connected entities.

## Files

```
knowledge-graph/
├── knowledge_graph.py    # Main Streamlit app
├── requirements.txt      # Dependencies
├── README.md            # This file
├── work_accident_ontology.yaml   # Copy from ../tyotapaturma_ammattitautilaki/ontology/
└── work_accident_rules.yaml      # Copy from ../tyotapaturma_ammattitautilaki/rules/
```
