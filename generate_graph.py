#!/usr/bin/env python3
"""Generate interactive knowledge graph from DMN rules."""

import json
from pyvis.network import Network
import os

def load_dmn_rules(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_graph(dmn_file, output_file):
    net = Network(height="800px", width="100%", bgcolor="#222222", font_color="white")
    net.barnes_hut()
    
    with open(dmn_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Add title
    law_name = os.path.basename(os.path.dirname(dmn_file)).replace('_', ' ').title()
    net.add_node("root", label=law_name, color="#ff6b6b", size=30, shape="star")
    
    decisions = data.get('decisions', [])
    
    for decision in decisions:
        decision_name = decision.get('name', 'Decision')
        legal_source = decision.get('legal_source', '')
        
        # Add decision node
        net.add_node(decision_name, label=decision_name, color="#4ecdc4", size=20)
        net.add_edge("root", decision_name)
        
        # Add rules as child nodes
        rules = decision.get('rules', [])
        for rule in rules:
            inputs = rule.get('inputs', [])
            output = rule.get('output', '')
            source_text = rule.get('source_text', '')
            
            if inputs and output:
                # Create rule label
                input_str = ", ".join([str(i) for i in inputs[:2]])  # First 2 inputs
                rule_label = f"{output}\n({input_str})"
                
                rule_id = f"{decision_name}_{output[:15]}"
                net.add_node(rule_id, label=rule_label, color="#95e1d3", size=12, shape="box")
                net.add_edge(decision_name, rule_id)
    
    net.save_graph(output_file)
    print(f"Graph saved to {output_file}")

if __name__ == "__main__":
    import sys
    
    # Generate for all laws
    base_dir = "/home/molt/.openclaw/workspace/Finnish-law"
    
    laws = [
        ("liikennevakuutuslaki/car_insurance_dmn_rules.json", "car_insurance_graph.html"),
        ("tyotapaturma_ammattitautilaki/work_accident_dmn_rules.json", "work_accident_graph.html"),
        ("potilasvakuutuslaki/patient_insurance_dmn_rules.json", "patient_insurance_graph.html"),
    ]
    
    for dmn_file, output in laws:
        full_path = os.path.join(base_dir, dmn_file)
        if os.path.exists(full_path):
            create_graph(full_path, output)
            print(f"Created: {output}")
