#!/usr/bin/env python3
"""Delete the worked example so the brain starts empty.

Removes only files whose name starts with `example-`, plus the example digest.
Anything you have written yourself is left alone.
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
removed = []

for pattern in ("wiki/people/example-*.md", "wiki/projects/example-*.md",
                "wiki/topics/example-*.md", "wiki/digests/*-example.md"):
    for f in glob.glob(os.path.join(ROOT, pattern)):
        os.remove(f)
        removed.append(os.path.relpath(f, ROOT))

# Strip the example rows out of the index and the ledgers.
for name in ("wiki/index.md", "wiki/commitments.md", "wiki/facts.md", "wiki/log.md"):
    path = os.path.join(ROOT, name)
    if not os.path.exists(path):
        continue
    lines = open(path, encoding="utf-8").read().split("\n")
    kept = [l for l in lines if "example-" not in l and "EXAMPLE" not in l]
    if len(kept) != len(lines):
        open(path, "w", encoding="utf-8").write("\n".join(kept))
        removed.append(f"{name} (example rows)")

print(f"removed {len(removed)} item(s)")
for r in removed:
    print("  -", r)
print("\nNow run: python3 scripts/lint.py")
