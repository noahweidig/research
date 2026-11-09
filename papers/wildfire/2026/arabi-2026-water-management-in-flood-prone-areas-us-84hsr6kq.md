---
title: 'Water management in flood-prone areas using nature-based solutions: an AI-assisted systematic review and thematic analysis'
authors:
- Arabi, Shiva
- Yaméogo, Djigui David Stéphane
- Rahman, Musfiqur
- Bereded, Behailu
- Shibeshi, Tefera
- Kwak, Nayeon
- Eason, Melinda
- Smith, Virginia B.
year: '2026'
journal: Frontiers in Sustainability
doi: 10.3389/frsus.2026.1966241
tags:
- large wildfires
- modeling
- united states
- urban ecology
zotero_key: 84HSR6KQ
item_type: journalArticle
url: https://openalex.org/W7223093151
source_url: 'unpaywall: https://www.frontiersin.org/journals/sustainability/articles/10.3389/frsus.2026.1966241/pdf'
fulltext_status: fulltext
synced: '2026-11-09'
---

# Water management in flood-prone areas using nature-based solutions: an AI-assisted systematic review and thematic analysis

## Abstract

Nature-based solutions (NbS) are increasingly used to reduce flood risk and improve water management in flood-prone areas. However, research remains fragmented across disciplines, regions, and scales, making it difficult to identify research trends, knowledge gaps, and priorities. This study presents an artificial intelligence (AI)-assisted systematic review of peer-reviewed articles published between 2016 and 2025, retrieved from Web of Science and Scopus. Following the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) framework, a large language model (LLM) was used to screen titles and abstracts, followed by full-text review by the research team. A structured dataset was developed through LLM-assisted data extraction and human validation. Semantic clustering and LLM-assisted synthesis were then used to identify research themes and summarize implementation conditions, benefits, limitations, and research needs. A total of 185 studies were included, which were predominantly published between 2021 and 2025. Nine research themes emerged, with urban green infrastructure for runoff mitigation, spatial planning and decision support, and catchment and hydraulic modeling accounting for 47.6% of the studies. Research was concentrated in the United Kingdom, China, and the United States, with limited representation from Africa and Latin America. The evidence relied mainly on scenario modeling and short monitoring periods, while social equity, public acceptance, and maintenance outcomes were rarely assessed using standardized metrics. While literature reviews have been previously done on the topic of NbS for flood-prone water management, to our knowledge, this is the first review of NbS for flood-prone water management to combine LLM-assisted screening, data extraction, and synthesis with semantic clustering and human validation. The study provides a thematic evidence map, examines temporal and geographic research trends, and presents a reproducible workflow to support future environmental evidence synthesis.

## Full text

TYPE Systematic Review PUBLISHED 21 October 2026 DOI 10.3389/frsus.2026.1966241 

#### OPEN ACCESS 

EDITED BY Amin Talei, Monash University, Australia 

REVIEWED BY Ahmed AL-Dujaili, Amirkabir University of Technology, Iran Pierre-Antoine Versini, École des ponts ParisTech (ENPC), France *CORRESPONDENCE Shiva Arabi shiva.arabi@unf.edu 

RECEIVED 12 August 2026 REVISED 02 October 2026 ACCEPTED 07 October 2026 PUBLISHED 21 October 2026 

##### CITATION 

Arabi S, Yam´eogo DDS, Rahman M, Bereded B, Shibeshi T, Kwak N, Eason M and Smith V (2026) Water management in flood-prone areas using nature-based solutions: an AI-assisted systematic review and thematic analysis. _Front. Sustain._ 7:1966241. doi: 10.3389/frsus.2026.1966241 

##### COPYRIGHT 

© 2026 Arabi, Yam´eogo, Rahman, Bereded, Shibeshi, Kwak, Eason and Smith. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms. 

# Water management in flood-prone areas using nature-based solutions: an AI-assisted systematic review and thematic analysis 

Shiva Arabi<sup>1,2</sup> *, Djigui David St´ephane Yam´eogo<sup>3</sup> , Musfiqur Rahman<sup>2</sup> , Behailu Bereded<sup>2</sup> , Tefera Shibeshi<sup>2</sup> , Nayeon Kwak<sup>2</sup> , Melinda Eason<sup>2</sup> and Virginia Smith<sup>2</sup> 

1Department of Construction Management, College of Computing, Engineering, and Construction, University of North Florida, Jacksonville, FL, United States,<sup>2</sup> Department of Civil and Environmental Engineering, Villanova University, Villanova, PA, United States,<sup>3</sup> Department of Sustainable Engineering, Villanova University, Villanova, PA, United States 

Nature-based solutions (NbS) are increasingly used to reduce flood risk and improve water management in flood-prone areas. However, research remains fragmented across disciplines, regions, and scales, making it difficult to identify research trends, knowledge gaps, and priorities. This study presents an artificial intelligence (AI)-assisted systematic review of peer-reviewed articles published between 2016 and 2025, retrieved from Web of Science and Scopus. Following the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) framework, a large language model (LLM) was used to screen titles and abstracts, followed by full-text review by the research team. A structured dataset was developed through LLM-assisted data extraction and human validation. Semantic clustering and LLM-assisted synthesis were then used to identify research themes and summarize implementation conditions, benefits, limitations, and research needs. A total of 185 studies were included, which were predominantly published between 2021 and 2025. Nine research themes emerged, with urban green infrastructure for runoff mitigation, spatial planning and decision support, and catchment and hydraulic modeling accounting for 47.6% of the studies. Research was concentrated in the United Kingdom, China, and the United States, with limited representation from Africa and Latin America. The evidence relied mainly on scenario modeling and short monitoring periods, while social equity, public acceptance, and maintenance outcomes were rarely assessed using standardized metrics. While literature reviews have been previously done on the topic of NbS for flood-prone water management, to our knowledge, this is the first review of NbS for flood-prone water management to combine LLM-assisted screening, data extraction, and synthesis with semantic clustering and human validation. The study provides a thematic evidence map, examines temporal and geographic research trends, and presents a reproducible workflow to support future environmental evidence synthesis. 

##### KEYWORDS 

artificial intelligence (AI), flood management, Large Language Models (LLMs), naturebased solutions (NbS), systematic review, thematic analysis 

Frontiers in Sustainability 

01 

frontiersin.org 

10.3389/frsus.2026.1966241 

Arabi et al. 

## 1 Introduction 

Flooding is among the most costly and widespread environmental hazards worldwide, with climate change, urbanization, and land-use change increasing both the frequency and severity of flood events (Izuchukwu Precious et al., 2025; Maimuri et al., 2025). In response, nature-based solutions (NbS) have gained significant attention as a sustainable approach for mitigating the impacts of stormwater in flood-prone areas. By leveraging natural processes such as infiltration, evapotranspiration, storage, and ecosystem restoration, NbS can reduce flood risk while simultaneously providing co-benefits including improved water quality, enhanced biodiversity, carbon sequestration, and increased community resilience (Cook et al., 2024). 

Over the past two decades, research on NbS for flood management has expanded rapidly across disciplines including hydrology, ecology, environmental engineering, urban planning, landscape architecture, and climate adaptation. This growth has produced a diverse body of literature examining a wide range of interventions, from green stormwater infrastructure and wetland restoration to floodplain reconnection and watershedscale ecosystem management. However, the resulting knowledge base remains highly fragmented. Studies vary considerably in terminology, spatial scale, performance metrics, methodological approaches, and geographic focus, making it difficult to identify overarching themes, compare findings across contexts, and determine where critical knowledge gaps remain. 

Existing review studies have provided valuable insights into specific NbS applications, regions, or outcomes, but few have systematically synthesized the broader literature on water management in flood-prone areas (Johnson et al., 2022; Fang et al., 2023). Building on this work, this study focuses specifically on NbS for water management in flood-prone areas. It also applies an artificial intelligence (AI)-assisted approach to analyze the full texts of all reviewed studies, which allows implementationrelated topics such as costs, maintenance, equity, and barriers to be compared across a large body of literature. This approach complements existing reviews and offers a scalable way to synthesize the rapidly growing NbS literature. At the same time, the rapid growth of scientific publications in this field has created new challenges for evidence synthesis. Traditional systematic review approaches, while rigorous, are increasingly constrained by the scale and complexity of available literature, particularly when addressing interdisciplinary topics such as NbS where 

studies span multiple domains and methodological traditions. This has created a need for approaches that can support more efficient screening, structured extraction of qualitative information, and identification of latent thematic structures while preserving transparency and reproducibility. 

Recent advances in Large Language Models (LLMs) offer new opportunities to support these tasks as analytical tools within systematic review workflows (Scherbakov et al., 2025; Chen et al., 2026). When carefully constrained and guided, LLMs can assist in screening large volumes of abstracts, structuring unstructured textual information, and supporting qualitative coding of complex interdisciplinary literature. In this study, LLMs were used as an enabling tool to facilitate systematic screening and structured information extraction, supporting rather than replacing established review procedures. This allowed for consistent handling of a large and diverse body of literature while maintaining adherence to systematic review principles. LLM-assisted evidence synthesis has so far been applied mainly in the medical and health sciences (Scherbakov et al., 2025; Chen et al., 2026), and its use in environmental research remains limited to date. 

