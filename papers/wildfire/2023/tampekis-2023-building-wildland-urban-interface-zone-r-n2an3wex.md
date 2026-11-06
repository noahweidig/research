---
title: Building wildland–urban interface zone resilience through performance-based wildfire engineering. A holistic theoretical framework
authors:
- Tampekis, Stergios
- Sakellariou, Stavros
- Palaiologou, Palaiologos
- Arabatzis, Garyfallos
- Kantartzis, Apostolos
- Malesios, Chrisovalantis
- Stergiadou, Anastasia
- Fafalis, Dimitrios
- Tsiaras, Evangelos
year: '2023'
journal: Euro-Mediterranean Journal for Environmental Integration
doi: 10.1007/s41207-023-00385-z
tags:
- machine learning
- resilience
- risk management
- wildfire
zotero_key: N2AN3WEX
item_type: journalArticle
url: https://doi.org/10.1007/s41207-023-00385-z
source_url: 'unpaywall: https://link.springer.com/content/pdf/10.1007/s41207-023-00385-z.pdf'
fulltext_status: fulltext
synced: '2026-11-06'
---

# Building wildland–urban interface zone resilience through performance-based wildfire engineering. A holistic theoretical framework

## Abstract

Abstract In recent years, a worldwide expansion in the frequency of large, uncontrolled, and catastrophic wildfire events has occurred, creating drastic social, economic, and environmental damage, especially in wildland–urban interface (WUI) zones. This damage includes losses of life, infrastructure, and ecosystem services. The impacts of wildfires at the WUI derive from the complicated and multidimensional interconnected relationships present in the Anthropocene. To enforce resilience of the environment and human communities against wildfires, it is critical to comprehend the local social-ecological systems holistically. In this paper, we present a theoretical framework approach, built on performance-based wildfire engineering, that is envisioned to be a stepping stone towards WUI resilience. To attain this objective, performance benchmarking and design is disaggregated into explicit components of a rigorous mathematical framework. They are linked to a causal inference chain, providing an integrated picture and enabling decision analysis to identify the optimal management strategies based on quantitative parameters. The proposed framework is developed from the total probability theorem and divides the risk assessment into single parts, in particular (1) hazard (wildfire) analysis, (2) social-ecological impact characterization, (3) social-ecological interaction analysis, (4) social-ecological impact analysis, (5) damage analysis, and (6) loss analysis. Therefore, the proposed framework can be applied by emergency agencies directly to assess the performance of society and ecosystem recovery after a wildfire, making emergency management and resilience policy-making more effective.

## Full text

Euro-Mediterranean Journal for Environmental Integration (2023) 8:675–689 https://doi.org/10.1007/s41207-023-00385-z 

**ORIGINAL PAPER** 



# **Building wildland–urban interface zone resilience through performance‑based wildfire engineering. A holistic theoretical framework** 

**Stergios Tampekis**<sup>**1**</sup> **· Stavros Sakellariou**<sup>**2**</sup> **· Palaiologos Palaiologou**<sup>**1**</sup> **· Garyfallos Arabatzis**<sup>**3**</sup> **· Apostolos Kantartzis**<sup>**3**</sup> **· Chrisovalantis Malesios**<sup>**4**</sup> **· Anastasia Stergiadou**<sup>**5**</sup> **· Dimitrios Fafalis**<sup>**6**</sup> **· Evangelos Tsiaras**<sup>**7**</sup> 

Received: 22 February 2023 / Accepted: 25 May 2023 / Published online: 10 July 2023 © The Author(s) 2023 

#### **Abstract** 

In recent years, a worldwide expansion  in the frequency of large, uncontrolled, and catastrophic wildfire events has occurred, creating drastic social, economic, and environmental damage, especially in wildland–urban interface (WUI) zones. This damage includes losses of life, infrastructure, and ecosystem services. The impacts of wildfires at the WUI derive from the complicated and multidimensional interconnected relationships present in the Anthropocene. To enforce resilience of the environment and human communities against wildfires, it is critical to  comprehend the local social-ecological systems holistically. In this paper, we present a theoretical framework approach, built on performance-based wildfire engineering, that is envisioned to be a stepping stone towards WUI resilience. To attain this objective, performance benchmarking and design is disaggregated into explicit components of a rigorous mathematical framework. They are linked to a causal inference chain, providing an integrated picture and enabling decision analysis to identify the optimal management strategies based on quantitative parameters. The proposed framework is developed from the total probability theorem and divides the risk assessment into single parts, in particular (1) hazard (wildfire) analysis, (2) social-ecological impact characterization, (3) social-ecological interaction analysis, (4) social-ecological impact analysis, (5) damage analysis, and (6) loss analysis. Therefore, the proposed framework can be applied by emergency agencies directly to assess the performance of society and ecosystem recovery after a wildfire, making emergency management and resilience policy-making more effective. 

**Keywords** Machine learning · Resilience · Performance-based design · Wildfires · Risk management 

## **Introduction** 

Worldwide, wildfires have been an integral part of much of this planet’s evolution (Pausas and Keeley 2019; Fernadez Anez et al. 2021), but they are also considered one of 

the most dangerous “natural disasters” (Pausas et al. 2017; McLauchlan et al. 2020). In recent years, we have witnessed a dramatic increase in large wildfire events (Keeley et al. 2009; Tedim et al. 2018) worldwide, along with their adverse socioeconomic and ecological effects (Bowman et al. 2017). These 

##### Communicated by Mohamed Ksibi. 

- Stergios Tampekis stampeki@gmail.com 

- 1 Department of Forestry and Natural Environment Management, Agricultural University of Athens, 3 Dimokratias St, Karpenisi 36100, Greece 

- 2 Department of Environmental Sciences, University of Thessaly, Gaiopolis Campus, Larissa 41500, Greece 

- 3 Department of Forestry and Management of the Environment and Natural Resources, Democritus University of Thrace, 193 Pantazidou St, Orestiada 68200, Greece 

- 4 Department of Agricultural Economics and Rural Development, Agricultural University of Athens, 75 Iera Odos St, Athens 11855, Greece 

- 5 Department of Forestry and Natural Environment, Aristotle University of Thessaloniki, Thessaloniki 54124, Greece 

- 6 College of Engineering, Drexel University, 3141 Chestnut St, Philadelphia, PA 19104, USA 

- 7 Department of Energy Systems, University of Thessaly, Gaiopolis Campus, Ring-Road of Larissa, Trikala, GR 41500, Greece 

Vol.:(0123456789)1 3 

Euro-Mediterranean Journal for Environmental Integration (2023) 8:675–689 

676 

include losses of life, infrastructure, and ecosystem services (Wotton et al. 2017; Bowman et al. 2020; Turco et al. 2018; McWethy et al. 2019; Abatzoglou et al. 2021). 

Approximately 368,263.934 ha of forest and farmland burned down in less than 2 weeks in Greece during the worst wave of wildfires that took place in August 2021 (National & Kapodistrian University of Athens 2021). Furthermore, during the summer of 2018, in Eastern Attica (Mati and Rafina), Greece experienced the most catastrophic wildfire during the past 100 years, which burned more than 1431 ha of wildland–urban interface (WUI) zones, including approximately 2500 homes. Unfortunately, 104 people died according to the Hellenic Forest Service (2022). During the same period, the situation was also challenging elsewhere in Europe. In Portugal, during the wildfire in the Pedrógão Grande area in the summer of 2018, 66 people lost their lives, and the wildfire caused considerable household (approx. 485 houses) and ecosystem (approx. 2018 farmers wereaffected and 53,000 ha of land were burned) (Alberti 2018). In the summer of 2021, in the US, the Dixie Fire became the largest wildfire in the history of California, having destroyed more than 389,837 ha (Wikipedia Dixie Fire 2021). In Australia, in March 2020, fires burnt an estimated area of 19 million ha, including over 5900 buildings (including 2779 homes), and killed at least 445 people and millions of animals (Wikipedia 2020). 

It is known that WUI zones are where dynamic interactions and interlinkages between ontologies such as vegetation, wild fauna, and human activities take place (BarMassada et al. 2014). One of the most important problems that WUI zones face around the world are wildfire events (Radeloff et al. 2018), because these zones are where wildfire-related accidents and structures or human losses are established. Hence, it has been noticed that large fire prevention and firefighting costs are incurred at the WUI (Kramer et al. 2018; Miranda et al. 2020). WUI zones present a complex global problem considering the unprecedented rates of inorganic (climate change, landscape fragmentation, etc.), organic (animal species, biodiversity loss,etc.), and socioeconomic (human population growth, resource consumption, urbanization) changes that are occurring there. Frequency of wildfire-indiced alterations and wildfire disturbances in WUI zones are emerging due to the increasingly interlinked relations between human communities and fire-prone ecosystems (Radeloff et al. 2018). 

On the other hand, ‘social-ecological systems’ (SES) is an emerging concept which emphasizes that human and natural systems are intertwined in a complex, interconnected, and interdependent way (Berkes et al. 2000; Folke et al. 2011). Environmental risks arising from the interaction of human societies with their living environment are generated by SES (Kaikkonen et al. 2021). To evaluate and mitigate environmental risks, it is necessary to understand local systems that 

