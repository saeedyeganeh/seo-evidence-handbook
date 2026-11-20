# Chapter 3 — Relevance and Search Intent

> **Status:** Draft v0.1 · **Last verified:** 2026-11-20 · **Author:** [Saeed Yeganeh](https://saeedyeganeh.com/en/)

[Chapter 2](02-how-search-works.md) ended at the serving stage: a query arrives, documents are retrieved, and a funnel of ranking steps narrows them down. This chapter looks at the first thing that funnel has to get right. Before quality, links or freshness can matter, Google has to work out **what the searcher means** and **which documents are about that**.

Those are two separate problems. *Search intent* is about the query: what the person wants. *Relevance* is about the match: how well a document answers that want. Most "keyword" advice blurs them together. The evidence below keeps them apart.

---

## 3.1 What Google says publicly

Google's public "How Search works" site describes ranking in terms of several factor groups. Two of them are the subject of this chapter: the meaning of the query and the relevance of content `Official` ([Ranking results](https://www.google.co.uk/intl/en_uk/search/howsearchworks/how-search-works/ranking-results)).

### Meaning of the query

On that page, Google says it builds language models to work out how the few words a person types match up with the most useful content available `Official` (same page). It names concrete steps in this work `Official` (same page):

- recognising and correcting spelling mistakes;
- a synonym system that can find relevant documents even when they do not contain the exact words used in the query;
- recognising when a query is about current events, such as sports scores or company earnings, so the latest information is shown;
- recognising that many queries have a local intent.

### Relevance of content

The most basic relevance signal Google describes is simple. If a page contains the same keywords as the query, especially in its headings or body text, the page *might* be more relevant `Official` (same page). The word "might" is in Google's own sentence. Matching words are a starting point, not a guarantee.

The same section adds a second kind of evidence. Google says it uses "aggregated and anonymised interaction data" to assess whether results are relevant to queries `Official` (same page). In other words, Google states publicly that how people interact with results feeds into its judgement of relevance. Chapter 8 deals with interaction signals in detail.

### Context and settings

Relevance also depends on the person searching. Google says it uses information such as location, past Search history and Search settings to decide what is most relevant for that person at that moment `Official` (same page).

**What we can say:** Google publicly describes relevance as more than word matching. It names spelling correction, synonyms, query categories (fresh and local), keyword placement, anonymised interaction data and personal context.

**What we cannot say:** how these inputs are weighted against each other for any query.

---

## 3.2 From words to meaning: Google's language systems

Exact word matching fails often. People use different words from the page they need, and small words can change the whole meaning. Google has described several machine-learning systems built to close that gap.

In a February 2022 post, Pandu Nayak, Google Fellow and Vice President of Search, summarised four of them `Official` ([How AI powers great search results](https://blog.google/products/search/how-ai-powers-great-search-results/)):

| System | What the post says |
|---|---|
| **RankBrain** | Launched in 2015, it was Google's first deep learning system in Search. It helps relate words in a search to real-world concepts, and is used to help rank top results. |
| **Neural matching** | Introduced to Search in 2018. It looks at a whole query or page rather than only keywords, to understand the concepts behind them. |
| **BERT** | Launched in 2019. It looks at words in sequence and how they relate to each other, so important words in a query are not dropped. |
| **MUM** | Introduced the previous May. The post says MUM was then used only for specialised applications and was "not currently used to help rank" results. |

The post's RankBrain example is a query about the consumer at the highest level of a food chain, which RankBrain can connect to the concept of an apex predator even though the query does not use that term `Official` (same post).

### The "to" example

When BERT launched, Google gave a clear example of why word order and small words matter. For the query *2019 brazil traveler to usa need a visa*, earlier systems missed the importance of "to" and returned results about U.S. citizens travelling to Brazil. With BERT, Search understood the query was about a Brazilian travelling to the U.S. `Official` ([Understanding searches better than ever before](https://blog.google/products/search/search-language-understanding-bert/), 25 October 2019). The same post said BERT would help Search better understand "one in 10 searches" in U.S. English at that time `Official` (same post).

**What we can say:** for years Google has used language models that match queries and pages by meaning, not only by shared words. A page can be relevant to a query that uses none of its exact phrases.

**What we cannot say:** that these 2019–2022 descriptions match the current system. Both posts describe the state of Search on their publication dates. Google has not said whether these systems still run in the same form.

---

## 3.3 What the court record adds

The *U.S. v. Google* material (see [Chapter 1](01-reading-seo-evidence.md), section 1.2) gives a more technical picture. Two documents are interview notes, not sworn testimony. One is the court's own opinion.

### From word counting to learned signals

Notes of a 31 January 2025 call with Pandu Nayak describe Google's traditional approach to ranking as being in the style of Okapi BM25, a classic function for estimating how relevant a document is to a query `Testimony` (interview notes; [PXR0357](https://www.justice.gov/atr/media/1398866/dl), section II). The notes then describe a shift toward signals generated by machine learning and deep learning, naming RankEmbed, RankBrain and DeepRank `Testimony` (same exhibit, section II).

The same notes describe RankEmbed as a dual encoder model that places both the query and the document in an embedding space, where semantic properties of each are considered `Testimony` (same exhibit, section II). They also say Google found that signals from the BERT-based DeepRank model could be broken down into signals resembling traditional ones, and that combining the two gave better results `Testimony` (same exhibit, section II).

### Topicality and the "ABC" signals

The clearest description of relevance in the record comes from notes of an 18 February 2025 call with Google engineer HJ Kim `Testimony` (interview notes, not sworn; [PXR0356](https://www.justice.gov/atr/media/1398871/dl), section I). According to these notes:

- Google has three "fundamental" signals, called **ABC**: **Anchors** (links from a source page to a target page), **Body** (terms in the document) and **Clicks** (historically, how long a user stayed on a linked page before returning to the results page).
- These three signals are the key components of **topicality**, which the notes describe as Google's determination of how relevant a document is to the query.
- A signal called **T\*** (topicality) combines at least these three signals in a relatively hand-crafted way.
- Apart from RankBrain and DeepRank, almost every signal is hand-crafted, meaning engineers can analyse and adjust it. The stated reason: "if anything breaks Google knows what to fix."

The same notes say that query-based signals are not stored but computed at query time. They add that some such signals are kept in separate tables and looked up, and that some are stored in the index for convenience `Testimony` (same exhibit, section IV).

### The court's findings on RankEmbed

Judge Amit Mehta's remedies opinion of 2 September 2025 adds detail on RankEmbed `Testimony` (court opinion; [Memorandum Opinion, ECF No. 1436](https://www.courthousenews.com/wp-content/uploads/2025/09/judge-amit-mehta-google-search-monopoly-remedy-ruling.pdf), pp. 154–157):

- RankEmbed is described as a deep-learning system with "strong natural-language understanding". The court says this helps it find the best documents to retrieve even when a query lacks certain terms.
- The court, citing Nayak's trial testimony, says RankEmbed particularly helped Google improve answers to long-tail queries.
- Citing Eric Lehman's trial testimony, the court says RankEmbed was trained on 1/100th of the data used for earlier ranking models, yet gives higher-quality results.
- Its training data combines click-and-query data with scores that human raters gave to web pages.

The same opinion records Nayak's evidence that queries on mobile tend to have more location-focused intents `Testimony` (same opinion, p. 94).

### Careful reading: how much data trained RankEmbed?

The two sources describe the training data differently. The Nayak call notes say Google trained RankEmbed on a sample from a single month of search data `Testimony` ([PXR0357](https://www.justice.gov/atr/media/1398866/dl), section II). The court opinion says RankEmbed and its later version, RankEmbedBERT, rely on a share of 70 days of search logs plus human rater scores; the share itself is blank in the public copy `Testimony` ([Memorandum Opinion](https://www.courthousenews.com/wp-content/uploads/2025/09/judge-amit-mehta-google-search-monopoly-remedy-ruling.pdf), p. 154).

These may describe different versions of the model, or the notes may simplify. The record does not settle it. When you see one figure quoted on its own, check which document and which model it refers to.

**What we can say:** inside Google, relevance to a query ("topicality") has been built from at least three raw inputs: the words on the page, the links pointing to it, and how users responded to it. Learned models such as RankEmbed and DeepRank work alongside these hand-crafted signals, and they can match documents to queries that lack some of the query's terms.

**What we cannot say:** how T\* combines its inputs, how much each weighs, or how these signals are balanced against RankEmbed today. The HJ Kim and Nayak notes are summaries written by others; neither person's exact words are recorded.

---

## 3.4 What the leaked API reference adds

The Content Warehouse API reference (see [Chapter 1](01-reading-seo-evidence.md), section 1.2) has a family of modules for **salient terms**: the words and phrases that best describe something.

- `QualitySalientTermsSalientTermSet` describes itself as "a collection of terms (unigrams and bigrams) with associated weights" that can describe something `API Docs` ([v0.4.0](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.QualitySalientTermsSalientTermSet.html)). Its `salientTerm` field holds the terms sorted from highest to lowest weight, and its `version` field is described as specific to web documents salient terms.
- `QualitySalientTermsSalientTerm` holds each term. Its `salience` field is the term's importance as a descriptor on a scale from 0 to 1. Its `originalTerm` field lists the different forms in which a normalised term was found in the signals `API Docs` ([v0.4.0](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.QualitySalientTermsSalientTerm.html)).
- The same module has a field `signalTerm`. Its description reads: "signal_term contains extra signal-specific (e.g., body, anchors, clicks) data for this term." `API Docs` (same page).

The three examples in that description are the same three inputs as the ABC signals in the HJ Kim notes. Two independent kinds of evidence name the same trio. That they describe the same underlying design is `Inference`, but it is a well-supported one.

The remedies opinion also says RankEmbed's training data includes salient terms that Google derived from the query `Testimony` ([Memorandum Opinion](https://www.courthousenews.com/wp-content/uploads/2025/09/judge-amit-mehta-google-search-monopoly-remedy-ruling.pdf), p. 154).

**What we can say:** Google's internal data structures describe documents with weighted terms drawn not only from the page body but also from anchors and clicks. The words *other people* use about a page, in links and in queries that led to clicks, can become part of how the page is described.

**What we cannot say:** how salience is computed, how salient terms feed into ranking, or whether these modules are used in this form today.

---

## 3.5 Search intent: how Google thinks about what the searcher wants

The fullest public description of how Google thinks about intent is in its Search Quality Rater Guidelines. Raters' scores do not directly change rankings (see [Chapter 1](01-reading-seo-evidence.md), worked example B). The guidelines describe what Google's systems aim for, so they are useful here as a statement of goals, not as a description of signals.

The evidence below comes from Google's official overview of the guidelines, dated November 2023 `Official` ([Search Quality Rater Guidelines: An Overview](https://services.google.com/fh/files/misc/hsw-sqrg.pdf)). The full guidelines contain more detail, which this chapter does not cite.

### Intent is read from the query and, sometimes, location

The overview says intent is determined from the content of the query and, where relevant, the user's location `Official` (same document, Section 03, p. 28). Its example: a user in London searching for *coffee shops* probably wants coffee shops in London.

### Many queries have more than one meaning

The overview notes that many queries have more than one meaning. Its example is *mercury*, which could mean the planet or the chemical element `Official` (same document, p. 28). The Needs Met scale then refers to *dominant*, *common* and *minor* interpretations of a query, and rates a result by which of these it helps with `Official` (same document, p. 30). Location can rule some meanings out. For a user in California searching *batman*, the overview treats the Turkish city of Batman as an extremely unlikely intent `Official` (same document, p. 30).

### Meaning is judged as of now

The overview says Google assumes users want current information, and raters are told to consider a query's current meaning when rating `Official` (same document, p. 28). A query's dominant meaning can therefore differ from what it was a few years ago. That consequence is `Inference`.

### Needs Met

The rating that captures intent is **Needs Met**. The overview says usefulness depends on the user's intent, as interpreted from the query, and on how fully a result satisfies it `Official` (same document, pp. 27–28). The scale runs: Fully Meets, Highly Meets, Moderately Meets, Slightly Meets and Fails to Meet `Official` (same document, p. 30). Fully Meets is reserved for queries with a clear intent to find one specific result `Official` (same page).

**What we can say:** in Google's own framing, a result is good for a query when it satisfies the likely intent behind it. A page can be well written and still be a poor result for a query whose dominant meaning is something else.

**What we cannot say:** that Google's ranking systems classify queries into the same categories raters use, or score pages in the same way.

---

## 3.6 Keyword stuffing: where word matching stops helping

Because matching words is only a starting point, repeating them does not keep adding relevance. Google's spam policies define **keyword stuffing** as filling a page with keywords or numbers to manipulate rankings. It notes that such keywords often appear in a list or group, unnaturally or out of context `Official` ([Spam policies](https://developers.google.com/search/docs/essentials/spam-policies)). The examples Google gives are `Official` (same page):

- lists of phone numbers without substantial added value;
- blocks of text listing cities and regions a page is trying to rank for;
- repeating the same words or phrases so often that the text sounds unnatural.

**Practical reading:** use the words your audience uses, in headings and body text, because Google says that can signal relevance. Do not repeat them beyond what reads naturally, because Google treats that as spam. This advice is `Inference` from the two `Official` statements above.

---

## 3.7 Putting it together

**What we can say**

- Google works out what a query means through spelling correction, synonyms, language models, query categories and personal context such as location `Official`.
- Language systems such as RankBrain, neural matching and BERT were built to match queries and pages by meaning, not only by shared words `Official`.
- Internally, relevance to a query ("topicality") has been built from page text, anchors and clicks, combined in a largely hand-crafted way `Testimony` (interview notes). The API reference names the same three inputs for salient terms `API Docs`.
- Learned retrieval models such as RankEmbed help find relevant documents even when a query lacks some terms, and helped most with long-tail queries `Testimony` (court opinion).
- In Google's framing, a good result is one that satisfies the likely intent behind a query, judged as of now and, where relevant, for the user's location `Official`.

**What we cannot say**

- The weight of any relevance signal, or how topicality is combined with quality and other signals.
- Whether the systems named in 2019–2022 posts still run in the same form.
- That rater concepts such as "dominant interpretation" correspond directly to signals in Google's ranking systems.

---

## 3.8 Checklist: relevance and intent for one page

- [ ] **Intent.** What do most people who type this query want right now? Look at what Google currently shows for it.
- [ ] **Multiple meanings.** Does the query have more than one meaning? Which one does your page serve, and is it the dominant one?
- [ ] **Location.** Does the intent change with where the searcher is? If the query has a local intent, does your page serve that place?
- [ ] **Vocabulary.** Does the page use the words your audience uses, in headings and body text, without forced repetition?
- [ ] **Meaning over exact match.** Does the page answer the question even for variations of the query that do not share its exact words?
- [ ] **Anchors.** Do internal links to the page use text that describes what the page is about?
- [ ] **Satisfaction.** Would a searcher with the dominant intent need to go back to the results after visiting? If so, the page does not fully meet the need.
- [ ] **Spam check.** Are there lists of cities, numbers or repeated phrases that exist only to match queries? Remove them.

---

## Sources for this chapter

| # | Source | Type | Checked |
|---|---|---|---|
| 1 | Google — [How Search works: ranking results](https://www.google.co.uk/intl/en_uk/search/howsearchworks/how-search-works/ranking-results) | Official | 2026-11-20 |
| 2 | Google Blog — [Pandu Nayak, "How AI powers great search results" (3 Feb 2022)](https://blog.google/products/search/how-ai-powers-great-search-results/) | Official | 2026-11-20 |
| 3 | Google Blog — [Pandu Nayak, "Understanding searches better than ever before" (25 Oct 2019)](https://blog.google/products/search/search-language-understanding-bert/) | Official | 2026-11-20 |
| 4 | Google — [Search Quality Rater Guidelines: An Overview (Nov 2023)](https://services.google.com/fh/files/misc/hsw-sqrg.pdf) | Official | 2026-11-20 |
| 5 | Google Search Central — [Spam policies for Google web search](https://developers.google.com/search/docs/essentials/spam-policies) | Official | 2026-11-20 |
| 6 | U.S. DOJ — [PXR0356, notes of 18 Feb 2025 call with HJ Kim](https://www.justice.gov/atr/media/1398871/dl) | Testimony (interview notes) | 2026-11-20 |
| 7 | U.S. DOJ — [PXR0357, notes of 31 Jan 2025 call with Pandu Nayak](https://www.justice.gov/atr/media/1398866/dl) | Testimony (interview notes) | 2026-11-20 |
| 8 | *U.S. v. Google LLC* — [Remedies Memorandum Opinion, ECF No. 1436 (2 Sep 2025)](https://www.courthousenews.com/wp-content/uploads/2025/09/judge-amit-mehta-google-search-monopoly-remedy-ruling.pdf) | Testimony (court opinion) | 2026-11-20 |
| 9 | HexDocs — [`QualitySalientTermsSalientTermSet`, google_api_content_warehouse v0.4.0](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.QualitySalientTermsSalientTermSet.html) | API Docs | 2026-11-20 |
| 10 | HexDocs — [`QualitySalientTermsSalientTerm`, google_api_content_warehouse v0.4.0](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.QualitySalientTermsSalientTerm.html) | API Docs | 2026-11-20 |

The copy of the remedies opinion cited above is hosted by Courthouse News Service. Page numbers are the opinion's printed page numbers, not the ECF header page numbers.

---

*Next chapter (planned): Content quality, originality and effort — what Google says it rewards, and what the evidence shows.*
