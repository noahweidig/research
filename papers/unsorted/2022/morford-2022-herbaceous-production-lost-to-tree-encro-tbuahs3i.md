---
title: Herbaceous production lost to tree encroachment in United States rangelands
authors:
- Morford, Scott L.
- Allred, Brady W.
- Twidwell, Dirac
- Jones, Matthew O.
- Maestas, Jeremy D.
- Roberts, Caleb P.
- Naugle, David E.
year: '2022'
journal: Journal of Applied Ecology
doi: 10.1111/1365-2664.14288
tags: []
zotero_key: TBUAHS3I
item_type: journalArticle
url: https://besjournals.onlinelibrary.wiley.com/doi/10.1111/1365-2664.14288
source_url: 'unpaywall: https://www.biorxiv.org/content/biorxiv/early/2021/11/02/2021.04.02.438282.full.pdf'
fulltext_status: fulltext
synced: '2026-11-06'
---

# Herbaceous production lost to tree encroachment in United States rangelands

## Abstract

Abstract
            
              
                
                  Rangelands of the United States provide ecosystem services that benefit society and rural economies. Native tree encroachment is often overlooked as a primary threat to rangelands due to the slow pace of tree cover expansion and the positive public perception of trees. Still, tree encroachment fragments these landscapes and reduces herbaceous production, thereby threatening habitat quality for grassland wildlife and the economic sustainability of animal agriculture.
                
                
                  Recent innovations in satellite remote sensing permit the tracking of tree encroachment and the corresponding impact on herbaceous production. We analysed tree cover change and herbaceous production across the western United States from 1990 to 2019.
                
                
                  
                    We show that tree encroachment is widespread in US rangelands; absolute tree cover has increased by 50% (77,323 km
                    2
                    ) over 30 years, with more than 25% (684,852 km
                    2
                    ) of US rangeland area experiencing tree cover expansion. Since 1990, 302 ± 30 Tg of herbaceous biomass have been lost. Accounting for variability in livestock biomass utilization and forage value reveals that this lost production is valued at between $4.1–$5.6 billion US dollars.
                  
                
                
                  
                    Synthesis and applications
                    . The magnitude of impact of tree encroachment on rangeland loss is similar to conversion to cropland, another well‐known and primary mechanism of rangeland loss in the US Prioritizing conservation efforts to prevent tree encroachment can bolster ecosystem and economic sustainability, particularly among privately‐owned lands threatened by land‐use conversion.

## Full text

bioRxiv preprint doi: https://doi.org/10.1101/2021.04.02.438282; this version posted November 2, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

# **Main Manuscript for** 

Tree invasions threaten the conservation potential and sustainability of U.S. rangelands 

Scott L. Morford<sup>a,b,*</sup> , Brady W. Allred<sup>a,b</sup> , Dirac Twidwell<sup>c</sup> , Matthew O. Jones<sup>a,b</sup> , Jeremy D. Maestas<sup>d</sup> , David E. Naugle<sup>b</sup> 

- a Numerical Terradynamic Simulation Group, University of Montana, Missoula, MT 59812, USA 

- b University of Montana, W. A. Franke College of Forestry and Conservation, Missoula, MT 59812, USA 

- c Department of Agronomy and Horticulture, University of Nebraska–Lincoln, Lincoln, NE 68588, USA 

- d US Department of Agriculture, Natural Resources Conservation Service, Portland, OR 97232, USA 

*Corresponding Author: Scott L. Morford, Numerical Terradynamic Simulation Group. ISB 415, University of Montana, Missoula MT, 59812. (406) 461-4910. 

**Email:** scott.morford@ntsg.umt.edu 

**Author Contributions:** S.M. and B.A. designed the analysis with additional input from D.T. and M.J.  S.M. developed the modeling framework and performed the analysis. All authors assisted in 

evaluating and interpreting analysis results. S.M. wrote the paper with contributions from B.A., 

D.N., D.T, and M.J. All authors reviewed and provided input on the manuscript draft. 

**Competing Interest Statement:** None. 

**Keywords:** Woody encroachment, herbaceous production, yield gap, global change, agricultural land use, afforestation 

**Preprint server:** bioarxiv.org; https://doi.org/10.1101/2021.04.02.438282; <u>CC-BY-NC-ND 4.0</u> 

### **This PDF file includes:** 

Main Text Figures 1 to 4 

1 

bioRxiv preprint doi: https://doi.org/10.1101/2021.04.02.438282; this version posted November 2, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

### **Abstract** 

Rangelands of the United States provide ecosystem services that sustain biodiversity and rural economies. Native tree encroachment is a long-standing conservation challenge to these landscapes. Still, its impact is often overlooked due to the slow pace of tree invasions and the positive public perception of trees. We show that tree encroachment is a dominant change agent in U.S. rangelands; tree cover has increased by 50% (77,323 km<sup>2</sup> ) over 30 years, with more than 25% of U.S. rangelands experiencing sustained tree cover expansion. Since 1990, roughly 300 Tg of herbaceous biomass has been lost, totaling $5 billion in foregone revenue to small agricultural producers. The impact of tree encroachment to rangeland loss is similar in magnitude to row-crop conversion, another primary threat to U.S. rangelands. Prioritizing conservation efforts to prevent tree encroachment can bolster ecosystem and economic sustainability, particularly among privately-owned lands threatened by land-use conversion. 

### **Introduction** 

