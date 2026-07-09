#!/usr/bin/env python3
"""
Boomer Text Simplifier - Simple CLI app to generate short replies to long texts.
"""

import sys
import re

def analyze_boomer_text(text):
    key_topics = []
    if re.search(r'healing|cramping|doctor|health|pain', text, re.I):
        key_topics.append("health")
    if re.search(r'funeral|passed away|died|service|death|loss', text, re.I):
        key_topics.append("loss")
    if re.search(r'walk|visit|trip|Revere|reunion|family|plans', text, re.I):
        key_topics.append("plans")
    return key_topics

def generate_reply(text, user_status="I'm doing fine"):
    topics = analyze_boomer_text(text)
    
    greeting = "Hi!"
    status = f"{user_status}."
    closing = "Hope everything goes well!"
    
    acknowledgments = []
    if "health" in topics:
        acknowledgments.append("Glad the walks are helping with healing.")
    if "loss" in topics:
        acknowledgments.append("Sorry to hear about the family losses.")
    if "plans" in topics:
        acknowledgments.append("Hope the service and reunion go well.")
    
    ack_str = " ".join(acknowledgments) if acknowledgments else "Thanks for the update."
    
    reply = f"{greeting} {status} {ack_str} {closing}"
    return reply.strip()

def main():
    print("=== Boomer Text Simplifier ===\n")
    
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        print("Usage: python boomer_reply_simplifier.py \"paste long text here\"")
        print("Or run without args for interactive mode.")
        return
    
    reply = generate_reply(text)
    print("=== Suggested Concise Reply ===\n")
    print(reply)
    print("\nCopy, paste, and customize!")

if __name__ == "__main__":
    main()
