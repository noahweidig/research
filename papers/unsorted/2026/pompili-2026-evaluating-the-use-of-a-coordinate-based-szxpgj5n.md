---
title: Evaluating the use of a coordinate-based tensor-product for addressing spatial autocorrelation in shallow landslide susceptibility modelling
authors:
- Pompili, Laura
- Sorichetta, Alessandro
- Economou, Theodoros
- Bondarenko, Maksym
- Yankey, Ortis
- Camera, Corrado A. S.
year: '2026'
journal: Stochastic Environmental Research and Risk Assessment
doi: 10.1007/s00477-026-03283-2
tags:
- modeling
- spatial analysis
- statistics
- validation
zotero_key: SZXPGJ5N
item_type: journalArticle
url: https://doi.org/10.1007/s00477-026-03283-2
source_url: 'unpaywall: https://link.springer.com/content/pdf/10.1007/s00477-026-03283-2.pdf'
fulltext_status: fulltext
synced: '2026-11-09'
---

# Evaluating the use of a coordinate-based tensor-product for addressing spatial autocorrelation in shallow landslide susceptibility modelling

## Abstract

This study develops two statistical models for assessing shallow landslide susceptibility at the slope-unit scale in the Aosta Valley (Italy), explicitly accounting for spatial autocorrelation. A shallow landslide inventory was compiled by integrating the Italian Landslide Inventory (IFFI) with the Regional Inventory of Instabilities of the Aosta Valley and used as a binary response variable. Geo-environmental predictors were optimised through a structured workflow combining multicollinearity analysis, stepwise selection, Random Forest classification, and Generalised Additive Models (GAMs), which were used to explore predictor–response relationships. Spatial autocorrelation was addressed by including slope-unit coordinates through a tensor-product smooth, resulting in two models: model_A, excluding the tensor term, and model_B, including it. Model performance was evaluated using spatial and non-spatial k-fold cross-validation based on mean Decrease in Deviance explained (mDD%), Effective Degrees of Freedom (EDF), and AUROC. In addition, on the final maps, Global Moran’s I was calculated on prediction residuals to evaluate spatial autocorrelation. Both models are statistically significant and show high discriminatory power (AUROC > 0.85). Including the tensor term improved training performance as suggested by increasing deviance explained (39.0 vs 35.9), R2 (0.42 vs 0.39), and decreasing AIC (714.2 vs 724.5), and helped remove residual spatial autocorrelation. Distributions of mDD% and EDF indicate greater stability for model_B, with constrained variability in predictor contributions, whereas model_A shows wider dispersion, reflecting sensitivity to training data partitioning. However, improvements in testing performance under spatial cross-validation are modest, indicating that the spatial tensor captures local spatial structure but does not substantially enhance spatial generalisation.

## Full text

Stochastic Environmental Research and Risk Assessment (2026) 40:157 https://doi.org/10.1007/s00477-026-03283-2 

**ORIGINAL PAPER** 



# **Evaluating the use of a coordinate-based tensor-product for addressing spatial autocorrelation in shallow landslide susceptibility modelling** 

**Laura Pompili**<sup>**1**</sup> **· Alessandro Sorichetta**<sup>**1**</sup> **· Theodoros Economou**<sup>**2**</sup> **· Maksym Bondarenko**<sup>**3**</sup> **· Ortis Yankey**<sup>**3**</sup> **· Corrado A. S. Camera**<sup>**1**</sup> 

Received: 4 February 2026 / Accepted: 14 May 2026 / Published online: 5 June 2026 © The Author(s) 2026 

#### **Abstract** 

This study develops two statistical models for assessing shallow landslide susceptibility at the slope-unit scale in the Aosta Valley (Italy), explicitly accounting for spatial autocorrelation. A shallow landslide inventory was compiled by integrating the Italian Landslide Inventory (IFFI) with the Regional Inventory of Instabilities of the Aosta Valley and used as a binary response variable. Geo-environmental predictors were optimised through a structured workflow combining multicollinearity analysis, stepwise selection, Random Forest classification, and Generalised Additive Models (GAMs), which were used to explore predictor–response relationships. Spatial autocorrelation was addressed by including slope-unit coordinates through a tensor-product smooth, resulting in two models: model_A, excluding the tensor term, and model_B, including it. Model performance was evaluated using spatial and non-spatial k-fold cross-validation based on mean Decrease in Deviance explained (mDD%), Effective Degrees of Freedom (EDF), and AUROC. In addition, on the final maps, Global Moran’s I was calculated on prediction residuals to evaluate spatial autocorrelation. Both models are statistically significant and show high discriminatory power (AUROC > 0.85). Including the tensor term improved training performance as suggested by increasing deviance explained (39.0 vs 35.9), R<sup>2</sup> (0.42 vs 0.39), and decreasing AIC (714.2 vs 724.5), and helped remove residual spatial autocorrelation. Distributions of mDD% and EDF indicate greater stability for model_B, with constrained variability in predictor contributions, whereas model_A shows wider dispersion, reflecting sensitivity to training data partitioning. However, improvements in testing performance under spatial cross-validation are modest, indicating that the spatial tensor captures local spatial structure but does not substantially enhance spatial generalisation. 

**Keywords** Generalised Additive Model · Data-driven modelling · Slope units · k-fold cross-validation · Aosta Valley · Northern Italy 

Laura Pompili laura.pompili@unimi.it Alessandro Sorichetta alessandro.sorichetta@unimi.it Theodoros Economou T.Economou@exeter.ac.uk Maksym Bondarenko M.Bondarenko@soton.ac.uk Ortis Yankey O.Yankey@soton.ac.uk 

Corrado A. S. Camera corrado.camera@unimi.it 1 Dipartimento di Scienze della Terra “Ardito Desio”, Università degli Studi di Milano, Milan, Italy 2 Department of Mathematics and Statistics, University of Exeter, Exeter, UK 3 WorldPop, School of Geography and Environmental Science, University of Southampton, Southampton, UK 

**<mark>157</mark>** <mark>Page 2 of 26</mark> 

Stochastic Environmental Research and Risk Assessment (2026) 40:157 

## **1 Introduction** 

Landslides are among the most frequent natural hazards, posing a significant global threat to human lives, infrastructure, economies, and ecosystems. Therefore, predicting such events or at least identifying the susceptible areas is key for effective land management, as well as for exposure and vulnerability assessments (UNISDR 2017). Landslide susceptibility refers to the likelihood of a landslide occurring in a given area, based on local terrain conditions (Brabb 1984), and therefore depicts the degree to which slope movements can affect the terrain. However, the concept of susceptibility does not account for the temporal probability of instability or the magnitude of the expected phenomenon (Committee on the Review of the National Landslide Hazards Mitigation Strategies 2004). In mathematical terms, landslide susceptibility represents the probability of spatial occurrence of slope instabilities, given a set of geo-environmental characteristics (Guzzetti et al. 2005). It is then clear that landslide susceptibility is strongly linked to the landscape sensitivity concept, which concerns “the likelihood that a given change in the controls of a system or the forces applied to the system will produce a sensible, recognisable, and persistent response” (Brunsden 2001), e.g., landslide occurrence. 

Among the several types of landslides, we focused on shallow landslides, which typically occur on steep soilmantled slopes. Several methods exist for modelling landslide susceptibility, generally grouped into qualitative (i.e., descriptive) and quantitative (i.e., numerical) methods. Among the latter, statistically based approaches and machine learning techniques are widely used (e.g., Camera et al. 2021; Catani et al. 2013; Di Napoli et al. 2021; Petschko et al. 2012). When such methods are employed, variable selection becomes a crucial preliminary step, as it helps reduce the complexity of the model and avoids redundancy (Alvioli et al. 2024). In cases of extensive sets of predictors, the risk of overfitting becomes critical, potentially preventing the model from being generalised, interpreted, and applied to other study areas. A further complication concerns the computational expense associated with considering such large datasets. Over the years, many variable selection strategies have been proposed, each characterised by different assumptions, advantages, and limitations. Most studies rely on a single feature selection technique. Some studies rely on collinearity or multicollinearity assessments (e.g., Di Napoli et al. 2021; Swain et al. 2024), whereas others depend on the inherent feature-selection capability of the chosen modelling approach (e.g., Camera et al. 2021; Catani et al. 2013). Another common strategy is the use of forward, backward, or both-way stepwise selection to minimise the Akaike Information Criterion (e.g., Broeckx et al. 2019). Hybrid variable selection approaches offer 

an increase in the robustness of the selection process and mitigate the biases associated with individual techniques. Machine-learning frameworks usually combine one selection method with a classifier (e.g., Abdel-salam et al. 2024). Sequential combinations of multiple selection strategies are much less common in applied studies, with examples mainly pertaining to the medical domain (e.g., Song et al. 2025), and only a handful in the environmental sciences. In this work, we test a new multi-stage variable selection workflow that integrates the strengths of multicollinearity assessment, both-way stepwise selection, Random Forest classification, the Akaike Information Criterion (AIC), and penalised smooth functions embedded in a Generalised Additive Model (GAM) framework. 

Assessment of landslide susceptibility requires the preliminary selection of an appropriate Terrain Mapping Unit (TMU), which refers to a portion of the surface characterised by a set of ground conditions that differ from those of adjacent units across distinct physical or geographical boundaries (Carrara et al. 1995; Guzzetti et al. 2005). Commonly used mapping units include grid cells (e.g., Di Napoli et al. 2021; Camera et al. 2021; Liu et al. 2024) and slope units (e.g., Liang et al. 2021; Alvioli et al. 2024). Grid-cell-based modelling is straightforward and computationally convenient (Ba et al. 2018), but grid cells are arbitrarily defined in space; hence, they lack intrinsic physical meaning, and any physical interpretation is inherited from the associated values. Conversely, slope units (SUs) are geomorphologically defined, corresponding to single slopes, combinations of adjacent slopes, or small catchments (Alvioli et al. 2016; Woodard et al. 2024). Given their nature, SUs are more directly associated with the actual geological and morphological framework than grid cells. For this reason, we selected SUs as mapping units for landslide susceptibility modelling in this study. 

Landslide susceptibility modelling has increasingly relied on data-driven approaches, including statistical and machine learning methods, to relate landslide occurrence to environmental predictors (e.g., Goetz et al. 2015; Reichenbach et al. 2018). Despite their widespread use, statistically based models have several limitations. First, they only forecast whether a landslide is probable to occur within a mapping unit, regardless of the number or size of the expected landslides in each unit (Lombardo et al. 2020). Second, they usually ignore the spatial relationship between landslide occurrences in adjacent mapping units; as a result, adjacent, neighbouring, and distant mapping units are treated equally (Lombardo et al. 2020). Third, they assume the likelihood of landslides within an area is _time-independent_ (e.g., Cama et al. 2015), an assumption that is unrealistic given temporal variations in both predisposing and triggering factors. 

```
1 3
```

<mark>Page 3 of 26</mark> **<mark>157</mark>** 

Stochastic Environmental Research and Risk Assessment (2026) 40:157 

Among these limitations, the lack of explicit spatial structure is particularly relevant. Landslide data are inherently spatial, and nearby observations often tend to be more similar than distant ones. Samia et al. (2017a, b) introduced this concept as “landslide path dependency”, meaning that new landslides are more likely to occur within or close to previous landslides. Ignoring this spatial dependence may lead to biased parameter estimates, inflated model performance, and reduced generalisability (e.g., Brenning 2005; Dormann 2007). Moreover, spatially autocorrelated residuals are commonly interpreted as evidence of model misspecification and unaccounted spatial structure/processes (Li et al. 2019). This issue is particularly relevant in mountainous regions characterised by strong topographic variability, where landslides tend to cluster spatially. Empirical evidence shows that spatially explicit models significantly outperform non-spatial counterparts, with improvements in predictive accuracy of up to 35% (Aristizábal et al. 2025). 

To address this limitation, several approaches have been proposed, including spatial regression models, eigenvectorbased spatial filtering, and the inclusion of spatial predictors or neighbourhood-based features (e.g., Brenning 2012; Li et al. 2019). Recent studies have increasingly recognised the importance of spatial dependence in landslide susceptibility modelling (e.g., Fang et al. 2025; Ding et al. 2025; Ebrahim et al. 2026). For instance, Lombardo et al. (2020) incorporate the spatial dimension by accounting for the areal extent of landslides. Zhang et al. (2024) address spatial autocorrelation by partitioning the dataset into four equally sized latitudinal sections and using each section in turn as the test set, while training the model on the remaining three. Fang et al. (2025) implement a spatial binomial GAM that incorporates continuous and discrete spatial dependence via Duchon splines and Markov random field functions, respectively. 

Despite these advances, many susceptibility studies still rely on random data partitioning and do not explicitly account for spatial dependence. As a result, high predictive accuracy may coexist with spatially inconsistent predictions and limited generalisability and transferability (Roberts et al. 2017). Indeed, although machine learning methods often improve predictive performance, they do not inherently solve spatial dependence issues (e.g., Al-Najjar and Pradhan 2021), and even high-performing models may exhibit poor spatial reliability (Zhou and Xing 2025). This highlights the need for simple, transparent approaches to incorporating spatial structure into statistical modelling frameworks. 

In other environmental applications, some studies have incorporated a two-dimensional smooth function (i.e., a tensor-product smooth) to deal with spatial structure in the data, such as in analyses of toxin concentrations (Stoner et al. 2023) and daily temperature (Economou et al. 2023). To our knowledge, no landslide susceptibility analysis has 

implemented such an approach. Including a tensor-product smooth of spatial coordinates allows the model to capture residual spatial structure that is not fully explained by the other geo-environmental predictors, thereby improving model fit and stability. However, such smooths primarily act as a proxy for spatial structure, capturing large-scale spatial variation, and should be interpreted as a spatial adjustment term rather than an additional explanatory predictor. 

This study aims to develop a statistically based model for assessing shallow landslide susceptibility across the entire Aosta Valley, with a specific focus on explicitly addressing potential spatial autocorrelation. The key novelty of this work lies in the inclusion of a coordinate-based tensor-product smooth within the set of geo-environmental predictors in a landslide susceptibility model, allowing the GAM to capture spatial structures in the data. By doing so, we aim to improve the model’s predictive accuracy. In particular, the specific objectives of this study are to: (i) test a new multistage methodological workflow for optimising the selection of geo-environmental predictors; (ii) evaluate the statistical significance and physical plausibility of the predictors within a GAM; and (iii) assess the importance of explicitly modelling spatial autocorrelation via a tensor-product smooth in a landslide susceptibility model within the GAM framework. 