Native trees are invading global rangeland biomes<sup>1,2</sup> .  Fire suppression, livestock overgrazing, nutrient pollution, and increasing CO2 emissions contribute to extensive tree encroachment to rangelands (here defined as grasslands, shrublands, and open woodlands)<sup>3</sup> . These invasions exacerbate already substantial losses of rangelands to cropland conversion and threaten the resilience and conservation potential of grazing land biomes worldwide<sup>4–7</sup> . 

Tree encroachment negatively impacts a myriad of rangeland ecosystem services, including water storage and supply, habitat quality,  biodiversity, and land surface albedo 8–13. Most importantly, tree cover is a key regulator of herbaceous production (the combined production of grasses and forbs; i.e., forage) upon which both wildlife and livestock depend<sup>10</sup> . Substantial effort has been invested in disentangling the complex relationship between herbaceous production and tree cover<sup>10,14,15</sup> . Yet, critical knowledge gaps still exist for how herbaceous production responds to tree cover expansion at large scales. 

2 

bioRxiv preprint doi: https://doi.org/10.1101/2021.04.02.438282; this version posted November 2, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

Identifying where tree encroachment impacts ecosystem services has traditionally relied on methods such as historical image analysis, paired site investigations, and evaluations of the pollen record<sup>16–18</sup> . These methods have documented substantial tree canopy expansion in Africa, the Americas, Asia, and Australia 1. Unfortunately, critical intelligence on patterns, pace, and magnitude of tree invasions to rangelands remains absent at large scales. While satellite remote sensing tools are applied globally to track forest cover changes, these analyses typically lack the sensitivity to track tree cover gains in rangelands or omit analysis of tree cover in rangelands altogether<sup>19,20</sup> . 

Two-thirds of western U.S. rangelands are under private ownership, and conservation of these lands requires addressing linkages between ecological and economic sustainability. Declining ranch income hastens the conversion of intact grasslands to row-crop agriculture, energy production, and subdivision<sup>21,22</sup> . For example, row-crop conversion has accelerated in recent years due to commodity market fluctuations and declining economic returns from livestock production<sup>23</sup> . Tree encroachment is thought to exacerbate declines in ranching profitability as invading trees out-compete and displace grasses and forbs<sup>15</sup> . Revealing the economic cost of tree encroachment on forage production could help motivate livestock producers to implement proactive, conservation-focused tree management to prevent woody encroachment and promote greater biodiversity on their lands. However, scale-appropriate data and tools to evaluate the interaction of tree expansion and herbaceous production have not been available. 

Recent technological advances in remote sensing collectively suggest large-scale tree cover expansion in U.S. rangelands<sup>24–26</sup> , consistent with decades of empirical observations<sup>2</sup> . Related innovations in tracking annual herbaceous production now allow for an integrated spatiotemporal analysis across the western United States<sup>27,28</sup> . To assess how tree cover expansion impacts herbaceous production, we jointly analyzed tree cover change and herbaceous production across 17 western states for 1990 - 2019. This analysis _1)_ provides a spatial and temporal evaluation of tree encroachment in rangelands and _2)_ quantifies the difference between attainable and actual herbaceous production as a function of tree cover expansion, a difference termed yield gap<sup>29</sup> . Finally, yield gap estimates derived in this analysis are combined with grazing rental 

3 

bioRxiv preprint doi: https://doi.org/10.1101/2021.04.02.438282; this version posted November 2, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

rates from the United States Department of Agriculture (USDA) to estimate foregone revenue to livestock producers from tree encroachment. 

## **Results and Discussion** 

Tree cover gains between 1990 and 2019 in western U.S rangelands were substantial. Rangelands added 77,323 ± 1,222 km<sup>2</sup> of trees ( **Figure 1** ), increasing absolute tree cover from 154,502 km<sup>2</sup> to 231,825 km<sup>2</sup> ( **Supplemental Table 1** ). Tree cover grew on average 2,577 km<sup>2</sup> per year, with annual increases in all years on record. 

The observed 50% increase in absolute tree cover does not fully convey the impact and extent of invading trees on rangelands. Over these 30 years, tree invasions resulted in the loss of 147,700 km<sup>2</sup> (range: 135,283 - 150,827 km<sup>2</sup> ) of tree-free rangelands, transitioning roughly 8% of all these lands into woodlands ( **Figure 1, Panel C** ). Moreover, even where tree-free rangelands persist, they are increasingly vulnerable to invasion due to their proximity to nearby tree seed sources. For example, the area of intact tree-free rangelands (rangelands greater than 200 meters from a tree seed source) declined by 15% (204,651 km<sup>2</sup> ) over the 30 years, revealing that woodland extensification remains a dominant process driving rangeland vulnerability to woody encroachment in U.S. rangelands<sup>30</sup> . 

In total, we observed net sustained tree cover expansion across roughly 25% of all western U.S. rangelands, illustrating that tree encroachment is broadly distributed and not limited to a particular geography, climate, or ownership. Outsized impacts to wildlife habitat, hydrology, and land-surface albedo provide compelling evidence for how small increases in tree density impact the function of U.S rangelands<sup>8,9,13,31</sup> . 

