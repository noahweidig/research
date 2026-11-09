---
title: Global disparities and structural imbalances in AI integration for urban climate resilience research
authors:
- Meng, Meiyao
- Hamm, Nicholas A. S.
- Yang, Liang Emlyn
- Wang, Jianghao
- Chan, Faith Ka Shun
year: '2026'
journal: npj Climate Action
doi: 10.1038/s44168-026-00431-w
tags:
- climate
- large wildfires
- resilience
- united states
zotero_key: IE97SCPC
item_type: journalArticle
url: https://openalex.org/W7214455021
source_url: 'unpaywall: https://www.nature.com/articles/s44168-026-00431-w_reference.pdf'
fulltext_status: fulltext
synced: '2026-11-09'
---

# Global disparities and structural imbalances in AI integration for urban climate resilience research

## Abstract

Artificial intelligence (AI) holds transformative potential to decode urban climate resilience (UCR) complexities, yet its unguided expansion risks amplifying systemic biases. Here, we leverage large language models to conduct a systematic analysis of around 12,500 UCR publications from 2005 to 2024. Our findings reveal a fifteenfold increase in AI-related publications since 2018, yet this growth remains geographically concentrated: the United States, China, and the United Kingdom account for ~40% of AI-integrated studies, highlighting a deepening digital divide in both research capacity and geographic focus that limits the transferability of AI models to low-income regions. Crucially, we identify a statistically significant structural imbalance: while AI is heavily deployed for physical hazard prediction (40%), it remains under-represented in governance resilience domains (<4%). This asymmetry suggests a greater emphasis on quantifiable, engineering-oriented problems than on social-institutional adaptation needs relevant to vulnerable populations. We argue that bridging this gap requires a pivot from purely data-driven optimisation of physical systems toward human-centric AI paradigms that integrate unstructured socio-economic knowledge, ensuring technologies address the holistic needs of complex urban environments.

## Full text

npj | climate action 

Article 

## Article in Press 

https://doi.org/10.1038/s44168-026-00431-w 

# Global disparities and structural imbalances in AI integration for urban climate resilience research 



Check for updates 

Mei Meng 1,2, Nicholas A. S. Hamm1, Liang Emlyn Yang3,4, Jianghao Wang 2,5 & Faith K. S. Chan 1 

Artificial intelligence (AI) holds transformative potential to decode urban climate resilience (UCR) complexities, yet its unguided expansion risks amplifying systemic biases. Here, we leverage large language models to conduct a systematic analysis of around 12,500 UCR publications from 2005 to 2024. Our findings reveal a fifteenfold increase in AI-related publications since 2018, yet this growth remains geographically concentrated: the United States, China, and the United Kingdom account for ~40% of AI-integrated studies, highlighting a deepening digital divide in both research capacity and geographic focus that limits the transferability of AI models to low-income regions. Crucially, we identify a statistically significant structural imbalance: while AI is heavily deployed for physical hazard prediction (40%), it remains under-represented in governance resilience domains (<4%). This asymmetry suggests a greater emphasis on quantifiable, engineering-oriented problems than on social-institutional adaptation needs relevant to vulnerable populations. We argue that bridging this gap requires a pivot from purely data-driven optimisation of physical systems toward human-centric AI paradigms that integrate unstructured socio-economic knowledge, ensuring technologies address the holistic needs of complex urban environments. 

As climate shocks become increasingly frequent and intense, cities face a dual challenge of accelerating environmental change and deepening urban system complexity<sup>1</sup> . This urgency and complexity crisis has necessitated a paradigm transition from reactive disaster management to proactive systemic resilience<sup>2–4</sup> . Governments and international organisations have prioritised urban resilience, exemplified by SDG 11, mainly for reducing urban vulnerability, and SDG 13 emphasises adaptive capacity, catalysing a global surge in scientific enquiry<sup>5,6</sup> . Consequently, urban climate resilience (UCR) has emerged as a rapidly evolving research field that seeks to understand and enhance cities’ capacity to withstand, adapt to, and recover from climate-related shocks<sup>7,8</sup> . 

This concept has been extensively applied across diverse domains, ranging from addressing specific hazards like climate change adaptation<sup>9</sup> and urban flooding<sup>10</sup> , to reinforcing critical urban subsystems such as infrastructure resilience<sup>11–14</sup> , social resilience<sup>15,16</sup> , and governance and policy resilience<sup>17</sup> . Methodologically, the field has expanded to include diverse approaches, spanning from traditional engineering solutions to nature- 

based interventions, and from social vulnerability assessments to advanced computational modelling<sup>12,18–20</sup> . 

As UCR researchevolves into a multidisciplinary field characterisedby diverseapplicationscenarios,traditionalapproachesfacecriticallimitations, particularly when confronting the proliferation of heterogeneous data sources and the non-linear, interdependent mechanisms within urban systems<sup>21,22</sup> .Inresponse,artificialintelligence(AI)isdemonstratinggrowing potential across the entire resilience cycle, including forecasting hazards, assessing impacts during and after events, and enhancing the interpretation of complex risk information for diverse stakeholders<sup>23,24</sup> . Moreover, distinct AI algorithms address specific analytical needs: machine learning (ML) accelerates hazard risk assessment by replacing computationally expensive simulations<sup>25,26</sup> ; Deep learning (DL) extracts granular damage patterns from satellite or street-level imagery<sup>27</sup> ; while natural language processing (NLP) decodes urban social resilience by analysing policy documents and identifying governance gaps in adaptation plans<sup>28,29</sup> . 

> 1School of Geographical Sciences, University of Nottingham Ningbo China, Ningbo, China. 2State Key Laboratory of Resources and Environmental Information System, Institute of Geographic Sciences and Natural Resources Research, Chinese Academy of Sciences, Beijing, China.<sup>3</sup> Department of Geography, Ludwig Maximilian University of Munich (LMU), Munich, Germany.<sup>4</sup> Chulalongkorn University Social Research Institute, Chulalongkorn University, Bangkok, Thailand. 

> 5College of Resources and Environment, University of Chinese Academy of Sciences, Beijing, China. e-mail: wangjh@lreis.ac.cn; faith.chan@nottingham.edu.cn 

npj Climate Action 

Article in Press 

Article 

https://doi.org/10.1038/s44168-026-00431-w 



Fig. 1 | Methodological workflow for large-scale literature mining. The framework proceeds in three stages: (1) Data collection: Retrieval of 12,498 abstracts from Web of Science using a three-tier keyword search strategy; (2) AI classification and verification: Initial identification of 572 AI-related abstracts using GPT-4 Turbo, followed by manual verification, resulting in a final subset of 495 AI-integrated 

abstracts (see Methods and Supplementary Fig. 6 for the full screening process); and (3) Thematic analysis: Semantic clustering using BERTopic powered by the allMiniLM-L6-v2 sentence transformer, UMAP dimensionality reduction, and HDBSCAN clustering to identify 56 distinct research topics. 

Despite the rapid expansion of UCR research, the current understanding of this landscape remains fragmented. Recent reviews have synthesised knowledge across specific facets, such as coastal<sup>30</sup> and flood resilience<sup>31</sup> , or focused on isolated domains like governance<sup>32</sup> and infrastructure<sup>33</sup> . Similarly, other studies have examined AI applications from a purely methodological standpoint<sup>34,35</sup> . However, it remains unclear how research priorities have evolved at a systemic level, specifically whether AI technologies are addressing the most critical resilience deficits or merely optimising data-rich domains. Without a systemic understanding of these patterns, the field risks drifting towards a technological centre<sup>36–38</sup> , a trajectory driven by data availability rather than urgent urban adaptation needs. 

