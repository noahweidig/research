---
title: 'Multi-scale drivers of wildfire burn severity in Central Zagros: insights from remote sensing and machine learning'
authors:
- Shahidinejad, F
- Jourgholami, M
- Pourhanifeh, MM
- Esfandyar, A
year: '2026'
journal: iForest - Biogeosciences and Forestry
doi: 10.3832/ifor5027-019
tags:
- drivers
- fire severity
- machine learning
- wildfire
zotero_key: B76T94C3
item_type: journalArticle
url: https://openalex.org/W7211926672
source_url: 'unpaywall: https://iforest.sisef.org/pdf/?id=ifor5027-019'
fulltext_status: fulltext
synced: '2026-11-09'
---

# Multi-scale drivers of wildfire burn severity in Central Zagros: insights from remote sensing and machine learning

## Abstract

Over the past few decades, wildfire activity has increased globally. In the Central Zagros Mountains of Iran, widespread oak decline has significantly altered fuel structures and raised ecological concerns. However, the specific contribution of long-term vegetation degradation to wildfire burn severity remains under-quantified. This study addresses this gap by investigating whether decadal declines in the Normalized Difference Vegetation Index (NDVI) are associated with higher burn severity, while assessing their relative importance against short-term pre-fire environmental conditions, fuel types, topography, and human access gradients. Focusing on a major wildfire in June 2024 in the Kashkan Watershed, we mapped burn severity using the differenced Normalized Burn Ratio (dNBR) derived from Sentinel-2 imagery. A comprehensive suite of predictors was evaluated, including the long-term NDVI trend (May- September 2014-2023), pre-fire Normalized Difference Moisture Index (NDMI), Land Surface Temperature (LST), fuel categories based on ESA WorldCover, slope, aspect, spatial texture contrast, and distance to roads and settlements. A stratified sampling design supported statistical inference using ordinary least squares regression and predictive modeling via Random Forest and XGBoost algorithms with five-fold cross-validation. XGBoost demonstrated the highest predictive performance (cross-validated R2 = 0.70; RMSE = 0.11), outperforming Random Forest (R2 = 0.64) and linear regression (R2 = 0.34). Fuel moisture (NDMI) and thermal stress (LST) emerged as the primary drivers of severity, followed by land cover, topography, and spatial texture. While the long-term NDVI decline showed a small but consistent positive association with dNBR at the landscape scale, the results highlight a distinct multi-scale mechanism. In this dynamic, pre-fire moisture and temperature establish the broad watershed-scale environmental susceptibility, whereas specific fuel types and their spatial configurations drive the local-level amplification or damping of burn severity. These findings provide a framework for proactive vulnerability mapping in Zagros oak woodlands, suggesting that integrating dynamic fire-weather data and field-based fuel measurements could further refine future predictability.

## Full text

**_i_ F o r e s t Biogeosciences and Forestry** 

**Research Article doi: 10.3832/ifor5027-019 vol. 19, pp. 359-368** 

# **Multi-scale drivers of wildfire burn severity in Central Zagros: insights from remote sensing and machine learning** 

**Farid Shahidinejad**<sup>**(1)**</sup> **, Meghdad Jourgholami**<sup>**(2)**</sup> **, Mohammad Mahdi Pourhanifeh**<sup>**(3)**</sup> **, Amirreza Esfandyar**<sup>**(2)**</sup> 

(1) Department of Environmental Science, Faculty of Natural Resources, University of Tehran, Alborz, Karaj (Iran); (2) Department of Forestry and Forest Economics, Faculty of Natural Resources, University of Tehran, Alborz, Karaj (Iran); (3) Department of Arid and Mountainous Regions Reclamation, Faculty of Natural Resources, University of Tehran, Alborz, Karaj (Iran) 

**@** Meghdad Jourgholami (mjgholami@ut.ac.ir) 

Received: Nov 02, 2025 - Accepted: Jul 28, 2026 

**Citation:** Shahidinejad F, Jourgholami M, Pourhanifeh MM, Esfandyar A (2026). Multiscale drivers of wildfire burn severity in Central Zagros: insights from remote sensing and machine learning. iForest 19: 359-368. – doi: 10.3832/ifor5027-019 [online 2026-0908] 

_Communicated by: Davide Ascoli_ 

**Over the past few decades, wildfire activity has increased globally. In the Central Zagros Mountains of Iran, widespread oak decline has significantly altered fuel structures and raised ecological concerns. However, the specific contribution of long-term vegetation degradation to wildfire burn severity remains under-quantified. This study addresses this gap by investigating whether decadal declines in the Normalized Difference Vegetation Index (NDVI) are associated with higher burn severity, while assessing their relative importance against short-term pre-fire environmental conditions, fuel types, topography, and human access gradients. Focusing on a major wildfire in June 2024 in the Kashkan Watershed, we mapped burn severity using the differenced Normalized Burn Ratio (dNBR) derived from Sentinel-2 imagery. A comprehensive suite of predictors was evaluated, including the long-term NDVI trend (MaySeptember 2014-2023), pre-fire Normalized Difference Moisture Index (NDMI), Land Surface Temperature (LST), fuel categories based on ESA WorldCover, slope, aspect, spatial texture contrast, and distance to roads and settlements. A stratified sampling design supported statistical inference using ordinary least squares regression and predictive modeling** **_via_ Random Forest and XGBoost algorithms with five-fold cross-validation. XGBoost demonstrated the highest predictive performance (cross-validated R**<sup>**2**</sup> **= 0.70; RMSE = 0.11), outperforming Random Forest (R**<sup>**2**</sup> **= 0.64) and linear regression (R**<sup>**2**</sup> **= 0.34). Fuel moisture (NDMI) and thermal stress (LST) emerged as the primary drivers of severity, followed by land cover, topography, and spatial texture. While the long-term NDVI decline showed a small but consistent positive association with dNBR at the landscape scale, the results highlight a distinct multi-scale mechanism. In this dynamic, pre-fire moisture and temperature establish the broad watershed-scale environmental susceptibility, whereas specific fuel types and their spatial configurations drive the local-level amplification or damping of burn severity. These findings provide a framework for proactive vulnerability mapping in Zagros oak woodlands, suggesting that integrating dynamic fire-weather data and field-based fuel measurements could further refine future predictability.** 

**Keywords: Wildfire, Kashkan Watershed, DNBR (burn Severity), Oak Decline, Random Forest, Vegetation Degradation** 

## **Introduction** 

(Turco et al. 2018), Siberia (McCarty et al. 2021), Australia, the Amazon basin, and the Western US (Goss et al. 2020). 

Wildfire regimes across the globe are changing significantly, with fires becoming more frequent, severe, and widespread than in previous decades; current models predict continued increases due to climate change and forest management practices (Jolly et al. 2015). This intensification represents a major shift in how fire behaves in natural systems, moving beyond historical patterns that ecosystems and species have adapted to over thousands of years (Seidl et al. 2017). The combination of climate change effects, such as rising temperatures and altered precipitation patterns, with increased human pressures has created conditions that promote more destructive fire behavior, a trend particularly evident in Mediterranean-type ecosystems (Moreira et al. 2020, Costa-Saura et al. 2025). This global surge has been particularly dramatic since 2017, with unprecedented fire behavior occurring in the Mediterranean Basin 

Anthropogenic activities, specifically landuse shifts, management practices, and human-caused climate change, serve as critical drivers of global wildfire intensification (Abatzoglou et al. 2020). These land-use shifts are often driven by socioeconomic factors such as rural abandonment and the loss of agricultural mosaics, which can lead to large accumulations of combustible biomass or the expansion of flammable plantations (Moreira et al. 2011, Kelly et al. 2020). This results in vast accumulations of combustible material, making the landscape more prone to burning and leading to increasingly large, catastrophic wildfires (Kelly et al. 2020, Charles et al. 2025). Concurrently, the expansion of human development into the wildland-urban interface (WUI) has significantly increased both ignition sources and fire risks, as proximity to 

© SISEF https://iforest.sisef.org/ 

359 

iForest 19: 359-368 

#### _Shahidinejad F et al. - iForest 19: 359-368_ 

settlements facilitates higher anthropogenic ignition density (Modugno et al. 2016, Radeloff et al. 2018). In many regions, this is coupled with reduced cultural or prescribed burning, which, along with highbiomass invasive species, has changed spatial patterns of wildfire risk (Ruscalleda-Alvarez et al. 2021, Charles et al. 2025). These changes depart from indigenous fire stewardship practices that historically maintained ecosystem balance (Kelly et al. 2020). 

