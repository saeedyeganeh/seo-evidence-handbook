# Chapter 1 — Reading SEO Evidence: Sources and How Much to Trust Them

> **Status:** Draft v0.1 · **Last verified:** 2026-11-18 · **Author:** [Saeed Yeganeh](https://saeedyeganeh.com/en/)

SEO advice is everywhere, and much of it contradicts itself. Before you can decide *what to do*, you need to know *where a claim comes from* and *how much weight it can carry*. This chapter is the foundation for the rest of the handbook. It explains the kinds of evidence people use to describe how Google Search works and what each kind can and cannot prove. It also introduces the labels used on every claim in later chapters.

---

## 1.1 Why the source of a claim matters more than the claim

Two experienced people can say opposite things about the same ranking question, and both can sound convincing. The fastest way to resolve the disagreement is not to judge who sounds more confident. Ask **what the claim rests on**:

- Is it something Google has written in its own documentation?
- Is it something a Google engineer said under oath?
- Is it a field name in leaked internal documentation?
- Is it an idea described in a patent?
- Is it a survey of practitioners, or one person's observation on one site?

Each of these is a different *kind* of evidence. Each has different strengths and different failure modes. Most bad SEO conclusions come from treating one kind of evidence as if it were another. A common example is reading a patent as proof that a system is live today. Another is reading a leaked field name as proof of how much weight it carries.

---

## 1.2 The six kinds of evidence

### 1. Official Google documentation  `Official`

**What it is:** Google Search Central documentation, the Search Central blog, the [ranking systems guide](https://developers.google.com/search/docs/appearance/ranking-systems-guide), spam policies, and public statements from Google's search representatives.

**What it can tell you:** what Google is willing to state publicly about how its systems behave, and what it recommends.

**Its limits:** it is written for a broad audience and is deliberately general. It rarely gives weights, thresholds or internal names. The precise wording matters. Statements that look contradictory often turn out to answer narrower questions than people assume (see [Worked example A](#worked-example-a-does-google-have-a-site-level-quality-signal)).

**How to use it:** quote the exact sentence, link the page, and record the date you read it, because documentation is revised.

### 2. Sworn testimony and court exhibits  `Testimony`

**What it is:** material from *United States et al. v. Google LLC* (D.D.C., No. 1:20-cv-03010). This includes trial transcripts and the exhibits the U.S. Department of Justice has published on [justice.gov](https://www.justice.gov/atr/us-and-plaintiff-states-v-google-llc-2020-remedies-hearing-exhibits).

**What it can tell you:** concrete descriptions of internal systems given by people who built or ran them, under legal accountability.

**Its limits:** testimony answers the questions lawyers asked, not the questions SEOs have. It may describe a system at one point in time. Not every exhibit is testimony, either. Some are *demonstratives* (slides summarising testimony) or *interview notes* taken by a party's legal team. Record which one you are citing.

**Example of the distinction:** the claim that NavBoost uses about 13 months of click data appears in two places:
- A DOJ demonstrative quotes Eric Lehman's trial testimony of 20 September 2023 (transcript 1805:6–13) in a question-and-answer form ([PXRD016](https://www.justice.gov/media/1398886/dl)).
- Interview notes from a 31 January 2025 call with Pandu Nayak state that NavBoost "uses most recent 13 months of data" ([PXR0357](https://www.justice.gov/atr/media/1398866/dl)).

Both are court exhibits, but only the first reflects sworn trial testimony. The second is notes taken during a call.

### 3. Leaked internal API documentation  `API Docs`

**What it is:** the Google *Content Warehouse* API reference. An automated process published it to a public GitHub repository in March 2024. A follow-up commit on 7 May 2024 attempted to remove it ([The Register](https://www.theregister.com/2024/05/29/internal_google_search_documents/); [Mike King](https://ipullrank.com/google-algo-leak)). It became widely known after reports by [Rand Fishkin](https://sparktoro.com/blog/an-anonymous-source-shared-thousands-of-leaked-google-search-api-documents-with-me-everyone-in-seo-should-see-them/) and [Mike King](https://ipullrank.com/google-algo-leak) on 27 May 2024. Google confirmed the documents were authentic. A spokesperson also cautioned against "inaccurate assumptions" drawn from "out-of-context, outdated, or incomplete information" ([Search Engine Journal](https://www.searchenginejournal.com/google-validates-leak-igniting-questions-around-search-transparency/518006/)).

**What it can tell you:** what data structures exist, what fields are called, and the short descriptions engineers wrote next to them. Sometimes it also tells you which system consumes a field.

**Its limits:**
- A field existing means the data is **defined** and possibly stored. It does **not** tell you that the field is used in ranking, how much weight it carries, or whether it is still in use.
- There is no code, no weights, no thresholds.
- Many fields are typed with `default: nil`. That means *no value unless set*, which is not the same as zero.
- Some fields are explicitly marked *deprecated* or *only for experiments* in their own description.

**How to use it:** cite the exact module and field, quote its description, and link the reference page and version you read (for example, [`CompressedQualitySignals` in package v0.4.0](https://hexdocs.pm/google_api_content_warehouse/0.4.0/GoogleApi.ContentWarehouse.V1.Model.CompressedQualitySignals.html)). Never cite a field from a third-party summary table without checking the original description. Simplified tables often attach meanings the documentation itself does not state.

### 4. Patents  `Patent`

**What it is:** patents and patent applications filed by Google, searchable on [Google Patents](https://patents.google.com/).

**What it can tell you:** how Google engineers *designed* a method to solve a problem, often in great detail.

**Its limits:** a patent shows that an idea was worth protecting, not that it runs in Search today. Google has repeated this point for more than a decade. Matt Cutts said in 2013 that holding a patent does not mean it is currently part of the algorithm ([Search Engine Land](https://searchengineland.com/googles-matt-cutts-holding-a-patent-doesnt-mean-we-use-that-patent-in-search-quality-157970)). John Mueller repeated it in 2021 ([Search Engine Journal](https://www.searchenginejournal.com/google-patents-are-not-always-used-in-search/395383/)). Patents are also written broadly on purpose, so their wording covers more than any one implementation.

**How to use it:** cite the patent number. Describe it as *"Google patented a method that…"*, never as *"Google does…"*, unless another kind of evidence confirms the system is in use.

### 5. Third-party reporting, studies and surveys  `Secondhand`

**What it is:** news coverage, conference write-ups, correlation studies, and surveys of SEO practitioners.

**What it can tell you:** what happened at an event you did not attend, what many experienced people believe, and patterns across many sites.

**Its limits:** reporting can mis-hear or simplify. Correlation studies cannot separate cause from effect. Surveys measure **consensus, not truth**. A ranking of "factors" by expert vote is a map of opinion.

**How to use it:** name the outlet or study, link it, and say it is secondhand. When a report quotes a primary source, go to that source.

### 6. Practitioner experience  `Experience`

**What it is:** observations from your own projects.

**What it can tell you:** what happened on a specific site, under specific conditions, at a specific time. Experience is often the first place new patterns are noticed.

**Its limits:** one site is a sample of one. Search systems change, sites differ, and many changes happen at once, so attributing a result to a single cause is hard.

**How to use it:** label it clearly, describe the conditions, and avoid generalising beyond them.

---

## 1.3 A quick comparison

| Evidence | Strongest at showing | Cannot show by itself | Label |
|---|---|---|---|
| Official documentation | What Google publicly states and recommends | Internal weights, thresholds, names | `Official` |
| Testimony and exhibits | How specific systems were described by insiders | Current state; anything not asked | `Testimony` |
| Leaked API docs | Which data fields exist and their short descriptions | Whether or how much a field affects ranking | `API Docs` |
| Patents | How a method was designed | That it is used in Search today | `Patent` |
| Reporting, studies, surveys | Events, broad patterns, expert consensus | Causation; Google's internal reality | `Secondhand` |
| Experience | What happened on one site | That it generalises | `Experience` |

This table is a reading guide, not a scoring formula. A precise `Official` sentence beats a vague `Testimony` paraphrase. A well-documented `API Docs` field beats a loosely worded patent. Always judge the specific source in front of you.

In addition, the handbook uses **`Inference`** for conclusions drawn *from* evidence that the evidence does not state directly. Inference is necessary and useful, but it must never be presented as a fact.

---

## 1.4 Worked examples

### Worked example A: Does Google have a site-level quality signal?

This question shows how different evidence types fit together, and why careful wording matters.

1. **`Official`** — Google's ranking systems guide says its systems are designed to work at the page level, and that "site-wide signals and classifiers are also used" ([ranking systems guide](https://developers.google.com/search/docs/appearance/ranking-systems-guide)).
2. **`Official`** — Asked about "domain authority", John Mueller said in a 2018 Reddit AMA that Google does not use it. He added that Google tries to keep metrics granular but sometimes looks "a bit broader" ([Search Engine Journal summary](https://www.searchenginejournal.com/ranking-factors/domain-authority-ranking-factor/)). In context, "Domain Authority" is the name of a Moz metric.
3. **`API Docs`** — The leaked `CompressedQualitySignals` module includes a field `siteAuthority`. Its description says it is converted from `quality_nsr.SiteAuthority` and "applied in Qstar" ([v0.4.0 reference](https://hexdocs.pm/google_api_content_warehouse/0.4.0/GoogleApi.ContentWarehouse.V1.Model.CompressedQualitySignals.html)).

**What we can say:** Google publicly acknowledges site-wide signals. Internal documentation defines a site-level field named `siteAuthority` that is used by a quality component. Google's denials of "domain authority" are consistent with this if they refer to the third-party metric of that name.

**What we cannot say:** how `siteAuthority` is computed, whether links feed into it, how much it weighs, or whether it works like any SEO tool's score. Claims that go further are `Inference` and should be labelled that way.

### Worked example B: Do quality raters change rankings?

- **`Official`** — When Google updated its Search Quality Rater Guidelines in November 2023, it repeated that raters' ratings "don't directly influence ranking". Raters help evaluate how well ranking systems perform ([Search Central blog](https://developers.google.com/search/blog/2023/11/search-quality-rater-guidelines-update)).

**What we can say:** a rater scoring your page does not move your page. The guidelines describe what Google's systems are *aiming for*, so they are a useful lens on quality.

**What we cannot say:** that any concept in the guidelines maps one-to-one onto a ranking signal.

### Worked example C: Reading a leaked field correctly

Take `exactMatchDomainDemotion` from the same module. The documentation describes it as a page quality signal converted from `QualityBoost.emd.boost`. Separately, Google's public ranking systems guide describes an *exact match domain system* that avoids giving too much credit to domains built to match queries.

**What we can say:** both an internal field and a public statement describe the same idea. This is a good case of `API Docs` and `Official` evidence agreeing.

**What we cannot say:** how large the demotion is, or which domains trigger it.

---

## 1.5 How every claim is cited in this handbook

Each factual claim in later chapters carries:

1. **A label:** `Official`, `Testimony`, `API Docs`, `Patent`, `Secondhand`, `Experience` or `Inference`.
2. **A link to the primary source.** If the claim comes through a secondary source, that source is linked too.
3. **A locator** where possible: the transcript page and line, the exhibit number, the field name and package version, the patent number, or the documentation section.
4. **An entry in [`sources/claims.yml`](../sources/claims.yml)** with the date the source was checked.

If a claim cannot be traced to a source, it is removed or labelled `Inference`.

---

## 1.6 A checklist before you believe an SEO claim

- [ ] What kind of evidence is this? Can I name the original source, not a summary of it?
- [ ] Does the source say *this exactly*, or is someone drawing a conclusion from it?
- [ ] If it is a patent, is there separate evidence that the method is used?
- [ ] If it is a leaked field, have I read its own description, type, default and deprecation notes?
- [ ] If it is testimony, is it sworn testimony, a demonstrative, or interview notes? From what date?
- [ ] If it is official documentation, what exactly does the sentence cover, and when was the page last updated?
- [ ] If it is a survey or experience, am I treating it as opinion or one case, rather than proof?

---

## Sources for this chapter

| # | Source | Type | Checked |
|---|---|---|---|
| 1 | Google Search Central — [A guide to Google Search ranking systems](https://developers.google.com/search/docs/appearance/ranking-systems-guide) | Official | 2026-11-18 |
| 2 | Google Search Central Blog — [Search Quality Rater Guidelines update (Nov 2023)](https://developers.google.com/search/blog/2023/11/search-quality-rater-guidelines-update) | Official | 2026-11-18 |
| 3 | U.S. DOJ — [PXRD016, demonstrative citing Eric Lehman trial testimony](https://www.justice.gov/media/1398886/dl) | Testimony | 2026-11-18 |
| 4 | U.S. DOJ — [PXR0357, interview notes with Pandu Nayak, 31 Jan 2025](https://www.justice.gov/atr/media/1398866/dl) | Testimony (exhibit) | 2026-11-18 |
| 5 | HexDocs — [`CompressedQualitySignals`, google_api_content_warehouse v0.4.0](https://hexdocs.pm/google_api_content_warehouse/0.4.0/GoogleApi.ContentWarehouse.V1.Model.CompressedQualitySignals.html) | API Docs | 2026-11-18 |
| 6 | The Register — [Internal Google Search documents (29 May 2024)](https://www.theregister.com/2024/05/29/internal_google_search_documents/) | Secondhand | 2026-11-18 |
| 7 | Search Engine Journal — [Google validates leak (statement to The Verge)](https://www.searchenginejournal.com/google-validates-leak-igniting-questions-around-search-transparency/518006/) | Secondhand | 2026-11-18 |
| 8 | SparkToro — [Rand Fishkin, original leak report (27 May 2024)](https://sparktoro.com/blog/an-anonymous-source-shared-thousands-of-leaked-google-search-api-documents-with-me-everyone-in-seo-should-see-them/) | Secondhand | 2026-11-18 |
| 9 | iPullRank — [Mike King, "Secrets from the Algorithm" (27 May 2024)](https://ipullrank.com/google-algo-leak) | Secondhand | 2026-11-18 |
| 10 | Search Engine Land — [Matt Cutts on patents (2013)](https://searchengineland.com/googles-matt-cutts-holding-a-patent-doesnt-mean-we-use-that-patent-in-search-quality-157970) | Secondhand | 2026-11-18 |
| 11 | Search Engine Journal — [Mueller: patents not always used in Search (2021)](https://www.searchenginejournal.com/google-patents-are-not-always-used-in-search/395383/) | Secondhand | 2026-11-18 |
| 12 | Search Engine Journal — [Domain authority as a ranking factor (Mueller quotes)](https://www.searchenginejournal.com/ranking-factors/domain-authority-ranking-factor/) | Secondhand | 2026-11-18 |

---

*Next chapter (planned): How Google Search works end to end — discovery, crawling, indexing, ranking and serving.*
