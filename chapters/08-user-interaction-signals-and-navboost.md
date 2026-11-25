# Chapter 8 — User Interaction Signals and NavBoost

> **Status:** Draft v0.1 · **Last verified:** 2026-11-25 · **Author:** [Saeed Yeganeh](https://saeedyeganeh.com/en/)

Does Google use clicks to rank pages? For years this was one of the most argued questions in SEO. Google representatives often dismissed click-based theories in public. Then the *U.S. v. Google* trial put a system called NavBoost on the record. Engineers described it under oath as a store of past clicks for past queries.

This chapter sets out what each kind of evidence says about user interaction data: Google's public pages, sworn testimony, interview notes, the 2025 remedies opinion, the leaked API documentation, and one patent. It also explains why the public denials and the court record are less contradictory than they first look.

[Chapter 1](01-reading-seo-evidence.md) used NavBoost's 13-month window to show the difference between sworn testimony and interview notes. [Chapter 2](02-how-search-works.md), section 2.6, placed NavBoost in the serving funnel. This chapter goes deeper on the system itself.

---

## 8.1 What Google says publicly

Google's public "How Search works" site has one direct sentence on this topic. Under "Relevance of content", it says Google uses "aggregated and anonymized interaction data" to assess whether results are relevant to queries `Official` ([Ranking results](https://google.com/intl/en/search/howsearchworks/how-search-works/ranking-results/)). The next sentence says Google turns that data into signals that help its machine-learned systems estimate relevance `Official` (same page).

The same page describes personalisation separately. It says Google can use information such as location, past Search history and Search settings to decide what is most relevant to a user. It also says Google's systems can recognise when a user has visited the same page several times, and may move it higher for that user `Official` (same page).

**What we can say:** Google publicly states that interaction data feeds relevance signals. This is not a leak or an inference. It is on Google's own explainer page.

**What we cannot say from this page:** what "interaction data" contains, how it is aggregated, or how much it weighs. The page does not use the word "click" for organic ranking.

### Public statements that seemed to say the opposite

In a Reddit AMA in February 2019, Google's Gary Illyes said dwell time, CTR and similar theories were "generally made up crap" `Secondhand` ([Search Engine Roundtable, 8 Feb 2019](https://www.seroundtable.com/google-ctr-dwell-time-signals-myths-27083.html)). The report adds the author's own context: that Google had long called such metrics noisy and easy to spam. That part is the reporter's summary, not a Google quote.

Section 8.7 returns to how this statement fits with the court record.

---

## 8.2 NavBoost in sworn testimony

### Pandu Nayak, 18 October 2023

Pandu Nayak of Google's search quality team testified on 18 October 2023. In answer to DOJ counsel, he agreed to the following `Testimony` (sworn trial testimony, [transcript 18 Oct 2023 PM](https://thecapitolforum.com/wp-content/uploads/2023/10/101823-USA-v-Google-PM.pdf)):

- NavBoost is one of Google's core systems (p. 6402).
- It goes back to about 2005, and Nayak said it might be older (p. 6402).
- It memorises past clicks for past queries and is trained on user data (p. 6405).
- It holds this information for queries received in the past 13 months. Before 2017, the window was 18 months (p. 6405).
- It slices data by locale, and by mobile versus desktop (pp. 6412–6413). Asked whether Google has a specific NavBoost for mobile, Nayak said it is one of the slices (p. 6420).

Nayak also described Glue as another name for NavBoost that covers all the other features on the results page, not only web links (p. 6403). In these answers, most of the wording was counsel's, and Nayak agreed to it. That is normal in cross-examination, but it means the phrasing is the lawyer's.

Two of Nayak's own points limit what NavBoost can do:

- NavBoost does not reduce results to the final few hundred by itself, because many documents have no clicks (p. 6407).
- NavBoost works only on documents already retrieved. In his words: "you get navboost only after they're retrieved in the first place" (p. 6422).

### Eric Lehman, 20 September 2023

Eric Lehman, a former Google software engineer, testified on 20 September 2023 `Testimony` (sworn trial testimony, [transcript 20 Sep 2023 PM](https://thecapitolforum.com/wp-content/uploads/2023/10/20230920-APM-BT7-PM-PUBLIC-Google.pdf)):

- He agreed that Google sometimes uses "clicks" as shorthand for user interaction data (pp. 1752–1753).
- He said the team most engaged with this data has gone by names such as NavBoost, Glue and Tetris (p. 1753).
- He said some of Google's ranking systems are machine learning systems that train on user data (p. 1758).
- He described a short click as one where a user clicks a result and comes back to Google fairly soon after (p. 1769).

A DOJ demonstrative quotes a later part of Lehman's testimony (1805:6–13) `Testimony` (demonstrative quoting sworn testimony, [PXRD016](https://www.justice.gov/media/1398886/dl)). Asked whether NavBoost trains on about 13 months of user data, Lehman agreed, but said "trains" might mislead. He said NavBoost is not a machine learning system: "It's just a big table." He described it as counts of clicks for each query and document, aggregated with some extra data.

**What we can say:** two Google witnesses described, under oath, a long-running core system that stores aggregated click data per query and document, over a rolling window, sliced by location and device.

**What we cannot say:** how NavBoost's counts are turned into a ranking score, how much weight that score carries, or whether the system works the same way today as it did in 2023.

---

## 8.3 NavBoost in the 2025 interview notes

Notes of a 31 January 2025 call with Pandu Nayak describe NavBoost in similar terms `Testimony` (interview notes, not sworn; [PXR0357](https://www.justice.gov/atr/media/1398866/dl)). The notes are a scanned public version with some garbled text.

- Section I lists NavBoost as a traditional signal. It measures how often users, subset by location and device type, click on a document for a query. It uses the most recent 13 months of data (p. 1).
- Section III describes NavBoost as a query-to-document lookup table, used in both directions, holding counts of user activity by document (p. 3).
- The same section says it is hard to quantify how many signals are affected by user-side data, and that some are affected more than others (p. 3).
- Section II says Google avoids simply predicting clicks, because "clicks are easily manipulated" and are a poor proxy for user experience (p. 2).
- Section IV tells an anecdote. An early signal compared how often a link was shown with how often it was clicked. Google found that this measure was biased by the link's position on the page (pp. 3–4).

**What we can say:** in 2025, a senior Google engineer still described NavBoost as a click-count table and as one signal among others. The same notes record that Google treats raw clicks with caution.

**What we cannot say:** how Google corrects for position bias today. The OCR text describing the correction is cut off and partly unreadable.

---

## 8.4 What the court found in 2025

On 2 September 2025, Judge Amit Mehta issued the remedies opinion in *U.S. v. Google* `Testimony` (court opinion, [Memorandum Opinion, No. 1:20-cv-03010](https://www.govinfo.gov/content/pkg/USCOURTS-dcd-1_20-cv-03010/pdf/USCOURTS-dcd-1_20-cv-03010-3.pdf)). An opinion is not testimony. It is the judge's findings, drawn from testimony and exhibits. Page numbers below are the opinion's printed numbers.

The opinion says the following `Testimony` (court opinion, same document):

- NavBoost is one of Google's core ranking models and runs on 13 months of click-and-query data (p. 89).
- The court calls Glue a "super query log" and NavBoost an important part of the Glue data (p. 153).
- "User-side data" is data Google collects from pairing a user's query with the response it returns. Examples include the link clicked, how long a user hovers over a link, and whether the user clicks back (p. 152).
- The Glue data covers clicks, hovers and other parts of a user's journey on and from the results page (p. 157).
- The court ordered Google to share the Glue data and RankEmbed training data with qualified competitors, subject to limits and privacy protections (pp. 157–164).
- It declined to order sharing of ranking signals derived from user-side data, finding that part of the request too attenuated (pp. 142–143).

**What we can say:** a federal court found, on the trial record, that NavBoost is a core ranking model fed by click-and-query data, and that Google's interaction logs record more than clicks.

**What we cannot say:** that hover time or click-backs are ranking signals. The opinion lists them as kinds of logged data, not as inputs to a specific ranking system.

---

## 8.5 What the leaked API documentation shows

The Content Warehouse reference contains a family of modules whose names begin with `QualityNavboostCraps`. The documentation does not expand "Craps", so this handbook does not either.

### `QualityNavboostCrapsCrapsData`

This module has no prose description, only a source note `API Docs` ([v0.4.0 reference](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.QualityNavboostCrapsCrapsData.html)). Its fields, with what their own descriptions say `API Docs` (same page):

| Field | What its description says |
|---|---|
| `query`, `url` | No description |
| `impressions`, `clicks`, `goodClicks`, `badClicks` | No description for the click fields. `impressions` carries a note that these may become legacy fields |
| `lastLongestClicks` | The number of clicks that were last and longest in related user queries |
| `country`, `language`, `device` | The country, language, and device and OS "slice" of the data |
| `mobileSignals` | The part of the data aggregated from mobile interfaces |
| `mobileData` | Deprecated; the description says not to use it |
| `patternLevel` | Data can be held for URL patterns as well as single URLs; more general patterns get higher levels |
| `squashed`, `unsquashed` | `squashed` is marked "not used yet"; `unsquashed` is for a retuning rollout |
| `unscaledIpPriorBadFraction` | An IP-address-based prior, before a transform applied in a "craps-penalty" step |
| `voterTokenCount` | The number of distinct voter tokens: a lower bound on distinct contributing users, used for privacy filtering |

### `QualityNavboostCrapsCrapsClickSignals`

This module describes itself as click and impression signals for "craps" `API Docs` ([v0.4.0 reference](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.QualityNavboostCrapsCrapsClickSignals.html)). It repeats the click fields above and adds `unicornClicks`, described as the subset of clicks associated with an event from a "Unicorn" user. The documentation does not define a Unicorn user `API Docs` (same page). One field, `absoluteImpressions`, says it is stored in compressed form in per-document data and `CompressedQualitySignals` `API Docs` (same page).

### Reading these fields correctly

**What we can say:**

- Google's internal documentation defines click and impression counts per query and URL, inside modules named after NavBoost.
- The data is sliced by country, language and device. This matches Nayak's sworn testimony that NavBoost slices by locale and by mobile versus desktop (section 8.2). Here `API Docs` and `Testimony` agree.
- Clicks are split into kinds: good, bad, and "last longest". The documentation also records a minimum count of distinct users, for privacy filtering.

**What we cannot say:**

- what makes a click "good" or "bad". The fields have no description;
- how these counts are combined or weighted;
- whether every field was in use when the documentation leaked, or now. Some are marked deprecated or not used yet.

**`Inference`:** a "last longest" click matches the plain meaning of a search that ended on that result after a long visit. The field description says only "last and longest in related user queries", so the exact definition remains unknown.

**`Inference`:** `voterTokenCount` and `unscaledIpPriorBadFraction` suggest the pipeline counts distinct users and adjusts for suspicious sources. Together with the "easily manipulated" remark in PXR0357, this fits the view that Google does not take raw click counts at face value.

---

## 8.6 A patent on click duration

Google holds a patent, US 9,235,627 B1, titled "Modifying search result ranking based on implicit user feedback" `Patent` ([US9235627B1](https://patents.google.com/patent/US9235627)). The inventors listed include Hyung-Jin Kim, Simon Tong, Noam Shazeer and Michelangelo Diligenti. The priority date is 2 November 2006, and it was granted on 12 January 2016 `Patent` (same page).

Google patented a method that computes a measure of relevance for a result and query. It compares the number of longer views of the result with the number of shorter views, and passes the measure to a ranking engine for later searches of the same query `Patent` (same page, abstract). The description says:

- Viewing time can be measured from the click on a result until the user comes back to the results page `Patent` (same page, description).
- In one example weighting, short clicks get a low weight and long clicks a much higher weight `Patent` (same page).
- Users tend to click results with good snippets or higher positions, whatever their real relevance. The patent treats this as a bias to correct `Patent` (same page).
- Thresholds can differ by query type, such as navigational or informational queries `Patent` (same page).

**What we can say:** Google engineers designed a method to turn long and short clicks into a relevance measure, and they anticipated position and snippet bias.

**What we cannot say:** that NavBoost uses this method. No source in this chapter connects the patent to NavBoost, so any such link is `Inference` at best.

---

## 8.7 Clicks for evaluation, not only for ranking

Click data can be used in two different ways. It can be a *ranking input*, or it can be used to *test* whether a ranking change is better. The record shows both.

- Nayak described live experiments in which results from two versions of ranking are interleaved, and clicks are used to decide which side is better `Testimony` (sworn, [transcript 18 Oct 2023 PM](https://thecapitolforum.com/wp-content/uploads/2023/10/101823-USA-v-Google-PM.pdf), pp. 6411–6412).
- Search Engine Land reported a Google presentation, shown at trial, titled "Unified Click Prediction". It says one slide stated that showing results users want to click "is NOT the ultimate goal" of ranking `Secondhand` ([Search Engine Land](https://searchengineland.com/how-google-search-ranking-works-pandu-nayak-435395)). The article does not give an exhibit number, so this handbook could not check the slide itself.

### Squaring the public denials with the record

`Inference`: the 2019 denial and the court record can both be accurate if they answer different questions. The record describes **aggregated** click data over **13 months**, per query and document, as one signal among many. It does not describe a page's own click-through rate or dwell time being read as a live, direct score. Illyes's remark targeted theories of the second kind. Still, the remark was broad and informal. Sworn testimony later showed that click data plays a larger role than such public comments suggested.

---

## 8.8 Putting it together

| Question | Best evidence | Label | Strength |
|---|---|---|---|
| Does Google use interaction data for relevance? | "How Search works" ranking page | `Official` | Direct statement |
| Is NavBoost a click-based core system? | Nayak and Lehman, 2023 | `Testimony` | Sworn |
| How long is the data window? | Nayak 2023; PXRD016; PXR0357 | `Testimony` | 13 months (18 before 2017) |
| Is NavBoost machine learning? | Lehman via PXRD016 | `Testimony` | Lehman: no, a table of counts |
| Is it sliced by location and device? | Nayak 2023; `CrapsData` fields | `Testimony`, `API Docs` | Two kinds agree |
| What is logged besides clicks? | Remedies opinion, 2025 | `Testimony` (court opinion) | Hovers, click-backs logged; use unspecified |
| How are good and bad clicks defined? | `CrapsData` | `API Docs` | Fields exist; no definitions |
| Can long and short clicks signal relevance? | US 9,235,627 | `Patent` | Design, not proof of use |
| Does Google trust raw clicks? | PXR0357 | `Testimony` (notes) | Says clicks are easily manipulated |

---

## 8.9 Checklist: working with interaction signals

- [ ] **Satisfy the searcher, not the click.** Click data is aggregated over months and corrected for bias. Lasting results come from pages that end the search `Inference` (sections 8.2, 8.5).
- [ ] **Do not buy or fake clicks.** Google describes clicks as easily manipulated, and its data records distinct users and suspicious sources `Testimony`, `API Docs` (sections 8.3, 8.5).
- [ ] **Remember the retrieval step.** NavBoost acts only on documents already retrieved. Relevance and indexing come first `Testimony` (section 8.2).
- [ ] **Expect slow movement.** A 13-month window means past behaviour lingers `Inference` (section 8.2).
- [ ] **Check by device and country.** The data is sliced that way, so performance on mobile in one market may differ from desktop elsewhere `Testimony`, `API Docs` (sections 8.2, 8.5).
- [ ] **Write titles and snippets that set honest expectations.** A misleading snippet may win a click that ends in a quick return `Inference` (sections 8.2, 8.6).
- [ ] **Do not treat your CTR in Search Console as a ranking score.** No source shows a page's own CTR read directly as a signal `Inference` (section 8.7).

---

## Sources for this chapter

| # | Source | Type | Checked |
|---|---|---|---|
| 1 | Google — [How Search works: Ranking results](https://google.com/intl/en/search/howsearchworks/how-search-works/ranking-results/) | Official | 2026-11-25 |
| 2 | *U.S. v. Google LLC* — [Trial transcript, 18 Oct 2023 PM session (Nayak)](https://thecapitolforum.com/wp-content/uploads/2023/10/101823-USA-v-Google-PM.pdf), pp. 6402–6422 | Testimony (sworn) | 2026-11-25 |
| 3 | *U.S. v. Google LLC* — [Trial transcript, 20 Sep 2023 PM session (Lehman)](https://thecapitolforum.com/wp-content/uploads/2023/10/20230920-APM-BT7-PM-PUBLIC-Google.pdf), pp. 1751–1770 | Testimony (sworn) | 2026-11-25 |
| 4 | U.S. DOJ — [PXRD016, demonstrative quoting Lehman testimony, 1805:6–13](https://www.justice.gov/media/1398886/dl) | Testimony (demonstrative) | 2026-11-25 |
| 5 | U.S. DOJ — [PXR0357, notes of 31 Jan 2025 call with Pandu Nayak](https://www.justice.gov/atr/media/1398866/dl) | Testimony (interview notes) | 2026-11-25 |
| 6 | U.S. District Court for D.C. — [Memorandum Opinion (remedies), 2 Sep 2025](https://www.govinfo.gov/content/pkg/USCOURTS-dcd-1_20-cv-03010/pdf/USCOURTS-dcd-1_20-cv-03010-3.pdf) | Testimony (court opinion) | 2026-11-25 |
| 7 | HexDocs — [`QualityNavboostCrapsCrapsData`, v0.4.0](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.QualityNavboostCrapsCrapsData.html) | API Docs | 2026-11-25 |
| 8 | HexDocs — [`QualityNavboostCrapsCrapsClickSignals`, v0.4.0](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.QualityNavboostCrapsCrapsClickSignals.html) | API Docs | 2026-11-25 |
| 9 | Google Patents — [US9235627B1, "Modifying search result ranking based on implicit user feedback"](https://patents.google.com/patent/US9235627) | Patent | 2026-11-25 |
| 10 | Search Engine Roundtable — [Google: CTR, dwell time and other UX signals are made-up myths (8 Feb 2019)](https://www.seroundtable.com/google-ctr-dwell-time-signals-myths-27083.html) | Secondhand | 2026-11-25 |
| 11 | Search Engine Land — [How Google Search and ranking works, according to Pandu Nayak](https://searchengineland.com/how-google-search-ranking-works-pandu-nayak-435395) | Secondhand | 2026-11-25 |

Notes on this check: the trial transcripts were read only in part. Claims above come from the pages read verbatim (Nayak pp. 6392–6426; Lehman pp. 1732–1772); the 1805 passage comes from PXRD016. PXR0357 is a scanned public version with garbled OCR. Remedies opinion page numbers are the printed numbers, which run a few pages behind the PDF's ECF numbering. Leaked field descriptions are paraphrased, not quoted. The patent's abstract and parts of its description were read; its claims were not.

---

<a id="next-chapter"></a>*Next chapter (planned): Titles and snippets in results — how Google chooses the title link and snippet, and what the evidence says about rewriting.*