are affected by the interdependent factors that contribute to the likelihood and magnitude of adverse impacts. Additionally, there is growing knowledge that considers the intricate connections between the social and environmental domains as well as the emerging and frequently unexpected processes, characteristics, challenges, and opportunities that they might lead to (Preiser et al. 2018). These systemic analyses of SES rely on the characterization of a comprehensive structure defined as “a complex, adaptive system consisting of a biogeo-physical unit and its associated social actors and institutions” (Glaser et al. 2012). In recent years, SES research has developed strongly due to the growing interest in scientific studies of resilience. Previous works on resilience have tried to summarize and compare the existing theoretical frameworks for SES analysis (Cote and Nightingale 2012). 

The increasing number of evaluation methodologies for SES contain an extensive variety of effects that differ both spatially and temporally. This is a turning point in the design of a robust decision-making framework that addresses effective social-ecological resilience in the aftermath of wildfires while being aligned with ecological and socioeconomic realities. To increase the resilience of communities to wildfires, it is critical to understand the local social-ecological systems holistically. A comprehensive understanding of the interplays between the many components and their contribution to fire risk remains important (Aldersley et al. 2011; Rodrigues et al. 2016; De Rigo et al. 2017). 

Many different model types have been applied to explain human–nature relationships, varying from graphical mind maps to mathematical models (Zingraff-Hamed et al. 2018). Graphical presentations are an effective way to structure and explain how the environmental risks are generated in SESs (Kaikkonen et al. 2021). Such “visuals” often function as natural boundary objects, being parts of various social worlds and supporting the communication between actors (Van der Hoorn 2020). Causal diagrams can help to enhance the inclusivity of multiple viewpoints, improving inference and the common understanding of the conditional aspects of complex systems and management problems as well as the impact mechanisms of potential interventions (Carriger et al. 2018; Luoma et al. 2021). Such causal argumentation by drawing can be called, e.g., cognitive mapping or mental modeling (LaMere et al. 2020). The qualitative causal presentations provide a basis for constructing quantitative models to assess risks, make predictions, and analyze counterfactual scenarios. Examples of potential (semi)quantitative causal approaches include Bayesian networks, fuzzy cognitive maps, and system dynamics models (Dlamini 2011; Penman et al. 2020; Carriger et al. 2021). Wildfire-driven losses result from the complicated intertwined relationships between social and ecological ontologies (Balch et al. 2017; Syphard et al. 2017; Oliveira et al. 2021). The ability to live with wildfire (i.e., to be fire adapted) now underpins 

1 3 

Euro-Mediterranean Journal for Environmental Integration (2023) 8:675–689 

677 

wildfire policy globally (Brenkert-Smith et al. 2017; Schoennagel et al. 2017). At the same time, some researchers have highlighted the intertwined social-ecological dynamics, concentrating on pre-fire vulnerability (Moritz et al. 2014). 

Resilience strategies focus on strengthening a system’s capability to withstand or recover from a crisis and to adjust to changing conditions (Linkov et al. 2016; IRGC 2018; OECD 2019). Resilient systems are robust to disturbances and they adjust to shocks and/or changing conditions (Turner 2010; Falk et al. 2022). Systems that do not have the ability to adjust to disturbances and/or changing conditions are vulnerable. Therefore, vulnerability is the chance or possibility that a system will continue at the same level after its exposure to disruptions (Turner et al. 2003). By definition, ithe resilience, vulnerability, and robustness are the key factors when considering the sustainable development of complex systems (the Internet, trade networks, financial systems, ecosystems, etc.) (Walker and Salt 2012). 

Socio-ecological resilience refers to the ability of socioecological systems (SES) to withstand and recover from disturbances while maintaining their basic functions and structures. It is the capacity of these systems to adapt to changing conditions and to continue providing ecosystem services to human societies (Crawford 2001; Fair 2020). Resilience is a major characteristic of SESs, which are complex, interdependent systems that include both social and ecological components. SESs can be affected by a wide range of disturbances, including natural disasters, climate change, and human activities such as overfishing, deforestation, and pollution (Levin 1998; Falk et al. 2022). Building resilience into SESs requires a collaborative and interdisciplinary approach, which involves engaging a range of stakeholders, ranging from policy-makers to local communities, in efforts to manage and protect these systems (Staal et al. 2015; Suweis et al. 2015). The concept of socio-ecological resilience is increasingly important in the face of global environmental challenges such as climate change and biodiversity loss. By promoting resilience in SESs, we can help to ensure the sustainability and long-term viability of these systems and the essential ecosystem services they provide (Reggiani 2013; Wu 2013). 

The performance-based design (PBD) framework methodology was largely developed for use in nuclear engineering, but its use has since broadened to include performancebased earthquake engineering (PBEE). Recently, there has been growing knowledge of this design methodology in the following engineering sectors: (i) blast (Hamburger and Whittaker 2003), (ii) fire (Lamont and Rini 2008), (iii) tsunami (Riggs et al. 2008), and (iv) wind (Petrini et al. 2009; Griffis et al. 2013). Performance-based engineering (PBE) is a design approach that has been applied to make better seismic and hurricane risk decision-making through the use of benchmarking and design methods that are strongly based 

on scientific analysis and express alternative solutions in terms that enable stakeholders to make informed decisions (Cornell 2000; Cornell and Krawinkler 2000; Moehle and Deirlein 2004). PBE examines dissimilar design, modification, and/or preservation solutions through the probabilistic assessment of a series of decision variables (DVs), where the DVs symbolize dissimilar performance and safety purposes (Barbato et al. 2013; Pinelli and Barbato 2019). 

This proposal describes a holistic theoretical framework and robust methodology for performance-based wildfire engineering that improves the resilience of social-ecological systems in wildfire-prone areas. To achieve this goal, the performance evaluation and design procedure has been disaggregated into logical elements that can be examined and resolved separately in an accurate and logical way but, on the other hand, also linked to a causal inference chain, providing a holistic picture and enabling decision analysis to identify the optimal management strategies. Essential features of the process are the description, definition, and quantification of (1) hazard analysis, (2) social-ecological characterization, (3) social-ecological interaction analysis, (4) social-ecological analysis, (5) damage analysis, and (6) loss analysis. The proposed framework presents the dynamic wildfire risk through spatial probability density functions of disturbances to socialecological systems. These disturbances can include different decision variables, such as human (physical, social, economic, health) and environmental impacts, depending on the needs of the stakeholders and authorities. Also, the suggested approach consists of a computational framework to disseminate and integrate uncertainties in the wildfire different scenarios, taking under consideration the effects of wildfires on the WUI, damage, and loss analyses. The basic characteristics of this method are described, and the complex interactions that characterize wildfire social-ecological impacts as well as the need for an analytical process to include the perspectives of the range of stakeholders and authorities are discussed. 

## **Methodology synthesis** 

### **Intensity measures (hazard analysis)** 

The first assessment step in the process is the definition of hazard analysis based on the hazard intensity measure, which describes the energy released from the organic matter combustion process (Keeley 2009) and is often expressed as the fire size (i.e., the total area burned). In other words, the wildfire intensity measure (IM) is the definition of the wildfire magnitude through the probabilistic theorem (Johnston et al. 2017). 

Typically, the IM is reported as a mean annual probability of exceedance, p[IM], that depends on the location (O) and event characteristics (D) (Moehle and Deierlein 2004). 

1 3 

Euro-Mediterranean Journal for Environmental Integration (2023) 8:675–689 

678 

These characteristics might be expressed in terms of fire size or magnitude. Considering the timing, the wildfire’s initial speed and its duration are relevant and temporal characteristics that influence both human and ecological reactions (Sakellariou et al. 2017). Sometimes, the return period (in years) between fires (Westerling et al. 2006) also irrevocably influences the fuel composition and ecosystem services. In addition, the wildfire magnitude description can contain spatial parameters such as the fire perimeter. Also, the function of the rate of fire spread is influenced by spatial factors before and during the wildfire event (Sakellariou et al. 2022a). These aspects affect the overall spatial pattern for each wildfire’s impact. Furthermore, there is interplay between the reactions of human factors and fire characteristics that affects the wildfire’s intensity and the importance of impacts (Blanchi et al. 2014). Also, to define the IM, hazard analysis includes the definition of suitable wildfire intensity input measure records for answer history analyses (Sakellariou et al. 2020, 2022b). Recent studies on hazard analysis benefit from earth science, remote images processing technology, and machine learning. These contribute to improving the accuracy of conventional IM selection and to the investigation of other possible wildfire intensity measures that match with wildfire-induced damage. The abovedescribed possible measures may include, for instance, perimeter, total burned area, rate of spread, spotting distance, etc. This description of wildfire intensity measures includes temporal and spatial features. 

In the recommended approach, the IM is obtained using probabilistic wildfire hazard analyses, and is expressed as a mean annual probability of exceedance, p[IM], which is 

affected by the location characteristics (topography and spatial characteristics), local weather conditions, and event features such as the vegetation (fuel) and soil type. Remote image processing technology, wildfire simulation software, and machine learning algorithms (Table 1) can play a crucial role in defining the IM. In Fig. 1, we present a simulation of the 2018 Mati wildfire, where the behavior and spread of the fire every  15 min was output by Prometheus software. 

### **Environmental demand parameters and interaction analysis** 

The next step to the process is the definition of the environmental demand parameters (EDPs), which show the degree to which a site has been altered or changed by the wildfire. They are calculated by simulating  the rate of loss, i.e., the product of the fire intensity, vegetation susceptibility, and the residence time of the fire. The EDPs are related to Intensity measures that describe  the condition of the Earth’s biosphere. In other words, EDPs characterize the response in terms of the cumulative degree of impact to which a site has been altered or changed by wildfire. 

