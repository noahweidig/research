---
title: 'Understanding the wildfire adaptation communications landscape in the western United States: examining actors, media type, and geographies'
authors:
- Sachdeva, Sonya S.
- Johnson, Michelle Leigh
- Sachs, Jeff
- Hixson, Kathryn
year: '2026'
journal: Fire Ecology
doi: 10.1186/s42408-026-00576-3
tags:
- prescribed burning
- united states
- western united states
- wildfire
zotero_key: E3QRQTU5
item_type: journalArticle
url: https://openalex.org/W7221651948
source_url: 'unpaywall: https://link.springer.com/content/pdf/10.1186/s42408-026-00576-3.pdf'
fulltext_status: fulltext
synced: '2026-11-09'
---

# Understanding the wildfire adaptation communications landscape in the western United States: examining actors, media type, and geographies

## Abstract

Abstract Adaptations to living with fire are multifold, and U.S. wildfire policy has increasingly shifted toward proactive management. The U.S. Forest Service’s Wildfire Crisis Strategy (WCS) provides coordination and funding for landscape-scale adaptation, yet little is known about how wildfire adaptation is communicated in public online discourse. We analyze press releases, news media, and social media texts from September 2022 to February 2024 to characterize the salience and framing of wildfire adaptation concepts, identify which organizational types are most associated with major themes, and examine geographic variation across ten initial WCS landscapes. Using paragraph-level topic modeling and thematic clustering, we find that wildfire adaptation communication is dominated by prescribed fire, but that most adaptation concepts represented in the Fire Adapted Communities wheel appear across channels. Prescribed fire discourse is internally differentiated (operations, weather windows, and risk/safeguards), and thematic emphasis varies by platform and communicator type. We also observe meaningful state-level variation in adaptation themes within Twitter/X data, consistent with differences in fire history, governance context, and public attention. Together, these findings map a distributed wildfire adaptation communication ecosystem and highlight where key adaptation elements (e.g., codes, ordinances, and continuity planning) remain comparatively absent from public-facing discourse.

## Full text

Sachdeva _et al. Fire Ecology          (2026) 22:156_ https://doi.org/10.1186/s42408-026-00576-3 

Fire Ecology 



**Open Access** 

## **RESEARCH** 



# Understanding the wildfire adaptation communications landscape in the western United States: examining actors, media type, and geographies 

Sonya Sachdeva<sup>1*</sup> , Michelle L. Johnson<sup>2</sup> , Jeff Sachs<sup>3</sup> and Kathryn Hixson<sup>4</sup> 

### **Abstract** 

Adaptations to living with fire are multifold, and U.S. wildfire policy has increasingly shifted toward proactive management. The U.S. Forest Service’s Wildfire Crisis Strategy (WCS) provides coordination and funding for landscapescale adaptation, yet little is known about how wildfire adaptation is communicated in public online discourse. We analyze press releases, news media, and social media texts from September 2022 to February 2024 to characterize the salience and framing of wildfire adaptation concepts, identify which organizational types are most associated with major themes, and examine geographic variation across ten initial WCS landscapes. Using paragraph-level topic modeling and thematic clustering, we find that wildfire adaptation communication is dominated by prescribed fire, but that most adaptation concepts represented in the Fire Adapted Communities wheel appear across channels. Prescribed fire discourse is internally differentiated (operations, weather windows, and risk/safeguards), and thematic emphasis varies by platform and communicator type. We also observe meaningful state-level variation in adaptation themes within Twitter/X data, consistent with differences in fire history, governance context, and public attention. Together, these findings map a distributed wildfire adaptation communication ecosystem and highlight where key adaptation elements (e.g., codes, ordinances, and continuity planning) remain comparatively absent from publicfacing discourse. 

**Keywords** Wildfire adaptation, Communication, Natural language processing, Climate change 

### **Introduction** 

Wildfire management in the western USA has been shifting from a suppression-dominant paradigm toward “living with fire,” with agencies and communities investing in proactive adaptation—the policies, practices, and social arrangements that enable human and ecological systems 

*Correspondence: Sonya Sachdeva sonyasachdeva@u.northwestern.edu 1 Environment, Policy & Culture, Northwestern University, Evanston, IL, USA 2 City University of New York Graduate Center, New York, NY, USA 3 Yale University, New Haven, USA 4 Portland State University, Portland, OR, USA 

to coexist with fire as a recurring disturbance (BrenkertSmith et al. 2017)—rather than relying on suppression alone (Pyne 1982; Moritz et al. 2014). Frameworks such as the Fire Adapted Communities wheel and the Fire Menu codify a wide range of actionable practices, from defensible space to prescribed fire and cultural burning (FAC Net 2021; Sample et al. 2022). However, communication surrounding wildfire has remained largely event-driven and hazard-centric, emphasizing crisis and suppression over systemic adaptation (Morehouse and Sonnett 2010; Crow et al. 2017; Nilsson & Enander 2020; Paveglio et al. 2011; Mercer & Prisbrey 2004). Recent assessments continue to find sparse coverage of prescribed fire and other wildfire adaptation measures in 

> © The Author(s) 2026. **Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/. 

Sachdeva _et al. Fire Ecology          (2026) 22:156_ 

Page 2 of 20 

regional media (Wilson 2024). This misalignment matters because public communication does not simply report on wildfire adaptation but helps constitute it: what receives sustained coverage tends to gain institutional priority and funding, while what goes uncovered can stall regardless of its technical merit (McCombs and Shaw 1972; Entman 1993). Better-aligned communication, one that gives systemic adaptation practices comparable visibility to crisis and suppression coverage, would plausibly widen public and institutional support for the fuller range of adaptation tools; the current gap helps explain why, despite growing recognition of cultural burning, staffing and funding still favor suppression over planned fire, constraining implementation (Ingalsbee 2017; Marks-Block and Tripp 2021). Within the context of this communication gap, this study documents how wildfire adaptation is currently communicated in media landscapes across the western United States, examining _who_ communicates about adaptation, _what_ adaptation concepts are emphasized, and _how_ these patterns vary across landscapes identified in the USDA Forest Service’s wildfire priority areas (USFS 2022). 

The study of wildfire communication builds on broader scholarship on hazards and risk communication; although this literature has focused mainly on other hazard domains rather than wildfire specifically, it establishes general findings on how information flows, framing, and trust shape public responses to complex hazards (Tierney 2014; Wachinger et al. 2013). In many hazard domains, including flood, drought, hurricanes, and earthquake risk, researchers have shown that communication focusing solely on hazard warning can obscure opportunities for proactive adaptation and reduce longterm resilience (Morss et al. 2017; Paton 2008; Rollason et al. 2018). Wildfire presents similar challenges as attention spikes during crisis periods and wanes during intervals when adaptation planning and capacity-building could occur (Steelman& McCaffrey 2013). Integrating adaptation more prominently into wildfire discourse may therefore be important for achieving equitable, long-term hazard mitigation outcomes. 

Against this broader backdrop, the USDA Forest Service launched its Wildfire Crisis Strategy (WCS) in 2022 to address escalating wildfire risk by accelerating landscape-scale fuel treatments and investments in community and forest resilience (USFS 2022). The strategy elevated proactive adaptation as a national priority, identifying specific landscapes for focused investment rather than relying primarily on suppression and postfire recovery. As introduced above, wildfire adaptation encompasses the policies, practices, and social arrangements that enable human and ecological systems to coexist with fire as a recurring disturbance (Brenkert-Smith 

et al. 2017); in the U.S. context, this includes actions across multiple scales: household-level defensible space, community-level planning and zoning, landscape-scale fuel treatments, and governance arrangements that integrate Indigenous fire stewardship and prescribed fire into management regimes (Abrams et al. 2015; Edgeley & Paveglio 2024). Conceptually, wildfire adaptation aligns with broader climate and hazard adaptation frameworks that emphasize iterative learning, social capacity, and institutional flexibility in the face of chronic risk. As such, and consistent with framing and social-constructionof-risk perspectives in communication research, communication about wildfire adaptation is not simply the dissemination of technical practices, but a social process that shapes how communities interpret risk, legitimacy, and responsibility in a changing fire regime (Entman 1993; Tierney 2014). A baseline assessment of the ten initial WCS landscapes documents substantial variation in social settings, prior fuel-treatment activity, and county-level planning and regulatory tools, highlighting the different contexts in which WCS implementation is occurring (Anderson et al. 2025). Understanding how adaptation is represented and communicated across these contexts is therefore critical for assessing both the diffusion of adaptation concepts and the social conditions under which they gain traction. 

Communication about wildfire adaptation in the United States unfolds within a decentralized information environment that mixes official agency releases, news reporting, and platform-specific social media dynamics. Prior work documents inconsistencies in how risks are framed across sources and channels, reflecting different audiences, norms, and mental models (Brenkert et al. 2005; McCaffrey 2004; Paveglio et al. 2009; Remenick 2018; Jacobson et al. 2022). Platforms differ in user composition and affordances, with some social media platforms privileging rapid alerts over contextual explanations or over community learning—the slower, dialogic exchange of knowledge, questions, and shared experience among residents and organizations that supports collective adaptation capacity over time (Olteanu et al. 2015; Malik & Pfeffer 2016; Gligoric et al. 2018; Babić et al. 2021). Furthermore, decentralization and distrust can amplify variation across communities and networks (Bossetta 2018; Kreiss and McGregor 2018): as trust in national news and institutions has declined and social media platforms have proliferated and rapidly changed their moderation, algorithms, and ownership, wildfire information competes with, and is sometimes displaced by, misinformation, which can undermine accurate public understanding of adaptation practices such as prescribed fire (Jones et al. 2022). We focus on these mediated communication channels because they are the primary venue 