The pace of tree encroachment is similar in magnitude to recent row-crop conversion, another primary threat to the conservation and sustainability of U.S. rangelands. From 2008 to 2016, cropland conversion of intact rangelands accelerated rapidly across the western U.S; annual conversion rates over that period were observed to be 1,649 to 4,385 km<sup>2</sup> annually (median = 2,777 km<sup>2</sup> , **Supplemental Figure 1** )<sup>23</sup> . In comparison, the median annual loss of rangelands to tree encroachment was 1,899 km<sup>2</sup> over this same period. Together, these data suggest rangelands of the western U.S. are being lost at a 

4 

bioRxiv preprint doi: https://doi.org/10.1101/2021.04.02.438282; this version posted November 2, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

rate of 0.89 hectares (2.2 acres) per minute, losses that are 68% higher than estimates based solely on row-crop conversion. 

The rate of tree cover expansion varied spatially and temporally across western U.S. rangelands ( **Supplemental Figure 2** ). The Central and Northern Great Plains, Great Basin, and Intermountain West showed sustained or accelerating tree cover expansion. Texas and the southern Great Plains showed increasing tree cover but slowing rates of cover expansion through time. In contrast, tree cover declined in regions along the Pacific Ocean and portions of the desert southwest. Notability, rangelands of California, and southeastern Arizona (western Sierra Madre Piedmont) were the only regions to show sustained tree cover loss over our 30-year analysis period. 

Tree cover expansion contributed to sizable losses in herbaceous production ( **Figure 2** ). Production losses totaled 302 ± 30 Tg (dry biomass) from 1990 through 2019. In 2019, the yield gap totaled 20.0 Tg, representing 5% - 6% of the potential forage production for all western U.S. rangelands ( **Figure 2b** ). In an agricultural context, a 5% - 6% yield gap is comparable to yield losses sustained to commodity crops under extreme drought events<sup>32</sup> . 

Spatially, yield gaps are highest in the southern Great Plains, where production potential is greatest due to favorable climate conditions and where woody encroachment has expanded most rapidly. However, forage losses in the northern Great Plains and Great Basin are no less substantial; proportionally, losses in these regions can be similar to or exceed losses from more productive grazing lands of the southern Great Plains ( **Supplemental Figure 3** ). Rapidly accelerating tree cover expansion and production losses in the Dakotas, Montana, Nebraska, and Wyoming are particularly concerning; these states are central to ongoing efforts to protect the northern Great Plains biome’s connectivity and biodiversity, and are focal areas for preventing cropland conversion<sup>21,33</sup> . Moreover, these lands are home to the last remaining large-scale migrations of land mammals in the contiguous United States and critical habitat for grassland birds, some of the most imperiled wildlife on the continent<sup>11,34,35</sup> . California was the only state in our dataset that did not develop a yield gap over the 30-year record ( **Supplemental Table** 

5 

bioRxiv preprint doi: https://doi.org/10.1101/2021.04.02.438282; this version posted November 2, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

**5** ). 

To explore how lost herbaceous production may impact ranch economics, we used our yield gap data with pasture rental rates to estimate lost revenues due to tree cover expansion. Pasture rental rates compiled by the USDA (34) represent the private rate that ranchers pay to lease grazing land, so they are a meaningful proxy for the going-market value of forage<sup>36</sup> . We found that on an inflation-corrected basis, potential revenue losses across the 17 states totaled $4.83 ± 0.53 billion over the 30 years analyzed; losses exceeded $300 million in 2019 and are increasing at a rate of roughly $11.3 million per year ( **Figure 2c** ). These coarse estimates suggest that revenue losses from tree encroachment to rural agricultural economies are at a minimum on the order of $100s of millions of dollars per year.  Moreover, this calculation is likely conservative because it uses a tree cover basis from 1990 and excludes forage losses due to shrub encroachment. 

Importantly, primary production is not fixed or constant in an era of global environmental change<sup>37</sup> . We observed sizable increases in herbaceous production among rangelands where tree cover remained constant (averaging 195.7 kg ha<sup>-1</sup> yr<sup>-1</sup> more production in 2019 than 1990), consistent with other studies showing increasing continental-scale productivity<sup>37–39</sup> . Consequently, many regions of the western U.S. with increasing tree cover saw only moderate losses in total herbaceous production (averaging 37.7 kg ha<sup>-1</sup> yr<sup>-1</sup> less production in 2019 than in 1990; **Supplemental Figure 2** ). 

Locally, the imprint of increasing primary productivity buffers production losses during early tree colonization of rangelands. We observed that herbaceous production could remain stable, or even increase, following the inception of tree invasions and during the early development of yield gaps ( **Figure 3** ). In the absence of disturbance, however, yield gaps rapidly develop as tree cover continues to increase, resulting in large net declines in herbaceous production over relatively short periods. For example, at the Loess Canyon site ( **Figure 3 - Panel C** and **Figure 4** ) a herbaceous production yield gap took roughly 20 years to develop (1990 - 2010) as tree cover grew from 2 to 20%. Over the following five years (2010 - 2014), the yield gap expanded dramatically, resulting in a 30% loss of potential production. These yield gap data are consistent with field-based 

6 

bioRxiv preprint doi: https://doi.org/10.1101/2021.04.02.438282; this version posted November 2, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

investigations in the Loess Canyons, experimental woody-encroachment data from the Konza LTER ( **Supplemental Text** ), and literature-based reviews of tree-grass interactions in dryland systems<sup>10,40</sup> . 

