#!/usr/bin/env python3
"""
Run CrewAI swarm on Liikennevakuutuslaki (460/2016)
Outputs results to the swarm folder
"""

import os
import sys
import json
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from swarm import create_rule_extraction_crew, process_law_section, fetch_finlex_law

def run_law_analysis():
    """Run swarm analysis on liikennevakuutuslaki"""
    
    print("=" * 60)
    print("Law-to-Rules Swarm Analysis")
    print("Target: Liikennevakuutuslaki (460/2016)")
    print("=" * 60)
    
    # Load the law text
    law_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                            'laws', 'liikennevakuutuslaki.txt')
    
    print(f"\n📖 Loading law from: {law_path}")
    with open(law_path, 'r', encoding='utf-8') as f:
        law_text = f.read()
    
    print(f"   Law text size: {len(law_text)} characters")
    print(f"   Estimated sections: ~99")
    
    # Create output directory
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')
    os.makedirs(output_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    print("\n🔧 Using direct law text processing (no LLM calls in this demo)")
    print("   To run with full CrewAI swarm, use process_law_section() with API keys configured")
    
    # Create a summary output showing the structure
    sections_data = []
    current_section = None
    current_lines = []
    
    for line in law_text.split('\n'):
        line_stripped = line.strip()
        # Check if this is a section header (e.g., "5 §" or "12 §")
        if line_stripped and '§' in line_stripped:
            parts = line_stripped.split('§')
            if len(parts) == 2 and parts[0].strip().isdigit():
                # Save previous section
                if current_section:
                    sections_data.append({
                        'section': current_section,
                        'text': '\n'.join(current_lines[:20])  # First 20 lines
                    })
                # Start new section
                current_section = line_stripped
                current_lines = [line]
            else:
                current_lines.append(line)
        elif current_section:
            current_lines.append(line)
    
    # Don't forget the last section
    if current_section:
        sections_data.append({
            'section': current_section,
            'text': '\n'.join(current_lines[:20])
        })
    
    # Generate analysis summary
    result = {
        'law_name': 'Liikennevakuutuslaki',
        'law_reference': '460/2016',
        'timestamp': timestamp,
        'total_sections_found': len(sections_data),
        'sections_preview': sections_data[:10],  # First 10 sections
        'note': 'Full CrewAI analysis requires running process_law_section() with configured API keys'
    }
    
    # Save results
    output_file = os.path.join(output_dir, f'liikennevakuutuslaki_analysis_{timestamp}.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'='*60}")
    print(f"✅ Analysis complete!")
    print(f"📁 Results saved to: {output_file}")
    print(f"📊 Total sections found: {len(sections_data)}")
    print(f"{'='*60}")
    
    # Also create a markdown report
    md_file = os.path.join(output_dir, f'liikennevakuutuslaki_analysis_{timestamp}.md')
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(f"# Liikennevakuutuslaki (460/2016) Analysis\n\n")
        f.write(f"**Timestamp:** {timestamp}\n\n")
        f.write(f"**Total Sections:** {len(sections_data)}\n\n")
        f.write(f"## Sections Overview\n\n")
        for sec in sections_data[:20]:
            f.write(f"### {sec['section']}\n")
            f.write(f"```\n{sec['text'][:500]}...\n```\n\n")
    
    print(f"📄 Markdown report: {md_file}")
    
    return output_file

if __name__ == '__main__':
    run_law_analysis()
