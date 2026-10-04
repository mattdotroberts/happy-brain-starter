# happy-brain-starter

A second brain that writes itself, out of the messages you already send and
receive. It is a folder of markdown files an AI agent keeps current: one page
per person, one per project, a ledger of everything you owe, and a short daily
digest of what changed.

No app. No database. No vendor. Plain text in a folder, which means any AI tool
can read it and so can you, in ten years, with nothing installed.

Built from a working brain that has been running since late 2025. The ideas come
from [Karpathy's LLM wiki](https://github.com/karpathy/llm-wiki): compile
knowledge once into cited pages and keep them current, rather than retrieving
from a pile every time you ask.

## What makes this different from a notes app

- **You never file anything.** The agent reads your sources on a schedule and
  writes the pages.
- **It tracks obligations, not just facts.** Most knowledge bases answer "what is
  true?". This one also answers "what did I promise, and who is waiting on me?"
- **Every claim cites the message it came from.** You can always check.
- **It notices silence.** An unanswered ask and a passed deadline are things
  nothing arrives to tell you about. The ledger watches for them.
- **It can feed a second, shared brain.** One tag on a page decides what your
  team sees. Your copy stays the source of truth. Optional.

## Setup, about fifteen minutes

1. Click **Use this template** and make yourself a **private** repo. Private
   matters: this will hold other people's messages.
2. Clone it and open the folder in [Claude Code](https://claude.com/claude-code).
3. Run `/setup`. It interviews you: your name, which sources to read, what must
   never be touched, how often it runs, and whether you want a shared brain.
4. It writes your `AGENTS.md` from your answers. That file is the agent's rules,
   and editing it changes the agent's behaviour.
5. Say `sync`.

The setup deliberately asks before it writes. A brain configured by guesswork is
one you will not trust.

## What is in the box

```
AGENTS.md.template   the rules, with blanks the setup fills in
wiki/                the knowledge: people, projects, ledgers, digests
sources/             raw material, append-only, never edited
state/               per-source watermarks, so a run takes minutes
scripts/lint.py      mechanical checks: dead links, broken citations
scripts/sources/     one adapter per source, in plain markdown
.claude/             the setup skill and a session-start hook
```

A worked example ships with it: one person, one project, one digest, two raw
source files. Look at it, then delete it with
`python3 scripts/demo-wipe.py`.

## The sources

Adapters for chat, email, professional DMs, meeting notes, saved reading, and a
plain folder of documents. Each is a markdown page telling the agent how to
fetch, what counts as noise, and what has gone wrong before.

**This is the hard part, not the wiki.** Getting at your own messages means
authorising a CLI or a connector, and that is where people stall. Start with one
source. The folder-of-documents adapter needs nothing at all and is a fine way
to see the shape before you wire up anything real.

Adding a source means writing a markdown page, not shipping code. Good adapters
are very welcome as pull requests.

## The shared brain, if you want one

Your brain is private. A team brain can be fed from it through one narrow valve:

- Each project page either carries a scope tag or does not. Tagged means shared.
- On every run, tagged pages are copied to the shared folder, and the commitments
  ledger is filtered down to loops belonging to those projects.
- **Raw sources never cross.** Conclusions travel; the receipts stay home.
- Untagged is the default, because the safe mistake is keeping something private.

That shape scales to a team: one brain per person, one per company, holding
nothing of its own. Publishing is an explicit act on a page, never a guess made
by a machine.

## Privacy

The setup asks what must never be ingested and writes it into your rules.
Health, family and personal finance are offered as defaults. Excluded material is
not summarised or redacted; it never reaches `sources/` at all.

Identity numbers, addresses, passwords and one-time codes are stripped before
anything is written down, even in an archive only you can read.

Nothing leaves the folder unless you ask in that conversation.

## Honest limitations

- It cannot see work you did offline and never mentioned anywhere.
- It is only as good as the sources you connect, and connecting them is fiddly.
- A first run over six months of history will produce something shallow. Start
  with a week.
- It costs tokens. A daily run over an active inbox is not free.

## Licence

MIT. Take it, change it, make it yours.