Typically, after a natural hazard has impacted social or environmental systems, the ontologies will describe the damage level qualitatively as either nonexisting, minor, moderate, or severe damage due to the catastrophe. To minimize the subjectiveness of the catastrophe evaluation, physical damage to the different elements of the social or environmental ontologies can be defined quantitatively by specifying ascending levels of damage or damage limits. All the environmental part-damage cases can then be linked 

**Table 1** Machine-learning algorithms for burned area prediction 

|S. No.|Authors|Machine-learning method(s) used to predict burned area|
|---|---|---|
|1|Cortez and Morais (2007)|(i) Decision trees (DT), (ii) random forest (RF), (iii) artificial neural networks (ANN),<br>and (iv) support vector machines (SVM)|
|2|Toujani et al. (2018)|Hidden Markov models (HMM)|
|3|Özbayoğlu and Bozer (2012)|(i) Multilayer perceptron (MLP), (ii) radial basis function networks (RBFN), and (iii)<br>support vector machines (SVM)|
|4|Zwirglmaier et al. (2013)|Bayesian networks (BNs)|
|5|Shidik and Mustofa (2014)<br>fi|Fuzzy C-means and back-propagation ANN<br>i|
|6|Coffield et al. (2019)|Classification and regression tree (CART), RF, ANN, k nearest neighbor (KNN)|
|14|fi<br>Fairman et al. (2017)|i<br>Random forest (RF)|
|15|Cardil et al. (2019)|Boosted regression trees (BRT)<br>i|
|16|Debouk et al. (2013)|Artificial neural networks (ANN)|
|17|Barrett et al. (2011)|i<br>Random forest (RF)|
|18|Cai et al. (2013)|Boosted regression trees (BRT)|
|19|Hermosilla et al. (2015)|Random forest (RF)|
|20|Jung et al. (2013)|Genetic algorithms (GA) and random forest (RF)|
|21|Poon and Kinoshita (2018)|Support vector machines (SVM)|
|22|Hradsky et al. (2017)|Non-parametric BNs|



1 3 

Euro-Mediterranean Journal for Environmental Integration (2023) 8:675–689 

679 



**Fig. 1** Results of the Mati–Rafina wildfire perimeter simulation, where the results for 15 min intervals were obtained. The simulation was performed with Prometheus software 

**Fig. 2** Ecosystem fragility curves, Eastern Attica, Penteli, Mati, and Rafina 



to give the comprehensive environmental damage rate for a specific spatial extent (e.g., a town). The vulnerability model results are usually presented in two different patterns: (1) as vulnerability curves, which specify the damage intensity 

as a function of the hazard intensity, and (2) as fragility curves, which show the probability of exceeding a specified damage rate as a function of the hazard intensity (Pita et al. 2013, 2014). 

1 3 

Euro-Mediterranean Journal for Environmental Integration (2023) 8:675–689 

680 

Fragility curves are an alternative way to represent the vulnerability of an ecosystem. Such a curve presents the probability of exceeding a certain threshold of damage (the ordinate) for a given wildfire intensity (the abscissa) (Fig. 2). Fragility curves are graphical representations of the relationship between the intensity of a hazard and the probability of damage or failure of a structure. These curves are widely used in engineering to assess the vulnerability of buildings, bridges, and other infrastructure to natural or man-made hazards such as earthquakes, hurricanes, floods, and explosions (Cavallieri et al. 2020). Analytical fragility curves are based on mathematical models that describe the behavior of structures under different levels of hazard intensity. These models typically take into account factors such as the geometry, material properties, and boundary conditions of the structure as well as the characteristics of the hazard itself. Analytical fragility curves can be useful for predicting the performance of structures that are similar to those used in the model, but may not be accurate for structures with significantly different properties or behaviors (Forcellini and Alzabeebee 2022; Ko and Yang 2019). Empirical fragility curves, on the other hand, are based on the statistical analysis of observed damage or failure data from past events. These curves can provide more accurate estimates of the vulnerability of specific types of structures to specific hazards, but may be less useful for predicting the performance of structures that have not been tested in similar conditions (Ko and Yang 2019). Thereby, the novel ecosystem fragility curves will be very semantic for social-ecological resilience benchmarking. Cross-validated predictive models will be developed that are capable of estimating the ecosystem fragility index based on various damage features which depend on the wildfire magnitude, fire severity, and burn severity. 

Fragility curves are mathematical functions that express the probability that a system will reach a specific performance level or damage state given a certain hazard intensity. The specific form of the equation may vary depending on the type of hazard, the performance levels of interest, and the data available for analysis. In other words, the degree to which a system has been exposed to a hazard and can be damaged is commonly expressed through the damage functions that describe the interaction of the severity of the hazard with the level of the expected damage. The most common types of damage functions used in quantitative risk analysis and reliability analysis are fragility and vulnerability functions (Moschonas et al. 2009; Argyroudis et al. 2018). 

Fragility functions express the physical damage and give the probability that a system exceeds some undesirable limit states; for example, the serviceability for a given level of environmental excitation such as force, deformation, 

or other forms of loading to which the system is exposed to (Argyroudis et al. 2019; Kappes et al. 2012; Shinozuka et al. 2000) (Fig. 2). According to the type of system and the hazard that the system is exposed to, the impact of stress variable damage is frequently correlated with an Engineering Demand Parameter (EDP) (Argyroudis and Pitilakis 2012; Porter 2015). The lognormal distribution is a commonly used probability distribution for developing fragility curves, particularly for continuous performance levels. Fragility curves based on the lognormal distribution can be used to model the probability of reaching a specific damage state or performance level as a function of a hazard intensity measure. The fragility functions are usually described by a lognormal probability distribution (Carballo and Cornell 2000; Baker 2008): 



<!-- Start of picture text -->
P (Damage Level  i ) = Φ(ln (Intensity) − 휇i  ∕ 휎i ), (1)<br><!-- End of picture text -->

where: 

- _P_ (Damage Level _i_ ) is the probability of reaching a specific damage level (no damage, medium damage, or major damage). ‘Intensity’ is the intensity measure of the hazard (wildfire, earthquake, tornado or hurricane wind speed, etc.). Φ() is the cumulative distribution function (CDF) of the standard normal distribution. ln() is the natural logarithm. _μi_ and _σi_ are parameters that determine the location and scale of the lognormal distribution for the specific damage level _i_ . 

In this equation, the logarithm of the hazard intensity is used as the input to the lognormal distribution, which allows for the modeling of a wide range of intensity values while preserving the positive skewness often observed in real-world engineering data. The parameters _μi_ and _σi_ can be estimated from the available data, such as historical damage data, field testing, or numerical simulations, using statistical methods such as maximum likelihood estimation or Bayesian estimation. It's important to note that the specific values of _μi_ and _σi_ may vary depending on the type of system being analyzed, the hazard being considered, and the data available for analysis. The choice of the lognormal distribution as the model for fragility curves should be justified based on the characteristics of the data and the system being analyzed, and the resulting fragility curves should be validated using appropriate data and engineering judgment. The lognormal distribution is commonly used to model the variability of the IM and its relationship with the probability of exceeding a certain damage state. Once the fragility curve parameters are estimated, the curve can be plotted and used for wildfire risk assessment and decision-making (Baker and Cornel 2006). 

1 3 

Euro-Mediterranean Journal for Environmental Integration (2023) 8:675–689 

681 

Consequently, by providing as input the IM (fire size), the following step is to perform simulations to estimate the EDPs. For the suggested approach, we developed a dynamic analysis framework, which emphasizes the systematic process for identifying the conditional probability, p(EDP|IM), which can then be integrated with p[IM] to estimate the mean annual probabilities of exceeding the EDPs. Relationships between EDPs and the IM have been typically evaluated based on empirical simulations (based on the lognormal distribution), which have been supported by performance-based design research based on simulation and computational algorithms to assess the performance of social-ecological systems. In this approach, a numerical simulation is carried out in which an area is subjected to a wildfire with a prespecified IM amplitude; the responses of the EDPs are then calculated. This process is repeated for a set of data records for input wildfire intensity measures, which include features that are in agreement with the site conditions, and result in a set of relationships between the IM and EDPs. Fragility curves can be introduced in order to present the results from the previous process. One can estimate relevant statistical relations between the IM and EDPs, and determine the probability that the EDPs will exceed a series of given IM values. Having specified the fire hazard analysis that sets up the probabilities of exceeding the IM, one can combine them to acquire the hazard relationship for EDPs, which shapes the mean annual probability of exceeding EDPs. 

Therefore, the mean annualized probability of exceeding EDPs is then computed by integrating the fire hazard curve over the developed fragility curves for specific areas of interest (Pita et al. 2013). The fragility methodology summarized here has the potential to provide effective strategies for improving social-ecological safety and performance and for mitigating social and economic losses from competing natural hazards. 

### **Social‑ecological damage analysis (damage measures)** 

The next step in the process is to perform social-ecological damage analysis, which correlates the EDPs with damage measures (DMs). The DMs represent the quantification of damage to WUI components. This quantification must be relevant and detailed to enable the subsequent quantification of the necessary repairs, function disturbance, and safety hazards. 

The DMs describe the damage caused to the biosphere and human society (e.g., the visible ecological impact of a wildfire on soil properties, the hydrological cycle, carbon storage,  CO<sup>2</sup> emissions, vegetation, landscape fragmentation, wild fauna, land cover, human casualties, mental 

health, trauma, outmigration, tax revenue, homes, infrastructure, roads, etc.). 

