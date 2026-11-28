# Chapter 11 — Sensitive (YMYL) Topics

> **Status:** Draft v0.1 · **Last verified:** 2026-11-26 · **Author:** [Saeed Yeganeh](https://saeedyeganeh.com/en/)

"YMYL" is one of the most quoted terms in SEO. It stands for "Your Money or Your Life", and it describes topics where a bad page can hurt someone. Much SEO writing treats YMYL as a ranking category with its own penalty. Google's documents describe something narrower: a standard used by human raters, and a statement that ranking systems give more weight to trust signals on these topics.

This chapter sets out what the Search Quality Rater Guidelines say about YMYL, what Google's public guidance adds, and what we cannot conclude. [Chapter 4](04-content-quality-originality-effort.md) introduced E-E-A-T and the rater guidelines overview. This chapter applies them to sensitive topics.

---

## 11.1 Where the term comes from

YMYL is defined in Google's Search Quality Rater Guidelines. The version checked for this chapter is dated 11 September 2025 `Official` ([Search Quality Rater Guidelines](https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf), p. 1). Section 2.3 is titled "Your Money or Your Life (YMYL) Topics" `Official` (same document, p. 11).

As [Chapter 1](01-reading-seo-evidence.md) explained, raters do not change rankings. Google says their ratings are used to evaluate how well its systems work ([Search Central blog, Nov 2023](https://developers.google.com/search/blog/2023/11/search-quality-rater-guidelines-update)). The guidelines show what Google's systems aim for, not how they compute it.

---

## 11.2 What counts as YMYL

The guidelines describe YMYL topics as those that could significantly affect people's health, financial stability or safety, or the welfare or well-being of society `Official` ([Rater Guidelines](https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf), p. 11).

They name four kinds of harm `Official` (same document, pp. 11–12):

- YMYL Health or Safety
- YMYL Financial Security
- YMYL Government, Civics & Society, which includes election and voting information and trust in public institutions
- YMYL Other

### What changed in September 2025

Search Engine Roundtable reported that the 11 September 2025 update listed "Updated YMYL definitions" in its change log. It said the old category "YMYL Society" became "YMYL Government, Civics & Society", with election and voting information added `Secondhand` ([Search Engine Roundtable, 12 Sep 2025](https://www.seroundtable.com/google-ads-related-searches-based-on-your-browsing-40092.html)). The new category name and the election wording match the guidelines' own text on page 11 `Official` ([Rater Guidelines](https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf), p. 11). The same report said the update also added examples involving AI Overviews `Secondhand` (same article).

---

## 11.3 YMYL is a spectrum, not a label

The guidelines do not treat YMYL as on or off. They describe topics as clearly YMYL, clearly not YMYL, or somewhere in between `Official` ([Rater Guidelines](https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf), pp. 11–12).

To decide, raters are asked to consider two kinds of question `Official` (same document, p. 11):

- Would a careful person look for expert sources or highly trustworthy information on this topic?
- Or would most people be content to ask friends casually about it?

Page 12 has a table of examples sorted into clear YMYL, may be YMYL, and not or unlikely YMYL. The examples range from emergency information, such as tsunami evacuation, to everyday matters, such as when to replace a toothbrush or which pencils to buy `Official` (same document, p. 12).

**What we can say:** in Google's rater framework, YMYL depends on how much harm a wrong answer could do. It is not a fixed list of industries. A finance site can publish non-YMYL pages, and a hobby site can publish a YMYL one.

**What we cannot say:** that Google's ranking systems classify topics on this same three-level scale. The scale is written for human raters.

---

## 11.4 The higher standard for YMYL pages

The guidelines say Google has very high Page Quality rating standards for pages on clear YMYL topics `Official` ([Rater Guidelines](https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf), p. 11). A later table repeats that YMYL pages have higher standards than non-YMYL pages `Official` (same document, p. 19).

Three further points from the guidelines `Official` (same document):

- Trust is "the most important member of the E-E-A-T family" (p. 27).
- Informational pages on clear YMYL topics must be accurate to prevent harm to people and society (p. 27).
- Pages that need a high level of trust, such as medical sites or news coverage of major civic issues, deserve special scrutiny (p. 29).

Google's November 2023 overview of the guidelines makes the same point more briefly. It says raters apply very high Page Quality standards to pages on YMYL topics, and it uses a flu-symptoms page as a YMYL example `Official` ([Rater Guidelines overview](https://services.google.com/fh/files/misc/hsw-sqrg.pdf), pp. 25–26).

### Experience or expertise?

Section 3.4.1 of the guidelines is titled "YMYL Topics: Experience or Expertise?" `Official` ([Rater Guidelines](https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf), p. 28). It sets out, through a table of examples, when first-hand experience is useful and when expert information is needed. For a "how to vote" topic, the expert column lists matters such as eligibility and voter registration `Official` (same document, p. 28).

`Inference`: on YMYL topics, personal experience can add value, but it cannot replace accurate expert information where facts or rules decide the outcome. A page that shares experience about a medical condition, for example, is different from a page that gives dosage advice.

---

## 11.5 What Google says about ranking

Google's public guidance on helpful content links the rater concept to its ranking systems `Official` ([Creating helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content), last updated 2026-10-05):

- Its systems give even more weight to content that aligns with strong E-E-A-T for topics that could significantly affect people's health, financial stability or safety, or the welfare of society. The page calls these YMYL topics.
- Of the E-E-A-T aspects, trust is the most important.
- E-E-A-T itself is not a specific ranking factor.
- Rater data is not used directly in its ranking algorithms.

**What we can say:** Google publicly states that on YMYL topics its systems lean harder on signals associated with trust and E-E-A-T. This is a direct `Official` statement, not an inference from the rater guidelines.

**What we cannot say:**

- which signals make up "strong E-E-A-T" for ranking purposes;
- how Google's systems decide that a query or page is YMYL;
- how much extra weight applies.

---

## 11.6 What the leaked API documentation shows

SEO commentary often names YMYL-related fields from the 2024 leak. This handbook checked the `CompressedQualitySignals` module in package v0.4.0. It contains no field whose name includes "ymyl" `API Docs` ([v0.4.0 reference](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.CompressedQualitySignals.html)). Other modules were not checked for this chapter.

[Chapter 7](07-site-level-quality-signals.md), section 7.7, lists two site-level flags from the `QualityNsrNsrData` module: `isElectionAuthority` and `isCovidLocalAuthority`. Both relate to topics that the rater guidelines treat as YMYL.

**What we can say:** internal documentation defines site-level flags for authority on at least two sensitive topics, elections and COVID-19.

**What we cannot say:** that a general "YMYL score" exists, what it would measure, or how it is used. Any such claim needs a field name, module and description, which this chapter has not verified.

---

## 11.7 Common misreadings

| Claim often made | What the evidence supports |
|---|---|
| "YMYL sites get a penalty." | No source describes a YMYL penalty. Google says it gives *more weight* to trust signals on these topics (section 11.5). |
| "Only medical and finance sites are YMYL." | The guidelines name four kinds of harm, including civic and election topics, and treat YMYL as a spectrum (sections 11.2, 11.3). |
| "Raters downgrade YMYL pages in rankings." | Raters do not change rankings (section 11.1). |
| "E-E-A-T is a YMYL ranking factor." | Google says E-E-A-T is not a specific ranking factor (section 11.5). |
| "Author bios fix YMYL rankings." | No source in this chapter says that. Trust and accuracy are the stated priorities `Inference`. |

---

## 11.8 Putting it together

| Question | Best evidence | Label | Strength |
|---|---|---|---|
| What is YMYL? | Rater Guidelines §2.3 (Sept 2025) | `Official` | Direct definition; four kinds of harm |
| Is YMYL binary? | Rater Guidelines pp. 11–12 | `Official` | No; a spectrum with examples |
| Are election topics YMYL? | Rater Guidelines p. 11; SERoundtable | `Official`, `Secondhand` | Yes, explicitly since Sept 2025 |
| Do YMYL pages face higher standards? | Rater Guidelines pp. 11, 19; overview p. 25 | `Official` | Yes, for raters |
| Do ranking systems treat YMYL differently? | Creating helpful content | `Official` | More weight on E-E-A-T; details unstated |
| Is there a YMYL field in the leak? | `CompressedQualitySignals` | `API Docs` | None found in that module |

---

## 11.9 Checklist: publishing on sensitive topics

- [ ] **Place each page on the spectrum.** Ask whether a careful person would want expert sources for it `Official` (section 11.3).
- [ ] **Make accuracy the first priority.** Clear YMYL pages must be accurate to prevent harm `Official` (section 11.4).
- [ ] **Show why the page can be trusted.** Who wrote or reviewed it, what sources it rests on, and when it was checked `Inference` (sections 11.4, 11.5).
- [ ] **Separate experience from expertise.** Label personal accounts as such, and use expert sources for facts and rules `Official`, `Inference` (section 11.4).
- [ ] **Treat civic and election information as YMYL** `Official` (section 11.2).
- [ ] **Keep sensitive pages current.** Outdated health, financial or voting information can cause harm. [Chapter 10](10-freshness.md) covers dates `Inference`.
- [ ] **Do not chase a "YMYL score".** No source here verifies one `API Docs` (section 11.6).

---

## Sources for this chapter

| # | Source | Type | Checked |
|---|---|---|---|
| 1 | Google — [Search Quality Rater Guidelines](https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf) (version of 11 Sep 2025), §2.3 and pp. 11–29 | Official | 2026-11-26 |
| 2 | Google — [Search Quality Rater Guidelines: An Overview](https://services.google.com/fh/files/misc/hsw-sqrg.pdf) (Nov 2023), pp. 25–26 | Official | 2026-11-26 |
| 3 | Google Search Central — [Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) (last updated 2026-10-05) | Official | 2026-11-26 |
| 4 | Google Search Central Blog — [Search Quality Rater Guidelines update (Nov 2023)](https://developers.google.com/search/blog/2023/11/search-quality-rater-guidelines-update) | Official | 2026-11-18 (via Chapter 1) |
| 5 | Search Engine Roundtable — [Google Search Quality Raters Guidelines gains AI Overview and YMYL definitions](https://www.seroundtable.com/google-ads-related-searches-based-on-your-browsing-40092.html) (Barry Schwartz, 12 Sep 2025) | Secondhand | 2026-11-26 |
| 6 | HexDocs — [`CompressedQualitySignals`, v0.4.0](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.CompressedQualitySignals.html) | API Docs | 2026-11-26 |

Notes on this check: pages 1–29 of the full guidelines were read as text; later pages were not, so claims about the Lowest rating for YMYL pages are left out. The guidelines' example table on page 12 did not extract cleanly, so only examples whose placement is clear are described. Google's "How Search works" ranking page could not be fetched on this date and is not cited. Source 4 is cited from Chapter 1. Source 5's URL slug does not match its title; it resolves to the article named here.

---

<a id="next-chapter"></a>*Next chapter (planned): Technical SEO — what Google documents about crawlability, indexing controls, page experience and JavaScript.*
