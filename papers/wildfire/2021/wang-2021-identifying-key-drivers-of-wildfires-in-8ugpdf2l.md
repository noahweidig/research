---
title: Identifying Key Drivers of Wildfires in the Contiguous US Using Machine Learning and Game Theory Interpretation
authors:
- Wang, Sally S.-C.
- Qian, Yun
- Leung, L. Ruby
- Zhang, Yang
year: '2021'
journal: Earth's Future
doi: 10.1029/2020EF001910
tags:
- fire modeling
- machine learning
zotero_key: 8UGPDF2L
item_type: journalArticle
url: https://onlinelibrary.wiley.com/doi/abs/10.1029/2020EF001910
source_url: 'unpaywall: https://www.ncbi.nlm.nih.gov/pmc/articles/8243942'
fulltext_status: fulltext
synced: '2026-11-06'
---

# Identifying Key Drivers of Wildfires in the Contiguous US Using Machine Learning and Game Theory Interpretation

## Abstract

Understanding the complex interrelationships between wildfire and its environmental and anthropogenic controls is crucial for wildfire modeling and management. Although machine learning (ML) models have yielded significant improvements in wildfire predictions, their limited interpretability has been an obstacle for their use in advancing understanding of wildfires. This study builds an ML model incorporating predictors of local meteorology, land-surface characteristics, and socioeconomic variables to predict monthly burned area at grid cells of 0.25° × 0.25° resolution over the contiguous United States. Besides these predictors, we construct and include predictors representing the large-scale circulation patterns conducive to wildfires, which largely improves the temporal correlations in several regions by 14%–44%. The Shapley additive explanation is introduced to quantify the contributions of the predictors to burned area. Results show a key role of longitude and latitude in delineating fire regimes with different temporal patterns of burned area. The model captures the physical relationship between burned area and vapor pressure deficit, relative humidity (RH), and energy release component (ERC), in agreement with the prior findings. Aggregating the contribution of predictor variables of all the grids by region, analyses show that ERC is the major contributor accounting for 14%–27% to large burned areas in the western US. In contrast, there is no leading factor contributing to large burned areas in the eastern US, although large-scale circulation patterns featuring less active upper-level ridge-trough and low RH two months earlier in winter contribute relatively more to large burned areas in spring in the southeastern US.

## Full text

Earths Future

