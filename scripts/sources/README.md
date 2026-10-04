# Source adapters

One file per source. Each says how to fetch new items, where the watermark
lives, and what counts as noise. The agent reads the adapter before ingesting.

They are markdown, not code, on purpose. Adding a source means writing a page,
not shipping a library. Where a source genuinely needs code (a local database,
an unusual API) the adapter carries the snippet inline.

**Writing a new adapter.** Copy the shape of any file here:

1. **What it is.** One line.
2. **Access.** Exactly how you reach it on your machine. Be specific: the CLI
   name, the auth step, the thing that trips people up.
3. **Fetch.** How to get only what is new, using the watermark.
4. **Write.** Where raw items land and what frontmatter they carry.
5. **Noise.** What never earns a wiki edit.
6. **Gotchas.** What has actually gone wrong.

Send good adapters back as a pull request. The library of adapters is the part
of this kit that gets better with other people in it.
