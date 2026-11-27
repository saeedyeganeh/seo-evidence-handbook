# SEO Evidence Handbook

**How Google Search works, explained claim by claim, with the evidence behind each one.**

This is an open, English-language handbook on search engine optimisation. Every factual statement is traced to its source and labelled by the *kind* of evidence behind it. The aim is to separate what Google has documented, what its engineers said in court, what leaked internal documentation shows, and what is still interpretation or experience.

Maintained by **[Saeed Yeganeh](https://saeedyeganeh.com/en/)**: software engineer, information-retrieval researcher, and SEO and AI specialist.

---

## Why this handbook exists

Most SEO guides mix four different things without saying so: Google's public guidance, insider evidence, industry belief, and personal anecdote. The result is advice that sounds equally confident whether it rests on a sworn statement or a guess.

This handbook does the opposite. Each claim carries one of these labels:

| Label | Meaning |
|---|---|
| `Official` | Google's own documentation or public statements by its search representatives |
| `Testimony` | Material from *U.S. v. Google LLC*: trial testimony, demonstratives, or exhibits (the exhibit type is stated) |
| `API Docs` | The leaked Google Content Warehouse API reference, cited by module, field and version |
| `Patent` | A Google patent, cited by number. Describes a design, not proof of current use |
| `Secondhand` | Reporting, studies and surveys about Search |
| `Experience` | Practitioner observation, with conditions stated |
| `Inference` | A conclusion drawn from evidence that the evidence does not state directly |

Read [Chapter 1](chapters/01-reading-seo-evidence.md) first. It explains what each kind of evidence can and cannot prove.

## Contents

| # | Chapter | Status |
|---|---|---|
| 01 | [Reading SEO evidence: sources and how much to trust them](chapters/01-reading-seo-evidence.md) | Draft v0.1 |
| 02 | [How Google Search works end to end](chapters/02-how-search-works.md) | Draft v0.1 |
| 03 | [Relevance and search intent](chapters/03-relevance-and-search-intent.md) | Draft v0.1 |
| 04 | [Content quality, originality and effort](chapters/04-content-quality-originality-effort.md) | Draft v0.1 |
| 05 | [Links and how they are weighted](chapters/05-links-and-how-they-are-weighted.md) | Draft v0.1 |
| 06 | [Link spam and patterns](chapters/06-link-spam-and-patterns.md) | Draft v0.1 |
| 07 | [Site-level quality signals](chapters/07-site-level-quality-signals.md) | Draft v0.1 |
| 08 | [User interaction signals and NavBoost](chapters/08-user-interaction-signals-and-navboost.md) | Draft v0.1 |
| 09 | [Titles and snippets in results](chapters/09-titles-and-snippets.md) | Draft v0.1 |
| 10 | [Freshness](chapters/10-freshness.md) | Draft v0.1 |
| 11 | Sensitive (YMYL) topics | Planned |
| 12 | Technical SEO | Planned |
| 13 | Timing, updates and recovery | Planned |
| 14 | Diagnosing traffic drops | Planned |
| 15 | AI features in Search | Planned |
| — | Glossary | Planned |

## How to verify anything here

- Every chapter ends with a source table.
- Every claim is logged in [`sources/claims.yml`](sources/claims.yml) with its evidence type, source link, locator, and the date it was checked.
- If you find a claim that its source does not support, please [open an issue](https://github.com/saeedyeganeh/seo-evidence-handbook/issues). Corrections are the most valuable contribution to this project.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The one rule: **no source, no claim.**

## Licence

Text and diagrams are licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://github.com/saeedyeganeh/seo-evidence-handbook/blob/main/LICENSE). You may share and adapt them, including commercially, as long as you credit **Saeed Yeganeh** and link to this repository.

Quoted material remains the property of its owners and is quoted briefly for commentary and citation.

*This project is independent and is not affiliated with or endorsed by Google.*
