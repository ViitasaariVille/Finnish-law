#!/usr/bin/env python3
"""Test API keys and show full diagnostics"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

print("=" * 60)
print("API Key Diagnostics")
print("=" * 60)

# Moonshot
MOONSHOT_API_KEY = os.environ.get('MOONSHOT_API_KEY', '')
print(f"\n🌙 Moonshot API Key:")
print(f"   Length: {len(MOONSHOT_API_KEY)}")
print(f"   Starts with: {MOONSHOT_API_KEY[:25]}...")
print(f"   Ends with: ...{MOONSHOT_API_KEY[-20:]}")

url = 'https://api.moonshot.cn/v1/chat/completions'
headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {MOONSHOT_API_KEY}'}
data = {'model': 'kimi-k2.5', 'messages': [{'role': 'user', 'content': 'Hi'}], 'max_tokens': 50}

response = requests.post(url, headers=headers, json=data, timeout=30)
print(f"\n   Response Status: {response.status_code}")
print(f"   Response Body: {response.text}")

# MiniMax
print("\n" + "=" * 60)
MINIMAX_API_KEY = os.environ.get('MINIMAX_API_KEY', '')
print(f"\n⚡ MiniMax API Key:")
print(f"   Length: {len(MINIMAX_API_KEY)}")
print(f"   Starts with: {MINIMAX_API_KEY[:25]}...")
print(f"   Ends with: ...{MINIMAX_API_KEY[-20:]}")

url = 'https://api.minimax.chat/v1/text/chatcompletion_v2'
headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {MINIMAX_API_KEY}'}
data = {'model': 'MiniMax-Text-01', 'messages': [{'role': 'user', 'content': 'Hi'}]}

response = requests.post(url, headers=headers, json=data, timeout=30)
print(f"\n   Response Status: {response.status_code}")
print(f"   Response Body: {response.text}")

print("\n" + "=" * 60)
print("If keys are invalid, generate new ones at:")
print("  - Moonshot: https://platform.moonshot.cn/")
print("  - MiniMax: https://platform.minimax.chat/")
print("=" * 60)
