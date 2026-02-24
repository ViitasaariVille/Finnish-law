#!/usr/bin/env python3
"""
Parse Finlex Akoma Ntoso XML files to plain text.
Usage: python parse_finlex_xml.py input.xml [output.txt]
"""

import sys
import xml.etree.ElementTree as ET
import re

def parse_akn_xml(xml_path):
    """Parse Akoma Ntoso XML and extract plain text."""
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    # Define namespaces
    ns = {
        'akn': 'http://docs.oasis-open.org/legaldocml/ns/akn/3.0',
        'finlex': 'http://data.finlex.fi/schema/finlex'
    }
    
    lines = []
    
    # Extract title from preface
    preface = root.find('.//akn:preface', ns)
    if preface is not None:
        doc_num = preface.find('.//akn:docNumber', ns)
        doc_title = preface.find('.//akn:docTitle', ns)
        if doc_num is not None and doc_title is not None:
            lines.append(f"{doc_num.text} {doc_title.text}")
            lines.append("=" * 60)
            lines.append("")
    
    # Process body content
    body = root.find('.//akn:body', ns)
    if body is not None:
        _process_element(body, lines, ns, 0)
    
    return '\n'.join(lines)

def _process_element(element, lines, ns, depth):
    """Recursively process XML elements."""
    
    # Handle different element types
    tag = element.tag.split('}')[-1] if '}' in element.tag else element.tag
    
    if tag == 'chapter':
        num = element.find('akn:num', ns)
        heading = element.find('akn:heading', ns)
        if num is not None:
            lines.append("")
            lines.append(f"{num.text}")
            if heading is not None:
                lines.append(f"{heading.text}")
            lines.append("-" * 40)
    
    elif tag == 'section':
        num = element.find('akn:num', ns)
        heading = element.find('akn:heading', ns)
        if num is not None:
            lines.append("")
            lines.append(f"{num.text}")
            if heading is not None:
                lines.append(f"{heading.text}")
    
    elif tag == 'subsection':
        # Process content
        content = element.find('akn:content', ns)
        if content is not None:
            text = _extract_text(content, ns)
            if text:
                lines.append(text)
        
        # Process paragraphs
        for para in element.findall('akn:paragraph', ns):
            num = para.find('akn:num', ns)
            content = para.find('akn:content', ns)
            if content is not None:
                text = _extract_text(content, ns)
                if text:
                    if num is not None:
                        lines.append(f"{num.text} {text}")
                    else:
                        lines.append(text)
    
    elif tag == 'paragraph':
        num = element.find('akn:num', ns)
        content = element.find('akn:content', ns)
        if content is not None:
            text = _extract_text(content, ns)
            if text:
                if num is not None:
                    lines.append(f"{num.text} {text}")
                else:
                    lines.append(text)
    
    elif tag == 'content':
        text = _extract_text(element, ns)
        if text:
            lines.append(text)
    
    # Recursively process children (except for subsection/paragraph which we handle above)
    if tag not in ('subsection', 'paragraph', 'content'):
        for child in element:
            _process_element(child, lines, ns, depth + 1)

def _extract_text(element, ns):
    """Extract all text content from an element."""
    text_parts = []
    
    def _collect_text(elem):
        if elem.text and elem.text.strip():
            text_parts.append(elem.text.strip())
        for child in elem:
            _collect_text(child)
            if child.tail and child.tail.strip():
                text_parts.append(child.tail.strip())
    
    _collect_text(element)
    return ' '.join(text_parts)

def main():
    if len(sys.argv) < 2:
        print("Usage: python parse_finlex_xml.py input.xml [output.txt]")
        sys.exit(1)
    
    xml_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    text = parse_akn_xml(xml_path)
    
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Written to {output_path}")
    else:
        print(text[:5000])  # Print first 5000 chars

if __name__ == '__main__':
    main()
