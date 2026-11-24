# Chapter 7 — Site-Level Quality Signals

> **Status:** Draft v0.1 · **Last verified:** 2026-11-24 · **Author:** [Saeed Yeganeh](https://saeedyeganeh.com/en/)

Chapters 3 to 6 looked mostly at single pages and single links. This chapter asks a wider question. Does Google judge a *site* as a whole, and can that judgement change how its individual pages rank?

The short answer is yes, and Google now says so in its own documentation. The harder questions are *how* site-level judgements are formed, *what* they contain, and *how much* they matter for any one page. Here the evidence becomes uneven. Google's public statements are clear but brief. Notes from a 2025 call with a Google engineer describe a quality signal that relates mostly to the site. The leaked API documentation lists many site-level fields. Patents describe possible ways to score a site. None of these sources gives weights.

[Chapter 1](01-reading-seo-evidence.md), worked example A, introduced this topic briefly. This chapter goes through the evidence in full.

---

## 7.1 What Google says publicly

### The ranking systems guide

Google's ranking systems guide opens with a short paragraph on this exact question `Official` ([ranking systems guide](https://developers.google.com/search/docs/appearance/ranking-systems-guide)). In summary:

- Google's ranking systems are designed to work on the page level, using a variety of signals and systems.
- "Site-wide signals and classifiers are also used and contribute to our understanding of pages."
- Having some good site-wide signals does not mean that every page on the site will always rank highly. The reverse also holds for poor site-wide signals.

The page was last updated on 2025-12-10.

This paragraph was added in November 2024. Search Engine Roundtable reported the change on 20 November 2024 and quoted Google's stated reason: to make it easier to understand that Google has both page-level and site-wide signals `Secondhand` ([Search Engine Roundtable](https://www.seroundtable.com/google-search-site-wide-page-level-signals-38440.html)). Search Engine Journal reported the same change a day earlier `Secondhand` ([Search Engine Journal](https://www.searchenginejournal.com/google-page-level-site-wide-signals-both-matter-for-rankings/533063/)).

### The March 2024 core update post

The same position appeared earlier in Google's post on the March 2024 core update `Official` ([Search Central blog, 5 Mar 2024](https://developers.google.com/search/blog/2024/03/core-update-spam-policies)). The post said Google's core ranking systems are primarily designed to work on the page level. It also said: "We do have some site-wide signals that are also considered." `Official` (same post).

The same post warned about third-party scores. Tools that give sites a "reputation" or "authority" score do not correspond to any of Google's own signals and do not come from Google `Official` (same post).

**What we can say:** Google publicly confirms that site-wide signals and classifiers exist and affect how pages are understood and ranked. It also says that page-level signals come first in its design.

**What we cannot say:** which site-wide signals exist, how they are computed, or how they are balanced against page-level signals. Google does not publish this.

---

## 7.2 The helpful content signal: a documented site-wide classifier

The clearest public example of a site-level classifier is the helpful content system.

### What Google said in 2022

The August 2022 announcement, by Chris Nelson of Google Search Quality, described the update as introducing "a new site-wide signal" `Official` ([Search Central blog, 18 Aug 2022](https://developers.google.com/search/blog/2022/08/helpful-content-update?authuser=8)). The post made four points that matter here `Official` (same post):

- The signal is one among many other signals Google considers for ranking web pages.
- Removing unhelpful content could help the rankings of the site's other content.
- Sites identified by the update may find the signal applied to them over a period of months.
- The signal is weighted. Sites with lots of unhelpful content may notice a stronger effect.

### What happened in 2024

In the ranking systems guide, the helpful content system now sits under "Retired systems". The guide says it was announced in 2022 and that, in March 2024, it became part of Google's core ranking systems `Official` ([ranking systems guide, "Retired systems"](https://developers.google.com/search/docs/appearance/ranking-systems-guide)). The March 2024 post said there is no longer one signal or system used to judge helpfulness `Official` ([5 Mar 2024 post](https://developers.google.com/search/blog/2024/03/core-update-spam-policies)).

**What we can say:** between 2022 and 2024, Google ran a documented classifier that judged a site's content as a whole and could affect the ranking of all its pages. Google says that function is now inside its core ranking systems.

**What we cannot say:** that the 2022 site-wide signal still exists in the same form. Google says the approach changed. It does not say whether the core systems keep a separate site-wide helpfulness classifier.

**`Inference`:** the advice from 2022, that removing unhelpful content may help the rest of a site, is still consistent with the current documentation, which keeps the page-level and site-wide paragraph. It is not a guaranteed effect.

### Panda: the older precedent

The ranking systems guide also lists Panda as a retired system. It says Panda was announced in 2011 and became part of Google's core ranking systems in 2015 `Official` ([ranking systems guide, "Retired systems"](https://developers.google.com/search/docs/appearance/ranking-systems-guide)). The guide does not describe Panda as site-level, so this handbook does not claim it.

---

## 7.3 Recovery and timing: what the core updates page says

Google's page on core updates gives the most direct public guidance on how a whole site is reassessed `Official` ([Google Search's core updates and your website](https://developers.google.com/search/updates/core-updates)). The page was last updated on 2025-12-10.

- Core updates are described as broad. They do not target specific sites or individual pages `Official` (same page).
- If a whole site sees a large, sustained drop, the page points to a self-assessment. The questions ask whether the site *overall* is helpful, reliable and people-first, not only individual pages `Official` (same page).
- On timing, it says some changes can take effect in a few days, but it could take several months for Google's systems to learn and confirm that the site as a whole is producing helpful content `Official` (same page).
- If nothing changes after a few months, recovery may mean waiting until the next core update `Official` (same page).
- It advises against quick-fix changes. It calls deleting content a last resort, and notes that deleting whole sections may suggest they were made for search engines first `Official` (same page).

**What we can say:** Google describes site-level reassessment as slow. A site-level judgement is not updated the moment a page is fixed.

**What we cannot say:** an exact recovery time. Google gives ranges ("a few days", "several months"), not a schedule. Chapter 13 (planned) is meant to cover timing in more depth.

---

## 7.4 Site reputation and how a site's signals can be borrowed

If a site has strong site-level signals, other people may try to borrow them. Google's spam policies address this directly.

### Site reputation abuse

The March 2024 post introduced the site reputation abuse policy. It targeted third-party pages published with little or no first-party oversight, to take advantage of the host site's ranking signals. The post said the policy would take effect starting 5 May 2024 `Official` ([5 Mar 2024 post](https://developers.google.com/search/blog/2024/03/core-update-spam-policies)).

In November 2024, Google clarified the policy `Official` ([Updating our site reputation abuse policy, 19 Nov 2024](https://developers.google.com/search/blog/2024/11/site-reputation-abuse?hl=en)). In summary, the post said:

- Using third-party content to exploit a host site's ranking signals breaks the policy whether or not there is first-party involvement or oversight.
- Moving such content to a subdirectory or subdomain of the same site does not resolve the issue.
- The policy is enforced through manual actions, notified in Search Console.

In August 2026, Google changed how these manual actions apply in Europe `Official` ([Update to the Site Reputation Policy, 28 Aug 2026](https://developers.google.com/search/blog/2026/08/update-site-reputation-policy)). The post said: "For users inside the EEA, the impact of the manual action won't apply." Outside the European Economic Area, a manual action still affects results for the part of the site involved `Official` (same post). Google said the change followed discussion with the European Commission `Official` (same post).

### Expired domain abuse

The spam policies also cover domains bought for their history. Expired domain abuse is when an expired domain is bought and repurposed mainly to manipulate search rankings `Official` ([Spam policies, "Expired domain abuse"](https://developers.google.com/search/docs/essentials/spam-policies)). Google's examples include affiliate content on a site once used by a government agency, and casino content on a former school site `Official` (same page).

**What we can say:** Google treats a site's accumulated standing as something that can be exploited. Both policies only make sense if site-level signals carry real value.

**`Inference`:** these two policies are the strongest *indirect* evidence that site-level signals are meaningful in ranking. Google would not need rules against borrowing a site's reputation if that reputation had no effect.

---

## 7.5 Site diversity: a site-level rule for results pages

One documented system works at the site level in a different way. It does not judge quality. It limits how much space one site gets.

The ranking systems guide says the site diversity system means Google generally won't show more than two web page listings from the same site in its top results `Official` ([ranking systems guide, "Site diversity system"](https://developers.google.com/search/docs/appearance/ranking-systems-guide)). It says site diversity generally treats subdomains as part of the root domain. Subdomains are treated as separate sites only when deemed relevant `Official` (same page).

The guide also describes an exact match domain system, which stops domains that exactly match a query from getting too much credit for that alone `Official` (same page). [Chapter 1](01-reading-seo-evidence.md), worked example C, compares this with a related leaked field.

---

## 7.6 The court record: Q* and "the site rather than the query"

The *U.S. v. Google* exhibits include notes of a call with Google engineer HJ Kim ([PXR0356](https://www.justice.gov/atr/media/1398871/dl)). The header dates the call to 18 February 2025 `Testimony` (interview notes). These are notes taken during a call. They are not sworn trial testimony (see [Chapter 1](01-reading-seo-evidence.md), section 1.2). The document does not say who wrote them.

The notes say the following `Testimony` (interview notes, PXR0356, pp. 3–4):

- Q\* is described as page quality, linked to the notion of trustworthiness, and as "incredibly important".
- The quality score is said to be generally static across queries and not tied to a specific query.
- The notes say Q is "largely static and largely related to the site rather than the query."
- There is an exception. In some cases the quality signal uses information from the query and has to be computed at query time.
- A single PageRank-type signal, described as distance from a known good source, is said to be an input to the quality score.
- HJ Kim is recorded as having started the page quality team 17 years earlier, in response to content farms.

**What we can say:** a Google engineer described, in notes from a 2025 call, a central quality score that is mostly query-independent and mostly about the site.

**What we cannot say:**

- whether Q\* is computed per page, per site, or as a mix. The notes call it "page quality" and also say it relates mostly to the site;
- what goes into Q\* beyond the PageRank-type input mentioned;
- how much Q\* weighs against relevance signals.

---

## 7.7 What the leaked API documentation adds

The `QualityNsrNsrData` module in the Content Warehouse reference holds many fields described as site-level ([v0.4.0 reference](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.QualityNsrNsrData.html)). The module has no prose description, only a developer note `API Docs` (same page). As in earlier chapters, this handbook does not expand "NSR", because the documentation does not.

Selected fields and their own descriptions `API Docs` (same page):

| Field | What its description says |
|---|---|
| `siteChunk` | The primary NSR "sitechunk", usually the same as a host-level canonical URL |
| `tofu` | A site-level score: a site quality predictor based on content |
| `chardEncoded` | Also a site-level quality predictor based on content |
| `clutterScore` | A site-level signal in Q\* that penalises sites loading many distracting or annoying resources |
| `siteQualityStddev` | The spread of page-level quality ratings across a site |
| `smallPersonalSite` | A score for promoting small personal sites |
| `titlematchScore` | How well a site's titles match user queries |
| `localityScore` | The locality part of a "LocalAuthority" signal |
| `spambrainLavcScore` | A SpamBrain score, dated July 2022 in its description |
| `nsrOverrideBid` | Overrides NSR as a bid in Q\*; for emergencies only |
| `priorAdjustedNsr` | Whether the site is above or below average NSR in its slice |
| `impressions`, `chromeInTotal` | Site-level impressions; site-level Chrome views |

Other fields record site-level link data (`siteLinkIn`, `siteLinkOut`, `sitePr`), embeddings of the site (`site2vecEmbedding`), and flags such as `isElectionAuthority` and `isCovidLocalAuthority` `API Docs` (same page).

[Chapter 1](01-reading-seo-evidence.md), worked example A, covered a separate field, `siteAuthority`, in the `CompressedQualitySignals` module.

### Reading these fields correctly

**What we can say:**

- Google's internal documentation defines a family of site-level quality data, keyed to a "sitechunk" rather than to a single URL.
- Two field descriptions (`clutterScore`, `nsrOverrideBid`) refer to Q\*. This links the NSR data to the Q\* score described in the court notes in section 7.6.
- The data includes content-based predictors, measures of variation across a site's pages, and usage measures such as impressions and Chrome views.
- One field is described as promoting small personal sites. Site-level data is not only used to demote.

**What we cannot say:**

- how any field is computed or weighted;
- whether every field was in use when the documents leaked, or is in use now;
- that `chromeInTotal` or `impressions` feeds ranking directly. The descriptions say what the fields hold, not how they are used.

**`Inference`:** the `siteQualityStddev` field suggests Google tracks not only a site's average quality but how uneven it is. A site with a few excellent pages and many weak ones may look different from a site of even, middling quality. The documentation does not say how this is used.

---

## 7.8 Patents: ways to score a site

Two Google patents describe methods for scoring a whole site. As [Chapter 1](01-reading-seo-evidence.md) explains, a patent shows a design, not proof of use.

- **US 9,195,944 B1, "Scoring site quality".** Google patented a method that obtains measurements of how long users visit resources on a site, and computes a site quality score from them by "computing a statistical measure from the plurality of measurements" `Patent` ([US9195944B1](https://patents.google.com/patent/US9195944)). The description's main example of a visit is the time from a click on a search result until the user returns to the results page `Patent` (same page). Priority date 24 February 2012; granted 24 November 2015.
- **US 8,442,984 B1, "Website quality signal generation".** Google patented a method in which websites are rated, relationships between ratings and website signals are learned as models, and the models assign ratings to unrated websites `Patent` ([US8442984B1](https://patents.google.com/patent/US8442984)). Filed 31 March 2008.

**What we can say:** Google engineers designed methods to score a whole site, both from user behaviour and from rater-trained models.

**What we cannot say:** that either method runs in Search today, or that it relates to Q\* or to the NSR fields. No source connects them.

---

## 7.9 Putting it together

| Question | Best evidence | Label | Strength |
|---|---|---|---|
| Does Google use site-wide signals? | Ranking systems guide; March 2024 post | `Official` | Direct statement |
| Do good site signals guarantee page rankings? | Ranking systems guide | `Official` | Direct: no |
| Was there a documented site-wide classifier? | Helpful content update, 2022 | `Official` | Direct; now part of core |
| How fast does a site-level reassessment happen? | Core updates page | `Official` | Ranges only: days to months |
| Is there a mostly site-related quality score? | PXR0356 (HJ Kim call notes) | `Testimony` | Interview notes, not sworn |
| What site-level data is defined internally? | `QualityNsrNsrData` | `API Docs` | Fields exist; use and weight unknown |
| How could a site be scored? | US 9,195,944; US 8,442,984 | `Patent` | Designs, not proof of use |
| Are third-party "authority" scores Google's? | March 2024 post | `Official` | Direct: no |

---

## 7.10 Checklist: managing site-level quality

- [ ] **Judge the whole site, not just top pages.** Google's self-assessment asks about the site overall `Official` (section 7.3).
- [ ] **Find weak sections, not only weak pages.** Unhelpful content can affect how other content ranks `Official` (section 7.2).
- [ ] **Improve before you delete.** Google calls deletion a last resort `Official` (section 7.3).
- [ ] **Do not host third-party content to rank on your reputation.** Moving it to a subdomain or subfolder does not fix it `Official` (section 7.4).
- [ ] **Do not buy expired domains to reuse their history** for unrelated content `Official` (section 7.4).
- [ ] **Expect slow movement.** Site-level recovery can take months and may wait for a core update `Official` (section 7.3).
- [ ] **Ignore third-party "authority" scores as a measure of Google's view.** Google says they are not its signals `Official` (section 7.1).
- [ ] **Aim for even quality across the site.** Internal data tracks the spread of page quality `Inference` (section 7.7).

---

## Sources for this chapter

| # | Source | Type | Checked |
|---|---|---|---|
| 1 | Google Search Central — [A guide to Google Search ranking systems](https://developers.google.com/search/docs/appearance/ranking-systems-guide) (last updated 2025-12-10) | Official | 2026-11-24 |
| 2 | Google Search Central Blog — [What web creators should know about our March 2024 core update and new spam policies (5 Mar 2024)](https://developers.google.com/search/blog/2024/03/core-update-spam-policies) | Official | 2026-11-24 |
| 3 | Google Search Central Blog — [What creators should know about Google's August 2022 helpful content update (18 Aug 2022)](https://developers.google.com/search/blog/2022/08/helpful-content-update?authuser=8) | Official | 2026-11-24 |
| 4 | Google Search Central — [Google Search's core updates and your website](https://developers.google.com/search/updates/core-updates) (last updated 2025-12-10) | Official | 2026-11-24 |
| 5 | Google Search Central Blog — [Updating our site reputation abuse policy (19 Nov 2024)](https://developers.google.com/search/blog/2024/11/site-reputation-abuse?hl=en) | Official | 2026-11-24 |
| 6 | Google Search Central Blog — [Update to the Site Reputation Policy (28 Aug 2026)](https://developers.google.com/search/blog/2026/08/update-site-reputation-policy) | Official | 2026-11-24 |
| 7 | Google Search Central — [Spam policies for Google web search](https://developers.google.com/search/docs/essentials/spam-policies), section "Expired domain abuse" | Official | 2026-11-24 |
| 8 | U.S. DOJ — [PXR0356, notes of a call with Google engineer HJ Kim, 18 Feb 2025](https://www.justice.gov/atr/media/1398871/dl) | Testimony (interview notes) | 2026-11-24 |
| 9 | HexDocs — [`QualityNsrNsrData`, google_api_content_warehouse v0.4.0](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.QualityNsrNsrData.html) | API Docs | 2026-11-24 |
| 10 | Google Patents — [US9195944B1, "Scoring site quality"](https://patents.google.com/patent/US9195944) | Patent | 2026-11-24 |
| 11 | Google Patents — [US8442984B1, "Website quality signal generation"](https://patents.google.com/patent/US8442984) | Patent | 2026-11-24 |
| 12 | Search Engine Roundtable — [Google makes it clear it has both site-wide and page-level ranking signals (20 Nov 2024)](https://www.seroundtable.com/google-search-site-wide-page-level-signals-38440.html) | Secondhand | 2026-11-24 |
| 13 | Search Engine Journal — [Google: page-level and site-wide signals both matter (19 Nov 2024)](https://www.searchenginejournal.com/google-page-level-site-wide-signals-both-matter-for-rankings/533063/) | Secondhand | 2026-11-24 |

Notes on this check: source 5 was read through an extracted summary, so its points are paraphrased, not quoted. The PXR0356 text is a scanned public version with some garbled characters; quotes give the clearest reading. Patent details beyond the abstracts were read from the descriptions, not from the claims. The `CompressedQualitySignals` reference page could not be re-opened in this run, so this chapter only points to Chapter 1 for it and makes no new claim about it.

---

<a id="next-chapter"></a>*Next chapter (planned): User interaction signals and NavBoost — what the court record, Google's statements and the API documentation say about clicks.*