These site-specific data illustrate both challenges and opportunities to address tree encroachment in rangelands. The lag between when trees colonize and when yield gaps are detectable may promote a perverse incentive among some land managers to tolerate tree encroachment until an invasion reaches more advanced stages. In these cases, managing tree encroachment becomes more expensive and complex due to removing additional tree biomass and established seed stores<sup>41</sup> . Conversely, the time lag provides an opportunity to implement cost-effective management to prevent further tree encroachment, productivity decline, and economic harm to agricultural producers, particularly if pre-emptive management fails to control the reproductive source of tree encroachment. 

USDA conservation programs direct nearly $90 million annually in public and private funds towards tree and brush removal to promote rangeland health<sup>42</sup> . However, these interventions have generally been opportunistic rather than targeted, resulting in little mitigation of tree invasions at biologically relevant scales<sup>41</sup> . Directing these funds using state-of-the-art targeting, valuation, and monitoring tools will help prioritize projects that can simultaneously promote sustainable agricultural economics while maintaining and growing core, intact rangelands at scale<sup>25,43</sup> . To this end, we include a simple web-enabled map application that visualizes and investigates yield losses attributable to tree cover expansion (https://rangelands.app/yield-gap/). 

Our modeling approach is not without limitations. The hindcast modeling method used here does not consider future climate scenarios, so may not accurately inform future trajectories of production responses to tree encroachment. However, herbaceous productivity is forecasted to increase across much of western U.S. rangelands through 2100, lending some confidence that our findings are generalizable<sup>39,44</sup> . Second, our monetary estimates for lost revenues should be considered preliminary as they do not consider economic leakage or policy and social barriers that may limit the adoption of management alternatives at scale. Locally, our estimates for forage value agree well with 

7 

bioRxiv preprint doi: https://doi.org/10.1101/2021.04.02.438282; this version posted November 2, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

independent agricultural economic data ( **Supplemental text)** . Still, more sophisticated analyses will be required to assess how managing tree encroachment benefits ranching economics. 

Loss of rangeland production and corresponding impacts to ecosystem services need to be considered as part of global scientific advocacy efforts calling for the afforestation of rangelands<sup>45</sup> . Based on the current state of climate-vegetation science, increasing tree cover in rangelands is not a climate mitigation solution<sup>46,47</sup> . Tree encroachment can increase carbon storage in rangelands<sup>16,48</sup> , but these carbon storage gains are typically offset by reducing land-surface albedo at mid- to high- latitudes<sup>12,49</sup> . For example, across the northern Great Plains, tree cover would need to reach 95+% to contribute to climate cooling; such a scenario would result in the wholescale collapse of the northern Great Plains and its biodiversity therein<sup>4,12</sup> . The most effective climate mitigation strategy for rangelands remains preventing grassland conversion to row-crop agriculture and ensuring the massive carbon reservoirs found in rangeland soils are not lost to the atmosphere<sup>4,50</sup> . 

Identifying where tree encroachment creates yield gaps and how forage loss impacts ranching revenues provides a mechanism to focus private-land conservation efforts on economically sustainable outcomes that prevent land-use conversion. Herbaceous production is the cornerstone of food and fiber economics in working rangelands and evaluating it like other agricultural products provides a means to stack market incentives with other conservation subsidies. Preventing yield gaps in rangelands is a novel and landscape-scale conservation strategy to benefit nature and society. 

## **Materials and Methods** 

The analysis area included the 17 western-most states in the contiguous United States, consistent with other data products generated from the Rangelands Analysis Platform<sup>24</sup> . Our calculations only consider production lost to trees and do not include or consider additional production losses attributable to woody shrubs. The total area included in this analysis was 4.73 million km<sup>2</sup> , comprising 6.9 billion pixels. Model inputs and outputs consist of annualized data from 1990 to 2019 unless otherwise stated. Modeling 

8 

bioRxiv preprint doi: https://doi.org/10.1101/2021.04.02.438282; this version posted November 2, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

evaluation, data sources, and computational libraries used in this analysis are provided in the supplemental. 

## **_1. Mapping Rangelands_** 

The spatial extent of rangelands in the western United States was determined from Landfire Biophysical Settings (BPS), version 1.4.0. Landfire BPS represents the dominant vegetation system on the landscape before Euro-American settlement. Grasslands and shrublands were identified using the BPS categorization grouping attribute, while open woodlands were selected based on the BPS name component where ‘woodland’ was the primary attribute. Map units described as barren were excluded. Our rangeland classification layer from Landfire BPS was further modified to exclude crop agricultural and developed lands from the U.S. Geological Survey National Land Cover Database (2016) the National Agricultural Statistical Service Cropland Data Layer (NASS CDL). All production and monetary calculations provided in this manuscript omit riparian and primary forests map units. 

## **_2. Tree Cover Modeling_** 

Annual tree cover was taken from the _Rangeland Analysis Platform V2 (RAP)_ cover products<sup>24</sup> for the years 1990 through 2019. These data were processed using the LandTrendr (LT) segmentation algorithm in Google Earth Engine (GEE) to denoise the time-series data<sup>51</sup> . The LandTrendr parameters used in this analysis are summarized in **Table S2** . 

We applied two independent rules in our tree cover trend analysis to remove spurious tree-cover trends attributable to prediction uncertainty or model error. First, for the analysis to tally a change in pixel tree cover, the absolute difference between the maximum tree cover and minimum tree cover in the pixel time series had to be greater than 2.8%, corresponding to the mean absolute error (MAE) of the tree cover product (24). Second, we evaluated each pixel segment from the LT-GEE segmentation product to determine if the change in tree cover was an artifact of prediction uncertainty/variance (See Bayesian approximation discussion in ref. 24). To accomplish this, we performed a Welch T-test using the tree cover and prediction variance estimates from the first and 

9 

bioRxiv preprint doi: https://doi.org/10.1101/2021.04.02.438282; this version posted November 2, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

last observation in the pixel segment (n = 4, two-tailed, p-value  = 0.01). For tree cover change to be tallied in a pixel, it had to have one or more segments where the t-value < p-value. While imperfect, this approach was an effective screening tool to filter change estimates for pixels with high prediction uncertainty without implementing high computational cost Monte Carlo simulations. 

Tree-free rangelands in this analysis were defined functionally as rangelands where tree cover was less than 4%, corresponding to the minimum cover where impacts to ecosystem services are observed<sup>9</sup> . Vulnerable tree-free rangelands were calculated in GEE using a 200-meter circular buffer around each pixel where tree cover was greater than 2.8% (the MAE of the tree cover model). To tally a change in the aerial extent of intact or vulnerable rangelands, we applied a Welch T-test on the LT-GEE segmentation product using the methods described above. Tree-free rangelands within 200 meters of tree seed source that did not increase in tree cover over the 30s years of data were classified as intact. The uncertainty bands for intact and vulnerable rangelands represent the minimum and maximum calculated areas for each group by applying 1) no filtering and 2) filtering based on the LT-GEE segmentation plus a minimum tree cover change of 2.8%. 

