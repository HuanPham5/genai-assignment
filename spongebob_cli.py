#!/usr/bin/env python3
"""
Example: One-shot call to ai.sooners.us using gemma3:4b model.

Requires:
  pip install requests python-dotenv
"""

import os
import requests
from dotenv import load_dotenv

# Load API key and base URL from ~/.soonerai.env
load_dotenv(".soonerai.env")

API_KEY = os.getenv("SOONERAI_API_KEY")
BASE_URL = os.getenv("SOONERAI_BASE_URL", "https://ai.sooners.us").rstrip("/")
MODEL = os.getenv("SOONERAI_MODEL", "gemma3:4b")

if not API_KEY:
    raise RuntimeError("Missing SOONERAI_API_KEY in ~/.soonerai.env")

import os
import requests
from dotenv import load_dotenv

# Load API key etc.
load_dotenv(".soonerai.env")  # or load_dotenv(os.path.expanduser("~/.soonerai.env"))
API_KEY = os.getenv("SOONERAI_API_KEY")
BASE_URL = os.getenv("SOONERAI_BASE_URL")
MODEL = os.getenv("SOONERAI_MODEL")

# ---- Chat history ----
history = [
    {"role": "system", "content": "You are SpongeBob SquarePants. Speak cheerfully and use ocean humor."}
]

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ["exit", "quit"]:
        break

    # append user message
    history.append({"role": "user", "content": user_input})

    # build payload
    payload = {
        "model": MODEL,
        "messages": history,
        "temperature": 0.6,
    }

    # send POST request
    response = requests.post(
        f"{BASE_URL}/api/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=60,
    )

    if response.status_code == 200:
        data = response.json()
        reply = data["choices"][0]["message"]["content"]
        print("SpongeBob:", reply)

        # append assistant reply to history
        history.append({"role": "assistant", "content": reply})

        # truncate to last N turns to keep it short
        if len(history) > 20:
            # keep system + last 18 messages
            history = [history[0]] + history[-18:]

    else:
        print(f"Error {response.status_code}: {response.text}")