Burn severity represents a fundamental measure of fire’s environmental impact, defined as the extent of fire-induced change to physical ecosystem components such as vegetation and soil (Key & Benson 2006, Parks et al. 2019). This metric is most commonly operationalized through the Differenced Normalized Burn Ratio (dNBR), which allows for a standardized assessment of fire-induced ecological change across diverse forest types (Miller & Thode 2007). This metric goes beyond simple fire occurrence to capture the degree of environmental change, making it a critical factor for understanding post-fire ecological dynamics (Parks et al. 2019). The need to better understand factors controlling fire severity stems from concerns about public safety, infrastructure, critical wildlife habitat, and watershed health (Parks et al. 2018). Research has consistently shown that fire severity is controlled by both top-down weather and climate factors and bottom-up spatial controls from fuels and topography (Povak et al. 2025). However, these relationships are complex, as burn severity is co-influenced by forest structural attributes that dictate flammability traits, such as fuel loads and density (Viedma et al. 2020). 

Modeling the environmental drivers of wildfire is a critical scientific field, as confirmed by global datasets such as the Global Fire Emissions Database (GFED) and MODIS burned area products, which have been developed specifically to link fire occurrence to key environmental drivers, including climate, vegetation, topography, and human factors (Van Der Werf et al. 2017, Giglio et al. 2016). To capture the nonlinear and complex interactions among these diverse environmental drivers, recent studies have increasingly used machine learning models to predict fire outcomes with high accuracy. These models frequently utilize vegetation indices, such as the Normalized Difference Vegetation Index (NDVI), as robust proxies for fuel biomass and ecosystem state (Escuin et al. 2008). While prior machine learning studies have successfully modeled burn severity using short-term pre-fire conditions (Eskandari et al. 2021, Seydi et al. 2024), they often overlook long-term vegetation decline. This is a significant limitation, as decadal NDVI trends reveal gradual forest degradation and mortality that fundamentally alter fuel characteristics and forest structure over time, making fire behavior in chronically stressed forests harder to predict (Lambert et al. 2013). To address this, our study focuses on the Zagros Mountains, where forest decline is operationalized as decadal NDVI trends (2014-2023 Landsat data), serving as a proxy for chronic vegetation stress associated with Zagros oak decline syndrome (Mehri et al. 2024). By integrating decadal forest degradation into wildfire modeling, this study advances the current state of the art from short-term predictive snapshots to a more holistic ecological framework. Therefore, the primary 

objectives of this study are: (i) to statistically test the hypothesis that long-term forest decline impacts recent wildfire burn severity; (ii) to assess the relative importance of this long-term trend against critical short-term variables; and (iii) to develop a comprehensive regression model that analyzes the complex interactions between these ecological factors and human factors (distance to roads and settlements) within the Zagros ecosystem. 

This study offers practical value for Zagros forest management by developing a predictive framework to map vulnerability hotspots, integrating chronic decline with biophysical risks. It supports local stakeholders (forest services, communities) in preventive strategies like fuel management prioritization and early interventions, enhancing resilience against escalating fire threats (Mehri et al. 2024). 

## **Material and methods** 

### _Study area_ 

The Kashkan Watershed is situated within the Central Zagros Mountains, which host Iran’s most extensive forest ecosystem, oak-dominated woodlands covering 5-6 million hectares across western Iran and representing 40-44% of the nation’s total forest area (Darvishi Boloorani et al. 2020). These ancient semi-arid systems (origins ~5500 years ago – Eskandari et al. 2020) play a vital role in environmental balance (Mehri et al. 2024), but face escalating wildfire frequency and human disturbances, including land use changes, unregulated grazing, deforestation, and tourism (Moradi et al. 2023, Rahimi et al. 2024) 

The study was conducted in the Kashkan Watershed (approximately 9540 km<sup>2</sup> ) of 



**Fig. 1** - Geographical location of the study area. The map illustrates the Kashkan Watershed within the Central Zagros Mountains, Lorestan Province, western Iran. The main panel shows the region’s rugged topography, while the inset map indicates its location in Iran. This area has a semi-arid Mediterranean climate and a vegetation mosaic dominated by _Quercus brantii_ woodlands. 

360 

iForest 19: 359-368 

_Zagros burn severity drivers_ 

Lorestan Province, Central Zagros Mountains, western Iran (Fig. 1). This region features rugged topography (elevation 5002500 m a.s.l.) and a semi-arid Mediterranean climate, with cool-wet winters (mean annual precipitation ~500 mm) and hot-dry summers (mean temperature ~30 °C) that promote intense fire seasons. Vegetation comprises a mosaic of open oak woodlands, shrublands, grasslands, and rainfed croplands, dominated by Persian oak ( _Quercus brantii –_ Mehri et al. 2024, Sadeghi et al. 2024). 

The area is an ideal site for fire-ecosystem analysis because of overlapping pressures: high wildfire susceptibility (Sadeghi et al. 2024) and ongoing Zagros oak decline, which has simplified fuel structures from dense to open woodlands and shrublands (Mehri et al. 2024). A major wildfire in June 2024 (~5000 ha burned – Ismayilov 2024) provides a documented case for evaluating burn severity. 

### _Dependent variable: burn severity (dNBR)_ 

Burn severity was mapped using dNBR from Sentinel-2 MSI Level-2A surface reflectance (Zahabnazouri et al. 2025). Cloudfree composites were created for pre-fire (10-20 June 2024) and post-fire (23 June-12 July 2024) periods to capture the event while minimizing phenological bias. Clouds/ cirrus were masked via the QA60 bitmask. NBR was calculated as per eqn. 1 (USGS 2017): 



<!-- Start of picture text -->
NBR = NIR − SWIR (1)<br>NIR + SWIR<br><!-- End of picture text -->

and dNBR as per eqn. 2: 



<!-- Start of picture text -->
(2)<br>dNBR = NBR pre − NBR post<br><!-- End of picture text -->

where NBRpre and NBRpost are the NBR values pre-fire and post-fire, respectively (higher values = greater severity – USGS 2017). Rasters were reprojected to a 30-m UTM grid (EPSG: 32638, Zone 38N) for alignment. The nearest-neighbor resampling method was applied to all layers to preserve the original radiometric integrity of the spectral bands and avoid the artificial smoothing of fire-periphery pixels that results from bilinear interpolation. Landcover classes such as water bodies and barren lands, which comprised a negligible fraction of the study area (~1.7%), were retained in the modeling phase to ensure a spatially continuous dataset. While these surfaces occasionally exhibited spectral artifacts (false-high dNBR values) due to moisture or turbidity changes, their limited frequency ensured they did not significantly influence the overall performance or generalization of the machine learning model. Additionally, we retained negative dNBR values to preserve the full statistical distribution of the dataset, allowing the model to learn from the complete range of post-fire spectral responses. 

#### **Tab. 1** - Summary of datasets used in this study. 