The technical complexity and exponential growth of UCR literature pose significant challenges for traditional, expert-driven systematic reviews<sup>39,40</sup> . To overcome these bottlenecks, researchers have begun leveraging ML and large language models (LLMs) to assist with literature screening and thematic analysis<sup>41,42</sup> . For example, the application of bidirectional encoder representations from transformers (BERT) has enabled effective topic identification across large corpora exceeding 100,000 publications<sup>43–45</sup> . Furthermore, recent advancements in generative models, such as ChatGPT, have significantly accelerated the large-scale retrieval and automated classification of scientific literature<sup>46</sup> . 

Here, we employed advanced NLP techniques to map the evolution and current landscape of AI applications in UCR research. Our analysis addresses three key questions: (1) What are the temporal-spatial trends and 

thematic evolution characterising UCR research? (2) How has AI adoption progressed across time, geography, and research themes within UCR? (3) What are the application differences of various AI methods across specific UCR scenarios? To answer these questions, we developed a two-step analytical framework integrating GPT-4 Turbo with the BERTopic model to systematically analyse the abstracts of 12,498 UCR publications. Our findings reveal distinct evolutionary phases, identify structural imbalances in AI deployment across resilience domains, and expose the gap between technological capabilities and governance needs, offering data-driven insights for researchers and policymakers in global climate-resilient urban development. 

## Results 

### Model framework and validation 

To map the global UCR landscape, we established a comprehensive literature mining framework integrating generative AI with advanced topic modelling (see Fig. 1 and Methods for details): We first retrieved 12,498 bibliographicrecordsfromtheWebofScienceCoreCollection(2005–2024) using a three-tier keyword strategy that intersected resilience concepts, technological terminology, and urban systems interventions. To distinguish AI-integrated studies, we deployed GPT-4 Turbo as a binary classifier via specific prompt engineering (Supplementary Notes 1). Subsequently, we applied BERTopic<sup>47</sup> to analyse the semantic structure of the identified literature (Supplementary Fig. 1). This approach utilised UMAP for dimensionality reduction and HDBSCAN<sup>48,49</sup> for hierarchical clustering (see 

npj Climate Action 

Article in Press 

Article 

https://doi.org/10.1038/s44168-026-00431-w 

Supplementary Note 2 for details), which yielded 56 distinct thematic clusters. 

To validate the accuracy of the binary classification approach and mitigate potential abstraction bias, we implemented a multi-stage verification strategy (see Methods). First, we conducted a full-text accuracy assessmentusingastratifiedrandomsampleof 100publications.Theresults demonstrate high alignment between the abstract-level automated classification and full-text human review, achieving an average Cohen’s Kappa of 0.86 across all domains (Supplementary Table 1). Additionally, against an independent human-annotated ground truth of 650 abstracts (~5% of the total), GPT-4 Turbo achieved exceptional classification performance (Precision = 0.982, Recall = 0.988, F1-score = 0.985) (Supplementary Fig. 2). Furthermore, to mitigate potential model-specific biases in classification, cross-validation across multiple LLMs (DeepSeek-V3, Gemini-2.5-flash, and GPT-3.5-turbo) demonstrated “almost perfect” inter-model agreement (Fleiss’ κ ¼ 0:907), confirming that our classification criteria are objective (Supplementary Tables 2 and 3). 

Subsequently, to eliminate parameter selection bias within the UMAP and HDBSCAN algorithms, we implemented a Bayesian hyperparameter optimisationframework,achievingamaximumSilhouetteScoreof0.66and yielding 56 distinct thematic clusters (Supplementary Fig. 3). The semantic interpretability and distinctiveness of these clusters were quantitatively confirmed through high topic coherence (Cv ¼ 0:661) and topic diversity (TD ¼ 0:718) scores. To further validate the robustness of topic modelling, we conducted post hoc validation including inter-rater reliability tests and boundary-case inspections. The manual mapping of topics into broader thematic categories yielded a Cohen’s kappa of 0.89, and the validation of algorithmically derived clusters yielded 0.84, both indicating strong interrater agreement (Supplementary Table 4). 

Rapid expansion and acceleratingAI integration inUCR research Our systematic analysis of 12,498 publications delineates a trajectory of exponential growth and increasing technological sophistication. Aligning our periodisation with the release cycles of IPCC assessment reports (ARs)<sup>50–52</sup> , the milestone documents that have profoundly shaped climate change research agendas, we identify three distinct evolutionary phases: (1) an emergence phase (2005–2013) focused on foundational conceptualisation following AR4’s emphasis on mainstreaming urban adaptation; (2) a consolidation phase (2014–2021) characterised by steady methodological diversification in response to AR5’s call for integrated approaches combining adaptation and mitigation with broader societal goals; and (3) an acceleration phase (2022–2024) defined by a surge in output and the integration of advanced computational tools, reflecting AR6’s emphasis on transformative adaptation and digital solutions (see Fig. 2a). 

This acceleration phase is particularly striking, accounting for 51.8% of the total corpus with annual output surging from 1178 publications in 2020 to 2893 in 2024, a 145% increase. This proliferation aligns with heightened global climate urgency following major extreme weather events and international policy mandates (e.g., IPCC AR6, COP26), alongside the COVID19 pandemic, which brought systemic urban resilience into sharp focus. 

Crucially, AI adoption within this expanding landscape exhibits a distinctnon-lineartrajectory.Froma marginalpresencein2014(0.98%),AI integration has climbed to 7.29% by 2024. Most notably, we observe a pivotal inflexion point between 2023 and 2024, where AI-integrated publications more than doubled (from n = 88 to 211) (Supplementary Table 6). Thissurgesuggeststhatthe fieldhasmovedbeyondexperimentalpilotingto a phase of rapid technological assimilation, driven by the increasing accessibility of generative AI and advanced machine learning tools. 

### Global disparities and patterns of technological adoption 

Geographically, the UCR research landscape exhibits a profound geopolitical asymmetry, reflecting systemic inequalities in global research capacity (Fig. 2b). The top five contributors: the United States (17.0%), China (9.7%), the United Kingdom (7.1%), Australia (4.6%), and Germany (3.9%), collectivelyaccountforover40% of the globaloutput (SupplementaryTable 7). 

This concentration is even more stark when analysed through economic stratification (Fig. 2c): high-income economies produce 69.3% of all publications and control 60.1% of AI-integrated research, exceeding previously reported globalbenchmarksforscientific and technologicalproduction<sup>53</sup> .In sharp contrast, low-income nations contribute less than 1% to both categories, highlighting a critical digital divide in climate resilience knowledge production. 

The intensity of AI integration reveals a divergent technological landscape that challenges this volume-based hierarchy. While the United StatesmaintainstheleadinabsoluteAIpublicationvolume(n = 173),China exhibits a higher relative adoption rate (6.4 vs. 4.3%), suggesting a more pronounced strategic integration of computational methods in Chinese urban research. Notably, high adoption rates are also observed in emerging research communities such as Saudi Arabia (18.4%), Malaysia (12.7%), and Egypt (9.7%). To further investigate the drivers of geographic inequality and assess whether economic capacity directly forecasts AI adoption, we conducted a hierarchical regression analysis (Supplementary Table 8). The results indicate that economic wealth influences AI adoption indirectly through overall research infrastructure. This pattern underscores that geographic disparities in AI are largely explained by differences in established research ecosystems rather than mere economic resources. This imbalance extends beyond research production to the geographic focus of urban case studies. A comparison of author affiliation countries and extracted study-area locations indicates a dual underrepresentation of the Global South: low- and lower-middle-income countries are systematically underrepresented both as producers of knowledge and as subjects of investigation (Supplementary Fig. 4). 