Sachdeva _et al. Fire Ecology          (2026) 22:156_ 

Page 3 of 20 

through which agencies and other organizations can reach broad, geographically dispersed publics at scale; interpersonal communication (e.g., neighbor-to-neighbor, community meetings) likely also shapes adaptation attitudes and behavior, but is outside the scope of the text corpora analyzed here. Because different platforms and organizational voices reach different publics, a single-channel view of wildfire adaptation communication risks describing only part of the picture and, by extension, only part of who has access to adaptation information; a comparative, multi-channel view is needed so that gaps in one channel (e.g., underrepresentation of a topic on Twitter/X) can be checked against coverage elsewhere before concluding that a landscape or population is underserved. Local social context plays a role in support and acceptance of adaptation efforts (Paveglio et al. 2019), and this relationship likely runs in both directions: just as local context shapes what gets communicated and how, variation in local communication landscapes may 

itself constitute part of the social context that different communities bring to adaptation planning. 

The overarching objective of this paper is to document the current digital wildfire adaptation public communications landscape in the western United States. Context has been shown to create variation from place to place; we examine this potential variation in media communications at the landscape level. Here, we examine print news media and social media texts to understand the present saliency of wildfire adaptation concepts, across a range of organizational types, information channels, and geographic scales—by which we mean the WCS landscape level (10 priority landscapes, Fig. 1) and, for Twitter/X data specifically, the U.S. state level (the “Geographies” section)l This reference to geographic scale is distinct from the text scales (sentence, paragraph, document) discussed in Sect. “Data Processing and Analysis.” We use these data to understand which types of organizations are most likely to be associated with each 



**Fig. 1** Study area map 

Sachdeva _et al. Fire Ecology          (2026) 22:156_ 

Page 4 of 20 

category of adaptation. We compare these texts to WCS press releases to understand whether adaptation topics communicated by the USFS differ from those shared by other organizations. Additionally, we also examine whether and how the communication landscape differs across geographies, through examining wildfire adaptation communications for 10 WCS landscapes. We focus on media communications, both traditional print and digital, to enable this breadth of scope and comparisons across landscapes. 

### **Methods** 

#### **Data collection** 

We collected text data, typically original posts and comments, when available, from six information channels: the USFS WCS Tracker (an internal database of Forest Service Wildfire Crisis Strategy press releases), mass media, and social media (Facebook, Reddit, Twitter/X, and Instagram). We selected these three broad media types because they offer complementary vantage points on the same discourse: WCS Tracker press releases represent official agency framing, mass media represents professionally edited journalistic coverage, and social media represents largely user-generated, grassroots communication; comparing across these types was central to our first guiding question of who communicates about wildfire adaptation. Our collection timeframe (September 2022 to February 2024) was chosen to begin at the WCS’s initial designation of its ten priority landscapes in 2022 and captures roughly 18 months of subsequent communication; we discuss the limitations of this relatively short, fixed window in Sect. “Limitations and future research.” Text data ranged in length from individual tweets (280 characters) to in-depth news articles and press releases. We focused this data collection on 10 initial landscapes identified by the WCS (Fig. 1). As such, we parsed our mass media sample, collected using ProQuest TDM’s U.S. Newsstream, to include articles only from regional newspapers located in states with WCS landscapes (Arizona, California, Colorado, Idaho, Montana, New Mexico, Oregon, and Washington) (ProQuest n.d.). This sample was limited to news articles; op-eds, letters to the editor, and editorials were excluded via ProQuest’s content-type filters. Relying on a single news aggregator is itself a limitation, since coverage varies across news databases; U.S. Newsstream is one of the more comprehensive aggregators available to academic researchers, but a comparison with other aggregators (e.g., Factiva, Nexis Uni) could surface additional relevant coverage (Gilbert et al. 2024). The ten initial WCS landscapes served as the organizing geographic frame 

for data collection but were not treated as discrete units in a comparative statistical analysis. The formal geographic comparison described in the “Geographies” section was conducted at the state level and was limited to Twitter/X, the only source with usable location metadata. 

We also limited data from the USFS WCS Tracker to only include communications related to the 10 WCS landscapes (Fig. 1). We collected social media data (Facebook, Reddit, Twitter/X, and Instagram) via the social listening platform Sprinklr (Sprinklr n.d.), a commercial service that aggregates and indexes public posts across multiple social networks for keyword-based querying; we accessed Sprinklr through an existing institutional license held by a university partner (see Acknowledgments). Our social media collection was not restricted to specific accounts or account types in advance; instead, Sprinklr returned public posts matching our keyword-and-state queries from any public account on each platform, and we subsequently coded the organizational type of accounts that appeared in the results (the “Organizational types” section) rather than sampling by account type. For all social media channels, our corpus included both original posts and their associated comments/replies, combined without distinguishing between the two in subsequent analyses; for Instagram specifically, this consisted of post captions and comment text (not other extracted content such as OCR from images). This differs from the USFS WCS Tracker and mass media samples, which by the nature of those sources (press releases; ProQuest news articles) do not include reader comments. 

For mass media and social media datasets, we limited our datasets with a set of 96 keywords related to wildfire adaptation, developed through an iterative process combining review of WCS and FAC Net terminology, pilot searches to test recall and precision, and the research team’s domain expertise (please see supplemental materials for the full list); these keywords were matched as Boolean queries against the full text of each document (not restricted to titles or specific fields), so a keyword could appear anywhere in a post or article to return a match. Location metadata were not available in our Sprinklr queries except for Twitter/X, so we collected these data for each keyword query by performing searches where each state name was appended to the keywords—e.g., instead of “prescribed fire”: “california” AND “prescribed fire.” Initial sample sizes varied across information sources. Our sample sizes for each information channel were as follows: USFS WCS: 215; News: 1462; Facebook: 4104; Reddit: 14,067; Twitter/X: 19,090; Instagram: 13,596. These counts reflect sample sizes where duplicates and null or empty entries have been removed. 

Sachdeva _et al. Fire Ecology          (2026) 22:156_ 

Page 5 of 20 

#### **Data processing and analysis** 

We analyzed the full collection of texts (the corpus) using topic modeling to derive emergent themes for each document (Fig. 2). Topic modeling is a natural language processing approach that identifies patterns of word co-occurrence and assigns coherent themes to text segments (Blei and Lafferty 2009). Throughout, we use “topic” to refer to the model-derived clusters of paragraph segments produced directly by BERTopic, and “theme” to refer to the broader, human-labeled categories we constructed by grouping related topics through the hierarchical clustering step described in the “Thematic clustering” section; this differs from the inductive, researcher-derived themes typical of qualitative or interpretive coding, in that the initial grouping is modeldriven and researchers subsequently interpret and label the resulting structure. We evaluated candidate models at three text scales (sentence, paragraph, whole document) by comparing, at each scale, the coherence and specificity of the resulting topic keywords and the ease with which two of the authors could assign an interpretable label to each topic from its keywords and representative excerpts; paragraph-level models built from five-sentence segments consistently yielded topics that were specific enough to label without excessive redundancy, whereas sentence-level models produced overly fragmented topics and whole-document models produced overly diffuse ones. Accordingly, we first segmented each document into five-sentence paragraphs, retaining any final, shorter segment as its own chunk when a document’s sentence 

count was not an exact multiple of five (this matters especially for social media posts, many of which are shorter than five sentences and were therefore analyzed as a single, sub-five-sentence chunk); then cleaned the text by lowercasing, removing punctuation, special characters, and stop words. Sentence tokenization and stop-word removal were implemented with the NLTK library in Python. We applied BERTopic (Grootendorst 2022) to the paragraph segments to estimate topic assignments and generate topic representations. 

#### **_Data filtering_** 

Our keyword search cast a wide net and returned many items unrelated to wildfire. To remove this noise, we first ran an unsupervised screening step using topic modeling with BERTopic in Python, but replaced BERTopic’s default density-based clustering with k-means. In our data, the default (HDBSCAN) assigned a large share of paragraphs to the “ − 1” (unclustered/noise) bin, and inspection showed that many of these were in fact wildfire-relevant but sparse or idiosyncratic (e.g., short notices, local updates). K-means groups items (here, paragraph-level text embeddings) into k clusters based on similarity; k is chosen in advance, and the algorithm iteratively assigns items to the nearest cluster center (“centroid”) until assignments stabilize. Using k-means ensured complete partitioning (no “unclustered” items), improving recall of potentially relevant material for human review. 



**Fig. 2** Flowchart showing data collection, preprocessing, topic modeling, and examining by attributes for wildfire adaptation text dataset 

Sachdeva _et al. Fire Ecology          (2026) 22:156_ 

Page 6 of 20 

We therefore generated a high-granularity BERTopic model with k = 1,000 topics. The high k acted as a safety valve against over-merging heterogeneous content: smaller, more specific topics made it easier to surface niche but on-topic material that density-based methods had treated as noise. Members of the research team reviewed each of the 1,000 topics using (i) the topic’s top keywords and (ii) a set of representative paragraphs drawn from that topic, and marked each topic as wildfirerelated or not; we did not calculate a formal intercoderreliability statistic (e.g., percent agreement or kappa) on this review, which we note as a limitation. “Domain knowledge” here refers to the reviewers’ familiarity with wildfire management terminology, agency programs (e.g., WCS, CWPP), and adaptation practices, which allowed them to distinguish genuine wildfire-adaptation content from superficially similar but unrelated material returned by the keyword search (e.g., general references to “burning” or “fuel” outside a wildfire context). As a guardrail against the risk of forcing unrelated items into topics, we treated ambiguous topics conservatively, retaining them for the second-stage adaptation screen described below rather than discarding them at this stage. 