The suggested framework evolves the conditional damage probability relations, p(DM|EDP), for a number of characteristic components. As a consequence, these conditional probability correlations, p(DM|EDP), can be joined with the EDP probability, p(EDP), resulting in the mean annual probability of exceedance of the DM, i.e., p(DM). 

Wildfire consequences stem from the interaction of event (wildfire) characteristics and human reactions (Ellingwood et al. 1993; Brookshire et al. 1997), which can be introduced as direct damage (e.g., loss of houses, habitat loss, human deaths and injuries, decreased water quality) or indirect damage (e.g., subsequent negative health effects, deteriorating ecosystem services), and the spatial aspect of the impact. Indirect losses refer to the negative impacts that are not immediately visible or obvious but can have significant consequences for community resilience (Adey et al. 2004). These losses can affect a community's ability to bounce back after a crisis or disaster. Examples of indirect losses of community resilience include a loss of social cohesion, economic losses, and psychological impacts (Forcellini 2019). Overall, indirect losses can have significant impacts on a community's resilience, making it important to consider these factors when planning for and responding to disasters. Moreover, wildfires sometimes trigger secondary disaster events like water floods, debris flows, and landslides, which can trigger additional property losses (De Graff 2014; Buckland et al. 2019). Also, raised exposure to wildfire smoke can cause respiratory problems such as chronic obstructive pulmonary disease or asthma (Rappold et al. 2017; Thie and Tart 2018). These indirect types of damage make the community’s recovery more complicated. 

In the meantime, wildfire impacts on vegetation and its reaction to those impacts usually cause the post-fire ecological outcome with the biggest ecological footprint. Social and ecological effects are also interlinked and intertwined. As a consequence, landscape vegetation recovery is influenced by natural impacts (e.g., the post-fire response of plant species) and human impacts (e.g., restoration programs, fuel and vegetation management in the home ignition zone, and land cover changes) (Carroll et al. 2011; Syphard et al. 2007). Subsequent vegetation recovery also causes emotional and psychological disorders in human communities (Kooistra et al 2018). Wildfire events that may negatively influence human communities may have positive effects on ecosystems. In some ecosystems, the damage to local vegetation that follows a fire facilitates the spatial invasion of nonnative plants (primarily grasses), which can be more successful than native species (Keeley et al. 2005). These nonnative plants can negatively influence an ecosystem. 

Furthermore, wildfires cause large expenses due to the firefighting and fire prevention efforts, post-fire landscape 

1 3 

Euro-Mediterranean Journal for Environmental Integration (2023) 8:675–689 

682 

rehabilitation, restoration of affected houses and infrastructure, and refunds provided (Steelman and Burke 2007). In Canada, researchers have developed a framework for the effects of wildfires on natural assets through expert elicitation (McFayden et al. 2019). Additionally, a spatial framework for fire effects that presents both fire-related benefits and losses quantified in terms of value changes has been developed (Scott et al. 2013). There are several epistemic papers that evaluate wildfire effects, taking under consideration specific challenges, shortcomings, temporal and spatial scales, time, and financial requirements (Palaiologou et al. 2020). During the first post-fire year, the initial recovery concentrates on providing immediately required social needs and stopping any further ecological damage. In human communities that are impacted by wildfires, providing mass care, building temporary houses, and infrastructure restoration dominate the attention of local emergency managers during the first weeks and months (Kates et al. 2006). Human reactions also interact with fire features and affect the fire intensity and degree of impacts. For instance, inhabitants’ decisions to stay and defend their properties or to evacuate depend on the wildfire’s speed of spread and expected duration, thus affecting the number of casualties (Blanchi et al. 2014). 

Summarizing, taking into consideration the local vulnerability features, wildfire exposure patterns shape the degree of wildfire effects and set the procedure for post-wildfire recovery in social and ecological systems (Jain et al. 2020). In this paper, we recommend an approach that evaluates the conditional damage probability relationships, p(DM|EDP), for a number of common and characteristic components, based on examination data, post-fire inspection reports, and tests of a few selected elements. In order to make this process more effective within the probabilistic theorem of the suggested approach that includes DMs, it can be described in terms of fragility relations. Fragility correlations for ecosystem services identify the probability of reaching a given damage status as a function of diminishing impact on ecosystem services. 

### **Decision variables (DV) (loss analysis)** 

Finally, having presented the detailed probabilistic description of damage  above, the procedure comes to a climax with the calculations of the decision variables, which quantify the damage. The damage is then considered it in risk management decisions. Due to the decision-makers’ needs, the decision variables are quantified and presented as repair costs, restoration times, and casualty rates. The calculation of the decision variables (loss analysis) is the final phase in the suggested approach that estimates the annual probability of exceedance of the DV, G(DV), where DV can be used as an indicator that describes the social risk. Wildfires are among 

the most expensive natural hazards that have negative financial impacts on social systems (Schumann III et al. 2020). In consequence, DVs can be expressed in financial terms. It is important to acknowledge that, from a loss-based design point of view, social damage corresponds to catastrophic losses (which are added to the direct losses) because wildfires can cause social disruption for extended time periods, including the need for residents to move homes (Li et al. 2012). 

The DV can be selected as the repair cost related to the wildfire caused damages. Also, they can be evaluated by taking into account the financial damage, construction and maintenance costs, (restoration costs), and the functionality loss (Bjarnadottir et al. 2011). In general, the restoration costs are determined based on highly uncertain risks and updated data from insurance companies. In addition, they are necessary to gain a probabilistic description of the repair costs. Furthermore, both ethical and technical problems increase when the DV is correlated to the loss of human life and/or to a life quality index when social systems are exposed to a wildfire. As a consequence, more research is needed to determine the specifications that are related to the above-described aspects when estimating the losses associated with social-ecological system destruction due to the wildfires. Additionally, an effective dialogue is needed among different stakeholders to determine a framework on when and how to investigate life quality indices and costs associated with life losses into wildfire risk assessment (Syphard et al. 2012, 2019). 

The suggested procedure starts expressing the relationships in probabilistic terms, between the performances considered social-ecologicalsystems and dissimilar intensities of the wildfire events. Based on a specific performance, the social-ecological risk may be conventionally measured as the probability of exceeding a relevant value of the corresponding DV. This probability can be expressed as a mean annual frequency, which can be evaluated by considering wildfire hazard analysis (i.e., the occurrence of wildfire events of a specific intensity and the features at the site), the estimated social-ecological response and damage, and the interplay between the damage level and the relevant DV. 

In a similar way to that suggested for the previous variables, the DVs are determined by joining the conditional probabilities of DV given the DM, p(DV|DM), with the mean annual probability of exceedance of the DM, p(DM), for the chosen wildfire hazard, and then adapting the results using suitable analytics to the required model. Addressing decisions using the suggested approach involves more than the calculation of DVs. The approach needs to include a damage evaluation model that can examine the impacts of various DVs on different stakeholders. 

The main objective of the recommended methodology is the evaluation of the sufficiency of the social-ecological 

1 3 

Euro-Mediterranean Journal for Environmental Integration (2023) 8:675–689 

683 



systems through the probabilistic description of a set of decision variables (DVs). Each DV is a (quantitative) metric of social performance that can be described in terms of the main interest of the society and the environment. Examples of DVs are the casualties during wildfires, the damage expenses resulting from wildfires, the destroyed public infrastructure, and the discomfort of the residents. Therefore, the social-ecological risk is conventionally estimated as the probability of exceeding a specific value of a decision variable (DV) which matches with the target performance. Each DV is a metric of a specific social-ecological performance and can be estimated in terms of cost/benefit analysis for the users and/or the society (e.g., human casualties, economic expenses, exceedance of service ability). 

The social-ecological system resilience design can be made more effective by applying a decisional strategy to the risk analyses, with the goal being to minimize the total risk or to maximize the utility function. After a wildfire, social and ecological features start to respond and recover via complicated and interlinked interplays. Post-fire social effects can be assessed through surveys, interviews, photographs, and time series analyses (Burton et al. 2011; Annang et al. 2016). 

This methodology is presented in Fig. 3. 

The methodology in Fig. 3 is based on performancebased wildfire engineering metrics that evaluate wild–urban interface zone resilience. The methodology can be expressed in terms of the total probability theorem and is presented in Eq. 2 below: 



<!-- Start of picture text -->
G ( DV ) = ∫∫∫∫∫ G ( DV | DM ) ×  f ( DM | EDP )<br>×  f ( EDP | IM ,  IP ,  SP ) ×  f ( IP | IM ,  SP )<br>×  f ( IM ) ×  f ( SP ) ×  dDM  ×  dEDP<br>×  dIP  ×  dIM  ×  dSP , (2)<br><!-- End of picture text -->

where: 

_G_ (·) = complementary cumulative distribution function _G_ (·|·) = conditional complementary cumulative distribution function 

_f_ (·) = probability density function 

_f_ (·|·) = conditional probability density function 

_DM_ = damage measure (the parameter describing the wildfire-induced physical catastrophe in the social-ecological systems) 

_EDP_ = environmental demand parameter (the parameter describing the environmental responses for the performance evaluation) 

_IM_ = vector of intensity measures (the parameters used to analyze the wildfire hazard) 

1 3 