The interdisciplinary architecture of UCR research is vast, spanning 198 distinct disciplines and over 1900 journals (Supplementary Table 9). While the field is anchored by Environmental Sciences (33.5%) and Environmental Studies (21.4%), the penetration of AI varies significantly across domains (Fig. 2d). Environmental Sciences leads in the volume of AI applications(n = 201),yetRemoteSensingdemonstratesthehighestdensity of AI integration, with 20.18% of its publications employing AI methods. This disparity highlights a technological gradient, where data-rich, observation-based disciplines exhibit a significantly higher degree of AI integration compared to policy or social science-oriented domains. 

### Thematic landscape and research priority evolution 

Our semantic analysis (see Methods) uncovers a complex cognitive architecture comprising 56 distinct thematic clusters, mapping the evolving priorities of UCR research (Supplementary Tables 10–12). These clusters structurally align along two primary axes: hazard-specific responses and systemicurbaninterventions,with flowwidthsinFig. 3 quantifyingtheircooccurrence weights. 

The discourse is anchored by general climate change paradigms (41.1%, n = 3553), with a dominant emphasis on ecological resilience (25.1%, n = 2170).Notably,Topic2(green_nature_urban_nbs) and Topic6 (ecological_resilience_china_carbon) underscore a strategic shift towards ecosystem-based strategies (Detailed topic information see Supplementary Table 10). This trend is particularly pronounced in Chinese urban contexts, aligning with a surge in empirical studies evaluating regional policy pilots like the Sponge City initiative<sup>54</sup> . 

Parallel to this, governance remains a foundational pillar (12.6%, n = 1090), with Topic 1 (climate_adaptation_change_resilience) and 16 (flood_risk_resilience_flooding) focusing on the institutional architecture of resilience—specifically adaptation planning, assessment methodologies, and policy implementation frameworks. 

A distinct contrast in research approaches emerges when analysing hazard-specific research. Flood resilience (19.8%, n = 1710) exhibits a high degree of scientific attention. Over 32% of flood-related studies focus on engineering and computational solutions (Topic 20: flood_models_learning_model, Topics 21: flood_resilience_disaster_evaluation, Topics 28: flood_risk_hurricane_flooding, Topics 36: media_data_disaster_tweets, Topics 46: flood_model_flooding_rainfall). Specifically, Topics 

npj Climate Action 

Article in Press 

Article 

https://doi.org/10.1038/s44168-026-00431-w 



Fig. 2 | Trends and global distribution of publications related to UCR (2005–2024). a The blue line represents the annual total number of relevant publications, while the red bars indicate the annual share of publications using AI methods. Red error bars show the 95% confidence intervals for the AI- integrated share. Inset: The nested circles depict the hierarchical structure of the dataset: all publications retrieved from the WoS, the subset included in the analysis, and those 

identified as utilising AI techniques. b The geographical distribution of UCR publications based on the countries of the authors’ affiliated institutions. c Publication distribution by income group. The bar chart presents a classification of both the total and AI-integrated publications by national income level, following the World Bank’s income classifications for 2023–2024. d Publication distribution by discipline. Displays the top ten disciplinary fields by publication count. 

npj Climate Action 

Article in Press 

Article 

https://doi.org/10.1038/s44168-026-00431-w 

Fig. 3 | The semantic architecture of UCR research. The Sankey diagram displays the distribution and co-occurrence relationships of hazard clusters (left) and urban systems interventions (right) across all UCR-related abstracts, as classified by BERTopic. The width of the flows quantitatively represents the co-occurrence frequency (weight) between specific hazards and interventions. 



21 and 28 highlight the integration of AI for predictive modelling, while Topic 36 pioneers the use of urban big data (e.g., social media signals) for real-time risk identification. 

In contrast, heatwave research (18.0%, n = 1551) prioritises physiological well-being and spatial interventions. The vast majority of publications (80%, Topic 0: heat_thermal_urban_temperature) address the Urban Heat Island (UHI) effect through a multi-scalar framework: community-level interventions favour nature-based solutions such as green space expansion (Topic 22: trees_species_urban), while building-level approaches focus on energy optimisation and material performance (Topic 17: power_distribution_outages_energy). This divergence indicates that while flood research is driving the field’s computational frontier, heat research is advancing its socio-ecological integration. 

Finally, the analysis reveals a highly diverse thematic landscape characterised by integrated complexity and a methodological divergence across multi-hazardassessments.However,asFig. 3 providesonlyastaticsnapshot of the entire UCR field, to further explore how these research priorities have shifted over time and to what extent AI methodologies drive these capabilities, we further examine the AI-driven methodological landscape, temporal dynamics and specific functional applications through representative case studies. 

### AI-driven methodological transformation and functional applications 