Next, focusing only on wildfire-related topics, we conducted a second manual screen to isolate wildfire adaptation content (e.g., prescribed fire, defensible space, building codes, community preparedness). Using the same evidence (keywords and representative paragraphs), we retained topics whose content clearly pertained to adaptation. This reduced the 1,000 topics to 465 adaptation-related topics; documents containing any of these topics were kept for all subsequent analyses. 

#### **_Topic model_** 

We constructed topic models with BERTopic (Python), which chains together: (1) text embeddings (dense numeric vectors that capture semantic similarity), (2) dimensionality reduction to make clustering more stable, (3) clustering to form topics, (4) tokenization/ weighting to derive keywords, and (5) topic representations (human-readable labels/terms). We chose an automated topic-modeling approach over fully manual content coding because our corpus (over 52,000 documents across six information channels) exceeds what a small research team could code by hand within a reasonable timeframe; topic models of this kind have an established record in the social sciences as a means of estimating a coding scheme across large text corpora, at the cost of requiring researchers, rather than the model itself, to interpret and validate what a given topic represents (Blei and Lafferty 2009; DiMaggio et al. 2013). We treated this validation step as essential rather than optional: as described in the “Data filtering and 

“Thematic clustering” sections, every topic used in our final analysis was manually reviewed and labeled by the research team using its keywords and representative text segments, rather than accepted directly from the model output. 

To maintain comparability across sources (e.g., Facebook, news), we used a single, shared embedding model for the full corpus and then fit separate topic models per source. Embeddings were computed with the widely used _all-MiniLM-L6-v2_ sentence-transformer (SBERT family), a general-purpose English model suited to short and medium-length texts. The source-specific models were fitted to the corpus retained through this initial screening procedure. Thus, the 1,000 topics and 465 adaptation-related topics described in the “Data filtering” section refer to the initial screening model, whereas the topics subsequently grouped into the 11 themes were generated by the source-specific models described here. 

#### **_Thematic clustering_** 

To synthesize the resulting topics into broader themes, we applied agglomerative hierarchical clustering to the c-TF-IDF topic representations produced by BERTopic, using BERTopic’s default cosine-distance function and Ward linkage (Grootendorst 2022). We inspected solutions at two distance thresholds: a coarser solution at HC = 1.5 and a finer solution at HC = 1.0. We began with the coarser solution and, after manually reviewing topic keywords and representative paragraphs, divided groups that encompassed multiple distinct adaptation concepts according to the finer solution. We excluded residual non-adaptation groups at this stage, yielding 11 final themes for analysis; a catch-all “miscellaneous” group was also dropped. 

Once these themes were assigned to all documents (paragraph chunks), we examined their distribution for the entire corpus. To examine variation in theme prevalence across information channels, organizational types, and states, we constructed contingency tables crossing paragraph-level theme assignments with each grouping variable. Expected counts were calculated under the assumption of independence. We report Pearson standardized residuals, calculated as SR = (O − E)/ √ E, where O is the observed count and E is the expected count. Positive residuals indicate that a theme occurred more frequently than expected within a category, whereas negative residuals indicate that it occurred less frequently than expected. We used the residuals descriptively to characterize the direction and relative magnitude of departures from expected frequencies rather than as separate hypothesis tests for every individual cell. 

Sachdeva _et al. Fire Ecology          (2026) 22:156_ 

Page 7 of 20 

**Table 1** Organizational types assigned to Instagram, Facebook, and Twitter/X datasets through web searches 

|**Organizational type**|**Description**|
|---|---|
|USDA Forest Service|Forest Service|
|Other federal government|All other federal agencies beside the Forest<br>Service|
|State government|State government agencies|
|County government|County government|
|Municipal government|Municipal (village, town, or city) government|
|Business|For-profit organizations|
|Non-profit organization|Non-profit organization and/or community<br>group|
|Media|News media (TV, radio, newspaper, blog)|
|Individual|Not part of a group|
|University/school|University or K-12 schools|



#### **_Organizational types_** 

For Instagram, Facebook, and Twitter/X, we assigned each account (“handle”) to a broad organizational type via targeted web lookups of profile pages (see Table 1). We used these assignments to compare how thematic clusters vary by communicator type. 

#### **_Geographies_** 

The ten initial WCS landscapes served as the organizing geographic frame for data collection, whereas the formal geographic analysis was conducted at the state level within the Twitter/X subset. Because Twitter/X posts include a location field, we analyzed thematic distributions by U.S. state for this subset. We mapped each post to a state using the Sprinklr “Location” field (e.g., “Denver, CO” → Colorado) and aggregated results at the state level. As noted in Sect. “Data collection,” location metadata were not available for our other Sprinklrsourced channels (Facebook, Reddit, Instagram) or for mass media; Twitter/X posts without a usable location field, and all documents from these other channels, were excluded from this state-level analysis but were retained in all other (non-geographic) analyses in this paper. 

### **Results** 

The results below are organized around the relative volume and distribution of themes across channels, organizational types, and geographies. We report these patterns as evidence of salience, i.e., which adaptation concepts are made most visible and through which information channels and organizational types, consistent with the agenda-setting premise that the relative frequency and prominence of coverage shapes which issues audiences come to regard as important (McCombs and Shaw 1972). We do not interpret frequency of coverage as evidence 

of audience belief, behavior change, or communication effectiveness; we return to this distinction, and to what our data can and cannot support, in the Discussion. 

#### **Description of themes** 

Most of the adaptation content centers on putting prescribed fire<sup>1</sup> into practice; operational updates and schedules account for about a third of all paragraphs (29.8%; 72 topics), often paired with notes on weather windows (4.0%; 5 topics) and operational risks and safeguards (5.5%; 16 topics, Table 2). A second strand concerns how communities organize for risk reduction: Community Wildfire Protection Plans (CWPPs) and related participation make up 9.9% (6 topics), complemented by outreach and stewardship activities (2.2%; 8 topics) and steady knowledge-exchange—newsletters, webinars, agency briefings (4.5%; 10 topics). Privateproperty actions form another layer, with defensible space, home hardening, and insurance considerations at 3.8% (4 topics). We also observe substantial attention to Indigenous cultural burning (19.3%; 6 topics), highlighting efforts to restore good fire through collaboration and local knowledge. Rounding out the picture are references to specific landscapes (7.9%; 15 topics), broader framing of fire risk, including climate change and planning models (6.8%; 15 topics), and descriptions of mechanical fuel treatments such as thinning or mastication (6.2%; 7 topics). Together, these themes encompass planned fire, community planning, household action, cultural stewardship, and targeted fuel treatments. 

#### **Variation by information channel** 

The volume of paragraph chunks was highest from the Twitter/X platform (50.78%), with the other social media sources: Instagram (11.95%), Reddit (7.65%), and Facebook (3.94%). The USFS WCS Tracker had the second smallest corpus of paragraph chunks (4.3%), although the per document number of chunks was higher, as documents were longer than social media posts. The mass media source from ProQuest TDM Studio comprised 21.37% of the paragraph chunks. 

Notably, the distribution of thematic clusters (as measured by Standardized Residuals, SR from here on out) varied substantially across information platforms (Fig. 3). Twitter/X overwhelmingly featured content related to _Active and planned prescribed fire updates_ (SR = + 28.68) 

> 1 We use “wildfire” rather than the broader NWCG term “wildland fire” (which encompasses both unplanned wildfires and planned prescribed fires) because our focus is specifically on communication about adaptation to wildfire risk. Prescribed fire enters our analysis as one such adaptation practice, not as a separate category of fire we are studying in its own right; our object of study throughout is wildfire adaptation, for which prescribed fire is a primary tool, rather than wildland fire management more broadly. 

Sachdeva _et al. Fire Ecology          (2026) 22:156_ 

Page 8 of 20 

|**opics**<br>**Amt. (%) of**<br>**paragraphs**|29.8%<br>9.9%<br>3.8%<br>19.3%<br>4.5%<br>6.2%|
|---|---|
|**Example texts**<br>**No. of t**|Crews planning to pile burn along hwy 150 and near san<br>cristobal fire crews are planning to potentially begin<br>pile burning along and near highway 150 from valdez<br>nm to the taos ski valley area as early as friday dec 1<br>piles near san cristobal nm are also under considera-<br>tion both areas are within the wildland urban interface<br>where human development intermingles with the forest<br>72<br> <br>Learn more about how community mitigation assistance<br>teams foster partnerships that are focused on creat-<br>ing a more fire resilient community and landscape<br>and the teams work at the great lake wildfire<br>6<br>Home hardening includes making sure embers from a fire<br>are not able to fly into gutters vents or under exterior<br>doors other panelists agreed that home hardening<br>in addition to improving defensible space around struc-<br>tures needed to be done in conjunction and not one<br>or the other but some agencies are complicating such<br>efforts said jeff neuman a resident of sonoma countys<br>oakmont neighborhood during the meetings public com-<br>ment period he told the panel his property has about 300<br>to 400 feet of fence line that runs along trioneannadel<br>state park he wanted a permit to perform fuel reduction<br>work in the park which was within 130 feet of his structure<br>4<br>By the late 1800 s, local federal agencies banned such<br>the practices, but with recent calls for and respect<br>to these knowledge systems the state of California<br>and researchers like, Melinda Adams (scholar_melinda)<br>of the N’dee San Carlos Apache, are making strides to put<br>local collaboration at the front of this move towards man-<br>agement. #goodfire #indigenousknowledge #culturalfire<br>#environment #californiafire<br>6<br>With uptodate policy information agency input and sci-<br>encedriven management recommendations the news-<br>letter strives to provide landowners with all the facts<br>and some fun too to create a healthy and sustainable<br>landscape education naturalresources resourceconserva-<br>tion california conservation conservationmatters forest-<br>landstewardnewsletter<br>10<br>Over the past week dozens of goats from city grazing<br>have been clearing the overgrown brush in the old balboa<br>reservoir as part of an environmentally friendly approach<br>to rid the area of fire hazards and invasive vegetation<br>7|
|**Definition**|Documents providing information about current<br>and planned prescribed fires<br>Documents referring to Community Wildfire Protection<br>Plans or other aspects of community involvement in wild-<br>fire planning<br>Documents referring to wildfire actions on private<br>residential lands, like defensible space and home fire<br>insurance<br>Documents referring to Indigenous practices of inten-<br>tional burning for land management<br>Documents that point to knowledge exchange opportu-<br>nities, like webinars, discussions, etc<br>Documents that describe treatments like logging, thin-<br>ning, mastication, etc|
|**Theme label**|Active and planned prescribed fire updates<br>CWPP, community involvement<br>Defensible space and insurance<br>Cultural burning<br>Knowledge exchange<br>Mechanical fuel treatments|