Section 2 introduces the geographical and geological features of the study area, along with the description of the considered landslide inventory, mapping units, and geoenvironmental predictors. Section 3 presents the exploratory analysis for identifying the geo-environmental predictors and how they were integrated into a GAM-based landslide susceptibility model. Section 4 illustrates and discusses the results from the exploratory analysis, as well as those related to the assessment, validation, and interpretation of the statistical models. Finally, Sect. 6 provides a summary of the most important findings. 

## **2 Study area and available data** 

### **2.1 Study area overview** 

The Aosta Valley is the smallest Italian region (3602 km<sup>2</sup> ), located in the northwestern Alps, bordering the AuvergneRhône (France) to the West, Valais (Switzerland) to the North, and Piedmont (Italy) to the East and South. The region is a vast Alpine valley, with an elevation range spanning from 300 m to over 4000 m above sea level (Fig. 1a), encompassing major peaks such as Mont Blanc, Monte Rosa, the Matterhorn, and Gran Paradiso. It includes the entire mountainous Dora Baltea River basin, receiving water from several tributaries to the north and south. 

```
1 3
```

**<mark>157</mark>** <mark>Page 4 of 26</mark> 

Stochastic Environmental Research and Risk Assessment (2026) 40:157 



The complex topography of the Aosta Valley, as well as its tendency to slope instability, is the result of a composite geological and geomorphological history. The Aosta Valley lies in the axial zone of the Western Alps, an area 

**Fig. 1** ( **a** ) Location and elevation map of the study area (Aosta Valley, Italy), elaborated in ArcGIS Pro from TINITALY/1.1. The black dots represent the shallow landslide inventory. ( **b** ) Geological framework for Aosta Valley, modified after De Giusti et al. (2003): 0-quaternary deposits; Elvetic Units (1-non differentiated sedimentary covers, 2-arenaceous-carbonaceous schists, 3-Mont Blanc granites, 4-pre-granitic basement); Ultra-elvetic (M. Chetif Units: 5-sedimentary cover, 6-porphiroids and micro-granites, 7-calc-schists, schists and limestones, 8-cargneules, limestones and dolomites); Outer Penninic (Sion-Courmayeur Zone: 9-flysch and conglomerates, 10-gypsum, cargneules, dolomites and Triassic limestones, 11-quarzites and conglomerates, 12-black schists and micaceous sandstones; Versoyen Zone: 13-prasinites, 14-serpentinites, 15- pelitic-arenaceous calcschists, 16-quartzose mica schists); Mid-Penninic (Piccolo San Bernardo Zone: 17- calc-schists and siliceous limestones; 18-coquinas, cargneules and dolomites; Outer Brianzonese: 19-cargneules, gypsum and dolomites, 20-quartzites and conglomerates, 21-subvulcanic meta-granites, 22-conglomerates, metapsammites and metapelites, 23-schists and micaceous sandstones, 24-mica schists and gneiss, 25-granotoid gneiss; Inner Brianzonese: 26-marbles, dark schists and breccias, 27-limestones and dolomites, 28-quarztites and silver schists, 29-meta-granitoids and augen gneiss, 30-metagranophyres, 31-mica schists and Ab-gneiss and schists); Inner Penninic (32-schists and meta-conglomerates, 33-meta-granites and augen gneiss, 34-pragneiss); Piemontese Zone (Combin and Zermatt-Saas Units: 35-calcschists, 36-meta-basalts, amphibolites and eclogites, 37-meta-gabbros, 38-serpentinites; Exotic Units: 39-differentiated Permo-Mesozoic successions, 40-non-ophiolitic calc-schists and breccias); Austroalpine (Upper non-eclogitic nappes: 41-mesozoic cover, 43-ortogneiss and paraschists, 44-mica schists, marbles, metabasites and pegmatite dikes, 45-metagranites, 46-gabbros; Lower eclogitic nappes: 47-eclogitic mica schists complex; Sesia Lanzo Zone: 48-Outer complex of fine-grained gneiss, 49-eclogitic mica schists complex, 50-kinzigitic complex); post-metamorphic magmatisms: 51-Lamprophiric dikes. **(c)** Representation of slope units (SUs) for Aosta Valley elaborated by Alvioli et al. (2020) 

formed by an imbricated stack of continental and oceanic units affected by Alpine collision and subduction processes (e.g., Ellero and Loprieno 2018; Fig. 1b). This tectonometamorphic pile records metamorphic conditions ranging from blueschist to eclogitic, with local ultra-high-pressure facies (Frey et al. 1999). From top to bottom, the Aosta Valley includes (Bistacchi et al. 2001): (i) the Austroalpine system, with pre-Alpine granitoids, paragneisses, granulites and schists of the Sesia-Lanzo Zone and several outliers in blueschist and eclogitic facies, (ii) the Piedmont Zone ophiolites, consisting of the Combin Zone (calcschists and mafic–ultramafic rocks, recording blueschist facies; Tartarotti et al. 2019) and the Zermatt-Saas Zone (serpentinised peridotites with a metasedimentary cover showing eclogitic imprint), and (iii) the Penninic continental nappes, from the high-pressure Monte Rosa, Arcesa-Brusson and Grand Paradiso units to the lower-pressure Houillère and Ruitor nappes (Ellero and Loprieno 2018), and the Valais flysch units. These geological units are structurally bounded by the southeastern-dipping Penninic front, which separates them from the Mont Blanc Helvetic basement, which consists of pre-Alpine amphibolite facies meta-granitoids and 

```
1 3
```

<mark>Page 5 of 26</mark> **<mark>157</mark>** 

Stochastic Environmental Research and Risk Assessment (2026) 40:157 

migmatites. Moreover, post-collisional tectonics and brittle deformation, particularly along the east-west Aosta-Ranzola fault system (e.g., Bistacchi et al. 2001), further complicates the structural configuration. 

The geomorphology of the region reflects the combined action of concomitant and consecutive glacial, fluvial, and gravitational processes. Pleistocene glaciations were the dominant factor in shaping its morphology, leaving widespread depositional and erosional landforms (e.g., Giardino et al. 2017). The region still hosts major glaciers (Bert et al. 2024), although they have undergone marked retreat since the Little Ice Age, accelerating in recent decades due to climate change (e.g., Viani et al. 2020). This retreat has significantly influenced slope stability, particularly through debuttressing effects (Giordan et al. 2018). Fluvial incision further modified the glacial landforms, depositing loose sediments into large alluvial and alluvial-gravitational fans that are eventually mobilised by recurrent meteorological events (Ratto et al. 2003). Regarding gravitational processes, they are widespread and act across multiple scales, from small rockfalls to deep-seated gravitational slope deformations (DSGSDs), contributing significantly to slope instability in the region. Due to its complex geological and geomorphological background, the Aosta Valley presents all types of slope instabilities, with shallow landslides and rockfalls dominating, followed by complex landslides and DSGSDs. This study focuses on shallow landslides, which account for almost 20% of those occurring in the regional territory (Giardino and Ratto 2007). 

Due to its complex physiography, the Aosta Valley is characterised by micro-climatic features. According to the Köppen-Geiger climate classification (Rubel et al. 2017), the region can be subdivided into four climate classes: (i) arid in the areas close to Aosta; (ii) warm temperature in the main valleys; (iii) moderate at mid altitudes; (iv) alpine in the highest areas. Most precipitation occurs at higher altitudes, where mean annual values range from ~ 750 to ~ 950 mm/yr, whereas precipitation is limited at lower altitudes (~ 550 mm/yr). The south-eastern and northwestern areas are characterised by annual precipitation up to 2500 mm/year, influenced by Mediterranean humid and Atlantic air masses, respectively (Ponziani et al. 2023). Winters are mostly characterised by snowfall, while summers are marked by convective activity that produces short-duration, high-intensity rainstorms. Temperature distribution is strongly correlated with elevation, showing a decrease of about 0.6 °C per 100 m increase in altitude (Centro Funzionale Regione Autonoma Valle d’Aosta 2024). 

Shallow landslide triggering factors are closely correlated with rainfall patterns, with prolonged, high-intensity events and snowmelt being the most common. Variations in rainfall and snowmelt regimes directly affect the magnitude, 

seasonality, and distribution of shallow landslides, as they depend on other climatic variables, such as temperature, which is increasing due to global warming (Camera et al. 2021). 

### **2.2 Mapping units** 

