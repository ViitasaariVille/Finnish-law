#!/usr/bin/env python3
"""
Main entry point for Law-to-Rules Swarm
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.direct_extract import main as direct_extract_main

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>")
        print("Commands:")
        print("  extract     - Extract business rules from law")
        print("  analyze     - Run full law analysis")
        print("  test-keys   - Test API keys")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == 'extract':
        direct_extract_main()
    elif command == 'analyze':
        from src.run_analysis import run_law_analysis
        run_law_analysis()
    elif command == 'test-keys':
        from tests.test_keys import main as test_main
        test_main()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
