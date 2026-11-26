# Chapter 12 — Technical SEO

> **Status:** Draft v0.1 · **Last verified:** 2026-11-26 · **Author:** [Saeed Yeganeh](https://saeedyeganeh.com/en/)

Technical SEO is where myths do the most damage, because the work looks precise. A score turns green, a warning disappears, and it feels like rankings must follow. Google's documentation draws a clearer line. Some technical conditions decide whether a page can be in Search at all. Others are part of page experience, which Google says matters but does not outweigh relevance.

This chapter sets out what Google documents about the minimum technical requirements, status codes, robots.txt and `noindex`, mobile-first indexing, and page experience. [Chapter 2](02-how-search-works.md) covered crawling, rendering, canonicalisation and crawl budget. This chapter does not repeat that material.

---

## 12.1 The minimum: what a page needs to be indexed

Google's Search Essentials list three technical requirements for a page to be eligible for indexing `Official` ([Google Search technical requirements](https://developers.google.com/search/docs/essentials/technical?authuser=1), last updated 2025-12-18):

1. Googlebot is not blocked.
2. The page works, meaning Google receives an HTTP 200 (success) status code.
3. The page has indexable content: text in a supported file type that does not break the spam policies.

The page says meeting these requirements does not guarantee indexing. It also says client and server error pages are not indexed `Official` (same page).

**What we can say:** these three conditions are a floor. A page that fails one of them will not be indexed, whatever its content.

**What we cannot say:** that a page meeting them will be indexed or rank. The same page states the opposite.

---

## 12.2 Status codes and what they tell Google

Google's documentation on HTTP status codes explains how each class affects crawling and indexing `Official` ([How HTTP status codes affect Google's crawlers](https://developers.google.com/search/docs/crawling-indexing/http-network-errors?authuser=2), last updated 2026-02-04):

| Status | What the documentation says |
|---|---|
| 2xx | Does not guarantee indexing. A 2xx page that looks like an error page is reported as a soft 404 |
| 301, 308 | A strong signal that the redirect target should be processed |
| 302, 307 | A weak signal that the redirect target should be processed |
| 404, 410 | Treated the same way. Not indexed; already-indexed URLs are removed over time and crawled less often |
| 429 | Treated as a server error and a sign the server is overloaded |
| 5xx | Crawling slows. Indexed URLs are kept for a while but eventually dropped if errors persist |

Further points from the same page `Official` (same page):

- Googlebot follows up to 10 redirect hops.
- Sites should not use 401 or 403 to limit crawl rate.
- After a server recovers and returns 2xx again, the crawl rate recovers gradually.

The page gives no fixed number of days before a 4xx or 5xx page leaves the index.

**What we can say:** status codes are instructions Google takes seriously. Permanent and temporary redirects send different strengths of signal. Errors reduce crawling and can remove pages from the index.

`Inference`: use 301 or 308 for permanent moves, so the strong signal matches your intent. Do not return 200 for pages that are really errors; Google may treat them as soft 404s anyway, and the mixed signal can hide real problems in reports.

---

## 12.3 robots.txt is not `noindex`

Google's introduction to robots.txt says the file tells crawlers which URLs they can access. It is used mainly to avoid overloading a site with requests `Official` ([Introduction to robots.txt](https://developers.google.com/search/docs/advanced/robots), last updated 2025-12-10).

The same page says robots.txt "is not a mechanism for keeping a web page out of Google" `Official` (same page). A page blocked by robots.txt can still appear in search results, without a description. To keep a page out, Google says to use `noindex` or password-protect the page `Official` (same page).

The technical requirements page makes the same point. Blocking by robots.txt prevents crawling, but the URL can still appear. To keep a page out of the index, use `noindex` and allow crawling, so Google can see the `noindex` `Official` ([technical requirements](https://developers.google.com/search/docs/essentials/technical?authuser=1)).

**What we can say:** robots.txt controls crawling; `noindex` controls indexing. Blocking a page in robots.txt *and* adding `noindex` defeats the `noindex`, because Google cannot crawl the page to read it.

[Chapter 9](09-titles-and-snippets.md), section 9.4, shows a side effect: when Google cannot crawl a page, it may build the title link from anchor text on other pages.

---

## 12.4 Mobile-first indexing

Google's mobile documentation says Google uses the mobile version of a site's content, crawled with the smartphone agent, for indexing and ranking. Google calls this mobile-first indexing `Official` ([Mobile site and mobile-first indexing best practices](https://developers.google.com/search/mobile-sites/faq), last updated 2025-12-10).

The page recommends responsive design. It says a mobile version is very strongly recommended but not required for a site to be included in Search `Official` (same page).

Its best practices include `Official` (same page):

- The mobile site should contain the same content as the desktop site.
- Structured data should be the same on mobile and desktop.
- Titles and meta descriptions should be equivalent across both versions.
- Robots meta tags should be the same on both.
- Primary content should not be lazy-loaded only when a user interacts with the page.

**What we can say:** for indexing, the mobile page *is* the page. Content, links, markup or metadata that exist only on desktop may be missed.

**What we cannot say:** the current rollout status. The part of the page read verbatim did not state it, so this chapter makes no claim about it.

---

## 12.5 Page experience and Core Web Vitals

### What Google says about ranking

Google's page experience documentation says Core Web Vitals are used by its ranking systems `Official` ([Understanding page experience](https://developers.google.com/search/docs/guides/page-experience?authuser=8), last updated 2026-09-22). The same page qualifies this `Official` (same page):

- Good Core Web Vitals do not guarantee top rankings.
- Other aspects of page experience do not directly help a site rank higher.
- There is no single page experience signal.
- Google always seeks to show the most relevant content, even if its page experience is below par.
- Chasing a perfect score only for SEO reasons may not be the best use of time.
- Google generally evaluates content page by page, with some site-wide assessments.

The page offers self-check questions. Among them: whether pages are served securely, display well on mobile devices, and avoid intrusive interstitials `Official` (same page).

### The three Core Web Vitals

Google's Core Web Vitals page defines the "good" thresholds `Official` ([Understanding Core Web Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals), last updated 2025-12-10):

| Metric | Measures | Good |
|---|---|---|
| Largest Contentful Paint (LCP) | Loading | Within 2.5 seconds of the page starting to load |
| Interaction to Next Paint (INP) | Responsiveness | Under 200 milliseconds |
| Cumulative Layout Shift (CLS) | Visual stability | Under 0.1 |

The page says good Core Web Vitals, with other page experience aspects, align with what Google's core ranking systems seek to reward, and Google highly recommends achieving them `Official` (same page).

**What we can say:** Core Web Vitals are a confirmed ranking input. Google also says relevance comes first, and that there is no single page experience score.

**What we cannot say:**

- how much Core Web Vitals weigh, or whether they act as a tie-breaker. The documentation gives no weight;
- that moving from "needs improvement" to "good" will lift rankings by a measurable amount;
- that HTTPS, mobile display or interstitials are separate ranking signals. The current page presents them as self-check questions, not as named signals.

`Inference`: fix Core Web Vitals that are poor, because they affect users and are a stated ranking input. Do not trade content or relevance work for small gains on metrics that already pass.

---

## 12.6 What technical SEO can and cannot do

| Technical issue | What it can do | Evidence |
|---|---|---|
| Blocked crawling, non-200 status, no indexable content | Keep a page out of the index entirely | `Official` (section 12.1) |
| Wrong redirect type | Send a weaker canonical signal than intended | `Official` (section 12.2) |
| Persistent errors | Reduce crawling and remove pages over time | `Official` (section 12.2) |
| robots.txt used instead of `noindex` | Leave a URL in results without a description | `Official` (section 12.3) |
| Content missing on mobile | Leave that content out of indexing | `Official` (section 12.4) |
| Poor Core Web Vitals | Count against a page as one input among many | `Official` (section 12.5) |
| Perfect scores | No guaranteed gain | `Official` (section 12.5) |

`Inference`: technical SEO mostly removes obstacles. It decides whether relevance and quality can be seen. It rarely creates them.

---

## 12.7 Checklist: technical health

- [ ] **Confirm the three minimum requirements** for important pages: not blocked, HTTP 200, indexable content `Official` (section 12.1).
- [ ] **Use 301 or 308 for permanent moves,** and keep redirect chains short `Official`, `Inference` (section 12.2).
- [ ] **Return real 404 or 410 codes for missing pages,** not a 200 with an error message `Official` (section 12.2).
- [ ] **Watch for 5xx and 429 spikes.** They slow crawling and can drop pages `Official` (section 12.2).
- [ ] **Use `noindex`, not robots.txt, to keep pages out,** and leave those pages crawlable `Official` (section 12.3).
- [ ] **Check the mobile version:** same content, structured data, titles, descriptions and robots tags as desktop `Official` (section 12.4).
- [ ] **Bring poor Core Web Vitals to "good":** LCP within 2.5 s, INP under 200 ms, CLS under 0.1 `Official` (section 12.5).
- [ ] **Stop at "good".** Perfect scores for SEO alone may not be worth the time `Official` (section 12.5).

---

## Sources for this chapter

| # | Source | Type | Checked |
|---|---|---|---|
| 1 | Google Search Central — [Google Search technical requirements](https://developers.google.com/search/docs/essentials/technical?authuser=1) (last updated 2025-12-18) | Official | 2026-11-26 |
| 2 | Google Search Central — [How HTTP status codes, and network and DNS errors affect Google Search](https://developers.google.com/search/docs/crawling-indexing/http-network-errors?authuser=2) (last updated 2026-02-04) | Official | 2026-11-26 |
| 3 | Google Search Central — [Introduction to robots.txt](https://developers.google.com/search/docs/advanced/robots) (last updated 2025-12-10) | Official | 2026-11-26 |
| 4 | Google Search Central — [Mobile site and mobile-first indexing best practices](https://developers.google.com/search/mobile-sites/faq) (last updated 2025-12-10) | Official | 2026-11-26 |
| 5 | Google Search Central — [Understanding page experience in Google Search results](https://developers.google.com/search/docs/guides/page-experience?authuser=8) (last updated 2026-09-22) | Official | 2026-11-26 |
| 6 | Google Search Central — [Understanding Core Web Vitals and Google search results](https://developers.google.com/search/docs/appearance/core-web-vitals) (last updated 2025-12-10) | Official | 2026-11-26 |

Notes on this check: all six pages were read directly. Several redirect to newer canonical addresses; the links above are the addresses checked. The mobile-first page was read verbatim only in part; claims come from the part read verbatim, and no claim is made about rollout status. This chapter uses no leaked API fields or patents.

---

<a id="next-chapter"></a>*Next chapter (planned): Timing, updates and recovery — what Google says about core updates, how long changes take, and what recovery looks like.*