Analysis of 495 AI-integrated abstracts reveals a distinct methodological landscape dominated by traditional Machine Learning (ML) (60.6%, n = 300),followedbyDeep Learning(DL) approaches(29.1%, n = 144) (Fig. 4). Traditional ML methods (e.g., Random Forests and Gradient Boosting) are predominantly applied to risk forecasting and pattern recognition, while DL approaches (DNNs, CNNs, LSTMs are more commonly deployed for spatiotemporal modelling of complex urban systems. This aligns with their distinct technical strengths: ML offers interpretability for decision-making, while DL handles computationally intensive, high-resolution tasks like realtime flood simulation or metre-level vulnerability mapping<sup>55</sup> . 

AI demonstrates extensive applicability and dominant utility in physical hazard prediction and environmental optimisation (Fig. 4a), domains characterised by structured data availability. The prediction and assessment cluster (40.2%) is heavily concentrated on flooding and air pollution, where DLarchitecturesexcelatcapturingnon-lineardynamicprocesses.Similarly, in urban ecosystem and infrastructure research (combined ~42%, Fig. 4a), AI bridges analytical scales. As highlighted by the standardised ratios (Fig. 4c), there is a disproportionate methodological preference in these physical domains, from classifying individual street-level greenery using computer vision to monitoring city-wide heat island dynamics via remote sensing. For instance, the integration of Google Street View imagery with CNN architectures exemplifies a methodological leap, enabling the generation of finegrained vulnerability maps that traditional top-down indicators cannot achieve<sup>56</sup> . 

In stark contrast to the rapid advancement in physical domains, a critical structural imbalance persists in the social domain of resilience. Governance (3.8%, n = 19) and health/well-being (5.8%, n = 29) domains remain largely peripheral to the AI revolution (Fig. 3 vs. 4). This structural deficit is statistically significant, with governance themes being underrepresented in the AI subset relative to the expected distribution in the overall UCR baseline (χ² = 15.4, p < 0.001, Cohen’s h = 0.21). A comparable pattern is observed for health and well-being (χ² = 20.8, p < 0.001, Cohen’s h = 0.24) (Supplementary Table 13). This disparity is not merely a reflection of research interest but exposes a data availability trap: current AI models thriveonthestructured,quantitativedatasetstypicalofphysicalsciencesbut struggle with the unstructured, qualitative nuances of social governance. Existing applications in these marginalised domains are limited mostly to NLP for policy analysis (n = 11), highlighting a significant lag in developing AI paradigms capable of decoding the complex social-institutional dimensions of resilience. 

Furthermore, our longitudinal analysis reveals that this domain imbalance is not static (Supplementary Fig. 5). Tracking the proportional evolution of key topics demonstrates a clear structural shift toward diversification. In the early phases (pre-2016), AI integration exhibited severe 

npj Climate Action 

Article in Press 

Article 

https://doi.org/10.1038/s44168-026-00431-w 



Fig. 4 | Distribution of AI methods across the UCR research cluster. a Publication distribution across six primary research clusters. b Overall publication volume for each of the four AI categories across all 495 publications. c Standardised representation of AI methods across specific sub-domains. The standardised ratio is calculated as the number of publications in each sub-domain divided by the mean 

number of publications for the corresponding AI category and is displayed on a log2 scale. A ratio of 1 represents the category-specific average; values above 1 indicate above-average representation, whereas values below 1 indicate below-average representation. Error bars represent 95% confidence intervals. 

domain imbalance, heavily concentrated in physical systems such as infrastructure. Recently, this dominance has yielded to fluctuating ecosystemapplicationsandsteadilygrowinginterestinenergy.Thisdiversification is further evidenced by a parallel rise in social domains. Research in health/ well-being has experienced a pronounced surge since 2020, a trend likely catalysed by the heightened global focus on public health (COVID-19 pandemic). Concurrently, AI adoption in governance has accelerated. This trend has unfolded against the backdrop of the rapid advancements and broader accessibility of LLMs, providing a compelling context for this growth without assuming direct causality. 

Systematic characterisation of representative cases further elucidates this functional difference (see examples in Table 1). AI-based methods have 

increasingly enabled more dynamic and predictive analyses, particularly in scenarios requiring real-time processing of heterogeneous data streams (satellite images, sensor time series, social media text)<sup>21</sup> . This computational capacity for integrating diverse data sources can support adaptive management frameworks, in which urban resilience strategies are iteratively adjusted in response to evolving climate conditions and urban dynamics<sup>57</sup> . Yetthispotentialforadaptivemanagementappearstoremainunderutilised. The current landscape indicates that AI applications remain more concentrated on optimising physical urban systems and have yet to mature into tools for empowering social governance. Bridging this gap requires not just more data, but a methodological pivot towards hybrid AI approaches that 

npj Climate Action 

Article in Press 

Article 

https://doi.org/10.1038/s44168-026-00431-w 

|AI functional role<br>Representative study<br>Improve prediction performance through multi-factor<br>integration and spatial risk classification<br>Rafiei-Sardooi et al.(2021)96|Spatial optimisation of nature-based solution layout<br>under multi-objective constraints<br>Kraemer and Kabisch (2022)97|Identify non-linear relationships; Feature importance<br>ranking<br>Lu et al. (2023)98|significantly speed up simulations; Incorporate<br>comprehensive variables<br>Liu et al. (2021)99|Substantially reduce computational time; Improve<br>prediction accuracy<br>Nearing et al.(2024)70|Capture the spatiotemporal dependencies of the urban<br>road network<br>Wang et al. (2020)100|Overcoming data scarcity in grid management via<br>transfer learning domains<br>Wang, Majumdar and Rajagopal<br>(2023)88|Real-time extraction of evolving public needs from<br>social media<br>Zhao et al. (2024)101<br>Automated retrieval and classification of climate<br>policies; Policy gap identification<br>Ma et al. (2023)102||
|---|---|---|---|---|---|---|---|---|
|Potential AI methods<br>Traditional ML: RF, SVM,<br>XGBoost|Traditional ML: LR,<br>RF, SVM|Traditional ML: RF, GBDT|Traditional ML: RF, SVM|Deep learning: ANN,<br>CNN, LSTM|Deep learning:<br>GNN, DCRNN|Deep learning: CNN|NLP: LDA, LIWC<br>NLP: LDA, BERT|ological implementation.|
|The limitations of traditional approaches<br>Conventional hydrological and hydraulic methods are not appropriate for<br>providing hazard maps and risk assessments in urban areas|Remote sensing-based approaches are inadequate for neighbourhood-scale<br>assessments.|Non-linear relationships unclear; Coarse thermal resolution; Insufficient 3D<br>form integration|High computational complexity; limited influencing variables; Lack of long-<br>term energy forecasting capability|Physics-based models are computationally intensive with extended<br>prediction time; Limited real-time forecasting capability|Cannot capture realistic behavioural responses; Use only static metrics;<br>Limited dynamic traffic modelling|Grid topology data is proprietary/incomplete; Cannot optimise across<br>multiple objectives|Disaster impact and resident needs assessed using static indicators over<br>fixed time spans<br>The large volume and broad scope of policies prevent real-time updates of<br>policy understanding; Lack of unified policy classification standards.|re selected from the analysed dataset based on citation impact and the clarity of their method|
|Application Domain<br>Risk assessment|Green infrastructure|Urban heat island|Energy prediction|Prediction model|Road network|Energy allocation|Risk perception<br>Policy framework|Representative studies we|



can integrate expert knowledge and social values into computational models. 

## Discussion 

The integration of advanced NLP techniques with systematic evidence mapping enables transparency and rigour in assessing the expanding UCR landscape<sup>58–61</sup> . Our findings demonstrate the growing but uneven integration of AI and reveal a critical geographical imbalance.The concentration of AI applications in economically developed countries with robust research infrastructures (Global North) contrasts sharply with the actual distribution of climate risk, which disproportionately affects rapidly urbanising regions in the Global South<sup>62,63</sup> . Based on this observation, we hypothesise that this disparity poses a risk that AI models trained predominantly on data from structured, developed urban systems may fail to generalise to the datascarce, informal contexts of developing regions<sup>64</sup> . Consequently, such imbalances may theoretically exacerbate global inequities in adaptation capacities. 

AI demonstrates transformative efficacy in addressing the prediction and assessment of physical hazards, driven by the availability of structured data<sup>24</sup> . Our analysis illustrates that AI integration primarily focuses on floods and heatwaves, which are the most significant threats to urban infrastructure<sup>65</sup> . In these domains, AI technologies have matured from traditional ML algorithms for risk identification to advanced DL architectures<sup>26,66,67</sup> . For instance, CNNs now enable high-resolution flood modelling through spatial pattern processing<sup>68,69</sup> , while Transformers excel at modelling temporal variations for spatiotemporal forecasting<sup>70–72</sup> . Recent developments in foundational models like Aurora<sup>73</sup> further demonstrate AI’s potential to integrate heterogeneous data streams for environmental forecasting across scales<sup>74</sup> . 

Technological progress appears to follow an uneven pathway across resilience domains, alongside differences in data characteristics. AI applicationsareparticularlyprominentinphysicaldomainscharacterisedbyrich and structured data sources, such as remote sensing for large-scale coverage<sup>75</sup> and street-level imagery for fine-grained identification<sup>76,77</sup> . In contrast, domains involving qualitative social feedback and policy processes remain underrepresented. Despite the capability of AI to process diverse data streams, applications in governance and health remain limited (<10%, see Fig. 4). This structural imbalance may partly reflect the greater compatibility of current AI methods with data-rich, engineering-oriented problems, potentially contributing to less attention being directed toward social equity and institutional adaptation, where evidence is often more heterogeneous and unstructured. 

BridgingthisgaprequiresleveragingAItodecodesystemiccomplexity. While current applications largely focus on single hazards, the cascading effects of compound climate hazards amplify economic and health risks<sup>78,79</sup> . The emerging capability of LLMs to process unstructured policy documents and community feedback offers a pathway to integrate social dimensions into technical frameworks<sup>80–83</sup> . Furthermore, AI’s ability to fuse heterogeneous data streams (Table 1) positions it as a vital tool for moving from single-hazard prediction to holistic, multi-risk adaptive management. Despite these promising advancements, methodological challenges persist within the applied UCR literature. Specifically, issues regarding reproducibility, the inherent “black-box” nature of the deep learning architectures deployed for hazard forecasting<sup>84–86</sup> , and localised data scarcity continue to constrain the generalisability of these predictive models across different urban contexts<sup>87</sup> . 

We also acknowledge limitations in our review: our findings are constrained by our reliance on the WoS database, which may introduce linguistic, geographic, and content-coverage biases. In addition, because our classificationwasbasedonabstractsratherthanfulltexts,thisapproachmay miss content reported only in full texts. Consequently, the observed geographic patterns should be interpreted with caution, as they may partly reflect database coverage and metadata availability rather than actual differences in local research capacity. Finally, because part of the classification workflow relied on a closed-source LLM, exact reproducibility may be 

npj Climate Action 

Article in Press 

Article 

https://doi.org/10.1038/s44168-026-00431-w 

affected by model-version changes and platform updates. We mitigated this limitation by documenting the classification prompts and validation procedures, conducting manual checks, and using an open-source LLM for consistency checks on a subset of classifications. Despite these limitations, this search strategy aligns with standard systematic review protocols and adequately captures the macro-level trajectories of the field<sup>44,46</sup> . Furthermore, although our binary classification (AI and non-AI) reveals macrostructural imbalances, it inherently compresses the methodological spectrum of AI integration. Future research may consider transitioning beyond this binary framework to develop granular metrics capable of assessing the specific depth and typology of AI applications. 

We propose three strategic priorities to pivot from isolated technical approaches to integrated frameworks that jointly address physical, social, and governance dimensions of urban climate risk. First, improve AI access: developing transferable, data-efficient models (unsupervised domain adaptation and few-shot learning) is essential to bring predictive capabilities to the resource-constrained Global South<sup>88</sup> . Second, decode systemic complexity: move beyond single-hazard predictions, AI’s advanced feature extraction can better model the non-linear dynamics of compound and cascading events<sup>55,89</sup> . Third, reintegrate the social dimension: deploying multilingual and multimodal AI (e.g., LLM fine-tuning) captures localised socio-environmental interactions, integrating data- and model-driven insights into actionable policymaking and decision processes. In conclusion,our systematicmap helpsto shapethefuture research agenda forUCR. This will better align advanced AI capabilities with the urgent need for systemic climate adaptation in vulnerable cities worldwide. 

## Methods 

### Systematic retrieval and corpus construction 

We conducted a systematic literature search using the Web of Science (WoS) Core Collection (accessed in March 2025), selected for its comprehensive coverage of high-quality, peer-reviewed publications and standardised metadata structure. Our search strategy employed a three-tier keyword approach combining Boolean operators: resilience-related terms (resilience, adaptation, vulnerability), technological applications (modelling, assessment, and planning), and urban systems (transport, infrastructure, and health). Keywords within each subcomponent were combined using Boolean “OR” operators. We retrieved titles, abstracts, and metadata for all documents, but did not access full texts (Detailed keywords in Supplementary Table 14). 

Following PRISMA guidelines (Supplementary Fig. 6), our initial WoS search spanned 2005–2024 and was restricted to peer-reviewed journal articles published in English. The search period began in 2005, as our strategy revealed a natural absence of relevant literature before this year, with earlier studies largely fragmented under broader terms. To address overlappingWoSmetadataclassifications,weappliedpost-retrieval filtering to remove misclassified document types. To maintain consistent peerreview standards across diverse disciplines, we strictly excluded conference proceedings. Dissertations and theses were inherently excluded, as the WoS Core Collection does not index these materials<sup>90</sup> . Following data deduplication and the removal of records lacking complete abstracts or metadata, 12,498 publications were retained for analysis. 

### Categorising and identifying AI-relevant abstracts 

To systematically identify AI applications within UCR research, we developed anLLM-basedclassificationmethodusingtheGPT-4TurboAPI.This model was selected based on its demonstrated superior performance in text classification tasks compared to earlier versions, incorporating reinforcement learning techniques that enhance NLP capabilities<sup>91</sup> . We employed a structured prompt-engineering strategy incorporating task descriptions, classification criteria, annotated examples, and output specifications (see Prompt 1inSupplementaryNote 1).Drawingonpriordefinitionsof AIand its applications in sustainability research<sup>23,64,92,93</sup> , we define AI-integrated UCR research as studies that apply computational systems capable of prediction, decision-making, pattern recognition, or automated knowledge 

extraction to UCR problems. The inclusion criteria covered a broad spectrumof AI methodologies,includingML algorithms, DL architectures,NLP techniques, and AI tools specifically applied to UCR (Supplementary Table 15). Borderline cases, such as conventional statistical modelling or GIS modelling, were classified as AI-integrated only when the abstract explicitly indicated that these methods were implemented using AI/ML-based approaches. Notably, rather than a strict algorithmic division, this represents a task-oriented taxonomy: we maintain NLP as a distinct category to highlight textual analysis, separating it from the spatial and visual data processing predominantly captured in the DL cluster. In addition to AImethod classification, we used a dedicated LLM prompt to extract studyarealocations from abstracts. These locations were standardisedto countrylevel units to compare affiliation-based research production with studyarea-based research attention (see Prompt 2 in Supplementary Note 1). 

This classification process identified 572 AI-integrated publications from the general dataset, representing ~4.6% of the total corpus. To ensure contextualprecision,weconductedasecondarymanualverification.During this phase,we excluded articles that, despite containing AI-related methods, lacked specific empirical applications to urban subsystems. Following the removal of these false positives and non-empirical entries, a total of 495 publications were formed as a specialised subset for detailed analysis of AI integration patterns and methodological innovations in UCR research. 

### Extracting research topics from abstracts 

Forcomprehensivethematicanalysis,weemployedBERTopic,anadvanced topic modelling technique that leverages pre-trained Transformer architectures to capture semantic relationships more effectively than traditional bag-of-words methods like Latent Dirichlet Allocation<sup>94</sup> . Unlike bag-ofwords approaches, BERTopic can generate coherent, interpretable topics without manual annotation, making it particularly suitable for large-scale literature analysis<sup>47</sup> . 

We utilised the all-MiniLM-L6-v2 sentence-transformer model, optimised for semantic similarity tasks, with fine-tuning applied to the classification layer while preserving pre-trained weights (Supplementary Note 2). Finally, we applied the optimised BERTopic model to all abstracts, which generated 56distinctthematicclusters(SupplementaryTable10).Toenable structured analysis, we implemented a standardised, iterative manual coding process to map these clusters into two overarching analytical dimensions:hazardtypes(suchas flooding,heatwaves)andurbansystems(suchas infrastructure, governance, social systems). Recognising that algorithmic keywords can lack context, two independent experts classified each topic based on two features: the ten most distinctive terms based on c-TF-IDF (Supplementary Table 11), and the 10 exemplar abstracts with the highest assignment probabilities for that cluster. Crucially, we did not force topics into specific hazard categories. Topics addressing broad resilience or cascading threats were mapped to overarching domains such as Climate change or Disaster. Specific hazard labels were only applied when exemplar abstracts explicitly identified a physical threat as the primary driver. Discrepancies were resolved through discussion until full consensus was reached. 

### Validation of AI classification and extracted topics 

To ensure the robustness of our findings, we implemented multiple validation procedures for both the AI classification (GPT-4 Turbo) and the topicmodelling(BERTopic) (SupplementaryNote3).FortheGPT-4Turbo classification, we implemented a comprehensive validation procedure. First, to mitigate potential abstraction bias, we conducted a full-text accuracy assessment. Two independent coders manually reviewed a stratified random sample of 100 Open Access full texts (stratified by AI classification and topic domain). These ground-truth labels were cross-checked against our automated abstract-level outputs to evaluate potential rates of under- or over-detection. Subsequently, to ensure large-scale classification reliability, we validated the model using a manually annotated subset of 650 randomly selected abstracts. The manual annotation was conducted independently by two domain experts to ensure objectivity. Performance was assessed using 

npj Climate Action 

Article in Press 

Article 

https://doi.org/10.1038/s44168-026-00431-w 

precision, recall,F1-score, and Cohen’sKappa (κ) to quantify the agreement between the model and human judgment. Finally, to mitigate potential model-specific biases, we conducted a cross-validation study using three additional large language models (GPT-3.5-Turbo, DeepSeek-V3, and Gemini-2.5-Flash). Inter-model agreement was quantified using Fleiss’ Kappa (κ) to assess the consistency and robustness of the classification framework across different LLMs. 

For the BERTopic framework, we applied Bayesian hyperparameter optimisation to the UMAP<sup>48</sup> and HDBSCAN<sup>49</sup> algorithms to empirically determine the optimal configuration and minimise noise. To guarantee reproducibility across arbitrary seeds, the random state was strictly fixed (random_state = 42). Model convergence and clustering quality were evaluated using the Silhouette Score<sup>95</sup> , implemented via Python’s scikitlearn library. This metric quantifies both intra-cluster cohesion and intercluster separation, ranging from −1 to 1, with values >0.5 indicating welldefined cluster structures. Through iterative optimisation, the model achieved a maximum Silhouette Score of 0.66 (Supplementary Fig. 3). This optimal configuration naturally converged on 56 distinct clusters, confirming these represent significant thematic structures rather than noise, thereby eliminating the need for arbitrary manual cluster reduction. 

To quantitatively validate the semantic interpretability and distinctiveness of the BERTopic clusters, we evaluated topic coherence (Cv) and topic diversity (TD). Cv was calculated via the gensim library using normalised pointwise mutual information (NPMI) and cosine similarity to measure semantic interpretability<sup>95</sup> . Additionally, TD was calculated as the proportion of unique words among the top K terms across all topics to confirm cluster distinctiveness and prevent vocabulary redundancy. We further assessed the robustness of the BERTopic results through sensitivity analyses using alternative target topic numbers and an alternative sentencetransformer embedding model, with topic stability evaluated using Normalised Mutual Information (Supplementary Note 3.3 and Supplementary Table 5). 

## Data availability 

The original data used in this study were obtained through a query of the Web of Science Core Collection and are included in the Supplementary Information. The data underlying the results are available on https://github. com/MeiMeng11/Urban-climate-resilience_LLM. 

## Code availability 

The Python programming codes used for the generation of GPT-4 Turbo API and BERTopic outputs of this study are publicly available on https:// github.com/MeiMeng11/Urban-climate-resilience_LLM. 

Received: 12 February 2026; Accepted: 14 September 2026; 



## References 

1. Rentschler, J. et al. Global evidence of rapid urban growth in flood zones since 1985. Nature 622, 87–92 (2023). 

2. Moser, S., Meerow, S., Arnott, J. & Jack-Scott, E. The turbulent world of resilience: interpretations and themes for transdisciplinary dialogue. Clim. Change 153, 21–40 (2019). 

3. Chan, F. K. S. et al. Build in prevention and preparedness to improve climate resilience in coastal cities: lessons from China’s GBA. One Earth 4, 1356–1360 (2021). 

4. Wardekker, A. Contrasting the framing of urban climate resilience. Sustain. Cities Soc. 75, 103258 (2021). 

5. United Nations. Sendai framework for disaster risk reduction 20152030. https://www.undrr.org/publication/sendai-frameworkdisaster-risk-reduction-2015-2030 (2015). 

6. Spaans, M. & Waterhout, B. Building up resilience in cities worldwide – Rotterdam as participant in the 100 resilient cities programme. Cities 61, 109–116 (2017). 

7. Leichenko, R. Climate change and urban resilience. Curr. Opin. Environ. Sustain. 3, 164–168 (2011). 

8. Meerow, S., Newell, J. P. & Stults, M. Defining urban resilience: a review. Landsc. Urban Plan. 147, 38–49 (2016). 

9. Mehryar, S., Sasson, I. & Surminski, S. Supporting urban adaptation to climate change: what role can resilience measurement tools play? Urban Clim. 41, 101047 (2022). 

10. Chang, H. et al. Understanding urban flood resilience in the anthropocene: a social–ecological–technological systems (SETS) learning framework. Ann. Am. Assoc. Geogr. 111, 837–857 (2021). 

11. Coleman, N., Li, X., Comes, T. & Mostafavi, A. Weaving equity into infrastructure resilience research: a decadal review and future directions. npj Nat. Hazards 1, 25 (2024). 

12. Chan, F. K. S., Chen, W. Y., Gu, X., Peng, Y. & Sang, Y. Transformation towards resilient sponge cities in China. Nat. Rev. Earth Environ. 3, 99–101 (2021). 

13. Lu, X., Chan, F. K. S., Chan, H. K. & Chen, W.-Q. Mitigating flood impacts on road infrastructure and transportation by using multiple information sources. Resour. Conserv. Recycl. 206, 107607 (2024). 

14. Serdar, M. Z., Koç, M. & Al-Ghamdi, S. G. Urban transportation networks resilience: indicators, disturbances, and assessment methods. Sustain. Cities Soc. 76, 103452 (2022). 

15. Yabe, T., García Bulle Bueno, B., Frank, M. R., Pentland, A. & Moro, E. Behaviour-based dependency networks between places shape urban economic resilience. Nat. Hum. Behav. https://doi.org/10. 1038/s41562-024-02072-7 (2024). 

16. Yang, L. E., Weinelt, M., Unkel, I. & Petrie, C. A. Social resilience to changes in climate over the past 5000 years. Environ. Res. Lett. 19, 120201 (2024). 

17. Pitidis, V. & Coaffee, J. Catalysing governance transformations through urban resilience implementation: the case of Thessaloniki, Greece. Cities 107, 102934 (2020). 

18. Gounaridis, D., Waweru, W. & Newell, J. P. Triple exposure: the geographic correlation between flood risk, climate skepticism, and social vulnerability in the United States. Environ. Res. Lett. 19, 114084 (2024). 

19. Mester, B., Frieler, K., Korup, O., Desai, B. & Schewe, J. Socioeconomic predictors of vulnerability to flood-induced displacement. Nat. Commun. 16, 8296 (2025). 

20. Eyring, V. et al. Pushing the frontiers in climate modelling and analysis with machine learning. Nat. Clim. Chang. 14, 916–928 (2024). 

21. Yabe, T., Rao, P. S. C., Ukkusuri, S. V. & Cutter, S. L. Toward datadriven, dynamical complex systems approaches to disaster resilience. Proc. Natl. Acad. Sci. USA 119, e2111997119 (2022). 

22. Qu, D., Ma, Y. & Wang, Y. STR-GNN: stability-regularized graph neural networks for suppressing spurious temporal variations in dynamic community detection. Sci. Rep. 16, 25050 (2026). 

23. Camps-Valls, G. et al. Artificial intelligence for modeling and understanding extreme weather and climate events. Nat. Commun. 16, 1919 (2025). 

24. Reichstein, M. et al. Early warning of complex climate risk with integrated artificial intelligence. Nat. Commun. 16, 2564 (2025). 

25. Yarveysi, F., Alipour, A., Moftakhari, H., Jafarzadegan, K. & Moradkhani, H. Block-level vulnerability assessment reveals disproportionate impacts of natural hazards across the conterminous United States. Nat. Commun. 14, 4222 (2023). 

26. Qin, X. et al. Enhancing urban resilience through machine learningsupported flood risk assessment: integrating flood susceptibility with building function vulnerability. npj Urban Sustain. 5, 19 (2025). 

27. Huang, T., Zanocco, C., Wang, Z., Hwang, J. & Rajagopal, R. Built environment disparities are amplified during extreme weather recovery. Nature https://doi.org/10.1038/s41586-025-09804-3 (2025). 

npj Climate Action 

Article in Press 

Article 

https://doi.org/10.1038/s44168-026-00431-w 

28. Callaghan, M. et al. Machine learning map of climate policy literature reveals disparities between scientific attention, policy density, and emissions. npj Clim. Action 4, 7 (2025). 

29. Wu, L., Huang, Z., Zhang, X. & Wang, Y. Harmonizing existing climate change mitigation policy datasets with a hybrid machine learning approach. Sci. Data 11, 580 (2024). 

30. Wannewitz, M. et al. Progress and gaps in climate change adaptation in coastal cities across the globe. Nat Cities 1, 610–619 (2024). 

31. Prashar, N., Lakra, H. S., Kaur, H. & Shaw, R. Urban flood resilience: mapping knowledge, trends and structure through bibliometric analysis. Environ. Dev. Sustain. 26, 8235–8265 (2023). 

32. Han, H., Bai, X. & Dong, L. Global policy stocktake of urban climate resilience: a literature review. Resour. Conserv. Recycl. 212, 107923 (2025). 

33. Nik, V. M., Perera, A. T. D. & Chen, D. Towards climate resilient urban energy systems: a review. Natl. Sci. Rev. 8, nwaa134 (2021). 

34. Huntingford, C. et al. Machine learning and artificial intelligence to aid climate change research and preparedness. Environ. Res. Lett. 14, 124007 (2019). 

35. Zennaro, F. et al. Exploring machine learning potential for climate change risk assessment. Earth Sci. Rev. 220, 103752 (2021). 

36. Sætra, H. S. & Selinger, E. Technological remedies for social problems: defining and demarcating techno-fixes and technosolutionism. Sci. Eng. Ethics 30, 60 (2024). 

37. Couldry, N. & Mejias, U. A. Data colonialism: Rethinking big data’s relation to the contemporary subject. Telev. New Media 20, 336–349 (2019). 

38. McGovern, A. et al. Identifying and categorizing bias in AI/ML for Earth sciences. Bull. Am. Meteorol. Soc. 105, E567–E583 (2024). 

39. González, J. E. et al. Urban climate and resiliency: A synthesis report of state of the art and future research directions. Urban Clim. 38, 100858 (2021). 

40. Urquiza, A. et al. An integrated framework to streamline resilience in the context of urban climate risk assessment. Earths Future 9, e2020EF001508 (2021). 

41. Delgado-Chaves, F. M. et al. Transforming literature screening: The emerging role of large language models in systematic reviews. Proc. Natl. Acad. Sci. USA 122, e2411962122 (2025). 

42. Ofori-Boateng, R., Aceves-Martins, M., Wiratunga, N. & MorenoGarcia, C. F. Towards the automation of systematic reviews using natural language processing, machine learning, and deep learning: a comprehensive review. Artif. Intell. Rev. 57, 1–25 (2024). 

43. Callaghan, M. et al. Machine-learning-based evidence and attribution mapping of 100,000 climate impact studies. Nat. Clim. Chang. 11, 966–972 (2021). 

44. Chang, C. H. et al. Global evidence of human well-being and biodiversity impacts of natural climate solutions. Nat. Sustain. 8, 75–85 (2024). 

45. Hintz, M. J., Milojevic-Dupont, N., Creutzig, F., Repke, T. & Kaack, L. H. A systematic map of machine learning for urban climate change mitigation. Nat. Cities 2, 924–936 (2025). 

46. Lin, Z., Chen, A., Wang, X., Liu, Z. & Piao, S. Large language models reveal big disparities in current wildfire research. Commun. Earth Environ. 5, 168 (2024). 

47. Grootendorst, M. BERTopic: neural topic modeling with a classbased TF-IDF procedure. Preprint at arXiv:2203.05794 (2022). 

48. McInnes, L., Healy, J. & Melville, J. UMAP: uniform manifold approximation and projection for dimension reduction. arXiv:1802.03426 (2018). 

49. McInnes, L., Healy, J. & Astels, S. hdbscan: Hierarchical density based clustering. J. Open Source Softw. 2, 205 (2017). 

50. IPCC. Climate Change 2007: Synthesis Report. Contribution of Working Groups I, II and III to the Fourth Assessment Report of the 

- Intergovernmental Panel on Climate Change (eds Core Writing Team, Pachauri, R.K. & Reisinger, A.) (IPCC, 2007). 

- 51. IPCC. Climate Change 2014: Synthesis Report.Contribution of Working Groups I, II and III to the Fifth Assessment Report of the Intergovernmental Panel on Climate Change [Core Writing Team, R.K. Pachauri and L.A. Meyer (Eds.)]. (2014). 

- 52. IPCC. Climate Change 2023: Synthesis Report. Contribution of Working Groups I, II and III to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change (eds Core Writing Team, Lee, H. & Romero, J) (IPCC, 2023). 

- 53. United Nations Educational, Scientific and Cultural Organization. UNESCO Science Report 2021 (United Nations, 2021). 

- 54. McPhearson, T. et al. Global synthesis and regional insights for mainstreaming urban nature-based solutions. Proc. Natl. Acad. Sci. USA 122, e2315910121 (2025). 

- 55. Reichstein, M. et al. Deep learning and process understanding for data-driven Earth system science. Nature 566, 195–204 (2019). 

- 56. Xing, Z. et al. Flood vulnerability assessment of urban buildings based on integrating high-resolution remote sensing and street view images. Sustain. Cities Soc. 92, 104467 (2023). 

- 57. Feng, K., Lin, N., Kopp, R. E., Xian, S. & Oppenheimer, M. Reinforcement learning-based adaptive strategies for climate change adaptation: an application for coastal flood risk management. Proc. Natl. Acad. Sci. USA 122, e2402826122 (2025). 

- 58. Berrang-Ford, L. et al. Systematic mapping of global research on climate and health: a machine learning review. Lancet Planet. Health 5, e514–e525 (2021). 

- 59. An,C., Wang,J. & Zhou,C. The evolutionandcurrent landscapeof AI in geographical research: a large-scale systematic review. Geogr. Sustain. 7, 100392 (2025). 

60. Dagdelen, J. et al. Structured information extraction from scientific text with large language models. Nat. Commun. 15, 1418 (2024). 

61. Gao, J. & Wang, D. Quantifying the use and potential benefits of artificial intelligence in scientific research. Nat. Hum. Behav. 8, 2281–2292 (2024). 

62. Li, D. et al. Disproportionate flood exposure for slum populations of the Global South. Nat. Cities 2, 626–638 (2025). 

63. Zhang, Q. et al. Global South shows higher urban flood exposures than the Global North under current and future scenarios. Commun. Earth Environ. 6, 594 (2025). 

64. Vinuesa, R. et al. The role of artificial intelligence in achieving the sustainable development goals. Nat. Commun. 11, 233 (2020). 

65. Forzieri, G. et al. Escalating impacts of climate extremes on critical infrastructures in Europe. Glob. Environ. Change 48, 97–107 (2018). 

66. Guan, X., Yu, F., Xu, H., Li, C. & Guan, Y. Flood risk assessment of urban metro system using random forest algorithm and triangular fuzzy number based analytical hierarchy process approach. Sustain. Cities Soc. 109, 105546 (2024). 

67. Ha, J. & Kang, J. E. Assessment of flood-risk areas using random forest techniques: Busan metropolitan city. Nat. Hazards 111, 2407–2429 (2022). 

68. El baida, M., Boushaba, F., Chourak, M. & Hosni, M. Real-time urban flood depth mapping: convolutional neural networks for pluvial and fluvial flood emulation. Water Resour. Manag. 38, 4763–4782 (2024). 

69. Wang, Z., Lyu, H., Fu, G. & Zhang, C. Time-guided convolutional neural networks for spatiotemporal urban flood modelling. J. Hydrol. 645, 132250 (2024). 

70. Nearing, G. et al. Global prediction of extreme floods in ungauged watersheds. Nature 627, 559–563 (2024). 

71. Tarasova, L., Ahrens, B., Hoff, A. & Lall, U. The value of large-scale climatic indices for monthly forecasting severity of widespread flooding using dilated convolutional neural networks. Earths Future 12, e2023EF003680 (2024). 

npj Climate Action 

Article in Press 

Article 

https://doi.org/10.1038/s44168-026-00431-w 

72. Zhou, Y., Wu, W., Nathan, R. & Wang, Q. J. A rapid flood inundation modelling framework using deep learning with spatial reduction and reconstruction. Environ. Model. Softw. 143, 105112 (2021). 

73. Bodnar, C. et al. A foundation model for the Earth system. Nature 641, 1180–1187 (2025). 

74. Eyring, V., Gentine, P., Camps-Valls, G., Lawrence, D. M. & Reichstein, M. AI-empowered next-generation multiscale climate modelling for mitigation and adaptation. Nat. Geosci. 17, 963–971 (2024). 

75. Tellman, B. et al. Satellite imaging reveals increased proportion of population exposed to floods. Nature 596, 80–86 (2021). 

76. Zhai, W. & Peng, Z.-R. Damage assessment using Google Street View: evidence from Hurricane Michael in Mexico Beach, Florida. Appl. Geogr. 123, 102252 (2020). 

77. Ning, H. et al. Exploring the vertical dimension of street view image based on deep learning: a case study on lowest floor elevation estimation. Geogr. Inf. Syst. 36, 1317–1342 (2022). 

78. Chakraborty, T., Hsu, A., Manya, D. & Sheriff, G. Disproportionately higher exposure to urban heat in lower-income neighborhoods: a multi-city perspective. Environ. Res. Lett. 14, 105003 (2019). 

79. Buzan, J. R. & Huber, M. Moist heat stress on a hotter earth. Annu. Rev. Earth Planet. Sci. 48, 623–655 (2020). 

80. Feuerriegel, S. et al. Using natural language processing to analyse text data in behavioural science. Nat. Rev. Psychol. https://doi.org/ 10.1038/s44159-024-00392-z (2025). 

81. Li, B. et al. Measuring China’s policy stringency on climate change for 1954-2022. Sci. Data 12, 188 (2025). 

82. Hsu, A. & Rauber, R. Diverse climate actors show limited coordination in a large-scale text analysis of strategy documents. Commun. Earth Environ. 2, 30 (2021). 

83. Ma, Y., Qu, D. & Wang, Y. Tracking evolving communities in fake news cascades using temporal graphs. Sci. Rep. 16, 4952 (2026). 

84. Liu, Z., Felton, T. & Mostafavi, A. Interpretable machine learning for predicting urban flash flood hotspots using intertwined land and built-environment features. Comput. Environ. Urban Syst. 110, 102096 (2024). 

85. Liu, P., Zhang, Y. & Biljecki, F. Explainable spatially explicit geospatial artificial intelligence in urban analytics. Environ. Plan. B Urban Anal. City Sci. 51, 1104–1123 (2024). 

86. Dramsch, J. S. et al. Explainability can foster trust in artificial intelligence in geoscience. Nat. Geosci. 18, 112–114 (2025). 

87. Materia, S. et al. Artificial intelligence for climate prediction of extremes: state of the art, challenges, and future perspectives. Wiley Interdiscip. Rev. Clim. Change https://doi.org/10.1002/wcc.914 (2024). 

88. Wang, Z., Majumdar, A. & Rajagopal, R. Geospatial mapping of distribution grid with machine learning and publicly-accessible multi-modal data. Nat. Commun. 14, 5006 (2023). 

89. Zscheischler, J. et al. A typology of compound weather and climate events. Nat. Rev. Earth Environ. 1, 333–347 (2020). 

90. Martín-Martín, A., Orduna-Malea, E., Thelwall, M. & Delgado LópezCózar, E. Google Scholar, Web of Science, and Scopus: a systematic comparison of citations in 252 subject categories. J. Informetr. 12, 1160–1177 (2018). 

91. Rathje, S. et al. GPT is an effective tool for multilingual psychological text analysis. Proc. Natl. Acad. Sci. USA 121, e2308950121 (2024). 

92. LeCun, Y., Bengio, Y. & Hinton, G. Deep learning. Nature 521, 436–444 (2015). 

93. Jordan, M. I. & Mitchell, T. M. Machine learning: trends, perspectives, and prospects. Science 349, 255–260 (2015). 

96. Rafiei-Sardooi, E., Azareh, A., Choubin, B., Mosavi, A. H. & Clague, J. J. Evaluating urban flood risk using hybrid method of TOPSIS and machine learning. Int. J. Disaster Risk Reduct. 66, 102614 (2021). 

97. Kraemer, R. & Kabisch, N. Parks under stress: Air temperature regulation of urban green spaces under conditions of drought and summer heat. Front. Environ. Sci. 10, (2022). 

98. Lu, L., Fu, P., Dewan, A. & Li, Q. Contrasting determinants of land surface temperature in three megacities: implications to cool tropical metropolitan regions. Sustain. Cities Soc. 92, 104505 (2023). 

99. Liu, S. et al. Predicting long-term monthly electricity demand under future climatic and socioeconomic changes using data-driven methods: a case study of Hong Kong. Sustain. Cities Soc. 70, 102936 (2021). 

100. Wang, H.-W. et al. Evaluation and prediction of transportation resilience under extreme weather events: a diffusion graph convolutional approach. Transp. Res. Part C Emerg. Technol. 115, 102619 (2020). 

101. Zhao, Z., Zhou, X., Zheng, Y., Meng, T. & Fang, D. Enhancing infrastructural dynamic responses to critical residents’ needs for urban resilience through machine learning and hypernetwork analysis. Sustain. Cities Soc. 106, 105366 (2024). 

102. Ma, Y.-R. et al. A news-based climate policy uncertainty index for China. Sci. Data 10, 881 (2023). 

## Acknowledgements 

The authors would like to thank C. An for her assistance with abstract screening and coding. 

## Author contributions 

J.W. and F.K.S.C. conceived and designed the research, M.M., N.A.S.H., and J.W. performed the formal analysis, and M.M. drew the figures. M.M., N.A.S.H., J.W., and F.K.S.C. wrote the first version of the manuscript, with inputs and revisions from L.E.Y. 

## Funding 

This study was funded by the Strategic Priority Research Programme of the Chinese Academy of Sciences (Grant No. XDB0740100), the National NaturalScienceFoundationofChina(GrantsNo.W2432029and42571540), and the Ningbo Natural Science Foundation (Grants No. 2023J193 and 2022J173). The funders had no role in study design, data collection and analysis, decision to publish or preparation of the manuscript. 

## Competing interests 

The authors declare no competing interests. 

## Additional information 

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s44168-026-00431-w. 

Correspondence and requests for materials should be addressed to Jianghao Wang or Faith K. S. Chan. 

Reprints and permissions information is available at http://www.nature.com/reprints 

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

94. Blei, D. M. Latent dirichlet allocation. J. Mach. Learn. Res. 3, 993–1022 (2003). 

95. Röder, M., Both, A. & Hinneburg, A. Exploring the space of topic coherence measures. In Proc. Eighth ACM International Conference on Web Search and Data Mining 399–408 (ACM, 2015). 

npj Climate Action 

Article in Press 

Article 

https://doi.org/10.1038/s44168-026-00431-w 

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material isnot includedin thearticle's CreativeCommons licenceandyour intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/bync-nd/4.0/. 

This Article in Press is shared early to give you faster access to new research. It iscitable and carries a permanent DOI. The final edited version will replace it automatically. 

© The Author(s) 2026 

npj Climate Action 

Article in Press 
