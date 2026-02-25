"""
Streamlit Visualization for Finnish Law Ontologies
Interactive graph visualization for all Finnish law ontologies.
Supports: liikennevakuutuslaki, tyotapaturma_ammattitautilaki, potilasvakuutuslaki, 
vakuutusten_tarjoaminen, vakuutussopimuslaki, tyottomysturvalaki
"""

import streamlit as st
import json
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components
import tempfile
import os
from pathlib import Path

# Page config
st.set_page_config(
    page_title="Finnish Law Ontology Visualizer",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .stApp { background-color: #0e1117; }
    .title { font-size: 24px; font-weight: bold; color: #4ecdc4; }
    .subtitle { font-size: 16px; color: #a0a0a0; }
    .law-selector { padding: 10px; background: #1a1a2e; border-radius: 8px; }
</style>
""", unsafe_allow_html=True)

# Available ontologies
ONTOLOGIES = {
    "liikennevakuutuslaki": {
        "name": "Liikennevakuutuslaki",
        "law_number": "460/2016",
        "english": "Traffic Insurance Act",
        "emoji": "🚗",
        "color": "#e74c3c"
    },
    "tyotapaturma_ammattitautilaki": {
        "name": "Työtapaturma- ja ammattitautilaki",
        "law_number": "459/2015", 
        "english": "Work Accidents and Occupational Diseases Act",
        "emoji": "🏥",
        "color": "#3498db"
    },
    "potilasvakuutuslaki": {
        "name": "Potilasvakuutuslaki",
        "law_number": "948/2019",
        "english": "Patient Insurance Act",
        "emoji": "⚕️",
        "color": "#2ecc71"
    },
    "vakuutusten_tarjoaminen": {
        "name": "Laki vakuutusten tarjoamisesta",
        "law_number": "234/2018",
        "english": "Insurance Distribution Act",
        "emoji": "📋",
        "color": "#9b59b6"
    },
    "vakuutussopimuslaki": {
        "name": "Vakuutussopimuslaki",
        "law_number": "543/1994",
        "english": "Insurance Contract Act",
        "emoji": "📝",
        "color": "#f39c12"
    },
    "tyottomysturvalaki": {
        "name": "Työttömyysturvalaki",
        "law_number": "1290/2002",
        "english": "Unemployment Protection Act",
        "emoji": "👷",
        "color": "#e67e22"
    }
}

def get_ontology_dir():
    """Get the directory containing the ontologies"""
    return Path(__file__).parent

@st.cache_data
def load_ontology(law_folder):
    """Load the ontology JSON file for a specific law"""
    script_dir = get_ontology_dir()
    ontology_path = script_dir / law_folder / f"{law_folder}_ontology.json"
    
    # Try alternative naming
    if not ontology_path.exists():
        ontology_path = script_dir / law_folder / "car_insurance_ontology.json"
    
    if not ontology_path.exists():
        return None
        
    with open(ontology_path) as f:
        return json.load(f)

@st.cache_data
def build_graph(ontology):
    """Build NetworkX graph from ontology"""
    G = nx.DiGraph()
    
    if not ontology:
        return G
    
    # Handle different ontology structures
    if 'ontology' in ontology:
        ont = ontology['ontology']
    elif '@graph' in ontology:
        # JSON-LD format
        return G
    else:
        ont = ontology
    
    # Add class nodes
    entities = ont.get('entities', {})
    for cls_name, cls_data in entities.items():
        if isinstance(cls_data, dict):
            G.add_node(cls_name, 
                       label=cls_name,
                       description=cls_data.get('description', ''),
                       finnish_name=cls_data.get('finnish_name', ''),
                       legal_basis=cls_data.get('legal_basis', ''))
        elif isinstance(cls_data, str):
            G.add_node(cls_name, label=cls_name, description=cls_data)
    
    # Add subclass relationships
    for cls_name, cls_data in entities.items():
        if not isinstance(cls_data, dict):
            continue
        subclasses = cls_data.get('subclasses', {})
        if isinstance(subclasses, dict):
            for subclass_name in subclasses.keys():
                G.add_edge(subclass_name, cls_name, relationship='rdfs:subClassOf')
        elif isinstance(subclasses, list):
            for subclass_name in subclasses:
                G.add_edge(subclass_name, cls_name, relationship='rdfs:subClassOf')
    
    # Add other relationships (handle different formats)
    for rel in ont.get('relationships', []):
        if isinstance(rel, dict):
            # Try different formats: from/to or subject/predicate/object
            source = rel.get('from') or rel.get('subject')
            target = rel.get('to') or rel.get('object')
            rel_type = rel.get('type') or rel.get('predicate')
            if source and target:
                G.add_edge(source, target, relationship=rel_type or 'related')
    
    return G

def create_pyvis_network(G, selected_nodes=None, highlight_connected=True, law_color="#3498db"):
    """Create interactive pyvis network"""
    net = Network(
        height="600px",
        width="100%",
        bgcolor="#1a1a2e",
        font_color="white",
        directed=True
    )
    
    # Add nodes
    for node in G.nodes():
        node_data = G.nodes[node]
        color = law_color if selected_nodes and node in selected_nodes else '#95a5a6'
        size = 35 if selected_nodes and node in selected_nodes else (25 if G.degree(node) > 2 else 15)
        
        net.add_node(
            node,
            label=node_data.get('label', node),
            title=f"{node}\n{node_data.get('description', '')[:100]}...",
            color=color,
            size=size
        )
    
    # Add edges
    for source, target, edge_data in G.edges(data=True):
        if highlight_connected and selected_nodes:
            if source in selected_nodes or target in selected_nodes:
                net.add_edge(source, target, 
                           title=edge_data.get('relationship', ''),
                           color=law_color,
                           arrows='to')
        else:
            net.add_edge(source, target,
                       title=edge_data.get('relationship', ''),
                       color='#555555',
                       arrows='to')
    
    # Physics options
    net.set_options("""
    {
        "nodes": {
            "font": {"size": 14, "face": "arial", "color": "white"},
            "borderWidth": 2,
            "borderWidthSelected": 4
        },
        "edges": {
            "color": {"inherit": true},
            "smooth": {"type": "continuous"},
            "width": 2
        },
        "physics": {
            "forceAtlas2Based": {
                "gravitationalConstant": -80,
                "centralGravity": 0.015,
                "springLength": 120,
                "springConstant": 0.05
            },
            "minVelocity": 0.7,
            "solver": "forceAtlas2Based",
            "stabilization": {"iterations": 150}
        },
        "interaction": {
            "hover": true,
            "tooltipDelay": 100,
            "zoomView": true,
            "dragNodes": true,
            "dragView": true,
            "selectConnectedEdges": true,
            "multiselect": true
        }
    }
    """)
    
    return net

# Main app
st.markdown('<p class="title">⚖️ Finnish Law Ontology Visualizer</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Interactive Knowledge Graph for Finnish Legislation</p>', unsafe_allow_html=True)

# Sidebar - Law selection
st.sidebar.title("📚 Select Law")

selected_law = st.sidebar.selectbox(
    "Choose a law to visualize:",
    options=list(ONTOLOGIES.keys()),
    format_func=lambda x: f"{ONTOLOGIES[x]['emoji']} {ONTOLOGIES[x]['name']}"
)

law_info = ONTOLOGIES[selected_law]

# Load ontology
ontology = load_ontology(selected_law)
G = build_graph(ontology)

# Metrics
st.sidebar.markdown("### 📊 Statistics")
col1, col2 = st.sidebar.columns(2)
col1.metric("Classes", len(G.nodes()))
col2.metric("Relationships", len(G.edges()))

st.sidebar.markdown(f"**{law_info['name']}**")
st.sidebar.markdown(f"Law: {law_info['law_number']}")
st.sidebar.markdown(f"English: {law_info['english']}")

# Node selection
st.sidebar.markdown("### 🔍 Search Nodes")
all_nodes = sorted(G.nodes())
selected_nodes = st.sidebar.multiselect(
    "Select nodes to highlight",
    all_nodes,
    default=[]
)

# Show options
show_all_edges = st.sidebar.checkbox("Show all edges", value=False)

if ontology:
    # Main content - Graph
    st.markdown(f"### 📌 {law_info['emoji']} Interactive Graph")
    st.info("💡 Click and drag to move nodes. Scroll to zoom. Select nodes in sidebar.")
    
    # Create network
    net = create_pyvis_network(G, selected_nodes, not show_all_edges, law_info['color'])
    
    # Save and display
    with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as tmp:
        net.save_graph(tmp.name)
        tmp_path = tmp.name
    
    with open(tmp_path, 'r') as f:
        html_content = f.read()
    
    components.html(html_content, height=650)
    os.unlink(tmp_path)
    
    # Node details
    if selected_nodes:
        st.markdown("### 📋 Selected Node Details")
        
        for node in selected_nodes[:5]:
            node_data = G.nodes[node]
            with st.expander(f"**{node}**"):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**Description**")
                    st.write(node_data.get('description', 'N/A'))
                with col2:
                    st.markdown("**Legal Basis**")
                    st.write(node_data.get('legal_basis', 'N/A'))
    
    # Relationships
    if len(G.edges()) > 0:
        st.markdown("### 🔗 Relationships")
        rel_types = {}
        for source, target, data in G.edges(data=True):
            rel = data.get('relationship', 'related')
            if rel not in rel_types:
                rel_types[rel] = []
            rel_types[rel].append(f"{source} → {target}")
        
        for rel_type, connections in sorted(rel_types.items())[:5]:
            with st.expander(f"{rel_type} ({len(connections)})"):
                for conn in connections[:15]:
                    st.write(conn)
else:
    st.error(f"Could not load ontology for {law_info['name']}")
    st.write("Looking for file in:", get_ontology_dir() / selected_law)

# Footer
st.markdown("---")
st.markdown(
    "<small style='color: #666;'>Built with Streamlit + PyVis | Data: Finnish Law Ontologies</small>",
    unsafe_allow_html=True
)