To address these gaps, this study presents an AI-assisted systematic review and thematic analysis of the literature on NbS for water management in flood-prone areas. The main research question is: what are the dominant research themes, trends, implementation insights, benefits, and knowledge gaps in this literature? To answer this question across a large and interdisciplinary body of studies, the review applies a workflow that combines systematic review methods with LLM-assisted screening, structured dataset development, thematic mapping, and qualitative synthesis, supported by human validation. In doing so, the study provides a comprehensive assessment of the NbS literature and also illustrates how such a workflow can support transparent and scalable environmental evidence synthesis. 

## 2 Data and methods 

The methodology consisted of five main steps: (1) literature retrieval, (2) LLM-assisted study screening, (3) LLM-assisted structured dataset development, (4) thematic mapping and cluster development, and (5) LLM-assisted qualitative information synthesis. Figure 1 presents the overall methodological workflow used in this study. 

### 2.1 Literature retrieval 

Abbreviations: AI, Artificial intelligence; API, Application programming interface; c-TF-IDF, Class-based term frequency–inverse document frequency; EOM, Excess of Mass (HDBSCAN cluster selection method); GPT, Generative Pre-trained Transformer; GSI, Green Stormwater Infrastructure; HDBSCAN, Hierarchical Density-Based Spatial Clustering of Applications with Noise; JSON, JavaScript Object Notation (data format); LID, Low Impact Development; LLM, Large Language Model; NbS, Nature-based Solutions; PDF, Portable Document Format; PRISMA, Preferred Reporting Items for Systematic Reviews and Meta-Analyses; SuDS, Sustainable Drainage Systems; TF-IDF, Term frequency–inverse Document Frequency; UK, United Kingdom; UMAP, Uniform Manifold Approximation and Projection; U.S., United States; WSUD, Water Sensitive Urban Design. 

A systematic literature search was conducted using Web of Science and Scopus to identify studies related to NbS in flood-prone areas and water management. These databases were selected because of their broad coverage of peer-reviewed scientific literature across environmental, engineering, and water-related disciplines. The search strategy was developed using a combination of keywords and Boolean operators. The search terms were selected to capture different terminologies related to NbS and blue-green infrastructure approaches for flood and water management. The following search query was applied in both databases: 

Frontiers in Sustainability 

02 

frontiersin.org 

10.3389/frsus.2026.1966241 

Arabi et al. 



FIGURE 1 Methodology flowchart. 

(“nature-based solutions” OR “NbS” OR “green infrastructure” OR “blue-green infrastructure”) AND (“flood-prone” OR “flood risk” OR “floodplain” OR “flood-vulnerable”) AND (“water” OR “water management” OR “water resources”). 

The search initially identified 946 records (420 from Web of Science and 526 from Scopus). After filtering by publication date, language (English), and document type (journal articles only), 682 records remained (347 from Web of Science and 335 from Scopus). Removing 241 duplicate records left 441 unique records for screening. Of these, 211 were excluded during LLM-assisted study-type classification and 4 did not meet the inclusion criteria, so 226 studies were assessed for eligibility. After full-text review, a further 41 studies were excluded, resulting in a final dataset of 185 studies (Figure 2). References to the selected articles are provided in Appendix 1. 

### 2.2 LLM-assisted study screening 

Following literature retrieval and duplicate removal, an LLMassisted screening workflow was used to evaluate the relevance of the identified studies. The screening process was designed to improve consistency and efficiency in handling the large number of retrieved records. The overall study selection procedure followed the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) framework (Page et al., 2021) to ensure a transparent and reproducible review process. PRISMA guidelines were used to document the identification, screening, eligibility assessment, and final inclusion of studies throughout the review workflow. 

The screening process was implemented using the OpenAI GPT-5.4 (Generative Pre-trained Transformer) model, accessed via its application programming interface (API), through an automated Python-based workflow. Article titles and abstracts were provided to the model as structured inputs together with 

explicit screening instructions and predefined decision rules. A structured prompt-engineering framework was developed to guide the screening process. The prompts included clearly defined inclusion and exclusion criteria, standardized response formats, and domain-specific terminology related to NbS. Studies were included if they were: (1) focused on NbS, green infrastructure, or blue-green infrastructure; (2) addressed water-related challenges or water management; and (3) considered flood-prone, flood-risk, floodplain, or flood-vulnerable contexts. Studies were excluded if they did not address NbS-related approaches, lacked a water-related focus, lacked a flood-related context, or did not satisfy multiple inclusion criteria simultaneously. 

In addition to relevance screening, the LLM was used to classify studies according to publication type, including original research articles, review articles, conceptual or theoretical papers, and policy or planning documents. Only original research articles were retained for subsequent analysis, while the remaining publication types were excluded to maintain consistency in the reviewed dataset. Original research articles were retained regardless of research design, so the final dataset includes empirical field studies, case studies, and modeling studies. A fulltext review was subsequently conducted to verify the relevance of the screened studies and remove papers with insufficient focus on flood-prone water-related NbS applications. This step was performed manually within the research team. Reviewers read the full text of each study retained after LLM-assisted screening and confirmed that it addressed NbS, water management, and a flood-prone context. Disagreements were resolved by discussion. Studies were excluded at this stage mainly because NbS or flood-related water management was discussed only as a secondary topic rather than as the main focus of the study. The final dataset consisted of 185 research papers, which were downloaded and used for the subsequent analysis stages. Figure 2 presents the PRISMA flowchart summarizing the study selection process. 

Frontiers in Sustainability 

03 

frontiersin.org 

10.3389/frsus.2026.1966241 

Arabi et al. 



FIGURE 2 PRISMA flowchart summarizing the study selection process. 

### 2.3 LLM-assisted structured dataset development 

The full texts of the selected studies were processed using an AIassisted information extraction workflow to convert unstructured scientific documents into a structured research dataset. First, all selected Portable Document Format (PDF) files were collected in a centralized directory and converted into machine-readable text to enable automated processing and analysis. The extracted text from each study was then analyzed using the OpenAI GPT-5.4 API through a structured prompt-engineering framework designed for systematic academic information extraction. The workflow aimed to ensure consistent extraction of comparable information across all studies while reducing variability in model outputs. 

Several prompt-engineering strategies were incorporated to improve extraction quality and reliability. Role-based prompting was used by instructing the model to act as an academic research summarizer specialized in NbS and floodrelated water management studies. Few-shot prompting was implemented by providing example outputs demonstrating the 

desired extraction structure and level of detail. In addition, adversarial constraints were incorporated to reduce unsupported interpretation, hallucinated information, and overgeneralization. The prompts explicitly instructed the model to extract only information directly stated in the papers and to return missing or unavailable information as null values rather than generating assumptions. The extracted information included bibliographic details and thematic study characteristics, including publication year, study country, title, study objectives, methodology, paper summary, public acceptance, key barriers, success factors and enablers, equity considerations, maintenance requirements, ecosystem services, energy and resource benefits, social co-benefits, study limitations, and research gaps or future research needs. Information was extracted only when explicitly reported in the study. 

To improve consistency and accuracy, a human-in-the-loop evaluation and validation process was incorporated throughout the information extraction workflow. For each paper, the LLM was instructed to assign an overall extraction confidence level (high, medium, or low) and to record in a dedicated human 

Frontiers in Sustainability 

04 

frontiersin.org 

10.3389/frsus.2026.1966241 

Arabi et al. 

review flag field any value that was partially stated, ambiguous, or could not be reported as a quantitative outcome (Appendix 2). The research team verified all flagged fields against the original full texts and fully reviewed every record assigned medium or low confidence to evaluate the accuracy, completeness, and consistency of the LLM-generated outputs. The evaluation focused on whether extracted information was directly supported by the original publications, whether relevant information was correctly assigned to the predefined categories, and whether missing information was appropriately represented as null values rather than inferred by the model. Errors identified during the review process, including unsupported interpretations, inconsistent categorization, and formatting issues, were documented and used to refine the prompt instructions and extraction rules. The revised prompts were subsequently re-tested to assess improvements in extraction consistency and reduce ambiguity in model responses. This iterative validation process was repeated until the extraction outputs demonstrated acceptable consistency with the information reported in the original studies. Consistency was considered acceptable when the reviewed outputs no longer contained unsupported values, misassigned categories, or inferred values in place of null entries. The extraction confidence levels assigned to each record were retained as a quantitative indicator of output reliability and are reported in Section 3.7. The final validated information was organized into a structured dataset and stored in JavaScript Object Notation (JSON) format for subsequent analysis. 

### 2.4 Thematic mapping and cluster development 

A thematic mapping workflow was developed to identify major research themes and thematic relationships within the selected studies. The analysis aimed to group studies into coherent thematic clusters and identify dominant research directions, emerging topics, and relationships across the literature. The thematic mapping process was performed using the structured dataset generated in the previous step. Specifically, the title, study objective, paper summary, and methodology extracted from each paper were used as the primary textual inputs for the analysis. These fields were selected because they collectively capture the main research focus, study design, and scientific contribution of each paper. 

