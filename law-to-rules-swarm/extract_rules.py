#!/usr/bin/env python3
"""
Run REAL CrewAI swarm to extract DMN business rules from Liikennevakuutuslaki
"""

import os
import sys
import json
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from swarm import process_law_section

def fetch_section_from_finlex(law_reference: str, section: str):
    """Fetch law section directly from Finlex API"""
    number, year = law_reference.split("/")
    # Finlex API format: /year/number/ (e.g., /2016/460/)
    url = f"https://opendata.finlex.fi/finlex/avoindata/v1/akn/fi/act/statute-consolidated/{year}/{number}/fin@"
    
    headers = {
        'User-Agent': 'Law-to-Rules-Swarm/1.0',
        'Accept': 'application/xml'
    }
    
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()
    
    root = ET.fromstring(response.content)
    ns = {'akn': 'http://docs.oasis-open.org/legaldocml/ns/akn/3.0'}
    
    # Extract title
    lines = []
    preface = root.find('.//akn:preface', ns)
    if preface is not None:
        doc_num = preface.find('.//akn:docNumber', ns)
        doc_title = preface.find('.//akn:docTitle', ns)
        if doc_num is not None and doc_title is not None:
            lines.append(f"{doc_num.text} {doc_title.text}")
            lines.append("=" * 60)
            lines.append("")
    
    # Find the specific section - note: Finlex uses format "8 §" not just "8"
    section_num_clean = section.replace('§', '').strip()
    all_sections = root.findall('.//akn:section', ns)
    
    for sec in all_sections:
        num = sec.find('akn:num', ns)
        if num is not None:
            num_text = num.text.strip() if num.text else ""
            # Match either "8 §" or "8"
            if num_text == section or num_text.replace('§', '').strip() == section_num_clean:
                # Found the section, extract it
                heading = sec.find('akn:heading', ns)
                if heading is not None:
                    lines.append(f"{num_text} {heading.text}")
                else:
                    lines.append(f"{num_text}")
            
            # Process subsections
            for subsec in sec.findall('akn:subsection', ns):
                content = subsec.find('akn:content', ns)
                if content is not None:
                    text = _extract_text(content, ns)
                    if text:
                        lines.append(text)
                
                for para in subsec.findall('akn:paragraph', ns):
                    num_para = para.find('akn:num', ns)
                    content_para = para.find('akn:content', ns)
                    if content_para is not None:
                        text = _extract_text(content_para, ns)
                        if text:
                            if num_para is not None:
                                lines.append(f"{num_para.text} {text}")
                            else:
                                lines.append(text)
            
            return '\n'.join(lines)
    
    return f"Section {section} not found"

def _extract_text(element, ns):
    """Extract all text from element"""
    text_parts = []
    def _collect(elem):
        if elem.text and elem.text.strip():
            text_parts.append(elem.text.strip())
        for child in elem:
            _collect(child)
            if child.tail and child.tail.strip():
                text_parts.append(child.tail.strip())
    _collect(element)
    return ' '.join(text_parts)

