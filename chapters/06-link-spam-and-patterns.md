# Chapter 6 — Link Spam and Patterns

> **Status:** Draft v0.1 · **Last verified:** 2026-11-23 · **Author:** [Saeed Yeganeh](https://saeedyeganeh.com/en/)

[Chapter 5](05-links-and-how-they-are-weighted.md) looked at how links are weighted when they are treated as genuine. This chapter looks at the other side. What does Google count as link spam? How does it say it detects it? What happens to a site that buys, sells or attracts spammy links? And what does the leaked API documentation add about how spammy anchor text is handled?

The evidence here is unusually strong on the *policy* side. Google publishes a detailed list of link practices it treats as spam, and its help pages describe the manual actions in detail. The evidence is thinner on the *algorithmic* side. Google names its systems (Penguin, SpamBrain) and describes what they do in one or two sentences. The API documentation describes one anchor-spam component in more detail, but without weights or thresholds.

---

## 6.1 What Google defines as link spam

Google's spam policies define link spam by purpose. It is the creation of links to or from a site *mainly to manipulate search rankings* `Official` ([Spam policies, "Link spam"](https://developers.google.com/search/docs/essentials/spam-policies?hl=en)). The definition covers links in both directions. Selling links from your site is covered as much as buying links to it.

The same section lists examples `Official` (same page). In summary:

| Group | Examples Google lists |
|---|---|
| Paying for links | Money for links or for posts containing links; goods or services for links; sending a product in exchange for a review that includes a link |
| Exchanges | Excessive "link to me and I'll link to you" swaps; partner pages that exist only to cross-link |
| Automation | Automated programs or services that create links to your site |
| Forced links | Requiring a link in terms of service, a contract or a similar agreement, without letting the content owner qualify it |
| Ads that pass credit | Text ads or text links that do not block ranking credit; advertorials or native ads where paid articles contain links that pass credit |
| Anchor-text placement | Links with optimised anchor text in articles, guest posts or press releases on other sites |
| Low-quality placements | Low-quality directory or bookmark links; keyword-rich, hidden or low-quality links in widgets spread across sites; widely distributed footer or template links; forum comments with optimised links in the post or signature |
| Content made for links | Low-value content created mainly to manipulate linking and ranking signals |

### Paid links are not banned in themselves

The policy says Google understands that buying and selling links is a normal part of web advertising and sponsorship `Official` (same page). Such links do not break the policy if they are qualified with `rel="nofollow"` or `rel="sponsored"` `Official` (same page). [Chapter 5](05-links-and-how-they-are-weighted.md), section 5.2, covers these attributes.

**What we can say:** the line Google draws is not "money changed hands". It is whether a paid or arranged link is allowed to pass ranking credit.

**What we cannot say:** how Google decides that a link which is *not* labelled was paid for. The policy lists patterns. It does not describe the detection method.

### How violations are found and what they cost

The policies page says Google detects violations through automated systems and, when needed, human review that can lead to a manual action `Official` (same page). It also says sites that violate the policies may rank lower or not appear at all `Official` (same page). The page was last updated on 2026-08-28.

---

## 6.2 The automated systems: from Penguin to SpamBrain

### Penguin

Google's ranking systems guide lists Penguin among its retired systems. It describes Penguin as a system built to fight link spam, launched in 2012, and later folded into Google's core ranking systems `Official` ([ranking systems guide, "Retired systems"](https://developers.google.com/search/docs/appearance/ranking-systems-guide)).

The 2016 announcement, by Gary Illyes, gives more detail ([Penguin is now part of our core algorithm, 23 Sep 2016](https://developers.google.com/search/blog/2016/09/penguin-is-now-part-of-our-core)). The post made two changes public `Official`:

- Penguin became **real-time**.
- Penguin became **more granular**. It devalues spam by adjusting ranking based on spam signals, rather than affecting the ranking of the whole site.

**What we can say:** since 2016, Google has described its main algorithmic response to link spam as *devaluing* the spam, not punishing the whole site.

**What we cannot say:** that no algorithmic link problem can ever affect a whole site. The post describes Penguin's design. It does not rule out other systems.

### Link spam updates and SpamBrain

Google later announced named "link spam updates".

- **July 2021.** A post by Duy Nguyen announced a link spam update and described it as making Google more effective at identifying and *nullifying* link spam across languages `Official` ([A reminder on qualifying links and our link spam update, 26 Jul 2021](https://developers.google.com/search/blog/2021/07/link-tagging-and-link-spam-update)). The post said that when sites take part in link spam, those links are re-assessed by its algorithms `Official` (same post). It gave the rollout as about two weeks `Official` (same post).
- **December 2022.** A post announced that Google was using SpamBrain to neutralise the impact of unnatural links `Official` ([December 2022 link spam update, 14 Dec 2022](https://developers.google.com/search/blog/2022/12/december-22-link-spam-update)). It said SpamBrain could now detect both sites that buy links and sites used to pass outgoing links `Official` (same post). It said that credit passed by unnatural links may be lost, which can change rankings `Official` (same post). Rollout was again about two weeks `Official` (same post).

The ranking systems guide describes SpamBrain as one of several systems Google uses to detect content and behaviour that break its spam policies, updated over time as spam changes `Official` ([ranking systems guide, "Spam detection systems"](https://developers.google.com/search/docs/appearance/ranking-systems-guide)).

**What we can say:** Google's public language about algorithmic link spam has been consistent since 2016. Penguin "devalues", the 2021 update "nullifies", and the 2022 update "neutralises". All three describe removing the value of the spammy links.

**`Inference`:** for a site hit only by the algorithms, the practical effect is likely to look like *lost credit* rather than a penalty. Rankings that were held up by bought links fall back to what the remaining links support. Google does not state this outcome in these words.

**What we cannot say:** how SpamBrain identifies a link-selling site, what features it uses, or how much it relies on machine learning. The posts do not say.

---

## 6.3 Affiliate, sponsored and guest-post links

The July 2021 post addressed three common cases `Official` ([26 Jul 2021 post](https://developers.google.com/search/blog/2021/07/link-tagging-and-link-spam-update)):

- **Affiliate links.** Using affiliate links to earn money is generally fine. When sites fail to qualify affiliate links appropriately, Google may issue manual actions.
- **Sponsored and guest posts.** Google strongly recommends applying the right `rel` values to links in these posts. Algorithmic and manual actions may be applied, as with affiliate links.

This matches the "Anchor-text placement" and "Ads that pass credit" rows in section 6.1.

**What we can say:** a guest post or sponsored article is not spam because of its format. The risk comes from links in it that pass credit without a label.

---

## 6.4 Manual actions for links

A manual action is issued when a human reviewer at Google decides that pages on a site do not comply with the spam policies `Official` ([Manual actions report](https://support.google.com/webmasters/answer/9044175?hl=en)). The report in Search Console lists three link-related types. They differ in what Google did and in what the owner must do.

### "Unnatural links to your site"

Google has found a pattern of unnatural, artificial, deceptive or manipulative links pointing to the site `Official` (same page). The recommended steps are, in summary `Official` (same page):

1. Read the link spam policy.
2. Export the site's links from Search Console.
3. Check for links that break the policy, starting with top linking sites or recent links.
4. Ask the linking sites to remove the links or to stop them passing PageRank, for example with `nofollow`.
5. Disavow the links that could not be removed.
6. Request a review, with notes on what was removed and disavowed.

The page warns against shortcuts. Adding all backlinks to a disavow file is not treated as a good-faith effort, and disavowing everything without trying to remove links may lead to the request being rejected `Official` (same page). It also warns against disavowing organic links `Official` (same page).

### "Unnatural links to your site — impacts links"

This variant is different. Google says it has not acted on the site's overall ranking. It has instead "applied a targeted action to the unnatural links" `Official` ([Unnatural links to your site—impacts links](https://support.google.com/webmasters/answer/2604772?hl=en)). If the owner does not control those links, no action is required, because the links already do not count in ranking `Official` (same page). The owner may still remove them and request reconsideration `Official` (same page).

### "Unnatural links from your site"

Here the problem is outbound. Google has found a pattern of unnatural, artificial, deceptive or manipulative links *on* the site `Official` ([Manual actions report](https://support.google.com/webmasters/answer/9044175?hl=en)). The fix is to find paid or otherwise violating outbound links, then remove them or change them so they no longer pass PageRank, and then request a review `Official` (same page).

### Reconsideration

A review should be requested only when the issues are fixed on all affected pages `Official` (same page). Most reviews take several days or weeks. Link-related requests may take longer than usual `Official` (same page).

### Comparison

| Manual action | Who is affected | Must the owner act? |
|---|---|---|
| Unnatural links to your site | The site's ranking | Yes: clean up, disavow what remains, request review |
| Unnatural links to your site — impacts links | Only the links | No, if the owner does not control the links |
| Unnatural links from your site | The site, for its outbound links | Yes: remove or qualify links, request review |

---

## 6.5 The disavow tool

The disavow tool lets an owner ask Google to ignore specific links ([Disavow links to your site](https://support.google.com/webmasters/answer/2648487?hl=en)). Google's help page sets narrow conditions for using it `Official` (same page):

- In most cases, Google can judge which links to trust without help, so most sites will not need the tool.
- It describes the tool as advanced, to be used with caution.
- Use it only when **both** are true: there are a considerable number of spammy, artificial or low-quality links to the site, **and** they have caused, or likely will cause, a manual action.
- Try to remove the links first. Disavow only those that cannot be removed.

The file rules, from the same page `Official`:

- One URL or domain per line. A whole domain is written with the `domain:` prefix. A subpath such as `example.com/en/` cannot be disavowed.
- Lines starting with `#` are comments and are ignored.
- The file must be a `.txt` file in UTF-8 or 7-bit ASCII. The limit is 100,000 lines (including blank and comment lines) and 2 MB. URLs may be up to 2,048 characters.
- A new upload replaces the previous list for that property. A file with errors does not replace the old one.
- The list applies to the property it was uploaded to and its child properties. Domain properties are not supported.
- It can take a few weeks for the list to take effect, as Google recrawls the web.
- Disavowed links still appear in the Links report.

**What we can say:** Google presents disavow as a repair tool for manual-action situations, not as routine maintenance.

**What we cannot say:** that disavowing links has no effect outside manual actions. The help page does not say that either way.

---

## 6.6 What the leaked API documentation adds: anchor spam

The Content Warehouse reference (see [Chapter 1](01-reading-seo-evidence.md), section 1.2) includes a module that summarises the output of a component called `AnchorSpamPenalizer` ([`IndexingDocjoinerAnchorSpamInfo`, v0.4.0](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.IndexingDocjoinerAnchorSpamInfo.html)). [Chapter 5](05-links-and-how-they-are-weighted.md) mentioned it briefly. This section reads all of its 22 fields.

The module description says spammy anchors are tagged with `LINK_SPAM_PHRASE_PENALIZER` and demoted to a "SPAM locality" `API Docs` (same page). The fields fall into four groups `API Docs` (same page):

| Group | Fields | What the descriptions say |
|---|---|---|
| Classification signals | `phraseCount`, `phraseFraq`, `phraseDays`, `phraseRate` | Spam phrases found across unique domains; their share of all anchors; over how many days 80% of them were found; the average daily rate of spam-anchor discovery |
| Prediction | `spamProbability`, `spamPenalty` | A predicted probability of spam; a combined penalty for anchor demotion |
| Demotion record | `demoted`, `demotedAll`, `demotedStart`, `demotedEnd`, `anchorFraq` | How many anchors were demoted; whether all anchors in the period were demoted or only those classed as spam; the demotion period; the ratio of demoted period to the whole anchor period |
| Trusted sources | `trustedTotal`, `trustedTarget`, `trustedDemoted`, `trustedMatching`, `trustedExamples`, `sources` | How many trusted sources point to the URL; whether the URL is itself on a trusted source; trusted anchors used in the spam-probability computation; trusted anchors whose text matches spam terms; examples |

Other fields record the first and last anchor dates (`anchorStart`, `anchorEnd`), the number of anchors processed, whether anchors were sampled, and debug information `API Docs` (same page).

### Reading these fields correctly

**What we can say:**

- The documented component looks at anchor *text*, specifically spam phrases, not just at the linking sites.
- Speed matters to it. Two fields measure how quickly spam anchors appear (`phraseDays`, `phraseRate`).
- Demotion has a time window, and it can apply either to all anchors in that window or only to the spam-classed ones (`demotedAll`).
- Anchors from trusted sources are counted separately and feed into the spam-probability computation.

**What we cannot say:**

- what counts as a "spam phrase" or a "trusted source";
- the threshold at which anchors are demoted, or how large the penalty is;
- whether this component is the same thing as Penguin or SpamBrain. The documentation names neither, and this handbook does not link them;
- whether the component was in use when the documents leaked, or is in use now.

**`Inference`:** the fields suggest the component reacts to a *burst* of anchors with spam-like text, checked against what trusted sources say about the same page. That fits the policy examples of optimised anchor text in guest posts, widgets and forum signatures. It is a reading of field names and descriptions, not a documented rule.

---

## 6.7 Putting it together

| Question | Best evidence | Label | Strength |
|---|---|---|---|
| What is link spam? | Spam policies, "Link spam" | `Official` | Direct definition and examples |
| Are paid links allowed? | Same: yes, if qualified with `nofollow` or `sponsored` | `Official` | Direct statement |
| Does the algorithm punish or ignore spammy links? | Penguin 2016, link spam updates 2021 and 2022 | `Official` | Consistent wording: devalue, nullify, neutralise |
| Can a link-selling site be detected? | December 2022 post on SpamBrain | `Official` | Stated; method not described |
| What does a links manual action require? | Manual actions report; "impacts links" page | `Official` | Detailed steps |
| When should disavow be used? | Disavow help page | `Official` | Narrow, stated conditions |
| How is anchor-text spam handled internally? | `IndexingDocjoinerAnchorSpamInfo` | `API Docs` | Fields exist; thresholds and current use unknown |

---

## 6.8 Checklist: auditing link risk

- [ ] **Label every paid or arranged link** you place or sell: ads, sponsorships, affiliate links, guest posts and product-for-review deals. Use `sponsored` (or `nofollow`).
- [ ] **Check outbound links too.** The policy covers links *from* your site. Look at footers, templates, widgets and old sponsored posts.
- [ ] **Do not require links in contracts or terms** unless the other side is free to qualify them.
- [ ] **Check Search Console's Manual actions report** before deciding anything. The right response depends on which link action, if any, is listed.
- [ ] **Do not disavow by default.** Google says most sites do not need it. Keep it for cases of many spammy links tied to a real or likely manual action.
- [ ] **If you disavow, remove first and document.** A blanket disavow file is not treated as a good-faith effort.
- [ ] **Watch for sudden bursts of keyword-rich anchors** pointing at your pages. That is the pattern the documented anchor-spam fields measure. `Inference` from section 6.6.
- [ ] **Expect lost credit, not a quick fix.** If bought links are neutralised, rankings that depended on them may not return. `Inference` from section 6.2.

---

## Sources for this chapter

| # | Source | Type | Checked |
|---|---|---|---|
| 1 | Google Search Central — [Spam policies for Google web search](https://developers.google.com/search/docs/essentials/spam-policies?hl=en), section "Link spam" (last updated 2026-08-28) | Official | 2026-11-23 |
| 2 | Google Search Central — [A guide to Google Search ranking systems](https://developers.google.com/search/docs/appearance/ranking-systems-guide), sections "Spam detection systems" and "Retired systems" (last updated 2025-12-18) | Official | 2026-11-23 |
| 3 | Google Search Central Blog — [Penguin is now part of our core algorithm (23 Sep 2016)](https://developers.google.com/search/blog/2016/09/penguin-is-now-part-of-our-core) | Official | 2026-11-23 |
| 4 | Google Search Central Blog — [A reminder on qualifying links and our link spam update (26 Jul 2021)](https://developers.google.com/search/blog/2021/07/link-tagging-and-link-spam-update) | Official | 2026-11-23 |
| 5 | Google Search Central Blog — [December 2022 link spam update (14 Dec 2022)](https://developers.google.com/search/blog/2022/12/december-22-link-spam-update) | Official | 2026-11-23 |
| 6 | Search Console Help — [Manual actions report](https://support.google.com/webmasters/answer/9044175?hl=en) | Official | 2026-11-23 |
| 7 | Search Console Help — [Unnatural links to your site—impacts links](https://support.google.com/webmasters/answer/2604772?hl=en) | Official | 2026-11-23 |
| 8 | Search Console Help — [Disavow links to your site](https://support.google.com/webmasters/answer/2648487?hl=en) | Official | 2026-11-23 |
| 9 | HexDocs — [`IndexingDocjoinerAnchorSpamInfo`, google_api_content_warehouse v0.4.0](https://google-api-content-warehouse.hexdocs.pm/0.4.0/GoogleApi.ContentWarehouse.V1.Model.IndexingDocjoinerAnchorSpamInfo.html) | API Docs | 2026-11-23 |

Notes on this check: source 2 was served in its Russian-language version, so its statements are paraphrased from that version. The article bodies of sources 3, 4 and 5 were read through an extracted summary, so they are paraphrased, not quoted.

---

<a id="next-chapter"></a>*Next chapter (planned): Site-level quality signals — what Google says about site-wide signals, and what the court record and API documentation show.*