Sachdeva _et al. Fire Ecology          (2026) 22:156_ 

Page 9 of 20 

|**Theme label**<br>**Definition**<br>**Example texts**<br>**No. of topics**<br>**Amt. (%) of**<br>**paragraphs**|Outreach and stewardship<br>Documents that reference outreach and stewardship<br>activities<br>Now theyre focusing on better connecting with vulner-<br>able residents in their communities such as those who<br>speak spanish and older adults who might have limited<br>mobility or trouble evacuating and ensuring there are<br>redundancies in place so everyone is alerted when it<br>counts sonoma county emergency management<br>director christopher godley said cope groups and other<br>similar resident preparedness programs have changed<br>how neighborhoods especially in more rural areas<br>respond to and prepare for disasters less than a handful<br>of those efforts were known to exist before the firestorm<br>now there are more than 70 across sonoma county he<br>said preparedness godley said has been built into the fab-<br>ric of the community now<br>8<br>2.2%<br>Risks of prescribed fires<br>Documents that describe or discuss the risks of prescribed<br>fires<br>Please be advised that the prescribed burn planned<br>at Lory State Park will not start today as planned.<br>Unfortunately, not enough snow cover exists and we<br>are therefore out of prescription. Weather will continue<br>to be monitored for favorable conditions in the future.<br>Prescribed burning will only be conducted under specific<br>guidelines and plans established by the Colorado Division<br>of Fire Prevention and Control, including having accept-<br>able weather forecasts and fuels conditions that meet<br>guidelines for safe and effective burning and adequate<br>smoke dispersal. #cofire #coloradofire #dfpcfire #wildfire<br>#firefighter #wildlandfire #wildlandfirefighter #RxFire<br>#prescribedfire<br>16<br>5.5%<br>WCS landscape<br>Documents that reference a particular region<br>rt tontoforest confronting the wildfire crisis strategy<br>protecting communities and critical infrastructure learn<br>how the tontonf is using mastication to reduce the risk<br>of wildfires to communities and critical infrastructure<br>wildfirecrisisstrategy<br>15<br>7.9%<br>Fire risk, including climate change and modelling<br>Documents that describe or discuss overall wildfire risk,<br>for planning purposes<br>A changing landscape mori comes from a long line<br>of ranchers dating back 95 years five generations of his<br>family currently work on his ranch he knows the land<br>mori said hes seen a drastic increase in the frequency<br>and intensity of wildfires in recent years when the warm<br>dry summer temperatures arrive the threat of wildfire<br>becomes a constant concern he added<br>15<br>6.8%|
|---|---|



Sachdeva _et al. Fire Ecology          (2026) 22:156_ 

Page 10 of 20 

Sachdeva _et al. Fire Ecology          (2026) 22:156_ 

Page 11 of 20 



**Fig. 3** Pearson standardized residuals of paragraph-level BERTopic results for all information channels, plotted by theme ( _x_ -axis) and information channel ( _y_ -axis). Dashed lines at +2 and −2 indicate overrepresentation and underrepresentation, respectively 

and also elevated _CWPP, community involvement_ (SR = + 14.15); themes such as _Cultural burning_ (SR = − 15.46), _Mechanical fuel treatments_ (SR = − 14.22), and _Prescribed fire and weather_ (SR = − 13.76) were comparatively underrepresented. 

In contrast, Reddit and Facebook showed higher relative representation of several community-centered themes, but in distinct ways. Reddit showed a striking overrepresentation of _Cultural burning_ (SR = + 35.08) alongside modest elevation for _Defensible space and insurance_ (SR = + 2.85), while down-weighting day-of operational updates ( _Active and planned prescribed fire updates_ , SR = − 15.29) and even _Knowledge exchange_ (SR = − 5.23). Facebook, by comparison, overindexed on _Cultural burning_ (SR = + 12.34) and _Knowledge exchange_ (SR = + 4.19), but did not overrepresent _Outreach and stewardship_ (SR = − 2.56). Complementing 

these patterns, Instagram concentrated on stewardship and practice: _Outreach and stewardship_ (SR = + 15.50), _Knowledge exchange_ (SR = + 11.25), _Mechanical fuel treatments_ (SR = + 11.05), and _Defensible space and insurance_ (SR = + 6.85)—and de-emphasized operational updates ( _Active and planned prescribed fire updates,_ SR = − 11.55). 

The USFS WCS Tracker (i.e., Forest Service press releases) was, unsurprisingly, the dominant channel for the WCS landscape theme (SR = + 46.65), with relatively high representation of spatial strategy and monitoring across defined management units. It was underrepresented in _Active and planned prescribed fire updates_ (SR = − 10.67), _CWPP, community involvement_ (SR = − 7.63), and _Prescribed fire and weather_ (SR = − 6.28). 

Sachdeva _et al. Fire Ecology          (2026) 22:156_ 

Page 12 of 20 

Finally, mass media showed pronounced positive residuals for _Prescribed fire and weather_ (SR = + 34.19), _Mechanical fuel treatments_ (SR = + 23.40), _Risks of prescribed fire_ (SR = + 20.22), and _Fire risk, including climate change, and modeling_ (SR = + 15.43), while Active and planned prescribed fire updates were underrepresented (SR = − 25.03). Taken together, theme prevalence differed substantially across information channels; the largest positive and negative residuals for each channel are reported above and summarized in Fig. 3. 

#### **Variation by organizational type for social media (Twitter/X, Facebook, and Instagram) data** 

We then examined how theme prevalence varied by organizational type within the social media datasets. Individual users dominated the wildfire adaptation discourse on Twitter/X, Facebook, and Instagram, contributing 65.64% of paragraph chunks and representing the largest share of the social-media corpus. Among organizational users, the USFS emerged as the most prominent institutional voice (7.81%), followed by media outlets (6.73%), state government agencies (5.01%), non-profit organizations (4.65%), coalition/task forces (2.58%), county government (2.32%), other federal government agencies (1.85%), universities and schools (1.29%), businesses (1.14%), and municipal government (0.98%). 

The distribution of themes across organizational types for only the social media data varied by category (Fig. 4). USFS maintained a relatively even footprint across clusters (e.g., _Defensible space and insurance_ SR = + 2.35; _Fire risk, including climate change, and modeling_ SR = + 1.54; many others near 0). 

Other government organizations at different scales displayed different patterns of thematic emphasis. County government overrepresented _CWPP/community involvemen_ t (SR = + 7.69). Municipal governments overrepresented _Cultural burning_ (SR = + 14.50) and _Outreach and stewardship_ (SR = + 3.90) while underrepresenting _Active and planned prescribed fire updates_ (SR = − 5.71). State governments showed positive residuals for _Risks of prescribed fir_ e (SR = + 4.13), _Prescribed fire and weather_ (SR = + 2.09), and _WCS landscap_ e (SR = + 1.97), while Cultural burning (SR = − 1.12) and Outreach and stewardship (SR = − 1.05) were comparatively lower. Other federal agencies showed positive residuals for _Mechanical fuel treatments_ (SR = + 2.87), _Prescribed fire and weather_ (SR = + 2.39), and _Cultural burning_ (SR = + 1.12), while _WCS landscape_ (SR = − 2.19) and _Fire risk, including climate change, and modeling_ (SR = − 2.66) were underrepresented. 

Non-profit organizations showed pronounced overrepresentation in _Active and planned prescribed fire updates_ (SR = + 7.17) alongside underrepresentation 

across several themes, including _CWPP/community involvement_ (SR = − 4.27), _Defensible space and insurance_ (SR = − 3.80), _Cultural burning_ (SR = − 3.72), _Knowledge exchange_ (SR = − 3.46), _Fire risk, including climate change, and modeling_ (SR = − 3.94), and _Mechanical fuel treatments_ (SR = − 2.14). 

