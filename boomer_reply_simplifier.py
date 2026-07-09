#!/usr/bin/env python3
"""
Boomer Text Simplifier v2
CLI tool that turns long, detailed Boomer texts into short, warm, natural replies.
"""

import sys
import re
from typing import List, Dict

def analyze_boomer_text(text: str) -> Dict[str, bool]:
    """Detect key topics in the Boomer message."""
    text_lower = text.lower()
    topics = {
        "health": bool(re.search(r'healing|cramp|pain|doctor|health|sick|hurt|recovery', text_lower)),
        "loss": bool(re.search(r'funeral|passed away|died|death|loss|service|condolences', text_lower)),
        "plans": bool(re.search(r'walk|visit|trip|revere|reunion|plans|going to|family', text_lower)),
        "greeting": bool(re.search(r'hi|hello|hey', text_lower)),
        "question_back": bool(re.search(r'how are you|how.*doing', text_lower)),
    }
    return topics

def generate_replies(text: str, user_status: str = "I'm doing fine", user_name: str = "", num_variations: int = 3) -> List[str]:
    """Generate 1-3 natural reply variations."""
    topics = analyze_boomer_text(text)
    replies = []
    
    base_greeting = "Hi!" if topics["greeting"] else "Hey there!"
    status_part = f"{user_status}."
    if user_name:
        status_part = f"{user_name} here — {user_status}."
    
    closing_options = [
        "Hope everything goes well!",
        "Take care!",
        "Let me know how it goes.",
        "Sounds like a busy time — hope it all works out."
    ]
    
    # Build acknowledgment based on topics
    acks = []
    if topics["health"]:
        acks.append("Glad you're getting out for walks and healing up.")
    if topics["loss"]:
        acks.append("Sorry to hear about the family losses — thinking of you.")
    if topics["plans"]:
        acks.append("Hope the service goes okay and the reunion planning is nice.")
    
    ack_str = " ".join(acks) if acks else "Thanks for the update!"
    
    # Variation 1: Straightforward & warm
    reply1 = f"{base_greeting} {status_part} {ack_str} {closing_options[0]}"
    replies.append(reply1.strip())
    
    if num_variations > 1:
        # Variation 2: Slightly more personal
        reply2 = f"{base_greeting} {status_part} {ack_str} Appreciate you sharing all that. {closing_options[2]}"
        replies.append(reply2.strip())
    
    if num_variations > 2:
        # Variation 3: Short & sweet
        reply3 = f"{base_greeting} {status_part} {ack_str} {closing_options[3]}"
        replies.append(reply3.strip())
    
    return replies

def get_multiline_input(prompt: str = "Paste the Boomer text below (press Enter twice to finish):") -> str:
    """Simple multi-line input helper."""
    print(prompt)
    lines = []
    while True:
        try:
            line = input()
            if line.strip() == "" and lines:
                break
            lines.append(line)
        except EOFError:
            break
    return "\n".join(lines).strip()

def main():
    print("=== Boomer Text Simplifier v2 ===\n")
    print("Turns long detailed texts into short, friendly replies.\n")
    
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        text = get_multiline_input()
        if not text:
            print("No text provided. Example:")
            print('python boomer_reply_simplifier.py "Hi! I’m doing well! Still having cramping..."')
            return
    
    user_status = input("Your status (default: I'm doing fine): ").strip() or "I'm doing fine"
    user_name = input("Your name/nickname (optional, press Enter to skip): ").strip()
    
    try:
        num_var = int(input("How many reply variations? (1-3, default 3): ").strip() or "3")
        num_var = max(1, min(3, num_var))
    except ValueError:
        num_var = 3
    
    replies = generate_replies(text, user_status, user_name, num_var)
    
    print("\n" + "="*50)
    print("SUGGESTED REPLIES")
    print("="*50 + "\n")
    
    for i, reply in enumerate(replies, 1):
        print(f"Option {i}:")
        print(reply)
        print()
    
    print("Copy one, tweak as needed, and send! 😊")
    print("\nTip: Shorter replies often work great with Boomer texters.")

if __name__ == "__main__":
    main()
