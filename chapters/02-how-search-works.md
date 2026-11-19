# Chapter 2 — How Google Search Works End to End

> **Status:** Draft v0.1 · **Last verified:** 2026-11-19 · **Author:** [Saeed Yeganeh](https://saeedyeganeh.com/en/)

Every later chapter in this handbook talks about a signal, a system or a problem. All of them sit somewhere in one pipeline: a URL is discovered, fetched, rendered, analysed, stored, and finally retrieved and ranked for a query. This chapter walks through that pipeline in order. For each stage it shows what Google documents publicly, what came out in court, and what the leaked API reference adds.

The point is practical. When a page does not get traffic, the first question is *which stage it failed at*. A page that was never crawled needs a different fix from a page that was indexed but ranks poorly.

---

## 2.1 The pipeline in one view

Google describes Search as a fully automated engine. Most pages in its results were never submitted by anyone; crawlers found them `Official` ([How Search works](https://developers.google.com/search/docs/fundamentals/how-search-works)).

Google's guide names three stages: **crawling**, **indexing** and **serving search results**. It also states that "not all pages make it through each stage" `Official` ([How Search works](https://developers.google.com/search/docs/fundamentals/how-search-works)).

The same guide makes two further points that frame everything below `Official`:

- Google does not take payment to crawl a site more often or to rank it higher.
- Google does not guarantee that it will crawl, index or serve any page, even one that follows Google Search Essentials.

In this chapter the pipeline is split a little more finely, because the extra steps are where many real problems hide:

| Step | Question it answers | Typical failure |
|---|---|---|
| Discovery | Does Google know the URL exists? | No links or sitemap point to it |
| Crawling | Did Googlebot fetch it? | Blocked, server errors, low priority |
| Rendering | Did Google see the content JavaScript produces? | Content only appears after scripts run |
| Indexing | Was it analysed and stored, and as which canonical? | Duplicate, low quality, `noindex` |
| Serving | Is it retrieved and ranked for a query? | Weak relevance, low quality |

Rendering is described by Google as part of crawling in the general guide, and as its own phase in the JavaScript guide (see 2.4). Splitting discovery from crawling follows the general guide, which treats URL discovery as the first step of crawling.

---

## 2.2 Discovery: how Google learns that a URL exists

There is no central list of all web pages. Google therefore has to keep looking for new and changed pages `Official` ([How Search works](https://developers.google.com/search/docs/fundamentals/how-search-works)). The guide names three routes:

1. **Pages Google already knows**, which it revisits.
2. **Links** from a known page to a new one, which Google extracts.
3. **Sitemaps** that a site owner submits.

Discovery is not the same as crawling. Once Google knows a URL, it *may* visit it; Googlebot does not crawl every page it discovers `Official` ([How Search works](https://developers.google.com/search/docs/fundamentals/how-search-works)).

A sitemap is a file that lists a site's pages, videos and other files and tells Google about them. Google states that submitting one does not guarantee every listed item will be crawled and indexed `Official` ([Sitemaps overview](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview)). The same page says sitemaps help most when a site is large, when it is new with few external links, or when it has a lot of image or video content or appears in Google News `Official`.

**Practical reading:** a sitemap tells Google a URL exists. It does not raise that URL's priority on its own. Internal links do two jobs at once: they make a URL discoverable, and they show that the site itself treats the page as part of its structure. The second part is `Inference`; Google's documentation describes links here only as a discovery route.

---

## 2.3 Crawling: deciding what to fetch, and how fast

### Who decides

Googlebot uses an algorithmic process to choose which sites to crawl, how often, and how many pages to fetch from each `Official` ([How Search works](https://developers.google.com/search/docs/fundamentals/how-search-works)). Its crawlers try not to crawl a site too fast. They adjust to how the site responds; for example, HTTP `500` errors are read as a signal to slow down `Official` (same page).

### Crawl budget: capacity and demand

Google's crawl budget guide defines a site's crawl budget as the set of URLs that Google *can* and *wants to* crawl `Official` ([Crawl budget](https://developers.google.com/crawling/docs/crawl-budget)). Two parts make it up:

- **Crawl capacity limit.** This caps how much of your server's time Google's connections can occupy. It rises when the site answers quickly and reliably, and falls when the site slows down or returns server errors. Google also says its own resources are finite and must be shared across the web.
- **Crawl demand.** Without guidance, Google tries to crawl most or all URLs it knows about on a site. URLs that are more popular on the web tend to be recrawled more often, and Google wants to recrawl pages often enough to notice changes.

Three details in the current version of that guide are worth knowing `Official` ([Crawl budget](https://developers.google.com/crawling/docs/crawl-budget), last updated 2026-07-22 when checked):

- Every site starts with the same "default, conservative crawl capacity limit".
- The capacity limit is shared across all of Google's crawlers, not only the one for Search.
- Returning a `304 Not Modified` response tells Google it can reuse its cached copy.

The guide is aimed at large sites (roughly a million or more unique pages changing weekly) and medium sites (roughly ten thousand or more pages changing daily). Google adds that these are not exact thresholds `Official`. For most small sites, crawl budget is not the bottleneck. That last sentence is `Inference` from who the guide is written for.

### Why crawling fails

Google lists common reasons Googlebot cannot fetch a page `Official` ([How Search works](https://developers.google.com/search/docs/fundamentals/how-search-works)):

- problems with the server that hosts the site;
- network problems;
- `robots.txt` rules that block Googlebot;
- pages that need a login.

### What Googlebot is

Googlebot has two main crawler types: Googlebot Smartphone and Googlebot Desktop. Google states that most crawl requests use the mobile crawler `Official` ([Googlebot](https://developers.google.com/search/docs/crawling-indexing/googlebot)). The same page says Googlebot crawls the first 2MB of a supported file type and the first 64MB of a PDF; the limit applies to uncompressed data. Once the limit is reached, Googlebot stops the fetch and sends only the part already downloaded for indexing consideration `Official`.

### `robots.txt` controls crawling, not indexing

Google describes `robots.txt` as mainly a way to avoid overloading a site with requests. It states that it is "not a mechanism for keeping a web page out of Google" `Official` ([robots.txt introduction](https://developers.google.com/search/docs/crawling-indexing/robots/intro)). A page blocked in `robots.txt` can still be indexed if other sites link to it; it may then appear without a description `Official` (same page). To keep a page out of results, Google points to `noindex` or password protection instead (see 2.5).

---

## 2.4 Rendering: seeing what JavaScript produces

Many sites build their content with JavaScript. If Google did not render pages, it might not see that content `Official` ([How Search works](https://developers.google.com/search/docs/fundamentals/how-search-works)). During crawling, Google renders the page and runs its JavaScript with a recent version of Chrome `Official` (same page).

Google's JavaScript guide describes three phases for JavaScript web apps: crawling, rendering and indexing `Official` ([JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)). The guide adds these specifics `Official` (same page):

- Before fetching a URL, Googlebot checks `robots.txt`. If the URL is disallowed, it skips the request.
- Every page that returns HTTP `200` is sent to the rendering queue, whether or not it uses JavaScript.
- A page may wait in that queue for a few seconds, but it can take longer.
- For non-`200` responses, such as a `404` page, rendering might be skipped.
- Google uses the rendered HTML to index the page.
- If Google finds `noindex` in the original HTML, it may skip rendering. Removing `noindex` with JavaScript later may therefore not work.
- Rendering uses an evergreen (regularly updated) version of Chromium.

**What we can say:** rendering is a real, separate step with its own queue. What matters for indexing is the HTML *after* rendering, not only the HTML the server sent.

**What we cannot say:** how long the queue is for a given site, or whether some sites wait longer than others. Google gives no numbers beyond "a few seconds" or longer.

---

## 2.5 Indexing: analysis, duplicates and the canonical

### What indexing does

After crawling, Google tries to understand what a page is about. It analyses the text, key tags and attributes such as `<title>` and `alt`, images and videos `Official` ([How Search works](https://developers.google.com/search/docs/fundamentals/how-search-works)).

A central part of this step is **canonicalization**. Google groups pages with similar content into a cluster. It then picks the page that best represents the cluster as the canonical, which is the version that may be shown in results. The other pages become alternate versions that may be served in other contexts, for example to a mobile user or for a very specific query `Official` (same page).

Google also collects signals about the canonical page and its content. The guide gives the page's language, the country the content is local to, and the page's usability as examples. Information about the canonical page and its cluster may be stored in the Google index, which the guide describes as a large database hosted on thousands of computers `Official` (same page).

### How the canonical is chosen

Google defines canonicalization as choosing the representative URL for a piece of content `Official` ([Canonicalization](https://developers.google.com/search/docs/crawling-indexing/canonicalization)). It says it weighs a handful of factors, including:

- whether the URL is served over HTTP or HTTPS;
- redirects;
- whether the URL appears in a sitemap;
- `rel="canonical"` annotations.

A declared canonical is "a hint, not a rule", so Google may choose a different URL `Official` (same page). Google also says the canonical is crawled most regularly, while duplicates are crawled less often to reduce load on the site `Official` (same page). This links indexing back to crawling: messy duplication can spend crawl effort on URLs that will never be shown. That consequence is `Inference`.

### Why a page is not indexed

Google says indexing is not guaranteed and lists common reasons a processed page is not indexed `Official` ([How Search works](https://developers.google.com/search/docs/fundamentals/how-search-works)):

- the content is low quality;
- robots meta rules forbid indexing;
- the site's design makes indexing difficult.

To remove a page from results, `noindex` works only if Googlebot can fetch the page and see the rule. Google states that the page **must not** be blocked by `robots.txt`; otherwise the crawler never sees `noindex` and the page can still appear `Official` ([Block indexing with noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing)).

### Reading the Search Console statuses

The Page indexing report in Search Console maps directly onto the stages above `Official` ([Page indexing report](https://support.google.com/webmasters/answer/7440203?hl=en)):

| Status | Stage it points to | What Google says it means |
|---|---|---|
| Discovered – currently not indexed | Discovery → crawling | Found but not crawled yet; typically Google expected crawling to overload the site and rescheduled it |
| Crawled – currently not indexed | Crawling → indexing | Crawled but not indexed; common, and not necessarily a problem |
| Duplicate, Google chose different canonical than user | Indexing (canonicalization) | Google thinks another URL in the set makes a better canonical |
| Alternate page with proper canonical tag | Indexing (canonicalization) | Points correctly to an indexed canonical; nothing to do |

The same help page says most sites have some unindexed pages, and that you should expect only canonical pages to be indexed, not every URL `Official`.

### The inside view: what the leaked API reference adds

The leaked Content Warehouse API reference (see [Chapter 1](01-reading-seo-evidence.md), section 1.2) contains structures that fit this stage. Two are useful here.

- `CompositeDoc` is described as a "Protocol record used for collecting together all information about a document" `API Docs` ([CompositeDoc, v0.4.0](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.CompositeDoc.html)). Its fields include sub-records for per-document data, quality signals, indexing information and robots information.
- `CompositeDocIndexingInfo` is described as information "mostly used within indexing". Its field `selectionTierRank` is described as a language-normalised score from 0 to 1 over the serving tier, and the description names three tiers: Base, Zeppelins and Landfills `API Docs` ([CompositeDocIndexingInfo, v0.4.0](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.CompositeDocIndexingInfo.html)). The same module also has fields for a URL's change rate, its change history, its crawl status, and the time a URL stopped being canonical.

**What we can say:** the documentation defines a per-document record that gathers crawl, indexing, robots and quality information together. It also refers to named serving tiers and a per-document score over them.

**What we cannot say:** what places a document in a given tier, what each tier means for ranking, or whether these structures are still used in this form. The field descriptions do not say. Reading the tier name "Landfills" as a penalty or demotion goes beyond the text and is `Inference` at best.

---

## 2.6 Serving: retrieval and ranking

### What Google says publicly

When someone searches, Google looks in its index for matching pages and returns the results it believes are the highest quality and most relevant to the query. Google says relevancy depends on hundreds of factors, which can include the user's location, language and device `Official` ([How Search works](https://developers.google.com/search/docs/fundamentals/how-search-works)). The page also says the search features shown change with the query. Its example: a search for bicycle repair shops is likely to show local results, while a search for a modern bicycle is more likely to show images.

Google's public "How Search works" site lists key signal groups: the meaning of the query, relevance, quality, usability and context. It adds that the weight of each factor varies with the query; for example, freshness matters more for news topics than for dictionary definitions `Official` ([Ranking results](https://google.com/intl/en/search/howsearchworks/how-search-works/ranking-results/)).

The [ranking systems guide](https://developers.google.com/search/docs/appearance/ranking-systems-guide) says Google's automated ranking systems look at many factors and signals about hundreds of billions of web pages. It separates core ranking systems from systems for specific needs, and lists named systems such as BERT, neural matching, passage ranking, freshness systems and deduplication systems `Official`. Later chapters cover these one by one.

### What sworn testimony adds: a funnel

Trial testimony gives a more detailed picture of the serving stage. On 18 October 2023, Pandu Nayak, who described himself as part of Google's search quality team, answered questions from the judge and from DOJ counsel. In summary `Testimony` (sworn trial testimony, [transcript 18 Oct 2023 PM](https://thecapitolforum.com/wp-content/uploads/2023/10/101823-USA-v-Google-PM.pdf), pp. 6405–6408):

1. **Retrieval.** For a query, Google retrieves documents from the index that match it. Nayak described the index as recording, for every word, the pages on which it occurs, and described walking postings lists (6406–6407).
2. **First narrowing.** Retrieval continues until there are tens of thousands of candidate documents (6406:25; 6407:5).
3. **Ranking with signals.** Signals then cut this to several hundred (6407:9). Asked whether NavBoost alone does this, Nayak said it is not the only factor. He named core topicality signals, PageRank signals and localization signals as also involved (6407:19–6408:2).
4. **Further ranking.** The smaller set then goes to a next phase of ranking that, in Nayak's words, uses machine learning among other things (6407). Counsel's later summary of the sequence put deep learning at this point, and Nayak agreed (6408).

Separate interview notes from 2025 add detail on how signals are combined. Notes of a 31 January 2025 call with Nayak describe signals being combined "into a single score" that determines a document's place among the blue links. The notes also describe Twiddlers as components that re-rank a set of already selected results `Testimony` (interview notes, not sworn testimony; [PXR0357](https://www.justice.gov/atr/media/1398866/dl), section I). The notes list the attendees, including lawyers from Williams & Connolly and an expert; the note-taker is not named.

**What we can say:** serving is staged. A large candidate set is retrieved from an inverted index and then narrowed in steps, with different signals doing work at different stages. NavBoost, topicality, PageRank and localization signals all played a part in the middle stage as of 2023.

**What we cannot say:** the exact number of stages today, the size of each candidate set for a given query, or how much any signal weighs. The numbers in the testimony were rough orders of magnitude given in answer to questions. They are not a specification.

### Careful reading: "Google's index has 400 billion documents"

This figure is often quoted as Google's own statement. In the transcript it is a *question*. DOJ counsel asked whether the index was about 400 billion documents in 2020. Nayak replied: "I don't know the specific number, but maybe." `Testimony` ([transcript 18 Oct 2023 PM](https://thecapitolforum.com/wp-content/uploads/2023/10/101823-USA-v-Google-PM.pdf), 6397:9–11). He went on to say the number had come down for a period, that Google wants a comprehensive index, and that bigger is not automatically better because an index can be filled with junk (6397–6398).

The accurate statement is: *DOJ counsel put a figure of about 400 billion documents for 2020 to Pandu Nayak, who did not confirm it.* This is a good example of the method in [Chapter 1](01-reading-seo-evidence.md): testimony answers the questions lawyers asked, and the exact words matter.

---

## 2.7 Putting it together

**What we can say**

- Pages pass through discovery, crawling, rendering, indexing and serving, and many drop out at each step. Google says so plainly and gives no guarantees at any stage `Official`.
- Crawling is rationed by capacity (how much your server can take) and demand (how much Google wants your URLs) `Official`.
- Google indexes the rendered page, and rendering is queued `Official`.
- Duplicates are clustered and one canonical is chosen. Your declared canonical is a hint `Official`.
- Serving is a funnel from retrieval to successive ranking stages `Testimony`.

**What we cannot say**

- How Google sets crawl priority for an individual URL beyond the factors it lists.
- How the "serving tiers" named in the API reference are assigned or used.
- The size of Google's index today. The ranking systems guide speaks only of "hundreds of billions of web pages".
- The weight of any ranking signal.

---

## 2.8 Checklist: find the stage where a page fails

- [ ] **Discovery.** Is the URL linked from at least one crawlable page on the site, and listed in the sitemap if you use one?
- [ ] **Crawl access.** Is it allowed in `robots.txt`? Does it return `200` without a login?
- [ ] **Server health.** Are there `5xx` errors or slow responses that could lower crawl capacity?
- [ ] **Rendering.** Does the main content appear in the rendered HTML (URL Inspection → view crawled page), not only after user interaction?
- [ ] **Size.** Is the important content within the first 2MB of the uncompressed HTML?
- [ ] **Indexing rules.** Is there a `noindex` in the original HTML or the `X-Robots-Tag` header? If you want the page removed, is it crawlable so the rule can be seen?
- [ ] **Canonical.** Which URL did Google choose as canonical? Do redirects, `rel="canonical"`, internal links and the sitemap all point to the same URL?
- [ ] **Search Console status.** Which status does the Page indexing report show, and which stage does it point to?
- [ ] **Serving.** If the page is indexed but gets no impressions, is it relevant to what people search for, and is it good enough to compete? (Chapters 3 and 4.)

---

## Sources for this chapter

| # | Source | Type | Checked |
|---|---|---|---|
| 1 | Google Search Central — [In-depth guide to how Google Search works](https://developers.google.com/search/docs/fundamentals/how-search-works) | Official | 2026-11-19 |
| 2 | Google Search Central — [Optimize your crawl budget](https://developers.google.com/crawling/docs/crawl-budget) | Official | 2026-11-19 |
| 3 | Google Search Central — [Googlebot](https://developers.google.com/search/docs/crawling-indexing/googlebot) | Official | 2026-11-19 |
| 4 | Google Search Central — [Introduction to robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro) | Official | 2026-11-19 |
| 5 | Google Search Central — [Sitemaps overview](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview) | Official | 2026-11-19 |
| 6 | Google Search Central — [Understand the JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics) | Official | 2026-11-19 |
| 7 | Google Search Central — [What is canonicalization](https://developers.google.com/search/docs/crawling-indexing/canonicalization) | Official | 2026-11-19 |
| 8 | Google Search Central — [Block Search indexing with noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing) | Official | 2026-11-19 |
| 9 | Search Console Help — [Page indexing report](https://support.google.com/webmasters/answer/7440203?hl=en) | Official | 2026-11-19 |
| 10 | Google — [How Search works: ranking results](https://google.com/intl/en/search/howsearchworks/how-search-works/ranking-results/) | Official | 2026-11-19 |
| 11 | Google Search Central — [A guide to Google Search ranking systems](https://developers.google.com/search/docs/appearance/ranking-systems-guide) | Official | 2026-11-19 |
| 12 | *U.S. v. Google LLC* — [Trial transcript, 18 Oct 2023 PM session (Nayak)](https://thecapitolforum.com/wp-content/uploads/2023/10/101823-USA-v-Google-PM.pdf), pp. 6397–6408 | Testimony (sworn) | 2026-11-19 |
| 13 | U.S. DOJ — [PXR0357, notes of 31 Jan 2025 call with Pandu Nayak](https://www.justice.gov/atr/media/1398866/dl) | Testimony (interview notes) | 2026-11-19 |
| 14 | HexDocs — [`CompositeDoc`, google_api_content_warehouse v0.4.0](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.CompositeDoc.html) | API Docs | 2026-11-19 |
| 15 | HexDocs — [`CompositeDocIndexingInfo`, google_api_content_warehouse v0.4.0](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.CompositeDocIndexingInfo.html) | API Docs | 2026-11-19 |

The trial transcript copy cited above is hosted by The Capitol Forum.

---

*Next chapter (planned): Relevance and search intent — how Google matches a query to what the searcher means.*