Coalitions/task forces overrepresented _Fire risk, including climate change, and modeling_ (SR = + 13.38), _Knowledge exchange_ (SR = + 6.08), and _WCS landscape_ (SR = + 2.34), while underrepresenting _Active and planned prescribed fire updates_ (SR = − 3.65), _Cultural burning_ (SR = − 2.65), and Risks of prescribed fire (SR = − 2.38). Universities/schools overrepresented _Cultural burning_ (SR = + 7.74), _Risks of prescribed fire_ (SR = + 2.56), _Mechanical fuel treatments_ (SR = + 2.28), and _Knowledge exchange_ (SR = + 1.92). Media accounts overrepresented _CWPP/community involvement_ (SR = + 3.65) and _Active and planned prescribed fire updates_ (SR = + 2.27), while _Cultural burning_ (SR = − 4.29) and _Fire risk, including climate change, and modeling_ (SR = − 2.78) were underrepresented. Business accounts overrepresented _Outreach and stewardship_ (SR = + 2.82), _Defensible space and insurance_ (SR = + 2.33), and _Active and planned prescribed fire updates_ (SR = + 1.94). Individuals showed the largest positive residual for _CWPP/community involvement_ (SR = + 8.04), with smaller positive residuals for _Knowledge exchange_ (SR = + 1.48) and _Risks of prescribed fire_ (SR = + 0.52), and a negative residual for Active and planned prescribed fire updates (SR = − 3.07). Together, these patterns show that theme prevalence differed across organizational types; their broader implications are considered in the Discussion. 

#### **Variation by geography for Twitter/X data** 

Next, we examined geographic variation in wildfire adaptation discourse across states. This location information was only available from Twitter/X data; we report it because Twitter/X is our single largest information channel, comprising 50.78% of all paragraph chunks across the entire corpus, but the patterns below describe this one platform and should not be read as a full account of geographic variation across the broader communication landscape. The geographic distribution of thematic clusters across states revealed regional differences in which themes were over- or under-represented. 

Several notable patterns emerged across themes (Fig. 5). Colorado was overrepresented in _CWPP/community involvement_ (SR = + 6.86), while Montana (−2.63), Arizona (−3.53), and New Mexico (−3.68) were underrepresented. New Mexico, Washington, and Oregon showed clear overrepresentation in _Risks of prescribed fire_ (SRs = + 11.39, + 3.64, + 3.38, respectively). 

Sachdeva _et al. Fire Ecology          (2026) 22:156_ 

Page 13 of 20 



**Fig. 4** Pearson standardized residuals of paragraph-level BERTopic results for social media data only, plotted by theme ( _x_ -axis) and organizational type ( _y_ -axis). Dashed lines at +2 and −2 indicate overrepresentation and underrepresentation, respectively 

Sachdeva _et al. Fire Ecology          (2026) 22:156_ 

Page 14 of 20 



**Fig. 5** Pearson standardized residuals of paragraph-level BERTopic results for Twitter/X data only, plotted by theme ( _x_ -axis) and state ( _y_ -axis). Dashed lines at +2 and −2 indicate overrepresentation and underrepresentation, respectively 

California dominated _Mechanical fuel treatments_ discourse (SR = + 2.73), whereas Arizona (−3.10) and Oregon (−2.66) were underrepresented. _Cultural burning_ was overrepresented in Montana (+7.16) and Washington (+5.09) but underrepresented in California (−2.75) and Arizona (−3.11); we discuss this pattern relative to tribal-state governance context below. 

The _WCS landscape_ theme was overrepresented in Idaho (SR = + 2.88), Arizona (+ 3.29), and Colorado (+ 2.60), and underrepresented in California (− 3.31). Arizona showed particularly active engagement with real-time fire communication, overrepresented in _Active and planned prescribed fire updates_ (+ 7.13), while Idaho (− 2.64), Washington (− 4.21), and Oregon (− 7.13) were underrepresented in that theme. Arizona (−2.68) was the most underrepresented state in the _Defensible space and insurance_ theme, but several states were below expectation, including Colorado (− 1.65) and New Mexico (− 1.16). 

Oregon dominated _Fire risk, including climate change, and modeling_ (SR = + 18.65) while California (− 4.99) and Arizona (− 3.35) underindexed. Second, _outreach and stewardship_ was overrepresented not only in Montana 

(+ 2.91) and Oregon (+ 2.15), but also in Idaho (+ 1.59), Washington (+ 1.59), and Colorado (+ 1.14), with California underrepresented (− 2.55). Finally, _Knowledge exchange_ skewed strongly toward California (+ 5.71) and away from Colorado (− 3.86), Oregon (− 3.04), and Washington (− 3.01). 

Taken together, these geographic patterns show that thematic emphasis within the Twitter/X subset varied by state: Oregon showed the strongest climate/modeling emphasis, Arizona the strongest emphasis on real-time updates, and Montana and Washington the strongest cultural-burning emphasis. 

### **Discussion** 

Our analysis reveals a varied communication landscape about wildfire adaptation in the western United States, reinforcing the broader communication gap identified in the literature—between crisis-oriented, event-driven messaging and systemic, adaptation-oriented discourse. Despite policy momentum toward “living with fire,” public communication continues to emphasize active events and suppression-oriented activities over proactive 

Sachdeva _et al. Fire Ecology          (2026) 22:156_ 

Page 15 of 20 

adaptation, though important exceptions and innovations exist across regions, organizations, and platforms. 

This study addressed three guiding questions: _who_ communicates about wildfire adaptation, _what_ adaptation concepts are emphasized, and _how_ these patterns vary across landscapes prioritized under the USDA Forest Service’s Wildfire Crisis Strategy (WCS). By comparing news and social media texts with WCS press releases, we documented a complex, multi-actor communications ecosystem. By “mapping,” we mean specifically that we identified, at a scale not previously attempted, which organizational types and platforms are associated with which adaptation themes and where those associations concentrate geographically, rather than that we have characterized the wildfire adaptation communication ecosystem in its entirety. The results show that communication about adaptation extends well beyond traditional institutional sources such as the USFS, involving networks of state agencies, local governments, non-profits, and community coalitions. 

These findings suggest that wildfire adaptation communication functions as a social process rather than a technical exercise, one that reflects how diverse actors interpret risk, responsibility, and legitimacy within their own geographic and institutional contexts. In this sense, our findings are consistent with broader hazard communication scholarship arguing that hazard-centric communication can obscure opportunities for collective learning and long-term resilience (Tierney 2014; Wachinger et al. 2013); our data speak to the hazard-centric emphasis of current discourse but do not themselves measure collective learning or resilience outcomes. Studying the contours of this evolving communication landscape is one input, among others, to realizing the “living with fire” paradigm envisioned by contemporary wildfire management frameworks. 

#### **Public communications differ by organization type** 

Addressing our first guiding question, who communicates about wildfire adaptation, we find that communication occurs through a decentralized network of organizations rather than a single institutional voice. This multi-actor structure reflects the broader governance patterns of wildfire management, where responsibility for adaptation is distributed across agencies, non-profits, and local governments. 

Non-profit organizations dominate _Active and planned fire updates_ , while coalitions and task forces focus on landscape-scale planning ( _WCS landscapes_ ) and risk communication ( _Risks of prescribed fires_ , _Fire risk including climate change and modeling_ ). County governments specialize in community involvement and protection planning ( _CWPP/community involvement_ ), 

while municipal governments emphasize _Outreach and stewardship_ and _Cultural burning_ practices. This specialization pattern is consistent with wildfire adaptation communication operating through a network of organizational voices rather than any single institution, similar to governance practices (Hamilton and Evers 2023). 

The platform-specific patterns further reinforce this finding: Twitter/X dominated _Active and planned prescribed fire updates_ and _CWPP/community involvement_ , while Facebook was overrepresented in cultural burning discussions, Reddit in _Cultural Burning_ and selected homeowner-facing discussions, and news media in _Prescribed fire and weather_ , _Fire risk including climate change and modeling_ , and _Mechanical fuel treatments_ . These platform-specific patterns show that different adaptation themes were most frequently represented through different communication channels. 

#### **Topics of public communications on wildfire vary with geography** 

Our geographic analysis, drawn from Twitter/X data only, reveals that certain topics achieve widespread coverage while others are concentrated in specific states; we treat these as patterns in public discourse rather than as direct evidence of underlying local conditions, and note the scope of this analysis is necessarily limited to what one platform captures. Topic clusters such as _Outreach and stewardship_ , _Mechanical fuel treatments_ , _Prescribed fire and weather_ , and _Defensible space and insurance_ showed relatively even geographic distribution, suggesting these represent broadly relevant adaptation strategies. In contrast, other topics demonstrated pronounced regional concentration: Colorado for _CWPP/community involvement_ , Montana and Washington for _Cultural burning_ , California for _Knowledge exchange_ , and Oregon for _Fire risk_ discussions. The _CWPP/community involvement_ prevalence in Colorado aligns with research on governance networks, showing many coalition members and high levels of collaboration (Muttaqee et al. 2025). 

The concentration of cultural burning discourse in Montana and Washington, while being underrepresented in California and Arizona, is particularly noteworthy given California’s extensive Indigenous fire history (Greenler et al. 2024). At the same time, the role of cultural burning in Pacific Northwest forests is increasingly recognized (Long et al. 2021). The underrepresented pattern for _Cultural burning_ in California may reflect the complex dynamics of tribal-state relationships and the institutional barriers that persist in California despite growing recognition of Indigenous fire practices (Eriksen and Hankins 2014). Together, this state-level variation in cultural burning discourse is consistent with the differing political contexts, tribal sovereignty considerations, 

Sachdeva _et al. Fire Ecology          (2026) 22:156_ 

Page 16 of 20 

and collaborative frameworks that operate at the state and regional scale; we note this is a distinct claim from the local, place-specific contingency described in prior wildfire adaptation scholarship (e.g., Paveglio et al. 2019), since our Twitter/X data can speak only to state-level patterns and not to variation within states or communities. 

