"""
Streamlit app to visualize Finnish Law Business Rules as an interactive decision tree.
Supports any rules file in the format: tyotapaturma_ammattitautilaki/rules/work_accident_rules.yaml
"""

import streamlit as st
import yaml
import os

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
    
    # Decision tree visualization
    st.header("🌲 Decision Tree")
    
    if rules:
        # Build simple tree representation
        tree_data = []
        for rule in rules[:20]:  # Limit to first 20 for performance
            rule_id = rule.get("id", "")
            desc = rule.get("description", "")[:60]
            condition = rule.get("condition", {})
            result = rule.get("result", {})
            legal = rule.get("legal_basis", "")
            
            tree_data.append({
                "id": rule_id,
                "description": desc,
                "condition": str(condition)[:80],
                "result": str(result)[:80],
                "legal_basis": legal
            })
        
        st.dataframe(tree_data, use_container_width=True)
    
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