To represent semantic similarities among studies, transformerbased sentence embedding models were used to generate document embeddings from the combined textual content. Specifically, the Sentence-Transformers framework (Reimers and Gurevych, 2020) with the all-MiniLM-L6-v2 model (Yin and Zhang, 2024) was used to convert each study into a high-dimensional semantic vector representation. This model is the default English embedding model of the BERTopic topic-modeling framework and has been widely used for clustering scientific text (Grootendorst, 2022). This approach enabled studies with similar research topics, methodologies, and objectives to be positioned closer together within the embedding space. The high-dimensional embeddings were subsequently reduced into a lower-dimensional representation using Uniform Manifold Approximation and Projection (UMAP) (McInnes et al., 2018). 

UMAP was used to preserve the semantic structure of the dataset while improving cluster separability and enabling visualization of thematic relationships among studies. The dimensionality reduction process was implemented using cosine similarity as the distance metric to better capture semantic relationships within the textual data. 

The reduced embeddings were then clustered using Hierarchical Density-Based Spatial Clustering of Applications with Noise (HDBSCAN) (McInnes et al., 2017). This clustering approach was selected because it can identify clusters with varying densities, sizes, and shapes while also handling noise and outlier studies that do not strongly belong to a specific thematic group. Unlike traditional clustering approaches that require a predefined number of clusters, HDBSCAN determines the cluster structure directly from the data, making it suitable for exploratory thematic analysis of heterogeneous scientific literature. To characterize the content of each cluster, representative keywords were extracted using a class-based term frequency–inverse document frequency (c-TF-IDF) approach (Grootendorst, 2022). Cluster-level documents were generated by aggregating the textual content of studies within each cluster, and the most representative unigrams and bigrams were identified using TF-IDF weighting. This process enabled identification of the dominant concepts and research topics associated with each cluster. The tools and parameter settings used for semantic embedding, dimensionality reduction, clustering, and keyword extraction are summarized in Table 1. 

An additional LLM-assisted interpretation step was subsequently conducted to improve the interpretability of the identified clusters. The representative keywords extracted from each cluster were provided to the OpenAI GPT-5.4 model, which generated concise human-readable labels describing the primary research topic represented by each cluster. Finally, the identified clusters and their corresponding labels were further consolidated into broader, non-overlapping thematic categories suitable for synthesis within the review paper. During this step, the LLM analyzed cluster labels and representative keywords collectively to group related clusters into higher-level thematic domains. The resulting themes were manually reviewed to ensure thematic consistency, reduce overlap between categories, and improve interpretability for the final synthesis and discussion. 

### 2.5 LLM-assisted qualitative information synthesis 

An LLM-assisted synthesis workflow was developed to generate cross-study thematic summaries from the extracted dataset. The workflow aimed to synthesize findings across studies within each identified research theme while reducing repetitive paper-by-paper descriptions and improving consistency in the synthesis process. For each thematic category identified in the thematic mapping stage, the extracted study information was aggregated and provided to the OpenAI GPT-5.4 model as structured input. The synthesis process used information extracted in the previous stages, including maintenance requirements, public acceptance, barriers, enablers, 

Frontiers in Sustainability 

05 

frontiersin.org 

10.3389/frsus.2026.1966241 

Arabi et al. 

TABLE 1 Parameters used in the thematic mapping and clustering workflow. 

|Stage|Tool/library|Parameter|Value|Description|
|---|---|---|---|---|
|Embedding|Sentence-transformers|Model|all-MiniLM-L6-v2|Pre-trained transformer that produces a<br>384-dimensional semantic vector for each study|
|Dimensionality<br>reduction|UMAP|n_neighbors|30|Size of the local neighborhood used to learn the<br>manifold structure|
|||n_components|2|Number of output dimensions|
|||metric|Cosine|Distance metric used to measure semantic<br>similarity|
|||min_dist|0.1|Minimum distance between points in the<br>low-dimensional space|
|||random_state|42|Fixed seed for reproducibility|
|Clustering|HDBSCAN|min_cluster_size|4|Minimum number of studies required to form a<br>cluster|
|||min_samples|1|Number of neighbors required for a point to count<br>as a core point|
|||cluster_selection_epsilon|0.1|Distance threshold below which clusters are<br>merged|
|||cluster_selection_method|Excess of Mass<br>(EOM)|Method for selecting clusters from the cluster<br>hierarchy|
|||metric|Euclidean (default)|Distance metric applied to the UMAP-reduced<br>embeddings|
|Keyword extraction|scikit-learn TfidfVectorizer|max_features|1000|Maximum vocabulary size|
|||ngram_range|(1, 2)|Unigrams and bigrams|
|||stop_words|English|English stop words removed|



success factors, ecosystem services, equity considerations, energy co-benefits, social co-benefits, research gaps, and study limitations. 

A structured prompt-engineering framework was designed to guide the synthesis process and improve output consistency. The prompts explicitly instructed the model to perform qualitative cross-study synthesis rather than individual paper summarization. The workflow emphasized identification of recurring patterns, agreements, differences, and emerging trends across studies within each theme. The prompts also instructed the model to use synthesis-oriented academic language and concise thematic interpretation. Several prompt-engineering techniques were incorporated to improve synthesis quality and reduce unsupported interpretation. Role prompting was used by instructing the model to act as a researcher conducting qualitative synthesis of peer-reviewed NbS literature. Few-shot prompting was implemented by providing example synthesis paragraphs demonstrating the expected writing style, structure, and level of abstraction. In addition, adversarial constraints were included to minimize hallucinated information, unsupported claims, excessive generalization, and introduction of external knowledge beyond the provided dataset. The prompts explicitly instructed the model to synthesize only evidence present in the extracted study information. 

The synthesis outputs were generated separately for each thematic dimension and organized into structured thematic summaries. A systematic human-in-the-loop review process was then conducted to evaluate the quality and validity of the 

generated syntheses. The review assessed whether the synthesized statements accurately represented patterns reported across the included studies, whether conclusions were supported by the extracted evidence, whether contradictory findings were appropriately represented, and whether the synthesis avoided introducing information beyond the reviewed dataset. Potential issues, including overgeneralization, unsupported claims, and inaccurate interpretation of study findings, were recorded and used to refine the synthesis prompts and improve output reliability. Following prompt refinement, the synthesis process was repeated and reviewed to enhance consistency across thematic categories. The final thematic summaries were retained only after confirming alignment between the synthesized interpretations and the underlying extracted evidence. Appendix 2 provides the prompt templates for (A) screening, (B) extraction, (C) cluster labeling, and (D) synthesis. 

## 3 Results and discussion 

The results and discussion are organized into the following subsections: (1) Descriptive Overview of the Reviewed Literature, (2) Geographic Distribution of Studies, (3) Thematic Landscape of NbS Research, (4) Implementation of NbS for Flood Management, 

Frontiers in Sustainability 

06 

frontiersin.org 

10.3389/frsus.2026.1966241 

Arabi et al. 

### 3.2 Geographic distribution of studies 



FIGURE 3 Annual distribution of the included studies. 

(5) Benefits of NbS, (6) Limitations and Knowledge Gaps of NbS for Flooding, and (7) Limitations of the LLM-Assisted Workflow. 

### 3.1 Descriptive overview of the reviewed literature 

Figure 3 shows the rapidly growing interest in the application of NbS for flood mitigation. Annual publication counts indicated a strong upward trajectory throughout the study period, increasing from only two publications in 2016 up to 45 publications in 2025. Publication activity remained modest through the early part of the study period, with fewer than 10 papers published annually between 2016 and 2019, suggesting that NbS research on floodprone water management was still an emerging area of inquiry during this time. This period coincides with the early adoption of NbS initiatives in many cities worldwide (Keeler, 2020). Although publication counts plateaued in 2019 and declined slightly in 2023, the overall trend demonstrates sustained growth, with the sharpest increase occurring after 2020. The 147 papers published between 2021 and 2025 account for nearly 80% of the included studies. This expansion likely reflects the broader recognition of NbS, particularly as an effective approach for improving climate resilience and reducing flood risk, as climate change has intensified the frequency and severity of hydrologic extremes worldwide (Seddon et al., 2020). Additionally, the increasing emphasis on sustainable and adaptive water management has driven greater research investments and policy interest in NbS (Wild et al., 2020; Zhai et al., 2023). Part of this growth may also reflect the evolving terminology in the field. Before NbS became widely adopted as an umbrella concept, similar interventions were often described using terms such as ecosystem-based adaptation, sustainable drainage systems (SuDS), low impact development (LID), and WaterSensitive Urban Design (WSUD) (Fletcher et al., 2015). As these practices have increasingly been framed under the NbS and green or blue-green infrastructure terminology used in this review, the observed increase may partly represent a shift in terminology rather than solely an increase in research activity. At the same time, numerous studies have identified the need for more comprehensive and integrated syntheses of the rapidly expanding literature (Massenberg and Panduro, 2024). These trends underscore the growing importance of NbS in flood management research. 