def extract_business_rules():
    """Extract actual DMN business rules using CrewAI swarm"""
    
    print("=" * 70)
    print("🤖 CrewAI Swarm - Business Rule Extraction")
    print("Target: Liikennevakuutuslaki (460/2016)")
    print("=" * 70)
    
    # Process just 1 section for demo (to save API costs)
    sections = [
        ("8 §", "Poikkeukset vakuuttamisvelvollisuudesta"),
    ]
    
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')
    os.makedirs(output_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    all_results = []
    
    for section_num, section_name in sections:
        print(f"\n{'='*70}")
        print(f"📋 Processing {section_num}: {section_name}")
        print(f"{'='*70}")
        
        try:
            # Fetch from Finlex API
            print(f"   🔍 Fetching from Finlex...")
            law_text = fetch_section_from_finlex('460/2016', section_num)
            
            if law_text.startswith('Section') or law_text.startswith('Error'):
                print(f"   ❌ Failed to fetch: {law_text}")
                continue
            
            print(f"   📄 Section text: {len(law_text)} chars")
            print(f"   📝 Preview:\n{law_text[:300]}...")
            
            # Run CrewAI swarm
            print(f"\n   🤖 Running CrewAI swarm (this may take 1-2 minutes)...")
            result = process_law_section(
                law_text=law_text,
                section_number=section_num
            )
            
            # Convert to dict for JSON serialization
            result_dict = {
                'section': section_num,
                'name': section_name,
                'law_name': result.law_name,
                'law_reference': result.law_reference,
                'confidence_score': result.confidence_score,
                'gaps_identified': result.gaps_identified,
                'business_rules': [
                    {
                        'rule_id': r.rule_id,
                        'rule_name': r.rule_name,
                        'legal_basis': r.legal_basis,
                        'condition': r.condition,
                        'action': r.action,
                        'exceptions': r.exceptions,
                        'priority': r.priority,
                        'rule_type': r.rule_type
                    }
                    for r in result.business_rules
                ],
                'dmn_rules': [
                    {
                        'name': d.name,
                        'description': d.description,
                        'hit_policy': d.hit_policy,
                        'input_variables': d.input_variables,
                        'output_variable': d.output_variable,
                        'legal_source': d.legal_source,
                        'rules': d.rules
                    }
                    for d in result.dmn_rules
                ]
            }
            
            all_results.append(result_dict)
            
            print(f"   ✅ Extracted {len(result.business_rules)} business rules")
            for rule in result.business_rules:
                print(f"      - {rule.rule_id}: {rule.rule_name}")
            print(f"   ✅ Generated {len(result.dmn_rules)} DMN rule tables")
            
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
            import traceback
            traceback.print_exc()
            all_results.append({
                'section': section_num,
                'name': section_name,
                'error': str(e)
            })
    
    # Save results
    output_file = os.path.join(output_dir, f'liikennevakuutuslaki_business_rules_{timestamp}.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'law_name': 'Liikennevakuutuslaki',
            'law_reference': '460/2016',
            'timestamp': timestamp,
            'total_sections': len(sections),
            'sections_processed': len([r for r in all_results if 'error' not in r]),
            'results': all_results
        }, f, indent=2, ensure_ascii=False)
    
    # Generate DMN markdown
    md_file = os.path.join(output_dir, f'liikennevakuutuslaki_business_rules_{timestamp}.md')
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(f"# DMN Business Rules: Liikennevakuutuslaki (460/2016)\n\n")
        f.write(f"**Generated:** {timestamp}\n\n")
        f.write(f"**Sections Processed:** {len([r for r in all_results if 'error' not in r])}/{len(sections)}\n\n")
        f.write("---\n\n")
        
        for result in all_results:
            if 'error' in result:
                f.write(f"## ERROR: {result['section']}\n\n")
                f.write(f"Error: {result['error']}\n\n")
                continue
            
            f.write(f"## {result['section']}: {result['name']}\n\n")
            f.write(f"**Confidence Score:** {result['confidence_score']}/10\n\n")
            
            if result['gaps_identified']:
                f.write(f"**⚠️ Gaps Identified:**\n")
                for gap in result['gaps_identified']:
                    f.write(f"- {gap}\n")
                f.write("\n")
            
            f.write(f"### Business Rules ({len(result['business_rules'])})\n\n")
            for rule in result['business_rules']:
                f.write(f"#### {rule['rule_id']}: {rule['rule_name']}\n\n")
                f.write(f"- **Legal Basis:** {rule['legal_basis']}\n")
                f.write(f"- **Type:** {rule['rule_type']}\n")
                f.write(f"- **Priority:** {rule['priority']}/10\n")
                f.write(f"- **Condition (IF):** {rule['condition']}\n")
                f.write(f"- **Action (THEN):** {rule['action']}\n")
                if rule['exceptions']:
                    f.write(f"- **Exceptions:** {', '.join(rule['exceptions'])}\n")
                f.write("\n")
            
            f.write(f"### DMN Decision Tables ({len(result['dmn_rules'])})\n\n")
            for dmn in result['dmn_rules']:
                f.write(f"#### {dmn['name']}\n\n")
                f.write(f"{dmn['description']}\n\n")
                f.write(f"- **Hit Policy:** {dmn['hit_policy']}\n")
                f.write(f"- **Inputs:** {', '.join(dmn['input_variables'])}\n")
                f.write(f"- **Output:** {dmn['output_variable']}\n")
                f.write(f"- **Legal Source:** {dmn['legal_source']}\n\n")
                
                if dmn['rules']:
                    f.write("| Rule | Inputs | Output |\n")
                    f.write("|------|--------|--------|\n")
                    for i, rule in enumerate(dmn['rules']):
                        inputs = rule.get('inputs', [])
                        output = rule.get('output', '')
                        f.write(f"| {i+1} | {inputs} | {output} |\n")
                    f.write("\n")
            
            f.write("---\n\n")
    
    print(f"\n{'='*70}")
    print(f"✅ Business rule extraction complete!")
    print(f"📁 JSON: {output_file}")
    print(f"📄 DMN Markdown: {md_file}")
    print(f"📊 Sections processed: {len([r for r in all_results if 'error' not in r])}/{len(sections)}")
    print(f"{'='*70}")
    
    return output_file, md_file

if __name__ == '__main__':
    extract_business_rules()