Euro-Mediterranean Journal for Environmental Integration (2023) 8:675–689 

684 

_SP_ = vector of social parameters (the parameters representing the relative properties of the social system and non-environmental actions) 

_IP_ = vector of interaction analysis parameters (the parameters reporting the interaction phenomena between the social-ecological systems). 

This approach assumes that the performance benchmarking elements can be addressed using a discrete Markov process, where the conditional probabilities of the different parameters in the model are independent. 

## **Discussion** 

The recommended probabilistic risk assessment framework may provide a robust analytical approach for wildfire risk engineering as it has already been applied to other natural hazards (earthquakes, tsunamis, tornados). It is necessary to overcome the lack of knowledge through systematic requirements and coordinated multidisciplinary research efforts. However, in the case of wildfires, resilience is of paramount importance for emergency planning and the risk management of WUI zones. The suggested computational framework integrates uncertainties in wildfire scenarios and considers wildfire-induced complex disturbances of WUI areas, damage, and loss analyses in human–environmental systems. Within this context, the proposed approach introduces interdisciplinary aspects that bridge the chasm between decisionmaking and performance methodological developments that address effective WUI resilience. In particular, it delivers a theoretical methodological framework based on a computational method that perceives socio-ecological resilience in the aftermath of a wildfire from a completely new perspective. Moreover, the new approach develops a state-of-the-art wildfire-risk-based computational framework through performance-based benchmarking metrics and design methods that have a strong scientific basis. This will enable stakeholders to take informed decisions by providing actionable information that can be used by decision-makers for post-ignition emergency response management. 

Considering the wide range of complex effects and interlinkages among the human and natural elements of fire risk, it is difficult to evaluate them using traditional statistical modeling (Elith et al. 2008). Therefore, computational methods and machine-learning algorithms provide a persuasive alternative solution for benchmarking risk based on multiple drivers because they can present the complex interactions among predictors and response variables. Additionally, they are particularly effective in 

realistic applications of parametric modeling that explain the phenomena of interest in terms of both linear and nonlinear relationships and their interactions. 

This research provides a rigorous computational approach that quantifies and predicts socio-ecological resilience after wildfires based on performance-based design metrics (hazard analyses, interaction analyses, damage measures, loss analyses). This aim has been achieved by integrating interdisciplinary scientific techniques from the fields of (a) high-performance data analytics, (b) computational modeling, (d) sophisticated prediction algorithms, (e) machine learning, (f) artificial intelligence, and (g) model-based inference to improve the resilience of human communities and ecosystems when faced with wildfires. 

The multiple scientific advancements that stem from the recommended approach include, among others, (a) an integrated computational platform for probabilistic WUI zone resilience assessment, (b) a holistic computational framework approach including a wildfire-simulating model, ecological and socioeconomic prediction modeling of wildfire damage in terms of economic, social-human, and ecosystem services losses, (c) a novel data-driven modeling approach for urban-fire  simulation which is based on the proposed computational model for the change in quality of life (QoL) due to socio-ecological resilience, and (d) a Markov model inference framework approach to quantify modeling uncertainties and to update decision variables by integrating a new holistic computational platform. Thus, WUI zone resilience systems based on performance-based design metrics can be predicted and monitored . 

## **Conclusions** 

In this paper, a holistic theoretical framework for WUI resilience through performance-based wildfire engineering has been presented. This framework methodology can be used to evaluate the social-ecological risk associated with facilities located in the fragile wild–urban interface zones. Based on the total probability theorem, the problem of risk assessment was disaggregated into the following parts: (1) hazard analysis, (2) social-ecological impact characterization, (3) social-ecological interaction analysis, (4) social-ecological impact analysis, (5) damage analysis, and (6) loss analysis. We have also presented a perspective on resilience engineering after wildfires that provides a totally new basis for building a holistic management approach that improves the resilience and adaptive capacity of the WUI in uncertain times. WUI zones are experiencing unprecedented rates of abiotic, biotic, and socio-economic changes. It is important to note that current management methods cannot continue to be guided 

1 3 

Euro-Mediterranean Journal for Environmental Integration (2023) 8:675–689 

685 

by resilience principles based on maintaining stable wildfire risk tactics when considering WUI resilience through performance-based wildfire engineering. Nowadays, the uncertain future caused by climatic changes significantly guides resilience and adaptive principles, replacing the classic and primary goals of WUI resilience strategy management. Scenario resilience that explores a range of possible futures will replace predictive expectations. Building WUI resilience through performance-based wildfire engineering as dynamic systems, thus, prioritizes accurate future state predictions while leveraging adaptation to new demanding situations. 

Also, this approach based on PBE is a design framework that (1) explicitly describes the performance requirements for the complex interactions among all the ontologies in the WUI impacted by wildfire events, (2) specifies criteria and methods for validating the accomplishment of the performance objectives, and (3) suggests convenient metrics to enhance the design of WUI resilience. Considering the inherent uncertainty and variability of wildfire events leads directly to the fact that the performance-based methodology should be calculated based on the probabilistic theorem. Also, acknowledging the inherent uncertainties, these variables are presented probabilistically, as conditional probabilities of exceedance. This process can be considered a discrete Markov chain, where the conditional probabilities of parameters are independent. 

Furthermore, in the proposed approach, the PBE framework is extended into the field of wildfires, creating an innovative, fully probabilistic methodology for WUI resilience benchmarking. The described computational method integrates uncertainties in the wildfire scenario, considering the complex disturbances caused by fire in WUI areas. The interlinked relationships among the multiple hazards have also been presented. This approach demonstrates several new perspectives when compared to other existing methodologies. In fact, while other methodologies concentrate on single hazards, the suggested method focuses on the hazard of wildfire, which involves many and different hazard receivers (i.e., humans, houses, infrastructures, flora, and fauna). Consequently, a novel arrangement for describing the uncertainties from all relevant sources (wildfires, WUI zones, resilience) through a probabilistic performance assessment analysis has been proposed. Moreover, analytical models of the relevant WUI resilience that is produced by wildfires have been briefly demonstrated. Building a holistic WUI zone resilience framework that considers performance-based wildfire engineering is a very complex task, requiring interdisciplinary knowledge and data. Therefore, it delivers an effective function by providing scientists with a bright illustration of where their knowledge fits into the broader 

framework of performance-based engineering, and how their research conclusions need to be presented. 

This method is focused on how we can apply modern concepts in performance-based engineering to improve the performance and resilience of human communities and ecosystems when attacked by such a major hazard. Therefore, the suggested technique provides a fundamental tool in probabilistic modeling and resistance, with many potential future applications. The consistent probabilistic approach explicitly considers and quantifies the inherent uncertainties for reliable wildfire performance resilience assessment. Furthermore, it is capable of identifying the optimal resilience strategy for WUI planning in terms of the complexity of social-ecological systems, residential developments, locations, climate scenarios, cost and benefit analysis, as well as hazard analysis. 

Finally, this methodology provides an evidence-based and transparent decision-making approach that leads to greater resilience of communities against wildfires, which is achieved through evaluation and design with a strong scientific basis. Using the WUI zone resilience framework, stakeholders (policy-makers, local authorities, emergency managers, etc.) can make more effective decisions regarding resilience, mitigation, adaptation, and evacuations. Another important contribution of the framework is the definition of performance metrics that are suitable for decision-making aimed at wildfire risk mitigation. The methodology provides a consistent procedure that characterizes the wildfire hazard and allows scientists from different disciplines to focus on different aspects of the problem, and that relates these quantitatively to the defined performance metrics (Cornell 2000; Cornell and Krawinkler 2000; Moehle and Deierlein 2004). 

**Funding** Open access funding provided by HEAL-Link Greece. 

**Data availability** The authors confirm that the data supporting the findings of this study are available within the article [and/or] its supplementary materials. 

**Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http:// creat iveco mmons. org/ licen ses/ by/4. 0/. 

1 3 

Euro-Mediterranean Journal for Environmental Integration (2023) 8:675–689 

686 

## **References** 

- Abatzoglou JT, Williams AP, Boschetti L, Zubkova M, Kolden CA (2018) Global patterns of interannual climate–fire relationships. Glob Change Biol 24(11):5164–5175 

- Abatzoglou JT, Battisti DS, Williams AP, Hansen WD, Harvey BJ, Kolden CA (2021) Projected increases in western US forest fire despite growing fuel constraints. Commun Earth Environ 2(1):1–8 

- Adey B, Hajdin R, Brühwiler E (2004) Effect of common cause failures on indirect costs. J Bridg Eng 9(2):200–208 

- Alberti M (2018) Portugal's wildfire that broke a community. BBC News. http:// www. bbc. co. uk/ news/ world- europe- 44438 505. Accessed 17 Aug 2020 

- Aldersley A, Murray SJ, Cornell SE (2011) Global and regional analysis of climate and human drivers of wildfire. Sci Total Environ 409(18):3472–3481 

- Annang L, Wilson S, Tinago C, Wright Sanders L, Bevington T, Carlos B, Cornelius E, Svendsen E (2016) Photovoice: assessing the long-term impact of a disaster on a community’s quality of life. Qual Health Res 26(2):241–251 

- Argyroudis SA, Pitilakis KD (2012) Seismic fragility curves of shallow tunnels in alluvial deposits. Soil Dyn Earthq Eng 35:1–12 

- Argyroudis SA, Mitoulis SΑ, Winter MG, Kaynia AM (2019) Fragility of transport assets exposed to multiple hazards: stateof-the-art review toward infrastructural resilience. Reliab Eng Syst Saf 191:106567 