The geographic distribution of the included studies demonstrates that research and implementation of Green Stormwater Infrastructure (GSI) are concentrated in a small number of countries, particularly the United Kingdom (UK), China, and the United States (U.S.), followed by Italy and Australia (Figure 4). This distribution reflects substantial public investment in urban water infrastructure, increasing policy commitments to climate adaptation, and the adoption of sustainable urban development strategies (Keeler, 2020). In the U.S., the third-largest contributor, research has been largely driven by regulatory frameworks associated with the Clean Water Act and U.S. Environmental Protection Agency. NbS have been shown to be effective and efficient interventions for stormwater management, improving water quality, reducing negative geomorphic impacts downstream, and reducing combined sewer overflows (Cook et al., 2024). Consequently, much of the U.S. literature emphasizes engineered NbS practices related to green stormwater infrastructure, and flood mitigation is viewed as a co-benefit (Cook et al., 2024). China also emerges as a major research hotspot, largely driven by the national “Sponge City” program launched in 2015, which mandated large-scale NbS implementation for urban flood control and generated a substantial body of evaluation and planning studies (Li et al., 2017; Wang et al., 2018). By continent, Europe accounted for 41.6% of the reviewed studies, followed by Asia (29.7%), North America (10.8%), Oceania (5.4%), South America (4.9%), and Africa (2.7%). The remaining studies either spanned several continents (1.1%) or did not specify a study location (3.8%). 

In contrast, European research reflects a broader interpretation of green infrastructure that extends beyond stormwater management. European planning frameworks increasingly view green infrastructure as multifunctional systems capable of delivering multiple ecosystem services, including flood mitigation, biodiversity conservation, urban cooling, carbon sequestration, recreation, public health, and climate resilience (Hansen and Pauleit, 2014; Cook et al., 2024). Rather than focusing largely on stormwater management, European studies frequently integrate ecological, social, and economic objectives into planning and design (Cook et al., 2024). Publications appear to be more closely associated with areas using NbS for stormwater than areas experiencing elevated flood risk. 

This mismatch is most evident in Africa, Latin America, and parts of South and Southeast Asia, which are highly exposed to flooding but remain underrepresented in the reviewed literature. Several factors likely contribute to this gap. First, limited research funding and institutional capacity constrain long-term NbS projects and monitoring programs. Second, data scarcity, including limited hydrological records, rainfall data, and high-resolution spatial information, restricts model-based studies, which dominate the field (Ahmad et al., 2024). Third, publication and language bias may play a role, as this review relied on Web of Science and Scopus and was restricted to English-language articles, which likely excludes relevant regional and non-English studies. Addressing these disparities will require targeted international funding for NbS research in flood-vulnerable regions, North-South research partnerships that build local capacity, greater use of open-access 

Frontiers in Sustainability 

07 

frontiersin.org 

10.3389/frsus.2026.1966241 

Arabi et al. 



FIGURE 4 Geographic distribution of the included studies. 

remote sensing and global datasets to overcome data limitations (Iqbal et al., 2025), and the inclusion of regional and non-English databases in future evidence syntheses. 

This geographic pattern highlights important regional differences in NbS implementation priorities. While the U.S. has historically invested in GSI to address regulatory compliance and stormwater management, European countries have increasingly embraced multifunctionality by designing green infrastructure to provide a broader range of ecosystem services. Cook et al. (2024) argue that future GSI implementation should move beyond single-purpose designs and intentionally integrate multiple environmental and social functions, allowing flood mitigation to be treated as a design goal. The reviewed publications indicate a missed opportunity to bridge the gap between designing for stormwater management and including flood mitigation as a design objective. These findings suggest that future NbS implementation, particularly in rapidly urbanizing regions, should adopt a more holistic and multifunctional approach to maximize the longterm environmental and societal benefits of green infrastructure (Cook et al., 2024). 

### 3.3 Thematic landscape of NbS research 

The unsupervised thematic clustering of the 185 studies revealed nine coherent research themes with NbS application for flood mitigation, as shown in Figure 5, reflecting a structure that emerged from the literature rather than from a predefined classification scheme. As described in Section 2.4, representative terms for each cluster were extracted using c-TF-IDF, and these keywords were provided to the OpenAI GPT-5.4 model to generate cluster labels, which were then consolidated into broader themes and manually reviewed by the research team. Because the clusters 

were derived from the data rather than predefined categories, the resulting themes reflect semantic patterns present in the corpus. 

Beyond their thematic content, the relative size of these clusters provides insight into the research priorities that have shaped the evolution of NbS research for flood management. Urban Green Infrastructure for Runoff Mitigation (T1; 35 papers), Spatial Planning and Decision Support (T2; 28), and Catchment and Hydraulic Modeling for Flood Risk Reduction (T3; 25) together comprise nearly half of the corpus (47.6%), indicating that NbS research remains strongly oriented toward the design, placement, and hydraulic evaluation of urban interventions. This pattern is consistent with the engineering and modeling orientation of the field, strongly associated with stormwater regulation, where scenario-based simulations continue to serve as the principal mode of evidence generation. In contrast, the mid-sized themes, Ecological and Hydro-geomorphic Processes in NbS Systems (T5; 22), Governance, Stakeholder Engagement, and Societal Uptake of NbS (T7; 19), and Floodplains, Wetlands, and Agricultural Landscapes for Flood Regulation (T4; 11), suggest growing but still secondary attention to ecological functioning, institutional conditions, and rural and upstream flood management. This aligns with previous studies on NbS ecosystem services (Krauss and Rippy, 2022; Wang et al., 2023; Cook et al., 2024). The smaller clusters, Coastal Flood Risk and Shoreline Protection (T6; 4) and NbS Systems for Urban Water Services and Climate Adaptation (T8; 7), remain comparatively underrepresented despite their increasing relevance to sea-level rise and compound climate hazards. The substantial unclassified group, Emerging Approaches in Flood Management (T9; 34), points to the conceptual and methodological diversity of a field that is still evolving and reflects emerging interest in co-benefits. 

Taken together, these themes show that the literature is organized primarily around intervention type and analytical 

Frontiers in Sustainability 

08 

frontiersin.org 

10.3389/frsus.2026.1966241 

Arabi et al. 



FIGURE 5 Thematic clustering of NbS literature for flood-prone areas (Total number of papers = 185). 

methods rather than outcomes, equity, or long-term performance. The trends in the subgroups reflect the general evolution of NbS interest and investment on a global level. Their significance lies not only in mapping the structure of the field but also in revealing knowledge gaps, particularly the underdevelopment of long-term monitoring, social and ecological co-benefit assessment, and governance and justice-related questions. Comparing the two halves of the study period, the share of Urban Green Infrastructure studies decreased from 31.6% in 2016–20 to 15.6% in 2021 – 25, while studies on spatial planning, floodplains and wetlands, and hybrid approaches increased. Coastal and governance research showed limited growth. 

### 3.4 Implementation of NbS for flood management 

Table 2 shows that implementing NbS for flood management is fundamentally a systems challenge rather than simply an engineering one. Across the literature, successful implementation is consistently associated with the ability to integrate hydrological, ecological, institutional, and social considerations within a single interdisciplinary planning framework. This finding suggests that implementation success depends less on the individual NbS measure itself than on the extent to which planning and governance accommodate interactions among natural processes, built infrastructure, and human systems. 

A notable pattern in the literature is the shift from site-scale interventions to integrated watershed and urban-scale planning. Rather than treating NbS as isolated flood-control measures, recent studies increasingly emphasize their role in interconnected blue-green infrastructure networks that address flood mitigation, ecosystem functioning, and climate adaptation. However, this shift is still emerging, as most reviewed studies (69.7%) were conducted at the local scale, compared with 16.2% at the regional 

scale and 14.1% at the national or international scale. This shift reflects growing recognition that flood resilience depends on cumulative system behavior rather than the performance of individual infrastructure components. The findings also show that implementation challenges are rarely due to technical limitations alone. Instead, institutional fragmentation, competing planning priorities, and uncertainty about future environmental conditions frequently constrain implementation. Consequently, improving flood resilience requires governance structures capable of coordinating across administrative boundaries, engineering disciplines, and stakeholder groups. This highlights an important research direction: developing implementation frameworks that integrate technical decision-support tools with institutional and policy processes. 

A recurring concern across nearly all themes is the unequal distribution of costs and benefits among stakeholders. Upstream communities, farmers, and landowners often bear the costs of implementation, while downstream and urban populations receive most of the flood protection benefits. Socially vulnerable groups may also face greater risks when adaptation measures, such as managed retreat, are implemented. Despite this, equity considerations were reported in only 30.8% of the reviewed studies, and community engagement in 44.9%. These findings suggest that equity should not be treated as a secondary consideration but as a fundamental aspect of NbS implementation that should be integrated into planning and cost-sharing decisions from the outset, rather than addressed after projects have been designed. 

