# Chat (WhatsApp, Signal, Telegram)

> **A known-good setup** is listed in [`docs/what-i-use.md`](../../docs/what-i-use.md), with what breaks.

Usually the richest source and the most sensitive. Most of what a person agrees
to happens here, mixed in with their family.

## Access

You need something that keeps a **local store** of your own messages. A CLI that
syncs to a local database is the only approach that gives you a watermark, full
history and no rate limits. A phone export is a one-off and cannot be repeated
daily.

Whatever you use, authenticate it once, confirm it has caught up, and note the
command in `AGENTS.md`.

## Fetch

Pull everything since the watermark, per chat. From a local SQLite store the
shape is:

```sql
SELECT chat_id, timestamp, sender, text
FROM messages
WHERE timestamp >= <watermark>
ORDER BY chat_id, timestamp;
```

Resolve sender ids to names from the contacts table where you can. An id in the
wiki is useless six months later.

## Write

`sources/chat/YYYY-MM-DD/<a-short-slug>.md`, one file per day per theme rather
than one per message. Group by conversation, keep the timestamps, keep who said
what.

## Noise

- Reaction echoes ("Reacted 👍 to..."). They show what landed, but never quote
  them as something a person said.
- Pure logistics with no decision in them.
- Anything in an excluded chat. Those never reach `sources/` at all.

## Gotchas

- **Media is not text.** Images and voice notes arrive as a filename. Either
  download and look at them, or say in the wiki that the content was not captured.
- **Your own messages matter most.** Everything you send is evidence of what you
  promised. Ingest outbound as carefully as inbound.
- **Group names drift.** Store the stable id in the state file, not the name.