- Argyroudis S, Mitoulis S, Kaynia AM, Winter MG (2018) Fragility assessment of transportation infrastructure systems subjected to earthquakes. In: Brandenberg SJ, Manzari MT (eds) Geotechnical Earthquake Engineering and Soil Dynamics V: Numerical Modeling and Soil Structure Interaction.  American Society of Civil Engineers, Reston 

- Baker JW (2008) An introduction to probabilistic seismic hazard analysis (PSHA). White paper, version 1:72. scits. stanf ord. edu; https:// scits. stanf ord. edu/ sites/g/ files/ sbiyb j22081/ files/ media/ file/ baker_ 2013_ intro_ psha_ v2_0. pdf 

- Baker JW, Cornell CA (2006) Correlation of response spectral values for multi-component ground motions. Bull Seismol Soc Am 96(1):215–227 

- Balch JK, Bradley BA, Abatzoglou JT, Nagy RC, Fusco EJ, Mahood AL (2017) Human-started wildfires expand the fire niche across the United States. Proc Natl Acad Sci 114(11):2946–2951 

- Barbato M, Petrini F, Unnikrishnan VU, Ciampoli M (2013) Performance-based hurricane engineering (PBHE) framework. Struct Saf 45:24–35 

- Bar-Massada A, Radeloff VC, Stewart SI (2014) Biotic and abiotic effects of human settlements in the wildland–urban interface. Bioscience 64(5):429–437 

- Barrett K, McGuire AD, Hoy EE, Kasischke ES (2011) Potential shifts in dominant forest cover in interior Alaska driven by variations in fire severity. Ecol Appl 21(7):2380–2396 

- Berkes F, Folke C, Colding J (eds) (2000) Linking social and ecological systems: management practices and social mechanisms for building resilience. Cambridge University Press, Cambridge 

- Bjarnadottir S, Li Y, Stewart MG (2011) A probabilistic-based framework for impact and adaptation assessment of climate change on hurricane damage risks and costs. Struct Saf 33(3):173–185 

- Blanchi R, Leonard J, Haynes K, Opie K, James M, de Oliveira FD (2014) Environmental circumstances surrounding bushfire fatalities in Australia 1901–2011. Environ Sci Policy 37:192–203 

Bowman DM, Williamson GJ, Abatzoglou JT, Kolden CA, Cochrane MA, Smith A (2017) Human exposure and sensitivity to globally extreme wildfire events. Nat Ecol Evol 1(3):1–6 

Bowman DM, Kolden CA, Abatzoglou JT, Johnston FH, van der Werf GR, Flannigan M (2020) Vegetation fires in the anthropocene. Nat Rev Earth Environ 1(10):500–515 

Brenkert-Smith H, Meldrum JR, Champ PA, Barth CM (2017) 

Where you stand depends on where you sit: qualitative inquiry into notions of fire adaptation. Ecol Soc 22(3) 

Brookshire DS, Chang SE, Cochrane H, Olson RA, Rose A, Steenson 

- J (1997) Direct and indirect economic losses from earthquake damage. Earthq Spectra 14(4):683–701 

Buckland CE, Bailey RM, Thomas DSG (2019) Using artificial neural networks to predict future dryland responses to human and climate disturbances. Sci Rep 9(1):1–13 

- Burton C, Mitchell JT, Cutter SL (2011) Evaluating post-Katrina recovery in Mississippi using repeat photography. Disasters 35(3):488–509 

- Cai W, Yang J, Liu Z, Hu Y, Weisberg PJ (2013) Post-fire tree recruitment of a boreal larch forest in Northeast China. For Ecol Manag 307:20–29 

- Cardil A, Mola-Yudego B, Bl’azquez-Casado A, Gonz’alez-Olabarria JR (2019) Fire and burn severity assessment: calibration of relative differenced normalized burn ratio (RdNBR) with field data. J Environ Manag 235:342–349 

- Carriger JF, Dyson BE, Benson WH (2018) Representing causal knowledge in environmental policy interventions: advantages and opportunities for qualitative influence diagram applications. Integr Environ Assess Manag 14:381–394 

- Carriger JF, Thompson M, Barron MG (2021) Causal Bayesian networks in assessments of wildfire risks: opportunities for ecological risk assessment and management. Integr Environ Assess Manag 17(6):1168–1178 

- Carroll MS, Paveglio T, Jakes PJ, Higgins LL (2011) Nontribal community recovery from wildfire five years later: the case of the Rodeo-Chediski fire. Soc Nat Resour 24(7):672–687 

- Cavalieri F, Correia AA, Crowley H, Pinho R (2020) Seismic fragility analysis of URM buildings founded on piles: influence of dynamic soil–structure interaction models. Bull Earthq Eng 18:4127–4156 

- Coffield SR, Graff CA, Chen Y, Smyth P, Foufoula-Georgiou E, Randerson JT (2019) Machine learning to predict final fire size at the time of ignition. Int J Wildland Fire 28(11):861–873 

- Cornell CA, Krawinkler H (2000) Progress and challenges in seismic performance assessment. PEER Center News 3:1–3 

- Cornell A (2000) Progress and challenges in seismic performance assessment. PEER Newsletter, Berkeley. https:// apps. peer. berke ley. edu/ news/ 2000s pring/ perfo rmance. html 

- Cortez P, Morais ADJR (2007) A data mining approach to predict forest fires using meteorological data. Associação Portuguesa para a Inteligência Artificial (APPIA), Porto 

- Cote M, Nightingale AJ (2012) Resilience thinking meets social theory: situating social change in socio-ecological systems (SES) research. Prog Hum Geogr 36(4):475–489 

- Crawford SH (2001) Understanding the complexity of economic, ecological, and social systems. Ecosystems 4(5):390–405 

De Graff JV (2014) Improvement in quantifying debris flow risk for post-wildfire emergency response. Geoenviron Disasters 1(1):1–10 

- Debouk H, Riera-Tatché R, Vega-García C (2013) Assessing postfire regeneration in a Mediterranean mixed forest using lidar data and artificial neural networks. Photogramm Eng Remote Sensing 12:1121–1130 

De Rigo D, Libertà G, Durrant TH, Vivancos TA, San-Miguel-Ayanz J (2017) Forest fire danger extremes in Europe under climate 

1 3 

Euro-Mediterranean Journal for Environmental Integration (2023) 8:675–689 

687 

change: variability and uncertainty. Doctoral dissertation. Publications Office of the European Union, Luxembourg Dlamini WM (2011) Application of Bayesian networks for fire risk mapping using GIS and remote sensing data. GeoJournal 76(3):283–96. http:// www. jstor. org/ stable/ 41148 456 Dolfing AG, Leuven JR, Dermody BJ (2019) The effects of network topology, climate variability and shocks on the evolution and resilience of a food trade network. PLoS ONE 14(3):e0213378 Elith J, Leathwick JR, Hastie T (2008) A working guide to boosted regression trees. J Anim Ecol 77(4):802–813 

- Ellingwood B, Corotis RB, Boland J, Jones NP (1993) Assessing cost of dam failure. J Water Resour Plan Manag 119(1):64–82 

- Carballo JE, Cornell CA (2000) Probabilistic seismic demand analysis: spectrum matching and design. PhD dissertation. Stanford University, Stanford 

- Dixie Fire (2021). https:// en. wikip edia. org/ wiki/ Dixie_ Fire. Accessed 02 Mar 2022 

- Fair K (2020) Modelling resilience and sustainability of complex human-environment systems in agriculture and ecology. PhD thesis. University of Waterloo, Waterloo. http:// hdl. handle. net/ 10012/ 15966 

- Fairman TA, Bennett LT, Tupper S, Nitschke CR (2017) Frequent wildfires erode tree persistence and alter stand structure and initial composition of a fire-tolerant sub-alpine forest. J Veg Sci 28(6):1151–1165 

- Falk DA, van Mantgem PJ, Keeley JE, Gregg RM, Guiterman CH, Tepley AJ, Young DJ, Marshall LA (2022) Mechanisms of forest resilience. For Ecol Manag 512:120129 

- Fernandez-Anez N, Krasovskiy A, Müller M, Vacik H, Baetens J, Hukić E, Kapovic Solomun M, Atanassova I, Glushkova M, Bogunović I, Fajković H (2021) Current wildland fire patterns and challenges in Europe: a synthesis of national perspectives. Air Soil Water Resear 14:11786221211028184 

- Folke C, Jansson Å, Rockström J, Olsson P, Carpenter SR, Chapin FS, Crépin AS, Daily G, Danell K, Ebbesson J, Elmqvist T (2011) Reconnecting to the biosphere. Ambio 40(7):719–738 

- Forcellini D (2019) A new methodology to assess indirect losses in bridges subjected to multiple hazards. Innov Infrastruct Solut 4:1–9 

- Forcellini D, Alzabeebee S (2022) Seismic fragility assessment of geotechnical seismic isolation (GSI) for bridge configuration. Bull Earthq Eng 1–22 

- Glaser M, Krause G, Ratter BM, Welp M (eds) (2012) Human–nature interactions in the Anthropocene: potentials of social-ecological systems analysis. Routledge, Abingdon-on-Thames 

- Gómez-González S, González ME, Paula S, Díaz-Hormazábal I, Lara A, Delgado-Baquerizo M (2019) Temperature and agriculture are largely associated with fire activity in Central Chile across different temporal periods. For Ecol Manag 433:535–543 