Based on these findings, social and environmental objectives are increasingly inseparable in NbS implementation. The literature indicates that flood-risk reduction alone is not considered a sufficient metric of success. Instead, implementation is increasingly evaluated by its ability to deliver broader environmental, ecological, and societal outcomes. This evolution reflects a broader paradigm shift from traditional stormwater management applications or flood-control strategies toward multifunctional, landscape-based 

Frontiers in Sustainability 

09 

frontiersin.org 

10.3389/frsus.2026.1966241 

Arabi et al. 

TABLE 2 Implementation insights of NbS identified from the reviewed studies. 

|Theme|Public|Key barriers|Success|Equity|Maintenance|
|---|---|---|---|---|---|
||acceptance||factors/enablers|considerations|requirements|
|**Urban green**<br>**infrastructure for**<br>**runoff mitigation**|Support is generally<br>stronger when<br>flood-reduction and<br>environmental benefits<br>are visible, although<br>concerns about costs and<br>upkeep may reduce<br>acceptance.|High implementation<br>costs, limited urban<br>space, drainage<br>integration challenges,<br>and uncertainty under<br>extreme rainfall.|Strategic siting,<br>hydrological<br>connectivity, integration<br>with gray–blue<br>infrastructure, and<br>supportive policy and<br>planning frameworks.|Unequal access to green<br>infrastructure and<br>potential green-driven<br>gentrification remain<br>concerns.|Regular outlet cleaning,<br>sediment removal,<br>control of clogging, and<br>vegetation management<br>are commonly required.|
|**Spatial planning**<br>**and decision**<br>**support for Urban**<br>**flood management**|Acceptance increases<br>when interventions<br>visibly reduce risk and<br>involve stakeholders in<br>planning.|Limited spatial and<br>hydrological data,<br>modeling uncertainty,<br>fragmented planning,<br>and land-use<br>competition.|Fine-scale geospatial<br>analysis, integrated<br>hydrological–land-use<br>planning, and<br>institutional<br>coordination.|Benefits and risks may be<br>unevenly distributed<br>across vulnerable or<br>lower-income<br>communities.|Maintenance is<br>acknowledged in<br>planning frameworks but<br>rarely addressed<br>operationally.|
|**Catchment and**<br>**hydraulic modeling**<br>**for flood risk**<br>**reduction**|Support is shaped by<br>perceived economic and<br>land-use impacts,<br>particularly in rural<br>areas.|Uncertain hydrological<br>data, limited land<br>availability, and weak<br>integration into planning<br>standards.|Catchment-scale<br>hydraulic design,<br>connected retention<br>systems, and<br>scenario-based planning<br>tools.|Upstream communities<br>may absorb costs while<br>downstream areas<br>receive protection<br>benefits.|Maintenance focuses on<br>sustaining hydraulic<br>functionality through<br>sediment and vegetation<br>management.|
|**Floodplains,**<br>**wetlands, and**<br>**agricultural**<br>**landscapes for flood**<br>**regulation**|Some stakeholders<br>perceive NbS approaches<br>as less reliable than<br>conventional<br>infrastructure.|Land-use conflicts,<br>floodplain development,<br>and trade-offs between<br>agriculture, ecology, and<br>flood protection.|Floodplain connectivity,<br>storage capacity,<br>upstream retention, and<br>controlled water release.|Farmers and upstream<br>landowners may bear<br>implementation costs<br>disproportionately.|Engineered systems<br>often require sediment<br>management, while<br>restored vegetated<br>systems generally need<br>less intensive upkeep<br>after establishment.|
|**Ecological and**<br>**hydro-geomorphic**<br>**processes in NbS**<br>**systems**|Public support is often<br>linked to recreation,<br>aesthetics, and visible<br>environmental<br>improvements.|Site-specific<br>hydro-geomorphic<br>constraints, sediment<br>accumulation, and<br>uncertainty in ecological<br>responses.|Design aligned with<br>hydrological and<br>ecological conditions,<br>adaptive management,<br>and long-term<br>monitoring.|Uneven access to<br>blue–green spaces may<br>influence distribution of<br>environmental benefits.|Sediment-control<br>structures require<br>periodic upkeep, whereas<br>mature ecological<br>systems may require<br>limited intervention.|
|**Coastal flood risk**<br>**and shoreline**<br>**protection**|Protective and hybrid<br>shoreline measures<br>generally receive greater<br>support than managed<br>retreat strategies.|Uncertainty under<br>sea-level rise, strict<br>physical suitability<br>requirements, and high<br>implementation costs.|Hybrid coastal systems<br>tailored to local shoreline<br>dynamics and sediment<br>conditions.|Managed retreat and<br>adaptation measures<br>may disproportionately<br>affect socially vulnerable<br>populations.|Hybrid and engineered<br>systems often require<br>reinforcement and<br>sediment management.|
|**Governance,**<br>**stakeholder**<br>**engagement, and**<br>**societal uptake of**<br>**NbS**|Trust, transparency, and<br>local relevance strongly<br>influence public support.|Fragmented governance,<br>weak coordination,<br>limited funding, and<br>unclear policy<br>frameworks.|Multi-level governance,<br>cross-sector<br>collaboration, and early<br>integration into planning<br>processes.|Key concerns include<br>procedural fairness,<br>inclusion of<br>marginalized groups,<br>and distribution of costs<br>and benefits.|Long-term monitoring,<br>funding, and clearly<br>defined maintenance<br>responsibilities are<br>essential.|
|**NbS systems for**<br>**Urban water**<br>**services and climate**<br>**adaptation**|Public support is<br>generally favorable when<br>interventions address<br>flooding, heat stress, and<br>urban livability.|Fragmented governance,<br>limited funding, land<br>competition, and<br>uncertainty in long-term<br>performance.|Interconnected<br>blue–green systems<br>integrated with existing<br>infrastructure and spatial<br>planning tools.|Outcomes depend on<br>how costs,<br>responsibilities, and<br>benefits are distributed<br>across communities.|Ongoing vegetation care,<br>irrigation, sediment<br>removal, and component<br>replacement are<br>commonly required.|



_(Continued)_ 

Frontiers in Sustainability 

10 

frontiersin.org 

10.3389/frsus.2026.1966241 

Arabi et al. 

TABLE 2 (Continued) 

|Theme|Public|Key barriers|Success|Equity|Maintenance|
|---|---|---|---|---|---|
||acceptance||factors/enablers|considerations|requirements|
|**Emerging**<br>**approaches in flood**<br>**management**<br>**(unclassified)**|Public support is<br>strongest for visible and<br>participatory<br>interventions with clear<br>local relevance.|Governance<br>fragmentation, weak<br>monitoring datasets,<br>insufficient funding, and<br>dependence on gray<br>infrastructure.|Integrated planning,<br>context-specific design,<br>hybrid measures, and<br>decision-support tools.|Unequal exposure,<br>vulnerability, and access<br>to protection remain<br>important concerns.|Maintenance strategies<br>remain underdeveloped<br>and are rarely quantified<br>systematically.|



approaches that provide multiple co-benefits while enhancing longterm resilience. 

Despite this progress, the literature continues to reveal a significant gap between implementation planning and long-term system management. Considerable attention has been devoted to NbS design and initial implementation, whereas comparatively little effort has focused on understanding long-term operational performance, adaptive management, and lifecycle sustainability. Modeling studies accounted for 40% of the reviewed literature, and only two studies monitored implemented NbS for more than 5 years: a 70-month monitoring of blue-green roofs in Hamburg, Germany (Richter and Dickhaut, 2023) and a ten-year assessment of a riverbank bioengineering intervention in Brazil (Kettenhuber et al., 2023). Similarly, only 23.2% of studies reported monetary implementation costs. This imbalance is particularly important because the hydraulic and ecological performance of NbS evolves over time in response to sediment accumulation, vegetation dynamics, climate variability, and changing watershed conditions. A similar gap is evident in public acceptance which was addressed in only 30.8% of the reviewed studies. Support is consistently higher when the flood protection benefits of NbS are visible and stakeholders are actively involved in planning. Similar results have been shown for GSI (Khaniya et al., 2026). However, these same interventions often receive insufficient longterm maintenance. Although maintenance is widely recognized as essential, it is rarely addressed in practice or evaluated using standardized metrics, a common issue for all NbS (Knapik et al., 2025). In the reviewed literature, half of the studies (50.3%) did not report any maintenance requirements. As a result, the long-term performance of NbS may not meet the expectations established during planning and implementation. Future research should therefore place greater emphasis on long-term monitoring and adaptive performance assessment to ensure that flood mitigation benefits are sustained throughout the infrastructure lifecycle. 

Overall, the evidence from this analysis suggests that future advances in flood-focused NbS can be achieved by shifting from evaluating individual practices to developing integrated implementation frameworks that simultaneously incorporate engineering performance, governance capacity, environmental sustainability, and adaptive management. Projects incorporating equity and public trust as core design criteria, not as secondary considerations, show higher rates of long-term success. Such frameworks are likely to be essential for supporting resilient flood management amid increasing urbanization and climate uncertainty. 