Defining mapping units aims to maximise within-unit homogeneity and between-unit heterogeneity (e.g., Alvioli et al. 2016; Erener and Düzgün 2012). In this study, we employed the SUs delineated by Alvioli et al. (2020) for the whole of Italy. These SUs were generated using the _r.slopeunits_ addon toolset available in GRASS and the European Digital Elevation Model (EU DEM; Alvioli et al. 2016; Fig. 1c), and are available for download as a national shapefile from the IRPI website (Istituto di Ricerca per la Protezione Idrogeologica; https:/ /geomor phology .irpi .cnr.it/. Then, we clipped this shapefile to the Aosta Valley regional boundaries (available at  h t t p s : / / w w w . i s t a t . i t / . . . / c o n fi  n i - d e l l e - u n i t a - a m m i n i s t r a t i v e - a - fi  n i - s t a t i s t i c i - a l - 1 - g e n n a i o - 2 0 1 8 - 2 / ) . The main limitations of using SUs concern: (i) the difficulty in tailoring their size to the known landslides’ distribution, which may lead a single SU to include both stable and unstable areas, thereby influencing the outcomes of the susceptibility analysis; and (ii) the potential mismatch between SU boundaries and geomorphological or land-use subdivisions that are relevant for assessing landslide susceptibility (Guzzetti et al. 2005). Nevertheless, several recent studies have successfully applied SUs in susceptibility analysis for shallow landslides (e.g., Ba et al. 2018; Liu et al. 2021). 

### **2.3 Landslide inventory** 

The dependent (response) variable in landslide susceptibility modelling is typically binary, indicating the presence or absence of landslides in each mapping unit (Lombardo et al. 2020). Past and present landslide distributions can be derived from inventory maps or catalogues (Bajni et al. 2022). The quality and completeness of these databases are crucial, as inaccuracies can bias susceptibility assessments (Van Den Eeckhaut & Hervás, 2012), making them the most critical component of susceptibility modelling (e.g., Tanyas and Lombardo 2020). In particular, landslide inventories are commonly affected by spatial and temporal biases, including the underrepresentation of small or old events, preferential detection in easily accessible or densely populated areas, and inconsistencies arising from heterogeneous mapping techniques. These issues can result in imbalanced and non-representative training datasets, ultimately affecting model performance and predictive reliability. Furthermore, the reliability of both landslide and non-landslide samples is critical, as misclassified or uncertain samples may introduce 

```
1 3
```

**<mark>157</mark>** <mark>Page 6 of 26</mark> 

Stochastic Environmental Research and Risk Assessment (2026) 40:157 

systematic errors in susceptibility models (Hong et al. 2024). To address this issue, some studies incorporate sample reliability into the modelling process (e.g., Hong et al. 2024), while others use visibility masks to define the areas where the model can be reliably trained (e.g., Bornaetxea et al. 2018; Knevels et al. 2020; Bajni et al. 2022). 

For this study, two point-based datasets were combined: the national IFFI inventory (Inventario dei Fenomeni Franosi in Italia – Italian Landslide Inventory; www.progettoiffi.isprambiente.it/) and the Regional Inventory of Aosta Valley (https:/ /catast odisses ti.pa rtout.it/), which includes photos of most recorded events. The IFFI database follows a standardised methodology based on aerial photo interpretation, field surveys, historical archives, and documentary sources (Trigila et al. 2007). The IFFI dataset for Aosta Valley, updated to 2017, contains 5812 events representing several kinematics (e.g., slides, rockfalls, flows, DSGSDs). The Regional Inventory integrates multiple data sources and contains 14,389 landslides classified according to 14 categories, updated to March 2024. For this work, we extracted only shallow landslides, yielding 2061 events from the IFFI dataset (i.e., slides, slow/rapid flows, diffused shallow landslide areas) and 127 events from the Regional Inventory dataset (i.e., diffused superficial landslide areas, slow flows, rapid flows, and slides). Both datasets present a spatial distribution concentrated along the main and tributary valleys, reflecting a potential survey bias. Field surveys are typically conducted along main pathways and forestry roads, meaning that landslides in remote areas are often underrepresented (Bajni et al. 2023). A comparison of the two inventories revealed partial overlap, with the regional dataset adding more recent (2017–2024) and a few isolated occurrences. Where overlap occurred, we retained records from the Regional Inventory in preference to those from IFFI, as we assume the latter were derived from the Regional Inventory. The merged inventory used in this study includes a total of 2512 shallow landslide events (Fig. 1a). Finally, we used the landslide points to obtain the binary response variable – SUs containing at least one shallow landslide were associated with one, otherwise with zero. 

### **2.4 Geo-environmental predictors** 

Following Di Napoli et al. (2021) and Alvioli et al. (2024), this study focused exclusively on geo-environmental and topographic predictors, excluding triggering factors such as heavy rainfall. The original SUs dataset derived from Alvioli et al. (2020) contained several topographic and morphometric predictors, such as elevation, slope, aspect, and curvature. Since these predictors strongly depend on DEMs’ quality and resolution, we adopted a multi-resolution approach, testing predictors derived from DEMs having 

different spatial resolutions. Specifically, we used elevation, profile curvature, planar curvature, and total curvature variables already available from the 25-m-resolution EU DEM, and computed the same predictors from the 10-m-resolution TINITALY/1.1 (Fig. 2a, b, c, d; Tarquini et al. 2023). We kept both, because higher DEM resolution does not necessarily give better accuracy in predicting landslide susceptibility than coarser ones (Rabby et al. 2020). In addition, we calculated the Terrain Ruggedness Index (TRI; Riley et al. 1999) from TINITALY/1.1, which provides an immediate and objective measure of terrain heterogeneity (Fig. 2e). All new predictors were generated in R (www.r-project.org) using the zonal statistics tool within the _terra_ package (Hijmans et al. 2025). 

Land use information was derived from two sources: (i) European Space Agency (ESA) WorldCover  (h t t p s : / / e s a - w o r l d c o v e r . o r g / e n ; Fig. 3a) and (ii) Land Cover RAVA 2022 (Regione Autonoma Valle d’Aosta – Autonomous Region of Aosta Valley, https:/ /geopor tale.re gione .vda.it/; Fig. 3b). The RAVA dataset provides detailed vegetation classes, distinguishing between broad-leaved and needle-leaved forests, unlike ESA WorldCover, which groups them as “trees”. Land cover influences slope stability, although its relationship remains ambiguous and complex to generalise: indeed, forests can enhance stability through root anchoring in some contexts (Carrara et al. 1991), but may also increase landslide risk due to their weight in adjacent areas (Carrara et al. 1995). To better capture this relationship, we distinguished between broad-leaved and needle-leaved forests. Additionally, we computed Euclidean distances from trees, sparse vegetation, built-up areas, and water bodies (Fig. 3c, d, e, f) using the _distance()_ function from the _terra_ R package (Hijmans et al. 2025), as proximity to these features can influence landslide susceptibility. Buildings can increase the soil weight by promoting instability and alter drainage systems by diverting water and accelerating erosion. Water bodies can erode the base of the slope, leading to instabilities. Additionally, soil near water can become saturated, decreasing its resistance to external solicitations. Finally, we calculated the density of each land-cover class within each SU from the RAVA 2022 map. 

To capture spatial dependency in the statistical model, we included the centroid coordinates of each SU as variables of a two-dimensional smooth function (constructed as a tensor-product of two marginal regression splines). This approach identifies spatial patterns in the distribution of environmental variables, such as landslides, meteorological variables, or toxin concentrations, by using their locations as input data (Stoner et al. 2023; Economou et al. 2023). The final set of predictors can be consulted in the Supplementary Materials. 

```
1 3
```

<mark>Page 7 of 26</mark> **<mark>157</mark>** 

Stochastic Environmental Research and Risk Assessment (2026) 40:157 



**Fig. 2 (a)** The TINITALY/1.1 has a resolution of 10 m and represents the DEM from which new geomorphological predictors were calculated in ArcGIS Pro: **(b)** planar curvature; **(c)** profile curvature; **(d)** 

total curvature; **(e** ) Terrain Ruggedness Index. TINITALY/1.1 was modified after Tarquini et al. (2023) because some inaccurate elevation values were found during the preliminary elaboration phase 

## **3 Methods** 

### **3.1 Variable selection** 

The methodology consists of three main steps. First, we built a methodological workflow to select the most significant geo-environmental predictors and investigate their relationship with shallow landslide initiation. This first step aims to select the most important predictors to account for in the susceptibility analysis. Second, we used the final set of predictors to build two susceptibility models, and we evaluated their statistical and physical significance. To explicitly consider spatial autocorrelation, one of the two models incorporates the tensor product of the SU centroid’s set of coordinates. Third, we compared the two models to evaluate the importance of explicitly considering spatial autocorrelation using a tensor-product smooth. We describe these steps in detail in the following sub-sections. We also present a flowchart summarising the overall methodological framework for clarity (Fig. 4). 

This first phase consisted of three main steps. First, we use a correlation matrix to explore pairwise relationships among predictors to identify potential multicollinearity. Second, we apply a both-way stepwise selection to derive an initial parsimonious subset of predictors. Third, we use a Random Forest classifier to assess variable importance, relying on permutation to evaluate predictor relevance. 

#### **3.1.1 Correlation matrix** 

Multicollinearity represents the non-independence between predictor variables. When two or more predictors in a statistical model are linear combinations of each other, they offer no additional information in predicting the response. We computed the correlation matrix for exploratory purposes, in order to assess the strength and direction of relationships among the variables and obtain an overall understanding of the correlated predictors. We normalised the predictors by performing the Z-score normalisation according to Eq. 1, ensuring comparability. 

```
1 3
```

**<mark>157</mark>** <mark>Page 8 of 26</mark> 

Stochastic Environmental Research and Risk Assessment (2026) 40:157 



**Fig. 3** ( **a** ) ESA World Cover showing the region divided into 10 land cover classes. ( **b** ) RAVA Soil Cover 2022, showing the regional territory divided into 15 land cover classes. From the ESA World Cover, 

four new predictors were computed using Euclidean Distance on ArcGIS Pro: ( **c** ) distance to bare/sparse vegetation; ( **d** ) distance to trees; ( **e** ) distance to built-up areas; ( **f** ) distance to water 

```
1 3
```

<mark>Page 9 of 26</mark> **<mark>157</mark>** 

Stochastic Environmental Research and Risk Assessment (2026) 40:157 



**Fig. 4** Flowchart illustrating the workflow for landslide susceptibility modelling, from the initial set of geo-environmental predictors through (1) multicollinearity assessment via a correlation matrix, (2) variable selection to reduce predictor redundancy, (3) GAM modelling, and (4) model validation, comparison, and spatial autocorrelation assessment 

_Z_ = _X − µ σ_ (1) 

In Eq. 1, _Z_ is the Z-score, _X_ is the data point, _µ_ is the data mean, and _σ_ is the data standard deviation. 

The correlation matrix was created in R using the _corrr_ package (Kuhn et al. 2025), where collinearity is computed with the Pearson method, and displayed using the _corrrplot_ package (Wei et al. 2024). The values in the matrix represent the strength (0–1) and direction (positive or negative) of the predictor associations. We sorted the predictors based on similarity, resulting in groups of highly correlated predictors, to identify clusters. 

In literature, fixed universal thresholds for correlation coefficients do not exist; however, commonly used guidelines can be consulted, depending on the domain and application (e.g., Overholser and Sowinski 2008; and references therein). We followed the correlation coefficients suggested by Koo and Li (2016) in the biomedical field and also adopted in environmental studies such as Agyekum et al. (2024): (i) values less than 0.50 indicate poor correlation, (ii) values between 0.50 and 0.75 indicate moderate correlation, (iii) values between 0.75 and 0.90 suggest strong correlation, and (iv) values greater than 0.90 suggest very strong correlation. Following Erener and Düzgün (2012), we identified and expected predictors showing an absolute correlation value greater than or equal to 0.70 to be excluded in the subsequent step (i.e., stepwise selection). 

#### **3.1.2 Stepwise selection** 

The next step involved performing a both-way stepwise selection, identifying the most important predictors among all considered. We implemented the _ols_step_both_p()_ function from the _olsrr_ R package (Hebbali 2024) to build a linear regression model by combining forward selection and backwards removal. Specifically, from a set of 58 candidate predictors, the model was built by adding and removing predictors based on their statistical significance ( _p-value_ ), using a stepwise approach, until no more variables were left to add or remove. The selected and randomly ordered predictors were then used to build the final linear model. Finally, the Variance Inflation Factor (VIF; Marquardt 1970) was used to measure multicollinearity among the resulting predictors and thus potentially exclude additional predictors. High VIFs indicate strong intercorrelations, while low VIFs correspond to weak correlations – after the model is fit, further complementing the original selection based on raw correlations. Following Montgomery et al. (2021), when predictors 

```
1 3
```

**<mark>157</mark>** <mark>Page 10 of 26</mark> 

Stochastic Environmental Research and Risk Assessment (2026) 40:157 

with VIF above 5 are present, the predictor with the highest VIF is removed, and the linear model is refitted to assess whether multicollinearity decreases. 

#### **3.1.3 Random forest classification** 

The final step in variable selection involved applying Random Forest (RF; Breiman 2001), a non-parametric supervised machine learning algorithm used for classification and regression. RF builds prediction rules from different types of predictor variables without assuming prior associations with the response (e.g., Probst et al. 2019). It consists of an ensemble of binary decision trees with three types of nodes: the root node (i.e., entire dataset, initial split), decision nodes (i.e., subsequent splits based on rules), and leaf nodes (i.e., final class or predicted value). The branches connect the nodes and represent the decision paths. Trees are trained on bootstrap samples of the dataset, while about one-third of the data – the Out-Of-Bag (OOB) samples – are used for internal validation. At each split, only a random subset of predictors is considered, which prevents overfitting (Breiman 2001; Catani et al. 2013; Touw et al. 2013). Given its random nature, a single decision tree does not give an accurate result. The strength of RF lies in mitigating this problem by aggregating the decision trees, which balances the source of errors (Taalab et al. 2018). Each tree casts an unweighted vote, and the majority vote determines the final class (Touw et al. 2013). RF needs several hyperparameters to be set, including the minimal node size, number of trees ( _ntree_ ), and number of predictors considered at each split ( _mtry_ ). Though default values often perform well, tuning can further improve accuracy (e.g., Camera et al. 2017; Probst et al. 2019). 

RF provides two main variable importance measures (Breiman 2001): Mean Decrease in Accuracy (MDA), based on OOB permutation tests, and Mean Decrease in Impurity (MDI), based on improvements in the splitting criterion. Both metrics identify the same relevant predictors but rank them differently: MDA evaluates accuracy loss after randomly shuffling predictor values, whereas MDI measures the reduction in Gini impurity across trees. Given that MDA is often regarded as more robust than MDI, particularly with respect to biases related to variable scale and tree structure (e.g., Loecher 2022), we based our analysis on the ranking of the most important variables as expressed by the MDA, taking care to remove negative and very low values (~ 0). 

Implementing RF classifier in the variable selection has several advantages (Cutler et al. 2007; RodriguezGaliano et al. 2012): (i) it gives a direct measure of predictors importance (i.e., MDA and MDI); (ii) it combines multiple single classifiers optimising the overall classification’s performance and minimising the noise posed by the 

single classifiers; (iii) it can deal with large datasets; (iv) it computes an internal unbiased estimate of the generalisation error (i.e., OOB error); (v) it is not computationally demanding. 

Here, we use RF classification as a screening tool to identify the most relevant predictors based on permutation importance. As a non-parametric method, RF allows us to assess predictor importance without imposing assumptions on the data, supporting the identification of robust predictors to be further evaluated within the GAM framework. We implemented this step of the analysis in R using the _randomForest_ package (Breiman et al. 2024). 

### **3.2 Susceptibility analysis** 

#### **3.2.1 Generalised additive model** 

We analysed the functional relationship between the shallow landslide inventory and geo-environmental predictors through a susceptibility model using a GAM, as introduced by Wood (2017). Unlike simple linear regression, which assumes linear predictor effects, GAMs allow non-linear relationships by estimating non-linear smooth functions directly from the data (Simpson 2018), while ensuring the amount of smoothness is optimally estimated. This makes them especially suitable for natural processes, such as landslides, that often display complex, non-linear behaviour. GAMs extend Generalised Linear Models by replacing parametric terms with smooth functions, thus combining flexibility with interpretability (Simpson 2018). In this study, we modelled the binary response variable (landslide presence/absence) through the logit link function of the conditional probability _p_ , the probability of landslide presence given the predictors _xj_ (Eq. 2). 



<!-- Start of picture text -->
p ( xj )<br>logit  ( xj ) = ln 1  − p  ( xj ) = ln ( odds ) (2)<br><!-- End of picture text -->

The _logit_ is the conventional link function used in logistic regression to characterise the probability of the event of interest (shallow landslide occurrence) with functions of the predictors _xj_ . In GAMs, these functions are assumed to be additive, non-linear, smooth functions _f (xj)_ , constructed using penalised regression splines (Eq. 3). 



<!-- Start of picture text -->
logit  ( xj ) =  f  ( xj ) (3)<br><!-- End of picture text -->

In GAMs, variable selection can be performed through several penalisation techniques (Wood 2017). In this study, we applied shrinkage smoothers, which introduce an additional penalty allowing smooth functions to shrink to zero when not significant. 

```
1 3
```

<mark>Page 11 of 26</mark> **<mark>157</mark>** 

Stochastic Environmental Research and Risk Assessment (2026) 40:157 

A common diagnostic issue is concurvity, the GAM analogue of multicollinearity. Concurvity values range from 0 (no redundancy) to 1 (complete overlap of smooth functions), and values above 0.8 may cause model instability (Camera et al. 2021). High concurvity undermines model stability and may indicate inconsistent variable selection (Wood 2017; Kovács 2024). In geomorphological modelling, GAMs have been widely adopted because they are less prone to overfitting than machine learning models, while retaining flexibility and interpretability (e.g., Petschko et al. 2012; Bajni et al. 2023). 

#### **3.2.2 Model optimisation and validation** 

We discarded a total of 1679 out of 2512 SUs because they were deemed unsuitable for this study. Specifically, we excluded 78 SUs showing depth to bedrock, bulk density, a weight% of sand, silt, and clay set to zero, as well as land cover classes corresponding to bare rock, permanent snow and ice, or water surfaces. Indeed, these attributes indicate a 



**Fig. 5 (a)** Main road network in the Aosta Valley, used to compute the distance of slope units from roads. **(b)** Boxplot of slope unit distances from the main road network. **(c)** Visibility mask generated using the upper whisker value (485 m). **(d)** Slope units with at least 70% of their area covered by the visibility mask, selected for model training to reduce inventory bias 

potential absence of soil cover, which is necessary to generate a shallow landslide. Furthermore, as recent studies have shown (Bornaetxea et al. 2018; Knevels et al. 2020; Bajni et al. 2022), the use of a visibility mask reduces survey bias by delineating the eligible area for training the model, thereby making the process more rigorous compared to approaches without such a mask. In this study, we generated the visibility mask in ArcGIS Pro (https://www.esri.com/) using the Visibility Tool (Fig. 5). We downloaded main roads from the OpenStreetMap database (Fig. 5a; h t t p s : / / w w w . o p e n s t r e e t m a p . o r g / # m a p = 1 0 / 4 5 . 7 2 7 8 / 7 . 1 3 0 1 ) , and we computed Euclidean distances from landslides to the road network. We defined the radius as the upper whisker value of the boxplot of the resulting minimum landslide-to-road distances (Fig. 5b). We retained only the SUs with at least 70% of their area covered by the visibility mask, resulting in the exclusion of 1601 SUs from the model training; however, we extended predictions to the entire study area (Fig. 5d). In the end, we calculated landslide counts per SU and converted to binary values (1 = presence, 0 = absence). 

We implemented the model in R using the _mgcv_ package (Wood 2025). We included the predictors retained after the variable selection workflow in the final models, with each predictor being represented by a thin plate regression spline to model their non-linear relationships with the response variable. We estimated the smoothing parameters ( _λ_ ) using the Restricted Maximum Likelihood (REML) method and excluded predictors weakly associated with the response through the GAM penalisation framework. Although penalisation can flatten or remove weak predictors, we also inspected the Component Smoothing Functions (CSFs) to identify any implausible or unstable relationships. We applied cut-offs to shrink the predictor distribution when the CSFs show large confidence intervals for the most extreme and least frequent values, and excluded the predictors still showing large uncertainty or poor interpretability. We incorporated spatial autocorrelation using a tensor-product smooth of the latitude and longitude of each SU’s centroid (ED50 / UTM 32 N, EPSG:23032), producing a bi-dimensional smooth with each coordinate having its own penalty parameter (Wood 2017). Although we previously analysed multicollinearity (Sect. 3.3.1), we also checked multi-concurvity among smooth terms. 

Model construction began with all the predictors retained after the variable selection workflow, progressively removing or adding predictors based on _p_ values, which must be lower than 0.05 to deem a predictor statistically significant. Indeed, the _p_ value quantifies the consistency between the results obtained in the analysis and the pure explanation for those results (Thisted 1998). We compared two model types: (i) one excluding spatial terms (i.e., tensor product of coordinates), and (ii) one including spatial terms. Within each 

```
1 3
```

**<mark>157</mark>** <mark>Page 12 of 26</mark> 

Stochastic Environmental Research and Risk Assessment (2026) 40:157 

type, we evaluated the models using deviance explained, R<sup>2</sup> , AIC, and BIC (Bayesian Information Criterion). Specifically, we performed an AIC-guided model selection: if the AIC difference between two models is lower than two, the simpler model is preferred; if greater than 3–10, the lower AIC model is chosen (Burnham and Anderson 2004). We analysed BIC to investigate the increase/decrease in complexity from one model to another, following the guidelines of Kass & Raftery (1995). 

Following Lombardo et al. (2020), we assessed model performance through a 10-repetition 10-fold cross-validation (CV), whereby in each repetition 10% of the dataset was randomly withheld for testing, and the remaining 90% was used to train the model. We carried out the CV using the _sperrorest_ R package (Brenning 2012). We applied both non-spatial and spatial partitioning strategies: non-spatial CV relied on random data partitioning, whereas spatial CV was based on k-means clustering of the spatial coordinates. Non-spatial (random) CV helps assess model robustness under random data splits, while spatial CV allows us to evaluate predictive performance under spatially structured data. We assessed the predictive power via the Area Under the Receiver Operating Characteristic Curve (AUROC). A SU classified as unstable results is a true positive when overlaid with a recorded landslide; otherwise, it is a true negative. According to Swets (1988), AUROC values classify model performance as: (i) non-informative (0.5), (ii) low accuracy (0.5–0.7), (iii) moderate accuracy (0.7–0.9), (iv) high accuracy (0.9–1.0), and (v) perfection (1.0). 

We evaluated the relevance of each predictor within the final models using the penalisation frequency, calculated as the percentage of CV runs with Effective Degrees of Freedom (EDF) lower than 0.70 (after Bajni et al. 2023), and the mean decrease in deviance explained (mDD%). The EDF corresponds to the number of degrees of freedom used by the smooths to adapt to the data: an EDF ≈ 1 indicates a linear effect, while an EDF > 1 indicates a non-linear effect. The REML algorithm penalises weak effects, reducing their EDF toward zero. 

For both final models, we generated and mapped susceptibility predictions over the entire study area. To facilitate interpretation, we subsequently reclassified the predicted probabilities into five equal-interval susceptibility classes. In addition to the direct prediction maps, we also computed and mapped: (i) the absolute difference between the two predictions, highlighting areas where the models diverge the most; (ii) the standard errors of predictions for both models, used to represent spatial uncertainty; (iii) the difference between their standard errors, which allows identification of areas where the inclusion of the spatial tensor reduces or increases predictive uncertainty. To assess spatial autocorrelation, we computed the Global Moran’s I statistic 

(Moran 1950) on the Pearson residuals of the predictions for both models. Specifically, we evaluated whether the spatial tensor removed, or at least minimised, residual spatial autocorrelation. We calculated the statistic using an inversedistance spatial weighting scheme, with a distance threshold set to cover 5% of the study area extent (radius of 7600 m). We carried out all post-processing and reclassification procedures in ArcGIS Pro, while we derived the predictions and uncertainty estimates in R. 

To evaluate how the susceptibility classes relate to actual landslide occurrence, we first produced contingency tables counting the number of landslides and the total number of SUs within each susceptibility class for both models. From these tables, we calculated landslide density as the ratio of the number of landslides to the total number of SUs in each class, representing the conditional probability of a landslide occurring given that a SU belongs to a particular susceptibility class. We represented the resulting densities as bar charts, allowing a direct comparison between models and between training and testing subsets. This approach provides an intuitive assessment of model consistency, since we expect higher susceptibility classes to show proportionally higher landslide densities. 

We evaluated the predictive calibration of both models using reliability diagrams and calibration curves. We evaluated calibration by grouping the predicted probabilities into 10 bins and comparing the mean predicted probability in each bin with the observed landslide frequency. We plotted the resulting calibration curve against the 1:1 diagonal, which represents perfect calibration. Deviations from the diagonal indicate systematic overconfidence (above the line) or underconfidence (below the line). In the reliability diagrams, the discrepancy between confidence and accuracy is highlighted by the grey gaps where the bars representing observed accuracy separate from – or overlap with – the 1:1 reference line. We complemented this graphical information with quantitative metrics, including the Brier score (Brier 1950), scaled Brier score, Expected Calibration Error (ECE), and Maximum Calibration Error (MCE), as well as calibration intercept and slope. Together, these indicators provide a comprehensive assessment of how well the predicted probabilities reflect actual event frequencies. 

## **4 Results and discussion** 

### **4.1 Variable selection** 

Figure 6 shows the results of the correlation analysis, with the predictors sorted based on similarity. Several clusters emerge, showing both positive and negative correlations. 

```
1 3
```

<mark>Page 13 of 26</mark> **<mark>157</mark>** 

Stochastic Environmental Research and Risk Assessment (2026) 40:157 



**Fig. 6** Correlation matrix of the initial set of 58 predictors, where blue dots indicate a positive correlation and red dots a negative correlation. The matrix was created using the ggplot R package, and the use of 

“order = hclust” allows us to identify clusters of correlated predictors. Both the mean (mn) and standard deviation (sd) have been considered 

Table 1 synthesises the predictors with a correlation coefficient greater than 0.70 

The predictors summarised in Table 1 are directly or indirectly related to terrain morphology, indicating that many of them capture overlapping aspects of local spatial variability. For instance, the mean and standard deviation of elevation extracted from the 25-m-resolution EU DEM (i.e., elev_mn and elev_sd) are almost perfectly correlated with the corresponding values derived from the 10-m-resolution TINITALY/1.1 (i.e., DEM_mn and DEM_sd; correlation ≈ 1). This suggests that higher DEM spatial resolution does not substantially alter the large-scale topographic information 

captured by the predictors. Similarly, mean elevation is positively correlated with the mean density of bare rock (i.e., LC10_dens) and the mean distance from built-up areas (BUp_dst_mn), and negatively correlated with the mean depth to bedrock (BDRICM_mn) and the mean percentage of clay particles (CLYPPT_mn). This pattern is consistent with expectations, as bare rock exposure and distance from inhabited areas tend to increase with elevation, while depth to bedrock and the proportion of clay particles (and soils in general) typically decrease. We did not exclude any predictor after constructing the correlation matrix, as it serves only an exploratory purpose. 

```
1 3
```

**<mark>157</mark>** <mark>Page 14 of 26</mark> 

Stochastic Environmental Research and Risk Assessment (2026) 40:157 

**Table 1** Pairs of correlated predictors with an absolute correlation coefficient greater than 0.70 

|Predictorpairs w|ith Correlation > 0.7|0||
|---|---|---|---|
|Based on the corr|elation matrix of 58|predictors||
|Predictor 1|Predictor 2|Correlation|Correlation|
|DEM_mn|elev_mn|1.000|1.000|
|DEM_sd|elev_sd|0.999|0.999|
|ttcv10_sd|plcv10_sd|0.980|0.980|
|TRI_mn|slope_mn|0.956|0.956|
|DEM_mn|BDRICM_mn|− 0.882|0.882|
|BDRICM_mn|elev_mn|− 0.882|0.882|
|plcv10_sd|TRI_mn|0.825|0.825|
|SNDPPT_sd|CLYPPT_sd|0.823|0.823|
|prcv25_mn|plcv25_mn|− 0.806|0.806|
|ttcv10_sd|TRI_mn|0.800|0.800|
|TRI_mn|prcv25_sd|0.797|0.797|
|BSV_dst_sd|BSV_dst_mn|0.789|0.789|
|DEM_mn|CLYPPT_mn|− 0.786|0.786|
|CLYPPT_mn|elev_mn|− 0.785|0.785|
|CLYPPT_mn|BDRICM_mn|0.782|0.782|
|TRI_sd|slope_sd|0.780|0.780|
|BUp_dst_mn|BDRICM_mn|− 0.763|0.763|
|TRI_sd|TRI_mn|0.754|0.754|
|SNDPPT_mn|CLYPPT_mn|− 0.754|0.754|
|DEM_mn|BUp_dst_mn|0.750|0.750|
|TRI_mn|twi_mn|− 0.749|0.749|
|BUp_dst_mn|elev_mn|0.748|0.748|
|ttcv10_sd|prcv10_sd|0.745|0.745|
|twi_mn|slope_mn|− 0.735|0.735|
|SLTPPT_mn|BLDFIE_mn|0.723|0.723|
|ttcv10_sd|prcv25_sd|0.719|0.719|
|prcv10_mn|plcv25_mn|0.718|0.718|
|LC10_dens|BDRICM_mn|− 0.717|0.717|
|plcv10_sd|prcv25_sd|0.717|0.717|
|DEM_mn|LC10_dens|0.717|0.717|
|LC12_dens|Tr_dist_mn|0.716|0.716|
|LC10_dens|BUp_dest_mn|0.715|0.715|
|LC10_dens|BUp_dst_mn|0.712|0.712|
|plcv10_sd|slope_mn|0.708|0.708|
|Tr_dst_mn|BUp_dst_mn|0.700|0.700|



**Table 2** The 14 predictors that emerged from the both-way stepwise selection and entered the importance analysis in Random Forest (RF) 

|Predictor names|Description|
|---|---|
|slope_mn|Slope mean|
|nthns_mn|Northness mean|
|easns_mn|Eastness mean|
|elev_sd|Elevation SD|
|twi_sd|TWI SD|
|CLYPPT_mn|Clay weight% mean|
|area|Area|
|Wtr_dst_mn|Distance to water bodies mean|
|BUp_dst_mn|Distance to built-up areas mean|
|BUp_dst_sd|Distance to built-up areas SD|
|LC6_dens|LC6 (needle-leaved forests) density|
|LC7_dens|LC7 (mixed forests and heaths) density|
|LC13_dens|LC13 (water courses) density|
|plcv10_sd|Planar curvature SD(10-m-resolution)|



In the actual first step of variable selection, the both-way stepwise procedure retained 15 predictors in the final model. The final model was statistically significant (F = 29.18, _p_ < 0.001) and explained approximately 35% of the variance (R<sup>2</sup> = 0.35, Adj. R<sup>2</sup> = 0.34). Model diagnostics indicated acceptable predictive performance (RMSE = 0.381, MAE = 0.317) and no evidence of overfitting (R<sup>2</sup> = 0.35; R<sup>2</sup> pred<sup>= 0.32).</sup> 

Among the 15 predictors selected by the stepwise regression, TRI_mn and slope_mn show VIFs way greater than 5, of ⁓28.31 and ⁓22.16, respectively, which suggests their multicollinearity with some other predictors. By removing TRI_mn, with the highest VIF, the VIF of slope_mn dropped to ⁓3.30, indicating a strong correlation between the two, and the VIF of the remaining ones slightly decreased. This step retained 14 predictors (Table 2), which we used as inputs to the RF for importance ranking. 

The MDA bar plot (Fig. 7) highlights the importance of all 14 predictors, with values ranging from − 0.633 to 11.037. Based on their importance value, the predictors can be grouped into four main categories: (i) predictors showing 

**Fig. 7** Barplots of the Mean Decrease Accuracy (MDA) values for the predictors resulting from the previous forward and backward stepwise selection. Two predictors (easns_mn and twi_sd) have extremely low importance values (~ 0 or below), thus they were removed from further analysis 



```
1 3
```

<mark>Page 15 of 26</mark> **<mark>157</mark>** 

Stochastic Environmental Research and Risk Assessment (2026) 40:157 

**Table 3** Final set of predictors resulting from variable selection, comprising 12 predictors that primarily describe morphological, soil, and land-cover characteristics in the Aosta Valley 

|Predictor name|Description|
|---|---|
|area|Slope unit areas|
|BUp_dst_mn|Mean distance to built-up areas|
|elev_sd|Standard deviation of elevation|
|LC7_dens|Density of mixed forests and heaths (LC7)|
|CLYPPT_mn|Mean percentage of clay particles|
|LC6_dens|Density of needle-leaved forests (LC6)|
|nthns_mn|Mean northness|
|LC13_dens|Density of water courses (LC13)|
|plcv10_sd|Standard deviation of planar curvature based<br>on the 10-m-resolution TINITALY/1.1|
|BUp_dst_sd|Standard deviation of the distance to built-<br>up areas|
|slope_mn|Mean slope|
|Wtr_dst_mn|Mean distance to water courses|



relatively high importance values (~ 11 to ~ 8); (ii) predictors exhibiting medium importance values (~ 6 to ~ 4); (iii) predictors displaying relatively low importance values (~ 3 to ~ 1); and (iv) predictors having extremely low importance values (~ 0 or below). We removed the predictors belonging 

to the fourth category from further analysis. Forest density has an impact on the occurrence of shallow landslides, with the density of mixed forests and heaths (i.e., LC7_dens) and that of needle-leaved forests (i.e., LC6_dens) showing moderately high importance values. Table 3 shows the final set of predictors resulting from the variable selection workflow, comprising 12 predictors that primarily describe morphological, soil, and land-cover characteristics of the study area. Nearly all predictors exhibiting high correlation in Table 1 were removed by the end of the variable selection procedure. The only exception concerns the pair composed of the mean slope and the standard deviation of planar curvature at 10-m resolution. 

### **4.2 Susceptibility analysis through GAM** 

We first evaluated the contribution of the 12 predictors retained after the variable selection workflow by examining their CSFs. In Fig. 8, the black curve represents the final fitted function, while the indigo band describes the associated confidence interval. Penalisation led to the exclusion of the mean percentage of clay particles (CLYPPT_mn), the 

**Fig. 8** The Component Smoothing Functions (CSF) of the predictors selected by Random Forest (RF) classification and included into the models, after the cut-off. The black line is the final CSF, while the indigo area is the confidence interval. LC7 refers to mixed forests and heaths, LC6 to needle-leaved forests, and LC13 to water 



```
1 3
```

**<mark>157</mark>** <mark>Page 16 of 26</mark> 

Stochastic Environmental Research and Risk Assessment (2026) 40:157 

density of needle-leaved forests (LC6_dens), and the standard deviation of the distance from built-up areas (BUp_ dst_sd), all characterised by flat CSFs. We also excluded the density of watercourses (LC13_dens), as its CSF could not be meaningfully interpreted and was penalised by the model beyond the cut-offs. Among the predictors of model_B, we retained both mean slope and the standard deviation of planar curvature at 10-m resolution despite their relatively high correlation (≈ 0.71), as models excluding either or both variables exhibited reduced performance (e.g., lower R<sup>2</sup> and explained deviance, and higher AIC). 

As introduced in Sect. 3, we developed two model families: one including a tensor-product smooth for spatial coordinates, and one without it. Based on R<sup>2</sup> , explained deviance, AIC, and BIC (Table 4), we selected model_B and model_A as the best-performing models within their respective families. 

Both final models are statistically significant, with all smooth terms contributing meaningfully to the model fit ( _p_ < 0.05). In model_A, the adjusted R<sup>2</sup> is 0.39 and the explained deviance 35.9%, whereas in model_B, which includes the spatial tensor-product smooth, these values increase slightly to 0.42 and 39.0%, respectively. This, together with the decrease in AIC (from 724.5 to 714.2), suggests that incorporating the spatial tensor slightly improves model fit and predictive capacity. However, BIC increased from 825.5 to 869.0, indicating greater model complexity. Thus, although the model including the tensor-product smooth provides a better fit, it does so at the expense of parsimony and transferability. 

In model_A, the standard deviation of elevation is the most influential predictor (mDD% ≈ 30%), followed by mean distance from built-up areas (mDD% ≈ 9%); all remaining predictors contribute less than 5%. In contrast, 

in model_B, the mean distance from built-up areas becomes dominant (mDD% ≈ 37%), followed by SU area (mDD% ≈ 16%), while the other predictors show contributions between ~ 8% and ~ 12%. Notably, the importance of the standard deviation of elevation decreases in model_B, suggesting that some of the spatial variability previously attributed to elevation is instead captured by the spatial tensor. Concurvity is generally low in both models (0.14–0.77). The highest values refer to topographic predictors: standard deviation of elevation and mean slope in both models, and standard deviation of planar curvature in model_B. Importantly, concurvity stays nearly identical between model_A and model_B, indicating that the spatial tensor does not introduce additional multicollinearity among predictors. 

The CSF for the SU area increases steeply for small SUs (< 2 km<sup>2</sup> ) and gradually levels off for larger ones, indicating a positive relationship between SU size and landslide presence. Indeed, the greater the area, the greater the probability of occurrence. The CSF for mean distance from builtup areas shows the opposite pattern: landslide likelihood decreases sharply at short distances (< 2 km) and approaches zero at greater distances. This is plausible, as both urbanised areas and shallow-landslide processes are typically associated with soil cover, increasing the probability of landslide occurrence. Furthermore, urban activities can alter near-surface conditions in ways that favour the development of shallow landslides in proximity to built-up areas. For instance, road-cut constructions may steepen lower slope segments, modify surface and subsurface drainage, and increase pore pressure (e.g., Rohan et al. 2023), thereby potentially enhancing slope instability. Additionally, urbanisation often involves increased soil sealing, which reduces water infiltration, thereby increasing the surface water accumulation. Johnston et al. (2021) demonstrated that landslide hazard 

**Table 4** Model_A and model_B summaries along with AIC and BIC values, mean Decrease in Deviance explained (mDD%), concurvity values, and penalisation frequency during spatial (s) and non-spatial (ns) cross-validation (CV) 

|Model ID|Adj. R<sup>2</sup>|Deviance explained [%]|AIC|BIC|mDD%|Concurvity|Predictors|Penalisatio<br>frequency|n|
|---|---|---|---|---|---|---|---|---|---|
|||||||||nsCV|sCV|
|model_A|0.39|35.9|724.5|825.5|4.5|0.35|area|0.0|0.0|
||||||8.6|0.30|BUp_dst_mn|0.0|0.0|
||||||29.5|0.63|elev_sd|0.2|1.2|
||||||2.5|0.18|LC7_dens|0.4|0.0|
||||||1.5|0.22|nthns_mn|6.0|6.2|
||||||0.7|0.69|slope_mn|0.4|0.0|
||||||0.4|0.23|Wtr_dst_mn|0.0|0.0|
|model_B|0.42|39.0|714.2|869.0|12.0|0.14|te (x1,y1)|0.0|0.0|
||||||16.1|0.36|area|0.0|0.0|
||||||37.0|0.43|BUp_dst_mn|0.0|0.0|
||||||10.0|0.67|elev_sd|1.0|1.8|
||||||8.9|0.60|plcv10_sd|1.6|0.8|
||||||8.1|0.77|slope_mn|0.4|1.0|
||||||7.9|0.36|Wtr_dst_mn|0.2|1.0|



```
1 3
```

<mark>Page 17 of 26</mark> **<mark>157</mark>** 

Stochastic Environmental Research and Risk Assessment (2026) 40:157 

is significantly more sensitive to precipitation in urbanised areas than in non-urbanised ones, a pattern that could extend to landslide susceptibility. The CSFs for elevation (elev_sd) and planar curvature variability (plcv10_sd) show variable yet overall increasing trends, suggesting that landslide occurrence increases with greater topographic complexity. The standard deviation of elevation is often identified as a significant explanatory predictor in susceptibility models (e.g., Amato et al. 2021), as is the standard deviation of planar curvature (e.g., Loche, Lombardo, et al., 2022). Terrain exhibiting high roughness may promote water accumulation in irregular or concave sections of the slopes (Schlögl et al. 2025). High roughness may also reflect areas affected by previous slope instability, and the presence of past landslides can increase susceptibility to subsequent landsliding (Samia et al. 2018). The density of mixed forests and heaths (LC7_dens) shows a slightly increasing trend, suggesting that landslides may be more likely to occur where this landcover class is prevalent. This association may reflect the tendency of mixed forests and heathlands to occur on soil-mantled lower- to mid-slope positions (Fig. 3b), where soil depth, moisture availability (due to greater water accumulation during rainfall events), and weathering processes are generally greater. In addition, the strength of root-soil cohesion depends on several factors, such as species, root architecture, density, depth, and soil-root bonding, all characterised by high spatial and temporal variability (Masi et al. 2021). Thus, the coexistence of different vegetation types may lead to spatial variability in root-soil cohesion, which could locally reduce slope stability. Mean northness (nthns_ mn) shows a very weak inverse relationship, indicating a slightly higher propensity for shallow landslides to occur on south-facing slopes. Several studies confirm this result, relating it to weathering (due to high temperatures), intense wetting and drying cycles (due to high solar radiation), or locally greater root strength on north-facing slopes (e.g., McGuire et al. 2016; Piacentini et al. 2012). Mean slope displays an M-shaped relationship, with peaks near 15° and 30° and a minimum around 22°. As summarised by Yu et al. (2017), most shallow landslides occur on slopes between 20° and 40°. Slopes steeper than 45° experience fewer shallow landslides due to limited soil cover, possibly because erosive processes dominate over gravitational forces, whereas slopes below 20° are less susceptible because their gradients are too low to promote slope failure. Silva et al. (2023) confirmed these results by classifying slopes as follows: (i) 0°–10° as areas with potential for deposition; (ii) 10°–20° as low landslide potential; (iii) 20°–30° as medium landslide potential; (iv) 30°–45° as high landslide potential; and (v) slopes greater than 45°, characterised by thin soils, as having the lowest potential for shallow landslides. This justifies the observed increase in landslide occurrence between 22° 

and 30°. Conversely, the increase in landslide occurrence to 15° and the following decrease to 22° is more complex to explain. This anomaly could also be influenced by the SU averaging, whereby the mean slope of a SU may be substantially lower than the local slope at the actual initiation zone. Finally, the CSF for distance to watercourses shows a weak non-linear pattern, with a slight decrease followed by stabilisation. Watercourses influence slope stability in two main ways: (i) by eroding and undercutting the slope, which may trigger failure (Rohan et al. 2023); and (ii) by increasing local soil moisture near streams and water bodies, thereby decreasing soil resistance to external solicitations (e.g., Halter et al. 2025). 

Table 4 also reports penalisation frequencies under spatial and non-spatial cross-validation (CV), while Fig. 9 illustrates the variability of mDD% and EDF. In model_A, mean northness is the most frequently penalised predictor (~ 6%). In model_B, the standard deviation of elevation and that of planar curvature are penalised most often (~ 2%) in spatial and non-spatial CV, respectively. The mDD% boxplots show comparable explanatory capacity between models, though model_A displays greater dispersion than model_B. In both models, mDD% changes only slightly when switching from non-spatial to spatial CV. Mean distance from built-up areas remains the most relevant predictor, followed by SU area, and most boxplots show only a minimal effect on deviance explained. In model_B, the standard deviation of elevation shows a large mDD% variability from non-spatial to spatial CV, suggesting the idea that terrain heterogeneity becomes more influential when training data are spatially clustered. 

The EDF distributions further clarify the behaviour of the two models: model_A shows wider dispersion and more outliers than model_B, suggesting greater variability in smoothness across folds. Conversely, model_B exhibits more constrained EDF distributions than model_A, indicating a more stable model structure. When switching from nonspatial to spatial CV, the EDFs tend to become slightly more constrained in both models. Most predictors in model_A, and the majority in model_B, have EDF < 5, while the tensor product of the SU coordinates consistently exhibits the highest EDF, reflecting the flexibility required to capture spatial interactions. This effect becomes more pronounced under spatial CV in comparison to non-spatial CV. Because spatial coordinates correspond to SU centroids, they may not fully represent the true spatial distribution of occurrences, especially in large SUs. Model_B shows overall more compact distributions of both mDD% and EDF across all folds than model_A, suggesting its structure is more stable and less sensitive to training partitioning than model_A. 

Figure 10 presents the boxplots of AUROC values for training and testing subsets obtained from non-spatial and spatial CV. Overall, AUROC values are high (> 0.85), 

```
1 3
```

**<mark>157</mark>** <mark>Page 18 of 26</mark> 

Stochastic Environmental Research and Risk Assessment (2026) 40:157 



```
1 3
```

<mark>Page 19 of 26</mark> **<mark>157</mark>** 

Stochastic Environmental Research and Risk Assessment (2026) 40:157 

**Fig. 9** Predictors mean Decrease in Deviance explained (mDD%) and Effective Degrees of Freedom (EDF) for model_A ( **a** , **c** , **e** , **g** ) and model_B ( **b** , **d** , **f** , **h** ). CV stands for cross-validation 

indicating good model discrimination. Training performance is consistently high and stable, with median AUROC values of 0.877 for model_A under both non-spatial and spatial CV, and 0.891 and 0.890 for model_B under nonspatial and spatial CV, respectively. The slightly higher training AUROC for model_B in comparison to model_A suggests that it may capture the local spatial structure of the data more effectively through the inclusion of the spatial tensor. Nevertheless, this improvement may partly reflect the model’s sensitivity to spatial autocorrelation. As a result, a fraction of the predictive performance may be due to spatial proximity between training and testing samples rather than to strictly generalisable predictor-response relationships. As expected, testing AUROCs are lower than their training counterparts and display wider distributions, with median values of 0.855 and 0.854 for model_A under nonspatial and spatial CV, and 0.859 and 0.856 for model_B under non-spatial and spatial CV, respectively. Across both models, spatial CV resulted in a slightly narrower distribution of testing AUROC values compared to non-spatial CV, indicating lower variability in predictive performance across spatial folds. In contrast, the greater variability observed in testing AUROC under non-spatial CV could reflect sensitivity to the random partitioning of spatially autocorrelated observations between training and testing subsets. Under non-spatial CV, model_B exhibits a slightly higher testing AUROC than model_A, indicating improved predictive performance when spatial proximity between training and testing samples is preserved. However, under spatial CV, the difference between models decreases, indicating that the inclusion of the spatial tensor in model_B does not lead to substantially improved spatial generalisation once spatial dependence is explicitly accounted for. 

A comparison with the study by Fang et al. (2025) provides a useful, albeit not fully equivalent, benchmark. In their work, the authors report ROC–AUC values of approximately 0.93 for the GAM-DS model, which integrates continuous spatial covariates with discrete spatial dependencies, evaluated through 10-fold cross-validation on general landslide occurrences. In contrast, the present study focuses specifically on shallow landslides, which are driven by more localised processes (e.g., rainfall infiltration and near-surface soil properties) and may therefore exhibit different levels of predictability. It is also important to consider differences in validation design when interpreting performance. While Fang et al. (2025) rely on a standard cross-validation scheme, this study employs a 10-repetition 10-fold cross-validation framework using the _sperrorest_ approach, including both non-spatial and spatial strategies. 

Overall, although the reported AUC values are broadly comparable with those in the literature, differences in landslide type and validation strategy suggest that such comparisons should be interpreted qualitatively rather than as a direct comparison of model performance. 

We used both models to generate susceptibility maps for shallow landslides across the entire Aosta Valley (Fig. 11a, b). Equal-interval reclassification into five classes allowed the calculation of SU percentages per class (Table 5). The lowest class (0.0–0.2) dominates (> 50% of SUs) and is concentrated at high elevations characterised by bare rock, ice, and snow. The mid-low class (0.2–0.4) accounts for ~ 15–16% of SUs and is also located at high elevations. The medium class (0.4–0.6) covers ~ 11–14% of SUs and is more uniformly distributed. The mid-high class (0.6–0.8; ~10.5%) and highest class (0.8–1.0; ~7–7.5%) are concentrated along the main and lateral valleys, where vulnerable elements such as roads and settlements are present. Although the two models produce similar susceptibility class proportions, their spatial distributions differ. To better highlight these differences, the absolute difference between model_A and model_B was mapped (Fig. 11c). Differences range from ~ 0.0 to 0.6, with the greatest differences located in: (i) the north-western portion of the Aosta Valley, northeast of Courmayeur, (ii) the south-eastern part of the region, close to the lower Champorcher valley, (iii) a portion to south-east of Aosta and Nus, and (iv) the south-western part of the region, along Valgrinsenche, Rhemes valley and Valsavarenche. 

Model_B shows higher standard errors than model_A, reaching values of up to 0.6 in seven SUs and 0.3 in many others (Fig. 11d, e). The difference map of standard errors indicates that the spatial tensor does not uniformly improve prediction confidence across the study area. Negative differences (blue SUs in Fig. 11f) identify locations where Model_B produces lower standard errors than Model_A, suggesting that the spatial component captures meaningful spatial structure and provides more stable estimates. These areas form several spatial clusters, suggesting that neighbouring locations share similar geomorphological conditions that the spatial tensor is able to exploit. Conversely, positive differences (red SUs in Fig. 11f) mark regions where model_B yields higher uncertainty. This may be associated with areas characterised by strong local variability, irregular data density, or abrupt changes in terrain properties, where the spatial tensor introduces additional complexity without reducing uncertainty. Overall, the map highlights that the spatial tensor improves precision only in certain portions of the territory, revealing a spatially selective benefit rather than a global reduction in uncertainty. This supports the conclusion that model_B still encounters limitations in terms of spatial generalisation. 

```
1 3
```

**<mark>157</mark>** <mark>Page 20 of 26</mark> 

Stochastic Environmental Research and Risk Assessment (2026) 40:157 



**Fig. 10** Training and testing AUROC (Area Under the Receiver Operating Characteristic curve) values for model_A (left) and model_B (right). nsCV denotes non-spatial cross-validation, while sCV denotes spatial cross-validation 

Consistent with these observations, a statistical assessment of spatial autocorrelation further confirms the role of the spatial tensor. Model_A exhibits a Global Moran’s I of 0.04 ( _p-value_ = 0.00; _z-score_ = 1.13), indicating a weak but statistically significant presence of spatial autocorrelation in the prediction residuals. This corresponds to less than 1% likelihood that the observed clustered pattern arose by chance. In contrast, model_B shows a reduction in Moran’s I to 0.01, which is not statistically significant ( _p-value_ = 0.28; _z-score_ = 1.08), indicating that its residual pattern does not differ significantly from randomness. Although spatial autocorrelation in model_A is relatively low, model_B exhibits no significant residual spatial autocorrelation. Taken together with the improved performance metrics (AUROC, R<sup>2</sup> , deviance explained, and AIC) reported in previous sections, these results indicate that the inclusion of the spatial tensor allows for an effective representation of spatial structure and contributes to improved model performance and more reliable predictions. 

Figure 12 displays landslide density per susceptibility class for training and testing subsets, based on contingency tables. For each susceptibility class, we calculated landslide density as the proportion of landslide occurrences relative to the total number of observations within that class. The comparative analysis of landslide density across susceptibility classes for both models reveals consistent trends across classes in both training and testing subsets, confirming the validity of the classification framework. Model_B generally exhibits slightly higher values than model_A, particularly in the highest susceptibility class, suggesting an improved identification of unstable conditions. However, model_A demonstrates comparable performance, generally underestimating the highest and the lowest classes. Differences between the models are although modest, typically within 2–3%. These results indicate that both models are able to capture the general susceptibility to landslides in the study area with reasonable accuracy. 

**Fig. 11** Maps of susceptibility to shallow landslides for Aosta Valley, generated from **(a)** model_A and **(b)** model_B. Susceptibility classes were generated through the equal interval classification method. Predictions exhibit distinct spatial distribution, highlighted by the map of their absolute difference **(c)** . Maps of prediction residual errors for **(d)** model_A and **(e)** model_B, along with **(f)** their actual difference 

Figure 13 presents a calibration performance of the two models, and their relative reliability diagrams, whereas Table 6 shows the calibration metrics. Both models exhibit reasonable alignment with the diagonal: model_A shows a good fit with the bisector at the extremes of the confidence interval, while model_B aligns more closely to the bisector than model_A in the mid-to-high confidence range. Although both models display a mix of positive and negative calibration gaps across bins, indicating alternating patterns of overconfidence and underconfidence, model_A exhibits narrower gaps compared to model_B. Quantitative metrics confirm these patterns: model_A achieves a slightly lower Brier score (0.124 vs 0.125) and a higher scaled Brier score (0.385 vs 0.380) than model_B, suggesting marginally better overall probabilistic accuracy and discrimination. Furthermore, model_B shows slightly higher Expected Calibration Error (ECE = 0.023 vs 0.018) and Maximum Calibration Error (MCE = 0.049 vs 0.045), reflecting larger deviations between predicted confidence and observed accuracy than model_A. Model_B has an intercept closer to zero (–0.007 vs − 0.040), indicating less systematic bias. However, its slope is lower than that of model_A (0.899 vs 0.950), suggesting a tendency toward underconfident predictions; i.e., model_B tends to produce probability estimates that are more conservative compared to model_A. 

## **5 Conclusions** 

This work developed and evaluated two statistical models for assessing regional shallow landslide susceptibility at the SU level in the Aosta Valley. Initially, we considered a set of 58 morphometric, pedological, and land cover predictors. The combined use of correlation analysis, stepwise selection, RF classification, and GAM penalisation led to a final set of eight predictors, describing terrain morphology, soil properties, anthropogenic proximity, and vegetation cover. We incorporated these predictors into two GAM-based model families, one including a tensor-product smooth for spatial coordinates (model_B) and one not including it (model_A). Both models achieved comparable performance, explaining ⁓36–39% (model_A and model_B, respectively) of deviance and obtaining AUROC values above 0.85 under spatial and non-spatial CV. Model_B showed slightly higher adjusted R<sup>2</sup> , lower AIC, and marginally better discrimination in training than model_A, indicating that the spatial 

```
1 3
```

<mark>Page 21 of 26</mark> **<mark>157</mark>** 

Stochastic Environmental Research and Risk Assessment (2026) 40:157 



```
1 3
```

**<mark>157</mark>** <mark>Page 22 of 26</mark> 

Stochastic Environmental Research and Risk Assessment (2026) 40:157 

**Table 5** Counts and percentages of slope units in each susceptibility class for model_A and model_B 

|SU distri|butionper|susceptibilityclass|||
|---|---|---|---|---|
||model_|A|model_|B|
|Class|Count|Percentage [%]|Count|Percentage [%]|
|0.0–0.2|1342|53.42|1376|54.78|
|0.2–0.4|380|15.13|396|15.76|
|0.4–0.6|349|13.89|287|11.43|
|0.6–0.8|263|10.47|265|10.55|
|0.8–1.0|178|7.09|188|7.48|



tensor captures part of the underlying spatial dependence. However, BIC increased substantially, and improvements in testing performance were modest, suggesting that higher model complexity does not translate into consistent gains in spatial generalisation. 

As expected, the analysis confirmed consistent geomorphological control. Susceptibility increased with SU area and indicators of terrain heterogeneity (standard deviation of elevation and planar curvature) and decreased with distance to built-up areas. Susceptibility mapping showed consistent patterns, with the highest susceptibility concentrated along valley bottoms and major hydrographic networks, corresponding to areas of thicker soil covers and stronger hydrological influence, and low to very low susceptibility at high elevations where rock outcrops and poorly developed soil cover dominate. Although both models showed comparable susceptibility patterns, the spatial distribution of predicted susceptibility differed between the two models. Indeed, standard error maps confirmed that the model including the spatial tensor improves prediction confidence only in specific areas. Global Moran’s I suggest that the inclusion of the spatial tensor helps remove residual spatial autocorrelation, thereby reducing uncertainty. Calibration analyses further show that model_A slightly outperforms 

model_B in terms of probabilistic reliability, while model_B tends to produce more conservative predictions, reflected in its lower calibration slope. 

Overall, the results show that the spatial GAM provides a modest improvement in fit and partially captures spatial structure, but these benefits are heterogeneous and come with increased complexity. One possible explanation lies in the way spatial information is represented. In the current framework, spatial autocorrelation is accounted for through the coordinates of SU centroids. However, these coordinates may not adequately represent the true spatial distribution of landslides within each SU, particularly when the centroid is distant from the areas where failures occurred. This limitation is consistent with the high geomorphological variability typical of Alpine terrain and may reduce the effectiveness of the spatial tensor in capturing meaningful spatial dependence. A possible refinement would involve replacing geometric centroids with weighted centroids that account for the observed distribution of landslides within each SU. Such an approach would be aligned with the concept of “landslide path dependency” introduced by Samia et al. (2017a, b), where spatial influence propagates preferentially downslope and along expected runout trajectories. Given the importance of the climatic factors in the initiation of shallow landslides, especially in a warming climate, future research should also incorporate precipitation intensity, snowmelt, and seasonal patterns in a way that captures distinct microclimatic conditions and their medium- to long-term evolution. Framing these factors as descriptors of spatial variability – rather than as indicators of precise triggering times – would allow susceptibility models to better represent heterogeneous environmental settings without overstating their short-term predictive capabilities. 



**Fig. 12** Landslide density comparison across susceptibility classes for model_B (turquoise) and model_A (salmon), evaluated on **(a)** training and **(b)** testing subsets. For each susceptibility class, landslide density represents the conditional probability of landslide occurrence given 

that a slope unit belongs to that class. The plots highlight the progressive increase in landslide occurrence with increasing susceptibility and reveal nuanced performance differences between model_B and model_A across both training and generalisation scenarios 

```
1 3
```

<mark>Page 23 of 26</mark> **<mark>157</mark>** 

Stochastic Environmental Research and Risk Assessment (2026) 40:157 

**Fig. 13 (a)** Calibration curves for model_A and model_B comparing predicted probabilities to observed outcomes, with deviations from the diagonal indicating miscalibration. Reliability diagrams for **(b)** model_A and **(c)** model_B illustrate accuracy across 10 confidence bins; closer alignment with the diagonal suggests better reliability. 



**Table 6** Calibration metrics comparison between model_A and model_B, including Brier score, scaled Brier score, Expected Calibration Error (ECE), Maximum Calibration Error (MCE), and logistic regression calibration parameters (intercept and slope). Lower Brier and calibration errors, along with slope values closer to 1 and intercepts near 0, indicate better calibration Calibration metrics 

|Metric|model_A|model_B|
|---|---|---|
|Brier score|0.124|0.125|
|Brier scaled|0.385|0.380|
|ECE|0.018|0.023|
|MCE|0.045|0.049|
|Intercept|− 0.040|− 0.007|
|Slope|0.950|0.899|



**Funding** Open access funding provided by Università degli Studi di Milano within the CRUI-CARE Agreement. LP and CC are supported by the the European Regional Development Fund, under the Interreg VI-A Italy-Switzerland Cooperation Program 2021–2027, among the activities of the Project ID 0200072 A.M.AL.PI. MO.RE. “Alpi in Movimento, Movimento nelle Alpi: Monitoraggio e Resilienza”. LP spent a 3-month period at WorldPop (University of Southampton) supported by an Erasmus Traineeship fellowship. The funders had no role in study design, data collection and analysis, decision to publish, and preparation of the manuscript. Open access funding provided by Università degli Studi di Milano within the CRUI-CARE Agreement. 

**Data availability** The data that support the findings of this study are available from the corresponding author upon reasonable request. 

### **Declarations** 

**Supplementary Information** The online version contains supplementary material available at  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 0 0 4 7 7 - 0 2 6 - 0 3 2 8 3 - 2 . 

**Acknowledgements** The authors would like to thank the technical offices of Centro Funzionale Regione Autonoma Valle d’Aosta for data sharing and data management support. 

**Author contributions** Conceptualisation: LP, CC, AS, TE. Methodology: LP, CC, AS, TE, MB, OY. Formal analysis and investigation: LP, CC, MB. Writing – original draft: LP. Writing – review & editing: CC, AS, TE, MB, OY. Supervision: CC, AS. Funding acquisition: CC. 

**Conflict of interest** The authors declare no conflict of interest. 

**Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended 

```
1 3
```

**<mark>157</mark>** <mark>Page 24 of 26</mark> 

Stochastic Environmental Research and Risk Assessment (2026) 40:157 

use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit  h t t p : / / c r e a t i v e c o m m o n s . o r g / l i c e n s e s / b y / 4 . 0 / . 

## **References** 

- Centro Funzionale Regione Autonoma Valle d’Aosta (2024) Fattori di influenza climatica in Valle d’Aosta. In: Cent. Funz. Reg. Auton. Val. Aosta. http:// cf.regi one.vda .it/i t/inquadramento-climatico. Accessed 7 Oct 2025 

- Committee on the Review of the National Landslide Hazards Mitigation Strategies (2004) Partnerships for reducing landslide risk: assessment of the national landslide hazards mitigation strategy. National Academies Press 

- UNISDR (2017) 3. Landslide Hazard and Risk Assessment. Words into Action Guidelines: National Disaster Risk Assessment. United Nations Office for Disaster Risk Reduction 

- Abdel-salam M, Kumar N, Mahajan S (2024) A proposed framework for crop yield prediction using hybrid feature selection approach and optimized machine learning. Neural Comput Appl 36:20723– 20750. https:/ /doi.or g/10.10 07/s0 0521-024-10226-x 

- Agyekum TP, Antwi-Agyei P, Dougill AJ, Stringer LC (2024) Benefits and barriers to the adoption of climate-smart agriculture practices in West Africa: a systematic review. Clim Resil Sustain 3:e279. https:/ /doi.or g/10.10 02/cl i2.79 

- Al-Najjar HAH, Pradhan B (2021) Spatial landslide susceptibility assessment using machine learning techniques assisted by additional data created with generative adversarial networks. Geosci Front 12:625–637. https:/ /doi.or g/10.10 16/j. gsf.2020.09.002 

- Alvioli M, Marchesini I, Reichenbach P et al (2016) Automatic delineation of geomorphological slope units with r.slopeunits v1.0 and their optimization for landslide susceptibility modeling. Geosci Model Dev 9:3975–3991.  h t t p s : / / d o i . o r g / 1 0 . 5 1 9 4 / g m d - 9 - 3 9 7 5 - 2 0 1 6 

- Alvioli M, Guzzetti F, Marchesini I (2020) Parameter-free delineation of slope units and terrain subdivision of Italy. Geomorphology 358:107124. https:/ /doi.or g/10.10 16/j. geomorph.2020.107124 

- Alvioli M, Loche M, Jacobs L et al (2024) A benchmark dataset and workflow for landslide susceptibility zonation. Earth-Sci Rev 258:104927. https:/ /doi.or g/10.10 16/j. earscirev.2024.104927 

- Amato G, Palombi L, Raimondi V (2021) Data–driven classification of landslide types at a national scale by using Artificial Neural Networks. Int J Appl Earth Obs Geoinf 104:102549.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . j a g . 2 0 2 1 . 1 0 2 5 4 9 

- Aristizábal E, Lombardo L, Korup O (2025) Spatial regression models to estimate landslide susceptibility. SSRN.  h t t p s : / / d o i . o r g / 1 0 . 2 1 3 9 / s s r n . 5 4 5 8 3 6 4 

- Ba Q, Chen Y, Deng S et al (2018) A comparison of slope units and grid cells as mapping units for landslide susceptibility assessment. Earth Sci Inf 11:373–388. h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 2 1 4 5 - 0 1 8 - 0 3 3 5 - 9 

- Bajni G, Camera CAS, Brenning A, Apuani T (2022) Assessing the utility of regionalized rock-mass geomechanical properties in rockfall susceptibility modelling in an alpine environment. Geomorphology 415:108401. h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . g e o m o r p h . 2 0 2 2 . 1 0 8 4 0 1 

- Bajni G, Camera CAS, Apuani T (2023) A novel dynamic rockfall susceptibility model including precipitation, temperature and snowmelt predictors: a case study in Aosta Valley (northern Italy). Landslides 20:2131–2154.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 3 4 6 - 0 2 3 - 0 2 0 9 1 - x 

- Bert M, Falasco E, Mobili L et al (2024) Diatom assemblages in glacial-fed streams of Italian Western Alps. Bot Lett 0:1–17.  h t t p s : / / d o i . o r g / 1 0 . 1 0 8 0 / 2 3 8 1 8 1 0 7 . 2 0 2 4 . 2 4 0 0 6 6 1 

- Bistacchi A, Dal Piaz G, Massironi M et al (2001) The Aosta–Ranzola extensional fault system and Oligocene–Present evolution of the Austroalpine–Penninic wedge in the northwestern Alps. Int J Earth Sci 90:654–667. https:/ /doi.or g/10.10 07/s0 05310000178 

- Bornaetxea T, Rossi M, Marchesini I, Alvioli M (2018) Effective 

   - surveyed area and its role in statistical landslide susceptibility assessments. Nat Hazards Earth Syst Sci 18:2455–2469.  h t t p s : / / d o i . o r g / 1 0 . 5 1 9 4 / n h e s s - 1 8 - 2 4 5 5 - 2 0 1 8 

- Brabb EE (1984) Innovative approaches to landslide hazard and risk mapping. University of Toronto, Toronto (Canada), pp 307–323 

- Breiman L (2001) Random Forests. Mach Learn 45:5–32.  h t t p s : / / d o i . o r g / 1 0 . 1 0 2 3 / A : 1 0 1 0 9 3 3 4 0 4 3 2 4 

- Breiman L, Cutler A, Liaw A, Wiener M (2024) randomForest: Breiman and Cutlers random forests for classification and regression 

- Brenning A (2005) Spatial prediction models for landslide hazards: review, comparison and evaluation. Nat Hazards Earth Syst Sci 5:853–862. https:/ /doi.or g/10.51 94/nh ess-5-853-2005 

- Brenning A (2012) Spatial cross-validation and bootstrap for the assessment of prediction rules in remote sensing: The R package sperrorest. In: 2012 IEEE International geoscience and remote sensing symposium. pp 5372–5375 

- Brier WG (1950) Verification of forecasts expressed in terms of probability. Mon Weather Rev 78:1–3 

- Broeckx J, Maertens M, Isabirye M et al (2019) Landslide susceptibility and mobilization rates in the Mount Elgon region, Uganda. Landslides 16:571–584. https:/ /doi.or g/10.10 07/s1 0346-018-1085-y 

- Brunsden D (2001) A critical assessment of the sensitivity concept in geomorphology. CATENA 42:99–123. h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / S 0 3 4 1 - 8 1 6 2 ( 0 0 ) 0 0 1 3 4 - X 

- Burnham KP, Anderson DR (eds) (2004) Advanced Issues and Deeper Insights. In: Model selection and multimodel inference: a practical information-theoretic approach. Springer New York, New York, NY, pp 267–351 

- Cama M, Lombardo L, Conoscenti C et al (2015) Predicting storm-triggered debris flow events: application to the 2009 Ionian Peloritan disaster (Sicily, Italy). Nat Hazards Earth Syst Sci 15:1785–1806. https:/ /doi.or g/10.51 94/nh ess-15-1785-2015 

- Camera CAS, Zomeni Z, Noller JS et al (2017) A high resolution map of soil types and physical properties for Cyprus: A digital soil mapping optimization. Geoderma 285:35–49.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . g e o d e r m a . 2 0 1 6 . 0 9 . 0 1 9 

- Camera CAS, Bajni G, Corno I et al (2021) Introducing intense rainfall and snowmelt variables to implement a process-related non-stationary shallow landslide susceptibility analysis. Sci Total Environ 786:147360. https:/ /doi.or g/10.10 16/j. scitotenv.2021.147360 

- Carrara A, Cardinali M, Detti R et al (1991) GIS techniques and statistical models in evaluating landslide hazard. Earth Surf Process Landf 16:427–445. https:/ /doi.or g/10.10 02/es p.3290160505 

- Carrara A, Cardinali M, Guzzetti F, Reichenbach P (1995) GIS Technology in Mapping Landslide Hazard. In: Carrara A, Guzzetti F (eds) Geographical Information Systems in Assessing Natural Hazards. Springer Netherlands, Dordrecht, pp 135–175 

- Catani F, Lagomarsino D, Segoni S, Tofani V (2013) Landslide susceptibility estimation by random forests technique: sensitivity and scaling issues. Nat Hazards Earth Syst Sci 13:2815–2831. https:/ /doi.or g/10.51 94/nh ess-13-2815-2013 

- Cutler DR, Edwards TC Jr., Beard KH et al (2007) Random Forests for Classification in Ecology. Ecology 88:2783–2792.  h t t p s : / / d o i . o r g / 1 0 . 1 8 9 0 / 0 7 - 0 5 3 9 . 1 

- Di Napoli M, Di Martire D, Bausilio G et al (2021) Rainfall-induced shallow landslide detachment, transit and runout susceptibility mapping by integrating machine learning techniques and 

```
1 3
```

<mark>Page 25 of 26</mark> **<mark>157</mark>** 

Stochastic Environmental Research and Risk Assessment (2026) 40:157 

- GIS-based approaches. Water 13:488. h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / w Johnston EC, Davenport FV, Wang L et al (2021) Quantifying the 1 3 0 4 0 4 8 8 Effect of Precipitation on Landslide Hazard in Urbanized and 

- Ding L, Jiang W, Li Q, Shen W (2025) A hybrid framework for landslide Non-Urbanized Areas. Geophys Res Lett 48. h t t p s : / / d o i . o r g / 1 0 . prediction integrating machine learning and sample enhanced by 1 0 2 9 / 2 0 2 1 G L 0 9 4 0 3 8 . e2021GL094038 spatial autocorrelation. Stoch Environ Res Risk Assess 39:5477– Kass RE, Raftery AE (1995) Bayes Factors. J Am Stat Assoc 90:773– 5501. https:/ /doi.or g/10.10 07/s0 0477-025-03079-w 795. https:/ /doi.or g/10.10 80/01 621459.1995.10476572 

- Dormann CF (2007) Effects of incorporating spatial autocorrelation Knevels R, Petschko H, Proske H et al (2020) Event-Based Landslide into the analysis of species distribution data. Glob Ecol Biogeogr Modeling in the Styrian Basin, Austria: Accounting for Time16:129–138. https:/ /doi.or g/10.11 11/j. 1466-8238.2006.00279.x Varying Rainfall and Land Cover. Geosciences 10:217.  h t t p s : / / d o  h t t p s : / / d o 

- Ebrahim K, Taiwo R, Zayed T (2026) Data-driven interface for shali . o r g / 1 0 . 3 3 9 0 / g e o s c i e n c e s 1 0 0 6 0 2 1 7 low rainfall-induced landslide forecasting considering trigKoo TK, Li MY (2016) A Guideline of Selecting and Reporting Intrager randomness and spatiotemporal dependencies. Landslides class Correlation Coefficients for Reliability Research. J Chiropr 23:1205–1228. https:/ /doi.or g/10.10 07/s1 0346-025-02679-5 Med 15:155–163. https:/ /doi.or g/10.10 16/j. jcm.2016.02.012 

- Economou T, Lazoglou G, Tzyrkalli A et al (2023) A data integration Kovács L (2024) Feature selection algorithms in generalized additive framework for spatial interpolation of temperature observations models under concurvity. Comput Stat 39:461–493.  h t t p s : / / d o i . o r using climate model data. PeerJ 11:e14519. h t t p s : / / d o i . o r g / 1 0 . 7 g / 1 0 . 1 0 0 7 / s 0 0 1 8 0 - 0 2 2 - 0 1 2 9 2 - 7 7 1 7 / p e e r j . 1 4 5 1 9 Kuhn M, Jackson S, Cimentada J (2025) corrr: Correlations in R 

- Van Den Eeckhaut M, Hervás J (2012) State of the art of national Li H, Chen Y, Deng S et al (2019) Eigenvector Spatial Filtering-Based landslide databases in Europe and their potential for assessing Logistic Regression for Landslide Susceptibility Assessment. landslide susceptibility, hazard and risk. Geomorphology 139ISPRS Int J Geo-Inf 8:332. https:/ /doi.or g/10.33 90/ij gi8080332https:/ /doi.or g/10.33 90/ij gi8080332 140:545–558. https:/ /doi.or g/10.10 16/j. geomorph.2011.12.006 Liang Z, Wang C, Khan KUJ (2021) Application and comparison of 

- Ellero A, Loprieno A (2018) Nappe stack of Piemonte–Ligurian units different ensemble learning machines combining with a novel south of Aosta Valley: New evidence from Urtier Valley (Western sampling strategy for shallow landslide susceptibility mapping. Alps). Geol J 53:1665–1684. https:/ /doi.or g/10.10 02/gj .2984 Stoch Environ Res Risk Assess 35:1243–1256.  h t t p s : / / d o i . o r g / 1 0  h t t p s : / / d o i . o r g / 1 0 

- Erener A, Düzgün HSB (2012) Landslide susceptibility assessment: . 1 0 0 7 / s 0 0 4 7 7 - 0 2 0 - 0 1 8 9 3 - y what are the effects of mapping unit and mapping method? EnviLiu X, Su P, Li Y et al (2021) Susceptibility assessment of small, shalron Earth Sci 66:859–877.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 2 6 6 5 - 0 1 1 - 1 low and clustered landslide. Earth Sci Inf 14:2347–2356.  h t t p s : / /  h t t p s : / / 2 9 7 - 0 d o i . o r g / 1 0 . 1 0 0 7 / s 1 2 1 4 5 - 0 2 1 - 0 0 6 8 7 - 2 

   - Knevels R, Petschko H, Proske H et al (2020) Event-Based Landslide Modeling in the Styrian Basin, Austria: Accounting for TimeVarying Rainfall and Land Cover. Geosciences 10:217.  h t t p s : / / d o  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / g e o s c i e n c e s 1 0 0 6 0 2 1 7 

   - Kuhn M, Jackson S, Cimentada J (2025) corrr: Correlations in R Li H, Chen Y, Deng S et al (2019) Eigenvector Spatial Filtering-Based Logistic Regression for Landslide Susceptibility Assessment. ISPRS Int J Geo-Inf 8:332. https:/ /doi.or g/10.33 90/ij gi8080332https:/ /doi.or g/10.33 90/ij gi8080332 

   - Liang Z, Wang C, Khan KUJ (2021) Application and comparison of different ensemble learning machines combining with a novel sampling strategy for shallow landslide susceptibility mapping. Stoch Environ Res Risk Assess 35:1243–1256.  h t t p s : / / d o i . o r g / 1 0  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 0 0 4 7 7 - 0 2 0 - 0 1 8 9 3 - y 

   - Liu X, Su P, Li Y et al (2021) Susceptibility assessment of small, shallow and clustered landslide. Earth Sci Inf 14:2347–2356.  h t t p s : / /  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 2 1 4 5 - 0 2 1 - 0 0 6 8 7 - 2 

- Fang Z, Wang J, Wang Y et al (2025) Improved landslide prediction by considering continuous and discrete spatial dependency. Landslides 22:1107–1122. h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 3 4 6 - 0 2 4 - 0 2 4 3 1 - 5 

- Frey M, Desmons J, Neubauer F (1999) The New Metamorphic Map of the Alps. p 1 

   - Liu X-D, Xiao T, Zhang S-H et al (2024) Comparative study of sampling strategies for machine learning-based landslide susceptibility assessment. Stoch Environ Res Risk Assess 38:4935–4957. https:/ /doi.or g/10.10 07/s0 0477-024-02841-w 

   - Loche M, Lombardo L, Gorum T et al (2022) Distinct Susceptibility Patterns of Active and Relict Landslides Reveal Distinct Triggers: A Case in Northwestern Turkey. Remote Sens 14:1321.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / r s 1 4 0 6 1 3 2 1 

- Giardino M, Ratto S (2007) Analisi del dissesto da frana in Valle d’Aosta. Rapp Sulle Frane Ital 21–150 

- Giardino M, Mortara G, Chiarle M (2017) The Glaciers of the Valle d’Aosta and piemonte regions: records of present and past environmental and climate Changes. In: Soldati M, Marchetti M (eds) Landscapes and Landforms of Italy. Springer International Publishing, Cham, pp 77–88 

- Giordan D, Cignetti M, Wrzesniak A et al (2018) Operative Monographies: Development of a New Tool for the Effective Management of Landslide Risks. Geosciences 8:485.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / g e o s c i e n c e s 8 1 2 0 4 8 5 

   - Loecher M (2022) Unbiased variable importance for random forests. Commun Stat - Theory Methods 51:1413–1425.  h t t p s : / / d o i . o r g / 1 0 . 1 0 8 0 / 0 3 6 1 0 9 2 6 . 2 0 2 0 . 1 7 6 4 0 4 2 

   - Lombardo L, Opitz T, Ardizzone F et al (2020) Space-time landslide predictive modelling. Earth-Sci Rev 209:103318.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . e a r s c i r e v . 2 0 2 0 . 1 0 3 3 1 8 

   - Marquardt DW (1970) Generalized Inverses, Ridge Regression, Biased Linear Estimation, and Nonlinear Estimation. Technometrics 12:591–612.  h t t p s : / / d o i . o r g / 1 0 . 1 0 8 0 / 0 0 4 0 1 7 0 6 . 1 9 7 0 . 1 0 4 8 8 6 9 9 

- De Giusti F, Dal Piaz GV, Massironi M, Schiavo A (2003) Carta geotettonica della Valle d’Aosta. Mem. Sci. Geol. 55 

   - Masi EB, Segoni S, Tofani V (2021) Root Reinforcement in Slope Stability Models: A Review. Geosciences 11:212.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / g e o s c i e n c e s 1 1 0 5 0 2 1 2 

- Goetz JN, Brenning A, Petschko H, Leopold P (2015) Evaluating machine learning and statistical prediction techniques for landslide susceptibility modeling. Comput Geosci 81:1–11.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . c a g e o . 2 0 1 5 . 0 4 . 0 0 7 

   - McGuire LA, Rengers FK, Kean JW et al (2016) Elucidating the role of vegetation in the initiation of rainfall-induced shallow landslides: Insights from an extreme rainfall event in the Colorado Front Range. Geophys Res Lett 43:9084–9092.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 2 / 2 0 1 6 G L 0 7 0 7 4 1 

- Guzzetti F, Reichenbach P, Cardinali M et al (2005) Probabilistic landslide hazard assessment at the basin scale. Geomorphology 72:272–299. https:/ /doi.or g/10.10 16/j. geomorph.2005.06.002 

- Halter T, Lehmann P, Bast A et al (2025) In situ soil moisture data improve precipitation-based shallow landslide early warning through innovative machine learning methods. Landslides 22:3599–3614. https:/ /doi.or g/10.10 07/s1 0346-025-02599-4 

   - Montgomery DC, Peck EA, Vining GG (2021) Introduction to linear regression analysis. John Wiley & Sons 

   - Moran PAP (1950) Notes on Continuous Stochastic Phenomena. Biometrika 37:17–23. https:/ /doi.or g/10.23 07/23 32142 

- Hebbali A (2024) olsrr: Tools for Building. OLS Regression Models Hijmans RJ, Barbosa M, Bivand R et al (2025) terra: Spatial Data Analysis 

   - Overholser BR, Sowinski KM (2008) Biostatistics primer: part 2. Nutr Clin Pract Off Publ Am Soc Parenter Enter Nutr 23:76–84. https:/ /doi.or g/10.11 77/01 1542650802300176 

- Hong H, Wang D, Zhu A-X, Wang Y (2024) Landslide susceptibility mapping based on the reliability of landslide and non-landslide sample. Expert Syst Appl 243:122933. h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . e s w a . 2 0 2 3 . 1 2 2 9 3 3 

- Petschko H, Bell R, Glade T, Brenning A (2012) Landslide susceptibility modeling with generalized additive models – facing the heterogeneity of large regions. Landslides Eng Slopes Prot Soc Improv Underst 1:769–777 

```
1 3
```

**<mark>157</mark>** <mark>Page 26 of 26</mark> 

Stochastic Environmental Research and Risk Assessment (2026) 40:157 

- Piacentini D, Troiani F, Soldati M et al (2012) Statistical analysis for assessing shallow-landslide susceptibility in South Tyrol (southeastern Alps, Italy). Geomorphology 151–152:196–206.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . g e o m o r p h . 2 0 1 2 . 0 2 . 0 0 3 

- Ponziani M, Ponziani D, Giorgi A et al (2023) The use of machine learning techniques for a predictive model of debris flows triggered by short intense rainfall. Nat Hazards 117:143–162.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 1 0 6 9 - 0 2 3 - 0 5 8 5 3 - x 

- Probst P, Wright MN, Boulesteix A-L (2019) Hyperparameters and tuning strategies for random forest. WIREs Data Min Knowl Discov 9:e1301. https:/ /doi.or g/10.10 02/wi dm.1301 

- Rabby YW, Ishtiaque A, Rahman MS (2020) Evaluating the effects of digital elevation models in landslide susceptibility mapping in Rangamati District, Bangladesh. Remote Sens 12:2718.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / r s 1 2 1 7 2 7 1 8 

- Ratto S, Bonetto F, Comoglio C (2003) The October 2000 flooding in Valle d'Aosta (Italy): Event description and land planning measures for the risk mitigation. Int J River Basin Manag 1:105–116. https:/ /doi.or g/10.10 80/15 715124.2003.9635197 

- Reichenbach P, Rossi M, Malamud BD et al (2018) A review of statistically-based landslide susceptibility models. Earth-Sci Rev 180:60–91. https:/ /doi.or g/10.10 16/j. earscirev.2018.03.001 

- Riley SJ, De Gloria SD, Elliot R (1999) A terrain ruggedness index that quantifies topographic heterogeneity. Int J Sci 5 

- Roberts DR, Bahn V, Ciuti S et al (2017) Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure. Ecography 40:913–929. https:/ /doi.or g/10.11 11/ec og.02881 

- Rodriguez-Galiano VF, Ghimire B, Rogan J et al (2012) An assessment of the effectiveness of a random forest classifier for land-cover classification. ISPRS J Photogramm Remote Sens 67:93–104. https:/ /doi.or g/10.10 16/j. isprsjprs.2011.11.002 

- Rohan T, Shelef E, Mirus B, Coleman T (2023) Prolonged influence of urbanization on landslide susceptibility. Landslides 20:1433– 1447. https:/ /doi.or g/10.10 07/s1 0346-023-02050-6 

- Rubel F, Brugger K, Hasliger K, Auer I (2017) The climate of the European Alps: Shift of very high resolution Köppen-Geiger climate zones 1800–2100. Meteorol Z 26:115–125.  h t t p s : / / d o i . o r g / 1 0 . 1 1 2 7 / m e t z / 2 0 1 6 / 0 8 1 6 

- Samia J, Temme A, Bregt A et al (2017a) Characterization and quantification of path dependency in landslide susceptibility. Geomorphology 292:16–24.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . g e o m o r p h . 2 0 1 7 . 0 4 . 0 3 9 

- Samia J, Temme A, Bregt A et al (2017b) Do landslides follow landslides? Insights in path dependency from a multi-temporal landslide inventory. Landslides 14:547–558.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 3 4 6 - 0 1 6 - 0 7 3 9 - x 

- Samia J, Temme A, Bregt AK et al (2018) Implementing landslide path dependency in landslide susceptibility modelling. Landslides 15:2129–2144. https:/ /doi.or g/10.10 07/s1 0346-018-1024-y 

- Schlögl M, Spiekermann R, Steger S (2025) Towards a holistic assessment of landslide susceptibility models: insights from the Central Eastern Alps. Environ Earth Sci 84:113.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 2 6 6 5 - 0 2 4 - 1 2 0 4 1 - y 

- Silva RPda, Coelho Netto AL, Lacerda WA (2023) Hydro-geomorphological conditions for the classification of terrain susceptibility to shallow translational landslides: a geo-hydro ecological approach. Soils Rocks 46:e2023005623.  h t t p s : / / d o i . o r g / 1 0 . 2 8 9 2 7 / S R . 2 0 2 3 . 0 0 5 6 2 3 

- Simpson GL (2018) Modelling Palaeoecological Time Series Using Generalised Additive Models. Front Ecol Evol.  h t t p s : / / d o i . o r g / 1 0 . 3 3 8 9 / f e v o . 2 0 1 8 . 0 0 1 4 9 . 6: 

- Song Y-W, Wang J-S, Qi Y-L et al (2025) Serial filter-wrapper feature selection method with elite guided mutation strategy on cancer gene expression data. Artif Intell Rev 58:111.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 4 6 2 - 0 2 4 - 1 1 0 2 9 - 1 

- Stoner O, Economou T, Torres R et al (2023) Quantifying Spatio-temporal risk of Harmful Algal Blooms and their impacts on bivalve shellfish mariculture using a data-driven modelling approach. Harmful Algae 121:102363. h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . h a l . 2 0 2 2 . 1 0 2 3 6 3 

- Swain JB, Singh NJ, Gupta LR (2024) Landslide susceptibility zonation of a hilly region: A quantitative approach. Nat Hazards Res 4:75–86. https:/ /doi.or g/10.10 16/j. nhres.2023.07.008 

- Swets JA (1988) Measuring the Accuracy of Diagnostic Systems. Science 240:1285–1293. https:/ /doi.or g/10.11 26/sc ience.3287615 

- Taalab K, Cheng T, Zhang Y (2018) Mapping landslide susceptibility and types using Random Forest. Big Earth Data 2:159–178. https:/ /doi.or g/10.10 80/20 964471.2018.1472392 

- Tanyas H, Lombardo L (2020) Completeness Index for EarthquakeInduced Landslide Inventories. Eng Geol 264:105331.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . e n g g e o . 2 0 1 9 . 1 0 5 3 3 1 

- Tarquini S, Isola I, Favalli M et al (2023) TINITALY, a digital elevation model of Italy with a 10 meters cell size (Version 1.1).  h t t p s : / / d o i . o r g / 1 0 . 1 3 1 2 7 / t i n i t a l y / 1 . 1 . Ist Naz Geofis E Vulcanol INGV 10: 

- Tartarotti P, Guerini SSG, Rotondo F et al (2019) Superposed Sedimentary and Tectonic Block-In-Matrix Fabrics in a Subducted Serpentinite Mélange (High-Pressure Zermatt Saas Ophiolite, Western Alps). Geosciences 9:358. h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / g e o s c i e n c e s 9 0 8 0 3 5 8 

- Thisted RA (1998) What is a _P_ value? Dep Stat Health Stud 

- Touw WG, Bayjanov JR, Overmars L et al (2013) Data mining in the Life Sciences with Random Forest: a walk in the park or lost in the jungle? Brief Bioinform 14:315–326.  h t t p s : / / d o i . o r g / 1 0 . 1 0 9 3 / b i b / b b s 0 3 4 

- Trigila A, Iadanza C, Guerrieri L (2007) The IFFI Project (Italian Landslide Inventory): methodology and results. Guidelines for mapping areas at risk of landslides in Europe. Institute for Environment and Sustainability Joint Research Centre (JRC), Ispra, Italy, p 15 

- Viani C, Machguth H, Huggel C et al (2020) Potential future lakes from continued glacier shrinkage in the Aosta Valley Region (Western Alps, Italy). Geomorphology 355:107068.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . g e o m o r p h . 2 0 2 0 . 1 0 7 0 6 8 

- Wei T, Simko V, Levy M et al (2024) corrplot: Visualization of a Correlation Matrix 

- Wood SN (2017) Generalized additive models: an introduction with R, 2nd edn. Chapman and Hall/CRC, New York 

- Wood SN (2025) mgcv: Mixed GAM Computation Vehicle with Automatic Smoothness Estimation 

- Woodard JB, Mirus BB, Wood NJ et al (2024) Slope Unit Maker (SUMak): an efficient and parameter-free algorithm for delineating slope units to improve landslide modeling. Nat Hazards Earth Syst Sci 24:1–12. https:/ /doi.or g/10.51 94/nh ess-24-1-2024 

- Yu B, Zhu Y, Liu Y (2017) Topographical factor-based shallow landslide hazard assessment: a case of Dayi area of Guizhou Province in China. Geoenvironmental Disasters 4:24.  h t t p s : / / d o i . o r g / 1 0 . 1 1 8 6 / s 4 0 6 7 7 - 0 1 7 - 0 0 8 8 - 7 

- Zhang D, Jindal D, Roy N et al (2024) Enhancing landslide susceptibility mapping using a positive-unlabeled machine learning approach: a case study in Chamoli, India. Geoenvironmental Disasters 11:21. https:/ /doi.or g/10.11 86/s4 0677-024-00281-w 

- Zhou X, Xing Y (2025) Spatial consistency assessment and landslide susceptibility prediction optimization. Front Earth Sci 13.  h t t p s : / / d o i . o r g / 1 0 . 3 3 8 9 / f e a r t . 2 0 2 5 . 1 7 0 2 6 8 8 

**Publisher’s note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

```
1 3
```
