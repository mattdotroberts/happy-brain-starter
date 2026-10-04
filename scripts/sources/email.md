# Email

Where the deadlines live: invoices, bookings, confirmations, the things with
dates attached.

## Access

A CLI or connector that can list messages after a timestamp and fetch a message
body. Note which account, and whether you have more than one.

## Fetch

Query by **epoch seconds**, not by date. A date-only query re-fetches the whole
day every run and makes duplicates you then have to skip.

Fetch metadata first, decide what is signal, then pull full bodies only for
those. Bodies are large and most mail is noise.

## Write

`sources/email/YYYY-MM-DD/msg-<id>.md`, one file per message, or one file per
day holding the signal with the ids listed in the frontmatter if volume is high.

## Noise

Newsletters, promotions, receipts with no business meaning, login links,
calendar RSVPs, automated digests. Strip them before fetching bodies.

**Never classify as noise:** anyone who already has a wiki page, anything from a
client or supplier domain, and ops alerts about failed payments, usage limits or
security. Those get at least a digest line even when they do not earn a page.

## Gotchas

- Redact one-time codes, confirmation numbers and anything that doubles as a
  password, even in an archive only you can read.
- Your own sent mail is a source. Promises live in it.
