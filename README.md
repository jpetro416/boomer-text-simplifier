## Boomer Text Simplifier

A fun CLI tool that helps you craft short, warm, natural replies to those long, detailed text messages from Boomer relatives.

### Why?
Boomers often text like they're writing letters or emails — full of life updates, health news, family stories, and plans all in one big block. This tool analyzes the message and suggests concise, friendly responses so you can reply without writing a novel back.

### Features (v2)
- Detects common topics: health/recovery, family losses/funerals, plans & activities
- Generates 1–3 reply variations
- Supports custom status, your name/nickname, and number of options
- Works from command line or interactive paste mode
- Keeps replies warm and appreciative

### Installation & Usage

```bash
git clone https://github.com/jpetro416/boomer-text-simplifier.git
cd boomer-text-simplifier
python3 boomer_reply_simplifier.py
```

Or run directly with text as argument:

```bash
python3 boomer_reply_simplifier.py "Hi! I’m doing well! Still having a little cramping but I have a few weeks more of healing to go..."
```

### Example

**Input text:**
> Hi! I’m doing well! Still having a little cramping but I have a few weeks more of healing to go. We have been going for little walks so it’s nice to get out. 
> We’re going to Revere on Tuesday. Auntie Anna’s funeral and then Maureen called and her twin sister passed away! They’re only doing a private service for them. She wants to do a family reunion later in the summer.
> How are you doing?? I was going to text you today.

**Sample Output:**

```
=== Suggested Replies ===

Option 1:
Hi! I'm doing fine. Glad you're getting out for walks and healing up. Sorry to hear about the family losses — thinking of you. Hope the service goes okay and the reunion planning is nice. Hope everything goes well!

Option 2:
Hi! I'm doing fine. Glad you're getting out for walks and healing up. Sorry to hear about the family losses — thinking of you. Hope the service goes okay and the reunion planning is nice. Appreciate you sharing all that. Let me know how it goes.

Option 3:
Hi! I'm doing fine. Glad you're getting out for walks and healing up. Sorry to hear about the family losses — thinking of you. Hope the service goes okay and the reunion planning is nice. Sounds like a busy time — hope it all works out.
```

### Tips
- Customize with your name for a more personal touch.
- Choose fewer variations if you want quick suggestions.
- Always tweak the final reply to sound like *you*.

Made with ❤️ for better generational texting harmony.

---

*Inspired by real family group chats and the eternal "How are you?" → novel reply phenomenon.*