Our findings echo Paveglio et al. ’s (2019) emphasis on the importance of local context in wildfire adaptation acceptance and support, and are consistent with the possibility that public discourse both reflects and shapes local adaptation priorities. Public communication has already been treated as a local context variable in this literature; what our analysis adds is a state-level, multi-platform description of how that variable itself varies, which future work could pair with the more established factors this literature has examined, such as fuels-treatment history, public land values, and existing advocacy networks. We note, however, that this state-level analysis relies on Twitter/X data alone, which limits how far these patterns can be generalized to the broader communication landscape; we return to this limitation in Sect. “Limitations and future research.” 

#### **Some key adaptations are less prevalent in public communications on wildfire** 

In examining what adaptation concepts are emphasized across communication channels, we found that despite the breadth of topics covered across our corpus, _several elements of wildfire adaptation remain notably absent from public communications_ . Referring back to the fire adapted communities wheel (FAC Net 2021), topics related to infrastructure and business continuity, as well as codes and ordinances, received minimal attention across all platforms and organizational types. The limited discussion of codes and ordinances is notable given their role in wildfire adaptation implementation: building codes, zoning regulations, and land-use planning are established tools for reducing wildfire risk, yet they generate comparatively little public-facing digital discourse in our corpus. We did not analyze where these topics are discussed instead, so we do not draw conclusions here about which other forums (e.g., professional conferences, regulatory proceedings) may carry this content; we note the absence as a finding and leave its explanation to future work. 

#### **Prescribed fire was the dominant topic of public communications on wildfire** 

The overwhelming dominance of prescribed fire discourse from 2022 to 2024, with active and planned updates alone comprising nearly 30% of all communications, represents a striking finding that warrants careful consideration. This emphasis likely reflects several factors 

identified in prior research, though our data cannot adjudicate between them. First, prescribed fire’s visibility as an active, in-progress management practice is consistent with findings that wildfire communication tends toward event-driven and hazard-centric content (Morehouse and Sonnett 2010; Crow et al. 2017); this visibility connects to its direct relationship to wildfire risk reduction and its capacity to generate both support and controversy, given the institutional and staffing tensions between suppression and planned fire documented elsewhere (Ingalsbee 2017; Marks-Block and Tripp 2021), including its potential to affect neighboring lands through escaped fires. Second, active and planned prescribed fire updates likely also serve a practical public-safety function: agencies have an incentive to publicize planned burns so that residents who see or smell smoke do not flood 9–1-1 and dispatch centers with non-emergency calls, which could both increase dispatcher workload and risk crowding out reports of genuine emergencies. Third, the prevalence of prescribed fire discussions may reflect the practice’s increasing institutionalization within federal and state fire management agencies (Sample et al. 2022), creating multiple channels for public communication about implementation, planning, and outcomes. Finally, this dominance could also reflect the particular events, organizational priorities, and platforms captured in our sample rather than a general property of wildfire adaptation communication: specific high-profile prescribed burns or escaped fires within our September 2022–February 2024 window, agency-level decisions to prioritize this topic, or the particular mix of channels and time periods we analyzed could each independently produce this pattern, and a different sample (other outlets, other years, other messengers) might show a more even distribution across adaptation topics. While prescribed fire dominates the overall discourse, it manifests in multiple distinct contexts rather than as a monolithic topic. 

This dominance of prescribed fire discourse points to a potential imbalance in the diversity of adaptation options represented in public communication; our data speak to what is discussed, not to how audiences understand or respond to it, so we frame this as a question about representational balance rather than a claim about public understanding. While prescribed fire represents an important tool, the relative lack of discussion about other adaptation strategies, such as defensible space, mechanical treatments, or land use planning, suggests that public communications may not fully represent the diversity of approaches available for wildfire risk reduction. Drawing from the economics literature, one possible explanation is that higher levels of prescribed fire communication and focus could have a “crowding out” effect on other adaptation strategies (Prante et al. 2011): if the volume 

Sachdeva _et al. Fire Ecology          (2026) 22:156_ 

Page 17 of 20 

of prescribed fire communications is much higher than other wildfire adaptation strategies, whether because it is more controversial, occurs more often, or requires more communication across landowners, it may reduce the visibility of smaller, but no less important, conversations about strategies such as wildfire-adaptive building codes and ordinances. We hold this alongside two other plausible, non-exclusive explanations that our data cannot distinguish from crowding-out: 1) prescribed fire may simply have been more newsworthy or operationally active during our particular sample window and locations (e.g., specific high-profile burns or escaped fires), or 2) organizations in our sample may have made deliberate priority decisions to promote this one adaptation activity over others. A sample drawn from different outlets, time periods, or messengers might well show a more even distribution across adaptation topics; distinguishing between these explanations would require data our corpus does not provide. 

#### **Limitations and future research** 

Our analysis has several limitations that suggest directions for future research. First, our location data were limited to Twitter/X, and this limitation is more consequential than platform coverage alone: Twitter/X users are not demographically representative of the general population of these states, skewing younger and more technology-engaged than a representative sample would be, so state-level patterns in our data describe Twitter/X discourse specifically rather than the states’ populations as a whole (Gottfried 2024). Our September 2022–February 2024 collection window also coincided with a period of substantial change at Twitter/X, including a change in ownership and subsequent changes to content moderation policies and algorithmic ranking, which likely altered both the platform’s user base and the kinds of content promoted or suppressed during our sampling period; we cannot rule out that these platform-level changes affected which wildfire adaptation content appeared in our data or how it was distributed across themes and states. We treat our geographic findings as conservative, platform-specific observations rather than general claims about western U.S. populations, and future work using Twitter/X data should account for this shifting platform context explicitly. 

Second, our focus on English-language content may miss important communications in other languages, particularly given the cultural burning discussions and their connections to Indigenous communities. Third, the temporal scope of our analysis may not capture seasonal variations in wildfire communication patterns or the evolution of discourse over time; relatedly, we did not systematically catalog which specific wildfire events, 

prescribed burns, or policy developments occurred within our sample window and locations, so we cannot rule out that particular newsworthy events drove some of the patterns we report rather than more general or durable features of the communication landscape. Fourth, and more fundamentally, our approach measures topic occurrence, i.e., how often a theme appears in public text, which is not the same as topic importance or influence; a topic can occur frequently without being especially consequential for audience understanding or behavior, and a topic that occurs rarely is not necessarily unimportant. This does not diminish the value of documenting what is discussed and by whom, but it does mean our findings should be read as a map of public-facing discourse rather than as a measure of communicative effect. Fifth, one aspect of our analysis pipeline limits exact reproducibility: the manual review used to identify wildfireand adaptation-related topics and to interpret the final thematic groupings was conducted by members of the research team without a formal intercoder-reliability statistic. Future applications of this approach would benefit from a preregistered review protocol and a formal reliability assessment of the manual screening and labeling steps. 

Future work could examine how wildfire adaptation communications change during active fire seasons versus non-fire periods, investigate the role of visual content and multimedia in shaping public understanding, and explore how different demographic groups engage with wildfire adaptation information across platforms. The occurrence/importance distinction noted above points most directly to the importance of research that pairs content analysis of the kind presented here with audience-side measures, e.g., surveys, experiments, or engagement data, that can speak to whether and how different communication strategies affect actual adaptation behavior; such work, conducted both online and in-person, could help practitioners and policymakers identify which communication strategies are most effective for which audiences and contexts, a question our corpus can motivate but not answer. 

### **Conclusion** 

The current wildfire adaptation communications landscape represents a complex, multi-actor ecosystem that extends far beyond traditional institutional sources. Across news and social media, our analysis demonstrates that current wildfire adaptation discourse emerges across diverse platforms and geographic contexts through a distributed network of federal, state, local, and non-profit actors rather than any single institutional voice. Prescribed fire dominates public communication, reflecting both its visibility as a management tool and the 

Sachdeva _et al. Fire Ecology          (2026) 22:156_ 

Page 18 of 20 

persistence of event-driven, hazard-centric narratives, while more systemic strategies such as land-use planning, building codes, and business continuity remain underrepresented. Geographic variation further underscores how local political, cultural, and governance contexts shape what aspects of adaptation are publicly visible or neglected. These patterns suggest that communication itself constitutes a critical dimension of adaptation capacity: it shapes how communities interpret responsibility, legitimacy, and risk in a changing fire regime. As wildfire risks continue to grow, understanding and leveraging this distributed communication ecosystem will improve effective adaptation planning and implementation. 

### **Supplementary Information** 

The online version contains supplementary material available at https:// doi. org/ 10. 1186/ s42408- 026- 00576-3. 