- Griffis L, Patel V, Muthukumar S, Baldava S (2013) A framework for performance-based wind engineering. In: Jones CP, Griffis LG (eds) Advances in hurricane engineering: learning from our past. American Society of Civil Engineers, Reston, pp 1205–1216 

- Hamburger RO, Whittaker AS (2003) Considerations in performancebased blast resistant design of steel structures. In: Proc AISCSINY Symp on Resisting Blast and Progressive Collapse, New York, NY, USA, 4–5 Dec 2003 

- Hellenic Forest Service (2022) Data of 2022 wildfire in Eastern Attica, Mati and Rafina. Hellenic Forest Service, Athens 

- Hermosilla T, Wulder MA, White JC, Coops NC, Hobart GW (2015) Regional detection, characterization, and attribution of annual forest change from 1984 to 2012 using Landsat-derived timeseries metrics. Remote Sens Environ 170:121–132 

- Hradsky BA, Penman TD, Ababei D, Hanea A, Ritchie EG, York A, Di Stefano J (2017) Bayesian networks elucidate interactions 

between fire and other drivers of terrestrial fauna distributions. Ecosphere 8(8):e01926 IRGC (2018) Guidelines for the governance of systemic risks.  International Risk Governance Center, Lausanne 

Jain P, Coogan SC, Subramanian SG, Crowley M, Taylor S, Flannigan MD (2020) A review of machine learning applications in wildfire science and management. Environ Rev 28(4):478–505 

Johnston JM, Wooster MJ, Paugam R, Wang X, Lynham TJ, Johnston LM (2017) Direct estimation of Byram’s fire intensity from infrared remote sensing imagery. Int J Wildland Fire 26(8):668–684 

Jung M, Tautenhahn S, Wirth C, Kattge J (2013) Estimating basal area of spruce and fir in post-fire residual stands in central Siberia using quickbird, feature selection, and random forests. Procedia Comput Sci 18:2386–2395 

Kaikkonen L, Parviainen T, Rahikainen M, Uusitalo L, Lehikoinen A (2021) Bayesian networks in environmental risk assessment: a review. Integr Environ Assess Manag 17(1):62–78 Kappes MS, Papathmoa-Kohle M, Keiler M (2012) Assessing physical vulnerability for multi-hazards using an indicator-based methodology. Appl Geogr 32(2):577–590 

Kates RW, Colten CE, Laska S, Leatherman SP (2006) Reconstruction of New Orleans after Hurricane Katrina: a research perspective. Proc Natl Acad Sci 103(40):14653–14660 

- Keeley JE (2009) Fire intensity, fire severity and burn severity: a brief review and suggested usage. Int J Wildland Fire 18(1):116–126 

- Keeley JE, Baer-Keeley M, Fotheringham CJ (2005) Alien plant dynamics following fire in Mediterranean-climate California shrublands. Ecol Appl 15(6):2109–2125 

- Keeley JE, Safford H, Fotheringham CJ, Franklin J, Moritz M (2009) The 2007 southern California wildfires: lessons in complexity. J Forest 107(6):287–296 

- Ko Y-Y, Yang H-H (2019) Deriving seismic fragility curves for sheetpile wharves using finite element analysis. Soil Dyn Earthq Eng 123(2019):265–277 

- Kooistra C, Hall TE, Paveglio T, Pickering M (2018) Understanding the factors that influence perceptions of post-wildfire landscape recovery across 25 wildfires in the Northwestern United States. Environ Manag 61(1):85–102 

- Kramer HA, Mockrin MH, Alexandre PM, Stewart SI, Radeloff VC (2018) Where wildfires destroy buildings in the US relative to the wildland–urban interface and national fire outreach programs. Int J Wildland Fire 27(5):329–341 

- LaMere K, Mäntyniemi S, Haapasaari P (2020) The effects of climate change on Baltic salmon: framing the problem in collaboration with expert stakeholders. Sci Total Environ 10(738):140068 

- Lamont S, Rini D (2008) Performance-based structural fire engineering for modern building design. In: Proc Structures Congr 2008, Vancouver, BC, Canada, 24–26 Apr  2008 

- Levin SA (1998) Ecosystems and the biosphere as complex adaptive systems. Ecosystems 1(5):431–436 

- Li Y, van de Lindt JW, Dao T, Bjarnadottir S, Ahuja A (2012) Loss analysis for combined wind and surge in hurricanes. Nat Hazard Rev 13(1):1–10 

- Liang H, Zhang M, Wang H (2019) A neural network model for wildfire scale prediction using meteorological factors. IEEE Access 7:176746–176755 

- Linkov I, Trump BD, Fox-Lent C (2016) Resilience: approaches to risk analysis and governance. An edited collection of authored pieces comparing, contrasting, and integrating risk and resilience with an emphasis on ways to measure resilience. In: Florin M-V, Linkov I (eds)IRGC resource guide on resilience. EPFL International Risk Governance Center, Lausanne, pp 3–14 

- Luoma K, Niemi JV, Aurela M, Lun Fung P, Helin A, Hussein T, Kangas L, Kousa A, Rönkkö T, Timonen H, Virkkula A, Petäjä T (2021) Spatiotemporal variation and trends in equivalent black 

1 3 

Euro-Mediterranean Journal for Environmental Integration (2023) 8:675–689 

688 

carbon in the Helsinki metropolitan area in Finland. Atmos Chem Phys 21(2):1173–1189 

- McFayden CB, Boychuk D, Woolford DG, Wheatley MJ, Johnston L (2019) Impacts of wildland fire effects on resources and assets through expert elicitation to support fire response decisions. Int J Wildland Fire 28(11):885–900 

- McLauchlan KK, Higuera PE, Miesel J, Rogers BM, Schweitzer J, Shuman JK, Tepley AJ, Varner JM, Veblen TT, Adalsteinsson SA, Balch JK (2020) Fire as a fundamental ecological process: research advances and frontiers. J Ecol 108(5):2047–2069 

- McWethy DB, Schoennagel T, Higuera PE, Krawchuk M, Harvey BJ, Metcalf EC, Schultz C, Miller C, Metcalf AL, Buma B, Virapongse A (2019) Rethinking resilience to wildfire. Nat Sustain 2(9):797–804 

- Miller JD, Yool SR (2002) Mapping forest post-fire canopy consumption in several overstory types using multi-temporal Landsat TM and ETM data. Remote Sens Environ 82(2–3):481–496 

- Miranda A, Carrasco J, González M, Pais C, Lara A, Altamirano A, Weintraub A, Syphard AD (2020) Evidence-based mapping of the wildland-urban interface to better identify human communities threatened by wildfires. Environ Res Lett 15(9):094069 

- Miyanishi K (2001) Forest fires: behavior and ecological effects. Elsevier, Amsterdam 

- Moehle J, Deierlein GG (2004) A framework methodology for performance-based earthquake engineering. In: 13th world conference on earthquake engineering, vol 679, Vancouver, BC, Canada, 1–6 Aug 2004 

- Moritz MA, Batllori E, Bradstock RA, Gill AM, Handmer J, Hessburg PF, Leonard J, McCaffrey S, Odion DC, Schoennagel T, Syphard AD (2014) Learning to coexist with wildfire. Nature 515(7525):58–66 

- Moschonas IF, Kappos AJ, Panetsos P, Papadopoulos V, Makarios T, Thanopoulos P (2009) Seismic fragility curves for Greek bridges: methodology and case studies. Bull Earthq Eng 7:439–468 

- National & Kapodistrian University of Athens (2021) The July-August 2021 Wildfires in Greece. Newslett Environ Disaster Crises Management Strategies 25. https:// forest- fires- greece- nkua1 837. hub. arcgis. com. Accessed 21 Mar 2020 

- OECD (2019) Good governance for critical infrastructure resilience. OECD, Paris 

- Oliveira S, Gonçalves A, Zêzere JL (2021) Reassessing wildfire susceptibility and hazard for mainland Portugal. Sci Total Environ 762:143121 

- Özbayoğlu AM, Bozer R (2012) Estimation of the burned area in forest fires using computational intelligence techniques. Procedia Comput Sci 12:282–287 

- Palaiologou P, Kalabokidis K, Day MA, Kopsachilis V (2020) Evaluating socioecological wildfire effects in Greece with a novel numerical index. Fire 3(4):63 

- Pausas JG, Keeley JE (2019) Wildfires as an ecosystem service. Front Ecol Environ 17(5):289–295 

- Pausas JG, Keeley JE, Schwilk DW (2017) Flammability as an ecological and evolutionary driver. J Ecol 105(2):289–297 

- Penman TD, Cirulis B, Marcot BG (2020) Bayesian decision network modeling for environmental risk management: a wildfire case study. J Environ Manag 15(270):110735 

- Petrini F, Augusti G, Ciampoli M (2009) A probabilistic framework for performance-based wind engineering. In: Proc 5th European & African Conf on Wind Eng, Florence, Italy, 19–23 July 2009, pp 119–122 

- Pinelli JP, Barbato M (2019) A comparison study of catastrophe modeling vs. performance-based design. In: 13th Int Conf on Applications of Statistics and Probability in Civil Engineering (ICASP13), Seoul, South Korea, 26–30 May 2019 

- Pita GL, Pinelli JP, Gurley KR, Hamid S (2013) Hurricane vulnerability modeling: development and future trends. J Wind Eng Ind Aerodyn 114:96–105 

