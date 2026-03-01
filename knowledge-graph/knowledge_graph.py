"""
Streamlit app to visualize Finnish Law as an integrated knowledge graph.
Combines ontology (entities/classes) with business rules (decisions).
Entities in rules are matched to ontology classes via name matching.
"""

import streamlit as st
import yaml
import os
import networkx as nx
from pyvis.network import Network
import tempfile
import re

# Page config
st.set_page_config(page_title="Finnish Law Knowledge Graph", layout="wide")

st.title("🇫🇮 Finnish Law Knowledge Graph")
st.markdown("Integrated visualization: Ontology entities + Decision rules")

# Configuration
st.sidebar.header("Configuration")

# Look for ontology and rules files
APP_DIR = os.path.dirname(__file__)

# Find ontology file
ontology_file = st.sidebar.text_input("Ontology YAML file", "work_accident_ontology.yaml")

# Find rules file
rules_file = st.sidebar.text_input("Rules YAML file", "work_accident_rules.yaml")

ontology_path = os.path.join(APP_DIR, ontology_file)
rules_path = os.path.join(APP_DIR, rules_file)

# Load data
@st.cache_data
def load_ontology(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

@st.cache_data
def load_rules(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

ontology = load_ontology(ontology_path)
rules = load_rules(rules_path)

if ontology is None:
    st.error(f"Ontology file not found: {ontology_path}")
    st.stop()

if rules is None:
    st.error(f"Rules file not found: {rules_path}")
    st.stop()

# Extract ontology entities
ontology_classes = ontology.get("classes", {})
ontology_relationships = ontology.get("relationships", [])

# Extract rules decisions
decisions = rules.get("decisions", [])

# Build integrated knowledge graph
@st.cache_data
def build_integrated_graph(ontology_classes, ontology_relationships, decisions):
    G = nx.DiGraph()
    
    # Color scheme
    colors = {
        "class": "#4ecdc4",      # teal for ontology classes
        "decision": "#ff6b6b",   # red for decisions
        "rule": "#ffeaa7",       # yellow for rules
        "input": "#a29bfe",      # purple for input variables
        "output": "#00b894",     # green for output variables
    }
    
    # 1. Add ontology classes as nodes
    entity_name_mapping = {}  # normalized name -> original
    
    for class_name, class_data in ontology_classes.items():
        label = class_data.get("label", class_name)
        finnish = class_data.get("finnish", "")
        category = class_data.get("category", "unknown")
        legal_basis = class_data.get("legal_basis", "")
        
        # Normalize for matching
        normalized = class_name.lower().replace("_", "")
        
        G.add_node(class_name,
                  label=label,
                  finnish=finnish,
                  category=category,
                  legal_basis=legal_basis,
                  node_type="class",
                  color=colors["class"],
                  shape="box")
        
        entity_name_mapping[normalized] = class_name
        entity_name_mapping[label.lower().replace(" ", "")] = class_name
        if finnish:
            entity_name_mapping[finnish.lower().replace(" ", "")] = class_name
    
    # 2. Add ontology relationships as edges
    for rel in ontology_relationships:
        source = rel.get("source")
        target = rel.get("target")
        rel_type = rel.get("type", "")
        legal_basis = rel.get("legal_basis", "")
        
        if source and target and G.has_node(source) and G.has_node(target):
            G.add_edge(source, target,
                      relationship=rel_type,
                      legal_basis=legal_basis,
                      edge_type="ontology",
                      color="#cccccc")
    
    # 3. Add decisions as nodes
    for decision in decisions:
        decision_id = decision.get("id", "unknown")
        label = decision.get("label", decision_id)
        finnish = decision.get("finnish", "")
        legal_basis = decision.get("legal_basis", "")
        
        G.add_node(decision_id,
                  label=label,
                  finnish=finnish,
                  legal_basis=legal_basis,
                  node_type="decision",
                  color=colors["decision"],
                  shape="ellipse")
        
        # Add rules as child nodes of decisions
        for rule in decision.get("rules", []):
            rule_id = rule.get("id", "")
            description = rule.get("description", "")[:50]
            
            G.add_node(f"{decision_id}_{rule_id}",
                      label=rule_id,
                      description=description,
                      node_type="rule",
                      color=colors["rule"],
                      shape="diamond")
            
            # Connect rule to decision
            G.add_edge(decision_id, f"{decision_id}_{rule_id}",
                      edge_type="contains",
                      color="#888888")
        
        # 4. Connect decisions to ontology entities based on variable names
        # Extract entity references from input/output IDs (e.g., "injuredParty.daysSinceInjury" -> injuredParty)
        for inp in decision.get("input", []):
            inp_id = inp.get("id", "")
            # Extract first part before dot
            entity_ref = inp_id.split(".")[0] if "." in inp_id else inp_id
            
            # Try to match to ontology class
            normalized = entity_ref.lower().replace("_", "")
            
            matched_class = None
            if entity_ref in ontology_classes:
                matched_class = entity_ref
            elif normalized in entity_name_mapping:
                matched_class = entity_name_mapping[normalized]
            else:
                # Partial match
                for ont_class in ontology_classes:
                    if ont_class.lower().replace("_", "") in normalized or normalized in ont_class.lower().replace("_", ""):
                        matched_class = ont_class
                        break
            
            if matched_class and matched_class != decision_id:
                G.add_edge(matched_class, decision_id,
                          relationship="inputs_to",
                          edge_type="rule_to_entity",
                          color="#a29bfe")
        
        for out in decision.get("output", []):
            out_id = out.get("id", "")
            entity_ref = out_id.split(".")[0] if "." in out_id else out_id
            
            normalized = entity_ref.lower().replace("_", "")
            
            matched_class = None
            if entity_ref in ontology_classes:
                matched_class = entity_ref
            elif normalized in entity_name_mapping:
                matched_class = entity_name_mapping[normalized]
            else:
                for ont_class in ontology_classes:
                    if ont_class.lower().replace("_", "") in normalized or normalized in ont_class.lower().replace("_", ""):
                        matched_class = ont_class
                        break
            
            if matched_class and matched_class != decision_id:
                G.add_edge(decision_id, matched_class,
                          relationship="outputs_to",
                          edge_type="entity_to_rule",
                          color="#00b894")
    
    return G, entity_name_mapping

G, entity_mapping = build_integrated_graph(ontology_classes, ontology_relationships, decisions)

# Sidebar controls
st.sidebar.header("Graph Controls")

# Filter by node type
node_types = list(set(nx.get_node_attributes(G, 'node_type').values()))
selected_types = st.sidebar.multiselect("Show node types", node_types, default=node_types)

# Filter graph by selection
if selected_types:
    G_filtered = G.copy()
    nodes_to_remove = [n for n, d in G_filtered.nodes(data=True) 
                      if d.get('node_type') not in selected_types]
    G_filtered.remove_nodes_from(nodes_to_remove)
else:
    G_filtered = G

# Show/hide ontology edges
show_ontology_edges = st.sidebar.checkbox("Show ontology relationships", value=True)
show_rule_edges = st.sidebar.checkbox("Show rule connections", value=True)

if not show_ontology_edges:
    edges_to_remove = [(u, v) for u, v, d in G_filtered.edges(data=True) if d.get('edge_type') == 'ontology']
    G_filtered.remove_edges_from(edges_to_remove)

if not show_rule_edges:
    edges_to_remove = [(u, v) for u, v, d in G_filtered.edges(data=True) if d.get('edge_type') in ['rule_to_entity', 'entity_to_rule', 'contains']]
    G_filtered.remove_edges_from(edges_to_remove)

# Stats
st.sidebar.markdown("### Graph Statistics")
st.sidebar.write(f"**Total nodes:** {G_filtered.number_of_nodes()}")
st.sidebar.write(f"**Total edges:** {G_filtered.number_of_edges()}")

class_count = len([n for n, d in G.nodes(data=True) if d.get('node_type') == 'class'])
decision_count = len([n for n, d in G.nodes(data=True) if d.get('node_type') == 'decision'])
rule_count = len([n for n, d in G.nodes(data=True) if d.get('node_type') == 'rule'])

st.sidebar.write(f"**Ontology classes:** {class_count}")
st.sidebar.write(f"**Decisions:** {decision_count}")
st.sidebar.write(f"**Rules:** {rule_count}")

# Main visualization
st.header("🌐 Integrated Knowledge Graph")

# Create PyVis network
net = Network(height="600px", width="100%", bgcolor="#222222", font_color="white", directed=True)
net.force_atlas_2based()
net.options.edges.smooth.enabled = True
net.options.edges.smooth.type = "continuous"

# Add nodes
for node, data in G_filtered.nodes(data=True):
    node_type = data.get("node_type", "unknown")
    color = data.get("color", "#cccccc")
    
    if node_type == "class":
        title = f"**{data.get('label', node)}**\n({data.get('finnish', '')})\n\nCategory: {data.get('category', 'N/A')}\nLegal: {data.get('legal_basis', 'N/A')}"
        shape = "box"
        size = 20
    elif node_type == "decision":
        title = f"**{data.get('label', node)}**\n({data.get('finnish', '')})\n\nLegal: {data.get('legal_basis', 'N/A')}"
        shape = "ellipse"
        size = 25
    elif node_type == "rule":
        title = f"Rule: {data.get('label', node)}\n{data.get('description', '')}"
        shape = "diamond"
        size = 15
    else:
        title = node
        shape = "circle"
        size = 15
    
    net.add_node(node, label=data.get("label", node)[:25], color=color, title=title, shape=shape, size=size)

# Add edges
for source, target, data in G_filtered.edges(data=True):
    edge_type = data.get("edge_type", "unknown")
    color = data.get("color", "#888888")
    
    if edge_type == "ontology":
        label = data.get("relationship", "")[:20]
    elif edge_type == "rule_to_entity":
        label = "in"
    elif edge_type == "entity_to_rule":
        label = "out"
    elif edge_type == "contains":
        label = "⊂"
    else:
        label = ""
    
    net.add_edge(source, target, label=label, arrows="to", color=color, font={"color": "#aaaaaa"})

# Render
with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmp:
    net.save_graph(tmp.name)
    with open(tmp.name, "r", encoding="utf-8") as f:
        html_content = f.read()
    os.unlink(tmp.name)

st.components.v1.html(html_content, height=650)

# Legend
st.markdown("### Legend")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("🔷 **Ontology Classes** - Entity classes from the ontology")
with col2:
    st.markdown("🔴 **Decisions** - Business decision points")
with col3:
    st.markdown("🔶 **Rules** - Individual decision rules")
with col4:
    st.markdown("⬜ **Edges** - Relationships and data flows")

# Entity-Decision mapping table
st.header("🔗 Entity-Decision Mappings")
st.markdown("Shows which ontology entities are connected to which decisions")

mappings = []
for decision in decisions:
    decision_id = decision.get("id", "")
    label = decision.get("label", "")
    
    # Get connected entities
    in_edges = [(u, v) for u, v, d in G.edges(data=True) if v == decision_id and d.get("edge_type") == "rule_to_entity"]
    out_edges = [(u, v) for u, v, d in G.edges(data=True) if u == decision_id and d.get("edge_type") == "entity_to_rule"]
    
    in_entities = sorted(set([u for u, v in in_edges]))
    out_entities = sorted(set([v for u, v in out_edges]))
    
    if in_entities or out_entities:
        mappings.append({
            "Decision": decision_id,
            "Label": label,
            "Input Entities": ", ".join(in_entities[:3]) + ("..." if len(in_entities) > 3 else ""),
            "Output Entities": ", ".join(out_entities[:3]) + ("..." if len(out_entities) > 3 else "")
        })

if mappings:
    st.dataframe(mappings, use_container_width=True)

# Decision details
st.header("📋 Decision Details")

decision_options = ["All Decisions"] + [f"{d.get('id', '')} - {d.get('label', '')}" for d in decisions]
selected = st.selectbox("Select Decision", decision_options)

if selected != "All Decisions":
    decision_id = selected.split(" - ")[0]
    decision = next((d for d in decisions if d.get("id") == decision_id), None)
    
    if decision:
        st.subheader(f"{decision.get('label', '')} ({decision.get('finnish', '')})")
        st.markdown(f"**Legal Basis:** {decision.get('legal_basis', 'N/A')}")
        
        # Show connected entities
        in_ents = [u for u, v, d in G.edges(data=True) if v == decision_id and d.get("edge_type") == "rule_to_entity"]
        out_ents = [v for u, v, d in G.edges(data=True) if u == decision_id and d.get("edge_type") == "entity_to_rule"]
        
        if in_ents:
            st.markdown("**Input from Ontology:**")
            for ent in in_ents[:5]:
                ent_label = G.nodes[ent].get("label", ent)
                st.markdown(f"- {ent_label}")
        
        if out_ents:
            st.markdown("**Output to Ontology:**")
            for ent in out_ents[:5]:
                ent_label = G.nodes[ent].get("label", ent)
                st.markdown(f"- {ent_label}")
        
        # Show rules
        rules_list = decision.get("rules", [])
        st.markdown(f"**Rules:** {len(rules_list)}")
        
        for rule in rules_list[:10]:
            with st.expander(f"{rule.get('id', '')}: {rule.get('description', '')}"):
                st.markdown(f"**Legal:** {rule.get('legal_basis', 'N/A')}")
                st.code(f"Condition: {rule.get('condition', {})}")
                st.code(f"Result: {rule.get('result', {})}")

# All ontology classes
st.header("📚 Ontology Classes")
classes_list = []
for class_name, class_data in ontology_classes.items():
    classes_list.append({
        "Class": class_name,
        "Label": class_data.get("label", ""),
        "Finnish": class_data.get("finnish", ""),
        "Category": class_data.get("category", ""),
        "Legal Basis": class_data.get("legal_basis", "")[:30]
    })

if classes_list:
    st.dataframe(classes_list, use_container_width=True, height=400)