## **_3. Herbaceous Production & Yield Gap Modeling_** 

We used XGBoost, a supervised machine learning library, to predict herbaceous biomass production as a function of tree cover and other biophysical variables<sup>52</sup> . Biomass in our model was derived from total annual herbaceous production reported by the Rangeland Analysis Platform (27); we term this biomass variable _Observed Production_ . Conceptually and numerically, our analysis used the following general framework ( **_equation 1)_** . 

_Observed Production(YR)_ = _f_ (YR, MU, LP, TC(yr),, SP) **eqn 1.** 

In our framework, _YR_ represents year, MU = soil map unit, LP = landscape position, TC(yr) = tree cover for year YR, SP = spatial position/coordinates. Factor variables were encoded as integers during training and inference. Model variables, source data, and a rationale for their inclusion are presented in **Supplemental Table 3** . 

10 

bioRxiv preprint doi: https://doi.org/10.1101/2021.04.02.438282; this version posted November 2, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

Model training and inference were performed using the XGBoost implementation from the open-source H2O.ai library. To improve computational performance, we enabled LightGBM emulation and implemented the dart booster drop-out method to limit overfitting. We used a cartesian grid search for hyper-parameter selection, optimized for the lowest MAE on 10 million randomly selected records. The optimization (loss) function used for model training was mean squared error (MSE) with L2 regularization. Our ensemble used 60 trees with a maximum tree depth of 15.  A complete list of model parameters is included in **Supplemental Table 4** . 

_Model training_ : We split our analysis area into 53 units (models) using the spatial extent of Level-3 EcoRegions developed by the US EPA. The size of the training data for each unit was limited to 71,582,780 records due to computational limitations; the remaining training data were used as hold-out (test) data. The models were trained with 3.8 billion records, randomly sampled from our dataset; the remaining 5.5 billion records were used for holdout evaluation. Evaluation of the training metrics showed that holdout MAE values closely matched training MAE values, suggesting the model did not overfit the data ( **Supplemental Figure 5)** . 

_Model inference:_ For each pixel-year combination, the XGBoost model generates two predictions.  Prediction one estimates herbaceous production for a given year using the corresponding tree cover for that year _;_ we term this _Estimated Production (_ **_equation 2_** _)_ , 

_Estimated Production(YR,TC(yr))_ =  E[ **_m_** | _YR_ , _MU_ , _LP_ , _TC(yr)_ , _SP_ ] **eqn 2.** 

where **_m_** is the model and _TC(yr)_ is the tree cover for year _YR_ . Prediction two estimates the herbaceous production for the year _YR_ using the tree cover from 1990.  We term prediction two _Achievable Production (_ **_equation 3_** _)_ , it represents the herbaceous production for year _YR_ using 1990 tree-cover. 

_Achievable Production(YR,TC(1990))_ =  E[ **_m_** | _YR_ , _MU_ , _LP_ , _TC(1990)_ , _SP_ ] **eqn 3.** 

11 

bioRxiv preprint doi: https://doi.org/10.1101/2021.04.02.438282; this version posted November 2, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

The yield gap attributable to tree cover expansion since 1990 is calculated using the difference of these two predictions for each pixel-year combination ( **_equation 4_** ). Note that the yield gap can be negative in cases where tree cover declines over time. 

_Yield Gap(YR)  = Achievable Production(YR,TC(1990)) –_ 

_Estimated Production(YR,TC(yr))_ **eqn 4.** 

Prediction error for each pixel was calculated as the absolute difference between _Observed Production and Estimated Production_ **_(equation 5)_** _. Model Error_ was represented as the MAE **(equation 6)** , aggregated by year and map unit to provide some localization; _n_ in **equation 6** is the number of observations for each MU. 

_Prediction Error(YR)_ = 



<!-- Start of picture text -->
| Observed Production(YR)  –  Estimated Production(YR,TC(yr)) | eqn 5.<br><!-- End of picture text -->

