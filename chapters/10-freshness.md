# Chapter 10 — Freshness

> **Status:** Draft v0.1 · **Last verified:** 2026-11-26 · **Author:** [Saeed Yeganeh](https://saeedyeganeh.com/en/)

"Update your content to rank better" is common SEO advice. It mixes up two separate ideas. One is that some queries need recent results. The other is that a newer date on any page is a ranking advantage. Google's public record supports the first idea, and it warns against acting on the second.

This chapter covers what Google says about freshness systems, how Google decides what date a page has, what the leaked API documentation shows about dates, and what Google representatives have said about changing dates. [Chapter 4](04-content-quality-originality-effort.md) covered "fake freshness" as a warning sign of low-effort content. This chapter covers the mechanics behind it.

---

## 10.1 What Google says: freshness depends on the query

Google's ranking systems guide has a short section headed "Freshness systems" `Official` ([ranking systems guide](https://developers.google.com/search/docs/appearance/ranking-systems-guide)). It says Google has various "query deserves freshness" systems. They are designed to show fresher content for queries where people would expect it `Official` (same page).

The guide gives two examples `Official` (same page):

- Someone searching for a film that has just been released probably wants recent reviews, not articles from when production began.
- A search for "earthquake" normally returns material about preparing for earthquakes. If an earthquake has just happened, news and fresher content may appear instead.

The page was last updated on 2025-12-10.

**What we can say:** Google publicly describes freshness as a property of the *query* and the moment, not of every page. The same word, "earthquake", can call for old or new content depending on events.

**What we cannot say:** how Google detects that a query needs fresh results, or how much freshness weighs against other signals once it does. The guide gives examples, not mechanics.

[Chapter 3](03-relevance-and-search-intent.md) covered how Google reads query intent. Freshness is one part of that: the same query can have a different intent on a different day.

---

## 10.2 The 2011 freshness update

The fullest public description of freshness comes from 2011. On 3 November 2011 Amit Singhal, then a Google Fellow, announced a ranking change aimed at fresher results `Official` ([Inside Search blog](https://search.googleblog.com/2011/11/giving-you-fresher-more-recent-search.html)).

The post said the change affected roughly 35 percent of searches `Official` (same page). An update to the post, dated 7 November 2011, clarified the number. It meant that at least one result on the page changed. The post said the change *noticeably* affected 6 to 10 percent of searches, depending on language and domain `Official` (same page).

The post described three kinds of searches that benefit from fresher results `Official` (same page):

| Kind of search | Examples given in the post |
|---|---|
| Recent events or hot topics | A protest in the news; a sports league lockout |
| Regularly recurring events | An annual conference; an election; sports scores; company earnings |
| Frequent updates | Product research, such as the best cameras or reviews of a car model |

The post linked the change to Caffeine, the web indexing system Google said it had completed the year before. It said Caffeine lets Google crawl and index fresh content quickly and at large scale `Official` (same page).

**What we can say:** in 2011 Google described freshness as a set of query types, and tied it to its ability to index new content quickly. The 35% figure counts any change on a results page, not a large change.

**What we cannot say:** that the 2011 system works the same way today. The post describes Search fifteen years ago. The current ranking systems guide confirms that freshness systems exist, but it does not repeat the three categories (section 10.1).

`Inference`: the 2011 categories are still a useful way to ask whether a query is time-sensitive. A product-review query and an annual-event query both have a natural "use-by date". An evergreen how-to query may not.

---

## 10.3 How Google decides what date a page has

Google's documentation on byline dates explains how Google estimates when a page was published or last updated `Official` ([Influence your byline dates](https://developers.google.com/search/docs/appearance/publication-dates)). The page was last updated on 2025-12-10.

It says Google does not rely on a single date factor, because every factor can be wrong. Its systems look at several factors to estimate when a page was published or significantly updated `Official` (same page). Google may show that date in results when it is useful to users, but it does not guarantee to show one `Official` (same page).

The page gives two ways to help `Official` (same page):

1. **A visible date.** Show a date prominently on the page, with a label such as "Published" or "Last updated". You can show a publication date, an update date, or both.
2. **Structured data.** Use `datePublished` and `dateModified` in the markup of a `CreativeWork` type, such as `Article`, `BlogPosting` or `VideoObject`.

It also lists best practices `Official` (same page):

- A date is required; a time is optional but recommended.
- If you give a time zone, it must be correct, including daylight saving time.
- The visible date and the structured data date should match.
- Do not use a future date, or the date of an event the page describes. Use event markup for events.
- If Google picks the wrong date, reduce the number of other dates on the page.

**What we can say:** Google estimates a page's date from several signals and wants the visible and marked-up dates to agree. Its stated aim is the date a page was published or *significantly* updated.

**What we cannot say:** which factors Google trusts most, or what counts as a "significant" update. The page does not define either.

---

## 10.4 Changing dates without changing content

The byline page itself does not discuss changing a date without changing the page. Google has addressed it elsewhere.

- **`Official`** — Google's guidance on helpful content lists, among warning signs, changing the dates of pages to make them look fresh when the content has not really changed. [Chapter 4](04-content-quality-originality-effort.md), section 4.2, covers this list ([Creating helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)).
- **`Secondhand`** — Search Engine Journal reported that in a Search Central SEO hangout recorded on 1 April 2021, John Mueller said updating a date without significant changes would not change anything for search. He advised updating the date only after significant changes. He said it was fine if a CMS changes dates automatically and the site cannot control it ([Search Engine Journal, 7 Apr 2021](https://www.searchenginejournal.com/googles-john-mueller-changing-dates-on-pages-wont-improve-rankings/)).

**What we can say:** Google has said in its guidance and through a representative that a new date alone is not a freshness signal worth chasing. Its date estimate aims at significant updates (section 10.3).

**What we cannot say:** whether changing dates is ever penalised. The sources describe it as unhelpful and as a warning sign, not as a spam violation with a stated penalty.

---

## 10.5 What the leaked API documentation shows about dates

The Content Warehouse reference contains a family of modules whose names begin with `QualityTimebased`. As [Chapter 1](01-reading-seo-evidence.md) explained, these show which data is defined, not how it is weighted.

### `QualityTimebasedSyntacticDate`

This module has no prose description `API Docs` ([v0.4.0 reference](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.QualityTimebasedSyntacticDate.html)). Selected fields, with what their own descriptions say `API Docs` (same page):

| Field | What its description says |
|---|---|
| `date` | Seconds since 1970; may be negative for older dates, such as newspaper archives |
| `bylineDate` | Set only when the byline date differs from `date`, for example when it falls within 24 hours of the crawl time, or is off because of time zones |
| `useAsBylineDate` | Whether the date is good to display as the snippet's byline date |
| `info` | Bit flags, including a high-confidence byline, and a high-confidence byline without support from content age |
| `trustSyntacticDateInRanking` | Set when the date is believed to be high-confidence but does not qualify as a byline date |
| `syntacticDateNotForRestrict` | If true, the date should not be used in date restricts |
| `timeZoneOffsetSeconds`, `fromExplicitTimeZone` | The time zone offset applied to get a UTC date; whether the source had an explicit time zone |

The description of `bylineDate` also notes that the syntactic date is never later than the crawl time `API Docs` (same page).

### `QualityTimebasedLastSignificantUpdate`

This module also has no prose description `API Docs` ([v0.4.0 reference](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.QualityTimebasedLastSignificantUpdate.html)). Its fields `API Docs` (same page):

- `date` — the timestamp of the last significant update. The description says it comes from a newer signal ("LSU Selector V2") when that is enabled, and otherwise falls back to an older one.
- `source` — the source the signal comes from.
- `adjustmentInfo` — stored only for debugging.
- `dateUnreliabilityInfo` — no description.

### Reading these fields correctly

**What we can say:**

- Google's internal documentation separates a date found in a page's text (a "syntactic" date) from a date it is willing to *display* as a byline. This matches the public statement that Google may or may not show a byline date (section 10.3). Here `API Docs` and `Official` agree.
- The documentation tracks how confident it is in a date, and whether that confidence is supported by the content's age.
- It defines a "last significant update" date. This matches the public wording about pages being "significantly updated". Again, `API Docs` and `Official` point the same way.
- At least one field refers to ranking: `trustSyntacticDateInRanking`.

**What we cannot say:**

- what makes an update "significant" to the LSU signal;
- how dates feed ranking, or how much they weigh;
- whether these fields were in use when the documentation leaked, or now.

`Inference`: the fields `info` and `dateUnreliabilityInfo` suggest Google checks a page's claimed date against other evidence, such as content age. Together with Google's public warnings (section 10.4), this fits the view that changing a visible date alone is unlikely to make a page look new to Google's systems.

---

## 10.6 Freshness and crawling

A page can only be shown as fresh once Google has crawled the new version.

- **`Official`** — The 2011 post tied fresher results to Caffeine, which it said allowed fast crawling and indexing of fresh content at scale ([Inside Search blog](https://search.googleblog.com/2011/11/giving-you-fresher-more-recent-search.html)).
- [Chapter 2](02-how-search-works.md), section 2.3, covers how Google decides what to crawl and how often, including its crawl budget documentation.

`Inference`: for time-sensitive content, the practical bottleneck is often discovery and recrawling, not ranking. Clear internal links to new pages and accurate sitemaps help Google find updates. Chapter 12 covers technical SEO.

---

## 10.7 Putting it together

| Question | Best evidence | Label | Strength |
|---|---|---|---|
| Does Google favour fresh content for some queries? | Ranking systems guide | `Official` | Direct statement, current |
| Which queries? | 2011 freshness post; ranking systems guide examples | `Official` | Examples only; 2011 categories may be dated |
| How many searches did the 2011 change affect? | 2011 post | `Official` | ~35% any change; 6–10% noticeable |
| How does Google date a page? | Byline dates documentation | `Official` | Several factors; visible date plus structured data |
| Does changing a date help? | Helpful content guidance; Mueller via SEJ | `Official`, `Secondhand` | No; listed as a warning sign |
| Does Google track confidence in dates? | `QualityTimebasedSyntacticDate` | `API Docs` | Fields exist; use unknown |
| Does Google track significant updates? | `QualityTimebasedLastSignificantUpdate` | `API Docs` | Field exists; definition unknown |

---

## 10.8 Checklist: working with freshness

- [ ] **Ask whether the query is time-sensitive.** News, recurring events and fast-changing products are; many evergreen topics are not `Official` (sections 10.1, 10.2).
- [ ] **Update the substance, then the date.** Change the date only when the page has changed significantly `Official`, `Secondhand` (section 10.4).
- [ ] **Show a labelled date.** Use "Published" or "Updated", and match it in `datePublished` and `dateModified` `Official` (section 10.3).
- [ ] **Get time zones right,** including daylight saving time `Official` (section 10.3).
- [ ] **Do not use future dates or event dates as the page date.** Use event markup for events `Official` (section 10.3).
- [ ] **Remove clutter dates** if Google shows the wrong one `Official` (section 10.3).
- [ ] **Refresh recurring pages fully.** Update the year in the title, heading and body together. [Chapter 9](09-titles-and-snippets.md) shows Google rewriting stale titles `Official`.
- [ ] **Help Google recrawl.** Fresh content cannot rank until it is crawled `Inference` (section 10.6).

---

## Sources for this chapter

| # | Source | Type | Checked |
|---|---|---|---|
| 1 | Google Search Central — [A guide to Google Search ranking systems](https://developers.google.com/search/docs/appearance/ranking-systems-guide), section "Freshness systems" (last updated 2025-12-10) | Official | 2026-11-26 |
| 2 | Google Inside Search blog — [Giving you fresher, more recent search results](https://search.googleblog.com/2011/11/giving-you-fresher-more-recent-search.html) (Amit Singhal, 3 Nov 2011, updated 7 Nov 2011) | Official | 2026-11-26 |
| 3 | Google Search Central — [Influence your byline dates in Google Search](https://developers.google.com/search/docs/appearance/publication-dates) (last updated 2025-12-10) | Official | 2026-11-26 |
| 4 | Google Search Central — [Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | Official | 2026-11-21 (via Chapter 4) |
| 5 | Search Engine Journal — [Google's John Mueller: changing dates on pages won't improve rankings](https://www.searchenginejournal.com/googles-john-mueller-changing-dates-on-pages-wont-improve-rankings/) (7 Apr 2021) | Secondhand | 2026-11-26 |
| 6 | HexDocs — [`QualityTimebasedSyntacticDate`, v0.4.0](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.QualityTimebasedSyntacticDate.html) | API Docs | 2026-11-26 |
| 7 | HexDocs — [`QualityTimebasedLastSignificantUpdate`, v0.4.0](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.QualityTimebasedLastSignificantUpdate.html) | API Docs | 2026-11-26 |

Notes on this check: sources 1, 2, 3, 5, 6 and 7 were read directly. Source 4 was not re-read for this chapter; the claim comes from Chapter 4. A 2019 Search Central blog post on dates could not be read (only its archive navigation loaded), so it is not cited. The original video of the April 2021 hangout was not checked; the Mueller statements come through Search Engine Journal. Leaked field descriptions are paraphrased.

---

<a id="next-chapter"></a>*Next chapter (planned): Sensitive (YMYL) topics — what "Your Money or Your Life" means in Google's guidelines, and what the evidence says about higher standards for those pages.*
