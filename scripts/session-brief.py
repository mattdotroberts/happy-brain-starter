#!/usr/bin/env python3
"""SessionStart hook: hand the new session the map and what is owed.

Prints the JSON shape Claude Code injects into the model's context. Stays silent
on any error: a broken brief must never stop a session from starting.
"""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    if not os.path.exists(os.path.join(ROOT, "AGENTS.md")):
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": "This brain has not been set up yet. Run /setup.",
        }}))
        return

    bits = ["You are in an agent-managed wiki (happy-brain-starter). "
            "Read AGENTS.md before acting on it."]

    digests = sorted(glob.glob(os.path.join(ROOT, "wiki/digests/*.md")))
    if digests:
        with open(digests[-1], encoding="utf-8") as f:
            bits.append("Last run: " + f.readline().strip().lstrip("# "))

    counts = []
    for label, pattern in (("people", "wiki/people/*.md"),
                           ("projects", "wiki/projects/*.md"),
                           ("source files", "sources/**/*.md")):
        n = len(glob.glob(os.path.join(ROOT, pattern), recursive=True))
        counts.append(f"{n} {label}")
    bits.append("Holds " + ", ".join(counts) + ".")

    # The newest "New this sync" block is what is currently owed.
    path = os.path.join(ROOT, "wiki/commitments.md")
    if os.path.exists(path):
        text = open(path, encoding="utf-8").read()
        blocks = re.split(r"^### New this sync ", text, flags=re.M)
        if len(blocks) > 1:
            block = "### New this sync " + blocks[1]
            block = block.split("\n### ")[0].strip()
            if len(block) > 2000:
                block = block[:2000].rstrip() + "\n(truncated, read wiki/commitments.md)"
            bits.append("Newest commitments block:\n" + block)

    bits.append("Facts with one correct answer live in wiki/facts.md. "
                "Run `python3 scripts/lint.py` to check the wiki mechanically.")

    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": "\n\n".join(bits),
    }}))

try:
    main()
except Exception:
    sys.exit(0)