_Model Error_ (MU | YR) =[∑ _Prediction Error_ (MU | YR)] / n **eqn 6.** 

For the analysis, the yield gap is only tallied when _Yield Gap_ > _Model Error_ for 3 or more consecutive years. This prevents spikes in yield gap attributable to data noise or modeling error from being included in lost potential production estimates. _Potential Production_ in our analysis and map products is presented as the _Observed Production_ plus _Yield Gap._ Additional information regarding sensitivity and uncertainty in our model predictions are presented in the Supplemental. 

## **_4. Monetary calculations_** 

We calculated the value of forage lost to tree cover expansion using our yield gap estimates with grazing rental rates from USDA National Agricultural Statistics Service (NASS)<sup>36</sup> . We used the annual state-level data reported as dollars per animal unit month (AUM) because these records were the most complete for our analysis (1990 - 2019). Military and protected non-grazing lands (e.g. National Parks) were excluded from the monetization calculations, but other federal grazing lands (i.e., BLM and USFS allotments) were included. Missing data were imputed using a linear-interpolation of the 

12 

bioRxiv preprint doi: https://doi.org/10.1101/2021.04.02.438282; this version posted November 2, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

time series data. The value of forage production on a mass basis was calculated as follows: 



**eqn. 7** 

In this calculation, dollars per AUM was taken from NASS tables; AUM per kg forage was assumed to equal to 1 / 344.73, equivalent to 760 lbs per AUM; kg forage per kg production represents the utilization factor ( _UF_ ), and was assumed to equal 0.40 across all locations. The selection of the UF was data-driven: it was derived from an analysis of available NASS rental rates in combination with herbaceous production data ( **_equation 8)_** . The general form of the equation was: 



**eqn. 8** 

where _$/acre_ and _$/AUM_ represent rental rates extracted from NASS data for years 2008 - 2019. Finally, dollar estimates were inflation corrected to 2019 dollars using the consumer price index from the Bureau of Labor Statistics<sup>53</sup> . A summary of annual state-level yield gap and forage value data is provided in **Supplemental Table 5** . 

The $90 million figure presented as tree removal conservation expenditures in the text reflects 2019 EQIP spending on _Practice 314_ plus 25% private matching funds. 

## **5. Production trends and local scale production responses to tree encroachment.** 

Production trends presented in **Figure 3** and **Supplemental Figure 4** represent _Observed Production_ values extracted directly from the Rangeland Analysis Platform and were independent of yield gap calculations. In both cases, the data presented is based on a long-term pixel-wise trend analysis using a linear fit in Google Earth Engine. Production trends from **Supplemental Figure 4** have been masked to rangelands with increasing, stable, and decreasing tree cover using the methods described in sections 1 and 2 of the methods. 

13 

bioRxiv preprint doi: https://doi.org/10.1101/2021.04.02.438282; this version posted November 2, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

### **Acknowledgments** 

This work was made possible by the USDA-Natural Resources Conservation Service’s (NRCS) Conservation Effects Assessment Project - Wildlife Component, the NRCS’s Working Lands for Wildlife, the Arkansas Game & Fish Commission through cooperative agreement 1434-04HQRU1567, and the Bureau of Land Management. Model data will be made available via our web application and archived at Zenodo. Code to replicate the analysis will be archived on Zenodo. Any use of trade, firm, or product names is for descriptive purposes only and does not imply endorsement by the U.S. Government. 

14 

bioRxiv preprint doi: https://doi.org/10.1101/2021.04.02.438282; this version posted November 2, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

### **Reference** 

1. Nackley, L. L., West, A. G., Skowno, A. L. & Bond, W. J. The Nebulous Ecology of Native Invasions. _Trends Ecol. Evol._ **32** , 814–824 (2017). 

2. Archer, S. R. _et al._ Brush Management as a Rangeland Conservation Strategy: A Critical Evaluation. in _Conservation benefits of rangeland practices: Assessment, recommendations, and knowledge gaps._ (ed. Briske, D. D.) 66 (USDA Natural Resources Conservation Service, 2011). 

3. Asner, G. P., Elmore, A. J., Olander, L. P., Martin, R. E. & Harris, A. T. Grazing systems, ecosystem responses, and global change. 45 (2004). 

4. Hoekstra, J. M., Boucher, T. M., Ricketts, T. H. & Roberts, C. Confronting a biome crisis: global disparities of habitat loss and protection: Confronting a biome crisis. _Ecol. Lett._ **8** , 23–29 (2004). 

5. Fargione, J. E. _et al._ Natural climate solutions for the United States. _Sci. Adv._ **4** , eaat1869 (2018). 

6. Kremen, C. & Merenlender, A. M. Landscapes that work for biodiversity and people. _Science_ **362** , eaau6020 (2018). 

7. Veldman, J. W. _et al._ Where Tree Planting and Forest Expansion are Bad for Biodiversity and Ecosystem Services. _BioScience_ **65** , 1011–1018 (2015). 

8. Huxman, T. E. _et al._ Ecohydrological implications of woody plant encroachment. _Ecology_ **86** , 308–319 (2005). 

9. Baruch-Mordo, S. _et al._ Saving sage-grouse from the trees: A proactive solution to reducing a key threat to a candidate species. _Biol. Conserv._ **167** , 233–241 (2013). 

10. Archer, S. R. & Predick, K. I. An ecosystem services perspective on brush management: research priorities for competing land-use objectives. _J. Ecol._ 14 (2014). 

