# Chapter 4 — Content Quality, Originality and Effort

> **Status:** Draft v0.1 · **Last verified:** 2026-11-21 · **Author:** [Saeed Yeganeh](https://saeedyeganeh.com/en/)

[Chapter 3](03-relevance-and-search-intent.md) asked whether a page is *about* the query. This chapter asks the next question: once many pages are relevant, which ones deserve to be shown first? Google's public answer is "helpful, reliable content". That phrase is easy to repeat and hard to act on. This chapter breaks it into the parts the evidence actually supports: originality, added value, care, expertise, and effort.

As in earlier chapters, the evidence comes in layers. Google's own guidance says what it wants. The rater guidelines say how humans are trained to judge it. Google's spam announcements show where it draws the line. The leaked API documentation shows that some of these ideas exist as named fields. None of these layers, alone, tells us how much any one factor weighs.

---

## 4.1 What Google says it rewards

Google's main page on this topic is *Creating helpful, reliable, people-first content* ([Search Central](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)). It opens by saying that Google's automated ranking systems are designed to give priority to helpful, reliable information `Official`. The page then defines **people-first content** as content created mainly for people, not to manipulate search rankings `Official` (same page).

The core of the page is a set of self-assessment questions. Google does not present them as a scoring formula. They are questions a site owner can ask about their own work.

### Content and quality

The page groups twelve questions under content and quality `Official` (same page). They fall into four themes:

| Theme | What the questions ask |
|---|---|
| **Originality** | Does the content provide original information, reporting, research or analysis? |
| **Depth** | Does it give a substantial or comprehensive description of the topic? Does it offer more than other pages in the search results? |
| **Added value** | If it draws on other sources, does it simply copy or rewrite them, or does it add value of its own? |
| **Care** | Is it free of spelling and style problems? Was it produced with care, or does it look rushed? Is it produced by many creators or largely outsourced, so that individual pages may not get much attention? |

The same list also asks about titles. A title should give a clear summary of the page, and a headline should avoid exaggeration or shock `Official` (same page). Chapter 9 covers titles in detail.

Two of the questions are useful tests in practice. One asks whether the page is something you would bookmark, share with a friend or recommend. Another asks whether the content could appear in a printed magazine, encyclopedia or book `Official` (same page).

### Expertise

A second group of four questions concerns expertise `Official` (same page). They ask whether:

- the content presents information in a way that makes you want to trust it, for example through clear sourcing and information about the author;
- someone researching the site would come away thinking it is trustworthy or an authority on its topic;
- the content is written or reviewed by an expert or enthusiast who knows the topic well;
- the content contains easily verified factual errors.

### E-E-A-T is a lens, not a factor

The same page discusses E-E-A-T: experience, expertise, authoritativeness and trust. It says that trust is the most important of the four `Official` (same page). It also says E-E-A-T is not itself a specific ranking factor `Official` (same page).

The page repeats a point from [Chapter 1](01-reading-seo-evidence.md#worked-example-b-do-quality-raters-change-rankings): search quality raters have no control over how pages rank, and their feedback does not directly affect Google's ranking algorithms `Official` (same page).

**What we can say:** Google publicly describes quality in terms of originality, depth, added value, care and trustworthy expertise. It describes E-E-A-T as a framework for thinking about quality, not as a single signal.

**What we cannot say:** which of these questions, if any, corresponds to a measurable signal, or how the answers are weighted.

---

## 4.2 What Google says it does *not* reward

The same page includes a second list. It describes **search engine-first** content: content made mainly to attract search visits. Google says that answering yes to some or all of these questions is a sign to re-evaluate how you create content `Official` (same page).

The warning signs include `Official` (same page):

- The main goal of the content is to attract visits from search engines.
- You produce a lot of content on many different topics, hoping some of it will perform well.
- You use extensive automation to produce content on many topics.
- You mainly summarise what others have to say.
- You write about a topic simply because it is popular at the moment.
- After reading, people feel they need to search again.
- You write to a particular word count because you heard Google prefers one. The page says that is not the case.
- You entered a niche topic without real expertise.
- Your content answers a question that has no confirmed answer.
- You change the dates on pages to make them look fresh when the content has not really changed.
- You add a lot of new content, or remove a lot of old content, as a search tactic. The page says this technique does not work.

Three of these points correct common SEO habits directly:

1. **Word count.** Google says it has no preferred word count `Official` (same page). Length is not a goal in itself. "Comprehensive" in the first list refers to covering the topic, not to a number of words `Inference`.
2. **Fake freshness.** Changing a date without changing the content is listed as a warning sign `Official` (same page). Chapter 10 covers freshness.
3. **Mass pruning or mass publishing.** Adding or removing large amounts of content as a tactic is described as not working `Official` (same page). This does not mean that removing genuinely poor pages is never useful. It means that volume changes alone are not a quality improvement `Inference`.

---

## 4.3 How raters are taught to judge quality

The Search Quality Rater Guidelines explain how Google's human raters evaluate pages. As [Chapter 1](01-reading-seo-evidence.md) explains, raters do not change rankings. Their ratings are used to evaluate ranking systems. The guidelines are still valuable, because they describe what Google's systems are *aiming for*.

Google's 36-page overview of the guidelines, dated November 2023, summarises the Page Quality rating process ([Search Quality Rater Guidelines: An Overview](https://services.google.com/fh/files/misc/hsw-sqrg.pdf)). Three statements in it matter for this chapter:

- **Purpose comes first.** Websites and pages should be created to help people. If a page is not, a rating of Lowest may be warranted `Official` (same document, Page Quality section).
- **Effort, originality and skill.** As a general rule, the main content of a page is high quality if creating it takes a "significant amount of effort, originality, and talent or skill" `Official` (same document, Page Quality rating process).
- **The bottom of the scale.** Lowest-quality pages are described as untrustworthy, deceptive, or harmful to people or society `Official` (same document, Page Quality section).

The overview is a summary. It refers readers to the full guidelines for the detailed definitions and examples. This chapter cites only the overview, because that is the document checked for it.

**What we can say:** in Google's own framework for human evaluation, effort, originality and skill are the three things that separate high-quality main content from the rest. Purpose (helping people) is the first test.

**What we cannot say:** that "effort" or "originality" in the rater guidelines are computed by ranking systems in the same way a human rater would judge them. Section 4.5 shows that related fields exist, but not how they relate to rater concepts.

---

## 4.4 Scale, automation and the line into spam

Low-quality content is not always spam. But Google draws a clear line when content is produced in large volumes mainly to rank.

### The March 2024 changes

In March 2024 Google announced a set of changes aimed at low-quality and unoriginal results ([New ways we're tackling spammy, low-quality content on Search](https://blog.google/products/search/google-search-update-march-2024/)). The announcement said the changes would together reduce low-quality, unoriginal content in search results by 40% `Official`. An update to the same post, dated 26 April 2024, said the rollout was complete as of 19 April. It revised the figure to 45% less low-quality, unoriginal content `Official` (same post, April 2024 update).

The same post described three policy changes `Official` (same post):

| Policy | What the post says |
|---|---|
| **Scaled content abuse** | The policy was strengthened to cover producing content at scale to boost search rankings, "whether automation, humans or a combination are involved". It targets pages that claim to answer popular searches but do not deliver helpful content. |
| **Site reputation abuse** | Very low-value, third-party content produced mainly for ranking, without close oversight by the website owner, is treated as spam. The post said enforcement would begin on 5 May. |
| **Expired domain abuse** | Buying an expired domain and repurposing it to boost the ranking of low-quality content is treated as spam. |

### Why "automation, humans or a combination" matters

The wording of the scaled content policy is the most important detail here. The policy is defined by **purpose and scale**, not by the tool. A thousand thin pages written by hired writers fall under the same description as a thousand thin pages produced by software `Official` (same post).

This fits the warning signs in section 4.2, which list extensive automation, producing content on many topics hoping some will perform, and outsourcing to many creators side by side `Official` ([Creating helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)).

**What we can say:** Google treats mass-produced content made mainly to rank as a spam problem, whatever produces it. It reported a large measured reduction in low-quality, unoriginal results after the March 2024 changes.

**What we cannot say:** how Google measured the 40% and 45% figures, or what "low-quality, unoriginal" means operationally in that measurement. The post gives the figures without a method.

---

## 4.5 What the leaked API documentation shows

The Content Warehouse API reference (see [Chapter 1](01-reading-seo-evidence.md), section 1.2) defines several fields whose names and descriptions touch on effort, originality and low quality. As always, a field's existence shows that data is defined. It does not show weight or current use.

### Effort

In the `QualityNsrPQData` module, the field `contentEffort` is described as "LLM-based effort estimation for article pages" `API Docs` ([v0.4.0 reference](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.QualityNsrPQData.html)). Its type is a list of `QualityNsrVersionedFloatSignal`, so it holds versioned numeric values `API Docs` (same page). The description ends with an internal reference that the documentation does not explain.

In the `CompressedQualitySignals` module, a separate field `ugcDiscussionEffortScore` is described as user-generated-content (UGC) page quality signals, multiplied by 1,000 and rounded down `API Docs` ([v0.4.0 reference](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.CompressedQualitySignals.html)).

### Originality

In the `PerDocData` module, the field `OriginalContentScore` is stored in 7 bits, from 0 to 127 `API Docs` ([v0.4.0 reference](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.PerDocData.html)). Its description adds a limit that is easy to miss: only pages with little content have this field `API Docs` (same page).

### Low quality and spam-like text

The same `PerDocData` module defines `KeywordStuffingScore` and `GibberishScore`, each stored in 7 bits from 0 to 127 `API Docs` (same page).

In `CompressedQualitySignals`, several fields describe low-quality or demotion signals `API Docs` (same page):

- `lowQuality` is described as an S2V low quality score converted from `quality_nsr.NsrData` and applied in Qstar.
- `pandaDemotion` is described as an encoding of Panda fields from a site quality features proto.
- `babyPandaV2Demotion` is described as a new demotion applied on top of Panda, meant to replace `babyPandaDemotion`.
- `pqData` is described as encoded page-level PQ signals.

The `QualityNsrPQData` module also includes a field `vlq`, described only as the URL-level score of the VLQ model `API Docs` ([v0.4.0 reference](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.QualityNsrPQData.html)). The documentation does not expand "VLQ", "PQ", "S2V" or "NSR", and this handbook does not guess.

### Reading these fields correctly

**What we can say:** at the time of the leaked documentation, Google defined a field for estimating the effort behind article pages using a large language model. It also defined an original-content score, though only for pages with little content. Low-quality, keyword-stuffing and gibberish scores were defined as well. These fields line up with the themes in Google's public guidance: effort, originality, and the avoidance of thin or manipulative text.

**What we cannot say:**

- that `contentEffort` is used in ranking, or how much it weighs;
- what "effort" means to the model behind it, or which features it looks at;
- that `OriginalContentScore` applies to normal, substantial pages. Its own description limits it to pages with little content;
- that any of these fields is still in use today.

**`Inference`:** the agreement between the public guidance (section 4.1), the rater framework (section 4.3) and these field names suggests that effort and originality are things Google has tried to measure, not only to recommend. This is a reasonable reading of three independent kinds of evidence. It is still an inference.

---

## 4.6 Putting it together

| Question | Best evidence | Label | Strength |
|---|---|---|---|
| Does Google want original, value-adding content? | Self-assessment questions on the helpful content page | `Official` | Direct statement |
| Is there a preferred word count? | Same page: no | `Official` | Direct statement |
| Is E-E-A-T a ranking factor? | Same page: not a specific factor; trust matters most | `Official` | Direct statement |
| Is effort part of how quality is judged? | Rater overview: effort, originality, talent or skill | `Official` | Human-rating framework, not a signal |
| Does Google define an effort field? | `contentEffort` in `QualityNsrPQData` | `API Docs` | Field exists; use and weight unknown |
| Does Google define an originality field? | `OriginalContentScore` in `PerDocData`, limited to pages with little content | `API Docs` | Field exists; narrow scope |
| Is mass-produced content spam even when humans write it? | March 2024 post on scaled content abuse | `Official` | Direct statement |

A pattern runs through this table. The public guidance and the internal field names point the same way. Neither gives a formula. The practical conclusion is not "add effort signals". It is to do the work that makes a page genuinely more useful than the pages already ranking, and to make that work visible to the reader `Inference`.

---

## 4.7 Checklist: quality, originality and effort for one page

- [ ] **Original contribution.** What does this page offer that the current top results do not: data, testing, first-hand experience, analysis, or a clearer explanation?
- [ ] **Added value over sources.** If the page draws on other sources, does it add substantial value, or does it mainly rewrite them?
- [ ] **Completeness, not length.** Does it fully cover what the reader needs? Ignore word-count targets.
- [ ] **Visible care.** Is it free of factual errors, spelling problems and signs of rushing?
- [ ] **Visible expertise.** Is it clear who wrote or reviewed it and why they know the topic? Are claims sourced?
- [ ] **Purpose.** Would you publish this page if search engines did not exist?
- [ ] **Scale check.** Is it one of many near-identical pages made mainly to catch queries? If so, it risks falling under scaled content abuse, whoever or whatever wrote it.
- [ ] **No fake freshness.** Has the date changed only when the content changed?
- [ ] **Search-again test.** After reading, would a visitor need to go back to the results?

---

## Sources for this chapter

| # | Source | Type | Checked |
|---|---|---|---|
| 1 | Google Search Central — [Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | Official | 2026-11-21 |
| 2 | Google — [Search Quality Rater Guidelines: An Overview (Nov 2023)](https://services.google.com/fh/files/misc/hsw-sqrg.pdf) | Official | 2026-11-21 |
| 3 | Google Blog — [New ways we're tackling spammy, low-quality content on Search (March 2024, updated 26 April 2024)](https://blog.google/products/search/google-search-update-march-2024/) | Official | 2026-11-21 |
| 4 | HexDocs — [`QualityNsrPQData`, google_api_content_warehouse v0.4.0](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.QualityNsrPQData.html) | API Docs | 2026-11-21 |
| 5 | HexDocs — [`PerDocData`, google_api_content_warehouse v0.4.0](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.PerDocData.html) | API Docs | 2026-11-21 |
| 6 | HexDocs — [`CompressedQualitySignals`, google_api_content_warehouse v0.4.0](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.CompressedQualitySignals.html) | API Docs | 2026-11-21 |

Source 1 was checked on 2026-11-21 through the page's French-language version, which showed a last-updated date of 2026-11-10. Statements from it are paraphrased, not quoted.

Not yet included, because they could not be re-checked for this draft: Google's 2023 post on AI-generated content, the guidance page on using generative AI content, the ranking systems guide entries on original content and reviews, and the full spam policy definitions. They are planned for the next revision.

---

*Next chapter (planned): Links and how they are weighted — what Google says about links, and what the court record and API documentation add.*