. 2021 Jun 10;9(6):e2020EF001910. doi: [10.1029/2020EF001910](https://doi.org/10.1029/2020EF001910)

# Identifying Key Drivers of Wildfires in the Contiguous US Using Machine Learning and Game Theory Interpretation

[Sally S‐C Wang](https://pubmed.ncbi.nlm.nih.gov/?term="Wang%20SSC"[Author])

### Sally S‐C Wang

1Atmospheric Sciences and Global Change Division, Pacific Northwest National Laboratory, Richland, WA, USA

Find articles by [Sally S‐C Wang](https://pubmed.ncbi.nlm.nih.gov/?term="Wang%20SSC"[Author])

1,✉, [Yun Qian](https://pubmed.ncbi.nlm.nih.gov/?term="Qian%20Y"[Author])

### Yun Qian

1Atmospheric Sciences and Global Change Division, Pacific Northwest National Laboratory, Richland, WA, USA

Find articles by [Yun Qian](https://pubmed.ncbi.nlm.nih.gov/?term="Qian%20Y"[Author])

1, [L Ruby Leung](https://pubmed.ncbi.nlm.nih.gov/?term="Leung%20LR"[Author])

### L Ruby Leung

1Atmospheric Sciences and Global Change Division, Pacific Northwest National Laboratory, Richland, WA, USA

Find articles by [L Ruby Leung](https://pubmed.ncbi.nlm.nih.gov/?term="Leung%20LR"[Author])

1,✉, [Yang Zhang](https://pubmed.ncbi.nlm.nih.gov/?term="Zhang%20Y"[Author])

### Yang Zhang

2Department of Civil and Environmental Engineering, Northeastern University, Boston, MA, USA

Find articles by [Yang Zhang](https://pubmed.ncbi.nlm.nih.gov/?term="Zhang%20Y"[Author])

2

* Author information
* Article notes
* Copyright and License information

1Atmospheric Sciences and Global Change Division, Pacific Northwest National Laboratory, Richland, WA, USA

2Department of Civil and Environmental Engineering, Northeastern University, Boston, MA, USA

\*

**Correspondence to:**
S. S.‐C. Wang and L. Ruby Leung, sing-chun.wang@pnnl.gov; Ruby.Leung@pnnl.gov

✉

Corresponding author.

Revised 2021 Mar 19; Received 2020 Nov 20; Accepted 2021 May 9; Issue date 2021 Jun.

© 2021. Battelle Memorial Institute.

This is an open access article under the terms of the [http://creativecommons.org/licenses/by-nc/4.0/](https://creativecommons.org/licenses/by-nc/4.0/) License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited and is not used for commercial purposes.

[PMC Copyright notice](/about/copyright/)

PMCID: PMC8243942  PMID: [34222556](https://pubmed.ncbi.nlm.nih.gov/34222556/)

## Abstract

Understanding the complex interrelationships between wildfire and its environmental and anthropogenic controls is crucial for wildfire modeling and management. Although machine learning (ML) models have yielded significant improvements in wildfire predictions, their limited interpretability has been an obstacle for their use in advancing understanding of wildfires. This study builds an ML model incorporating predictors of local meteorology, land‐surface characteristics, and socioeconomic variables to predict monthly burned area at grid cells of 0.25° × 0.25° resolution over the contiguous United States. Besides these predictors, we construct and include predictors representing the large‐scale circulation patterns conducive to wildfires, which largely improves the temporal correlations in several regions by 14%–44%. The Shapley additive explanation is introduced to quantify the contributions of the predictors to burned area. Results show a key role of longitude and latitude in delineating fire regimes with different temporal patterns of burned area. The model captures the physical relationship between burned area and vapor pressure deficit, relative humidity (RH), and energy release component (ERC), in agreement with the prior findings. Aggregating the contribution of predictor variables of all the grids by region, analyses show that ERC is the major contributor accounting for 14%–27% to large burned areas in the western US. In contrast, there is no leading factor contributing to large burned areas in the eastern US, although large‐scale circulation patterns featuring less active upper‐level ridge‐trough and low RH two months earlier in winter contribute relatively more to large burned areas in spring in the southeastern US.

**Keywords:** machine learning, wildfire modeling

## Key Points

* US fire burned areas are well predicted by a machine learning model and SHAP improves interpretation of the contributing factors
* Including large‐scale circulation patterns conducive to wildfires as predictors improve prediction of burned areas in several regions
* Fire‐season fuel dryness and dry winters are important contributors to large burned areas in western and southeastern US, respectively

## 1. Introduction

In the past decades, the frequency and intensity of wildfires have been growing across the United States (Abatzoglou & Williams, [2016](#eft2821-bib-0003); Westerling et al., [2006](#eft2821-bib-0073)). Over 10 million acres were burned in the United States in 2017, compared to only 2.8 million acres burned in 1985 (NIFC, [2019](#eft2821-bib-0051)). In California, 14 out of the 20 largest wildfires on record have occurred over the past 15 years (CAL FIRE, [2021](#eft2821-bib-0014)). In the southeastern US (SEUS), extremely large fires along with severe drought occurred in 2011 and 2016, leading to more than 4 million acres burned. These large fires have direct impacts on the society and economy by threatening life and properties. Smokes emitted from fires can lead to degradation of air quality on both local and continental scales, with influence on human health, weather, and climate (Carvalho et al., [2011](#eft2821-bib-0015); Goodrick et al., [2013](#eft2821-bib-0030); Jaffe et al., [2008](#eft2821-bib-0034); Miranda et al., [2008](#eft2821-bib-0046); Sarangi et al., [2020](#eft2821-bib-0059); Wang et al., [2018](#eft2821-bib-0072)). Wildfire is a complex system controlled by multiple environmental and anthropogenic factors. Climate affects burned area by modifying fuel abundance and moisture of the fuels, especially during drought (Littell et al., [2009](#eft2821-bib-0041); Riley et al., [2013](#eft2821-bib-0057)). The warming and drying effects of anthropogenic climate change have been linked to increased fire frequency and size in the western US (Abatzoglou & Williams, [2016](#eft2821-bib-0003)). Besides climate, land surface characteristics, including vegetation, soil, and topography, also play a role in controlling fire occurrences and burned areas (Birch et al., [2015](#eft2821-bib-0012); Parks et al., [2014](#eft2821-bib-0052)). For example, topography affects fire development through its influence on the spread of fires and microclimate (Bigler et al., [2005](#eft2821-bib-0011); Dillon et al., [2011](#eft2821-bib-0023)). In addition to environmental controls, human activities can have predominant impacts on wildfires, directly by ignition and suppression, or indirectly through land management (Andela et al., [2017](#eft2821-bib-0008); Syphard et al., [2007](#eft2821-bib-0067)). In particular, human‐ignited fires dominate over the eastern US during spring, fall, and winter and over the western coastal areas in fall. Besides humans, lightning also plays a key role as ignition sources, especially over the mountainous areas in the western US in summer (Balch et al., [2017](#eft2821-bib-0009)). Given the complex interrelationships among fires, climate, weather, air quality, land cover and land use, and human activities, accurately predicting fire occurrences and their burned area for effective management requires a better understanding of the major factors controlling wildfires.

Numerous studies have devoted efforts to analyzing the relationships between wildfires and their environmental drivers (Abatzoglou & Kolden, [2013](#eft2821-bib-0002); Liu & Wimberly, [2015](#eft2821-bib-0043); Morton et al., [2013](#eft2821-bib-0047); Spracklen et al., [2009](#eft2821-bib-0065); Yue et al., [2013](#eft2821-bib-0077)) or human activities (Nagy et al., [2018](#eft2821-bib-0048); Zubkova et al., [2019](#eft2821-bib-0080)) in the United States using statistical methods. For instance, Urbieta et al. ([2015](#eft2821-bib-0069)) used multiple linear regression (MLR) and identified the mean seasonal FWI as the most critical variable explaining fires in the Pacific west coast of the United States, compared to other climatic variables. A recent study by Williams et al. ([2019](#eft2821-bib-0074)) demonstrated the linkage between California wildfire and warming‐driven increases in atmospheric aridity by utilizing MLR and the Pearson correlation coefficient. In these studies, regional heterogeneity and month‐to‐month variation in the fire‐driver relationships are usually neglected. Since most of these studies used traditional parametric statistical methods such as MLR, the number and variety of predictors are generally limited. Thus, the model may not be able to well capture the contributions from all the potential factors and the effects of their interactions on wildfires.

While the complexity of wildfires challenges modeling, machine learning (ML) techniques have emerged as novel tools to advance modeling and understanding of the relationships between wildfires and their predictor variables. Various ML methods have been applied to predict wildfire burned area and analyze the environmental controls of fires (Aldersley et al., [2011](#eft2821-bib-0005); Birch et al., [2015](#eft2821-bib-0012); Dillon et al., [2011](#eft2821-bib-0023); Kane et al., [2015](#eft2821-bib-0036)). Cortez and Morais ([2007](#eft2821-bib-0020)) made the first attempt to use several ML methods (decision trees, random forest, artificial neural network, and support vector machine) and fire weather data to predict burned area for every single fire in the Montesinho natural park in Portugal. Their models demonstrated promising results in predicting forest fires for fire control purposes. A recent study integrated multiple ML methods to predict monthly burned area at a spatial resolution of 0.5° × 0.5° over the South‐Central United States for the winter‐spring and summer fire season (Wang & Wang, [2020](#eft2821-bib-0071)). Their results with variable importance from random forest showed different environmental controls of burned area for the two fire seasons. Although ML methods typically perform better and have fewer pre‐assumptions than linear models such as MLR or logistic regression, they are considered as black boxes for lack of interpretability. Additionally, even though the random forest model provides variable importance, its variable importance is measured by considering the entire data set rather than calculated for each individual sample. Therefore, the key challenge remains in disclosing the black box and explaining the drivers controlling wildfires in the ML models.

This study aims at developing an ML model of monthly wildfire burned area to (a) improve understanding of the physical drivers of burned area and (b) provide a model for future investigations of the response of wildfires to global warming. To open the black box and better understand the controls of wildfires, we utilize a novel game‐theory‐based approach, the Shapley additive explanation (SHAP), to interpret the ML model used to predict wildfire burned area. The ML model is built using the Extreme Gradient Boosting (XGBoost) algorithm to predict monthly wildfire burned area in the contiguous United States (CONUS) at a spatial resolution of 0.25° × 0.25°. The model incorporates multiple factors reported to contribute to the burned area, including local meteorology, land surface characteristics, and socioeconomic variables. In addition to these factors, we also include predictors developed to describe the impact of large‐scale meteorological patterns on the burned area at the synoptic scale, which have been reported to be a critical factor influencing wildfires in previous studies (Huang et al., [2009](#eft2821-bib-0033); Pereira et al., [2005](#eft2821-bib-0053)). Besides understanding the relationships between wildfire burned area with the physical variables, this study also aims at developing a skillful model for predicting monthly burned area that can be used to project future changes in wildfires, given changes in the physical variables.

We first introduce the data (Section [2](#eft2821-sec-0020)) and methods (Section [3](#eft2821-sec-0090)) used to build and validate our ML model. We then evaluate the model performance for the whole domain and individual grids (Section [4](#eft2821-sec-0130)). The model performance with and without the predictors of large‐scale meteorological patterns is compared and discussed. The leading factors controlling the burned area for the entire data set and the effects of different predictors and their interactions on the burned area are explored and explained (global importance, Section [5.1](#eft2821-sec-0150)). In addition, we investigate the predominant drivers of large burned area for regions in the CONUS by aggregating the importance of each grid for the regions (local importance, Section [5.2](#eft2821-sec-0180)). Finally, two case studies of the SEUS and Northern California (NCA) are used to demonstrate the primary controls of burned area in these two regions during different time periods (Section [5.3](#eft2821-sec-0190)). The results highlight how our ML model with SHAP analysis of the local and global importance bridge the gaps between ML models and interpretability.

## 2. Data

### 2.1. Wildfire Data

The model developed in this study uses wildfire burned area data from the Fire Program Analysis Fire‐Occurrence Database (FPA‐FOD) (Short, [2017](#eft2821-bib-0064)). The FPA‐FOD documents daily wildfires recorded by federal, state, and local governments from 1992 to 2017. The wildfire records in the data set include discovery dates, burned area, and location in longitude and latitude. As the FPA‐FOD data collects only wildfire information, it intentionally excludes prescribed fires except the ones that escape and require suppression response. Although some small fires may be missing in the FPA‐FOD data set, the missing data are tolerable for analysis since the largest 5% of all fires account for around 85% of the total area burned (Short, [2014](#eft2821-bib-0063)).

To construct a prediction model for monthly wildfire burned area over the CONUS at a grid resolution of 0.25° × 0.25°, we use the inverse distance weighting (IDW) method (Bartier & Keller, [1996](#eft2821-bib-0010); Shepard, [1968](#eft2821-bib-0062)) to interpolate daily wildfire point data to monthly gridded burned area at 0.25° × 0.25°. Compared to the spatial averaging method, the IDW method can reduce spatial heterogeneity while ensuring the total burned area within a search distance remains the same (Kernan & Hessl, [2010](#eft2821-bib-0038)), making the resulting averaged data more predictable by models. In addition, the IDW method precludes the total burned area from being assigned to a single grid cell of ignition, particularly for the large fires, which often burn across the grid cell boundaries and may have burned areas exceeding the grid cell area. The parameterization of IDW for wildfire data is described in the supplementary. Note that grids with less than 30 months of burned area >0 are excluded (∼66% of the total number of grid cells), as there are insufficient data for the XGboost model to construct relationships between burned area and the predictors. For each grid, the interpolated burned area is normalized based on its 18‐year mean and the standard deviation to reduce the skewness and improve data symmetry. Thus, the target variable of the model is the normalized burned area.

### 2.2. Predictor Variables

We develop an empirical model at 0.25° × 0.25° grid resolution driven by several types of predictor variables, including local meteorological variables, land‐surface variables, coordinates of the grids, and socioeconomic variables at a monthly scale. In addition, we also include and design predictors that capture the influences of large‐scale meteorological patterns on wildfires. Given the data sets have different spatial resolutions, all the predictor variables are resampled to the spatial resolution of 0.25° × 0.25° by linear interpolation. A complete list of the predictor variables used in the model is provided in Table [S1](#eft2821-sup-0001).

#### 2.2.1. Local Meteorology

We include monthly average of the following variables: surface temperature, relative humidity (RH) at 2 m, daily precipitation, zonal (U) and meridional (V) components of wind at 10 m from the North American Regional Reanalysis (NARR) with a spatial resolution of 32 × 32 km2 (Mesinger et al., [2006](#eft2821-bib-0045)) (Table [S1](#eft2821-sup-0001)). We also include derived meteorological variables from the gridMET data set, with a spatial resolution of 4 × 4 km2 (Abatzoglou, [2013](#eft2821-bib-0001)), including monthly average of Palmer Drought Severity Index (PDSI), 1000‐h dead fuel moisture (FM1000), energy release component (ERC), vapor pressure deficit (VPD) (Table [S1](#eft2821-sup-0001)). ERC obtained from the gridMET data set was calculated by the fuel model G (short needle pine and heavy dead loads). These variables have been shown to influence the start, spread and, sustainability of wildfires in prior studies (Preisler et al., [2016](#eft2821-bib-0056); Riley et al., [2013](#eft2821-bib-0057); Seager et al., [2015](#eft2821-bib-0060); Williams et al., [2015](#eft2821-bib-0075)). Additionally, they can be calculated from weather forecasts or climate model outputs, enabling their use in dynamical wildfire prediction and future projection. These meteorological variables represent the effects of local meteorology on wildfires.

#### 2.2.2. Large‐Scale Meteorological Patterns

Wildfire occurrence and burned area are not only associated with local meteorology but also large‐scale meteorological patterns. Previous studies have demonstrated several large‐scale meteorological patterns related to large wildfire events, particularly at synoptic scale (Crimmins, [2006](#eft2821-bib-0021); Fauria & Johnson, [2006](#eft2821-bib-0026); Pollina et al., [2013](#eft2821-bib-0055); Trouet et al., [2009](#eft2821-bib-0068)). Although linkages between large‐scale meteorological patterns and wildfires have been demonstrated, predictors capturing the impact of large‐scale meteorological patterns have not been used in wildfire prediction. Even for predicting monthly burned area, the day‐to‐day variability of large‐scale circulation is important as it affects wildfires at shorter timescales that contribute to the monthly total burned area. For regions with episodic wildfires, synoptic weather variability may be even more important than other regions for predicting the monthly total burned area. Here, we design predictors representing the synoptic circulation factors of wildfires for several regions in the CONUS. The singular value decomposition (SVD) method from Shen et al. ([2017](#eft2821-bib-0061)) is adopted to construct the predictors by considering the spatial correlations between daily burned area in a region and meteorological variables in the surrounding grid cells.

To capture the day‐to‐day variability of synoptic weather with a lifetime of 5–7 days, we use daily meteorology to construct SVDs that represent the synoptic patterns driving the burned area variability. We consider three regions that periodically experience large wildfires, including NCA, southern Rocky Mountain areas (SRM), and SEUS, as shown in Figure [1a](#eft2821-fig-0001). Some regions in the western United States, including Pacific Northwest and Northern Rocky Mountain, are hotspots of large wildfires. They are not selected for constructing SVDs as the SVDs of NCA can represent the influences of large‐scale circulation patterns on burned area in other regions in the western US. The SVD analysis is briefly summarized here but more detailed discussion and results are included in the supplement. For each region, we first spatially average the burned area based on their discovery date in FPA‐FOD over all the grids to obtain a daily mean burned area time series representative of that region. Then, we calculate the day‐to‐day correlations between the burned area with five gridded daily meteorological variables (surface temperature, 2‐m RH, U‐wind and V‐wind at 850 hPa, and geopotential height at 500 hPa) for all 1° × 1° grid cells within the domain, yielding a correlation map for each meteorological variable (Figures [S1, S3,](#eft2821-sup-0001) and [S5](#eft2821-sup-0001)). The daily burned area and meteorological variables are deseasonalized by subtracting the 30‐day moving averages to focus on day‐to‐day, synoptic variability (Equation [S2](#eft2821-sup-0001)). The correlation matrices are then used to derive the SVD modes representing the synoptic weather systems. Time series of the first two SVD modes (SVD1 and SVD2) calculated using the meteorological fields (Equation [S4](#eft2821-sup-0001)) are then converted to predictors at a monthly time scale by calculating the monthly standard deviation of the daily SVD time series, representing the month‐to‐month variations of synoptic fluctuations and atmospheric instability (Figures [S2, S4,](#eft2821-sup-0001) and [S6](#eft2821-sup-0001)).

##### Figure 1.

![Figure 1](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3042/8243942/dbc1f9775519/EFT2-9-e2020EF001910-g001.jpg)

[Open in a new tab](figure/eft2821-fig-0001/)

Top and bottom left: The burned area map average over 2000–2017 for the (a) observation, (b) prediction, and (c) the differences between them (prediction minus observation). Bottom right: (d) The distribution of the observed and predicted burned area in the logarithm scale. The map of (a) shows the three regions that periodically experience large wildfires, including Northern California (NCA; green box), southern Rocky mountain area (SRM; red box), and southeastern US (SEUS; blue box).

For the NCA region, SVD1 features low RH, high temperature, high pressure, and northeasterly winds over the NCA region while SVD2 is characterized by low RH and northwesterly winds inland (Figures [S1](#eft2821-sup-0001) and [S2](#eft2821-sup-0001)). The two SVD modes capture a semi‐persistent synoptic pattern conductive to wildfires in NCA, consistent with prior studies (Dong et al., [2021](#eft2821-bib-0024); Zhong et al., [2020](#eft2821-bib-0079)). Time series of monthly standard deviation of the two SVDs and the monthly burned area over NCA show moderate negative correlations, indicating that large burned area is associated with the more stagnant or less stormy synoptic weather identified by the SVD analysis. Similar results are shown for the SRM region (Figures [S3](#eft2821-sup-0001) and [S4](#eft2821-sup-0001)).

The identified SVDs of SEUS are different from NCA and SRM. For SEUS (Figure [S6](#eft2821-sup-0001)), SVD1 is characterized by a bimodal pattern, corresponding to high RH, southerly winds, and high pressure over the SEUS region. SVD2 features high RH and low pressure over SEUS. SVD1 may represent a westward extension of the North Atlantic subtropical high‐pressure center, directing warm and moist southerly air flows across the eastern US. The synoptic patterns of both SVDs may favor storm development, as supported by the upper‐level ridge‐trough anomaly to be discussed further in Section [5.2](#eft2821-sec-0180). Therefore, unlike NCA and SRM, weak positive correlations between concurrent monthly burned area and monthly standard deviation of daily SVDs suggest that large variability in daily SVDs representing weather disturbances leads to larger burned area in the SEUS. Interestingly, the largest correlation of the SVDs with the monthly burned area appears when the monthly standard deviation of SVDs is at a 2‐month lag, suggesting a delayed response of wildfires to the large‐scale meteorological patterns possibly due to the effect of synoptic weather on longer memory processes such as vegetation and soil moisture dynamics that influence wildfires in later period (Figures [S6e](#eft2821-sup-0001) and [S6f](#eft2821-sup-0001)). To maximize the impact of the SVD predictors, we choose the 2‐month lag monthly standard deviation of the two SVDs of SEUS as predictors. More detailed discussions of the SVDs of SEUS are given in Section [5.2](#eft2821-sec-0180).

#### 2.2.3. Land‐Surface Properties

Several land‐surface variables are selected to represent the effects of land and vegetation on burned area, including evapotranspiration (ET), surface soil moisture, Normalized Difference Vegetation Index (NDVI), land types, and topography. These variables have been reported to influence wildfire ignition and spread by modulating fuel abundance and flammability (Abatzoglou, [2013](#eft2821-bib-0001); Chéret & Denux, [2007](#eft2821-bib-0018); Krueger et al., [2016](#eft2821-bib-0039); Van Wagtendonk & Root, [2003](#eft2821-bib-0070)). The monthly mean ET and surface soil moisture from Global Land Data Assimilation System (GLDAS‐2) with a spatial resolution of 0.25° × 0.25° is included in the model (Rodell et al., [2004](#eft2821-bib-0058)). For NDVI, we obtain NDVI at a spatial resolution of 0.05° ​× 0.05° from MODerate resolution Imaging Spectroradiometer (MODIS) instruments (Didan, [2015](#eft2821-bib-0022)).

Wildfire burned area is also related to land types and topography. Hence, we use the land cover data from the Terra and Aqua combined MODIS Land Cover Climate Modeling Grid (CMG) Version 6 data (Friedl & Sulla‐Menashe, [2015](#eft2821-bib-0029)). The land cover data is at yearly intervals from 2001 to 2018 and at a spatial resolution of 0.05° × 0.05°. We use the LAI classification scheme, which records the percentage of 10 land classes. Due to a lack of observation, the land cover data for the year 2000 uses 2001 instead. The topography data, including slope and elevation, is obtained from Amatulli et al. ([2018](#eft2821-bib-0007)), which is based on Global Multi‐resolution Terrain Elevation Data 2010 (GMTED2010) at global 250 m and the NASA Shuttle Radar Topography Mission (SRTM) at a resolution of 90 m. The data provides a fully standardized and global multivariate product of different terrain features in the spatial grid resolutions of 1, 5, 10, 50, and 100 km to support large‐scale research applications. We include the median slope and elevation at the spatial scale of 100 km in our model.

#### 2.2.4. Socioeconomic and Coordinate Variables

Anthropogenic activities are important drivers of wildfires. We include two socioeconomic variables that have been widely used to represent human effects on wildfires: Gross domestic product (GDP) per capita and population density. For the GDP per capita, we extract United States data from the gridded global data set for 2000–2015 with a spatial resolution of 5′ (Kummu et al., [2018](#eft2821-bib-0040)). For the GDP data of 2016 and 2017, we use the data of 2015 instead. The population density data is obtained from the Gridded Population of the World data collection (GPW V4) for the years 2000, 2010, 2015, and 2020, with a spatial resolution of 30″ (CIESIN‐Columbia University, [2017](#eft2821-bib-0016)). The populations in other years are linearly extrapolated by using the data of the abovementioned 4 years. Additionally, one of the human‐caused fire ignitions is camping (Narayanaraj & Wimberly, [2012](#eft2821-bib-0049); Pew & Larsen, [2001](#eft2821-bib-0054)). Therefore, we retrieve geographical information of campsites across the CONUS from the website of public campgrounds in the entire United States and Canada (<http://www.uscampgrounds.info/>). This data set includes the longitude and latitude of camp sites. We aggregate the number of campsites into the 0.25° × 0.25° grid cells.

Different regions may exhibit different wildfire regimes characterized by the pattern, frequency, and intensity of wildfires related to the seasonality of human activities, fire weather, hydroclimatology, and other factors. Predicting wildfire burned area in a large continent marked by different fire regimes is challenging. Since it may be hard to quantify or encode all the information related to the wildfire regimes, we include the longitude and latitude of the grids and the month as predictor variables to capture the information contributing to the broad spatiotemporal patterns of wildfire regimes in the CONUS. Unlike other variables representing dynamic conditions, topography, longitude, latitude, and month are static variables.

## 3. Methods

### 3.1. eXtreme Gradient Boosting Model

The eXtreme Gradient Boosting (XGBoost) is an ensemble learning method based on the idea of boosting (Chen & Guestrin, [2016](#eft2821-bib-0017)). The boosting approach incorporates multiple decision trees and combines all the predictions to obtain the correct final prediction. XGBoost is designed to prevent over‐fitting and be computationally more efficient than the gradient boosting machine, a weighted ensemble of weak prediction models. The XGBoost model builds multiple trees sequentially, with each subsequent tree intending to reduce the errors of the previous tree. As the training proceeds iteratively, new trees are added to predict the error of the prior tree. Such a fitting process is repeated several times until the stopping criterion is met (e.g., when the root mean square error [RMSE] reaches an asymptotic value). The ultimate prediction of the model is the sum of the predictions from all the trees. The formula for the prediction at step *t* and grid location *i* can be defined as follows:

|  |
| --- |
| y^it=∑k=1tfk(xi)=y^i(t−1)+ft(xi) |

where *f*
*t*(*x*
*i*) is the tree model at step *t*, y^it and y^i(t−1) are the predictions at steps *t* and *t−1*, and *x*
*i* are the predictor variables. The parameters of the model *f*
*t*(*x*
*i*) are selected by optimizing the objective function that measures how well the model fit the training data:

|  |
| --- |
| Objt=∑i=1nLt+Ωt |

which is composed of the loss function *L*
*t* and the regularizing term Ωt in each step. *L*
*t* is defined as l(yi,y^it−1+ft(xi)) and Ωt is defined as γT+12λ‖ω‖2, where γ is the regularization term which penalizes the number of leaves in the tree *T* and λ is the regularization term which penalizes ω, the weights of different leaves. There are several important parameters of XGBoost that we adjust in this study: nrounds, maximum depth, subsample, and learning rate, where nrounds is the maximum number of boosting iterations, maximum depth is the maximum depth of an individual tree, subsample is the subsample ratio of the training samples, and learning rate is the shrinkage the model does at every step (i.e., lower learning rate indicates more steps used to get the optimum). Model tuning was done by using grid search. Grid search is a tuning technique for computing the optimal values of hyperparameters. To save computational time, we use five‐fold cross‐validation for grid search. The search was first conducted for learning rate, with values of 0.1, 0.25, 0.35, and 0.5. With the optimal values of the learning rate, the search was then conducted over max\_depth and subsample with the selected ranges of 7–12 (increment of 1) and 0.2–1 (increment of 0.2), respectively. Finally, nrounds was tested from 100 to 400 (increment of 50). The XGBoost model produces the best performance with nrounds, maximum depth, subsample, and learning rate equal to 300, 9, 1, and 0.35, respectively.

### 3.2. Model Evaluation

We apply the ten‐fold cross‐validation (CV) technique to evaluate the model and avoid overfitting. The whole data set of the CONUS during 2000–2017 is randomly divided into 10 equal‐sized splits. For each round of CV, the model is trained with nine splits of the data, and the trained model is then used to predict burned area in the remaining one split. The burned area predictions are evaluated using RMSE. Since RMSE only measures the spread of the residuals, to assess the predicted spatiotemporal patterns of burned area, we also use correlation coefficient (*R*) and the index of agreement (IoA) to evaluate our model performance:

|  |
| --- |
| IoA=1−∑i=1N(yi−yi^)2∑i=1N(|yi^−y¯|+|yi−y¯|)2 |

where *y*
*i* is the observations, yi^ is prediction, y¯ is the mean of the observations. The value of IoA ranges between 0 and 1, with values closer to one indicating a better fit.

### 3.3. Shapley Additive Explanations

To identify the relative importance of the predictor variables, we use the SHAP, a novel approach to resolve and explain variable importance based on game theory (Lundberg & Lee, [2017](#eft2821-bib-0082)). When applying game theory to the explanation of variable importance, the predictor variables are considered “players” in a cooperative game in which the goal is a prediction for a single observation. Each predictor variable obtains a “payout” corresponding to its contribution from the game, so the “payout” is the corresponding variable importance, considering all possible combinations of the predictor variables. For one predictor variable, the SHAP value considers the difference in the models’ predictions *f*
*x* made by including and excluding the predictor *i* for all the combinations of predictors:

|  |
| --- |
| ϕi=∑S⊆F\{i}|S|!(F−|S|−1)!F![fx(S∪{i})−fx(S)] |

where ϕi is the weighted average of all marginal contribution of predictor *i*, *F* is the total number of features, *S* is the subset of predictors from all predictors except for predictor *i*, |S|!(F−|S|−1)!F! is the weighting factor counting the number of permutations of the subset *S*. *f*
*x*(*S*) is the expected output given the predictors subset *S*. [fx(S∪{i})−fx(S)] is the difference made by predictor *i*.

Other commonly used feature importance methods such as the gain method or split count only provide global variable importance—that is, the importance metric is limited to the entire data set but not for individual samples. Moreover, the variable importance of those methods may be inconsistent considering the order of features in the model. Unlike the abovementioned methods, SHAP values yield a relatively consistent variable importance and individual samples can have their own set of variable importance (i.e., local variable importance). Besides local variable importance, global importance is the average of the absolute SHAP values for each predictor.

## 4. Model Performance and Validation

Figure [1](#eft2821-fig-0001) shows the observed and predicted monthly burned area over the CONUS averaged over 2000–2017. The mean monthly burned area predicted by the model is 0.15 km2, while the observation is 0.17 km2. The model can well reproduce the spatial distribution of the burned area (Figures [1a](#eft2821-fig-0001) and [1b](#eft2821-fig-0001)). It successfully captures the large burned area at the border of Arizona‐New Mexico and over southern California (SCA), Pacific Northwest (PNW), and southern Florida. The spatial correlation between the observed and predicted burned area is 0.97, and the corresponding IoA is 0.96, showing a good agreement between the long‐term observations and predictions. Comparing the differences between the predicted and observed burned area averaged for 2000–2017, regions with large burned area show positive biases (Figure [1c](#eft2821-fig-0001)). As shown by the histograms, the predicted gridded burned area is within the range of observations (Figure [1d](#eft2821-fig-0001)). However, the model tends to predict fewer grids with small burned areas (log[burned area] < 2) and more grids with large burned areas (log[burned area] > 2), leading to overestimation of the averaged burned area.

Looking beyond long‐term averages, our model can reproduce the interannual variability of the burned area summed across the CONUS (Figure [2b](#eft2821-fig-0002)), with a correlation of 0.96 and IoA of 0.97. In particular, the model correctly captures several peak values, including some extreme events during May‐August 2012 and August 2015. The model also demonstrates the good performance of modeling interannual variability at the grid level, with an RMSE of 2.04 km2 and an IoA of 0.71. Correlation between the observed and predicted monthly burned area time series for each grid is displayed in Figure [2a](#eft2821-fig-0002). More than 75% of the grids have a correlation greater than 0.4 between the observed and predicted time series of burned area. Similar model evaluation metrics, including RMSE, correlation (*r*), and IoA for different subregions (Figure [7](#eft2821-fig-0007)) are summarized in Table [S2](#eft2821-sup-0001). The regional metrics were calculated based on the observation and prediction at each grid cell within the region (grid scale) as well as the time series of the total observed and predicted burned area over the region (regional scale). Better agreements with higher correlation and IoA at both scales are found over PNW and NCA. In contrast, lower correlation and IoA are generally found over the SEUS, northeastern US (NEUS), SCA, and southern Rocky Mountain (SRM), where humans are responsible for a significant fraction of fires (Keeley & Syphard, [2015](#eft2821-bib-0037); Nagy et al., [2018](#eft2821-bib-0048)). Although our model includes human‐related predictors such as population density and GDP, it is still challenging to simulate burned area without the detailed information of ignition and suppression for regions heavily influenced by human interference.

### Figure 2.

![Figure 2](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3042/8243942/29fdc5da4423/EFT2-9-e2020EF001910-g008.jpg)

[Open in a new tab](figure/eft2821-fig-0002/)

(a) The map of temporal correlation between observed and predicted burned area for each grid. Time series of observed (black) and predicted (red) burned area (b) average across the CONUS, and at grids of (c) lon: 121.625°W, lat: 44.375°, (d) lon: 122.375°W, lat: 38.375°N, (e) lon: 118.375°W, lat: 34.375°, (f) lon: 82.375°W, lat: 37.125°, (g) lon: 83.625°W, lat: 35.625°N, (h) lon: 97.375°W, lat: 30.375°N. CONUS, contiguous United States.

### Figure 7.

![Figure 7](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3042/8243942/b8b145691ce0/EFT2-9-e2020EF001910-g004.jpg)

[Open in a new tab](figure/eft2821-fig-0007/)

(a) Map of the six regions: Southern Rocky Mountain (SRM), Southern California (SCA), Northern California (NCA), Pacific Northwest (PNW), southeastern US (SEUS), and northeastern US (NEUS). (b) The relative contribution of the top five predictors to the large burned area for the six regions.

To better evaluate the model's ability to capture the temporal variability of burned area and reproduce the extreme fire events, we select several grids from different regions with large or recurrent wildfires for evaluation. Figure [2c](#eft2821-fig-0002) shows the burned area of a grid at Linn County, Oregon, where wildfires frequently occur in summer. The predicted burned area generally agrees with the observation (*r* = 0.87, IoA = 0.87), even though the peaks are slightly underestimated. For Sonoma city, California, which experienced extremely large wildfires (Figure [2d](#eft2821-fig-0002)), the largest burned area in the recorded history in October 2017 is well simulated. The temporal variability of the burned area is also well reproduced by the model (*r* = 0.93; IoA = 0.96). For a selected grid in SCA (Figure [2e](#eft2821-fig-0002)), the model can successfully identify the peak burned area from October 2008 to September 2009, but the modeled burned areas of these large fires are underestimated. Regarding the burned areas in the eastern US, their temporal variability is distinct from those in the western US. For example, for a selected grid in Kentucky, wildfires occur more frequently but with smaller burned area in general (∼<1 km2/month), compared to the episodic wildfires with larger burned areas (∼>1 km2/month) in the western US (e.g., Figure [2c](#eft2821-fig-0002)). Although the burned area patterns in the eastern US are different from those in the western US, our model is able to capture the variability of burned area well for the grid in Kentucky (Figure [2f](#eft2821-fig-0002)), with a correlation of 0.82 and an IoA of 0.89. To evaluate model performance specifically for the large burn events in the eastern US, we select two grids from North Carolina and Texas, which experienced devastating wildfires associated with severe droughts in 2016 and 2011, respectively. The model reasonably reproduces the temporal variability, and the largest burned areas for the two cases are well predicted (Figures [2g](#eft2821-fig-0002) and [2h](#eft2821-fig-0002)).

We also examine the influences of large‐scale meteorological patterns represented by SVDs by comparing the model performance with and without the SVD predictors. Overall, IoA increases from 0.53 to 0.71 and RMSE decreases from 2.33 to 2.04, when we include the SVD predictors. To further compare and quantify the impacts of the SVD predictors, we illustrate the distributions of correlations with and without the SVD predictors for the three large regions of western US, eastern US, and SEUS (Figure [S7](#eft2821-sup-0001)). Significant improvements in correlations are shown in all three regions (Table [S3](#eft2821-sup-0001)). The results suggest that the SVD predictors designed for regional wildfires (NCA, SRM, and SEUS) have broader impacts on wildfire prediction across the CONUS beyond the three regions. Specifically, the western US has the largest enhancements in median correlation increasing by 44% when we include the SVD predictors, indicating more significant impacts of large‐scale meteorology on wildfires in the western US than other regions. The results show that including the SVD predictors representing the fire‐favorable large‐scale meteorological patterns can significantly improve the model performance in simulating the temporal variability of burned area across the CONUS. Overall, the results presented collectively demonstrate good performances of the model in reproducing the spatiotemporal distribution of monthly burned area at 0.25° × 0.25° grid cells and capturing the large burned area in the extreme fire years.

## 5. Contribution of Predictors to Predicted Wildfire Burned Area

### 5.1. Global Importance of Variables

#### 5.1.1. Importance of Coordinate Variable

We first show the variable importance in our model by considering the mean absolute SHAP values described in Section [3](#eft2821-sec-0090). Figure [3](#eft2821-fig-0003) shows the 20 most important variables for the model, with larger mean absolute SHAP values indicative of larger contributions of the variables to the burned area prediction. The same plot with the standard deviation of the mean |SHAP| is provided in Figure [S8](#eft2821-sup-0001). Overall, coordinate variables of longitude and latitude are identified as the first and fourth most important variables, respectively, indicating wildfire occurrences or burned areas are highly dependent on the geographic location. As discussed in Section [2.2.4](#eft2821-sec-0080), the predictive power of geographic locations may be related to differences in wildfire regimes such as frequent small wildfires versus episodic large wildfires in different regions (Figure [2](#eft2821-fig-0002)), which will be demonstrated later. We also compare the global importance derived from SHAP and the gain method. The gain method is a classic approach that calculates the fractional contribution based on the total reduction of loss contributed by all splits involving a given feature. The variable importance calculated by the two methods are found to be generally consistent, with a correlation coefficient of 0.82. Both methods show that coordinate variables and local meteorology have higher rank than other variables (Figure [S9](#eft2821-sup-0001)).

##### Figure 3.

![Figure 3](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3042/8243942/36d6f0356817/EFT2-9-e2020EF001910-g006.jpg)

[Open in a new tab](figure/eft2821-fig-0003/)

Top 20 variables for the model based on the mean absolute SHAP value with the 95% confidence intervals. SHAP, Shapley additive explanation.

We then analyze the relationships between the predictor variables and the burned area learned by our model by showing a SHAP summary plot for each variable. In Figure [4](#eft2821-fig-0004), for each predictor variable displayed on the *y*‐axis, each colored point represents one grid at a particular month, and the SHAP values displayed on the *x*‐axis denote the contribution of that predictor variable, which can be positive or negative, to the predicted burned area. For instance, considering the RH value for a given grid and a given month, low RH would increase the burned area (positive contribution, positive SHAP values) while high RH would decrease the burned area (negative contribution, negative SHAP values). The gradient color for each point indicates the values of the predictor variables, which can vary from low (yellow) to high (purple) values. Therefore, Figure [4](#eft2821-fig-0004) provides a quick overview of the relationships between the predictor variables and their contributions to the burned area. Given RH as an example, grids/points with positive SHAP values are mostly associated with lower RH (yellow) and vice versa. On the contrary, for longitude, grids with positive SHAP values are mostly associated with large longitude values. This indicates that locations with larger longitude value (on the east side) tend to increase the predicted burned area. Similar relationship is also shown for latitude, with higher latitude value (on the north side) positively impacting the burned area.

##### Figure 4.

![Figure 4](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3042/8243942/e7e053d3e773/EFT2-9-e2020EF001910-g003.jpg)

[Open in a new tab](figure/eft2821-fig-0004/)

SHAP summary plot of the top 20 most important variables ranked by the mean absolute SHAP values. The numbers on the *y*‐axis indicate the mean |SHAP| values of the variables. SHAP, Shapley additive explanation.

To better understand the dependence of burned area on longitude and latitude, we show the SHAP dependence plots demonstrating their relationships. Since the longitude and latitude of each grid do not vary with time, we average the SHAP values corresponding to different longitude and latitude values over the study period, as shown in Figure [5](#eft2821-fig-0005). Considering only the geographical effects (i.e., averaging the SHAP values over time), grids with longitude larger than 96°W (east‐side) have positive SHAP values while grids with longitude smaller than 96°W (west‐side) have negative SHAP values. To understand how the ML model uses longitude to predict burned area, we select three grids: (1) 45.375°N, 68.625°W (Maine), (2) 45.875°N, 101.125°W (South Dakota), and (3) 34.625°N, 117.375°W (Southern California), to display the time series of normalized burned area. The three grids located in eastern, central, and western US encompass different magnitudes and opposite signs of SHAP values. As Figure [5b](#eft2821-fig-0005) shows, the normalized burned area at 45.375°N, 68.625°W (Maine) with positive SHAP values for longitude has larger temporal variability, as fires are generally smaller and occur more frequently than the other two grids with negative SHAP values and less fire occurrences. In terms of the magnitude of the SHAP values, it is found to be related to episodic events. For instance, the grid in SCA with the largest absolute SHAP value of 0.78 (red dot in Figure [5a](#eft2821-fig-0005)) has an episodic event with the extremely large normalized burned area in October 2013 (Figure [5d](#eft2821-fig-0005)). Similar patterns can be seen for latitude as well (Figures [5e–5h](#eft2821-fig-0005)). For grids with latitude larger than 43°N (north‐side), the SHAP values are positive, and the corresponding temporal patterns of burned area have smaller variability (Figure [5f](#eft2821-fig-0005)). Negative SHAP values relate to grids with latitude smaller than 43°N (south‐side), associated with larger variability in the time series of normalized burned area (Figures [5g](#eft2821-fig-0005) and [5h](#eft2821-fig-0005)). Larger magnitude of SHAP values of latitude is related to episodic events (Figures [5f](#eft2821-fig-0005) and [5h](#eft2821-fig-0005)). Based on these results, we can conclude that the sign of SHAP values of longitude and latitude distinguishes fire regimes characterized by different temporal variability of burned area while the magnitude of SHAP values distinguishes episodic and nonepisodic fire regimes. The SHAP analyses show that longitude and latitude in the ML model identify regions with different fire regimes effectively when prediction is conducted over a large continent featuring different climate/geographical regimes and human activities. The performance only degrades slightly when longitude and latitude are removed, as other predictors such as meteorology and land‐surface characteristics may include information related to regional fire regimes. This is confirmed by a sensitivity experiment that removes latitude and longitude as predictors, showing slightly degraded model performance across the CONUS, with fewer grids achieving temporal correlation larger than 0.4 (Table [S4](#eft2821-sup-0001)). In terms of model performance, RMSE increases by 6.7% and IoA decreases by 11% (Table [S4](#eft2821-sup-0001)).

##### Figure 5.

![Figure 5](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3042/8243942/5a7a7d3f2bb4/EFT2-9-e2020EF001910-g002.jpg)

[Open in a new tab](figure/eft2821-fig-0005/)

The SHAP dependence plots between SHAP values and (a) longitude and (e) latitude. Time series of the normalized burned area of the selected grid: (b) 45.375°N, 68.625°W (Maine), (c) 45.875°N, 101.125°W (South Dakota), and (d) 34.625°N, 117.375°W (Southern California), (f) 48.875°N, 119.125°W (Washington), (g) 37.625°N, 89.125°W (Illinois), and (h) 33.625°N, 114.875°W (Southern California). SHAP, Shapley additive explanation.

#### 5.1.2. Importance of Meteorological Variables

Besides the geographic variables, local meteorological variables are identified as the leading factors in determining the burned area. Among these local meteorological variables, RH and ERC emerge as the second and third most important variables, followed by temperature and VPD (Figure [3](#eft2821-fig-0003)). Note that ERC is an index of the United States National Fire Danger Rating System (NFDRS), used as a proxy for fuel dryness and fire intensity by considering the cumulative drying effect of previous weather conditions (Abatzoglou & Kolden, [2013](#eft2821-bib-0002)). These interrelated meteorological variables have been found to be the primary drivers of burned area in the western US and SEUS (Preisler et al., [2016](#eft2821-bib-0056); Riley et al., [2013](#eft2821-bib-0057); Seager et al., [2015](#eft2821-bib-0060); Williams et al., [2015](#eft2821-bib-0075)). We will discuss the interactions between these key variables and their influences on the burned area next. For the variables ranked below VPD, they contribute equally little (∼<0.05) to the burned area, illustrative of the complexity of wildfires, as multiple factors rather than one or two leading factors are involved (Figure [3](#eft2821-fig-0003)). It is also worth noting that the variable importance presented here is the absolute mean SHAP values averaged over all the available grids, but the variable importance may vary by region and time, which will be discussed in Sections [5.2](#eft2821-sec-0180) and [5.3](#eft2821-sec-0190).

The SHAP summary plot also demonstrates the relationships between the key meteorological predictors and their effects on burned area predictions, such as the inverse relationship between RH and burned area (Figure [4](#eft2821-fig-0004)). The model also demonstrates that ERC and VPD have positive influences on the burned area. However, the relationship between VPD and burned area is relatively more nonlinear, as low VPD (yellow color) is associated with both negative and positive SHAP values. Nonlinear relationships between burned area and predictors are dominant for the rest of the variables, such as temperature, 1,000‐h fuel moisture, and PDSI. Despite the nonlinear relationship between PDSI and burned area, the model captures the very large positive contributions (SHAP values > 3) of low PDSI (yellow), representing drought conditions, to the burned area.

We also investigate the relationship between the key predictors and burned area and their interactions with other predictors by showing the SHAP dependence plots (Figure [6](#eft2821-fig-0006)). Here, we first show VPD plotted against the SHAP value colored by temperature for the year 2009 (Figure [6a](#eft2821-fig-0006)). Positive contribution of VPD is associated with VPD values larger than three, with larger contribution as VPD increases afterward. The increase in VPD and its contribution to the burned area correlate with the rise in temperature, which can be explained by the Clausius‐Clapeyron relationship (exponential relationship between saturated vapor pressure and temperature). Periods with high temperature can lead to higher VPD, and the higher evaporative demand depletes water from vegetation, thereby drying fuels and increasing flammability (Holden et al., [2018](#eft2821-bib-0032); Seager et al., [2015](#eft2821-bib-0060)). The model also captures an inverse relationship between RH and burned area, as demonstrated previously (Figure [6b](#eft2821-fig-0006)). Lower RH connects with a larger positive contribution to the burned area (Figure [6b](#eft2821-fig-0006)). Unlike VPD, RH is less correlated to temperature, particularly at low RH. For instance, when RH is lower than 25%, the corresponding SHAP values are mostly positive (96%), but the temperature values can range from 276  to 313 K. Therefore, low RH is a strong indicator of fire‐favorable weather that is relatively independent of temperature (Srock et al., [2018](#eft2821-bib-0066); Yue et al., [2013](#eft2821-bib-0077)). Figure [6c](#eft2821-fig-0006) shows the SHAP dependence plot for ERC, colored by VPD. The contribution of ERC increases with increasing ERC values, but ERC values lower than 28 are associated with negative SHAP values; the SHAP values become positive when ERC is larger than 70. Larger ERC is generally associated with higher VPD, suggesting that ERC captures the effects of dry fuels on large burned area.

##### Figure 6.

![Figure 6](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3042/8243942/72b7db3b3df0/EFT2-9-e2020EF001910-g007.jpg)

[Open in a new tab](figure/eft2821-fig-0006/)

The SHAP dependence plots (a) between SHAP values and VPD, showing the interaction with temperature (color scale); (b) between SHAP values and RH, showing interaction with temperature (color scale); (c) between SHAP values and ERC, showing interaction with VPD (color scale) for the year 2009. ERC, energy release component; RH, relative humidity; SHAP, Shapley additive explanation; VPD, vapor pressure deficit.

### 5.2. Regional Importance of Variables

In the results presented in Section [5.1](#eft2821-sec-0150), interpretations of the contribution of predictor variables to the burned area are based on the whole US domain, but the contributions may vary in different regions and across different periods. In this section, we investigate the variable importance in SHAP values over six regions, including NCA, PNW, SCA, southern Rocky Mountains (SRM), NEUS, and SEUS, as shown in Figure [7a](#eft2821-fig-0007), considering their fire seasons, ecoregions, and topography. To quantify the variables’ contribution to large wildfires in the regions, for each region and predictor variable, we calculate the mean SHAP values separately for months with large fires and nonlarge fires, respectively. Large fires are defined as fires with the monthly burned area larger than the 90th percentile of the study period in the region, while nonlarge fires are fires during months excluding those with large fires. After obtaining the mean SHAP values for each variable, region, and the two defined fire magnitudes (i.e., large and nonlarge), we calculate the difference in SHAP values between large and nonlarge fires, ΔSHAPk=(SHAPlg−SHAPn)k, where SHAPlg and SHAPn are the mean SHAP values for the months with large fires and nonlarge fires, respectively, *k* is the target predictor variable we focus on. A larger magnitude of ΔSHAPk indicates a greater contribution to large wildfires. To compare the contributions of variables across different regions, for each predictor variable, we convert ΔSHAPk to the percentage of contribution to large fires, which is defined as:

|  |
| --- |
| ΔSHAPk∑i=1m|ΔSHAPm|=(SHAPlg−SHAPn)k∑i=1m|(SHAPlg−SHAPn)m|×100% |

where *m* is the total number of variables.

Figure [7b](#eft2821-fig-0007) shows the relative contribution of the first five leading variables for the six regions. Note that we mainly focus on environmental and anthropogenic factors, so this graph excludes the time‐independent coordinate variables, including longitude and latitude. The major factors contributing to large wildfires in PNW and NCA are similar, and include ERC and VPD, followed by RH and precipitation. ERC and VPD are the top two leading factors contributing around 21% and 11% to the large burned area, respectively. For SCA, the top five leading factors are identical to PNW and NCA, but the most important contributing factors are precipitation and ERC, which contribute 13% and 14% to the large burned area considering the contributions from all the predictor variables, respectively. Compared to other regions in the western US, the leading factors of SRM include ERC (27%) and RH (15%). The greatest contribution of ERC to the large burned area in the SRM area has been demonstrated in prior studies (Williams et al., [2015](#eft2821-bib-0075)). Precipitation is an essential factor for the regions in the western US, except for SRM, which can be explained by the lower precipitation amount, a larger fraction of which is accumulated as snowpack in this region, so the burned area is more influenced by snow cover (Holden et al., [2018](#eft2821-bib-0032)). Although the identified leading variables such as ERC and VPD for the wildfires in PNW and NCA are correlated, they have different physical meanings and how well they can explain wildfires can be different depending on the region and time. The ML model with SHAP values will identify the important variables that can better explain wildfires for a specific region and a particular month even though the variables are correlated.

Unlike the western US, there is no primary variable identified for the eastern US (Figure [7b](#eft2821-fig-0007)). For example, for NEUS, the five leading variables’ contributions are roughly the same (7%–9%), including ERC, Month, NDVI, RH, and temperature. Likewise, the five leading variables contribute equally to the large burned area (7%–10%) in SEUS. Among these variables, SVD1\_SElag2 contributes slightly more (10%) than the other four variables. Note that the SVD1\_SElag2 is the 2‐month lag monthly standard deviation of the first SVD of SEUS (Section [2.2.2](#eft2821-sec-0060)). The regional analysis results show that ERC is the critical leading factor in predicting large burned area, particularly for the western US, which has been observed in prior studies (Collins, [2014](#eft2821-bib-0019); Finney et al., [2011](#eft2821-bib-0028); Trouet et al., [2009](#eft2821-bib-0068)). For the eastern US, multiple factors contribute equally to large burned area without a single or several leading factors, as the contributions of the five leading factors comprise only ∼44%, while their contributions account for 47%–58% in the western US.

The SVD1\_SElag2, an indicator representing the effects of large‐scale meteorological patterns, is identified as one of the primary contributors specifically for SEUS. Here, we further analyze the impact of SVD1\_SElag2 by utilizing the results from the SHAP analyses. Figure [S10](#eft2821-sup-0001) shows the time series of SHAP value of SVD1\_SElag2 (red bar) and the normalized burned area (black line) for SEUS. Some large fires such as the fires in April 2009 are associated with large positive SHAP values of SVD1\_SElag2, indicating the increasing effects of the SVD1\_SElag2 on the burned area. In addition, most cases of coinciding large positive SHAP values and large burned area occur in spring (February–April). Therefore, we construct the composite maps of monthly meteorology associated with both large burned area and SHAP values of SVD1\_SElag2 in the springtime, hereafter named “large fire SVD.” The large burned area and SHAP values are defined as values larger than the 90th percentile over the study period. Note that since SVD1\_SElag2 represents the large‐scale meteorological pattern with a 2‐month lag, we use the meteorology with a two‐month lag in the composite map (e.g., for the large fire in April 2009, we use the meteorology of February 2009). Figure [S11](#eft2821-sup-0001) shows the mean geopotential height at 500 hPa, surface RH, and number of consecutive days without rain for the large fire SVD group, the normal group, and their difference. The normal group corresponds to all months between February and April other than those associated with the large fire SVD. The large fire SVD group shows weaker ridge‐trough at the upper level associated with lower RH and more dry spell days over SEUS than the normal group during winter (Figure [S11](#eft2821-sup-0001)). The results confirm the discussions in Section [2.2.2](#eft2821-sec-0050) that the SVD1 represents synoptic patterns with high RH, high pressure with southerly winds that are linked to development of storms, so larger variability in such synoptic patterns (i.e., large SVD1\_SElag2; larger standard deviation of daily SVD in a month) means weaker upper‐level ridge‐trough, and hence weaker disturbances and less frequent storm development in winter favorable for fires in the following spring.

### 5.3. Case Study: 2011 SEUS and 2017 NCA Large Fires

The variable contributions indicated by the SHAP values shown in the previous section only consider the average over the past 18 years, while the contributions may vary across time. Here, we further demonstrate how our model combined with the SHAP help understand the leading contributors by presenting two cases, including SEUS in 2011 and NCA in 2017. Note that the predicted burned area matches the observed burned area well for these two regions (Figure [S12](#eft2821-sup-0001)). Figure [8a](#eft2821-fig-0008) shows the time series of SHAP values of the selected variables (bar) and predicted normalized burned area (black line) for SEUS from 2011 to 2014. For the regular fire season (February–April) in SEUS (e.g., March–April 2013 and 2014), many factors contribute equally to the burned area predictions, consistent with Figure [7b](#eft2821-fig-0007). More importantly, larger positive SHAP values of PDSI (light purple) and VPD (Turquoise blue) are found in June–September 2011, which is not the usual fire season for SEUS. Note that PDSI represents the severity of drought, and VPD is associated with vegetation response to drought events. The larger contributions of PDSI and VPD correspond to the intense drought afflicting SEUS during 2011, particularly in Texas, accompanied by devastating wildfires (Jones et al., [2013](#eft2821-bib-0035); Nielsen‐Gammon, [2012](#eft2821-bib-0050)). The above results show that the interpretation of the contributing factors by SHAP is reasonable and useful.

#### Figure 8.

![Figure 8](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3042/8243942/08b86edfc577/EFT2-9-e2020EF001910-g005.jpg)

[Open in a new tab](figure/eft2821-fig-0008/)

Time series of the average SHAP values (bar) and predicted normalized burned area (line) for the (a) SEUS from 2011 to 2014 and (b) NCA from 2014 to 2017. NCA, Northern California; SEUS, southeastern US; SHAP, Shapley additive explanation.

Figure [8b](#eft2821-fig-0008) shows the time series of SHAP value of the selected variables (bar) and predicted normalized burned area (black line) for the NCA from 2014 to 2017. In contrast to the wildfires in SEUS, the fires in NCA peak regularly almost every summer (June–August). However, the driving factors of fires may vary in different years. For example, the fires in July 2014 are driven by ERC (light orange) and PDSI (light purple), while for the fires in July 2017 (red arrow), SVD2\_NCA (pink) and the SVDs of RM (dark green and brown) are the major contributing factors. As Table [1](#eft2821-tbl-0001) shows, a larger contribution of PDSI calculated by SHAP is found in July 2014, while the contribution of SVDs is more dominant in July 2017. Note that the contribution of large‐scale meteorological patterns is defined as the summation of absolute SHAP values of SVD1\_NCA, SVD2\_NCA, SVD1\_RM, and SVD2\_RM. The above findings are supported by observations as well as prior studies that NCA experienced large wildfires associated with severe drought in July 2014 but the drought signals were not observed in July 2017 (AghaKouchak et al., [2014](#eft2821-bib-0004); Hatchett et al., [2018](#eft2821-bib-0031); Yoon et al., [2016](#eft2821-bib-0076)). Overall, the results of the SHAP analyses indicate different causes of the large wildfires in NCA, with the fires in July 2014 mainly driven by drought, while the fires in July 2017 are more related to the large‐scale meteorological patterns favorable for wildfires.

#### Table 1.

The Predicted Normalized Burned Area and the SHAP Values of PDSI and the Summation of Large‐Scale Meteorological Patterns Over NCA

|  | Predicted normalized burned area | PDSI | Large‐scale meteorological patterns |
| --- | --- | --- | --- |
| July 2014 | 1.52 | 0.24 | 0.34 |
| July 2017 | 1.46 | 0.13 | 0.52 |

[Open in a new tab](table/eft2821-tbl-0001/)

Abbreviations: NCA, Northern California; PDSI,Palmer Drought Severity Index.

## 6. Discussion and Conclusion

To our knowledge, our model is the first universal ML‐based model that incorporates predictors of fire‐favorable large‐scale meteorological patterns to estimate and explain burned area and investigate the controls on wildfire activity in the CONUS. Prior studies utilizing ML methods to estimate regional burned area and analyze the relationship between fire and weather mostly focused on annual/seasonal and country/ecoregion scale (Amatulli et al., [2013](#eft2821-bib-0006); Duane et al., [2019](#eft2821-bib-0025); Spracklen et al., [2009](#eft2821-bib-0065); Yue et al., [2013](#eft2821-bib-0077)). This study predicts monthly burned area nationwide at grid cells of 0.25° × 0.25° resolution from 2000 to 2017. The predictions agree with observations well, with an RMSE of 2.04 km2 and an IoA of 0.71. On the agreement of temporal variability between observation and prediction, more than 75% of the grids have a correlation larger than 0.4 between the observed and predicted time series of monthly burned area. The model shows promising results, particularly for the grids with large or recurrent wildfires in different regions in the US. The importance of synoptic large‐scale meteorological patterns is evident in wildfire occurrence and extent. Our results demonstrate that including the predictors of SVDs to describe the influence of large‐scale meteorological patterns on burned area improves the temporal correlations in several regions by 14%–44% in terms of median values, especially for the western US. Overall, the spatial and temporal resolution, coverage, and accuracy of our model show significant improvements over other empirical and process‐based burned area models, so our model is useful for wildfire and related modeling studies.

SHAP is introduced in this study to explain the relationships between the burned area and the predictors learned by our model at the grid and the whole domain level. According to the analysis, coordinate variables, including longitude and latitude, and local meteorological variables such as ERC, RH, temperature, and VPD are the important predictors determining burned area across the whole domain. The SHAP summary plots illustrate the physical relationships between these key variables and the burned area. For example, the increase in RH leads to a decrease in the burned area, which is in agreement with the mechanistic understanding. In addition, we interpret how the model learns the effects of longitude and latitude on the burned area by the SHAP values. The analysis shows that the magnitude of the SHAP values of longitude and latitude distinguishes between episodic and nonepisodic events and the sign identifies different temporal variability of burned area, indicating the model can discriminate the temporal patterns of burned area in regions broadly demarcated east and west of ∼100°W and north and south of 40°N (Figure [5](#eft2821-fig-0005)), which roughly coincides with the US climate zones.

Our results suggest that the coordinate variables contribute to the burned area prediction by carrying critical geographical information that broadly reflects the climatology, land‐use, human activities, and so on, which differentiates the temporal characteristics of different fire regimes. Although adding longitude or latitude or month as predictors would slightly alter the ranks and contributions of the key drivers as well as the magnitude of the sensitivity of burned area to the physical variables, it is not our objective to quantify the burned area sensitivity to physical variables. As discussed in the Introduction, our goals are to better understand the relationships between burned area and the physical variables and to produce a skillful model of burned area for studying future changes in burned area given changes in the physical variables. Including longitude (latitude) and month does not obscure the physical relationships while improving the model's prediction skill. As shown in Figure [S13](#eft2821-sup-0001), the predicted burned area depends heavily on the environmental factors rather than the coordinate variables. For a grid in Sonoma City, California, where the burned area is small before 2017, our model can still capture the largest burned area in October 2017, driven by extremely dry conditions with the lowest RH anomaly of −17.

An additional sensitivity test that removes longitude, latitude, and month as predictors also shows that excluding these variables only slightly affects the ranks and the contributions of the key drivers, while most of the variables in the top 20 variable list remain on the list and their contributions do not vary by much (Figure [S14](#eft2821-sup-0001)). Furthermore, for the case study of SEUS in 2011, there are no significant differences between the models with and without the coordinates and time variables in the contributions of the leading factors (VPD and PDSI) during June–September 2011 (Figure [S15](#eft2821-sup-0001)). These results indicate that the identified major driving variables do not vary significantly, and the model learns the underlying processes and physics regardless of the inclusion of longitude, latitude, and month as predictors. Finally, the SHAP dependence plots for the model without the coordinate and time variables, are similar to those of the original model shown in Figure [6](#eft2821-fig-0006). The only differences are the sensitivities of meteorological variables to the burned area (SHAP values), which become weaker when the coordinate and time variables are removed (Figure [S16](#eft2821-sup-0001)). This may be explained by the fact that, in essence, the coordinate variables help the model differentiate regions by their fire regimes (Figure [5](#eft2821-fig-0005)). By excluding the coordinate variables, the model leverages other predictors to capture the impact of missing predictors (e.g., human activities, land use) on burned area, which may confound and weaken the physical relationships between the predictors and the burned area. Overall, comparison of the models with and without the coordinate and time variables demonstrates that the ML model can predict burned areas by learning the real processes underlying the wildfires instead of simply learning the stationary effects of the coordinate or month predictor. Additionally, including the coordinate and time variables only slightly affects the relative contributions of the key drivers but does not severely influence the interpretability of the ML model.

Besides the relationship between the key predictors and burned area, we also demonstrate the effects of interactions between predictors on the burned area. For instance, the increasing contribution of VPD to the burned area with increasing VPD is associated with the increasing temperature. Such relationships and interactions have been observed in the summer wildfires in the western US (Holden et al., [2018](#eft2821-bib-0032); Seager et al., [2015](#eft2821-bib-0060)). As most of the major wildfires in the western US occur in summer, it is expected that the warming climate will be increasingly impactful on burned area considering the relationship between VPD and temperature (Brey et al., [2020](#eft2821-bib-0013); Ficklin & Novick, [2017](#eft2821-bib-0027)). On the other hand, for the fires occurring in fall when the temperature is relatively low, VPD may not be a strong predictor, but RH may be, as shown in Figures [6](#eft2821-fig-0006) and [8](#eft2821-fig-0008) (e.g., NCA in October 2017). To evaluate whether the SHAP values for each sample are meaningful or driven by random noise, we retrain our model 20 times on the bootstrapped resample of our data set (50%) and calculate the SHAP values. Figure [S17d](#eft2821-sup-0001) shows the distributions of correlations between the SHAP values derived from the original model and the 20 retrained models for the top 20 variables in 2009. Generally, the SHAP values we derived agree with the SHAP values calculated from the resampled model, and most of the variables have median correlations larger than 0.5. We then conduct a *t*‐test to determine whether the local importance determined by SHAP is statistically significantly different from zero for each grid in a certain month, using the SHAP values from our original model and the resampled models. Figures [S17a–S17c](#eft2821-sup-0001) plot the SHAP values with a 95% confidence interval for the key predictors (VPD, RH, and ERC). For demonstration purposes, here we only show 200 points from the data set of the year 2009. In general, the SHAP values for these predictors are statistically significant and different from zero, with *p*‐values < 0.05 and the 95% confidence intervals not containing zero, especially for the grids with large SHAP values. Thus, we believe the SHAP's local importance is generally reliable and stable, particularly for the large SHAP values representing the predominant contributions.

One of the benefits of SHAP is the local interpretability—that is, SHAP values can be obtained for each grid and month, which provides a great opportunity to investigate and compare the driving factors of large burned area for different regions in the US. The results show that ERC is the most important indicator of large burned area in the western US. In contrast, the second most important contributing factor is dissimilar between different regions in the western US. For example, for NCA and PNW, VPD is more important than other predictors other than ERC, while precipitation and RH are more critical for SCA and SRM, respectively. The differences may be explained by the fact that regional burned area is more sensitive to changes in fuel aridity represented by VPD in more vegetated areas (e.g., NCA and PNW) where the fuel is abundant and less limiting than SCA and SRM where shrub and desert comprise the majority of the land surface (Littell et al., [2018](#eft2821-bib-0042)). This finding is also consistent with the results of William et al. ([2019](#eft2821-bib-0074)) that the correlation between burned area and VPD is smaller in nonforest areas than forested areas in the western US. For NEUS and SEUS, there is no dominant factor driving the large burned area, as the top five leading factors contribute equally to the large burned area. Among these factors, SVD1\_SElag2 contributes slightly more than the other factors to the burned area in the SEUS. The SVD1\_SElag2 represents large variability in the large‐scale meteorological patterns related to storm development over SEUS in winter, which disturbs stormy weather and produces relatively dry conditions favorable for fire development in the following spring. Additionally, the results are supported by prior studies showing that the dry conditions in winter and early spring (December–February) are the important factors influencing wildfires in the SEUS during spring (Wang & Wang, [2020](#eft2821-bib-0071); Zhang et al., [2014](#eft2821-bib-0078)). Finally, the two case studies show the key factors driving the large burned area in June–September 2011 for SEUS and July 2017 for NCA. Drought indicators, PDSI and VPD, are identified as imperative predictors for the large fires in September 2011 in SEUS. The predictors of large‐scale meteorological patterns that are conducive to large burned area (i.e., high GPH and low RH over western US) are dominant in July 2017, which is different from the predominant predictors (PDSI) in July 2014 for NCA.

One of the limitations of this study is that the developed model does not consider the effects of long‐term antecedent climate on wildfires (e.g., meteorological field that is 1 or 2 years earlier than current area burned), although they have been reported to influence fuel accumulation in the western US (Littell et al., [2009](#eft2821-bib-0041); Yue et al., [2013](#eft2821-bib-0077)). The predictor variables used in the model mainly represent their short‐term effects on the burned area and some of them such as soil moisture and large‐scale meteorological patterns carry useful information of environmental conditions prior to the wildfire due to their inherent persistence. Despite excluding such an effect, our model with short‐term antecedent and concurrent information can still explain most of the temporal and spatial variability in the burned area. The second limitation is that our model only considers grid cells where wildfires frequently occur (more than 30 months within 18 years), and we did not include regions with longer fire return intervals due to the lack of sufficient training data. Furthermore, human activities have been identified as one of the major controls on fire activity (Andela et al., [2017](#eft2821-bib-0008); Balch et al., [2017](#eft2821-bib-0009); Mann et al., [2016](#eft2821-bib-0044); Syphard et al., [2007](#eft2821-bib-0067)). Although our model includes predictors of population density, GDP, and number of campsites representing the anthropogenic influences on burned area, relatively poor performance is found over the SEUS as well as Central California Sierra Nevada region, where humans are responsible for a significant proportion of fires (Keeley & Syphard, [2015](#eft2821-bib-0037); Nagy et al., [2018](#eft2821-bib-0048)). Also, the two socioeconomic variables and number of campsites are not identified as leading factors by SHAP, suggesting they may not fully represent the complex human impact on the burned area. Future work is needed to develop predictors that better describe the complex effects of human activities on wildfires.

Despite the limitations mentioned above, our ML model's performance is encouraging, encapsulating the future application of ML techniques in wildfire modeling that can possibly be implemented in climate models or coupled with the weather forecast models or online‐coupled meteorology/climate and air quality model. Additionally, we have demonstrated that SHAP values are a valuable tool that improves the interpretability of ML models and understanding of the complex relationships between wildfires and the predictors, which will be helpful for future fire controls and management. The ML model in combination with the SHAP values reveals the key predictors of large fires in different regions and the influence of large‐scale meteorological patterns on the burned area.

## Supporting information

Supporting Information S1

[Click here for additional data file.](/articles/instance/8243942/bin/EFT2-9-e2020EF001910-s001.pdf) (5.9MB, pdf)

## Acknowledgments

This study was performed at PNNL and funded under Assistance Agreement no. RD835871 by the U.S. Environmental Protection Agency to Yale University through the SEARCH (Solutions for Energy, AiR, Climate, and Health) Center. It has not been formally reviewed by EPA. The views expressed in this document are solely those of the SEARCH Center and do not necessarily reflect those of the Agency. EPA does not endorse any products or commercial services mentioned in this publication. This study was also partly supported by the U.S. Department of Energy Office of Science Biological and Environmental Research through the Regional and Global Model Analysis and Multisector Dynamics program areas. PNNL is operated by Battelle Memorial Institute for the U.S. Department of Energy under contract DE‐AC06‐76RLO‐1830. Sally S.‐C. Wang thanks Danny M. Leung for providing helpful comments on the SVD analysis and Karen Short for the assistance on the FPA‐FOD fire data.

Wang, S. S.‐C.
,
Qian, Y.
,
Leung, L. R.
, &
Zhang, Y.
(2021). Identifying key drivers of wildfires in the contiguous US using machine learning and game theory interpretation. Earth's Future, 9, e2020EF001910. 10.1029/2020EF001910

## Contributor Information

Sally S.‐C. Wang, Email: sing-chun.wang@pnnl.gov.

L. Ruby Leung, Email: Ruby.Leung@pnnl.gov.

## Data Availability Statement

The data sets and model output are publicly accessible online at [https://zenodo.org/record/4467161#.YA-pEHdKjOR](https://zenodo.org/record/4467161).

## References

1. Abatzoglou, J. T.
   (2013). Development of gridded surface meteorological data for ecological applications and modelling. International Journal of Climatology, 33(1), 121–131. 10.1002/joc.3413
    [[DOI](https://doi.org/10.1002/joc.3413)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=International%20Journal%20of%20Climatology&title=Development%20of%20gridded%20surface%20meteorological%20data%20for%20ecological%20applications%20and%20modelling&author=J.%20T.%20Abatzoglou&volume=33&issue=1&publication_year=2013&pages=121-131&doi=10.1002/joc.3413&)]
2. Abatzoglou, J. T.
   , &
   Kolden, C. A.
   (2013). Relationships between climate and macroscale area burned in the western United States. International Journal of Wildland Fire, 22(7), 1003–1020. 10.1071/WF13019
    [[DOI](https://doi.org/10.1071/WF13019)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=International%20Journal%20of%20Wildland%20Fire&title=Relationships%20between%20climate%20and%20macroscale%20area%20burned%20in%20the%20western%20United%20States&author=J.%20T.%20Abatzoglou&author=C.%20A.%20Kolden&volume=22&issue=7&publication_year=2013&pages=1003-1020&doi=10.1071/WF13019&)]
3. Abatzoglou, J. T.
   , &
   Williams, A. P.
   (2016). Impact of anthropogenic climate change on wildfire across western US forests. Proceedings of the National Academy of Sciences of the United States of America, 113(42), 11770–11775. 10.1073/pnas.1607171113
    [[DOI](https://doi.org/10.1073/pnas.1607171113)] [[PMC free article](/articles/PMC5081637/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/27791053/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Proceedings%20of%20the%20National%20Academy%20of%20Sciences%20of%20the%20United%20States%20of%20America&title=Impact%20of%20anthropogenic%20climate%20change%20on%20wildfire%20across%20western%20US%20forests&author=J.%20T.%20Abatzoglou&author=A.%20P.%20Williams&volume=113&issue=42&publication_year=2016&pages=11770-11775&pmid=27791053&doi=10.1073/pnas.1607171113&)]
4. AghaKouchak, A.
   ,
   Cheng, L.
   ,
   Mazdiyasni, O.
   , &
   Farahmand, A.
   (2014). Global warming and changes in risk of concurrent climate extremes: Insights from the 2014 California drought. Geophysical Research Letters, 41(24), 8847–8852. 10.1002/2014GL062308
    [[DOI](https://doi.org/10.1002/2014GL062308)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Geophysical%20Research%20Letters&title=Global%20warming%20and%20changes%20in%20risk%20of%20concurrent%20climate%20extremes:%20Insights%20from%20the%202014%20California%20drought&author=A.%20AghaKouchak&author=L.%20Cheng&author=O.%20Mazdiyasni&author=A.%20Farahmand&volume=41&issue=24&publication_year=2014&pages=8847-8852&doi=10.1002/2014GL062308&)]
5. Aldersley, A.
   ,
   Murray, S. J.
   , &
   Cornell, S. E.
   (2011). Global and regional analysis of climate and human drivers of wildfire. The Science of the Total Environment, 409(18), 3472–3481. 10.1016/j.scitotenv.2011.05.032
    [[DOI](https://doi.org/10.1016/j.scitotenv.2011.05.032)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/21689843/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=The%20Science%20of%20the%20Total%20Environment&title=Global%20and%20regional%20analysis%20of%20climate%20and%20human%20drivers%20of%20wildfire&author=A.%20Aldersley&author=S.%20J.%20Murray&author=S.%20E.%20Cornell&volume=409&issue=18&publication_year=2011&pages=3472-3481&pmid=21689843&doi=10.1016/j.scitotenv.2011.05.032&)]
6. Amatulli, G.
   ,
   Camia, A.
   , &
   San‐Miguel‐Ayanz, J.
   (2013). Estimating future burned areas under changing climate in the EU‐Mediterranean countries. The Science of the Total Environment, 450–451, 209–222. 10.1016/j.scitotenv.2013.02.014
    [[DOI](https://doi.org/10.1016/j.scitotenv.2013.02.014)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/23500819/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=The%20Science%20of%20the%20Total%20Environment&title=Estimating%20future%20burned%20areas%20under%20changing%20climate%20in%20the%20EU%E2%80%90Mediterranean%20countries&author=G.%20Amatulli&author=A.%20Camia&author=J.%20San%E2%80%90Miguel%E2%80%90Ayanz&volume=450%E2%80%93451&publication_year=2013&pages=209-222&pmid=23500819&doi=10.1016/j.scitotenv.2013.02.014&)]
7. Amatulli, G.
   ,
   Domisch, S.
   ,
   Tuanmu, M.‐N.
   ,
   Parmentier, B.
   ,
   Ranipeta, A.
   ,
   Malczyk, J.
   , &
   Jetz, W.
   (2018). A suite of global, cross‐scale topographic variables for environmental and biodiversity modeling. Scientific Data, 5, 180040. 10.1038/sdata.2018.40
    [[DOI](https://doi.org/10.1038/sdata.2018.40)] [[PMC free article](/articles/PMC5859920/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/29557978/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Scientific%20Data&title=A%20suite%20of%20global,%20cross%E2%80%90scale%20topographic%20variables%20for%20environmental%20and%20biodiversity%20modeling&author=G.%20Amatulli&author=S.%20Domisch&author=M.%E2%80%90N.%20Tuanmu&author=B.%20Parmentier&author=A.%20Ranipeta&volume=5&publication_year=2018&pages=180040&pmid=29557978&doi=10.1038/sdata.2018.40&)]
8. Andela, N.
   ,
   Morton, D. C.
   ,
   Giglio, L.
   ,
   Chen, Y.
   ,
   van der Werf, G. R.
   ,
   Kasibhatla, P. S.
   , et al. (2017). A human‐driven decline in global burned area. Science, 356(6345), 1356–1362. 10.1126/science.aal4108
    [[DOI](https://doi.org/10.1126/science.aal4108)] [[PMC free article](/articles/PMC6047075/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/28663495/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Science&title=A%20human%E2%80%90driven%20decline%20in%20global%20burned%20area&author=N.%20Andela&author=D.%20C.%20Morton&author=L.%20Giglio&author=Y.%20Chen&author=G.%20R.%20van%20der%20Werf&volume=356&issue=6345&publication_year=2017&pages=1356-1362&pmid=28663495&doi=10.1126/science.aal4108&)]
9. Balch, J. K.
   ,
   Bradley, B. A.
   ,
   Abatzoglou, J. T.
   ,
   Nagy, R. C.
   ,
   Fusco, E. J.
   , &
   Mahood, A. L.
   (2017). Human‐started wildfires expand the fire niche across the United States. Proceedings of the National Academy of Sciences of the United States of America, 114(11), 2946–2951. 10.1073/pnas.1617394114
    [[DOI](https://doi.org/10.1073/pnas.1617394114)] [[PMC free article](/articles/PMC5358354/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/28242690/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Proceedings%20of%20the%20National%20Academy%20of%20Sciences%20of%20the%20United%20States%20of%20America&title=Human%E2%80%90started%20wildfires%20expand%20the%20fire%20niche%20across%20the%20United%20States&author=J.%20K.%20Balch&author=B.%20A.%20Bradley&author=J.%20T.%20Abatzoglou&author=R.%20C.%20Nagy&author=E.%20J.%20Fusco&volume=114&issue=11&publication_year=2017&pages=2946-2951&pmid=28242690&doi=10.1073/pnas.1617394114&)]
10. Bartier, P. M.
    , &
    Keller, C. P.
    (1996). Multivariate interpolation to incorporate thematic surface data using inverse distance weighting (IDW). Computers & Geosciences, 22(7), 795–799. 10.1016/0098-3004(96)00021-0
     [[DOI](https://doi.org/10.1016/0098-3004(96)00021-0)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Computers%20&%20Geosciences&title=Multivariate%20interpolation%20to%20incorporate%20thematic%20surface%20data%20using%20inverse%20distance%20weighting%20(IDW)&author=P.%20M.%20Bartier&author=C.%20P.%20Keller&volume=22&issue=7&publication_year=1996&pages=795-799&doi=10.1016/0098-3004(96)00021-0&)]
11. Bigler, C.
    ,
    Kulakowski, D.
    , &
    Veblen, T. T.
    (2005). Multiple disturbance interactions and drought influence fire severity in Rocky Mountain subalpine forests. Ecology, 86(11), 3018–3029. 10.1890/05-0011
     [[DOI](https://doi.org/10.1890/05-0011)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Ecology&title=Multiple%20disturbance%20interactions%20and%20drought%20influence%20fire%20severity%20in%20Rocky%20Mountain%20subalpine%20forests&author=C.%20Bigler&author=D.%20Kulakowski&author=T.%20T.%20Veblen&volume=86&issue=11&publication_year=2005&pages=3018-3029&doi=10.1890/05-0011&)]
12. Birch, D. S.
    ,
    Morgan, P.
    ,
    Kolden, C. A.
    ,
    Abatzoglou, J. T.
    ,
    Dillon, G. K.
    ,
    Hudak, A. T.
    , &
    Smith, A. M. S.
    (2015). Vegetation, topography and daily weather influenced burn severity in central Idaho and western Montana forests. Ecosphere, 6(1), 17. 10.1890/ES14-00213.1
     [[DOI](https://doi.org/10.1890/ES14-00213.1)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Ecosphere&title=Vegetation,%20topography%20and%20daily%20weather%20influenced%20burn%20severity%20in%20central%20Idaho%20and%20western%20Montana%20forests&author=D.%20S.%20Birch&author=P.%20Morgan&author=C.%20A.%20Kolden&author=J.%20T.%20Abatzoglou&author=G.%20K.%20Dillon&volume=6&issue=1&publication_year=2015&pages=17&doi=10.1890/ES14-00213.1&)]
13. Brey, S. J.
    ,
    Barnes, E. A.
    ,
    Pierce, J. R.
    ,
    Swann, A. L. S.
    , &
    Fischer, E. V.
    (2020). Past variance and future projections of the environmental conditions driving western U.S. summertime wildfire burn area. Earth's Future, 9, e2020EF001645. 10.1029/2020EF001645
     [[DOI](https://doi.org/10.1029/2020EF001645)] [[PMC free article](/articles/PMC7900977/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/33681404/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Earth's%20Future&title=Past%20variance%20and%20future%20projections%20of%20the%20environmental%20conditions%20driving%20western%20U.S.%20summertime%20wildfire%20burn%20area&author=S.%20J.%20Brey&author=E.%20A.%20Barnes&author=J.%20R.%20Pierce&author=A.%20L.%20S.%20Swann&author=E.%20V.%20Fischer&volume=9&publication_year=2020&pages=e2020EF001645&pmid=33681404&doi=10.1029/2020EF001645&)]
14. CAL FIRE
    . (2021). Top 20 largest California wildfires. California Department of Forestry and Fire Protection. Retrieved from <https://www.fire.ca.gov/stats-events/>
     [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Top%2020%20largest%20California%20wildfires&publication_year=2021&)]
15. Carvalho, A.
    ,
    Monteiro, A.
    ,
    Flannigan, M.
    ,
    Solman, S.
    ,
    Miranda, A. I.
    , &
    Borrego, C.
    (2011). Forest fires in a changing climate and their impacts on air quality. Atmospheric Environment, 45(31), 5545–5553. 10.1016/j.atmosenv.2011.05.010
     [[DOI](https://doi.org/10.1016/j.atmosenv.2011.05.010)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Atmospheric%20Environment&title=Forest%20fires%20in%20a%20changing%20climate%20and%20their%20impacts%20on%20air%20quality&author=A.%20Carvalho&author=A.%20Monteiro&author=M.%20Flannigan&author=S.%20Solman&author=A.%20I.%20Miranda&volume=45&issue=31&publication_year=2011&pages=5545-5553&doi=10.1016/j.atmosenv.2011.05.010&)]
16. Center For International Earth Science Information Network‐CIESIN‐Columbia University
    . (2017). Gridded Population of the World, Version 4 (GPWv4): Population Density, Revision 11 [Data set]. Socioeconomic Data and Applications Center (SEDAC). 10.7927/H49C6VHW
     [[DOI](https://doi.org/10.7927/H49C6VHW)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Gridded%20Population%20of%20the%20World,%20Version%204%20(GPWv4):%20Population%20Density,%20Revision%2011%20[Data%20set]&publication_year=2017&)]
17. Chen, T.
    , &
    Guestrin, C.
    (2016). XGBoost. Paper presented at the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 785–794). Association for Computing Machinery. 10.1145/2939672.2939785
     [[DOI](https://doi.org/10.1145/2939672.2939785)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=XGBoost.%20Paper%20presented%20at%20the%2022nd%20ACM%20SIGKDD%20International%20Conference%20on%20Knowledge%20Discovery%20and%20Data%20Mining&author=T.%20Chen&author=C.%20Guestrin&publication_year=2016&)]
18. Chéret, V.
    , &
    Denux, J. P.
    (2007). Mapping wildfire danger at regional scale with an index model integrating coarse spatial resolution remote sensing data. Journal of Geophysical Research, 112(G2). 10.1029/2005JG000125
     [[DOI](https://doi.org/10.1029/2005JG000125)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Journal%20of%20Geophysical%20Research&title=Mapping%20wildfire%20danger%20at%20regional%20scale%20with%20an%20index%20model%20integrating%20coarse%20spatial%20resolution%20remote%20sensing%20data&author=V.%20Ch%C3%A9ret&author=J.%20P.%20Denux&volume=112&issue=G2&publication_year=2007&doi=10.1029/2005JG000125&)]
19. Collins, B. M.
    (2014). Fire weather and large fire potential in the northern Sierra Nevada. Agricultural and Forest Meteorology, 189–190, 30–35. 10.1016/j.agrformet.2014.01.005
     [[DOI](https://doi.org/10.1016/j.agrformet.2014.01.005)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Agricultural%20and%20Forest%20Meteorology&title=Fire%20weather%20and%20large%20fire%20potential%20in%20the%20northern%20Sierra%20Nevada&author=B.%20M.%20Collins&volume=189%E2%80%93190&publication_year=2014&pages=30-35&doi=10.1016/j.agrformet.2014.01.005&)]
20. Cortez, P.
    , &
    Morais, A.
    (2007). A data mining approach to predict forest fires using meteorological data. Paper presented at the 13th Portuguese Conference on Artificial Intelligence, Portugal (pp. 512–523). [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Paper%20presented%20at%20the%2013th%20Portuguese%20Conference%20on%20Artificial%20Intelligence,%20Portugal&title=A%20data%20mining%20approach%20to%20predict%20forest%20fires%20using%20meteorological%20data&author=P.%20Cortez&author=A.%20Morais&publication_year=2007&pages=512-523&)]
21. Crimmins, M. A.
    (2006). Synoptic climatology of extreme fire‐weather conditions across the southwest United States. International Journal of Climatology, 26(8), 1001–1016. 10.1002/joc.1300
     [[DOI](https://doi.org/10.1002/joc.1300)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=International%20Journal%20of%20Climatology&title=Synoptic%20climatology%20of%20extreme%20fire%E2%80%90weather%20conditions%20across%20the%20southwest%20United%20States&author=M.%20A.%20Crimmins&volume=26&issue=8&publication_year=2006&pages=1001-1016&doi=10.1002/joc.1300&)]
22. Didan, K.
    (2015). MOD13C2 MODIS/Terra Vegetation Indices Monthly L3 Global 0.05Deg CMG V006 [Data set]. NASA EOSDIS Land Processes DAAC. 10.5067/MODIS/MOD13C2.006
     [[DOI](https://doi.org/10.5067/MODIS/MOD13C2.006)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=MOD13C2%20MODIS/Terra%20Vegetation%20Indices%20Monthly%20L3%20Global%200.05Deg%20CMG%20V006%20[Data%20set]&author=K.%20Didan&publication_year=2015&)]
23. Dillon, G. K.
    ,
    Holden, Z. A.
    ,
    Morgan, P.
    ,
    Crimmins, M. A.
    ,
    Heyerdahl, E. K.
    , &
    Luce, C. H.
    (2011). Both topography and climate affected forest and woodland burn severity in two regions of the western US, 1984 to 2006. Ecosphere, 2(12), 130. 10.1890/ES11-00271.1
     [[DOI](https://doi.org/10.1890/ES11-00271.1)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Ecosphere&title=Both%20topography%20and%20climate%20affected%20forest%20and%20woodland%20burn%20severity%20in%20two%20regions%20of%20the%20western%20US,%201984%20to%202006&author=G.%20K.%20Dillon&author=Z.%20A.%20Holden&author=P.%20Morgan&author=M.%20A.%20Crimmins&author=E.%20K.%20Heyerdahl&volume=2&issue=12&publication_year=2011&pages=130&doi=10.1890/ES11-00271.1&)]
24. Dong, L.
    ,
    Leung, L. R.
    ,
    Qian, Y.
    ,
    Zou, Y.
    ,
    Song, F.
    , &
    Chen, X.
    (2021). Meteorological environments associated with California wildfires and their potential roles in wildfire changes during 1984‐2017. Journal of Geophysical Research: Atmospheres. 126(5), e2020JD033180. [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Journal%20of%20Geophysical%20Research:%20Atmospheres&title=Meteorological%20environments%20associated%20with%20California%20wildfires%20and%20their%20potential%20roles%20in%20wildfire%20changes%20during%201984%E2%80%902017&author=L.%20Dong&author=L.%20R.%20Leung&author=Y.%20Qian&author=Y.%20Zou&author=F.%20Song&volume=126&issue=5&publication_year=2021&pages=e2020JD033180&)]
25. Duane, A.
    ,
    Kelly, L.
    ,
    Giljohann, K.
    ,
    Batllori, E.
    ,
    McCarthy, M.
    , &
    Brotons, L.
    (2019). Disentangling the influence of past fires on subsequent fires in Mediterranean landscapes. Ecosystems, 22(6), 1338–1351. 10.1007/s10021-019-00340-6
     [[DOI](https://doi.org/10.1007/s10021-019-00340-6)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Ecosystems&title=Disentangling%20the%20influence%20of%20past%20fires%20on%20subsequent%20fires%20in%20Mediterranean%20landscapes&author=A.%20Duane&author=L.%20Kelly&author=K.%20Giljohann&author=E.%20Batllori&author=M.%20McCarthy&volume=22&issue=6&publication_year=2019&pages=1338-1351&doi=10.1007/s10021-019-00340-6&)]
26. Fauria, M. M.
    , &
    Johnson, E. A.
    (2006). Large‐scale climatic patterns control large lightning fire occurrence in Canada and Alaska forest regions. Journal of Geophysical Research, 111(G4). 10.1029/2006JG000181
     [[DOI](https://doi.org/10.1029/2006JG000181)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Journal%20of%20Geophysical%20Research&title=Large%E2%80%90scale%20climatic%20patterns%20control%20large%20lightning%20fire%20occurrence%20in%20Canada%20and%20Alaska%20forest%20regions&author=M.%20M.%20Fauria&author=E.%20A.%20Johnson&volume=111&issue=G4&publication_year=2006&doi=10.1029/2006JG000181&)]
27. Ficklin, D. L.
    , &
    Novick, K. A.
    (2017). Historic and projected changes in vapor pressure deficit suggest a continental‐scale drying of the United States atmosphere. Journal of Geophysical Research ‐ D: Atmospheres, 122(4), 2061–2079. 10.1002/2016JD025855
     [[DOI](https://doi.org/10.1002/2016JD025855)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Journal%20of%20Geophysical%20Research%20%E2%80%90%20D:%20Atmospheres&title=Historic%20and%20projected%20changes%20in%20vapor%20pressure%20deficit%20suggest%20a%20continental%E2%80%90scale%20drying%20of%20the%20United%20States%20atmosphere&author=D.%20L.%20Ficklin&author=K.%20A.%20Novick&volume=122&issue=4&publication_year=2017&pages=2061-2079&doi=10.1002/2016JD025855&)]
28. Finney, M. A.
    ,
    McHugh, C. W.
    ,
    Grenfell, I. C.
    ,
    Riley, K. L.
    , &
    Short, K. C.
    (2011). A simulation of probabilistic wildfire risk components for the continental United States. Stochastic Environmental Research and Risk Assessment, 25(7), 973–1000. 10.1007/s00477-011-0462-z
     [[DOI](https://doi.org/10.1007/s00477-011-0462-z)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Stochastic%20Environmental%20Research%20and%20Risk%20Assessment&title=A%20simulation%20of%20probabilistic%20wildfire%20risk%20components%20for%20the%20continental%20United%20States&author=M.%20A.%20Finney&author=C.%20W.%20McHugh&author=I.%20C.%20Grenfell&author=K.%20L.%20Riley&author=K.%20C.%20Short&volume=25&issue=7&publication_year=2011&pages=973-1000&doi=10.1007/s00477-011-0462-z&)]
29. Friedl, M.
    , &
    Sulla‐Menashe, D.
    (2015). MCD12C1 MODIS/Terra+Aqua Land Cover Type Yearly L3 Global 0.05Deg CMG V006 [Data set]. NASA EOSDIS Land Processes DAAC. 10.5067/MODIS/MCD12C1.006
     [[DOI](https://doi.org/10.5067/MODIS/MCD12C1.006)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=MCD12C1%20MODIS/Terra+Aqua%20Land%20Cover%20Type%20Yearly%20L3%20Global%200.05Deg%20CMG%20V006%20[Data%20set]&author=M.%20Friedl&author=D.%20Sulla%E2%80%90Menashe&publication_year=2015&)]
30. Goodrick, S. L.
    ,
    Achtemeier, G. L.
    ,
    Larkin, N. K.
    ,
    Liu, Y.
    , &
    Strand, T. M.
    (2013). Modelling smoke transport from wildland fires: A review. International Journal of Wildland Fire, 22(1), 83–94. 10.1071/WF11116
     [[DOI](https://doi.org/10.1071/WF11116)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=International%20Journal%20of%20Wildland%20Fire&title=Modelling%20smoke%20transport%20from%20wildland%20fires:%20A%20review&author=S.%20L.%20Goodrick&author=G.%20L.%20Achtemeier&author=N.%20K.%20Larkin&author=Y.%20Liu&author=T.%20M.%20Strand&volume=22&issue=1&publication_year=2013&pages=83-94&doi=10.1071/WF11116&)]
31. Hatchett, B. J.
    ,
    Smith, C. M.
    ,
    Nauslar, N. J.
    , &
    Kaplan, M. L.
    (2018). Brief communication: Synoptic‐scale differences between Sundowner and Santa Ana wind regimes in the Santa Ynez Mountains, California. Natural Hazards and Earth System Sciences, 18(2), 419–427. 10.5194/nhess-18-419-2018
     [[DOI](https://doi.org/10.5194/nhess-18-419-2018)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Natural%20Hazards%20and%20Earth%20System%20Sciences&title=Brief%20communication:%20Synoptic%E2%80%90scale%20differences%20between%20Sundowner%20and%20Santa%20Ana%20wind%20regimes%20in%20the%20Santa%20Ynez%20Mountains,%20California&author=B.%20J.%20Hatchett&author=C.%20M.%20Smith&author=N.%20J.%20Nauslar&author=M.%20L.%20Kaplan&volume=18&issue=2&publication_year=2018&pages=419-427&doi=10.5194/nhess-18-419-2018&)]
32. Holden, Z. A.
    ,
    Swanson, A.
    ,
    Luce, C. H.
    ,
    Jolly, W. M.
    ,
    Maneta, M.
    ,
    Oyler, J. W.
    , et al. (2018). Decreasing fire season precipitation increased recent western US forest wildfire activity. Proceedings of the National Academy of Sciences of the United States of America, 115(36), E8349–E8357. 10.1073/pnas.1802316115
     [[DOI](https://doi.org/10.1073/pnas.1802316115)] [[PMC free article](/articles/PMC6130364/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/30126983/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Proceedings%20of%20the%20National%20Academy%20of%20Sciences%20of%20the%20United%20States%20of%20America&title=Decreasing%20fire%20season%20precipitation%20increased%20recent%20western%20US%20forest%20wildfire%20activity&author=Z.%20A.%20Holden&author=A.%20Swanson&author=C.%20H.%20Luce&author=W.%20M.%20Jolly&author=M.%20Maneta&volume=115&issue=36&publication_year=2018&pages=E8349-E8357&pmid=30126983&doi=10.1073/pnas.1802316115&)]
33. Huang, C.
    ,
    Lin, Y.‐L.
    ,
    Kaplan, M. L.
    , &
    Charney, J. J.
    (2009). Synoptic‐scale and mesoscale environments conducive to forest fires during the October 2003 extreme fire event in Southern California. Journal of Applied Meteorology and Climatology, 48(3), 553–579. 10.1175/2008JAMC1818.1
     [[DOI](https://doi.org/10.1175/2008JAMC1818.1)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Journal%20of%20Applied%20Meteorology%20and%20Climatology&title=Synoptic%E2%80%90scale%20and%20mesoscale%20environments%20conducive%20to%20forest%20fires%20during%20the%20October%202003%20extreme%20fire%20event%20in%20Southern%20California&author=C.%20Huang&author=Y.%E2%80%90L.%20Lin&author=M.%20L.%20Kaplan&author=J.%20J.%20Charney&volume=48&issue=3&publication_year=2009&pages=553-579&doi=10.1175/2008JAMC1818.1&)]
34. Jaffe, D.
    ,
    Chand, D.
    ,
    Hafner, W.
    ,
    Westerling, A.
    , &
    Spracklen, D.
    (2008). Influence of fires on O3 concentrations in the western U.S. Environmental Science & Technology, 42(16), 5885–5891. 10.1021/es800084k
     [[DOI](https://doi.org/10.1021/es800084k)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/18767640/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Environmental%20Science%20&%20Technology&title=Influence%20of%20fires%20on%20O3%20concentrations%20in%20the%20western%20U.S&author=D.%20Jaffe&author=D.%20Chand&author=W.%20Hafner&author=A.%20Westerling&author=D.%20Spracklen&volume=42&issue=16&publication_year=2008&pages=5885-5891&pmid=18767640&doi=10.1021/es800084k&)]
35. Jones, J.
    ,
    April, S.
    , &
    Brad, S.
    (2013). 2011 Texas wildfires: Common denominators of home destruction. Texas A&M Forest Service. [[Google Scholar](https://scholar.google.com/scholar_lookup?title=2011%20Texas%20wildfires:%20Common%20denominators%20of%20home%20destruction&author=J.%20Jones&author=S.%20April&author=S.%20Brad&publication_year=2013&)]
36. Kane, V. R.
    ,
    Cansler, C. A.
    ,
    Povak, N. A.
    ,
    Kane, J. T.
    ,
    McGaughey, R. J.
    ,
    Lutz, J. A.
    , et al. (2015). Mixed severity fire effects within the Rim fire: Relative importance of local climate, fire weather, topography, and forest structure. Forest Ecology and Management, 358, 62–79. 10.1016/j.foreco.2015.09.001
     [[DOI](https://doi.org/10.1016/j.foreco.2015.09.001)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Forest%20Ecology%20and%20Management&title=Mixed%20severity%20fire%20effects%20within%20the%20Rim%20fire:%20Relative%20importance%20of%20local%20climate,%20fire%20weather,%20topography,%20and%20forest%20structure&author=V.%20R.%20Kane&author=C.%20A.%20Cansler&author=N.%20A.%20Povak&author=J.%20T.%20Kane&author=R.%20J.%20McGaughey&volume=358&publication_year=2015&pages=62-79&doi=10.1016/j.foreco.2015.09.001&)]
37. Keeley, J. E.
    , &
    Syphard, A. D.
    (2015). Different fire‐climate relationships on forested and non‐forested landscapes in the Sierra Nevada ecoregion. International Journal of Wildland Fire, 24(1), 27–36. 10.1071/WF14102
     [[DOI](https://doi.org/10.1071/WF14102)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=International%20Journal%20of%20Wildland%20Fire&title=Different%20fire%E2%80%90climate%20relationships%20on%20forested%20and%20non%E2%80%90forested%20landscapes%20in%20the%20Sierra%20Nevada%20ecoregion&author=J.%20E.%20Keeley&author=A.%20D.%20Syphard&volume=24&issue=1&publication_year=2015&pages=27-36&doi=10.1071/WF14102&)]
38. Kernan, J. T.
    , &
    Hessl, A. E.
    (2010). Spatially heterogeneous estimates of fire frequency in ponderosa pine forests of Washington, USA. Fire Ecology, 6(3), 117–135. 10.4996/fireecology.0603117
     [[DOI](https://doi.org/10.4996/fireecology.0603117)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Fire%20Ecology&title=Spatially%20heterogeneous%20estimates%20of%20fire%20frequency%20in%20ponderosa%20pine%20forests%20of%20Washington,%20USA&author=J.%20T.%20Kernan&author=A.%20E.%20Hessl&volume=6&issue=3&publication_year=2010&pages=117-135&doi=10.4996/fireecology.0603117&)]
39. Krueger, E. S.
    ,
    Ochsner, T. E.
    ,
    Carlson, J. D.
    ,
    Engle, D. M.
    ,
    Twidwell, D.
    , &
    Fuhlendorf, S. D.
    (2016). Concurrent and antecedent soil moisture relate positively or negatively to probability of large wildfires depending on season. International Journal of Wildland Fire, 25(6), 657–668. 10.1071/WF15104
     [[DOI](https://doi.org/10.1071/WF15104)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=International%20Journal%20of%20Wildland%20Fire&title=Concurrent%20and%20antecedent%20soil%20moisture%20relate%20positively%20or%20negatively%20to%20probability%20of%20large%20wildfires%20depending%20on%20season&author=E.%20S.%20Krueger&author=T.%20E.%20Ochsner&author=J.%20D.%20Carlson&author=D.%20M.%20Engle&author=D.%20Twidwell&volume=25&issue=6&publication_year=2016&pages=657-668&doi=10.1071/WF15104&)]
40. Kummu, M.
    ,
    Taka, M.
    , &
    Guillaume, J. H. A.
    (2018). Gridded global datasets for Gross Domestic Product and Human Development Index over 1990‐2015. Scientific Data, 5(1), 180004. 10.1038/sdata.2018.4
     [[DOI](https://doi.org/10.1038/sdata.2018.4)] [[PMC free article](/articles/PMC5800392/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/29406518/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Scientific%20Data&title=Gridded%20global%20datasets%20for%20Gross%20Domestic%20Product%20and%20Human%20Development%20Index%20over%201990%E2%80%902015&author=M.%20Kummu&author=M.%20Taka&author=J.%20H.%20A.%20Guillaume&volume=5&issue=1&publication_year=2018&pages=180004&pmid=29406518&doi=10.1038/sdata.2018.4&)]
41. Littell, J. S.
    ,
    McKenzie, D.
    ,
    Peterson, D. L.
    , &
    Westerling, A. L.
    (2009). Climate and wildfire area burned in western U.S. ecoprovinces, 1916‐2003. Ecological Applications, 19(4), 1003–1021. 10.1890/07-1183.1
     [[DOI](https://doi.org/10.1890/07-1183.1)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/19544740/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Ecological%20Applications&title=Climate%20and%20wildfire%20area%20burned%20in%20western%20U.S.%20ecoprovinces,%201916%E2%80%902003&author=J.%20S.%20Littell&author=D.%20McKenzie&author=D.%20L.%20Peterson&author=A.%20L.%20Westerling&volume=19&issue=4&publication_year=2009&pages=1003-1021&pmid=19544740&doi=10.1890/07-1183.1&)]
42. Littell, J. S.
    ,
    McKenzie, D.
    ,
    Wan, H. Y.
    , &
    Cushman, S. A.
    (2018). Climate change and future wildfire in the western United States: An ecological approach to nonstationarity. Earth's Future, 6(8), 1097–1111. 10.1029/2018EF000878
     [[DOI](https://doi.org/10.1029/2018EF000878)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Earth's%20Future&title=Climate%20change%20and%20future%20wildfire%20in%20the%20western%20United%20States:%20An%20ecological%20approach%20to%20nonstationarity&author=J.%20S.%20Littell&author=D.%20McKenzie&author=H.%20Y.%20Wan&author=S.%20A.%20Cushman&volume=6&issue=8&publication_year=2018&pages=1097-1111&doi=10.1029/2018EF000878&)]
43. Liu, Z.
    , &
    Wimberly, M. C.
    (2015). Climatic and landscape influences on fire regimes from 1984 to 2010 in the western United States. PLoS One, 10(10), e0140839. 10.1371/journal.pone.0140839
     [[DOI](https://doi.org/10.1371/journal.pone.0140839)] [[PMC free article](/articles/PMC4605733/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/26465959/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PLoS%20One&title=Climatic%20and%20landscape%20influences%20on%20fire%20regimes%20from%201984%20to%202010%20in%20the%20western%20United%20States&author=Z.%20Liu&author=M.%20C.%20Wimberly&volume=10&issue=10&publication_year=2015&pages=e0140839&pmid=26465959&doi=10.1371/journal.pone.0140839&)]
44. Lundberg, S.
    , &
    Lee, S. I.
    (2017). A unified approach to interpreting model predictions. Advances in Neural Information Processing Systems, 4765–4774. <https://arxiv.org/abs/1705.07874>
     [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Advances%20in%20Neural%20Information%20Processing%20Systems&title=A%20unified%20approach%20to%20interpreting%20model%20predictions&author=S.%20Lundberg&author=S.%20I.%20Lee&publication_year=2017&pages=4765-4774&)]
45. Mann, M. L.
    ,
    Batllori, E.
    ,
    Moritz, M. A.
    ,
    Waller, E. K.
    ,
    Berck, P.
    ,
    Flint, A. L.
    , et al. (2016). Incorporating anthropogenic influences into fire probability models: Effects of human activity and climate change on fire activity in California. PLoS One, 11(4), e0153589. 10.1371/journal.pone.0153589
     [[DOI](https://doi.org/10.1371/journal.pone.0153589)] [[PMC free article](/articles/PMC4849771/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/27124597/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PLoS%20One&title=Incorporating%20anthropogenic%20influences%20into%20fire%20probability%20models:%20Effects%20of%20human%20activity%20and%20climate%20change%20on%20fire%20activity%20in%20California&author=M.%20L.%20Mann&author=E.%20Batllori&author=M.%20A.%20Moritz&author=E.%20K.%20Waller&author=P.%20Berck&volume=11&issue=4&publication_year=2016&pages=e0153589&pmid=27124597&doi=10.1371/journal.pone.0153589&)]
46. Mesinger, F.
    ,
    DiMego, G.
    ,
    Kalnay, E.
    ,
    Mitchell, K.
    ,
    Shafran, P. C.
    ,
    Ebisuzaki, W.
    , et al. (2006). North American regional reanalysis. Bulletin of the American Meteorological Society, 87(3), 343–360. 10.1175/BAMS-87-3-343
     [[DOI](https://doi.org/10.1175/BAMS-87-3-343)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Bulletin%20of%20the%20American%20Meteorological%20Society&title=North%20American%20regional%20reanalysis&author=F.%20Mesinger&author=G.%20DiMego&author=E.%20Kalnay&author=K.%20Mitchell&author=P.%20C.%20Shafran&volume=87&issue=3&publication_year=2006&pages=343-360&doi=10.1175/BAMS-87-3-343&)]
47. Miranda, A. I.
    ,
    Monteiro, A.
    ,
    Martins, V.
    ,
    Carvalho, A.
    ,
    Schaap, M.
    ,
    Builtjes, P.
    , &
    Borrego, C.
    (2008). Forest fires impact on air quality over Portugal. In Borrego C., & Miranda A. I., (Eds.), Air pollution modeling and its application XIX (pp. 190–198). Springer Netherlands. 10.1007/978-1-4020-8453-9\_21
     [[DOI](https://doi.org/10.1007/978-1-4020-8453-9_21)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Air%20pollution%20modeling%20and%20its%20application%20XIX&author=A.%20I.%20Miranda&author=A.%20Monteiro&author=V.%20Martins&author=A.%20Carvalho&author=M.%20Schaap&publication_year=2008&)]
48. Morton, D. C.
    ,
    Collatz, G. J.
    ,
    Wang, D.
    ,
    Randerson, J. T.
    ,
    Giglio, L.
    , &
    Chen, Y.
    (2013). Satellite‐based assessment of climate controls on US burned area. Biogeosciences, 10(1), 247–260. 10.5194/bg-10-247-2013
     [[DOI](https://doi.org/10.5194/bg-10-247-2013)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Biogeosciences&title=Satellite%E2%80%90based%20assessment%20of%20climate%20controls%20on%20US%20burned%20area&author=D.%20C.%20Morton&author=G.%20J.%20Collatz&author=D.%20Wang&author=J.%20T.%20Randerson&author=L.%20Giglio&volume=10&issue=1&publication_year=2013&pages=247-260&doi=10.5194/bg-10-247-2013&)]
49. Nagy, R. C.
    ,
    Fusco, E.
    ,
    Bradley, B.
    ,
    Abatzoglou, J. T.
    , &
    Balch, J.
    (2018). Human‐related ignitions increase the number of large wildfires across U.S. ecoregions. Fire, 1(1), 4. 10.3390/fire1010004
     [[DOI](https://doi.org/10.3390/fire1010004)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Fire&title=Human%E2%80%90related%20ignitions%20increase%20the%20number%20of%20large%20wildfires%20across%20U.S.%20ecoregions&author=R.%20C.%20Nagy&author=E.%20Fusco&author=B.%20Bradley&author=J.%20T.%20Abatzoglou&author=J.%20Balch&volume=1&issue=1&publication_year=2018&pages=4&doi=10.3390/fire1010004&)]
50. Narayanaraj, G.
    , &
    Wimberly, M. C.
    (2012). Influences of forest roads on the spatial patterns of human‐ and lightning‐caused wildfire ignitions. Applied Geography, 32(2), 878–888. 10.1016/j.apgeog.2011.09.004
     [[DOI](https://doi.org/10.1016/j.apgeog.2011.09.004)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Applied%20Geography&title=Influences%20of%20forest%20roads%20on%20the%20spatial%20patterns%20of%20human%E2%80%90%20and%20lightning%E2%80%90caused%20wildfire%20ignitions&author=G.%20Narayanaraj&author=M.%20C.%20Wimberly&volume=32&issue=2&publication_year=2012&pages=878-888&doi=10.1016/j.apgeog.2011.09.004&)]
51. Nielsen‐Gammon, J. W.
    (2012). The 2011 Texas drought. Texas Water Journal, 3(1), 59–95. [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Texas%20Water%20Journal&title=The%202011%20Texas%20drought&author=J.%20W.%20Nielsen%E2%80%90Gammon&volume=3&issue=1&publication_year=2012&pages=59-95&)]
52. NIFC
    . (2019). Total wildland fires and acres (1926‐2019). National Interagency Fire Center. Retrieved from <https://www.nifc.gov/fireInfo/fireInfo_stats_totalFires.html>
     [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Total%20wildland%20fires%20and%20acres%20(1926%E2%80%902019)&publication_year=2019&)]
53. Parks, S. A.
    ,
    Parisien, M.‐A.
    ,
    Miller, C.
    , &
    Dobrowski, S. Z.
    (2014). Fire activity and severity in the western US vary along proxy gradients representing fuel amount and fuel moisture. PLoS One, 9(6), e99699. 10.1371/journal.pone.0099699
     [[DOI](https://doi.org/10.1371/journal.pone.0099699)] [[PMC free article](/articles/PMC4062429/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/24941290/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=PLoS%20One&title=Fire%20activity%20and%20severity%20in%20the%20western%20US%20vary%20along%20proxy%20gradients%20representing%20fuel%20amount%20and%20fuel%20moisture&author=S.%20A.%20Parks&author=M.%E2%80%90A.%20Parisien&author=C.%20Miller&author=S.%20Z.%20Dobrowski&volume=9&issue=6&publication_year=2014&pages=e99699&pmid=24941290&doi=10.1371/journal.pone.0099699&)]
54. Pereira, M. G.
    ,
    Trigo, R. M.
    ,
    da Camara, C. C.
    ,
    Pereira, J. M. C.
    , &
    Leite, S. M.
    (2005). Synoptic patterns associated with large summer forest fires in Portugal. Agricultural and Forest Meteorology, 129(1), 11–25. 10.1016/j.agrformet.2004.12.007
     [[DOI](https://doi.org/10.1016/j.agrformet.2004.12.007)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Agricultural%20and%20Forest%20Meteorology&title=Synoptic%20patterns%20associated%20with%20large%20summer%20forest%20fires%20in%20Portugal&author=M.%20G.%20Pereira&author=R.%20M.%20Trigo&author=C.%20C.%20da%20Camara&author=J.%20M.%20C.%20Pereira&author=S.%20M.%20Leite&volume=129&issue=1&publication_year=2005&pages=11-25&doi=10.1016/j.agrformet.2004.12.007&)]
55. Pew, K. L.
    , &
    Larsen, C. P. S.
    (2001). GIS analysis of spatial and temporal patterns of human‐caused wildfires in the temperate rain forest of Vancouver Island, Canada. Forest Ecology and Management, 140(1), 1–18. 10.1016/S0378-1127(00)00271-1
     [[DOI](https://doi.org/10.1016/S0378-1127(00)00271-1)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Forest%20Ecology%20and%20Management&title=GIS%20analysis%20of%20spatial%20and%20temporal%20patterns%20of%20human%E2%80%90caused%20wildfires%20in%20the%20temperate%20rain%20forest%20of%20Vancouver%20Island,%20Canada&author=K.%20L.%20Pew&author=C.%20P.%20S.%20Larsen&volume=140&issue=1&publication_year=2001&pages=1-18&doi=10.1016/S0378-1127(00)00271-1&)]
56. Pollina, J. B.
    ,
    Colle, B. A.
    , &
    Charney, J. J.
    (2013). Climatology and meteorological evolution of major wildfire events over the northeast United States. Weather and Forecasting, 28(1), 175–193. 10.1175/WAF-D-12-00009.1
     [[DOI](https://doi.org/10.1175/WAF-D-12-00009.1)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Weather%20and%20Forecasting&title=Climatology%20and%20meteorological%20evolution%20of%20major%20wildfire%20events%20over%20the%20northeast%20United%20States&author=J.%20B.%20Pollina&author=B.%20A.%20Colle&author=J.%20J.%20Charney&volume=28&issue=1&publication_year=2013&pages=175-193&doi=10.1175/WAF-D-12-00009.1&)]
57. Preisler, H. K.
    ,
    Riley, K. L.
    ,
    Stonesifer, C. S.
    ,
    Calkin, D. E.
    , &
    Jolly, W. M.
    (2016). Near‐term probabilistic forecast of significant wildfire events for the western United States. International Journal of Wildland Fire, 25(11), 1169–1180. 10.1071/WF16038
     [[DOI](https://doi.org/10.1071/WF16038)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=International%20Journal%20of%20Wildland%20Fire&title=Near%E2%80%90term%20probabilistic%20forecast%20of%20significant%20wildfire%20events%20for%20the%20western%20United%20States&author=H.%20K.%20Preisler&author=K.%20L.%20Riley&author=C.%20S.%20Stonesifer&author=D.%20E.%20Calkin&author=W.%20M.%20Jolly&volume=25&issue=11&publication_year=2016&pages=1169-1180&doi=10.1071/WF16038&)]
58. Riley, K. L.
    ,
    Abatzoglou, J. T.
    ,
    Grenfell, I. C.
    ,
    Klene, A. E.
    , &
    Heinsch, F. A.
    (2013). The relationship of large fire occurrence with drought and fire danger indices in the western USA, 1984‐2008: The role of temporal scale. International Journal of Wildland Fire, 22, 894–909. 10.1071/WF12149
     [[DOI](https://doi.org/10.1071/WF12149)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=International%20Journal%20of%20Wildland%20Fire&title=The%20relationship%20of%20large%20fire%20occurrence%20with%20drought%20and%20fire%20danger%20indices%20in%20the%20western%20USA,%201984%E2%80%902008:%20The%20role%20of%20temporal%20scale&author=K.%20L.%20Riley&author=J.%20T.%20Abatzoglou&author=I.%20C.%20Grenfell&author=A.%20E.%20Klene&author=F.%20A.%20Heinsch&volume=22&publication_year=2013&pages=894-909&doi=10.1071/WF12149&)]
59. Rodell, M.
    ,
    Houser, P. R.
    ,
    Jambor, U.
    ,
    Gottschalck, J.
    ,
    Mitchell, K.
    ,
    Meng, C.‐J.
    , et al. (2004). The global land data assimilation system. Bulletin of the American Meteorological Society, 85(3), 381–394. 10.1175/BAMS-85-3-381
     [[DOI](https://doi.org/10.1175/BAMS-85-3-381)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Bulletin%20of%20the%20American%20Meteorological%20Society&title=The%20global%20land%20data%20assimilation%20system&author=M.%20Rodell&author=P.%20R.%20Houser&author=U.%20Jambor&author=J.%20Gottschalck&author=K.%20Mitchell&volume=85&issue=3&publication_year=2004&pages=381-394&doi=10.1175/BAMS-85-3-381&)]
60. Sarangi, C.
    ,
    Qian, Y.
    ,
    Leung, L. R.
    ,
    Zhang, Y.
    ,
    Zou, Y.
    , &
    Wang, Y.
    (2020). Projected increases in Boreal Wildfires Challenge Regulatory Curtailment of PM2.5 over the Eastern US by 2050. Nature Communications. [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Nature%20Communications&title=Projected%20increases%20in%20Boreal%20Wildfires%20Challenge%20Regulatory%20Curtailment%20of%20PM2.5%20over%20the%20Eastern%20US%20by%202050&author=C.%20Sarangi&author=Y.%20Qian&author=L.%20R.%20Leung&author=Y.%20Zhang&author=Y.%20Zou&publication_year=2020&)]
61. Seager, R.
    ,
    Hooks, A.
    ,
    Williams, A. P.
    ,
    Cook, B.
    ,
    Nakamura, J.
    , &
    Henderson, N.
    (2015). Climatology, variability, and trends in the U.S. vapor pressure deficit, an important fire‐related meteorological quantity. Journal of Applied Meteorology and Climatology, 54(6), 1121–1141. 10.1175/JAMC-D-14-0321.1
     [[DOI](https://doi.org/10.1175/JAMC-D-14-0321.1)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Journal%20of%20Applied%20Meteorology%20and%20Climatology&title=Climatology,%20variability,%20and%20trends%20in%20the%20U.S.%20vapor%20pressure%20deficit,%20an%20important%20fire%E2%80%90related%20meteorological%20quantity&author=R.%20Seager&author=A.%20Hooks&author=A.%20P.%20Williams&author=B.%20Cook&author=J.%20Nakamura&volume=54&issue=6&publication_year=2015&pages=1121-1141&doi=10.1175/JAMC-D-14-0321.1&)]
62. Shen, L.
    ,
    Mickley, L. J.
    , &
    Murray, L. T.
    (2017). Influence of 2000‐2050 climate change on particulate matter in the United States: Results from a new statistical model. Atmospheric Chemistry and Physics, 17(6), 4355–4367. 10.5194/acp-17-4355-2017
     [[DOI](https://doi.org/10.5194/acp-17-4355-2017)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Atmospheric%20Chemistry%20and%20Physics&title=Influence%20of%202000%E2%80%902050%20climate%20change%20on%20particulate%20matter%20in%20the%20United%20States:%20Results%20from%20a%20new%20statistical%20model&author=L.%20Shen&author=L.%20J.%20Mickley&author=L.%20T.%20Murray&volume=17&issue=6&publication_year=2017&pages=4355-4367&doi=10.5194/acp-17-4355-2017&)]
63. Shepard, D.
    (1968). A two‐dimensional interpolation function for irregularly‐spaced data. Paper presented at the 1968 23rd ACM National Conference(pp. 517–524). Association for Computing Machinery. 10.1145/800186.810616
     [[DOI](https://doi.org/10.1145/800186.810616)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Paper%20presented%20at%20the%201968%2023rd%20ACM%20National%20Conference&author=D.%20Shepard&publication_year=1968&)]
64. Short, K. C.
    (2014). A spatial database of wildfires in the United States, 1992‐2011. Earth System Science Data, 6, 1–27. 10.5194/essd-6-1-2014
     [[DOI](https://doi.org/10.5194/essd-6-1-2014)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Earth%20System%20Science%20Data&title=A%20spatial%20database%20of%20wildfires%20in%20the%20United%20States,%201992%E2%80%902011&author=K.%20C.%20Short&volume=6&publication_year=2014&pages=1-27&doi=10.5194/essd-6-1-2014&)]
65. Short, K. C.
    (2017). Spatial wildfire occurrence data for the United States, 1992‐2015 [FPA\_FOD\_20170508] (4th ed.) [Data set]. Forest Service Research Data Archive. 10.2737/RDS-2013-0009.4
     [[DOI](https://doi.org/10.2737/RDS-2013-0009.4)] [[Google Scholar](https://scholar.google.com/scholar_lookup?title=Spatial%20wildfire%20occurrence%20data%20for%20the%20United%20States,%201992%E2%80%902015%20[FPA_FOD_20170508]%20(4th%20ed.)%20[Data%20set]&author=K.%20C.%20Short&publication_year=2017&)]
66. Spracklen, D. V.
    ,
    Mickley, L. J.
    ,
    Logan, J. A.
    ,
    Hudman, R. C.
    ,
    Yevich, R.
    ,
    Flannigan, M. D.
    , &
    Westerling, A. L.
    (2009). Impacts of climate change from 2000 to 2050 on wildfire activity and carbonaceous aerosol concentrations in the western United States. Journal of Geophysical Research, 114(D20). 10.1029/2008JD010966
     [[DOI](https://doi.org/10.1029/2008JD010966)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Journal%20of%20Geophysical%20Research&title=Impacts%20of%20climate%20change%20from%202000%20to%202050%20on%20wildfire%20activity%20and%20carbonaceous%20aerosol%20concentrations%20in%20the%20western%20United%20States&author=D.%20V.%20Spracklen&author=L.%20J.%20Mickley&author=J.%20A.%20Logan&author=R.%20C.%20Hudman&author=R.%20Yevich&volume=114&issue=D20&publication_year=2009&doi=10.1029/2008JD010966&)]
67. Srock, A.
    ,
    Charney, J.
    ,
    Potter, B.
    , &
    Goodrick, S.
    (2018). The hot‐dry‐windy index: A new fire weather index. Atmosphere, 9(7), 279. 10.3390/atmos9070279
     [[DOI](https://doi.org/10.3390/atmos9070279)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Atmosphere&title=The%20hot%E2%80%90dry%E2%80%90windy%20index:%20A%20new%20fire%20weather%20index&author=A.%20Srock&author=J.%20Charney&author=B.%20Potter&author=S.%20Goodrick&volume=9&issue=7&publication_year=2018&pages=279&doi=10.3390/atmos9070279&)]
68. Syphard, A. D.
    ,
    Radeloff, V. C.
    ,
    Keeley, J. E.
    ,
    Hawbaker, T. J.
    ,
    Clayton, M. K.
    ,
    Stewart, S. I.
    , &
    Hammer, R. B.
    (2007). Human influence on California fire regimes. Ecological Applications, 17(5), 1388–1402. 10.1890/06-1128.1
     [[DOI](https://doi.org/10.1890/06-1128.1)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/17708216/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Ecological%20Applications&title=Human%20influence%20on%20California%20fire%20regimes&author=A.%20D.%20Syphard&author=V.%20C.%20Radeloff&author=J.%20E.%20Keeley&author=T.%20J.%20Hawbaker&author=M.%20K.%20Clayton&volume=17&issue=5&publication_year=2007&pages=1388-1402&pmid=17708216&doi=10.1890/06-1128.1&)]
69. Trouet, V.
    ,
    Taylor, A. H.
    ,
    Carleton, A. M.
    , &
    Skinner, C. N.
    (2009). Interannual variations in fire weather, fire extent, and synoptic‐scale circulation patterns in northern California and Oregon. Theoretical and Applied Climatology, 95, 349–360. 10.1007/s00704-008-0012-x
     [[DOI](https://doi.org/10.1007/s00704-008-0012-x)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Theoretical%20and%20Applied%20Climatology&title=Interannual%20variations%20in%20fire%20weather,%20fire%20extent,%20and%20synoptic%E2%80%90scale%20circulation%20patterns%20in%20northern%20California%20and%20Oregon&author=V.%20Trouet&author=A.%20H.%20Taylor&author=A.%20M.%20Carleton&author=C.%20N.%20Skinner&volume=95&publication_year=2009&pages=349-360&doi=10.1007/s00704-008-0012-x&)]
70. Urbieta, I. R.
    ,
    Zavala, G.
    ,
    Bedia, J.
    ,
    Gutiérrez, J. M.
    ,
    Miguel‐Ayanz, J. S.
    ,
    Camia, A.
    , et al. (2015). Fire activity as a function of fire‐weather seasonal severity and antecedent climate across spatial scales in southern Europe and Pacific western USA. Environmental Research Letters, 10(11), 114013. 10.1088/1748-9326/10/11/114013
     [[DOI](https://doi.org/10.1088/1748-9326/10/11/114013)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Environmental%20Research%20Letters&title=Fire%20activity%20as%20a%20function%20of%20fire%E2%80%90weather%20seasonal%20severity%20and%20antecedent%20climate%20across%20spatial%20scales%20in%20southern%20Europe%20and%20Pacific%20western%20USA&author=I.%20R.%20Urbieta&author=G.%20Zavala&author=J.%20Bedia&author=J.%20M.%20Guti%C3%A9rrez&author=J.%20S.%20Miguel%E2%80%90Ayanz&volume=10&issue=11&publication_year=2015&pages=114013&doi=10.1088/1748-9326/10/11/114013&)]
71. Van Wagtendonk, J. W.
    , &
    Root, R. R.
    (2003). The use of multi‐temporal Landsat Normalized Difference Vegetation Index (NDVI) data for mapping fuel models in Yosemite National Park, USA. International Journal of Remote Sensing, 24(8), 1639–1651. 10.1080/01431160210144679
     [[DOI](https://doi.org/10.1080/01431160210144679)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=International%20Journal%20of%20Remote%20Sensing&title=The%20use%20of%20multi%E2%80%90temporal%20Landsat%20Normalized%20Difference%20Vegetation%20Index%20(NDVI)%20data%20for%20mapping%20fuel%20models%20in%20Yosemite%20National%20Park,%20USA&author=J.%20W.%20Van%20Wagtendonk&author=R.%20R.%20Root&volume=24&issue=8&publication_year=2003&pages=1639-1651&doi=10.1080/01431160210144679&)]
72. Wang, S. S.‐C.
    , &
    Wang, Y.
    (2020). Quantifying the effects of environmental factors on wildfire burned area in the south central US using integrated machine learning techniques. Atmospheric Chemistry and Physics, 20(18), 11065–11087. 10.5194/acp-20-11065-2020
     [[DOI](https://doi.org/10.5194/acp-20-11065-2020)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Atmospheric%20Chemistry%20and%20Physics&title=Quantifying%20the%20effects%20of%20environmental%20factors%20on%20wildfire%20burned%20area%20in%20the%20south%20central%20US%20using%20integrated%20machine%20learning%20techniques&author=S.%20S.%E2%80%90C.%20Wang&author=Y.%20Wang&volume=20&issue=18&publication_year=2020&pages=11065-11087&doi=10.5194/acp-20-11065-2020&)]
73. Wang, S. S.‐C.
    ,
    Wang, Y.
    ,
    Estes, M.
    ,
    Lei, R.
    ,
    Talbot, R.
    ,
    Zhu, L.
    , &
    Hou, P.
    (2018). Transport of Central American fire emissions to the U.S. Gulf Coast: Climatological pathways and impacts on ozone and PM2.5. Journal of Geophysical Research ‐ D: Atmospheres, 123(15), 8344–8361. 10.1029/2018JD028684
     [[DOI](https://doi.org/10.1029/2018JD028684)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Journal%20of%20Geophysical%20Research%20%E2%80%90%20D:%20Atmospheres&title=Transport%20of%20Central%20American%20fire%20emissions%20to%20the%20U.S.%20Gulf%20Coast:%20Climatological%20pathways%20and%20impacts%20on%20ozone%20and%20PM2.5&author=S.%20S.%E2%80%90C.%20Wang&author=Y.%20Wang&author=M.%20Estes&author=R.%20Lei&author=R.%20Talbot&volume=123&issue=15&publication_year=2018&pages=8344-8361&doi=10.1029/2018JD028684&)]
74. Westerling, A. L.
    ,
    Hidalgo, H. G.
    ,
    Cayan, D. R.
    , &
    Swetnam, T. W.
    (2006). Warming and earlier spring increase western U.S. forest wildfire activity. Science, 313(5789), 940–943. 10.1126/science.1128834
     [[DOI](https://doi.org/10.1126/science.1128834)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/16825536/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Science&title=Warming%20and%20earlier%20spring%20increase%20western%20U.S.%20forest%20wildfire%20activity&author=A.%20L.%20Westerling&author=H.%20G.%20Hidalgo&author=D.%20R.%20Cayan&author=T.%20W.%20Swetnam&volume=313&issue=5789&publication_year=2006&pages=940-943&pmid=16825536&doi=10.1126/science.1128834&)]
75. Williams, A. P.
    ,
    Abatzoglou, J. T.
    ,
    Gershunov, A.
    ,
    Guzman‐Morales, J.
    ,
    Bishop, D. A.
    ,
    Balch, J. K.
    , &
    Lettenmaier, D. P.
    (2019). Observed impacts of anthropogenic climate change on wildfire in California. Earth's Future, 7(8), 892–910. 10.1029/2019EF001210
     [[DOI](https://doi.org/10.1029/2019EF001210)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Earth's%20Future&title=Observed%20impacts%20of%20anthropogenic%20climate%20change%20on%20wildfire%20in%20California&author=A.%20P.%20Williams&author=J.%20T.%20Abatzoglou&author=A.%20Gershunov&author=J.%20Guzman%E2%80%90Morales&author=D.%20A.%20Bishop&volume=7&issue=8&publication_year=2019&pages=892-910&doi=10.1029/2019EF001210&)]
76. Williams, A. P.
    ,
    Seager, R.
    ,
    Macalady, A. K.
    ,
    Berkelhammer, M.
    ,
    Crimmins, M. A.
    ,
    Swetnam, T. W.
    , et al. (2015). Correlations between components of the water balance and burned area reveal new insights for predicting forest fire area in the southwest United States. International Journal of Wildland Fire, 24(1), 14–26. 10.1071/WF14023
     [[DOI](https://doi.org/10.1071/WF14023)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=International%20Journal%20of%20Wildland%20Fire&title=Correlations%20between%20components%20of%20the%20water%20balance%20and%20burned%20area%20reveal%20new%20insights%20for%20predicting%20forest%20fire%20area%20in%20the%20southwest%20United%20States&author=A.%20P.%20Williams&author=R.%20Seager&author=A.%20K.%20Macalady&author=M.%20Berkelhammer&author=M.%20A.%20Crimmins&volume=24&issue=1&publication_year=2015&pages=14-26&doi=10.1071/WF14023&)]
77. Yoon, J.‐H.
    ,
    Kravitz, B.
    ,
    Rasch, P. J.
    ,
    Simon Wang, S.‐Y.
    ,
    Gillies, R. R.
    , &
    Hipps, L.
    (2016). Extreme fire season in California: A glimpse into the future?. Bulletin of the American Meteorological Society, 96(12), S5–S9. 10.1175/BAMS-EEE\_2014\_ch2.1
     [[DOI](https://doi.org/10.1175/BAMS-EEE_2014_ch2.1)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Bulletin%20of%20the%20American%20Meteorological%20Society&title=Extreme%20fire%20season%20in%20California:%20A%20glimpse%20into%20the%20future?&author=J.%E2%80%90H.%20Yoon&author=B.%20Kravitz&author=P.%20J.%20Rasch&author=S.%E2%80%90Y.%20Simon%20Wang&author=R.%20R.%20Gillies&volume=96&issue=12&publication_year=2016&pages=S5-S9&doi=10.1175/BAMS-EEE_2014_ch2.1&)]
78. Yue, X.
    ,
    Mickley, L. J.
    ,
    Logan, J. A.
    , &
    Kaplan, J. O.
    (2013). Ensemble projections of wildfire activity and carbonaceous aerosol concentrations over the western United States in the mid‐21st century. Atmospheric Environment, 77, 767–780. 10.1016/j.atmosenv.2013.06.003
     [[DOI](https://doi.org/10.1016/j.atmosenv.2013.06.003)] [[PMC free article](/articles/PMC3763857/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/24015109/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Atmospheric%20Environment&title=Ensemble%20projections%20of%20wildfire%20activity%20and%20carbonaceous%20aerosol%20concentrations%20over%20the%20western%20United%20States%20in%20the%20mid%E2%80%9021st%20century&author=X.%20Yue&author=L.%20J.%20Mickley&author=J.%20A.%20Logan&author=J.%20O.%20Kaplan&volume=77&publication_year=2013&pages=767-780&pmid=24015109&doi=10.1016/j.atmosenv.2013.06.003&)]
79. Zhang, X.
    ,
    Kondragunta, S.
    , &
    Roy, D. P.
    (2014). Interannual variation in biomass burning and fire seasonality derived from geostationary satellite data across the contiguous United States from 1995 to 2011. Journal of Geophysical Research: Biogeosciences, 119(6), 1147–1162. 10.1002/2013JG002518
     [[DOI](https://doi.org/10.1002/2013JG002518)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Journal%20of%20Geophysical%20Research:%20Biogeosciences&title=Interannual%20variation%20in%20biomass%20burning%20and%20fire%20seasonality%20derived%20from%20geostationary%20satellite%20data%20across%20the%20contiguous%20United%20States%20from%201995%20to%202011&author=X.%20Zhang&author=S.%20Kondragunta&author=D.%20P.%20Roy&volume=119&issue=6&publication_year=2014&pages=1147-1162&doi=10.1002/2013JG002518&)]
80. Zhong, S.
    ,
    Yu, L.
    ,
    Heilman, W. E.
    ,
    Bian, X.
    , &
    Fromm, H.
    (2020). Synoptic weather patterns for large wildfires in the northwestern United States—A climatological analysis using three classification methods. Theoretical and Applied Climatology, 141, 1057–1073. 10.1007/s00704-020-03235-y
     [[DOI](https://doi.org/10.1007/s00704-020-03235-y)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Theoretical%20and%20Applied%20Climatology&title=Synoptic%20weather%20patterns%20for%20large%20wildfires%20in%20the%20northwestern%20United%20States%E2%80%94A%20climatological%20analysis%20using%20three%20classification%20methods&author=S.%20Zhong&author=L.%20Yu&author=W.%20E.%20Heilman&author=X.%20Bian&author=H.%20Fromm&volume=141&publication_year=2020&pages=1057-1073&doi=10.1007/s00704-020-03235-y&)]
81. Zubkova, M.
    ,
    Boschetti, L.
    ,
    Abatzoglou, J. T.
    , &
    Giglio, L.
    (2019). Changes in fire activity in Africa from 2002 to 2016 and their potential drivers. Geophysical Research Letters, 46(13), 7643–7653. 10.1029/2019GL083469
     [[DOI](https://doi.org/10.1029/2019GL083469)] [[PMC free article](/articles/PMC7241591/)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/32440032/)] [[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Geophysical%20Research%20Letters&title=Changes%20in%20fire%20activity%20in%20Africa%20from%202002%20to%202016%20and%20their%20potential%20drivers&author=M.%20Zubkova&author=L.%20Boschetti&author=J.%20T.%20Abatzoglou&author=L.%20Giglio&volume=46&issue=13&publication_year=2019&pages=7643-7653&pmid=32440032&doi=10.1029/2019GL083469&)]

## Associated Data

*This section collects any data citations, data availability statements, or supplementary materials included in this article.*

### Supplementary Materials

Supporting Information S1

[Click here for additional data file.](/articles/instance/8243942/bin/EFT2-9-e2020EF001910-s001.pdf) (5.9MB, pdf)

### Data Availability Statement

The data sets and model output are publicly accessible online at [https://zenodo.org/record/4467161#.YA-pEHdKjOR](https://zenodo.org/record/4467161).