### 3.5 Benefits of NbS 

Table 3 highlights that the benefits of NbS for flooding extend beyond flood reduction. The most consistent finding across the reviewed themes relates to ecosystem service benefits, particularly runoff regulation, infiltration, groundwater recharge, water storage, pollutant reduction, sediment retention, and nutrient control. This indicates that NbS are commonly designed and evaluated not only to reduce flood impacts, but also for improving water quantity and water quality outcomes. However, consistent metrics for measuring success are still lacking. 

The benefits also differ by application and physical setting. Urban green infrastructure is often linked to runoff retention, peakflow reduction, infiltration, water-quality improvement, urban cooling, and habitat support, while spatial planning and catchmentscale modeling studies emphasize flood attenuation, groundwater recharge, runoff detention, and water storage due to the regulations driving implementation. Floodplains, wetlands, and agricultural landscapes show additional benefits related to sediment retention, nutrient control, and carbon storage. In contrast, coastal flood-risk and shoreline-protection studies focus more on wave attenuation, storm-surge buffering, erosion control, shoreline stabilization, and sediment regulation. This pattern suggests that the value of NbS depends on the flood process, landscape context, and management objective. 

Social co-benefits are also reported across several NbS themes. Benefits such as aesthetics, recreation, thermal comfort, walkability, public-space quality, stakeholder engagement, education, protection of homes and livelihoods, safer living conditions, public awareness, and community cohesion show that NbS are often framed as community and landscape assets, not only as hydrologic interventions. Improvement of flood-prone area management involves both physical risk reduction and the improvement of urban and community spaces. This suggests that these social benefits are common co-benefits of NbS rather than outcomes unique to specific applications. However, these benefits are typically described using qualitative measures, rather than standardized or quantitative indicators, often due to a lack of sufficient metrics. 

Energy and climate co-benefits are documented in a limited number of studies. Reported benefits include reduced cooling demand from vegetated systems and lower operational energy requirements where gravity-based systems replace pumping. However, these outcomes are generally considered secondary cobenefits rather than direct flood-mitigation benefits. Across all 

Frontiers in Sustainability 

frontiersin.org 

11 

10.3389/frsus.2026.1966241 

Arabi et al. 

TABLE 3 Benefits of NbS identified from the reviewed studies. 

|Theme|Ecosystem services|Secondary energy/climate<br>co-benefits|Social co-benefits|
|---|---|---|---|
|**Urban green infrastructure for**<br>**runoff mitigation**|Runoff retention, peak-flow reduction,<br>infiltration, water-quality improvement,<br>urban cooling, and habitat support.|Reduced cooling demand through green<br>roofs and vegetated systems.|Improved aesthetics, recreation,<br>thermal comfort, walkability, and<br>urban livability.|
|**Spatial planning and decision**<br>**support for urban flood**<br>**management**|Flood attenuation, groundwater<br>recharge, infiltration, and water storage.|Indirect reductions in cooling demand<br>associated with urban greening.|Improved public space quality,<br>recreation, resilience, and<br>stakeholder engagement.|
|**Catchment and hydraulic**<br>**modeling for flood risk reduction**|Flood regulation, runoff detention,<br>groundwater recharge, and pollutant<br>reduction.|Limited evidence; occasionally linked to<br>resource-efficient water management.|Improved resilience, recreation,<br>education, and public-space<br>quality.|
|**Floodplains, wetlands, and**<br>**agricultural landscapes for flood**<br>**regulation**|Water storage, flow attenuation,<br>sediment retention, nutrient control,<br>and carbon storage.|Reduced operational energy demand where<br>gravity-based systems replace pumping.|Protection of homes and<br>livelihoods, especially in rural and<br>agricultural settings.|
|**Ecological and hydro-geomorphic**<br>**processes in NbS systems**|Flood regulation, sediment retention,<br>nutrient control, habitat provision, and<br>ecological enhancement.|Cooling benefits from vegetated and<br>water-based systems are occasionally<br>reported.|Recreation, tourism, amenity value,<br>and perceived well-being<br>associated with blue–green spaces.|
|**Coastal flood risk and shoreline**<br>**protection**|Wave attenuation, storm-surge<br>buffering, erosion control, shoreline<br>stabilization, and sediment regulation.|Direct energy-related benefits are rarely<br>reported.|Reduced flood exposure, safer<br>living conditions, and improved<br>coastal landscapes.|
|**Governance, stakeholder**<br>**engagement, and societal uptake**<br>**of NbS**|Flood mitigation, biodiversity<br>enhancement, and improved<br>environmental quality.|Energy-related outcomes are rarely evaluated<br>directly.|Improved well-being, sense of<br>place, public awareness, and<br>community cohesion.|
|**NbS systems for Urban water**<br>**services and climate adaptation**|Runoff reduction, infiltration,<br>groundwater recharge, and climate<br>regulation through interconnected<br>systems.|Potential reductions in urban cooling<br>demand through integrated system design.|Enhanced public health, recreation,<br>aesthetics, and urban livability.|
|**Emerging approaches in flood**<br>**management (unclassified)**|Runoff reduction, infiltration, retention,<br>groundwater recharge, and pollutant<br>control.|Modest reductions in building cooling<br>demand associated with vegetated<br>infrastructure.|Improved well-being, walkability,<br>recreation, and community<br>cohesion.|



nine thematic clusters, energy-related effects are typically described as indirect, context-dependent, or not systematically assessed, compared with the more established evidence for ecosystem services and social co-benefits. This highlights the need for further empirical research to better quantify energy and climate benefits while recognizing the multifunctional role of NbS as integrated flood-management strategies rather than solely floodcontrol measures. 

### 3.6 Limitations and knowledge gaps of NbS for flooding 

Table 4 reveals that the NbS flood management literature suffers from three converging weaknesses across all nine thematic clusters: over-reliance on scenario modeling rather than fieldvalidated evidence, short monitoring periods that cannot capture long-term system performance, and coarse spatial and hydrological data that limit transferability beyond individual study sites. These limitations are not isolated to particular themes; they appear with near-uniform consistency from green infrastructure and catchment hydraulics to coastal protection and governance, 

signaling a structural gap between the conceptual maturity of NbS frameworks and the empirical robustness of the evidence supporting their implementation. One notable exception is the Governance, Stakeholder Engagement, and Societal Uptake theme, where the main limitation is methodological rather than modeling related. Evidence in this area relies largely on case studies, expert opinion, and perception surveys with small sample sizes and limited long-term follow-up (Lupp et al., 2021; Bernello et al., 2022). This distinction is important because it shows that the field faces two complementary challenges: technical studies depend heavily on simulation, while social and institutional research is dominated by small-scale, cross-sectional qualitative methods. Although these limitations differ in nature, both reduce the generalizability of the findings. Another cross-cutting issue is the lack of standardized performance metrics. The need for consistent evaluation methods is identified across multiple themes, from catchment modeling to hybrid NbS approaches, indicating that the absence of common metrics is a field-wide barrier to comparing results and synthesizing evidence across different settings. 

The future research needs identified across themes converge on three priorities: long-term monitoring and validation under extreme and changing climate conditions, multi-scale 

Frontiers in Sustainability 

12 

frontiersin.org 

10.3389/frsus.2026.1966241 

Arabi et al. 

TABLE 4 Limitations and future research needs identified across the reviewed studies. 

