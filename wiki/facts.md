# Facts

One canonical value per fact, with the date it was true and the source that
settles it. For things with exactly one right answer: prices, rates, budgets,
counts, and the rules other people set for you.

**How to use it.** When a page states one of these, it must agree with this file.
When they disagree, this file wins and the page gets rewritten. When a value
changes, overwrite the row and move the old value to Superseded; never append a
second row. A value nobody has agreed yet is marked **OPEN** and must never be
quoted as settled.

| Fact | Value | As of | Source |
|---|---|---|---|
| EXAMPLE: day rate | **EUR 800** | 2026-01-15 | (src: sources/email/2026-01-15/example-quote-thread.md) |
| EXAMPLE: rebuild budget | **OPEN.** Ana floated EUR 6,000; nothing agreed. | 2026-01-15 | (src: sources/email/2026-01-15/example-quote-thread.md) |

## Superseded

Nothing yet. When a value above changes, the old one moves here with the date it
stopped being true, so a reader can tell a stale quote from a wrong one.