Additional file 1: List of keywords/terms used to collect data “prescribed burn” OR “prescribed fire” OR “rx fire” OR “rx burn” OR “(fire AND wui)” OR “fire ecology” OR “(fire AND adaptation)” OR “(fire AND fuels treatment)” OR “(fire AND fuel treatment)” OR “(fire AND air quality)” OR “(fire AND controlled burn)” OR “(fire AND defensible space)” OR “wildfire” OR “wildland urban interface” OR “forest fire” OR “(wildfire AND vegetation)” OR “(fuels AND forest)” OR “(wildfire AND fuel break)” OR “(wildfire AND cwpp)” OR “community wildfire protection plan” OR “firewise” OR “fire-adapted communities” OR “(fire AND thinning)” OR “(fire AND mastication)” OR “(fire AND grazing)” OR “(fire AND indigenous land management practices)” OR “fire adapted ecosystems” OR “fire-adapted ecosystems” OR “fuel ladder management” OR “wildfire risk reduction” OR “fire behavior” OR “(fire AND management)” OR “(fire AND suppression)” OR “(fire AND community outreach)” OR “(fire AND community)” OR “(fire AND homeowner mitigation)” OR “(fire AND nfs land)” OR “(fire AND national forest service land)” OR “(fire AND nf)” OR “(fire AND national forest)” OR “(fire AND wcs)” OR “wildfire crisis strategy” OR “(fire AND forest service)” OR “(fire AND usfs)” OR “fire district” OR “(fire AND forest restoration)” OR “(fire AND nepa)” OR “(fire AND national environmental policy act)” OR “(fire AND environmental impact statement)” OR “(fire AND eis)” OR “(fire AND environmental assessment)” OR “(fire AND dnr)” OR “(fire AND department of natural resources)” OR “(fire AND department of forestry)” OR “(fire AND forestry)” OR “(fire AND fac)” OR “(fire AND cwdg)” OR “community wildfire defense plan” OR “(fire AND priority landscapes)” OR “(fire AND pod)” OR “(fire AND pod boundaries)” OR “(fire AND potential operational delineations)” OR “(fire AND cwi)” OR “(climate and wildfire institute)” OR “climate & wildfire institute” OR “(fire AND administrative barriers)” OR “(fire AND regulatory)” OR “(fire AND lsr)” OR “(fire AND landscape scale restoration)” OR “(fire AND stewardship)” OR “(fire AND tribal land)” OR “(fire AND tribal)” OR “(fire AND sp&t)” OR “(fire AND state, private, and tribal)” OR “(fire AND spf)” OR “(fire AND state and private)” OR “wildfire hazard mitigation” OR “(fire AND mitigation)” OR “(fire AND fema)” OR “(fire AND federal emergency management agency)” OR “(fire AND silviculture)” OR “(fire AND forestry)” OR “(fire AND resilience)” OR “department of forestry and fire protection” OR “cal fire” OR “(fire AND department of lands)” OR “(fire AND idl)” OR “(fire AND department of natural resources and conservation)” OR “(fire AND dnrc)” OR “department of forestry and fire management” OR “(fire AND dffm)” OR “(fire AND energy, minerals, and natural resources department)” OR “(fire AND emnrd)” OR “cultural burn”. 

##### **Acknowledgements** 

This work was supported in part by the U.S. Department of Agriculture, Forest Service. We also thank Cody Evers and Miranda Mockrin for their thoughtful reviews of earlier versions of this manuscript. We thank Dani Dagan for helping us with data access. 

##### **Authors’ contributions** 

All authors contributed to the study conception and design. Data collection and preprocessing were performed by JS. Formal analysis and modeling were conducted by SS, MJ, JS. Interpretation of results was carried out by all authors. The first draft of the manuscript was written by SS, MJ, JS, and all authors commented on and revised subsequent versions of the manuscript. All authors read and approved the final manuscript. 

##### **Funding** 

This work was supported by the U.S. Forest Service through the Bipartisan Infrastructure Law (BIL) project “Fueling Adaptations.” 

##### **Data availability** 

The datasets analyzed during the current study were derived from publicly available sources and licensed media databases. Access to some data is subject to third-party licensing restrictions. Aggregated results and analytical code are available from the corresponding author on reasonable request. 

#### **Declarations** 

##### **Ethics approval and consent to participate** 

This study did not involve human participants, experiments, or identifiable personal data and therefore did not require ethics committee approval. 

##### **Consent for publication** 

Not applicable. 

##### **Competing interests** 

The authors declare no competing interests. 

Received: 1 April 2026   Accepted: 30 August 2026 



##### **References** 

- Abrams, J. B., M. Knapp, T. B. Paveglio, A. Ellison, C. Moseley, M. Nielsen-Pincus, and M. S. Carroll. 2015. Re-envisioning community-wildfire relations in the U.S. west as adaptive governance. _Ecology and Society_ 20 (3) : Article 34. https:// doi. org/ 10. 5751/ ES- 07848- 200334. 

- Anderson, R. M., Hixson, K., Johnston, K., Mockrin, M. H., & Mowery, M. 2025. _Adapting to wildfire: A review of ongoing wildfire planning and mitigation efforts across 10 landscapes in the Western United States_ (General Technical Report PNW-GTR-1030). U.S. Department of Agriculture, Forest Service, Pacific Northwest Research Station. https:// doi. org/ 10. 2737/ PNW- GTR- 1030. 

- Babić, K., Petrović, M., Beliga, S., Martinčić-Ipšić, S., Pranjić, M., & Meštrović, A. 2021. Prediction of COVID-19 related information spreading on Twitter. In _2021 44th International Convention on Information, Communication and Electronic Technology (MIPRO)_ (pp. 395–399). IEEE. https:// doi. org/ 10. 23919/ MIPRO 52101. 2021. 95966 93. 

- Blei, D. M., and J. D. Lafferty. 2009. Topic models. In _Text mining: Classification, clustering, and applications_ , ed. A. N. Srivastava and M. Sahami, 71–94. Chapman & Hall/CRC. https:// doi. org/ 10. 1201/ 97814 20059 458- 12. 

- Bossetta, M. 2018. The digital architectures of social media: Comparing political campaigning on Facebook, Twitter, Instagram, and Snapchat in the 2016 U.S. election. _Journalism & Mass Communication Quarterly_ 95 (2): 471–496. https:// doi. org/ 10. 1177/ 10776 99018 763307. 

- Brenkert, H., Champ, P. A., & Flores, N. 2005. _Mitigation of wildfire risk by homeowners_ (Research Note RMRS-RN-25). U.S. Department of Agriculture, Forest Service, Rocky Mountain Research Station. https:// doi. org/ 10. 2737/ RMRS- RN- 25. 

- Brenkert-Smith, H., J. R. Meldrum, P. A. Champ, and C. M. Barth. 2017. Where you stand depends on where you sit: Qualitative inquiry into notions of fire adaptation. _Ecology and Society_ 22 (3) : Article 7. https:// doi. org/ 10. 5751/ ES- 09471- 220307. 

- Crow, D. A., J. Berggren, L. A. Lawhon, E. A. Koebele, A. Kroepsch, and J. Huda. 2017. Local media coverage of wildfire disasters: An analysis of problems 

Sachdeva _et al. Fire Ecology          (2026) 22:156_ 

Page 19 of 20 

and solutions in policy narratives. _Environment and Planning c: Politics and Space_ 35 (5): 849–871. https:// doi. org/ 10. 1177/ 02637 74X16 667302. 

- DiMaggio, P., M. Nag, and D. Blei. 2013. Exploiting affinities between topic modeling and the sociological perspective on culture: Application to newspaper coverage of U.S. government arts funding. _Poetics_ 41 (6): 570–606. https:// doi. org/ 10. 1016/j. poetic. 2013. 08. 004. 

- Edgeley, C. M., and T. B. Paveglio. 2024. Bridging scales for landscape-level wildfire adaptation: A case study of the Kittitas Fire Adapted Communities Coalition. _Journal of Environmental Management_ 351 : Article 119818. https:// doi. org/ 10. 1016/j. jenvm an. 2023. 119818. 

- Entman, R. M. 1993. Framing: Toward clarification of a fractured paradigm. _Journal of Communication_ 43 (4): 51–58. https:// doi. org/ 10. 1111/j. 14602466. 1993. tb013 04.x. 

- Eriksen, C., and D. L. Hankins. 2014. The retention, revival, and subjugation of Indigenous fire knowledge through agency fire fighting in Eastern Australia and California. _Society & Natural Resources_ 27 (12): 1288–1303. https:// doi. org/ 10. 1080/ 08941 920. 2014. 918226. 

- Fire Adapted Communities Learning Network. 2021. _Fire adapted communities graphic and facilitator’s guide_ . https:// firea dapte dnetw ork. org/ resou rce/ fire- adapt ed- commu nities- graph ic- and- facil itato rs- guide/. 

- Gilbert, S., K. Kim, R. Kelley, A. Wright, and A. Zanin-Yost. 2024. Evaluation of six news aggregator databases: A comparison for researchers and librarians. _Journal of Electronic Resources Librarianship_ 36 (1): 36–54. https:// doi. org/ 10. 1080/ 19411 26X. 2024. 23060 45. 

- Gligorić, K., A. Anderson, and R. West. 2018. How constraints affect content: The case of Twitter’s switch from 140 to 280 characters. _Proceedings of the International AAAI Conference on Web and Social Media_ 12 (1): 596–599. https:// doi. org/ 10. 1609/ icwsm. v12i1. 15079. 

- Gottfried, J. 2024. _Americans’ social media use_ . Pew Research Center. https:// www. pewre search. org/ inter net/ 2024/ 01/ 31/ ameri cans- social- media- use/. 

- Greenler, S. M., F. K. Lake, W. Tripp, K. McCovey, A. Tripp, L. G. Hillman, C. J. Dunn, S. J. Prichard, P. F. Hessburg, W. Harling, and J. D. Bailey. 2024. Blending Indigenous and western science: Quantifying cultural burning impacts in Karuk Aboriginal Territory. _Ecological Applications_ 34 (4) : e2973. https:// doi. org/ 10. 1002/ eap. 2973. 

- Grootendorst, M. 2022. _BERTopic: Neural topic modeling with a class-based TFIDF procedure_ . arXiv. https:// doi. org/ 10. 48550/ arXiv. 2203. 05794. 

