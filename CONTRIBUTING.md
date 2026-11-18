# Contributing

Thank you for helping make this handbook more accurate.

## The one rule: no source, no claim

Every factual statement must link to a source that supports it **as written**. If the source supports only part of a statement, narrow the statement. If no source supports it, label it `Inference` or `Experience` and say so in the text, or remove it.

## Evidence labels

Use exactly one primary label per claim: `Official`, `Testimony`, `API Docs`, `Patent`, `Secondhand`, `Experience`, or `Inference`. Definitions are in [Chapter 1](chapters/01-reading-seo-evidence.md).

## Citing well

- **Official:** link the page; quote the exact sentence briefly; note the date you read it.
- **Testimony:** give the exhibit number (e.g. `PXRD016`) or transcript date, page and line. Say whether it is sworn testimony, a demonstrative, or interview notes.
- **API Docs:** give module, field, package version and link. Quote the field's own description.
- **Patent:** give the patent or publication number and link to Google Patents.
- **Secondhand:** name the outlet or study, author and date. Link the primary source it relies on when one exists.

## Adding a claim

1. Write the claim in the chapter with its label and link.
2. Add an entry to [`sources/claims.yml`](https://github.com/saeedyeganeh/seo-evidence-handbook/blob/main/sources/claims.yml).
3. Open a pull request describing what you verified and how.

## Reporting an error

Open an issue with the chapter, the claim, and what the source actually says. Errors are fixed first, before new content.

## Style

- Plain, precise English. Short sentences.
- No hype ("secret", "hack", "guaranteed").
- Keep quotations short, and only where exact wording matters; otherwise paraphrase and link.
