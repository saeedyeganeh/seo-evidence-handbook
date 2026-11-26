# Chapter 9 — Titles and Snippets in Results

> **Status:** Draft v0.1 · **Last verified:** 2026-11-26 · **Author:** [Saeed Yeganeh](https://saeedyeganeh.com/en/)

A search result is a small advertisement for a page. It has a clickable title, a short text excerpt, and a site name above the URL. Site owners write a `<title>` element and a meta description, and then find that Google shows something else. This chapter sets out what Google has documented about how it builds these parts, what changed in 2021, how site owners can limit snippets, and what the leaked API documentation adds.

[Chapter 8](08-user-interaction-signals-and-navboost.md) ended with a checklist item about honest titles and snippets. This chapter covers the mechanics behind that advice. It stays with ordinary web results. AI features in Search get their own chapter later.

---

## 9.1 The parts of a result, and Google's names for them

Google's documentation uses specific names. Using them makes the official pages easier to read.

- **Title link.** Google defines it as the title of a search result that links to the web page. It can appear in Google Search and in other Google properties, such as Google News `Official` ([Influencing your title links](https://developers.google.com/search/docs/appearance/title-link?hl=en&rd=1)).
- **Snippet.** The text excerpt shown with a result. Google says snippets are created automatically from page content `Official` ([Control your snippets](https://developers.google.com/search/docs/advanced/appearance/snippet)).
- **Site name.** A name for the site shown in the result. In July 2023 Google described it as appearing above the URL `Official` ([An update on site names](https://developers.google.com/search/blog/2023/07/sitenames)).
- **Featured snippet.** A snippet that Google's systems elevate for a query because the page would make a good featured snippet for it `Official` ([Featured snippets and your website](https://developers.google.com/search/docs/appearance/featured-snippets?hl=en)).

The older term "title tag" still appears in SEO writing. Google's documentation separates the HTML `<title>` element, which you write, from the title link, which Google shows. The two are often the same, but not always.

---

## 9.2 How Google chooses the title link

### The sources Google lists

Google's title link documentation says the process is "completely automated" `Official` ([title link documentation](https://developers.google.com/search/docs/appearance/title-link?hl=en&rd=1)). It takes into account both the content of the page and references to the page elsewhere on the web `Official` (same page).

The page lists the sources Google uses to determine a title link `Official` (same page):

- the content of the `<title>` element;
- the main visual title shown on the page;
- heading elements, such as `<h1>`;
- the content of `og:title` meta tags;
- other text that is large and prominent because of its styling;
- other text on the page;
- anchor text on the page;
- the text of links that point to the page;
- `WebSite` structured data.

The page also says Google cannot change title links by hand for individual sites `Official` (same page). After a site edits its titles, the page says Google must recrawl and reprocess the page, which can take a few days to a few weeks, and it suggests requesting a recrawl `Official` (same page).

### Why Google replaces a `<title>` element

The same page lists common problems and how Google handles them `Official` (same page). In summary:

| Problem | Example on Google's page | What Google may do |
|---|---|---|
| Half-empty title | The title holds only the site name after a separator | Use a heading or other prominent text to fill it |
| Obsolete title | A recurring page still names last year in its title | Use the newer year from the visible heading |
| Inaccurate title | A dynamic page whose title lists items no longer shown | Shorten it to match the page |
| Micro-boilerplate | Several pages of a TV show share one title, without season numbers | Add the season from prominent text on each page |
| No clear main title | Two or more headings with the same styling | Use the first heading |
| Language or script mismatch | A Hindi page with an English or transliterated title | Generate a title that matches the main content |
| Duplicated site name | The title repeats the site name already shown | Omit the site name from the title link |

The page states the general rule: if Google detects an issue, it may try to build a better title link from anchors, on-page text or other sources `Official` (same page).

**What we can say:** Google treats the `<title>` element as one input among several, and it replaces the element when it judges the element to be missing, stale, misleading, repeated or in the wrong language. Links from other pages can also feed the title link.

**What we cannot say:** how Google weighs these sources against each other, or what threshold makes it reject a `<title>` element. The documentation lists sources and examples, not rules.

---

## 9.3 The 2021 change to title generation

In August 2021 Google announced a new system for generating title links. The post is dated 24 August 2021 and signed by Danny Sullivan `Official` ([An update to how we generate web page titles](https://developers.google.com/search/blog/2021/08/update-to-generating-page-titles?hl=en)).

According to the post `Official` (same page):

- Before the change, the title shown could vary with the query. Under the new system, Google said this would generally no longer happen.
- The new system draws on text that people see on the page: the visual title or headline, header tags such as `<h1>`, other large and prominent text, other page text, and link text.
- The HTML `<title>` element remained the most likely source. Google put it at more than 80% of the time.

A follow-up post on 17 September 2021, also by Danny Sullivan, reported changes made after feedback `Official` ([More information on how Google generates titles](https://developers.google.com/search/blog/2021/09/more-info-about-titles)). It said:

- Google had used text other than the `<title>` element in some cases since 2012, such as empty titles, identical titles across pages, or pages with no title at all `Official` (same page).
- After the feedback-driven changes, Google used the `<title>` element about 87% of the time, up from about 80% `Official` (same page).
- It gave examples that match the current documentation, including half-empty titles, obsolete years and repeated titles across a subset of pages `Official` (same page).
- It pointed people to the Google Search Help Community to report problems `Official` (same page).

**What we can say:** since 2021, Google has said in writing that most title links come from the `<title>` element. It has also said the title link is generally the same for every query, unlike the snippet (section 9.5).

**What we cannot say:** what the share is today. The 80% and 87% figures describe 2021. The current documentation gives no percentage `Official` ([title link documentation](https://developers.google.com/search/docs/appearance/title-link?hl=en&rd=1)).

---

## 9.4 What Google recommends for `<title>` elements

The current title link documentation gives these recommendations `Official` ([title link documentation](https://developers.google.com/search/docs/appearance/title-link?hl=en&rd=1)):

- **Give every page a title** in the `<title>` element.
- **Be descriptive and concise.** Avoid vague labels such as "Home" or "Profile".
- **There is no length limit.** Google truncates the title link to fit the device width. The page gives no character count. Pixel or character limits in SEO tools are third-party estimates.
- **Avoid keyword stuffing.** The page's example repeats one term in several spellings.
- **Avoid repeated or boilerplate text.** If the same phrase appears on every page, or long titles differ by one word, update the title dynamically to reflect what each page contains.
- **Brand concisely.** The home page can carry more about the site. Other pages can place the site name at the start or end, separated by a hyphen, colon or pipe.
- **Make the main title clear.** The most prominent heading should be easy to tell apart, for example the first visible `<h1>` in a larger font.
- **Match the page's language and writing system.**
- **Use `noindex`, not robots.txt, to keep a page out of results.** If Google cannot crawl a page, it may rely on off-page content such as anchor text for the title link.
- **Leave flight prices out of titles.** The page says Google will likely not show price information in title links for flight pages.

`Inference`: most of these items are the mirror image of the replacement triggers in section 9.2. A title that is complete, current, accurate, unique and in the page's language gives Google fewer reasons to rewrite it. No source states that following them guarantees the title will be used.

---

## 9.5 How Google builds the snippet

The snippet documentation says snippets are "primarily created from the page content itself" `Official` ([Control your snippets](https://developers.google.com/search/docs/advanced/appearance/snippet)). The rest of what it says `Official` (same page):

- **Snippets depend on the query.** Google may show different snippets for different searches of the same page. This is the main difference from title links after 2021.
- **The meta description is used sometimes.** Google may use it when it would describe the page more accurately than text from the page.
- **There is no length limit for meta descriptions.** Snippets are truncated as needed, typically to fit the device width.
- **Write a unique description for each page.** Identical or similar descriptions across pages are not helpful. A site-level description suits the home page and other aggregation pages. Page-level descriptions suit the rest.
- **Include useful facts.** The page suggests information such as the author, date or price, depending on the page type.
- **Programmatic descriptions are fine.** For large database-driven sites, the page encourages generating descriptions from page-specific data.
- **Avoid lists of keywords.** The page says these are less likely to be shown as a snippet.

**What we can say:** a meta description is a suggestion. Google writes most snippets from the page, chooses the passage that fits the query, and uses the meta description when it fits better.

**What we cannot say:** how often Google uses the meta description. The page gives no figure. Studies that report a percentage are `Secondhand` measurements of a sample of queries, and this chapter cites none.

---

## 9.6 Limiting or blocking snippets

Google supports three controls for snippets. They are defined in the robots meta tag specification `Official` ([Robots meta tag specifications](https://developers.google.com/webmasters/control-crawl-index/docs/robots_meta_tag)):

| Control | Where it goes | What the specification says it does |
|---|---|---|
| `nosnippet` | Robots meta tag or `X-Robots-Tag` header | No text snippet or video preview. A static image thumbnail may still show |
| `max-snippet:[number]` | Robots meta tag or `X-Robots-Tag` header | Caps the text snippet at that many characters. `0` means no snippet; `-1` lets Google choose the length |
| `data-nosnippet` | HTML attribute on `span`, `div` or `section` | Marks parts of a page that should not be used in a snippet |

Further points from the same specification `Official` (same page):

- `nosnippet` applies to all forms of search results at Google. The page lists web search, Google Images, Discover, AI Overviews and AI Mode. It also stops the content from being used as a direct input for AI Overviews and AI Mode.
- `max-snippet` also limits how much content can be used as a direct input for AI Overviews and AI Mode. The page says this limit does not apply where a publisher has separately granted permission to use the content.
- `data-nosnippet` is not valid on other elements. Google advises against adding or removing it on existing elements with JavaScript.
- When rules conflict, the more restrictive one wins. If a page has both `max-snippet:50` and `nosnippet`, `nosnippet` applies.

**What we can say:** site owners can suppress or shorten snippets, and these controls now reach Google's AI features as well as classic results.

**What we cannot say:** whether these controls change a page's ranking. The specification does not say. `Inference`: they are presentation controls. A page with no snippet may attract fewer clicks, so test before applying them widely.

---

## 9.7 Featured snippets

Google's featured snippets page says its systems decide whether a page would make a good featured snippet for a query `Official` ([Featured snippets and your website](https://developers.google.com/search/docs/appearance/featured-snippets?hl=en)). Site owners cannot mark a page as a featured snippet. The page mentions no markup for it `Official` (same page).

Other points from the page `Official` (same page):

- To block all snippets, including featured ones, use `nosnippet`. Text marked with `data-nosnippet` also will not appear in featured or regular snippets.
- To make a featured snippet less likely while keeping normal snippets, lower `max-snippet`. Google gives no minimum length, and says a low value does not guarantee the page will stop appearing as a featured snippet.
- A click on a featured snippet takes the user to the matching section of the page. If Google cannot find the position, it goes to the top of the page.
- Featured snippets can also appear inside a "related questions" group.

---

## 9.8 Site names

In July 2023 Google said it had updated the system that chooses site names, to make them more representative `Official` ([An update on site names](https://developers.google.com/search/blog/2023/07/sitenames), Kenji Inoue, 28 July 2023). The post says:

- `WebSite` structured data is the best way to tell Google a preferred site name, and the documentation now encourages an `alternateName` as a fallback `Official` (same page).
- Google may not use a name in some cases, for example when two different global sites claim the same name. If no name is chosen, Google generally shows the domain or subdomain name `Official` (same page).
- Support for subdomains had started on mobile in English, French, German and Japanese. The post says it then extended to all devices in those languages, with more languages planned `Official` (same page).

The title link documentation connects the two features. It lists `WebSite` structured data as a title link source. It also says Google may drop a duplicated site name from the title link when the site name already appears in the result `Official` ([title link documentation](https://developers.google.com/search/docs/appearance/title-link?hl=en&rd=1)).

`Inference`: when Google shows the site name separately, repeating the brand in every `<title>` element adds less than it used to. The documentation still allows a short brand at the start or end (section 9.4).

---

## 9.9 What the leaked API documentation shows

The Content Warehouse reference includes modules that describe how titles and snippets are recorded and scored. As [Chapter 1](01-reading-seo-evidence.md) explained, these show which data is defined, not how it is weighted.

### `MustangReposWwwSnippetsSnippetsRanklabFeatures`

This module describes itself as a protocol buffer exported to flat files "in ranklab" `API Docs` ([v0.4.0 reference](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.MustangReposWwwSnippetsSnippetsRanklabFeatures.html)). Its fields, with what their own descriptions say `API Docs` (same page):

| Field | What its description says |
|---|---|
| `titles` | Title features for each candidate, sorted from best to worst; "the first element is the actually selected title" |
| `snippets` | Features for Muppet snippet candidates; in production, only the chosen snippet's data is recorded |
| `displaySnippet` | Features of the final chosen snippet; first filled by Muppet, then overwritten by Superroot if SnippetBrain is triggered |
| `titleQueryTermCoverage` | Query term coverage in titles |
| `snippetQueryTermCoverage` | Query term coverage in snippets |
| `titleSnippetQueryTermCoverage` | Query term coverage in titles and snippets |
| `titleDataSourceType`, `snippetDataSourceType` | Title data source; snippet data source |
| `documentLanguage`, `queryLanguage` | Locale of the document; locale of the query |
| `browserWidth` | Browser width |

### `QualityPreviewSnippetBrainFeatures` and `QualityPreviewChosenSnippetInfo`

`QualityPreviewSnippetBrainFeatures` describes itself as "Snippet brain scores". It has two fields: `modelScore`, the score from the SnippetBrain model, and `isSnippetBrainBoldingTriggered`, whether bolding was triggered `API Docs` ([v0.4.0 reference](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.QualityPreviewSnippetBrainFeatures.html)).

`QualityPreviewChosenSnippetInfo` holds information for the chosen snippet `API Docs` ([v0.4.0 reference](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.QualityPreviewChosenSnippetInfo.html)). Its `source` field says the source of the chosen snippet is decided in "PORC". Other fields record the rendered snippet HTML, whether it ends with an ellipsis, and whether it is a "vulgar candidate" `API Docs` (same page). The documentation does not expand PORC, so this handbook does not either.

[Chapter 7](07-site-level-quality-signals.md), section 7.7, covers a separate site-level field, `titlematchScore`, described as how well a site's titles match user queries.

### Reading these fields correctly

**What we can say:**

- Google's internal documentation defines several title and snippet candidates per result, and records which one was selected. This agrees with the public statement that Google picks from several sources (section 9.2). Here `API Docs` and `Official` agree.
- It records how much of the query the title and snippet cover, the languages of the document and query, and the browser width. These match public statements that snippets depend on the query and are truncated to the device width (section 9.5).
- A model named SnippetBrain can score snippets and can override the first choice.

**What we cannot say:**

- what SnippetBrain is, how it is trained, or how often it is triggered;
- whether query term coverage in titles feeds ranking. The module is a feature export "for ranklab". Its description does not say what ranklab does with the features;
- whether any field was in use when the documentation leaked, or now.

---

## 9.10 Do titles affect ranking?

This question is separate from how titles are displayed, and the documentation cited in this chapter is about display.

- **`Official`** — Google's guide to how Search works says Google analyses the text of a page and key tags and attributes such as `<title>` (covered in [Chapter 2](02-how-search-works.md), section 2.5).
- **`API Docs`** — The site-level `titlematchScore` field ([Chapter 7](07-site-level-quality-signals.md)) and the title query-coverage features above show that Google records how titles relate to queries.

`Inference`: the `<title>` element is part of what Google reads to understand a page, so it can plausibly affect relevance. No source in this chapter states how much it weighs. The title link Google shows does not prove what text was used for ranking. A rewritten title link does not mean your `<title>` element was ignored for understanding the page.

---

## 9.11 Putting it together

| Question | Best evidence | Label | Strength |
|---|---|---|---|
| Where can a title link come from? | Title link documentation | `Official` | Direct list of nine sources |
| How often is the `<title>` element used? | Sept 2021 blog post | `Official` | About 87% in 2021; no current figure |
| Does the title link change by query? | Aug 2021 blog post | `Official` | Generally no, since 2021 |
| Does the snippet change by query? | Snippet documentation | `Official` | Yes |
| Is the meta description always used? | Snippet documentation | `Official` | No, only when it fits better |
| Is there a length limit? | Title and snippet documentation | `Official` | No; truncated to device width |
| Can I block or shorten snippets? | Robots meta tag specification | `Official` | Yes; also covers AI Overviews and AI Mode |
| Can I request a featured snippet? | Featured snippets documentation | `Official` | No |
| Does Google score title and snippet candidates? | `SnippetsRanklabFeatures`, `SnippetBrainFeatures` | `API Docs` | Fields exist; weights unknown |

---

## 9.12 Checklist: titles and snippets

- [ ] **Write a unique, specific `<title>` for every page.** It is still the most common source of the title link `Official` (sections 9.3, 9.4).
- [ ] **Make the visible headline agree with the `<title>`.** Google compares them and uses the heading when the title is stale or empty `Official` (section 9.2).
- [ ] **Update recurring pages fully.** A new year in the heading but an old year in the title invites a rewrite `Official` (section 9.2).
- [ ] **Remove boilerplate.** Replace shared or near-identical titles with titles that reflect each page `Official` (section 9.4).
- [ ] **Keep titles and pages in the same language and script** `Official` (section 9.4).
- [ ] **Add `WebSite` structured data with your site name** and an `alternateName` `Official` (section 9.8).
- [ ] **Write meta descriptions as summaries, not keyword lists.** Expect Google to replace them for many queries `Official` (section 9.5).
- [ ] **Check rewrites in context.** If Google rewrites a title and no listed problem applies, ask whether its version fits the query better `Official` ([title link documentation](https://developers.google.com/search/docs/appearance/title-link?hl=en&rd=1)).
- [ ] **Use `nosnippet`, `max-snippet` and `data-nosnippet` deliberately.** They affect AI features as well as classic results `Official` (section 9.6).
- [ ] **Do not judge relevance by the displayed title.** Display and ranking are separate questions `Inference` (section 9.10).

---

## Sources for this chapter

| # | Source | Type | Checked |
|---|---|---|---|
| 1 | Google Search Central — [Influencing your title links in search results](https://developers.google.com/search/docs/appearance/title-link?hl=en&rd=1) (last updated 2025-12-10) | Official | 2026-11-26 |
| 2 | Google Search Central Blog — [An update to how we generate web page titles](https://developers.google.com/search/blog/2021/08/update-to-generating-page-titles?hl=en) (24 Aug 2021) | Official | 2026-11-26 |
| 3 | Google Search Central Blog — [More information on how Google generates titles for web page results](https://developers.google.com/search/blog/2021/09/more-info-about-titles) (17 Sep 2021) | Official | 2026-11-26 |
| 4 | Google Search Central — [Control your snippets in search results](https://developers.google.com/search/docs/advanced/appearance/snippet) (last updated 2026-04-20) | Official | 2026-11-26 |
| 5 | Google Search Central — [Robots meta tag, data-nosnippet, and X-Robots-Tag specifications](https://developers.google.com/webmasters/control-crawl-index/docs/robots_meta_tag) (last updated 2026-03-24) | Official | 2026-11-26 |
| 6 | Google Search Central — [Featured snippets and your website](https://developers.google.com/search/docs/appearance/featured-snippets?hl=en) (last updated 2025-12-10) | Official | 2026-11-26 |
| 7 | Google Search Central Blog — [An update on site names](https://developers.google.com/search/blog/2023/07/sitenames) (28 Jul 2023) | Official | 2026-11-26 |
| 8 | HexDocs — [`MustangReposWwwSnippetsSnippetsRanklabFeatures`, v0.4.0](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.MustangReposWwwSnippetsSnippetsRanklabFeatures.html) | API Docs | 2026-11-26 |
| 9 | HexDocs — [`QualityPreviewSnippetBrainFeatures`, v0.4.0](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.QualityPreviewSnippetBrainFeatures.html) | API Docs | 2026-11-26 |
| 10 | HexDocs — [`QualityPreviewChosenSnippetInfo`, v0.4.0](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.QualityPreviewChosenSnippetInfo.html) | API Docs | 2026-11-26 |

Notes on this check: the title link, snippet, robots meta tag and featured snippet pages were read directly. The three blog posts were read through extracted article text, because the pages open with a long archive list; their dates, authors and figures come from that text. The current site names documentation page could not be fetched, so section 9.8 relies on the July 2023 blog post only. The `titlematchScore` field was not re-checked for this chapter; it is cited from Chapter 7. Leaked field descriptions are paraphrased, with one short quote.

---

<a id="next-chapter"></a>*Next chapter (planned): Freshness — what Google says about recent content, dates on pages, and query deserves freshness.*