|_Theme_|_Limitations_|_Research gaps/future research needs_|
|---|---|---|
|**Urban green infrastructure for**<br>**runoff mitigation**|Predominantly based on scenario modeling and<br>site-specific studies, with simplified hydrological<br>assumptions, short monitoring periods, limited<br>calibration, and incomplete representation of<br>drainage interactions and extreme rainfall.|Need for long-term monitoring and validation under extreme rainfall and<br>future climate conditions. Additional priorities include understanding<br>spatial configuration, hydrological connectivity, and integration with gray<br>and blue systems.|
|**Spatial planning and decision**<br>**support for Urban flood**<br>**management**|Strong dependence on data quality, spatial resolution,<br>and modeling assumptions. Many studies use coarse<br>datasets, simplified spatial models, and limited<br>validation against observed flood events.|Further work is needed to validate planning outputs using observed events<br>and implementation outcomes. Improved treatment of uncertainty, future<br>conditions, and interactions among multiple interventions is also required.|
|**catchment and hydraulic**<br>**modeling for flood risk reduction**|Heavy reliance on hydrological and hydraulic<br>simulations with limited field validation. Coarse<br>rainfall and topographic data, simplified flood<br>representation, and scenario-based assumptions<br>reduce reliability.|Research should strengthen field validation, long-term monitoring, and<br>standardized evaluation methods across scales and climates. Basin-scale<br>interactions within connected and hybrid systems also remain insufficiently<br>understood.|
|**Floodplains, wetlands, and**<br>**agricultural landscapes for flood**<br>**regulation**|Evidence is often derived from short-term studies,<br>simplified hydrological and sediment representations,<br>and coarse spatial datasets. Findings are frequently<br>site-specific.|Long-term assessment under repeated flood events and changing<br>environmental conditions is needed. Additional research should address<br>sediment processes, operational performance, and trade-offs among flood<br>regulation, water quality, biodiversity, and agricultural functions.|
|**Ecological and hydro-geomorphic**<br>**processes in NbS systems**|Many studies rely on short monitoring periods,<br>single-site investigations, or controlled laboratory<br>and modeling conditions. Ecological and<br>hydro-geomorphic measurements are often<br>incomplete.|Future studies should link hydro-geomorphic and ecological dynamics<br>across broader spatial and temporal scales through long-term monitoring<br>and field validation. Sediment, pollutant, and biodiversity dynamics also<br>require further investigation.|
|**Coastal flood risk and shoreline**<br>**protection**|Existing evidence is largely scenario-based and<br>sensitive to assumptions regarding shoreline<br>dynamics, flood probability, and adaptation costs.<br>Long-term implementation evidence remains limited.|More evidence is needed on long-term durability and performance under<br>sea-level rise and extreme storms. Research should also examine shoreline<br>dynamics, sediment accretion, and hybrid coastal-system performance.|
|**Governance, stakeholder**<br>**engagement, and societal uptake**<br>**of NbS**|Studies are commonly based on case studies, expert<br>opinion, and perception surveys, with limited<br>longitudinal analysis and small sample sizes.|Additional research is needed on long-term implementation performance,<br>cost-effectiveness, and scalability across governance contexts. Institutional<br>structures, stakeholder interactions, and policy mechanisms also require<br>further evaluation.|
|**NbS systems for Urban water**<br>**services and climate adaptation**|Many studies use incomplete or low-resolution<br>hydrological and climate datasets with limited<br>calibration and validation. Empirical evidence is<br>often restricted to a small number of cases.|Future work should improve empirical validation under long-term climate<br>variability, particularly in data-poor urban areas. Vegetation dynamics,<br>system integration, and interactions with urban development also require<br>further study.|
|**Emerging approaches in flood**<br>**management (unclassified)**|Current evidence is dominated by conceptual<br>frameworks, modeling studies, and secondary<br>datasets with limited empirical validation. Short<br>observation periods and sparse calibration data<br>reduce broader applicability.|Further research should evaluate emerging and hybrid approaches under<br>extreme events and future climate conditions. Standardized performance<br>metrics, stronger monitoring datasets, and understanding of<br>local-to-catchment-scale interactions are also needed.|



integration from local interventions to basin-level interactions, and uncertainty-aware decision support that can account for climate, socioeconomic, and governance variability. These gaps are significant because they represent the missing links between NbS science and actionable investment planning, particularly in data-scarce or climate-vulnerable contexts where the stakes of under-informed decisions are highest. Collectively, Table 4 makes a strong case for research that is empirically grounded, longitudinally sustained, and explicitly designed to support decision-making under deep uncertainty. 

### 3.7 Limitations of the LLM-assisted workflow 

While the AI-assisted workflow improved the efficiency and consistency of evidence synthesis, its outputs are shaped by how the LLM processes scientific text at each stage of the review. During structured dataset development, information that is explicitly reported, such as study objectives, methods, and hydrological performance outcomes, was extracted more consistently than qualitative dimensions that are often discussed 

Frontiers in Sustainability 

frontiersin.org 

13 

10.3389/frsus.2026.1966241 

Arabi et al. 

briefly or indirectly, including social co-benefits, institutional conditions, and maintenance requirements. Similarly, during thematic mapping and cluster development, cluster labels were generated from representative keywords, which tend to favor dominant technical terminology and may assign interdisciplinary studies to engineering-oriented themes or to the unclassified group. During qualitative information synthesis, aggregating findings across many studies may also reduce the visibility of contradictory or context-specific results. These effects were addressed through several measures integrated into the methodology. Adversarial constraints restricted the model to information directly reported in the studies and required unreported information to be returned as null values rather than inferred. Role-based and fewshot prompting standardized the structure and level of detail of the outputs. Human-in-the-loop validation at the extraction and synthesis stages identified unsupported interpretations and inconsistent categorization, which were used to iteratively refine the prompts, and the consolidated themes were manually reviewed for consistency and interpretability. In the final dataset, 171 records (92.4%) were assigned high extraction confidence, 14 (7.6%) medium confidence, and none low confidence; all flagged fields and all medium-confidence records were verified against the original full texts. 

## 4 Conclusions 

This study presents an AI-assisted systematic review and thematic analysis of 185 peer-reviewed studies on nature-based solutions (NbS) for water management in flood-prone areas. The main findings are: 

1. Rapid growth of the literature. Publications increased from 2 studies in 2016 to 45 in 2025, with 79.5% of the reviewed studies published between 2021 and 2025. This growth partly reflects the wider adoption of NbS terminology. 

2. Nine research themes identified. Urban green infrastructure, spatial planning and decision support, and catchment and hydraulic modeling accounted for 47.6% of the literature. In contrast, coastal protection (2.2%) and integrated urban water systems (3.8%) received limited attention. 

3. Research priorities are shifting. Compared with 2016–20, the share of Urban green infrastructure studies decreased from 31.6 to 15.6% during 2021–25, while research on planning, floodplains and wetlands, and hybrid approaches increased. Coastal and governance research showed limited growth. 

4. Geographic coverage remains uneven. Research is concentrated in the United Kingdom, China, and the United States, followed by Italy and Australia, while Africa and Latin America remain strongly underrepresented. Broader geographic evidence is needed to improve the transferability of NbS knowledge. 

5. Implementation is strongly shaped by governance. Across the reviewed literature, successful NbS implementation depended not only on technical performance but also on integrated planning, cross-sector governance, public trust, maintenance, and equitable distribution of costs and benefits. 

6. NbS provide multiple benefits. Reported benefits included infiltration, water quality improvement, sediment retention, 

recreation, aesthetics, and community cohesion. Energy and climate co-benefits were less frequently quantified. 

7. Evidence gaps remain substantial. The literature relies heavily on scenario-based modeling and short-term monitoring, with limited standardized assessment of maintenance, equity, governance, and long-term performance. Evidence from diverse geographic and socioeconomic settings is also limited. 

8. AI-assisted analysis supported large-scale synthesis. LLMassisted screening, extraction, and synthesis combined with unsupervised clustering and human validation enabled systematic analysis of the large literature corpus. Compared with previous NbS reviews that relied on manual coding or bibliometric analysis, this approach enabled structured extraction of implementation-related information, such as costs, maintenance, equity, and barriers, from the full texts of all reviewed studies. However, risks related to unsupported statements, nuanced concepts such as equity, and language bias remain important considerations. Biases inherited from model training data may also affect outputs. These risks were mitigated through adversarial prompt constraints, null-value rules for unreported information, and human verification of flagged outputs. 

Overall, the findings indicate that future NbS research should prioritize long-term field-based monitoring under extreme events, standardized metrics for maintenance, equity, and co-benefits, multi-scale assessment linking site-level interventions to catchment processes, and greater evidence from underrepresented regions. These priorities align closely with current research and innovation programs, such as Horizon Europe and its Mission on Adaptation to Climate Change, which emphasize demonstrating NbS at scale, evaluating their long-term effectiveness, and supporting just and inclusive adaptation (Wild et al., 2020). These efforts can strengthen the empirical basis for resilient and transferable NbS implementation. 

## Data availability statement 

The original contributions presented in the study are included in the article/Supplementary material, further inquiries can be directed to the corresponding author. 

## Author contributions 

SA: Data curation, Investigation, Conceptualization, Visualization, Formal analysis, Validation, Writing – review & editing, Project administration, Writing – original draft, Methodology. DY: Investigation, Validation, Writing – original draft. MR: Validation, Investigation, Writing – original draft. BB: Validation, Investigation, Writing – original draft. TS: Validation, Writing – original draft, Investigation. NK: Investigation, Writing – original draft, Validation. ME: Investigation, Validation, Writing – original draft. VS: Writing – review & editing, Supervision, Conceptualization, Investigation, Validation, Methodology, Resources, Funding acquisition, Project administration, Writing – original draft. 

Frontiers in Sustainability 

frontiersin.org 

14 

10.3389/frsus.2026.1966241 

Arabi et al. 

## Funding 

The author(s) declared that financial support was not received for this work and/or its publication. 

## Acknowledgments 

Portions of this study’s methodology, including literature screening, structured data extraction, and thematic synthesis, were conducted using OpenAI’s GPT-5.4 API, as described in the data and methods section. 

## Conflict of interest 

The author(s) declared that this work was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest. 

## Generative AI statement 

The author(s) declared that Generative AI was used in the creation of this manuscript. Generative AI was used in the preparation of this manuscript, as described in detail in the 

Data and methods section. It was used to assist with literature screening, data extraction, organization, and thematic analysis. The author(s) reviewed and validated all AI-assisted outputs to ensure the accuracy of the content. 

Any alternative text (alt text) provided alongside figures in this article has been generated by Frontiers with the support of artificial intelligence and reasonable efforts have been made to ensure accuracy, including review by the authors wherever possible. If you identify any issues, please contact us. 

