#!/usr/bin/env python3
"""
Direct LLM-based business rule extraction for Finnish laws.
Bypasses CrewAI complexity for reliability.
"""

import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Use Kimi API directly
MOONSHOT_API_KEY = os.environ.get("MOONSHOT_API_KEY", "")
MINIMAX_API_KEY = os.environ.get("MINIMAX_API_KEY", "")

def call_kimi(prompt: str, system_prompt: str = None) -> str:
    """Call MiniMax API directly (fallback)"""
    url = "https://api.minimax.chat/v1/text/chatcompletion_pro"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {MINIMAX_API_KEY}"
    }
    
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    
    data = {
        "model": "MiniMax-M2.5",
        "messages": messages,
        "temperature": 0.2
    }
    
    response = requests.post(url, headers=headers, json=data, timeout=120)
    response.raise_for_status()
    result = response.json()
    return result['choices'][0]['message']['content']

def extract_rules_from_section(section_text: str, section_num: str, law_name: str) -> dict:
    """Extract business rules from a law section using LLM"""
    
    system_prompt = """You are a Finnish legal expert specializing in insurance law. 
Extract business rules from Finnish law text. Output ONLY valid JSON.

For each rule identify:
- rule_id: Unique identifier (e.g., "LV-001")
- rule_name: Human-readable name
- legal_basis: Section reference (e.g., "§8")
- rule_type: "obligation", "prohibition", "permission", or "definition"
- condition: IF condition in Finnish legal context
- action: THEN action/consequence
- exceptions: List of exceptions if any

Output format:
{
  "rules": [
    {
      "rule_id": "LV-001",
      "rule_name": "Vakuuttamisvelvollisuuden poikkeus",
      "legal_basis": "§8.1",
      "rule_type": "prohibition",
      "condition": "Ajoneuvo on moottorityökone tai traktori...",
      "action": "Ei tarvitse vakuutusta",
      "exceptions": []
    }
  ],
  "dmn_table": {
    "inputs": ["ajoneuvo_tyyppi", "rekisterointi", "nopeus"],
    "output": "vakuutusvelvollisuus",
    "rules": [
      {"inputs": ["moottorityökone", "ei rekisteröity", "≤15 km/h"], "output": "ei velvollisuutta"},
      {"inputs": ["moottorityökone", "ei rekisteröity", ">15 km/h"], "output": "velvollinen"}
    ]
  }
}"""

    prompt = f"""Extract business rules from this Finnish law section:

{section_text}

Section {section_num}

Extract ALL rules from this section. Be thorough - list every obligation, prohibition, and permission.
Output ONLY JSON, no other text."""

    result = call_kimi(prompt, system_prompt)
    
    # Parse JSON from response
    try:
        # Find JSON in response
        start = result.find('{')
        end = result.rfind('}') + 1
        if start >= 0 and end > start:
            json_str = result[start:end]
            return json.loads(json_str)
    except json.JSONDecodeError:
        return {"error": "Failed to parse JSON", "raw": result}

def main():
    """Main extraction"""
    
    # Read section 8 from local file
    law_path = os.path.join(os.path.dirname(__file__), '..', 'laws', 'liikennevakuutuslaki.txt')
    
    with open(law_path, 'r', encoding='utf-8') as f:
        full_text = f.read()
    
    # Extract just section 8
    lines = full_text.split('\n')
    section_8 = []
    in_section = False
    
    for line in lines:
        if line.strip().startswith('8 §'):
            in_section = True
        if in_section:
            section_8.append(line)
            if line.strip() and line.strip()[0].isdigit() and '§' in line and not line.startswith('8 §'):
                break
    
    section_text = '\n'.join(section_8)
    print(f"Section 8 text ({len(section_text)} chars):")
    print(section_text[:500])
    print("\n" + "="*60 + "\n")
    
    print("Extracting business rules with Kimi K2.5...")
    result = extract_rules_from_section(section_text, "8 §", "Liikennevakuutuslaki")
    
    print("\nExtracted rules:")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    
    # Save output
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    output_file = os.path.join(output_dir, f'business_rules_8_{timestamp}.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'section': '8 §',
            'law': 'Liikennevakuutuslaki (460/2016)',
            'timestamp': timestamp,
            'result': result
        }, f, indent=2, ensure_ascii=False)
    
    print(f"\nSaved to: {output_file}")

if __name__ == '__main__':
    main()
