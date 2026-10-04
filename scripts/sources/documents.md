# A folder of documents

The simplest source, and the right place to start if nothing else is connected.
Drop files in, the agent reads them.

## Access

A folder. That is all. Put it somewhere synced if you want it on more than one
machine.

## Fetch

Anything added or changed since the watermark. Compare by modification time and
by hash, so an edited file is re-read and an unchanged one is skipped.

## Write

Copy the extracted text to `sources/documents/YYYY-MM-DD/<filename>.md`, with the
original path in the frontmatter. Keep the original where it is.

## Noise

Nothing. You chose to put it there.

## Gotchas

- PDFs and spreadsheets need extracting before they are useful. A scanned PDF
  needs OCR, and if you cannot read it, say so rather than guessing from the
  filename.
- Big binaries do not belong in git. Keep them out of the repo and cite the path.