## Publisher’s note 

All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher. 

## Supplementary material 

The Supplementary Material for this article can be found online at: https://www.frontiersin.org/articles/10.3389/frsus.2026. 1966241/full#supplementary-material 

## References 

Ahmad, S., Jia, H., Ashraf, A., Yin, D., Chen, Z., Ahmed, R., et al. (2024). A novel GIS-SWMM-ABM approach for flood risk assessment in data-scarce urban drainage systems. _Water_ 16:1464. doi: 10.3390/w16111464 

Bernello, G., Mondino, E., and Bortolini, L. (2022). People’s perception of nature-based solutions for flood mitigation: the case of Veneto Region (Italy). _Sustainability_ 14:4621. doi: 10.3390/su14084621 

Chen, S. F., Alyakin, A., Seas, A., Yang, E., Choi, J. J., Lee, J. V., et al. (2026). LLMassisted systematic review of large language models in clinical medicine. _Nat. Med._ 32, 1152–1159. doi: 10.1038/s41591-026-04229-5 

Cook, L. M., Good, K. D., Moretti, M., Kremer, P., Wadzuk, B., Traver, R., et al. (2024). Towards the intentional multifunctionality of urban green infrastructure: a paradox of choice? _Npj Urban Sustain._ 4:12. doi: 10.1038/s42949-024-00145-0 

Fang, X., Li, J., and Ma, Q. (2023). Integrating green infrastructure, ecosystem services and nature-based solutions for urban sustainability: a comprehensive literature review. _Sustain. Cities Soc._ 98:104843. doi: 10.1016/j.scs.2023.104843 

Fletcher, T. D., Shuster, W., Hunt, W. F., Ashley, R., Butler, D., Arthur, S., et al. (2015). SUDS, LID, BMPs, WSUD and more–the evolution and application of terminology surrounding urban drainage. _Urban Water J._ 12, 525–42. doi: 10.1080/1573062X.2014.916314 

Grootendorst, M. (2022). BERTopic: neural topic modeling with a class-based TF-IDF procedure. ArXiv [Preprint] ArXiv: 220305794. 

Hansen, R., and Pauleit, S. (2014). From multifunctionality to multiple ecosystem services? A conceptual framework for multifunctionality in green infrastructure planning for urban areas. _Ambio_ 43, 516–29. doi: 10.1007/s13280-014-0510-2 

Iqbal, A., Soni, L., Qazi, A. W., and Nazir, H. (2025). Utilizing remote sensing for Sponge City development: enhancing flood management and Urban resilience in Karachi. _Remote Sens._ 17:1818. doi: 10.3390/rs17111818 

Izuchukwu Precious, O., Zino Izu, O., Frank Chudi, A., Theresa Ojevwe, A., and Chinwe Sheila, N. (2025). The economic costs of climate disasters analyzing data from recent floods, wildfires, and hurricanes. _Manuscr. Sustain. Econ. Finance Manag._ 2, 1–22. doi: 10.5281/zenodo.15010126 

Johnson, B. A., Kumar, P., Okano, N., Dasgupta, R., and Shivakoti, B. R. (2022). Nature-based solutions for climate change adaptation: a systematic review of systematic reviews. _Nat.-Based Solut._ 2:100042. doi: 10.1016/j.nbsj.2022.100042 

Keeler, B. (2020). _It is Not Easy Being Green: recognizing Unintended Consequences of Green Stormwater Infrastructure_ . Water. doi: 10.3390/w12020522 

Kettenhuber, P. L. W., Santos Sousa, R., Dewes, J. J., Rauch, H. P., Sutili, F. J., and Hörbinger, S. (2023). Performance assessment of a soil and water bioengineering work on the basis of the flora development and its associated ecosystem processes. _Ecol. Eng._ 186:106840. doi: 10.1016/j.ecoleng.2022.106840 

Khaniya, B., Szota, C., Fletcher, T. D., and Drake, J. (2026). Urban stormwater management using green infrastructure: challenges and solutions to enhance long-term performance and stakeholder acceptance. _Blue-Green Syst._ 8, 188–207. doi: 10.2166/bgs.2026.016 

Knapik, E., Brandimarte, L., and Usher, M. (2025). Maintenance in sustainable stormwater management: issues, barriers and challenges. _J. Environ. Plan. Manag._ 68, 2769–95. doi: 10.1080/09640568.2024.2325041 

Krauss, L., and Rippy, M. A. (2022). Adaptive strategy biases in engineered ecosystems: implications for plant community dynamics and the provisioning of ecosystem services to people. _People Nat._ 4, 1644–63. doi: 10.1002/pan3.10413 

Li, H., Ding, L., Ren, M., Li, C., and Wang, H. (2017). Sponge city construction in China: a survey of the challenges and opportunities. _Water_ 9:594. doi: 10.3390/w9090594 

Lupp, G., Huang, J. J., Zingraff-Hamed, A., Oen, A., Del Sepia, N., Martinelli, A., et al. (2021). Stakeholder perceptions of nature-based solutions and their collaborative co-design and implementation processes in rural mountain areas—a case study from PHUSICOS. _Front. Environ. Sci._ 9:678446. doi: 10.3389/fenvs.2021. 678446 

Maimuri, N., Altahir, A., Abdulameer, L., Rashid, F., and Al-Dujaili, A. (2025). Smart rubber balloon dam for coastal hurricane and tsunami protection: a renewable energypowered system with hydrodynamic design and adaptive control. _Int. J. Math. Eng. Manag. Sci._ 10, 2286–317. doi: 10.33889/IJMEMS.2025.10.6.106 

Frontiers in Sustainability 

frontiersin.org 

15 

10.3389/frsus.2026.1966241 

Arabi et al. 

Massenberg, J. R., and Panduro, T. E. (2024). _Nature-based solutions for flood risk reduction: a review and guidance for coastal protection_ . Scientific Report from DCE - Danish Centre for Environment and Energy No. 623. Aarhus: Aarhus University, DCE - Danish Centre for Environment and Energy. McInnes, L., Healy, J., and Astels, S. (2017). hdbscan: hierarchical density based clustering. _J. Open Source Softw._ 2:205. doi: 10.21105/joss.00205 

McInnes, L., Healy, J., and Melville, J. (2018). Umap: uniform manifold approximation and projection for dimension reduction. ArXiv [Preprint] ArXiv: 180203426. doi: 10.21105/joss.00861 

Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., et al. (2021). The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. _BMJ_ 372:n71. doi: 10.1136/bmj.n71 

Reimers, N., and Gurevych, I. (2020). “Making monolingual sentence embeddings multilingual using knowledge distillation,” in _Proceedings of the 2020 conference on empirical methods in natural language processing (EMNLP)_ (Online: Association for Computational Linguistics), 4512–4525. doi: 10.18653/v1/2020.emnlp-main.365 Richter, M., and Dickhaut, W. (2023). Long-term performance of blue-green roof systems—results of a building-scale monitoring study in Hamburg, Germany. _Water_ 15:2806. doi: 10.3390/w151 52806 

Scherbakov, D., Hubig, N., Jansari, V., Bakumenko, A., and Lenert, L. A. (2025). The emergence of large language models as tools in literature reviews: a large 

language model-assisted systematic review. _J. Am. Med. Inform. Assoc._ 32, 1071–86. doi: 10.1093/jamia/ocaf063 

Seddon, N., Chausson, A., Berry, P., Girardin, C. A., Smith, A., and Turner, B. (2020). Understanding the value and limits of nature-based solutions to climate change and other global challenges. _Philos. Trans. R. Soc. B Biol. Sci._ 375:20190120. doi: 10.1098/rstb.2019.0120 

Wang, H., Mei, C., Liu, J., and Shao, W. (2018). A new strategy for integrated urban water management in China: Sponge city. _Sci. China Technol. Sci._ 61, 317–29. doi: 10.1007/s11431-017-9170-5 

Wang, M., Sun, C., and Zhang, D. (2023). Opportunities and challenges in green stormwater infrastructure (GSI): a comprehensive and bibliometric review of ecosystem services from 2000 to 2021. _Environ. Res._ 236:116701. doi: 10.1016/j.envres.2023.116701 

Wild, T., Freitas, T., and Vandewoestijne, S. (2020). _Nature-Based Solutions: state of the Art in EU-Funded Projects_ . Luxembourg: Publications Office of the European Union. doi: 10.2777/236007 

Yin, C., and Zhang, Z. (2024). _A Study of Sentence Similarity Based on the All-Minilml6-v2 Model with “Same Semantics, Different Structure” After Fine Tuning_ . Atlantis Press 677–684. doi: 10.2991/978-94-6463-540-9_69 

Zhai, H., Gu, B., and Wang, Y. (2023). Evaluation of policies and actions for naturebased solutions in nationally determined contributions. _Land Use Policy_ 131:106710. doi: 10.1016/j.landusepol.2023.106710 

Frontiers in Sustainability 

16 

frontiersin.org 
