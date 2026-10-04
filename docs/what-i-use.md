# What I actually use

One person's stack, October 2026. Not a recommendation and not a sponsored
list. It is here because "find a CLI that keeps a local store" is the exact
sentence where people give up, and naming the thing is more useful than being
vague.

It will age. Check the dates before trusting any of it.

| Source | What I run | What hurts |
|---|---|---|
| WhatsApp | [wacli](https://wacli.sh), a CLI that syncs to a local SQLite store | Media is not downloaded by default, and WhatsApp expires it after a while |
| LinkedIn and X messages | [Beeper](https://beeper.com) desktop, read through its local API | It can send but not draft. Nothing sits in the composer for you to check |
| Email | the Google Workspace CLI (`gws`) | Date-only queries re-fetch the whole day. Query by epoch seconds |
| Meetings | [Granola](https://granola.ai) | It can go quiet for weeks without telling you |
| Saved reading | X bookmarks and YouTube watch history | Videos without captions need transcribing locally |
| Interface | [Claude Code](https://claude.com/claude-code) | The context cost of a long run is real |
| Storage | a synced folder, plus a private GitHub repo | Git inside a synced folder is slow |

## The things that actually cost me time

**Use one source per channel.** Beeper bridges WhatsApp too, and for a while I
had both it and the CLI able to read the same messages. Pick one and write the
other into your rules as forbidden, or you will ingest everything twice and
spend a sync working out which copy is real.

**Watch for the lock.** A scheduled sync and a manual one will fight over the
same local store. Let the running one finish rather than racing it.

**Keep API parallelism low.** Three concurrent requests is fine. Above that I
get TLS handshake failures that look like network problems and are not.

**Media expires.** If you want the photos, download them close to when they
arrive. Later you are asking the phone to re-upload, and sometimes it cannot.

**LinkedIn will block you.** Fetching twenty public profiles in a loop trips
their bot check within seconds, even from a real browser, even logged out. If
you need people's photos, ask them.

**Task managers have caps nobody documents.** I mirrored the commitments ledger
into a task app for months. It silently stopped accepting new items because the
inbox had hit a per-project limit, and the error blamed the plan rather than the
cap. Thirty-two syncs failed before the real cause surfaced. The wiki ledger was
fine the whole time, which is the argument for keeping the ledger in the wiki.

**A notetaker that goes quiet looks the same as a quiet week.** Check that each
source actually returned something, and say so in the digest when one did not.

## What I would start with

If you are setting this up today, connect **one** source and run it for a week
before adding a second. The folder-of-documents adapter needs nothing installed
and is the honest way to see whether the shape suits you.