11. Rosenberg, K. V. _et al._ Decline of the North American avifauna. _Science_ **366** , 120–124 (2019). 

12. Mykleby, P. M., Snyder, P. K. & Twine, T. E. Quantifying the trade-off between carbon sequestration and albedo in midlatitude and high-latitude North American forests. _Geophys. Res. Lett._ **44** , 2493–2501 (2017). 

13. Ge, J. & Zou, C. Impacts of woody plant encroachment on regional climate in the southern Great Plains of the United States. _J. Geophys. Res. Atmospheres_ **118** , 9093–9104 (2013). 

14. Scholes, R. J. Convex Relationships in Ecosystems Containing Mixtures of Trees and Grass. _Environ. Resour. Econ._ **26** , 559–574 (2003). 

15. Anadon, J. D., Sala, O. E., Turner, B. L. & Bennett, E. M. Effect of woody-plant encroachment on livestock production in North and South America. _Proc. Natl. Acad. Sci._ **111** , 12948–12953 (2014). 

16. Asner, G. P., Archer, S., Hughes, R. F., Ansley, R. J. & Wessman, C. A. Net changes in regional woody vegetation cover and carbon storage in Texas Drylands, 1937–1999. _Glob. Change Biol._ **9** , 316–335 (2003). 

17. Lubetkin, K. C., Westerling, A. L. & Kueppers, L. M. Climate and landscape drive the pace and pattern of conifer encroachment into subalpine meadows. _Ecol. Appl._ **27** , 1876–1887 (2017). 

18. Archer, S., Scifres, C., Bassham, C. R. & Maggio, R. Autogenic Succession in a Subtropical Savanna: Conversion of Grassland to Thorn Woodland. _Ecol. Monogr._ **58** , 111–127 (1988). 

19. Hansen, M. C. _et al._ High-Resolution Global Maps of 21st-Century Forest Cover Change. _Science_ **342** , 850–853 (2013). 

20. Rigge, M. _et al._ Quantifying Western U.S. Rangelands as Fractional Components with Multi-Resolution Remote Sensing and In Situ Data. _Remote Sens._ **12** , 412 (2020). 

15 

bioRxiv preprint doi: https://doi.org/10.1101/2021.04.02.438282; this version posted November 2, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

21. Lark, T. J. Protecting our prairies: Research and policy actions for conserving America’s grasslands. _Land Use Policy_ **97** , 104727 (2020). 

22. Allred, B. W. _et al._ Ecosystem services lost to oil and gas in North America. _Science_ **348** , 401–402 (2015). 

23. Lark, T. J., Spawn, S. A., Bougie, M. & Gibbs, H. K. Cropland expansion in the United States produces marginal yields at high costs to wildlife. _Nature Communications_ vol. 11 (2020). 

24. Allred, B. W. _et al._ Improving Landsat predictions of rangeland fractional cover with multitask learning and uncertainty. _Methods Ecol. Evol._ **0** , (2021). 

25. Jones, M. O. _et al._ Beyond Inventories: Emergence of a New Era in Rangeland Monitoring. _Rangel. Ecol. Manag._ **73** , 577–583 (2020). 

26. Filippelli, S. K. _et al._ Monitoring pinyon-juniper cover and aboveground biomass across the Great Basin. _Environ. Res. Lett._ **15** , 025004 (2020). 

27. Jones, M. O. _et al._ Annual and 16-Day Rangeland Production Estimates for the Western United States. _Rangel. Ecol. Manag._ **77** , 112–117 (2021). 

28. Robinson, N. P. _et al._ Rangeland Productivity Partitioned to Sub-Pixel Plant Functional Types. _Remote Sens._ **11** , 1427 (2019). 

29. van Ittersum, M. K. _et al._ Yield gap analysis with local to global relevance—A review. _Field Crops Res._ 14 (2013). 

30. Zhou, Y. _et al._ Woody encroachment happens via intensification, not extensification, of species ranges in an African savanna. _Ecol. Appl._ **n/a** , e02437. 

31. Hamilton, B. T., Roeder, B. L. & Horner, M. A. Effects of Sagebrush Restoration and Conifer Encroachment on Small Mammal Diversity in Sagebrush Ecosystem. 10 (2019). 

32. Lesk, C., Rowhani, P. & Ramankutty, N. Influence of extreme weather disasters on global crop production. _Nature_ **529** , 84–87 (2016). 

33. Haggerty, J. H., Auger, M. & Epstein, K. Ranching Sustainability in the Northern Great Plains: An Appraisal of Local Perspectives. _Rangelands_ **40** , 83–91 (2018). 

34. Joly, K. _et al._ Longest terrestrial migrations and movements around the world. _Sci. Rep._ **9** , 15333 (2019). 

35. Brennan, L. A. & Kublesky, William P. North American grassland Birds: an unfolding conservation crisis? _J. Wildl. Manag._ **69** , 1–13 (2005). 

36. United States Department of Agriculture. _National Agriculture Statistics Service Quick Stats Database_ . (2020). 

37. Hicke, J. A. _et al._ Trends in North American net primary productivity derived from satellite observations, 1982-1998. _Glob. Biogeochem. Cycles_ **16** , 2-1-2–14 (2002). 

