#!/usr/bin/env python3
"""Mechanical lint for the wiki. Judgement calls stay with the agent.

Checks: dead [[links]], citations pointing at files that no longer exist, pages
missing from wiki/index.md, and duplicate [wiki-sync:...] slugs in commitments.

Usage: python3 scripts/lint.py        # report, exit 1 if anything is wrong
       python3 scripts/lint.py --quiet # exit code only
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUIET = "--quiet" in sys.argv
problems = []

def wiki_files():
    return sorted(glob.glob(os.path.join(ROOT, "wiki/**/*.md"), recursive=True))

def rel(p):
    return os.path.relpath(p, ROOT)

pages = {os.path.relpath(f, os.path.join(ROOT, "wiki"))[:-3] for f in wiki_files()}

def is_append_only(path):
    # log.md and the digests are the historical record; AGENTS.md forbids
    # rewriting them, so a stale link there is not actionable.
    r = rel(path)
    return r == "wiki/log.md" or r.startswith("wiki/digests/")

# 1. dead wiki links (live pages only)
dead = {}
for f in (x for x in wiki_files() if not is_append_only(x)):
    body = open(f, encoding="utf-8", errors="ignore").read()
    for m in re.finditer(r"\[\[([^\]|#]+)", body):
        target = m.group(1).strip()
        if target.startswith("wiki-sync:"):
            continue  # a tracking slug, not a page
        if target not in pages:
            dead.setdefault(target, set()).add(rel(f))
for target, where in sorted(dead.items()):
    problems.append(f"dead link [[{target}]] in {', '.join(sorted(where)[:3])}")

# 2. citations pointing at missing source files
missing = {}
for f in wiki_files():
    body = open(f, encoding="utf-8", errors="ignore").read()
    for m in re.finditer(r"src:\s*(sources/[^\s\)\],]+)", body):
        cite = m.group(1).rstrip(".,;")
        if not os.path.exists(os.path.join(ROOT, cite)):
            missing.setdefault(cite, set()).add(rel(f))
for cite, where in sorted(missing.items()):
    problems.append(f"citation to a missing file {cite} in {', '.join(sorted(where)[:2])}")

# 3. pages the index does not list
index_path = os.path.join(ROOT, "wiki/index.md")
if os.path.exists(index_path):
    index = open(index_path, encoding="utf-8").read()
    skip = {"index", "commitments", "content-ideas", "log", "facts"}
    for page in sorted(pages):
        if page in skip or page.startswith("digests/"):
            continue
        if page not in index:
            problems.append(f"not listed in index: {page}")

# 4. duplicate commitment slugs inside one sync block
commitments = os.path.join(ROOT, "wiki/commitments.md")
if os.path.exists(commitments):
    text = open(commitments, encoding="utf-8").read()
    for block in re.split(r"^### ", text, flags=re.M)[1:]:
        head = block.split("\n", 1)[0].strip()
        # the canonical tag closes a bullet; an "(Updates `[wiki-sync:x]`)"
        # note mid-line is a cross-reference, not a second declaration
        slugs = re.findall(r"`\[wiki-sync:([a-z0-9-]+)\]`\s*$", block, flags=re.M)
        for slug in {s for s in slugs if slugs.count(s) > 1}:
            problems.append(f"slug [wiki-sync:{slug}] appears twice under '{head}'")

if not QUIET:
    if problems:
        print(f"{len(problems)} problem(s):")
        for p in problems:
            print("  -", p)
    else:
        print("clean")
    print(f"checked {len(pages)} pages")

sys.exit(1 if problems else 0)
