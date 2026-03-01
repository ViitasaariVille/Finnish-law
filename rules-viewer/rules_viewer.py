"""
Streamlit app to visualize Finnish Law Business Rules as an interactive knowledge graph.
Supports any rules file in the format: tyotapaturma_ammattitautilaki/rules/work_accident_rules.yaml
"""

import streamlit as st
import yaml
import os
import networkx as nx
from pyvis.network import Network
import tempfile

# Page config
st.set_page_config(page_title="Finnish Law Business Rules", layout="wide")

st.title("🇫🇮 Finnish Law Business Rules Viewer")
st.markdown("Interactive visualization of DMN-type decision rules")

# File selector
RULES_DIR = os.path.join(os.path.dirname(__file__))
yaml_files = [f for f in os.listdir(RULES_DIR) if f.endswith('.yaml') or f.endswith('.yml')]

if yaml_files:
    selected_file = st.selectbox("Select Rules File", yaml_files, index=0)
    
    # Load rules
    @st.cache_data
    def load_rules(filename):
        filepath = os.path.join(RULES_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    
    rules_data = load_rules(selected_file)
    
    # Show metadata
    if "metadata" in rules_data:
        st.sidebar.header("Metadata")
        meta = rules_data["metadata"]
        st.sidebar.markdown(f"**Name:** {meta.get('name', 'N/A')}")
        st.sidebar.markdown(f"**Law:** {meta.get('law', 'N/A')}")
        st.sidebar.markdown(f"**Version:** {meta.get('version', 'N/A')}")
    
    # Get all decisions
    decisions = rules_data.get("decisions", [])
    
    # Build knowledge graph
    @st.cache_data
    def build_rules_graph(decisions):
        G = nx.DiGraph()
        
        # Add decision nodes
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
                      color="#4ecdc4")
        
        # Analyze relationships between decisions based on input/output matching
        # Extract all input and output variable IDs
        decision_vars = {}
        for decision in decisions:
            decision_id = decision.get("id", "unknown")
            inputs = decision.get("input", [])
            outputs = decision.get("output", [])
            
            input_ids = set(inp.get("id", "").split(".")[0] for inp in inputs)
            output_ids = set(out.get("id", "") for out in outputs)
            
            decision_vars[decision_id] = {"inputs": input_ids, "outputs": output_ids}
        
        # Create edges based on variable connections
        for decision in decisions:
            decision_id = decision.get("id", "unknown")
            outputs = decision.get("output", [])
            
            output_ids = set(out.get("id", "") for out in outputs)
            
            # Check which other decisions use these outputs as inputs
            for other_id, other_vars in decision_vars.items():
                if other_id != decision_id:
                    # Check if this decision's outputs match other decision's inputs
                    matching_inputs = other_vars["inputs"] & output_ids
                    if matching_inputs:
                        G.add_edge(decision_id, other_id,
                                  relationship=f"feeds: {matching_inputs}",
                                  color="#cccccc")
        
        return G
    
    G = build_rules_graph(decisions)
    
    # Sidebar - view mode
    st.sidebar.header("View Mode")
    view_mode = st.sidebar.radio("Select View", ["📊 Knowledge Graph", "📋 Decision Details"])
    
    if view_mode == "📊 Knowledge Graph":
        st.header("🌐 Decision Knowledge Graph")
        
        # Stats
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Decisions", len(decisions))
        with col2:
            total_rules = sum(len(d.get("rules", [])) for d in decisions)
            st.metric("Total Rules", total_rules)
        with col3:
            st.metric("Relationships", G.number_of_edges())
        
        # Create PyVis network
        net = Network(height="600px", width="100%", bgcolor="#222222", font_color="white", directed=True)
        net.force_atlas_2based()
        
        # Decision colors
        decision_colors = {
            "D1": "#ff6b6b", "D2": "#4ecdc4", "D3": "#45b7d1",
            "D4": "#96ceb4", "D5": "#ffeaa7", "D6": "#dfe6e9",
            "D7": "#a29bfe", "D8": "#fd79a8", "D9": "#00b894",
            "D10": "#fdcb6e", "D11": "#e17055", "D12": "#74b9ff",
            "D13": "#81ecec", "D14": "#fab1a0"
        }
        
        for node, data in G.nodes(data=True):
            color = decision_colors.get(node[:2], "#cccccc")
            title = f"**{data.get('label', node)}**\n\n{data.get('finnish', '')}\n\nLegal basis: {data.get('legal_basis', 'N/A')}"
            net.add_node(node, label=data.get("label", node)[:20], color=color, title=title, shape="ellipse", size=25)
        
        for source, target, data in G.edges(data=True):
            title = data.get("relationship", "feeds into")
            net.add_edge(source, target, label="→", title=title, arrows="to", color="#888888")
        
        # Render graph
        with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmp:
            net.save_graph(tmp.name)
            with open(tmp.name, "r", encoding="utf-8") as f:
                html_content = f.read()
            os.unlink(tmp.name)
        
        st.components.v1.html(html_content, height=650)
        
        # Legend
        st.markdown("### Legend")
        st.markdown("""
        - 🔴 D1: Insurance Obligation
        - 🟢 D2: Personal Scope  
        - 🔵 D3: Event Classification
        - 🟢 D4: Daily Allowance Eligibility
        - 🟡 D5: Daily Allowance Amount
        - ⚪ D6: Accident Pension
        - 🟣 D7: Impairment Allowance
        - 🩷 D8: Care Allowance
        - 🟢 D9: Clothing Allowance
        - 🟡 D10: Survivors Pension
        - 🟠 D11: Claim Deadline
        - 🔵 D12: Decision Deadline
        - 🩵 D13: Appeal Deadline
        - 🧠 D14: Rehabilitation Allowance
        """)
        
        # Decision list with connections
        st.markdown("### Decision Flow")
        for decision in decisions:
            decision_id = decision.get("id", "")
            label = decision.get("label", "")
            rules_count = len(decision.get("rules", []))
            
            # Find outgoing edges
            successors = list(G.successors(decision_id))
            if successors:
                st.write(f"**{decision_id}** ({label}) → {', '.join(successors)}")
            else:
                st.write(f"**{decision_id}** ({label}) → (end)")
    
    else:
        # Decision Details View
        st.sidebar.header("Decisions")
        decision_names = [f"{d.get('id', 'N/A')} - {d.get('label', 'N/A')}" for d in decisions]
        selected_decision = st.sidebar.selectbox("Select Decision", decision_names)
        
        # Parse selected decision
        decision_idx = decision_names.index(selected_decision)
        decision = decisions[decision_idx]
        
        # Display decision details
        st.header(f"📋 {decision.get('label', 'N/A')}")
        st.markdown(f"**Finnish:** {decision.get('finnish', 'N/A')}")
        st.markdown(f"**Legal Basis:** {decision.get('legal_basis', 'N/A')}")
        
        # Tabs for inputs, outputs, rules
        tab1, tab2, tab3 = st.tabs(["📥 Inputs", "📤 Outputs", "📜 Rules"])
        
        with tab1:
            st.subheader("Input Variables")
            inputs = decision.get("input", [])
            if inputs:
                for inp in inputs:
                    with st.expander(f"{inp.get('id', 'N/A')}"):
                        st.markdown(f"**Label:** {inp.get('label', 'N/A')}")
                        st.markdown(f"**Type:** {inp.get('type', 'N/A')}")
                        if "values" in inp:
                            st.markdown(f"**Values:** {', '.join(str(v) for v in inp['values'])}")
                        if "note" in inp:
                            st.markdown(f"**Note:** {inp.get('note', '')}")
            else:
                st.info("No inputs defined")
        
        with tab2:
            st.subheader("Output Variables")
            outputs = decision.get("output", [])
            if outputs:
                for out in outputs:
                    with st.expander(f"{out.get('id', 'N/A')}"):
                        st.markdown(f"**Label:** {out.get('label', 'N/A')}")
                        st.markdown(f"**Type:** {out.get('type', 'N/A')}")
                        if "values" in out:
                            st.markdown(f"**Values:** {', '.join(str(v) for v in out['values'])}")
            else:
                st.info("No outputs defined")
        
        with tab3:
            st.subheader("Decision Rules")
            rules = decision.get("rules", [])
            if rules:
                # Search/filter
                search = st.text_input("Search rules", "")
                
                filtered_rules = rules
                if search:
                    filtered_rules = [r for r in rules if search.lower() in str(r).lower()]
                
                st.write(f"Showing {len(filtered_rules)} of {len(rules)} rules")
                
                for rule in filtered_rules:
                    with st.expander(f"📌 {rule.get('id', 'N/A')}: {rule.get('description', 'N/A')}"):
                        st.markdown(f"**Description:** {rule.get('description', 'N/A')}")
                        st.markdown(f"**Legal Basis:** {rule.get('legal_basis', 'N/A')}")
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown("**Condition:**")
                            condition = rule.get("condition", {})
                            if condition:
                                for k, v in condition.items():
                                    st.code(f"{k}: {v}")
                            else:
                                st.info("No condition (default rule)")
                        
                        with col2:
                            st.markdown("**Result:**")
                            result = rule.get("result", {})
                            if result:
                                for k, v in result.items():
                                    st.code(f"{k}: {v}")
                            else:
                                st.info("No result")
                        
                        if "note" in rule:
                            st.markdown(f"📝 **Note:** {rule.get('note', '')}")
            else:
                st.info("No rules defined")
        
        # Constants section
        if "constants" in decision:
            st.header("⚙️ Constants")
            constants = decision["constants"]
            st.json(constants)
    
    # Rules overview table
    st.header("📜 All Rules Overview")
    
    all_rules = []
    for decision in decisions:
        decision_id = decision.get("id", "")
        decision_label = decision.get("label", "")
        legal_basis = decision.get("legal_basis", "")
        
        for rule in decision.get("rules", []):
            all_rules.append({
                "Decision": decision_id,
                "Decision Label": decision_label,
                "Rule ID": rule.get("id", ""),
                "Description": rule.get("description", "")[:80],
                "Legal Basis": rule.get("legal_basis", "")
            })
    
    if all_rules:
        st.dataframe(all_rules, use_container_width=True, height=400)

else:
    st.warning("No YAML rules files found in the current directory.")
    st.markdown("""
    ## Setup
    
    1. Copy your rules YAML file to this folder
    2. Requirements:
    ```
    pip install -r requirements.txt
    streamlit run rules_viewer.py
    ```
    """)
