---
name: setup
description: Set up this brain for the first time. Interviews the owner, then writes AGENTS.md and the state file from the answers.
user-invocable: true
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, AskUserQuestion
---

# Set up this brain

Turn the template into one person's brain. Ask, then write. Never guess an
answer the owner should give.

**Stop if `AGENTS.md` already exists.** Say it is already set up and offer to
change one thing instead of starting over.

## Step 1: Interview

Ask with AskUserQuestion, one question at a time, in this order. Keep the
options short and recommend one.

1. **Name and timezone.** What should the agent call you? Which timezone are
   your dates in?

2. **Sources.** Which of these should the brain read? Multi-select.
   - Group and direct chat (WhatsApp, Signal, Telegram)
   - Email
   - Professional DMs (LinkedIn, X, Slack)
   - Meeting notes and transcripts
   - Saved reading (bookmarks, watched videos, articles)
   - A folder of documents you drop things into

3. **Access, per source chosen.** For each one, ask how they reach it today: a
   CLI already installed, a connector in this client, or a manual export. Write
   the answer into that source's line in AGENTS.md. **If they do not have
   access yet, say so plainly and leave the source out.** A source in the rules
   that cannot be fetched is worse than no source.

4. **Never ingest.** Offer health, family and personal finance as defaults, and
   ask what else. Ask for named people or groups to exclude entirely.

5. **Cadence.** How often does the ingest run? Hint: twice a day works for most
   people; hourly is rarely worth it.

6. **Shared brain.** Do you want a second brain that other people can read, fed
   from this one? If yes, ask for the folder path and what to call the tag that
   marks a page as shared. If no, leave the mirror out of AGENTS.md entirely.

7. **Version control.** Track this folder in git? If yes, offer to init and to
   create a **private** repo. Say out loud that `sources/` holds other people's
   messages and the repo must never be public.

## Step 2: Write AGENTS.md

Copy `AGENTS.md.template` to `AGENTS.md` and fill every placeholder:

| Placeholder | Fill with |
|---|---|
| `{{OWNER}}` | their name |
| `{{TIMEZONE}}` | IANA name, e.g. `Europe/Madrid` |
| `{{SOURCES}}` | one bullet per chosen source: what it covers and how it is reached |
| `{{EXCLUSIONS}}` | one bullet per excluded category, in their words |
| `{{CADENCE}}` | e.g. "twice a day, morning and evening" |
| `{{SCOPE_TAG_RULE}}` | the scope-tag paragraph if they want a shared brain, otherwise empty |
| `{{MIRROR_STEP}}` | the mirror step if they want one, otherwise empty |
| `{{COMMIT_STEP}}` | the commit step if they chose git, otherwise empty |

The scope-tag paragraph, when a shared brain is wanted:

```
- **Scope tag**: pages under `wiki/projects/` that belong to the shared brain get
  a `<!-- scope: {{SCOPE}} -->` HTML comment right after the title. Invisible when
  rendered, greppable. Untagged means private, which is the default. When in
  doubt, leave it untagged and ask.
```

The mirror step, when a shared brain is wanted:

```
8. **Last step, after everything else.** Refresh the shared brain at
   `{{MIRROR_PATH}}`. For every `wiki/projects/*.md` tagged
   `<!-- scope: {{SCOPE}} -->`, copy its current content there, stripping the
   scope comment. Regenerate the shared `commitments.md` as a filtered view:
   only bullets whose `[[projects/X]]` link points at a tagged page. **Never copy
   `sources/`.** Citations travel as plain provenance text; the raw material does
   not. Duplication between the two is expected and fine. This brain stays the
   source of truth regardless of what is mirrored out.
```

The commit step, when git was chosen:

```
9. Commit at the end of every run: `git add -A && git commit -m "run: <one line>"`.
   History is the backup and the audit trail. Never rewrite it, never force-push.
   The repo must stay private: `sources/` holds other people's messages.
```

## Step 3: Write the state file

Copy `state/ingest-state.example.json` to `state/ingest-state.json`, keeping only
the sources they chose, each with a null watermark and their access note.

## Step 4: Clear the example content

Ask whether to keep the worked example (one person, one project, one digest) as
a shape reference, or wipe it now. If wiping, run `python3 scripts/demo-wipe.py`.

## Step 5: Prove it works

Run `python3 scripts/lint.py`. It must print `clean`. Then run the first ingest
over a short window, one source only, and show them the digest it produced
before going wider. A first run that quietly swallows six months is how people
lose trust in this.

## Step 6: Hand over

Tell them, in plain words:
- Where the rules live, and that editing AGENTS.md changes the agent's behaviour.
- That they never hand-edit wiki pages; they tell the agent instead.
- The one command that matters: "sync".
