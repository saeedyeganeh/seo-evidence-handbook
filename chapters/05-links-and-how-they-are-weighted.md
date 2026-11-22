# Chapter 5 — Links and How They Are Weighted

> **Status:** Draft v0.1 · **Last verified:** 2026-11-22 · **Author:** [Saeed Yeganeh](https://saeedyeganeh.com/en/)

Links were the idea that set Google apart at the start. They are still the subject of more SEO folklore than almost anything else. This chapter asks three narrow questions. What did the original design say links were for? What does Google say about links today? And what do the court record and the leaked API documentation add about how links are *weighted*, as opposed to simply counted?

The answer is layered, as in earlier chapters. The original paper gives the design idea. Google's public documentation covers how site owners should mark links. Call summaries from *U.S. v. Google* say that PageRank still feeds quality signals. The API documentation shows that a link carries many attributes besides its existence. None of these sources gives a weight, a threshold or a formula.

Link spam, link schemes and the penalties for them are covered in [Chapter 6](#next-chapter).

---

## 5.1 The original design: PageRank and anchor text

Google's founders described the first version of the search engine in *The Anatomy of a Large-Scale Hypertextual Web Search Engine* ([Brin & Page, Stanford](https://www2.math.upenn.edu/~kazdan/210/LectureNotes/Google/Brin-Page.html)). It is a research paper, so the handbook labels it `Secondhand` in the sense of a published study. Like a patent, it describes a design. It does not prove how Google works today.

### PageRank

The paper explains PageRank with a "random surfer". This imaginary user is given a random page and keeps clicking links `Secondhand` (section 2.1.2).

Two consequences follow, and the paper states both `Secondhand` (section 2.1.2):

- A page can have high PageRank because many pages point to it.
- A page can also have high PageRank because a smaller number of pages with high PageRank point to it.

The paper's formula includes a damping factor, *d*. The authors say they usually set it to 0.85 `Secondhand` (section 2.1.1).

The key point for this chapter: **in the original design, links were never counted equally.** A link from an important page passed more value than a link from an obscure one.

### Anchor text

The paper also treats the visible text of a link, its *anchor text*, as a description of the page the link points to. The engine associated that text with the *target* page, not only with the page containing the link `Secondhand` (section 2.2). The authors gave two reasons:

1. Anchors often describe a page more accurately than the page describes itself `Secondhand` (section 2.2).
2. Anchors can exist for things a text-based engine cannot index, such as images, programs and databases `Secondhand` (section 2.2).

**What we can say:** from its first published design, Google used links in two ways. One was a link-based importance score (PageRank). The other was anchor text as a description of the target page.

**What we cannot say:** that today's PageRank uses the same formula, the same damping factor, or the same role. Section 5.3 shows that PageRank still exists in some form. It does not show its current formula.

---

## 5.2 What Google says publicly about links today

### Not every link is meant to pass credit

Google asks site owners to label some outbound links with a `rel` attribute ([Qualify your outbound links to Google](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links?hl=en)). The page sets out three values `Official`:

| Value | Use it for |
|---|---|
| `sponsored` | Links that are ads or paid placements |
| `ugc` | Links inside user-generated content, such as comments and forum posts |
| `nofollow` | Other cases, when you do not want Google to associate your site with the linked page or to crawl the linked page from your site |

The same page says several details that matter in practice `Official` (same page):

- More than one value can be combined, for example `rel="ugc nofollow"`.
- `nofollow` used to be the recommended marking for paid links. It is still acceptable, but `sponsored` is preferred.
- Links with these attributes are generally not followed. The linked pages can still be discovered in other ways, such as sitemaps or links from other sites.

### The attributes are hints, not commands

Google introduced `sponsored` and `ugc` on 10 September 2019 in a post by Danny Sullivan and Gary Illyes ([Evolving "nofollow"](https://developers.google.com/search/blog/2019/09/evolving-nofollow-new-ways-to-identify?hl=en)). The post made three points `Official`:

- All three attributes are treated as **hints** about which links to consider or exclude in Search.
- The reason given is that links carry useful information, such as how anchor text describes the target page. Ignoring marked links completely would throw that information away.
- From 1 March 2020, `nofollow` also became a hint for crawling and indexing. Site owners do not need to change existing `nofollow` links.

**What we can say:** Google wants paid and user-generated links labelled. Since 2019–2020, those labels are hints. Google may still learn from a marked link, for example from its anchor text.

**What we cannot say:** that a `nofollow` link passes ranking credit in any given case. "Hint" means Google decides. It does not mean the link counts.

---

## 5.3 What the court record adds

The U.S. Department of Justice published summaries of calls held in early 2025 with Google engineers, as exhibits in the remedies phase of *U.S. v. Google*. As explained in [Chapter 1](01-reading-seo-evidence.md), section 1.2, these are notes of a call, not sworn trial testimony. They are still first-hand descriptions from people who built the systems.

### HJ Kim, 18 February 2025 (PXR0356)

The call summary with Google engineer Hyung-Jin (HJ) Kim lists the main signal families ([PXR0356](https://www.justice.gov/atr/media/1398871/dl)):

- It defines **Anchors (A)** as a source page pointing to a target page, that is, links `Testimony` (call summary, p. 1).
- It describes **PageRank** as a single signal relating to "distance from a known good source". It adds that PageRank is used as an input to the Quality score `Testimony` (call summary, p. 3).
- It calls Q*, page quality understood as trustworthiness, "incredibly important" `Testimony` (call summary, p. 3). It describes Q* as largely static, though in some cases affected by the query `Testimony` (call summary, p. 4).

### Pandu Nayak, 31 January 2025 (PXR0357)

The call summary with Pandu Nayak makes a similar point in different words ([PXR0357](https://www.justice.gov/atr/media/1398866/dl)):

- PageRank, described as one of Google's original signals, continues to be one of the factors that go into the quality signals for pages `Testimony` (call summary, p. 1).
- A Google signal called Anchor identified a document's quality partly by how many other documents linked to it `Testimony` (call summary, p. 4).

### Reading these two exhibits together

**What we can say:** two senior Google engineers, in separate calls in 2025, described PageRank as still in use and as an input to page quality. One of them described it in terms of distance from trusted ("known good") sources. Links and anchors are named as a signal family of their own.

**What we cannot say:**

- how "distance from a known good source" is computed, or which sources count as known good;
- how much PageRank contributes to Q*, or how much Q* contributes to final ranking;
- that the Kim and Nayak summaries describe the same version of PageRank.

**`Inference`:** "distance from a known good source" is a different description from the random-surfer model in section 5.1. It suggests that PageRank has changed since 1998 towards measuring closeness to trusted pages. The exhibit does not state that history. It only gives the current description.

---

## 5.4 What the leaked API documentation shows

The Content Warehouse API reference (see [Chapter 1](01-reading-seo-evidence.md), section 1.2) defines how Google stored links, which it calls *anchors*. As always, a field shows that data was defined. It does not show weight or current use.

### A link is not one number

The `AnchorsAnchor` module describes a single link ([v0.4.0 reference](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.AnchorsAnchor.html)). Its fields include `API Docs`:

- `sourceType`, which records the quality of the anchor's source page. Its description says this is correlated with, but not identical to, the source page's index tier. It lists high, medium and low quality types.
- `weight`, an integer from 0 to 127.
- `pagerankWeight`, described as a weight stored in linkmaps for the "pageranker".
- `isLocal`, which roughly marks whether the source and target are on the same domain.
- `parallelLinks`, a count of additional links from the same source page to the same target domain.
- `firstseenDate`, the day the link was first seen, and `creationDate`, described as the first and last time the anchor was seen.
- `text` and `origText`, the anchor text, and `context2`, a hash of terms near the anchor.
- `experimental`, which marks anchors for experiments that should not be used in serving.

### The source page has its own scores

The `AnchorsAnchorSource` module holds attributes of the page the link comes from ([v0.4.0 reference](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.AnchorsAnchorSource.html)). Its fields include `pagerank` and `pagerankNs`, both on a 16-bit scale, plus `spamrank`, `indyrank` and `nsr` `API Docs`. A field `homePageInfo` records whether the source is a home page, using values named `NOT_HOMEPAGE`, `NOT_TRUSTED`, `PARTIALLY_TRUSTED` and `FULLY_TRUSTED` `API Docs` (same page). The documentation does not explain what makes a home page trusted.

### Not every link is kept

The `Anchors` module groups the links pointing to one target ([v0.4.0 reference](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.Anchors.html)). It includes counters for anchors *dropped* during processing: local home-page anchors, local non-home-page anchors, non-local anchors and redundant anchors `API Docs`. It also records the index tier the anchors were extracted from `API Docs` (same page).

### Anchor text can be penalised

The `IndexingDocjoinerAnchorSpamInfo` module summarises the output of a component called `AnchorSpamPenalizer` ([v0.4.0 reference](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.IndexingDocjoinerAnchorSpamInfo.html)). Its description says spammy anchors are tagged and demoted `API Docs`. Its fields include a predicted probability of spam, a combined penalty for anchor demotion, the number of spam phrases found, and the average daily rate at which spam anchors are discovered `API Docs` (same page). [Chapter 6](#next-chapter) returns to this module.

### Reading these fields correctly

**What we can say:** in the documented data model, a link carries far more than "exists or not". It records the quality of its source, a weight, a PageRank-related weight, whether it is internal, how many sibling links share its source, when it was first seen, and its text and nearby words. Some links are dropped before use, and anchor text can be demoted as spam.

**What we cannot say:**

- how `weight`, `pagerankWeight` or `sourceType` are calculated or combined;
- that internal links (`isLocal`) count less than external ones. The field only marks them;
- that links from "trusted" home pages count more. The enum names suggest a distinction, but no rule is documented;
- what "NSR", "indyrank" or "spamrank" stand for. The documentation does not expand them, and this handbook does not guess.

**`Inference`:** the agreement between the original design (links weighted by the importance of their source), the 2025 call summaries (PageRank as distance from known good sources) and these fields (source quality, trust levels, per-link weights) points the same way. Google weights links mainly by *where they come from*, not by how many there are. This is a reasonable reading of three independent kinds of evidence. It is still an inference.

---

## 5.5 How important are links now? What Googlers have said publicly

Statements about the *relative* importance of links come mostly from conference talks, reported by others. They are `Secondhand` and should be read with care.

- At Pubcon Pro in Austin in 2023, Gary Illyes said people overestimate links and that they have not been a top-three ranking factor "for some time" `Secondhand` ([Search Engine Land](https://searchengineland.com/links-google-search-ranking-factor-gary-illyes-432422)). The same report quotes him saying it is possible to rank without links.
- At SERP Conf in April 2024, Illyes reportedly said Google needs very few links to rank pages `Secondhand` ([Search Engine Roundtable, 22 April 2024](https://www.seroundtable.com/google-very-few-links-needed-rank-pages-37267.html)). The report relays this from an attendee's post, not from a transcript. It also shows a later post by Illyes on X saying he should not have said it.

**What we can say:** Google representatives have publicly played down the *relative* importance of links in recent years.

**What we cannot say:** that links do not matter. The 2025 call summaries in section 5.3 describe PageRank as still in use. "Not top three" and "very few links" are informal remarks with no stated measure. One was partly withdrawn.

---

## 5.6 Putting it together

| Question | Best evidence | Label | Strength |
|---|---|---|---|
| Were links weighted by source importance in Google's design? | Brin & Page paper, section 2.1 | `Secondhand` (study) | Original design, not current proof |
| Is anchor text used to describe the target page? | Brin & Page, section 2.2; Google's 2019 nofollow post | `Secondhand`, `Official` | Design plus current statement |
| Is PageRank still used? | PXR0356, PXR0357 | `Testimony` (call summaries) | First-hand, 2025 |
| What does PageRank measure now? | PXR0356: distance from a known good source | `Testimony` | Short description, no formula |
| Does Google honour `nofollow`? | 2019 post: a hint, not a directive | `Official` | Direct statement |
| Does a link carry quality, weight and trust data? | `AnchorsAnchor`, `AnchorsAnchorSource` fields | `API Docs` | Fields exist; use and weight unknown |
| Can anchor text be demoted as spam? | `IndexingDocjoinerAnchorSpamInfo` | `API Docs` | Component described; scale unknown |
| Are links a top-three factor? | Illyes, Pubcon 2023: no | `Secondhand` | Informal remark |

---

## 5.7 Checklist: thinking about links on your site

- [ ] **Source over count.** For each link you value, ask where it comes from. Is the source page itself trusted, relevant and well linked? `Inference` from sections 5.1, 5.3 and 5.4.
- [ ] **Anchor text describes the target.** Use link text that tells a reader what they will find. Google has used anchor text to describe target pages since its first design.
- [ ] **Label paid links.** Mark ads and paid placements with `rel="sponsored"`. Mark comment and forum links with `rel="ugc"`.
- [ ] **Do not rely on `nofollow` as a wall.** It is a hint. If you do not want a page crawled or indexed, use the tools built for that (covered in Chapter 12).
- [ ] **Do not chase link counts.** The documented data model records source quality and counts sibling links, and some anchors are dropped, so raw counts may add little. `Inference` from section 5.4.
- [ ] **Watch anchor-text patterns.** Large numbers of identical, keyword-heavy anchors are the pattern the anchor spam component is built to catch. See Chapter 6.

---

## Sources for this chapter

| # | Source | Type | Checked |
|---|---|---|---|
| 1 | Sergey Brin and Lawrence Page — [The Anatomy of a Large-Scale Hypertextual Web Search Engine](https://www2.math.upenn.edu/~kazdan/210/LectureNotes/Google/Brin-Page.html) (copy hosted by the University of Pennsylvania) | Secondhand (research paper) | 2026-11-22 |
| 2 | Google Search Central — [Qualify your outbound links to Google](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links?hl=en) | Official | 2026-11-22 |
| 3 | Google Search Central Blog — [Evolving "nofollow": new ways to identify the nature of links (10 Sep 2019)](https://developers.google.com/search/blog/2019/09/evolving-nofollow-new-ways-to-identify?hl=en) | Official | 2026-11-22 |
| 4 | U.S. DOJ — [PXR0356, call summary with HJ Kim, 18 Feb 2025](https://www.justice.gov/atr/media/1398871/dl) | Testimony (call summary) | 2026-11-22 |
| 5 | U.S. DOJ — [PXR0357, call summary with Pandu Nayak, 31 Jan 2025](https://www.justice.gov/atr/media/1398866/dl) | Testimony (call summary) | 2026-11-22 |
| 6 | HexDocs — [`AnchorsAnchor`, google_api_content_warehouse v0.4.0](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.AnchorsAnchor.html) | API Docs | 2026-11-22 |
| 7 | HexDocs — [`AnchorsAnchorSource`, v0.4.0](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.AnchorsAnchorSource.html) | API Docs | 2026-11-22 |
| 8 | HexDocs — [`Anchors`, v0.4.0](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.Anchors.html) | API Docs | 2026-11-22 |
| 9 | HexDocs — [`IndexingDocjoinerAnchorSpamInfo`, v0.4.0](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.IndexingDocjoinerAnchorSpamInfo.html) | API Docs | 2026-11-22 |
| 10 | Search Engine Land — [Links are not a top 3 Google Search ranking factor, says Gary Illyes (2023)](https://searchengineland.com/links-google-search-ranking-factor-gary-illyes-432422) | Secondhand | 2026-11-22 |
| 11 | Search Engine Roundtable — [Google: we need very few links to rank pages (22 Apr 2024)](https://www.seroundtable.com/google-very-few-links-needed-rank-pages-37267.html) | Secondhand | 2026-11-22 |

Notes on this check: source 2 was served in its Turkish-language version (last updated 2026-11-12), so its statements are paraphrased, not quoted. Source 3's article body was read through an extracted summary, so it is paraphrased too.

Not yet included, because they could not be fetched for this draft: the "Link analysis systems and PageRank" entry in Google's [ranking systems guide](https://developers.google.com/search/docs/appearance/ranking-systems-guide), and Google's [link best practices](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) page on crawlable links and anchor text. They are planned for the next revision.

---

<a id="next-chapter"></a>*Next chapter (planned): Link spam and patterns — Google's link spam policies, SpamBrain, and what the documentation says about unnatural links.*