38. Reeves, M. C., Hanberry, B. B., Wilmer, H., Kaplan, N. E. & Lauenroth, W. K. An Assessment of Production Trends on the Great Plains from 1984 to 2017. _Rangel. Ecol. Manag._ S1550742420300117 (2020) doi:10.1016/j.rama.2020.01.011. 

39. Boone, R. B., Conant, R. T., Sircely, J., Thornton, P. K. & Herrero, M. Climate change impacts on selected global rangeland ecosystem services. _Glob. Change Biol._ **24** , 1382–1393 (2018). 

40. Bielski, C., Scholtz, R., Donovan, V. M., Allen, C. R. & Twidwell, D. Overcoming an “irreversible” threshold: a 15-year fire experiment. _J. Environ. Manage._ **(Accepted)** ,. 

41. Roberts, C. P., Uden, D. R., Allen, C. R. & Twidwell, D. Doublethink and scale mismatch polarize policies for an invasive tree. _PLOS ONE_ **13** , e0189733 (2018). 

42. United States Department of Agriculture. _EQIP Data Dashboards_ . 

43. Uden, D. R. _et al._ Spatial Imaging and Screening for Regime Shifts. _Front. Ecol. Evol._ **7** , 407 (2019). 

16 

bioRxiv preprint doi: https://doi.org/10.1101/2021.04.02.438282; this version posted November 2, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

44. Reeves, M. C., Moreno, A. L., Bagne, K. E. & Running, S. W. Estimating climate change effects on net primary production of rangelands in the United States. _Clim. Change_ **126** , 429–442 (2014). 

45. Bastin, J.-F. _et al._ The global tree restoration potential. _Science_ **365** , 76–79 (2019). 

46. Friedlingstein, P., Allen, M., Canadell, J. G., Peters, G. P. & Seneviratne, S. I. Comment on “The global tree restoration potential”. _Science_ **366** , eaay8060 (2019). 

47. Nuñez, M. A. _et al._ Should tree invasions be used in treeless ecosystems to mitigate climate change? _Front. Ecol. Environ._ **19** , 334–341 (2021). 

48. Connell, R. K., Nippert, J. B. & Blair, J. M. Three Decades of Divergent Land Use and Plant Community Change Alters Soil C and N Content in Tallgrass Prairie. _J. Geophys. Res. Biogeosciences_ **125** , (2020). 

49. Bala, G. _et al._ Combined climate and carbon-cycle effects of large-scale deforestation. _Proc. Natl. Acad. Sci._ **104** , 6550–6555 (2007). 

50. Bossio, D. A. _et al._ The role of soil carbon in natural climate solutions. _Nat. Sustain._ **3** , 391–398 (2020). 

51. Kennedy, R. E., Yang, Z. & Cohen, W. B. Detecting trends in forest disturbance and recovery using yearly Landsat time series: 1. LandTrendr — Temporal segmentation algorithms. _Remote Sens. Environ._ **114** , 2897–2910 (2010). 

52. Chen, T. & Guestrin, C. XGBoost: A Scalable Tree Boosting System. in _Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ 785–794 (ACM, 2016). doi:10.1145/2939672.2939785. 

53. U.S. Bureau of Labor Statistics. _Consumer Price Index (CPI) Database_ . (2020). 

17 

bioRxiv preprint doi: https://doi.org/10.1101/2021.04.02.438282; this version posted November 2, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

### **Figures and Tables** 



**Figure 1.** Tree cover expansion in western U.S. rangelands (1990 - 2019). a) Net tree canopy expansion in rangelands shown in green; converted agricultural lands and built environment shown in white.  b) Cumulative net tree cover expansion; error bands represent the cumulative 95% prediction interval. c) Woodland extensification has resulted in an 8% decrease (147,700 km<sup>2</sup> ) of tree-free rangelands in the past 30 years. Intact tree-free rangelands (lands without a nearby tree seed source) have declined more rapidly than the whole as more tree-free rangelands have tree seed sources within 200 meters (defined here as vulnerable lands). 

18 

bioRxiv preprint doi: https://doi.org/10.1101/2021.04.02.438282; this version posted November 2, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 



**Figure 2.** Herbaceous production yield gap attributable to tree cover expansion: 1990 - 2019. a) Map of 2019 yield gap; converted agricultural lands and built environment shown in white. b) Total annual yield gap; includes dry herbaceous biomass (grass and forb); c) Annual lost revenue to ranching operations from tree cover expansion in the western United States. Model uncertainty is discussed in detail in the supplement. 

19 

bioRxiv preprint doi: https://doi.org/10.1101/2021.04.02.438282; this version posted November 2, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 



**Figure 3.** Localized relationships between tree cover change and herbaceous production from years 1990 - 2019 for five diverse locations across U.S rangelands. Impacts on herbaceous production from tree encroachment vary by location due to local biophysical conditions and climate. These data are calculated at the county scale and are truncated at ±20% to emphasize dominant threshold behavior. 

20 

bioRxiv preprint doi: https://doi.org/10.1101/2021.04.02.438282; this version posted November 2, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 



**Figure 4.** Local-scale evaluation of tree encroachment and yield gap development in the Loess Canyons, Nebraska (W100.44° N40.95°). Herbaceous production decreased by 34% percent between 1990 and 2019. **(Top)** Time series aerial imagery shows the dramatic expansion of Eastern Red Cedar ( _Juniperus virginiana)_ . ( **Bottom** ) Time-series and spatial trends in achievable and observed forage production show the forage yield gap’s evolution as a function of tree cover expansion. 

21 


