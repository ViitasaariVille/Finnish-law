"""
Streamlit app to visualize the Finnish Work Accident Insurance Ontology
as an interactive knowledge graph.
"""

import streamlit as st
import yaml
import networkx as nx
from pyvis.network import Network
import tempfile
import os

# Page config
st.set_page_config(page_title="Finnish Work Accident Ontology", layout="wide")

st.title("🇫🇮 Finnish Work Accident & Occupational Disease Insurance Ontology")
st.markdown("Interactive knowledge graph visualization of Työtapaturma-ammattitautilaki (459/2015)")

ONTOLOGY_PATH = os.path.join(os.path.dirname(__file__), "work_accident_ontology.yaml")

# Load ontology
@st.cache_data
def load_ontology():
    with open(ONTOLOGY_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

ontology = load_ontology()

# Sidebar controls
st.sidebar.header("Controls")

# Build graph
@st.cache_data
def build_graph(ontology):
    G = nx.DiGraph()
    
    # Add classes as nodes
    if "classes" in ontology:
        for class_name, class_data in ontology["classes"].items():
            category = class_data.get("category", "unknown")
            label = class_data.get("label", class_name)
            finnish = class_data.get("finnish", "")
            description = class_data.get("description", "")[:100]
            legal_basis = class_data.get("legal_basis", "")
            
            G.add_node(class_name, 
                      label=label,
                      finnish=finnish,
                      description=description,
                      legal_basis=legal_basis,
                      category=category,
                      node_type="class")
    
    # Add relationships as edges
    if "relationships" in ontology:
        for rel in ontology["relationships"]:
            source = rel.get("source")
            target = rel.get("target")
            rel_type = rel.get("type")
            legal_basis = rel.get("legal_basis", "")
            note = rel.get("note", "")
            
            if source and target:
                G.add_edge(source, target, 
                          relationship=rel_type,
                          legal_basis=legal_basis,
                          note=note)
    
    return G

G = build_graph(ontology)

# Category filter
if "classes" in ontology:
    categories = set()
    for class_data in ontology["classes"].values():
        if "category" in class_data:
            categories.add(class_data["category"])
    categories = sorted(categories)
    
    selected_categories = st.sidebar.multiselect(
        "Filter by category",
        categories,
        default=categories
    )
    
    # Filter graph by category
    if selected_categories:
        nodes_to_remove = [n for n, d in G.nodes(data=True) 
                          if d.get("node_type") == "class" and d.get("category") not in selected_categories]
        G_filtered = G.copy()
        G_filtered.remove_nodes_from(nodes_to_remove)
    else:
        G_filtered = G
else:
    G_filtered = G

# Graph stats
st.sidebar.markdown("### Graph Statistics")
st.sidebar.write(f"**Classes (nodes):** {len([n for n,d in G_filtered.nodes(data=True) if d.get('node_type')=='class'])}")
st.sidebar.write(f"**Relationships (edges):** {G_filtered.number_of_edges()}")

# Create PyVis network
def create_pyvis_network(G):
    net = Network(height="600px", width="100%", bgcolor="#222222", font_color="white", directed=True)
    net.force_atlas_2based()
    
    # Color map for categories
    color_map = {
        "person": "#ff6b6b",
        "organization": "#4ecdc4",
        "institution": "#45b7d1",
        "compensation": "#96ceb4",
        "decision": "#ffeaa7",
        "event": "#dfe6e9",
        "insurance_type": "#a29bfe",
        "party": "#fd79a8",
        "process": "#00b894",
        "document": "#fdcb6e",
    }
    
    for node, data in G.nodes(data=True):
        if data.get("node_type") == "class":
            category = data.get("category", "unknown")
            color = color_map.get(category, "#cccccc")
            title = f"{data.get('label', node)}\n({data.get('finnish', '')})\n\n{data.get('description', '')}\n\nLegal basis: {data.get('legal_basis', 'N/A')}"
            net.add_node(node, label=data.get("label", node), color=color, title=title, shape="box")
    
    for source, target, data in G.edges(data=True):
        label = data.get("relationship", "")
        title = f"{label}\n\nLegal basis: {data.get('legal_basis', 'N/A')}\n\nNote: {data.get('note', 'N/A')}"
        net.add_edge(source, target, label=label, title=title, arrows="to")
    
    return net

# Render graph
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("Knowledge Graph")
    
    # Generate HTML
    net = create_pyvis_network(G_filtered)
    
    # Save to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmp:
        net.save_graph(tmp.name)
        with open(tmp.name, "r", encoding="utf-8") as f:
            html_content = f.read()
        os.unlink(tmp.name)
    
    # Display in Streamlit
    st.components.v1.html(html_content, height=650)

with col2:
    st.subheader("Legend")
    st.markdown("""
    - 🔴 Person
    - 🟢 Organization  
    - 🔵 Institution
    - 🟡 Compensation
    - ⚪ Decision
    - 🟣 Insurance Type
    - 🩷 Party
    """)
    
    st.subheader("Node Info")
    selected_node = st.selectbox("Select a class", 
                                [n for n,d in G.nodes(data=True) if d.get("node_type")=="class"])
    
    if selected_node:
        data = G.nodes[selected_node]
        st.markdown(f"**{data.get('label', selected_node)}**")
        st.markdown(f"*{data.get('finnish', '')}*")
        st.write(f"**Category:** {data.get('category', 'N/A')}")
        st.write(f"**Legal basis:** {data.get('legal_basis', 'N/A')}")
        st.write(f"**Description:** {data.get('description', 'N/A')}")

# Show relationships table
st.subheader("All Relationships")
rels_data = []
for source, target, data in G_filtered.edges(data=True):
    source_label = G_filtered.nodes[source].get("label", source)
    target_label = G_filtered.nodes[target].get("label", target)
    rels_data.append({
        "Source": source_label,
        "Relationship": data.get("relationship", ""),
        "Target": target_label,
        "Legal Basis": data.get("legal_basis", "")
    })

if rels_data:
    st.dataframe(rels_data, use_container_width=True)
