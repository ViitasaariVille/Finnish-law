"""
Streamlit Visualization for Finnish Car Insurance Ontology (Liikennevakuutuslaki)
Interactive graph visualization with node selection, zoom, and details panel.
"""

import streamlit as st
import json
import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components
import tempfile
import os

# Page config
st.set_page_config(
    page_title="Liikennevakuutuslaki Ontology",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
    }
    .stApp {
        background-color: #0e1117;
    }
    .node-details {
        padding: 15px;
        background-color: #1a1a2e;
        border-radius: 10px;
        margin: 10px 0;
    }
    .title {
        font-size: 24px;
        font-weight: bold;
        color: #4ecdc4;
    }
    .subtitle {
        font-size: 16px;
        color: #a0a0a0;
    }
    .metric-card {
        background-color: #16213e;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #4ecdc4;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_ontology():
    """Load the ontology JSON file"""
    with open('liikennevakuutuslaki/car_insurance_ontology.json') as f:
        return json.load(f)

@st.cache_data
def build_graph(ontology):
    """Build NetworkX graph from ontology"""
    G = nx.DiGraph()
    ont = ontology['ontology']
    
    # Add class nodes
    for cls_name, cls_data in ont.get('entities', {}).items():
        G.add_node(cls_name, 
                   label=cls_name,
                   description=cls_data.get('description', ''),
                   finnish_name=cls_data.get('finnish_name', ''),
                   legal_basis=cls_data.get('legal_basis', ''))
    
    # Add subclass relationships
    for cls_name, cls_data in ont.get('entities', {}).items():
        subclasses = cls_data.get('subclasses', {})
        if isinstance(subclasses, dict):
            for subclass_name in subclasses.keys():
                G.add_edge(subclass_name, cls_name, relationship='rdfs:subClassOf')
        elif isinstance(subclasses, list):
            for subclass_name in subclasses:
                G.add_edge(subclass_name, cls_name, relationship='rdfs:subClassOf')
    
    # Add other relationships
    for rel in ont.get('relationships', []):
        G.add_edge(rel['from'], rel['to'], relationship=rel['type'])
    
    return G

def create_pyvis_network(G, selected_nodes=None, highlight_connected=True):
    """Create interactive pyvis network"""
    net = Network(
        height="600px",
        width="100%",
        bgcolor="#1a1a2e",
        font_color="white",
        directed=True
    )
    
    # Color scheme
    colors = {
        'Vehicle': '#e74c3c',
        'Insurance': '#3498db',
        'Person': '#2ecc71',
        'LegalEntity': '#9b59b6',
        'InsuranceEvent': '#f39c12',
        'Damage': '#e67e22',
        'Claim': '#1abc9c',
        'Compensation': '#ff6b6b'
    }
    
    # Add nodes
    for node in G.nodes():
        node_data = G.nodes[node]
        
        # Determine color
        color = '#95a5a6'
        for cat, col in colors.items():
            if cat in node:
                color = col
                break
        
        # Highlight selected nodes
        if selected_nodes and node in selected_nodes:
            color = '#ffffff'
            size = 35
        else:
            size = 25 if G.degree(node) > 2 else 15
        
        net.add_node(
            node,
            label=node_data.get('label', node),
            title=f"{node}\n{node_data.get('description', '')[:50]}...",
            color=color,
            size=size
        )
    
    # Add edges
    for source, target, edge_data in G.edges(data=True):
        if highlight_connected and selected_nodes:
            # Only show edges connected to selected nodes
            if source in selected_nodes or target in selected_nodes:
                net.add_edge(source, target, 
                           title=edge_data.get('relationship', ''),
                           color='#4ecdc4',
                           arrows='to')
        else:
            net.add_edge(source, target,
                       title=edge_data.get('relationship', ''),
                       color='#555555',
                       arrows='to')
    
    # Physics options for better layout
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
st.markdown('<p class="title">🚗 Liikennevakuutuslaki Ontology Visualizer</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Finnish Traffic Insurance Act (460/2016) - Interactive Knowledge Graph</p>', unsafe_allow_html=True)

# Load data
ontology = load_ontology()
G = build_graph(ontology)

# Sidebar
st.sidebar.title("📊 Statistics")

# Metrics
col1, col2, col3 = st.sidebar.columns(3)
col1.metric("Classes", len(G.nodes()))
col2.metric("Relationships", len(G.edges()))
col3.metric("Laws", "1")

# Category filter
st.sidebar.markdown("### 🎨 Categories")
categories = ['All', 'Vehicle', 'Insurance', 'Person', 'Damage', 'Claim', 'Compensation', 'Event']
selected_category = st.sidebar.selectbox("Filter by category", categories)

# Node selection
st.sidebar.markdown("### 🔍 Search")
all_nodes = sorted(G.nodes())
selected_nodes = st.sidebar.multiselect(
    "Select nodes to highlight",
    all_nodes,
    default=[]
)

# Show/hide edges
show_all_edges = st.sidebar.checkbox("Show all edges", value=False)
show_legend = st.sidebar.checkbox("Show legend", value=True)

# Build filtered graph
if selected_category != 'All':
    filtered_nodes = [n for n in G.nodes() if selected_category in n]
    H = G.subgraph(filtered_nodes).copy()
else:
    H = G

# Main content - Graph
st.markdown("### 📌 Interactive Graph")
st.info("💡 Click and drag to move nodes. Scroll to zoom. Use sidebar to select nodes.")

# Create network
net = create_pyvis_network(H, selected_nodes, highlight_connected=not show_all_edges)

# Save and display
with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as tmp:
    net.save_graph(tmp.name)
    tmp_path = tmp.name

# Read and display HTML
with open(tmp_path, 'r') as f:
    html_content = f.read()

# Display the graph
components.html(html_content, height=650)

# Cleanup
os.unlink(tmp_path)

# Legend
if show_legend:
    st.markdown("### 🎨 Legend")
    legend_cols = st.columns(4)
    legend_items = [
        ("Vehicle", "#e74c3c"),
        ("Insurance", "#3498db"),
        ("Person", "#2ecc71"),
        ("Damage", "#e67e22"),
        ("Claim", "#1abc9c"),
        ("Compensation", "#ff6b6b"),
        ("Event", "#f39c12"),
        ("Other", "#95a5a6")
    ]
    for i, (cat, color) in enumerate(legend_items):
        with legend_cols[i % 4]:
            st.markdown(
                f'<div style="display:flex;align-items:center;gap:8px;">'
                f'<div style="width:20px;height:20px;background:{color};border-radius:50%;"></div>'
                f'<span>{cat}</span></div>',
                unsafe_allow_html=True
            )

# Node details panel
if selected_nodes:
    st.markdown("### 📋 Selected Node Details")
    
    for node in selected_nodes[:5]:  # Limit to 5
        node_data = G.nodes[node]
        
        with st.expander(f"**{node}**", expanded=True):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Description**")
                st.write(node_data.get('description', 'N/A'))
                
                st.markdown("**Finnish Name**")
                st.write(node_data.get('finnish_name', 'N/A'))
            
            with col2:
                st.markdown("**Legal Basis**")
                st.write(node_data.get('legal_basis', 'N/A'))
                
                st.markdown("**Connections**")
                # Get connected nodes
                predecessors = list(G.predecessors(node))
                successors = list(G.successors(node))
                
                if predecessors:
                    st.write(f"⬆️ Parent classes: {', '.join(predecessors)}")
                if successors:
                    st.write(f"⬇️ Subclasses: {', '.join(successors)}")

# Relationship list
st.markdown("### 🔗 All Relationships")
rel_types = {}
for source, target, data in G.edges(data=True):
    rel = data.get('relationship', 'related')
    if rel not in rel_types:
        rel_types[rel] = []
    rel_types[rel].append(f"{source} → {target}")

for rel_type, connections in sorted(rel_types.items()):
    with st.expander(f"{rel_type} ({len(connections)})"):
        for conn in connections[:20]:
            st.write(conn)
        if len(connections) > 20:
            st.write(f"... and {len(connections) - 20} more")

# Footer
st.markdown("---")
st.markdown(
    "<small style='color: #666;'>Built with Streamlit + PyVis | Data: Liikennevakuutuslaki 460/2016</small>",
    unsafe_allow_html=True
)