|**Data Category**|**Data Source /**<br>**GEE Asset ID**|**Resolution **|<sup>**Temporal**</sup><br>**Coverage**|**Purpose in**<br>**Study**|
|---|---|---|---|---|
|Long-Term Vegetation<br>& Thermal|Landsat 8 OLI/TIRS C2<br>T1 L2|30 m|2014-2023|NDVI trend, LST|
|Fire Event & Fuel<br>Moisture|Sentinel-2 MSI<br>(Level-2A)|20 m|June-July<br>2024|dNBR, NDMI|
|Land Cover (Fuel<br>Type)|ESA WorldCover 2021|10 m|2021|LandCover|
|Topography|DEM (User Asset)|30 m|Static|Slope, Aspect|
|Human Factors 1<br>(Roads)|Roads Vector|Vector|2023|Road distance|
|Human Factors 2<br>(Villages)|Settlements Vector|Vector|2023|Distance to<br>villages|
|Image Texture (from<br>NDVI)|Derived in GEE: GLCM<br>from pre-fire NDVI<br>(3×3) and local<br>variance|10 m<br>(sampled at<br>30 m)|<br>June 2024|Texture Contrast;<br>Texture<br>Homogeneity;<br>Texture Variance|
|Study Boundary|AOI Vector|Vector|Static|Analysis Boundary|



### _Independent variables (predictors)_ 

nature (Wilson & Gallant 2000). To represent fuel models, we utilized the ESA WorldCover 2021 (10 m) product, reclassified into five fuel-oriented categories: Closed Forest, Open Forest, Shrub/Grassland, Cropland, and Bare/Water. The decision to merge shrublands and grasslands into a single class was based on their ecologically similar fire behavior in semi-arid ecosystems. Both vegetation types serve as fine surface fuels with high combustibility and rapid drying rates, acting as the primary carriers of fire. In the Zagros context, these classes often form a continuous surface fuel complex that facilitates fire spread, justifying their consolidation for improved modeling robustness. The categorical data were one-hot encoded (dropfirst) to prevent multicollinearity (James et al. 2021, Zanaga et al. 2022). Spatial structural heterogeneity was quantified using the Gray-Level Co-occurrence Matrix (GLCM) contrast. To ensure spatial consistency with the 30-m dependent variable (dNBR) and other environmental predictors, the Sentinel-2 NIR band was first aggregated to 30-m resolution before texture computation. We then applied a 3×3 kernel to capture stand-level horizontal fuel continuity and canopy complexity, providing the machine learning model with contextually relevant structural information (Zhou et al. 2024). Finally, we mapped human access gradients, key drivers of ignition probability, using vector layers of road networks and settlements. Euclidean distances to the nearest road and village were calculated at a 30-m resolution across the entire study area to ensure a continuous and accurate distance gradient. We then masked these proximity layers to vegetated and burnable surfaces during final data stacking. To accommodate the non-linear decay effects of these proximity variables within our models, we retained both raw distances and their log1p-transformed ver- 

To model burn severity drivers, we selected predictor variables encompassing long-term vegetation dynamics, pre-fire biophysical conditions, topography, fuel structures, and anthropogenic proximity; all features are detailed in Tab. 1. To address our primary research aim regarding forest decline, we operationalized longterm vegetation dynamics as annual MaySeptember NDVI trends (2014-2023). We derived these trends on a pixel-wise basis from Landsat-8/9 Collection 2 imagery using ordinary least squares (OLS) slope calculation with the “linearFit” reducer in Google Earth Engine<sup>®</sup> (GEE). To ensure data quality, we applied cloud and shadow masking _via_ the QA PIXEL band. We further mitigated potential atmospheric artifacts by calculating the annual mean NDVI for each growing season before trend estimation. Negative slope values indicate chronic vegetation decline (Withanage et al. 2024). To capture immediate pre-fire conditions, we utilized the Normalized Difference Moisture Index (NDMI) derived from multiscene median composites of Sentinel-2 imagery (June 10-20, 2024) to represent canopy moisture (eqn. 3): 



<!-- Start of picture text -->
NDMI = NIR − SWIR 1 (3)<br>NIR + SWIR 1<br><!-- End of picture text -->

Additionally, Land Surface Temperature (LST) was calculated from multi-scene mean composites of Landsat-8 Collection 2 imagery (May 1 - June 20, 2024). These biophysical metrics were aggregated using temporal averaging (median for NDMI and mean for LST) to ensure a representative baseline that aligns with the phenology of the dNBR evaluation period (USGS 2017). 

We incorporated topographic controls on fire spread using a 30-m SRTM Digital Elevation Model to extract slope and aspect, with the latter encoded into sine and cosine components to account for its circular 

iForest 19: 359-368 

361 

_Shahidinejad F et al. - iForest 19: 359-368_ 

zouri et al. 2025 – see Appendix 1 in Supplementary material). 

**Tab. 2** - Descriptive statistics for continuous variables used in the analysis (N = 89,314). (SD): standard deviation. 

For statistical inference, we established a baseline using Ordinary Least Squares (OLS) regression. Multicollinearity was assessed by computing Variance Inflation Factors (VIF) after all transformations (log1p) and dummy encoding (drop-first) were applied. We used an iterative screening process in which we recursively removed the variable with the highest VIF and recalculated VIF values for the remaining predictors until all variables met the threshold (VIF < 8). Finally, we applied HC3 robust standard errors to account for potential heteroscedasticity (Long & Ervin 2000, Marcoulides & Raykov 2019). To capture complex, non-linear relationships, we employed Random Forest and XGBoost algorithms. To ensure optimal performance and prevent overfitting, we tuned hyperparameters using a grid search across a predefined parameter space ( _e.g._ , tree depth, number of estimators, and learning rate). We then selected the best-performing configurations for the final models: Random Forest (500 estimators, max depth of 15) and XGBoost (600 estimators, learning rate of 0.08). Model performance was rigorously evaluated using five-fold cross-validation (4×4 grid bins) to account for spatial autocorrelation, relying on cross-validated R<sup>2</sup> and Root Mean Square Error (RMSE) to assess generalization (Breiman 2001, Chen & Guestrin 2016, Seydi et al. 2024, Novo et al. 2025). Furthermore, feature importance was extracted to rank driver influence, utilizing “Mean Decrease in Impurity” (MDI) for the Random Forest model and the “Gain metric” for the XGBoost model. Finally, non-parametric tests (Mann-Whitney U and Kruskal-Wallis) were utilized to assess group-level differences, as preliminary Shapiro-Wilk tests indicated that the dNBR data violated the assumption of normality. 

|**Variable**|**Mean**|**SD**|
|---|---|---|
|dNBR|0.25|0.20|
|NDVItrend|0.001|0.01|
|Slope|9.19|8.71|
|Aspect|181.87|105.29|
|LST|33.19|6.58|
|NDMI|0.08|0.22|
|Road distance<br>|1976.79|2346.26|
|Distance to villages<br>|1717.55|2163.50|
|Log-transformed<br>distance to roads|6.84|1.38|
|Log-transformed<br>distance to villages|6.99|0.93|
|Texture Contrast|169.02|346.05|
|Texture Homogeneity|0.18|0.11|
|Texture Variance|83.45|168.94|



sions (Eskandari et al. 2021, Li et al. 2022). We aligned and stacked all spatial layers into a unified raster mosaic for subsequent sampling. 

### _Sampling strategy and statistical analysis_ 

To construct a robust analytical dataset from the continuous raster mosaic, we employed a stratified random sampling approach based on burn severity classes. We stratified dNBR values into four categories to ensure a balanced, representative sample across the full spectrum of fire effects: Unburned/Regrowth (dNBR < 0.10), Low (0.10 ≤ dNBR < 0.27), Moderate (0.27 ≤ dNBR < 0.44), and High severity (dNBR ≥ 0.44). This stratification ensured balanced representation, extracting five points per class per square kilometer. Following multiple iterations and strict quality control to remove non-finite values, the final dataset comprised 89,314 valid points (Zahabna- 

All geospatial data were processed in Google Earth Engine (GEE) for consistency and reproducibility (Mohammed et al. 2025 – see also Appendix 1 in Supplementary material). 



**Fig. 2** - Distribution of land cover and fuel types in the Kashkan Watershed. The donut chart illustrates the area (km<sup>2</sup> ) and percentage of the five reclassified ESA WorldCover 2021 categories used in the modeling process. Open Forest and Shrub/Grassland represent the dominant fuel complexes in the study area, while nonburnable surfaces (Bare/Water) constitute a negligible fraction (0.2%). 

## **Results** 

### _Descriptive statistics and spatial patterns_ 

The cleaned analytical dataset contains 89,314 valid records. Descriptive statistics for all continuous variables are summarized in Tab. 2 as the basis for subsequent inference and modeling. The dependent variable dNBR showed a mean of 0.25 with substantial spread (standard deviation, SD = 0.20), indicating wide heterogeneity in burn severity across the landscape. The long-term decadal NDVI trend prior to the fire was near-neutral on average (mean = 0.01; SD = 0.01), suggesting overall stability with localized decline or recovery signals rather than a strong basin-wide trend. 

Pre-fire biophysical conditions depict moderately warm and variably moist canopies, with Land Surface Temperature (LST) averaging 33.19 °C (SD = 6.59) and NDMI averaging 0.08 (SD = 0.22), consistent with semi-arid summer conditions that modulate available fuel moisture. The landscape exhibits complex terrain, with a mean slope of 9.19° (SD = 8.72) and an aspect covering the full directional range (mean = 181.88°), creating diverse physical and microclimatic conditions that locally influence fire spread and resulting burn-intensity patterns. 

Human-access gradients exhibit pronounced right-skewness typical of proximity variables: mean distance to the nearest road is 1976.79 m (SD = 2346.26), and mean distance to the nearest settlement is 1717.55 m (SD = 2163.50), motivating the use of log1p transformation in the learning models, along with raw distances, to capture non-linear decay effects. The transformed counterparts reflect this stabilization, with the log-transformed distance to roads averaging 6.84 (SD = 1.38) and the log-transformed distance to villages averaging 6.99 (SD = 0.93). This transformation improves numerical behavior without losing critical information at zero distances. 

Fine-scale structural heterogeneity of the pre-fire landscape is evident in the spatial texture distributions. Specifically, texture contrast exhibits a high mean and substantial dispersion (mean = 169.02; SD = 346.05), texture homogeneity is concentrated near low values (mean = 0.18; SD = 0.11), and texture variance is broadly spread (mean = 83.45; SD = 168.94). These patterns collectively support the inclusion of a single screened texture metric (contrast) to reduce redundancy while retaining critical signals of fuel continuity. 

The land cover composition over the 9540.20 km<sup>2</sup> study area is illustrated in Fig. 2. The landscape was predominantly characterized by Open Forest, which constituted 63.10% (6017.50 km<sup>2</sup> ) of the total area. Shrub/Grassland was the second most prevalent category, covering 24.30% (2320.90 km<sup>2</sup> ). Other significant land cover types included Cropland at 9.70% (927.3 km<sup>2</sup> ) and Closed Forest at 2.70% (254 km<sup>2</sup> ). 

362 

iForest 19: 359-368 

_Zagros burn severity drivers_ 



<!-- Start of picture text -->
Fig. 3  - Spatial distribution<br>of environmental and fire-<br>related variables. (a) dNBR:<br>classified into Unburned<br>(less than 0.10), Low (0.10-<br>0.27), Moderate (0.27-<br>0.44), and High severity<br>(greater than or equal to<br>0.44) based on Key & Ben-<br>son (2006), adapted for<br>Zagros canopy density. (b)<br>NDVI Trend: 10-year Sen’s<br>slope (2014-2023) catego-<br>rized into Significant<br>Decline (less than -0.04),<br>Slight Decline (-0.04 to<br>-0.01), Stable (-0.01 to<br>+0.01), and Improvement<br>(greater than +0.01). (c)<br>LST: classified by 10 °C<br>intervals to represent<br>regional thermal gradients.<br>(d) NDMI: thresholds rep-<br>resent moisture stress (less<br>than 0) to high canopy<br>moisture (greater than<br>0.4). (e) Land Cover:<br>derived from ESA World-<br>Cover 2021 standard<br>classes.<br><!-- End of picture text -->

The Bare/Impervious/Water class represented a negligible fraction of the total area at just 0.20% (20.5 km<sup>2</sup> ). 

### _Spatial distribution of key variables_ 

The spatial distribution of burn severity (dNBR) across the basin was notably heterogeneous (Fig. 3a). While the landscape was predominantly affected by low and moderate-low severity burns, several distinct clusters of high severity were observed, particularly in the western and northern portions. Ecologically, this pattern corresponds spatially with the decadal NDVI trend (Fig. 3b), where many of the high-severity clusters coincided with areas exhibiting significant long-term vegetation decline. This visual correlation supports our hypothesis that prolonged ecosystem stress, which likely increases dead biomass and alters fuel continuity, exacerbates fire impacts. Conversely, areas characterized by vegetation stability or improvement were generally associated with lower burn severities. Pre-fire biophysical conditions also showed clear spatial structuring: Land Surface Temperature (LST) was highest in the lower-elevation, sparsely vegetated ar- 

eas in the south, while NDMI indicated higher canopy moisture content in the densely forested northern highlands (Fig. 3c, Fig. 3d). Together, these spatial patterns highlight how moisture deficits and chronic forest decline converge to create pockets of high vulnerability, providing crucial context for interpreting the regression models. 

trend compared to areas with stable or positive trends (Z = 18.81, p < 0.001, r = 0.06). Group summaries showed higher severity for declining pixels (mean/median dNBR = 0.26/0.28, N = 38,619) than for healthy or stable pixels (mean/median = 0.24/0.23; N = 50,695). This quantitatively confirms the linkage between previous vegetation decline and elevated burn severity (Tab. 3). Across the primary landcover classes, burn severity differed significantly (Kruskal-Wallis H = 13,616.97, p < 0.001). To account for the large sample size and ensure that our findings reflect meaningful ecological variation, we calculated the effect size using epsilon-squared (ε<sup>2</sup> ), 

### _Model performance and feature importance_ 

Statistical comparisons of pixel groups further reinforced these spatial observations. Burn severity was significantly higher in areas with a negative long-term NDVI 

**Tab. 3** - Comparison of burn severity (dNBR) between declined and healthy vegetation areas. 

|**Vegetation Trend Status**|**N**<br>**Mean**<br>**dNBR**|**Median**<br>**dNBR**|**Std. Dev.**<br>**dNBR**|
|---|---|---|---|
|Declined (NDVI trend < 0)|38619<br>0.26|0.28|0.20|
|Healthy / Stable (NDVI|50695<br>0.24|0.23|0.20|
|trend ≥ 0)||||
|_Mann-Whitney U test_|_Z = 18.80, p < 0.0001, Effect s_|_ize r = 0.06_||



iForest 19: 359-368 

363 

_Shahidinejad F et al. - iForest 19: 359-368_ 

**Tab. 4** - Comparison of burn severity (dNBR) across land cover classes. 

|**Land Cover Class**|**N**|**Mean**<br>**dNBR**|**Median**<br>**dNBR**|**Std. Dev**<br>**dNBR**|
|---|---|---|---|---|
|Closed Forest (Class 1)|819|0.07|0.001|0.13|
|Open Forest (Class 2)|25901|0.14|0.01|0.20|
|Shrub/Grassland (Class 3)|57253|0.30|0.30|0.17|
|Cropland (Class 4)|3794|0.19|0.002|0.27|
|_Kruskal-Wallis test_|_H = 13616.97, p_<br>_classes = 4 (burn_|_< 0.001; Epsilon-s_<br>_able fuel types)_|_quared (ε_<sup>2</sup>_) =_|_0.155; k_|



**Tab. 5** - Feature-importance rankings from Random Forest and XGBoost for predicting burn severity (dNBR). (Imp): Importance. 

|**RF Feature**|**Imp**|**XGB Feature**|**Imp**|
|---|---|---|---|
|NDMI|0.32|Bare/Water (Class 5.0)|0.51|
|LST|0.09|NDMI|0.12|
|Slope|0.09|Cropland (Class 4.0)|0.08|
|Log-transformed distance to roads|0.08|Shrub/Open Forest (Classes 2 & 3)|0.04|
|Distance to roads|0.07|Slope|0.03|
|NDVItrend|0.06|Distance to roads|0.03|
|TextureContrast|0.06|LST|0.02|
|Distance to villages|0.05|Log-transformed distance to roads|0.02|
|Log-transformed distance to<br>villages|0.05|NDVItrend|0.02|
|Bare/Water (Class 5.0)|0.03|TextureContrast|0.02|
|Aspect (sine)|0.01|Log-transformed distance to<br>villages|0.02|
|Aspect (cosine)|0.01|Distance to villages|0.02|
|Cropland (Class 4.0)|0.01|Aspect (cosine)|0.01|
|Shrub/Open Forest (Classes 2 & 3)|0.01|Aspect (sine)|0.01|





**Fig. 4** - Comparative performance analysis of Random Forest (RF) and XGBoost models. (a) Model goodness-of-fit based on training and 5-fold cross-validated R<sup>2</sup> values. (b) Predictive error based on mean cross-validated RMSE. The red values above the bars in panel (b) represent the standard deviation of R<sup>2</sup> across crossvalidation folds, indicating the high stability and consistency of both ensemble learners. 

which was found to be 0.15, indicating a moderate and robust relationship between fuel type and fire severity. The shrub and grassland class exhibited the highest central tendency (mean = 0.30), while closed forest showed the lowest (mean = 0.07 – Tab. 4). This pronounced contrast, even after excluding non-burnable surfaces to mitigate spectral noise, highlights the role of fuel structure; the fine, contiguous surface fuels in shrublands facilitate more intense burning compared to the more moisturebuffered closed-canopy oak stands. 

Fig. 4 illustrates the out-of-sample performance under 5-fold cross-validation, demonstrating that XGBoost achieved the best generalization (cross-validated R<sup>2</sup> ≈ 0.70, RMSE ≈ 0.11), followed by Random Forest (cross-validated R<sup>2</sup> ≈ 0.64, RMSE ≈ 0.12). Both models displayed high stability across data splits (R<sup>2</sup> standard deviation ≈ 0.00). The strong predictive capacity of these tree-based models indicates that burn severity in the Zagros ecosystem is driven by complex, non-linear interactions among predictors. The random _k_ -fold cross-validation used here may yield optimistic performance metrics because of the strong spatial autocorrelation inherent in raster data. Consequently, the cross-validation metrics reported in Tab. 4 should be interpreted as upper-bound estimates of generalization. 

Regarding variable importance (Tab. 5), the Random Forest model identified moisture (NDMI) as the most influential predictor, followed by thermal stress (LST) and slope. Secondary drivers included proximity to roads, the decadal NDVI trend, and spatial texture contrast. For the XGBoost model, categorical land cover emerged as the primary feature, followed by NDMI, slope, and distance to roads. 

Multicollinearity among continuous predictors was generally low to moderate (Tab. S1 in Supplementary material). For instance, LST and NDMI showed Variance Inflation Factors (VIF) of 2.74 and 3.17, respectively, while topographic, spatial texture, and proximity variables remained near 1.00 to 1.60. As expected, land-cover indicators exhibited larger VIFs (up to 7.19 for the combined shrub and grassland class). These diagnostics justify our use of tree-based learners, which robustly handle remaining categorical collinearity while effectively capturing the underlying ecological drivers of fire severity. 

### _Linear regression results_ 

The ordinary least squares (OLS) baseline model offered an interpretable approximation of burn-severity drivers, yielding a moderate fit (R<sup>2</sup> = 0.34, adj-R<sup>2</sup> = 0.34, F = 5041, p < 0.001, N = 89,314). While these linear relationships explain roughly one-third of the variance in dNBR, the substantial performance gap between OLS and the ensemble algorithms highlights that the ecological mechanisms driving fire severity in the Zagros Mountains are fundamentally 

364 

iForest 19: 359-368 

_Zagros burn severity drivers_ 

non-linear and rely heavily on the synergistic effects of moisture gradients, terrain, and long-term degradation. 

## **Discussion** 

_Interpretation of key findings_ 

The results indicate that machine learning algorithms, particularly tree-based ensembles, provide a robust predictive framework for modeling burn severity (dNBR) within the heterogeneous Zagros landscape (Seydi et al. 2024). However, compared to simpler parametric models, these enhanced predictive capacities should be interpreted contextually, bearing in mind that random cross-validation yields upperbound estimates due to spatial autocorrelation. 

These values are particularly noteworthy because the analyzed fire event was dominated by low-to-moderate severity, which compresses the dynamic range of the response variable and lowers the theoretical ceiling for explained variance. The ability of these models to recover spatially coherent patterns under such circumstances indicates non-linear structures and complex interactions among the drivers of burn severity, which linear models cannot capture. 

Model explainability from both ensembles converges on a moisture-thermal mechanism as the primary driver, which is further modulated by fuel type and its spatial structure (Seydi et al. 2024). In the Random Forest model, moisture (NDMI) and temperature (LST) emerged as the most influential predictors, followed by slope, proximity to roads, the decadal NDVI trend, and spatial texture contrast. Consistent with well-established literature, this hierarchy confirms that pre-fire fuel moisture and surface temperature impose first-order constraints on fire effects, while topography and anthropogenic access gradients shape where intense burning is most likely to occur (Eskandari et al. 2021, Povak et al. 2025). The XGBoost model corroborates the primacy of NDMI but elevates the importance of categorical land cover classes, most notably bare/impervious land (class 5.0) and, to a lesser extent, cropland (class 4.0) and the merged shrubland/open-forest class (classes 2 and 3), above many continuous predictors. Collectively, these results suggest a multi-layered dynamic. At the broader watershed scale, fuel moisture (NDMI) and thermal stress (LST), the top continuous predictors in our models, establish the baseline environmental susceptibility. Conversely, at the local patch level, specific fuel types and spatial configurations drive the amplification or damping of burn severity. This local modulation is empirically supported by the XGBoost model, which prioritized categorical land cover as the most critical feature, and the KruskalWallis test results (H = 13,616.97, p < 0.001). Specifically, the significant contrast between the high severity in contiguous fine fuels (Shrublands/Grasslands, mean = 0.30) 

and the lower severity in more resilient, moisture-buffered structures (Closed Forest, mean = 0.07) provides clear evidence of how local fuel characteristics modify the fire’s impact. 

These model-derived patterns are reinforced by independent statistical tests. The Mann-Whitney U test revealed that pixels with a negative long-term NDVI trend experienced significantly higher dNBR values (Smith et al. 2021), directly supporting the hypothesis that chronic vegetation decline predisposes ecosystems to more severe fires by reducing live fuel moisture and increasing the load of receptive fine fuels. Furthermore, the Kruskal-Wallis test confirmed significant differences in burn severity among land cover classes. Among vegetated types, shrubland/grassland exhibited the highest median severity, followed by open forest and cropland, while closedcanopy forest was the least severely burned (Miller et al. 2023). This pattern aligns with expected differences in fuel continuity, loading, and moisture-buffering capacity across these vegetation types. Synthesizing these findings, burn severity in the Zagros is best understood as an outcome of multi-scale interactions. At the macro-scale, pre-fire moisture and surface temperature establish the primary constraints on watershed-level fire potential. Concurrently, at the local scale, fuel type and neighborhood structure, captured by spatial texture, govern fire propagation and intensification. Finally, contextual factors such as terrain and anthropogenic access gradients further modify fire exposure and spread potential. This integrated understanding explains why flexible, non-linear models that can learn complex interactions generalize far better than their linear counterparts in an environment characterized by a limited dynamic range and complex spatial controls (Seydi et al. 2024). 

### _Comparison with existing research_ 

Our cross-validated model performance (XGBoost R<sup>2</sup> ≈ 0.70 and Random Forest R<sup>2</sup> ≈ 0.65) is consistent with results from other studies in structurally complex forests where modeling relies solely on static variables. Previous research has consistently affirmed the power of Random Forest for predicting burn severity (Hultquist et al. 2014, Collins et al. 2018). As noted in literature reviews, a key challenge is that much of the unexplained variance in such static models do not stem from algorithmic limitations, but from the absence of dynamic fire-weather and fine-scale fuel moisture 

data (Miller et al. 2023). 

Our finding that moisture (NDMI) and temperature (LST) are the most influential predictors aligns with other research highlighting the critical role of these factors. For instance, studies have shown that Land Surface Temperature (LST) is a foundational variable in developing burn severity indices (Zheng et al. 2016). Similarly, a large-scale analysis in Canada’s mountain 

national parks found that variables related to vegetation moisture and temperature (like NDMI and LST) were among the most important drivers of burn severity (dNBR – Wang et al. 2022). This convergence underscores a widely applicable moisturethermal mechanism. 

This distinction resolves apparent contradictions in previous NDVI-burn severity studies. Current research on Normalized Difference Vegetation Index (NDVI) and burn severity relationships reveals seemingly contradictory findings that highlight this complexity. Studies have found that higher NDVI values immediately before fire events are associated with increased burn severity (Huang et al. 2020). However, prefire forest health as measured by NDVI also plays a crucial role in post-fire recovery patterns. Areas with higher pre-fire NDVI values showed significant increases in postfire forest recovery metrics compared to areas with lower pre-fire NDVI values, suggesting that healthier pre-fire forest conditions may result in faster forest recovery (Viana-Soto et al. 2020, Alegria 2022). Our novel finding that a decadal negative NDVI trend enhances prediction is consistent with the principles of time-series analysis for forest monitoring. In this approach, long-term trends in satellite data, such as from Landsat, are used to detect and quantify changes in forest health and cover over time (Novo-Fernández et al. 2018). The observed association between the decadal NDVI trend and high burn severity suggests that long-term vegetation decline may act as a slow-acting predisposing factor. Rather than directly driving fire intensity, this trend could reflect an ecosystem’s increasing vulnerability to severe fire over time. 

Our models revealed that landscape structure, particularly vegetative landcover types, plays a significant role in predicting fire severity. However, interpretations of land-cover influence must account for spectral artifacts; non-burnable surfaces ( _e.g._ , Bare/Water) can exhibit artificially high dNBR values due to edge effects, potentially confounding machinelearning outputs if not masked. The high importance of the land cover variable is consistent with findings that emphasize the need for vegetation-specific information to improve burn severity prediction (He et al. 2024). Furthermore, the higher severity observed in shrublands than in dense forests aligns with studies showing that severity varies significantly across vegetation layers (Muhammad et al. 2024). The importance of spatial texture has also been confirmed elsewhere; for example, Hultquist et al. (2014) identified texture as a key predictor in their Random Forest model. While high dNBR values over bare surfaces are often artifacts of spectral edge effects (Collins et al. 2020), our conclusions regarding land-cover controls remain robust. By explicitly excluding these non-burnable surfaces from our core statis- 

iForest 19: 359-368 

365 

#### _Shahidinejad F et al. - iForest 19: 359-368_ 

tical evaluations (Tab. 5), we confirmed that structural differences among actual vegetative fuel types ( _e.g._ , shrublands _vs._ forests) genuinely drive the observed fire severity patterns. The high importance of non-burnable surfaces in the XGBoost model reflects the algorithm’s ability to maximize predictive accuracy by identifying “zero-severity” boundaries, although we excluded these areas from ecological mean-comparison tests to avoid biasing the drivers of actual fuel consumption. 

A substantial portion of the residual uncertainty in our model likely stems from the absence of dynamic fire-weather data. While we do not directly test this in our study, the literature suggests these variables are critical, and studies that integrate them often report significant improvements in model accuracy. For instance, Vanderhoof et al. (2025) increased their Random Forest model’s R<sup>2</sup> from 0.46 to 0.78 by adding event-specific weather indices like wind speed. This confirms that the primary limitation in predictive precision is often limited access to top-down forcings, a challenge also identified as a barrier to comparing results across studies (Miller et al. 2023). 

### _Novelty, limitations, and future research directions_ 

The primary novelty of this work lies not in the individual methodological components, but in their regional integration; we combined long-term NDVI trends with short-term biophysical variables and texture metrics to create a comprehensive, multi-scale framework for burn-severity modeling specific to the Zagros ecosystem. This was achieved by jointly integrating (i) long-term ecosystem decline (the decadal NDVI trend), (ii) pre-fire biophysical status (NDMI, LST), and (iii) a collinearity-screened GLCM texture metric. While machine learning has been used to model fire in various contexts, integrating long-term ecological degradation with short-term biophysical drivers remains largely unexplored in semi-arid Mediterranean-type forest ecosystems. Addressing this gap is critical because chronic vegetation decline, such as the oak decline observed in the Zagros, represents a slow-acting predisposing factor that fundamentally alters fuel characteristics and fire vulnerability. This study therefore establishes a reproducible baseline for future research on fire effects in these chronically stressed environments. These contributions, however, should be considered in light of two principal limitations: (i) missing dynamic fire-weather forcings –  hourly data fields for wind, humidity, and atmospheric stability were unavailable for the fire window; such variables are widely acknowledged as dominant “topdown” drivers of burn severity, and their exclusion is a recognized source of unexplained variance in remote sensing-based severity studies (Miller et al. 2023, Vanderhoof et al. 2025); (ii) the proxy nature of 

fuel descriptors – satellite-derived indices and texture metrics capture fuel moisture and structure only indirectly. They cannot resolve fine-scale dead-fuel moisture content or live-fuel loading, both of which are identified in the literature as common blind spots that propagate uncertainty into model outputs (Seydi et al. 2024). 

These constraints define clear priorities for future research: (i) integrate high-resolution meteorology – future models should incorporate data from station networks or downscaled reanalysis products to explicitly represent event-scale fire-weather coupling; (ii) incorporate field-calibrated fuel data – collecting or accessing field-calibrated fuel measurements is essential to validate and refine the spectral and textural proxies used, thereby addressing a critical data gap highlighted in comparative severity assessments; (iii) conduct external validation – the framework’s generalizability must be tested across multiple fires in the Zagros region; this includes benchmarking its performance against standardized burn-severity products, whose classification thresholds and ecological relevance continue to face scientific scrutiny. 

### _Strategic implications for fire_ 

### _management in the Zagros region_ 

The modeling results provide a foundation for shifting Zagros fire management from a predominantly reactive posture to a proactive, data-driven strategy that anticipates, rather than merely responds to, severe fire events. 

#### **Proactive vulnerability mapping** 

The strong pre-fire signals associated with NDMI, LST, and the decadal NDVI trend suggest the potential to identify landscapes primed for high burn severity months in advance. However, as our current findings are derived from a single fire event, prospective validation across multiple independent fires is required to confirm this as an operational early-warning capability. Operationally, these variables can be composited in Google Earth Engine to generate dynamic “fire-vulnerability hotspot” maps at the start of each fire season. This allows agencies to strategically stage suppression resources and focus public-awareness campaigns where risk is greatest (Eskandari et al. 2021, Sadeghi et al. 2024). 

#### **Landscape-structure management** 

The significance of both spatial texture metrics and topographic variables indicates that fire severity is governed not only by terrain but also by the spatial arrangement and continuity of fuels. Management, therefore, should extend beyond simple fuel-type inventories to actively manipulate spatial patterns, for example, by constructing fuel breaks across high-continuity corridors and conserving highly fragmented patches as potential refugia. 

#### **Resilience-oriented stewardship** 

While the predominance of low-to-moderate severity in the studied event could suggest underlying ecosystem resilience, alternative factors like favorable weather conditions during the fire or effective local suppression efforts must also be considered. By running the model in reverse and identifying combinations of moisture status, vegetation trend, and texture associated with low dNBR, managers can prioritize maintaining landscape attributes that foster desirable, low-severity fire regimes. Such a shift aligns with emerging regional policy recommendations that call for resilience-focused planning rather than an exclusive reliance on full suppression. Collectively, these implications argue for embedding the presented modeling framework within routine decision cycles, leveraging open-source platforms to deliver near-real-time risk products and guiding interventions that shape, not simply extinguish, future fire behavior. 

## **Conclusions** 

This study aimed to develop a predictive model for burn severity within the complex, fire-prone ecosystems of the Zagros Mountains by integrating long-term ecosystem health trends, spatial texture metrics, and traditional biophysical variables. Our findings indicate that machine learning ensembles, particularly XGBoost, offer a robust predictive framework. The models revealed that pre-fire biophysical conditions (notably moisture and temperature) and fuel type (land cover) are strongly associated with fire effects. Furthermore, longterm vegetation decline (NDVI trend), topography, and landscape structural heterogeneity (texture) emerged as important secondary predictors of local burn severity. However, these findings must be interpreted in the context of several methodological limitations. Given the correlational design, the identified relationships represent plausible ecological associations rather than proven causal mechanisms. Additionally, the reported predictive performance likely reflects upper-bound estimates due to spatial autocorrelation, and accurate interpretation required the careful masking of spectral artifacts over non-burnable surfaces. Because this study is based on a single fire event, the current framework provides a foundational, data-driven understanding of regional vulnerability rather than an operationally ready management tool. Future research should prioritize prospective validation across multiple independent fires and integrate dynamic fireweather data. Ultimately, this study advances the scientific understanding of spatial fire dynamics in the Zagros region, offering a vital first step toward developing proactive, spatially explicit landscape management strategies. 

## **List of abbreviations** 

The following abbreviations have been 

366 

iForest 19: 359-368 

_Zagros burn severity drivers_ 

used throughout the text: 

- dNBR: differenced Normalized Burn Ratio 

- GEE: Google Earth Engine 

- GLCM: Gray-Level Co-occurrence Matrix 

- HC3: Heteroscedasticity-Consistent Standard Errors (type 3) 

- LST: Land Surface Temperature 

- NDMI: Normalized Difference Moisture Index 

- NDVI: Normalized Difference Vegetation Index 

- NIR: Near-Infrared 

- OLS: Ordinary Least Squares 

- RF: Random Forest 

- RMSECV: cross-validated Root Mean Square Error 

- R<sup>2</sup> CV: cross-validated R-squared 

- VIF: Variance Inflation Factor 

- XGB: XGBoost 

## **Acknowledgements** 

We thank the University of Tehran for providing access to research facilities. No external funding was received for this research. 

## **References** 

Abatzoglou JT, Lasslop G, Bachelet D (2020). Climate, land use, and fire: can models inform management? Frontiers in Earth Science 8: 624171. - doi: 10.3389/feart.2020.624171 

Alegria C (2022). Vegetation monitoring and post-fire recovery: a case study in the centre inland of Portugal. Sustainability 14: 12698. - doi: 10.3390/su141912698 

Breiman L (2001). Random forests. Machine Learning 45: 5-32. - doi: 10.1023/A:10109334043 

##### 24 

Charles FE, Reside AE, Smith AL (2025). The influence of changing fire regimes on specialized plant-animal interactions. Philosophical Transactions of the Royal Society B: Biological Sciences 380: 20230448. - doi: 10.1098/rstb.2023. 

0448 

Chen T, Guestrin C (2016). XGBoost: a scalable tree boosting system. In: Proceedings of the “22<sup>nd</sup> ACM SIGKDD International Conference on Knowledge Discovery and Data Mining”. ACM (San Francisco, CA, USA) 13-17 Aug 2016, pp. 785-794. - doi: 10.1145/2939672.2939785 Collins L, Griffioen P, Newell G, Mellor A (2018). The utility of random forests for wildfire severity mapping. Remote Sensing of Environment 216: 374-384. - doi: 10.1016/j.rse.2018.07.005 

Collins L, McCarthy G, Mellor A, Newell G, Smith L (2020). Training data requirements for fire severity mapping using Landsat imagery and random forest. Remote Sensing of Environment 245: 111839. - doi: 10.1016/j.rse.2020.111839 

Costa-Saura JM, Bacciu V, Sirca C, Cappelluti O, Spano D, Elia M (2025). The growing link between heatwaves and megafires: evidence from southern Mediterranean countries of Europe. Natural Hazards 121: 17731-17742. - doi: 10.1007/s11069-025-07488-6 

Darvishi Boloorani A, Ranjbareslamloo S, Mirzaie S, Bahrami HA, Mirzapour F, Abbaszadeh Tehrani N (2020). Spectral behavior of Persian oak under compound stress of water deficit and dust storm. International Journal of Applied Earth Observation and Geoinformation 88: 

102082. - doi: 10.1016/j.jag.2020.102082 Escuin S, Navarro R, Fernández P (2008). Fire severity assessment by using NBR (Normalized Burn Ratio) and NDVI (Normalized Difference Vegetation Index) derived from LANDSAT TM/ ETM images. International Journal of Remote Sensing 29: 1053-1073. - doi: 10.1080/01431160 701281072 

Eskandari S, Jaafari MR, Oliva P, Ghorbanzadeh O, Blaschke T (2020). Mapping land cover and tree canopy cover in Zagros forests of Iran: application of Sentinel-2, Google Earth, and field data. Remote Sensing 12: 1912. - doi: 10.3390/rs 12121912 

Eskandari S, Pourghasemi HR, Tiefenbacher JP (2021). Fire-susceptibility mapping in the natural areas of Iran using new and ensemble datamining models. Environmental Science and Pollution Research 28: 47395-47406. - doi: 10.1007/ s11356-021-13881-y 

Giglio L, Schroeder W, Justice CO (2016). The collection 6 MODIS active fire detection algorithm and fire products. Remote Sensing of Environment 178: 31-41. - doi: 10.1016/j.rse.2016.02.054 Goss M, Swain DL, Abatzoglou JT, Sarhadi A, Kolden CA, Williams AP, Diffenbaugh NS (2020). Climate change is increasing the likelihood of extreme autumn wildfire conditions across California. Environmental Research Letters 15: 094016. - doi: 10.1088/1748-9326/ab83a7 He K, Shen X, Merow C, Nikolopoulos E, Gallagher RV, Yang F, Anagnostou EN (2024). Improving fire severity prediction in south-eastern Australia using vegetation-specific information. Natural Hazards and Earth System Sciences 24: 3337-3355. - doi: 10.5194/nhess-24-3337-2024 Huang Y, Jin Y, Schwartz MW, Thorne JH (2020). Intensified burn severity in California’s northern coastal mountains by drier climatic condition. Environmental Research Letters 15: 104033. - doi: 10.1088/1748-9326/aba6af 

Hultquist C, Chen G, Zhao K (2014). A comparison of Gaussian process regression, random forests and support vector regression for burn severity assessment in diseased forests. Remote Sensing Letters 5: 723-732. - doi: 10.1080/ 2150704X.2014.963733 

Ismayilov S (2024). Wildfires engulf forests in multiple Iranian provinces. Report.az, Global Media Group, Azerbaijan, website. [online] URL: http://report.az/en/region/wildfires-engul f-forests-in-multiple-iranian-provinces 

James G, Witten D, Hastie T, Tibshirani R (2021). An introduction to statistical learning: with applications in R (2<sup>nd</sup> edn). Series “Springer Text in Statistics”, Springer Science+Business Media, pp. 607. - doi: 10.1007/978-1-0716-1418-1 

Jolly WM, Cochrane MA, Freeborn PH, Holden ZA, Brown TJ, Williamson GJ, Bowman DM (2015). Climate-induced variations in global wildfire danger from 1979 to 2013. Nature Communications 6 (1): 481. - doi: 10.1038/ncomms85 

37 

Kelly LT, Giljohann KM, Duane A, Aquilué N, Archibald S, Batllori E, Bennett AF, Buckland ST, Canelles Q, Clarke MF, Fortin M-J, Hermoso V, Herrando S, Keane RE, Lake FK, McCarthy MA, Morán-Ordóñez A, Parr CL, Pausas JG, Brotons L (2020). Fire and biodiversity in the Anthropocene. Science 370: eabb0355. - doi: 10.1126/ science.abb0355 

Key CH, Benson NC (2006). Landscape assessment (LA). In: “FIREMON: Fire effects monitoring and inventory system” (Lutes DC, Keane RE, Caratti JF, Key CH, Benson NC, Sutherland S, Gangi LJ eds). Gen. Tech. Rep. RMRSGTR-164-CD, USDA Forest Service, Rocky Mountain Research Station, Fort Collins, CO, USA, pp. LA-1-55. 

Lambert J, Drenou C, Denux JP, Balent G, Cheret V (2013). Monitoring forest decline through remote sensing time series analysis. GIScience and Remote Sensing 50: 437-457. - doi: 10.1080/ 15481603.2013.820070 

Li W, Xu Q, Yi J, Liu J (2022). Predictive model of spatial scale of forest fire driving factors: a case study of Yunnan Province, China. Scientific Reports 12: 19029. - doi: 10.1038/s41598-022-236976 

Long JS, Ervin LH (2000). Using heteroscedasticity consistent standard errors in the linear regression model. The American Statistician 54: 217-224. - doi: 10.1080/00031305.2000.10474549 Marcoulides KM, Raykov T (2019). Evaluation of variance inflation factors in regression models using latent variable modeling methods. Educational and Psychological Measurement 79: 874882. - doi: 10.1177/0013164418817803 

McCarty JL, Aalto J, Paunu VV, Arnold SR, Eckhardt S, Klimont Z, Fain JJ, Evangeliou N, Venäläinen A, Tchebakova NM, Parfenova EI, Kupiainen K, Soja AJ, Huang L, Wilson S (2021). Reviews and syntheses: arctic fire regimes and emissions in the 21<sup>st</sup> century. Biogeosciences 18: 5053-5083. - doi: 10.5194/bg-18-5053-2021 

Mehri S, Alesheikh AA, Lotfata A (2024). Abiotic factors impact on oak forest decline in Lorestan Province, Western Iran. Scientific Reports 14: 545516. - doi: 10.1038/s41598-024-54551-6 Miller JD, Thode AE (2007). Quantifying burn severity in a heterogeneous landscape with a relative version of the delta Normalized Burn Ratio (dNBR). Remote Sensing of Environment 109: 66-80. - doi: 10.1016/j.rse.2006.12.006 Miller CW, Harvey BJ, Kane VR, Moskal LM, Alvarado E (2023). Different approaches make comparing studies of burn severity challenging: a review of methods used to link remotely sensed data with the Composite Burn Index. International Journal of Wildland Fire 32: 449475. - doi: 10.1071/WF22050 

Modugno S, Balzter H, Cole B, Borrelli P (2016). Mapping regional patterns of large forest fires in wildland-urban interface areas in Europe. Journal of Environmental Management 172: 112126. - doi: 10.1016/j.jenvman.2016.02.013 Mohammed, Khan A, Kuri A, Ahammed S, Abir KAM, Arfin-Khan MAS (2025). A Google Earth Engine approach for anthropogenic forest fire assessment with remote sensing data in RemaKalenga Wildlife Sanctuary, Bangladesh. Geology, Ecology, and Landscapes 9 (1): 45-66. - doi: 10.1080/24749508.2023.2165297 

Moradi MJ, Kiadaliri H, Kafaky SB, Bakhoda H (2023). Investigation of the efficiency of MaxEnt, TOPSIS and InVEST models on site suitability and decline potential of Persian oak forests in Zagros, Iran (Ilam Province). Cerne 29: e13135. - doi: 10.1590/01047760202329013135 Moreira F, Viedma O, Arianoutsou M, Curt T, Koutsias N, Rigolot E, Barbati A, Corona P, Vaz P, Xanthopoulos G, Mouillot F, Bilgili E (2011). 

iForest 19: 359-368 

367 

#### _Shahidinejad F et al. - iForest 19: 359-368_ 

Landscape-wildfire interactions in southern Europe: implications for landscape management. Journal of Environmental Management 92: 2389-2402. - doi: 10.1016/j.jenvman.2011.06.028 Moreira F, Ascoli D, Safford H, Adams MA, Moreno JM, Pereira JM, Fernandes PM (2020). Wildfire management in Mediterranean-type regions: paradigm change needed. Environmental Research Letters 15: 011001. - doi: 10.1088/1748-9326/ab541e 

Muhammad S, Ali A, Mehmood K, Ahmad H, Hayat M, Khan MT, Arbab N, Nizami M, Fahad S (2024). Temporal variations in burn severity among various vegetation layers in subtropical _Pinus roxburghii_ (Chir pine) forest of Hindu Kush mountain range. Trees, Forests and People 18: 100664. - doi: 10.1016/j.tfp.2024.100664 Novo-Fernández A, Franks S, Wehenkel C, LópezSerrano PM, Molinier M, López-Sánchez CA (2018). Landsat time series analysis for temperate forest cover change detection in the Sierra Madre Occidental, Durango, Mexico. International Journal of Applied Earth Observation and Geoinformation 73: 230-244. - doi: 10.1016/j.jag. 2018.06.015 

Novo A, Regos A, Fernández C (2025). Machine learning-based predictions of soil burn severity using spectral and LiDAR remote sensing data. Forest Ecology and Management 596: 123094. - doi: 10.1016/j.foreco.2025.123094 

Parks SA, Holsinger LM, Panunto MH, Jolly WM, Dobrowski SZ, Dillon GK (2018). High-severity fire: evaluating its key drivers and mapping its probability across western US forests. Environmental Research Letters 13: 044037. - doi: 10.1088/1748-9326/aab791 

Parks S, Holsinger L, Koontz M, Collins L, Whitman E, Parisien M-A, Loehman R, Barnes J, Bourdon J-F, Boucher J, Boucher Y, Caprio A, Collingwood A, Hall R, Park J, Saperstein L, Smetanka C, Smith R, Soverel N (2019). Giving ecological meaning to satellite-derived fire severity metrics across North American forests. Remote Sensing 11: 1735. - doi: 10.3390/rs1114 1735 

Povak NA, Prichard SJ, Hessburg PF, Griffey V, Salter RB, Furniss TJ, Cova G, Gray RW (2025). Evidence for strong bottom-up controls on fire severity during extreme events. Fire Ecology 21: 00368-1. - doi: 10.1186/s42408-025-00368-1 

Radeloff VC, Helmers DP, Kramer HA, Mockrin MH, Alexandre PM, Bar-Massada A, Butsic V, Hawbaker TJ, Martinuzzi S, Syphard AD, Stewart SI (2018). Rapid growth of the US wildlandurban interface raises wildfire risk. Proceedings of the National Academy of Sciences USA 115: 3314-3319. - doi: 10.1073/pnas.1718850115 

Rahimi I, Duarte L, Teodoro AC (2024). Zagros Grass Index - A new vegetation index to en- 

hance fire fuel mapping: case study in Zagros Mountains. Preprints 2024: 202403.0453.v1. - doi: 10.20944/preprints202403.0453.v1 Ruscalleda-Alvarez J, Moro D, Van Dongen R (2021). A multi-scale assessment of fire scar mapping in the Great Victoria Desert of Western Australia. International Journal of Wildland Fire 30: 886-898. - doi: 10.1071/WF21019 

Sadeghi A, Ahmadi Nadoushan M, Ahmadi Sani N (2024). Segment-level modeling of wildfire susceptibility in Iranian semi-arid oak forests: unveiling the pivotal impact of human activities. Trees, Forests and People 15: 100496. - doi: 10.1016/j.tfp.2024.100496 

Seidl R, Thom D, Kautz M, Martin-Benito D, Peltoniemi M, Vacchiano G, Wild J, Ascoli D, Petr M, Honkaniemi J, Lexer MJ, Trotsiuk V, Mairota P, Svoboda M, Fabrika M, Nagel TA, Reyer CP (2017). Forest disturbances under climate change. Nature Climate Change 7 (6): 395-402. - doi: 10.1038/nclimate3303 

Seydi ST, Abatzoglou JT, AghaKouchak A, Pourmohamad Y, Mishra A, Sadegh M (2024). Predictive understanding of links between vegetation and soil burn severities using physics-informed machine learning. Earth’s Future 12: e2024EF004873. - doi: 10.1029/2024EF004873 Smith CW, Panda SK, Bhatt US, Meyer FJ, Badola A, Hrobak JL (2021). Assessing wildfire burn severity and its relationship with environmental factors: a case study in Interior Alaska boreal forest. Remote Sensing 13: 1966. - doi: 10.3390/rs13101966 

Turco M, Rosa-Cánovas JJ, Bedia J, Jerez S, Montávez JP, Llasat MC, Provenzale A (2018). Exacerbated fires in Mediterranean Europe due to anthropogenic warming projected with nonstationary climate-fire models. Nature Communications 9: 3821. - doi: 10.1038/s41467-018-063 58-z 

USGS (2017). Landsat normalized burn ratio (NBR). Landsat missions, US Geological Survey - USGS, website. [online] URL: http://www.us gs.gov/landsat-missions/landsat-normalized-bu rn-ratio 

Van Der Werf GR, Randerson JT, Giglio L, Van Leeuwen TT, Chen Y, Rogers BM, Mu M, Van Marle MJE, Morton DC, Collatz GJ, Yokelson RJ, Kasibhatla PS (2017). Global fire emissions estimates during 1997-2016. Earth System Science Data 9 (2): 697-720. - doi: 10.5194/essd-9-6972017 

Vanderhoof MK, Menick CE, Picotte JJ, Robertson KM, Nowell HK, Matechik C, Hawbaker TJ (2025). Modelling and mapping burn severity of prescribed and wildfires across the Southeastern United States (2000-2022). International Journal of Wildland Fire 34. - doi: 10.1071/WF2 4137 

Viana-Soto A, Aguado I, Salas J, García M (2020). Identifying post-fire recovery trajectories and driving factors using Landsat time series in fireprone Mediterranean pine forests. Remote Sensing 12: 1499. - doi: 10.3390/rs12091499 

Viedma O, Chico F, Fernández JJ, Madrigal C, Safford HD, Moreno JM (2020). Disentangling the role of prefire vegetation _vs._ burning conditions on fire severity in a large forest fire in SE Spain. Remote Sensing of Environment 247: 111891. - doi: 10.1016/j.rse.2020.111891 

Wang W, Wang X, Wu W, Guo F, Park J, Wang G (2022). Burn severity in Canada’s Mountain National Parks: patterns, drivers, and predictions. Geophysical Research Letters 49: e2022GL0 97945. - doi: 10.1029/2022GL097945 

Wilson JP, Gallant JC (2000). Terrain analysis: principles and applications. Wiley, New York, USA, pp. 479. [online] URL: http://books.goo gle.com/books?id=1311_4-zvy4C 

Withanage NC, Mishra PK, Abdelrahman K, Singh R (2024). Monitoring deforestation, forest health, and environmental criticality in a protected area periphery using geospatial techniques. PeerJ 12: e17714. - doi: 10.7717/peerj. 17714 

Zahabnazouri S, Belmont P, David S, Wigand PE, Elia M, Capolongo D (2025). Detecting burn severity and vegetation recovery after fire using dNBR and dNDVI indices: insight from the Bosco Difesa Grande, Gravina in Southern Italy. Sensors 25: 3097. - doi: 10.3390/s25103097 

Zanaga D, Van De Kerchove R, De Keersmaecker W, Souverijns N, Brockmann C, Quast R, Wevers J, Cara C, Kapur M (2022). ESA WorldCover 10 m 2021 v200. European Space Agency – ESA. [dataset] - doi: 10.5281/zenodo.7254221 

Zheng Z, Zeng Y, Li S, Huang W (2016). A new burn severity index based on land surface temperature and enhanced vegetation index. International Journal of Applied Earth Observation and Geoinformation 45: 84-94. - doi: 10.1016/j. jag.2015.11.002 

Zhou B, Gao S, Yin Y, Zhong Y (2024). Enhancing active fire detection in Sentinel-2 imagery using GLCM texture features in random forest models. Scientific Reports 14 (1): 5629. - doi: 10.1038/ s41598-024-81976-w 

## **Supplementary Material** 

**Appendix 1** - Source code for preprocessing and burn-severity mapping. 

**Tab. S1** - Multicollinearity diagnostics for OLS (HC3): variance inflation factors (VIF) for all predictors. 

**Link:** Shahidinejad_5027@suppl001.pdf 

368 

iForest 19: 359-368 