- Hamilton, M., M. Nielsen-Pincus, and C. R. Evers. 2023. Wildfire risk governance from the bottom up: Linking local planning processes in fragmented landscapes. _Ecology and Society_ 28 (3) : Article 3. https:// doi. org/ 10. 5751/ ES- 13856- 280303. 

- Ingalsbee, T. 2017. Whither the paradigm shift? Large wildland fires and the wildfire paradox offer opportunities for a new paradigm of ecological fire management. _International Journal of Wildland Fire_ 26 (7): 557–561. https:// doi. org/ 10. 1071/ WF170 62. 

- Jacobson, M., H. Smith, H. R. Huber-Stearns, E. J. Davis, A. S. Cheng, and A. Deak. 2022. Comparing social constructions of wildfire risk across media, government, and participatory discourse in a Colorado fireshed. _Journal of Risk Research_ 25 (6): 697–714. https:// doi. org/ 10. 1080/ 13669 877. 2021. 19629 54. 

- Jones, G. M., E. K. Vraga, P. F. Hessburg, M. D. Hurteau, C. D. Allen, R. E. Keane, T. A. Spies, M. P. North, B. M. Collins, M. A. Finney, J. M. Lydersen, and A. L. Westerling. 2022. Counteracting wildfire misinformation. _Frontiers in Ecology and the Environment_ 20 (7): 392–393. https:// doi. org/ 10. 1002/ fee. 2553. 

- Kreiss, D., and S. C. McGregor. 2018. Technology firms shape political communication: The work of Microsoft, Facebook, Twitter, and Google with campaigns during the 2016 U.S. presidential cycle. _Political Communication_ 35 (2): 155–177. https:// doi. org/ 10. 1080/ 10584 609. 2017. 13648 14. 

- Long, J. W., F. K. Lake, and R. W. Goode. 2021. The importance of Indigenous cultural burning in forested regions of the Pacific West, USA. _Forest Ecology and Management_ 500 : Article 119597. https:// doi. org/ 10. 1016/j. foreco. 2021. 119597. 

- Malik, M. M., and J. Pfeffer. 2016. A macroscopic analysis of news content in Twitter. _Digital Journalism_ 4 (8): 955–979. https:// doi. org/ 10. 1080/ 21670 811. 2015. 11332 49. 

- Marks-Block, T., & Tripp, W. 2021. Facilitating prescribed fire in Northern California through Indigenous governance and interagency partnerships. _Fire_ 4 (3): Article 37. https:// doi. org/ 10. 3390/ fire4 030037. 

- McCaffrey, S. M. 2004. Thinking of wildfire as a natural hazard. _Society & Natural Resources_ 17 (6): 509–516. https:// doi. org/ 10. 1080/ 08941 92049 04524 45. 

- McCombs, M. E., and D. L. Shaw. 1972. The agenda-setting function of mass media. _Public Opinion Quarterly_ 36 (2): 176–187. https:// doi. org/ 10. 1086/ 267990. 

- Mercer, D., and D. Prisbrey. 2004. Vigilant geography: Newspaper coverage of a wildfire at the Hanford nuclear site. _Environmental Practice_ 6 (3): 247–256. https:// doi. org/ 10. 1017/ S1466 04660 40003 90. 

- Morehouse, B. J., and J. Sonnett. 2010. Narratives of wildfire: Coverage in four U.S. newspapers, 1999–2003. _Organization & Environment_ 23 (4): 379–397. https:// doi. org/ 10. 1177/ 10860 26610 385901. 

- Moritz, M. A., E. Batllori, R. A. Bradstock, A. M. Gill, J. Handmer, P. F. Hessburg, J. Leonard, S. McCaffrey, D. C. Odion, T. Schoennagel, and A. D. Syphard. 2014. Learning to coexist with wildfire. _Nature_ 515 (7525): 58–66. https:// doi. org/ 10. 1038/ natur e13946. 

- Morss, R. E., J. L. Demuth, H. Lazrus, L. Palen, C. M. Barton, C. A. Davis, C. Snyder, O. V. Wilhelmi, K. M. Anderson, D. A. Ahijevych, J. Anderson, M. Bica, K. R. Fossell, J. Henderson, M. Kogan, K. Stowe, and J. Watts. 2017. Hazardous weather prediction and communication in the modern information environment. _Bulletin of the American Meteorological Society_ 98 (12): 2653–2674. https:// doi. org/ 10. 1175/ BAMS-D- 16- 0058.1. 

- Muttaqee, M., Evers, C., Campbell, L. K., Nielsen-Pincus, M., Awbrey, O., Hixson, K., Johnson, M., & Svendsen, E. 2025. _Fueling adaptation: Collaborative wildfire governance in the Colorado Front Range landscape_ . Portland State University. https:// doi. org/ 10. 15760/ esm- report. 02. 

- Nilsson, S., and A. Enander. 2020. “Damned if you do, damned if you don’t”: Media frames of responsibility and accountability in handling a wildfire. _Journal of Contingencies and Crisis Management_ 28 (1): 69–82. https:// doi. org/ 10. 1111/ 1468- 5973. 12284. 

- Olteanu, A., C. Castillo, N. Diakopoulos, and K. Aberer. 2015. Comparing events coverage in online news and social media: The case of climate change. _Proceedings of the International AAAI Conference on Web and Social Media_ 9 (1): 288–297. https:// doi. org/ 10. 1609/ icwsm. v9i1. 14626. 

- Paton, D. 2008. Risk communication and natural hazard mitigation: How trust influences its effectiveness. _International Journal of Global Environmental Issues_ 8 (1–2): 2–16. https:// doi. org/ 10. 1504/ IJGEN VI. 2008. 017256. 

- Paveglio, T., M. S. Carroll, J. D. Absher, and T. Norton. 2009. Just blowing smoke? Residents’ social construction of communication about wildfire. _Environmental Communication_ 3 (1): 76–94. https:// doi. org/ 10. 1080/ 17524 03080 27049 71. 

- Paveglio, T., T. Norton, and M. S. Carroll. 2011. Fanning the flames? Media coverage during wildfire events and its relation to broader societal understandings of the hazard. _Human Ecology Review_ 18 (1): 41–52. 

- Paveglio, T. B., C. M. Edgeley, M. S. Carroll, M. Billings, and A. M. Stasiewicz. 2019. Exploring the influence of local social context on strategies for achieving fire adapted communities. _Fire_ 2 (2) : Article 26. https:// doi. org/ 10. 3390/ fire2 020026. 

- Prante, T., J. M. Little, M. L. Jones, M. McKee, and R. P. Berrens. 2011. Inducing private wildfire risk mitigation: Experimental investigation of measures on adjacent public lands. _Journal of Forest Economics_ 17 (4): 415–431. https:// doi. org/ 10. 1016/j. jfe. 2011. 04. 003. 

- ProQuest. n.d. TDM Studio [Database]. https:// tdmst udio. proqu est. com/. 

- Pyne, S. J. 1982. _Fire in America: A cultural history of wildland and rural fire_ . Princeton University Press. 

- Remenick, L. 2018. The role of communication in preparation for wildland fire: A literature review. _Environmental Communication_ 12 (2): 164–176. https:// doi. org/ 10. 1080/ 17524 032. 2017. 13465 19. 

- Rollason, E., L. J. Bracken, R. J. Hardy, and A. R. G. Large. 2018. Rethinking flood risk communication. _Natural Hazards_ 92 (3): 1665–1686. https:// doi. org/ 10. 1007/ s11069- 018- 3273-4. 

- Sample, M., A. E. Thode, C. Peterson, M. R. Gallagher, W. T. Flatley, M. Friggens, A. Evans, R. A. Loehman, S. Hedwall, L. A. Brandt, M. Janowiak, and C. W. Swanston. 2022. Adaptation strategies and approaches for managing fire in a changing climate. _Climate_ 10 (4) : Article 58. https:// doi. org/ 10. 3390/ cli10 040058. 

- Sprinklr. n.d. Sprinklr Insights: Social Listening [Database]. https:// www. sprin klr. com/ produ cts/ consu mer- intel ligen ce/ social- liste ning/. 

- Steelman, T. A., and S. M. McCaffrey. 2013. Best practices in risk and crisis communication: Implications for natural hazards management. _Natural Hazards_ 65 (1): 683–705. https:// doi. org/ 10. 1007/ s11069- 012- 0386-z. 

Sachdeva _et al. Fire Ecology          (2026) 22:156_ 

Page 20 of 20 

- Tierney, K. 2014. _The social roots of risk: Producing disasters, promoting resilience_ . Stanford University Press. 

- U.S. Department of Agriculture, Forest Service. 2022. _Confronting the wildfire crisis: A chronicle from the National Fire Plan to the Wildfire Crisis Strategy_ (FS-1187c). https:// www. fs. usda. gov/ sites/ defau lt/ files/ fs_ media/ fs_ docum ent/ WCS- Chron icle. pdf. 

- Wachinger, G., O. Renn, C. Begg, and C. Kuhlicke. 2013. The risk perception paradox—Implications for governance and communication of natural hazards. _Risk Analysis_ 33 (6): 1049–1065. https:// doi. org/ 10. 1111/j. 15396924. 2012. 01942.x. 

- Wilson, N. 2024. _Assessing the prevalence of prescribed fire in Pacific Northwest wildfire media coverage_ [Honors thesis, University of Oregon]. Scholars’ Bank. https:// schol arsba nk. uoreg on. edu/ items/ c055ff 8c- 2676- 42a3- 945c70a4d 48f95 3d. 

### **Publisher’s Note** 

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 