- Pita G, Pinelli JP, Gurley K, Mitrani-Reiser J (2014) State of the art of hurricane vulnerability estimation methods: a review. Nat Hazard Rev 16(2):04014022 

- Poon PK, Kinoshita AM (2018) Estimating evapotranspiration in a post-fire environment using remote sensing and machine learning. Remote Sens 10(11):1728 

- Porter KA (2003) An overview of PEER’s performance-based earthquake engineering methodology. In: Proc Ninth Int Conf on Applications of Statistics and Probability in Civil Eng, pp 973–980 

- Porter KA (2015) Beginner's guide to fragility, vulnerability, and risk. In: Beer M, Kougioumtzoglou I, Patelli E, Au IK (eds) Encyclopedia of earthquake engineering. Springer, Berlin 

- Preiser R, Biggs R, De Vos A, Folke C (2018) Social-ecological systems as complex adaptive systems. Ecol Soc 23(4) 

- Pyne SJ (2017) Fire in America: a cultural history of wildland and rural fire. University of Washington Press, Seattle 

- Radeloff VC, Helmers DP, Kramer HA, Mockrin MH, Alexandre PM, Bar-Massada A, Butsic V, Hawbaker TJ, Martinuzzi S, Syphard AD, Stewart SI (2018) Rapid growth of the US wildland–urban interface raises wildfire risk. Proc Natl Acad Sci 115(13):3314–3319 

- Rappold AG, Reyes J, Pouliot G, Cascio WE, Diaz-Sanchez D (2017) Community vulnerability to health impacts of wildland fire smoke exposure. Environ Sci Technol 51(12):6674–6682 

- Reggiani A (2013) Network resilience for transport security: some methodological considerations. Transp Policy 28:63–68 

- Riggs HR, Robertson IN, Cheung KF, Pawlak G, Young YL, Yim SC (2008) Experimental simulation of tsunami hazards to buildings and bridges. In: Proceedings of 2008 NSF Engineering Research and Innovation Conference, Knoxville, Tennessee, 7–10 Jan 2008, pp 1056–1064 

- Rodrigues M, Jiménez A, de la Riva J (2016) Analysis of recent spatial–temporal evolution of human driving factors of wildfires in Spain. Nat Hazards 84(3):2049–2070 

- Sakellariou S, Samara F, Tampekis S, Christopoulou O, Sfougaris A (2017) Optimal number and location of watchtowers for immediate detection of forest fires in a small island. Int J Agr Environ Inf Syst (IJAEIS) 8(4):1–19 

- Sakellariou S, Parisien MA, Flannigan M, Wang X, de Groot B, Tampekis S, Samara F, Sfougaris A, Christopoulou O (2020) Spatial planning of fire-agency stations as a function of wildfire likelihood in Thasos. Greece Sci Total Environ 729:139004 

- Sakellariou S, Sfougaris A, Christopoulou O, Tampekis S (2022a) Integrated wildfire risk assessment of natural and anthropogenic ecosystems based on simulation modeling and remotely sensed data fusion. Int J Disaster Risk Reduct 78:103129 

- Sakellariou S, Sfoungaris G, Christopoulou O (2022b) Territorial resilience through visibility analysis for immediate detection of wildfires integrating fire susceptibility, geographical features, and optimization methods. Int J Disaster Risk Sci 13:621–635 

- Schoennagel T, Balch JK, Brenkert-Smith H, Dennison PE, Harvey BJ, Krawchuk MA, Mietkiewicz N, Morgan P, Moritz MA, Rasker R, Turner MG (2017) Adapt to more wildfire in western North American forests as climate changes. Proc Natl Acad Sci 114(18):4582–4590 

- Schumann RL III, Mockrin M, Syphard AD, Whittaker J, Price O, Gaither CJ, Emrich CT, Butsic V (2020) Wildfire recovery as a “hot moment” for creating fire-adapted communities. Int J Disaster Risk Reduct 42:101354 

- Scott JH, Thompson MP, Calkin DE (2013) A wildland fire risk assessment framework for land and resource management. General 

1 3 

Euro-Mediterranean Journal for Environmental Integration (2023) 8:675–689 

689 

technical report RMRSGTR-315. USDA Forest Service, Rocky Mountain Research Station, Logan 

- Shidik GF, Mustofa K (2014) Predicting size of forest fire using hybrid model. In: Proc Information and Communication Technology: Second IFIP TC5/8 Int Conf (ICT-EurAsia 2014), Bali, Indonesia, 14–17 April 2014. Springer, Berlin, pp 316–327 

- Shinozuka M, Feng MQ, Kim HK, Kim SH (2000) Nonlinear static procedure for fragility curve development. J Eng Mech 126(12):1287–1295 

- Staal A, Dekker SC, Hirota M, van Nes EH (2015) Synergistic effects of drought and deforestation on the resilience of the south-eastern Amazon rainforest. Ecol Complex 22:65–75 

- Steelman TA, Burke CA (2007) Is wildfire policy in the United States sustainable. J Forest 105(2):67–72 

- Suweis S, Carr JA, Maritan A, Rinaldo A, D’Odorico P (2015) Resilience and reactivity of global food security. Proc Natl Acad Sci 112(22):6902–6907 

- Syphard AD, Clarke KC, Franklin J (2007) Simulating fire frequency and urban growth in southern California coastal shrublands, USA. Landscape Ecol 22(3):431–445 

- Syphard AD, Keeley JE, Massada AB, Brennan TJ, Radeloff VC (2012) Housing arrangement and location determine the likelihood of housing loss due to wildfire. PLoS ONE 7(3):e33954 

- Syphard AD, Keeley JE, Pfaff AH, Ferschweiler K (2017) Human presence diminishes the importance of climate in driving fire activity across the United States. Proc Natl Acad Sci 114(52):13750–13755 

- Syphard AD, Rustigian-Romsos H, Mann M, Conlisk E, Moritz MA, Ackerly D (2019) The relative influence of climate and housing development on current and projected future fire patterns and structure loss across three California landscapes. Glob Environ Chang 56:41–55 

- Tedim F, Leone V, Amraoui M, Bouillon C, Coughlan MR, Delogu GM, Fernandes PM, Ferreira C, McCaffrey S, McGee TK, Parente J (2018) Defining extreme wildfire events: difficulties, challenges, and impacts. Fire 1(1):9 

- Thie L, Tart KT (2018) On the front lines of climate health effects in North Carolina. N C Med J 79(5):318–323 

- Toujani A, Achour H, Faïz S (2018) Estimating forest fire losses using stochastic approach: case study of the Kroumiria Mountains (northwestern Tunisia). Appl Artif Intell 32(9–10):882–906 

   - due to anthropogenic warming projected with non-stationary climate-fire models. Nat Commun 9(1):1–9 

   - Turner MG, Romme WH, Gardner RH (1999) Prefire heterogeneity, fire severity, and early postfire plant reestablishment in subalpine forests of Yellowstone National Park, Wyoming. Int J Wildland Fire 9(1):21–36 

   - Turner BL, Kasperson RE, Matson PA, McCarthy JJ, Corell RW, Christensen L, Eckley N, Kasperson JX, Luers A, Martello ML, Polsky C (2003) A framework for vulnerability analysis in sustainability science. Proc Natl Acad Sci 100(14):8074–8079 

   - Turner BL II (2010) Vulnerability and resilience: coalescing or paralleling approaches for sustainability science. Glob Environ Chang 20(4):570–576 

   - United Nations Office for Disaster Risk Reduction (2020) Sendai Framework Terminology On Disaster Risk Reduction:  Vulnerability. https:// www. undrr. org/ termi nology/ vulne rabil ity. Accessed 20 Mar 2020 

   - Van der Hoorn B (2020) Seeing the bigger picture: conditions that influence effective engagement of project executives with visuals. Int J Project Manager 38(2):137–151 

   - Walker B, Salt D (2012) Resilience thinking: sustaining ecosystems and people in a changing world. Island, Washington, DC 

   - Westerling AL, Hidalgo HG, Cayan DR, Swetnam TW (2006) Warming and earlier spring increase western US forest wildfire activity. Science 313(5789):940–943 

   - Wikipedia (2020) 2019–20 Australian bushfire season. https:// en. wikip edia. org/ wiki/ 2019% E2% 80% 9320_ Austr alian_ bushfi re_ season. Accessed 5 Nov 2021 

   - Wotton BM, Flannigan MD, Marshall GA (2017) Potential climate change impacts on fire intensity and key wildfire suppression thresholds in Canada. Environ Res Lett 12(9):095003 

   - Wu J (2013) Landscape sustainability science: ecosystem services and human well-being in changing landscapes. Landscape Ecol 28(6):999–1023 

   - Zingraff-Hamed A, Noack M, Greulich S, Schwarzwälder K, Wantzen KM, Pauleit S (2018) Model-based evaluation of urban river restoration: conflicts between sensitive fish species and recreational users. Sustainability 10(6):1747 

   - Zwirglmaier K, Papakosta P, Straub D (2013) Learning a Bayesian network model for predicting wildfire behavior. In: ICOSSAR 2013, New York , NY, USA, 16–20 June 2013 

- Turco M, Rosa-Cánovas JJ, Bedia J, Jerez S, Montávez JP, Llasat MC, Provenzale A (2018) Exacerbated fires in Mediterranean Europe 

1 3 


