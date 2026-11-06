---
title: 'Dynamics and recurrence of fire in the Brazilian Cerrado: spatial patterns, land cover drivers, and implications for integrated fire management'
authors:
- Santos, Alex Mota dos
- Silva, Carlos Fabrício Assunção da
- Nunes, Fabrízia Gioppo
- Pinha, Gisele Daiane
- Amaral, Clayton Alexandre do
year: '2026'
journal: Arabian Journal of Geosciences
doi: 10.1007/s12517-026-12621-1
tags:
- drivers
- prescribed burning
zotero_key: 2ZRIPRFQ
item_type: journalArticle
url: https://openalex.org/W7222820332
source_url: 'unpaywall: https://link.springer.com/content/pdf/10.1007/s12517-026-12621-1.pdf'
fulltext_status: fulltext
synced: '2026-11-06'
---

# Dynamics and recurrence of fire in the Brazilian Cerrado: spatial patterns, land cover drivers, and implications for integrated fire management

## Abstract

Abstract Aims: This study analyzed the spatiotemporal distribution, interannual variability, and recurrence of burned areas across land-use and land-cover (LULC) classes in the Brazilian Cerrado from 2019 to 2024. The main objective was to evaluate how fire regimes interact with natural and human-modified landscapes to support territory-oriented management strategies. Methods: Using MapBiomas Fire (Col. 4.1) and LULC (Col. 10.1) datasets, we quantified burned proportions across LULC types using R ( terra package) and QGIS. Statistical analyses included descriptive statistics, the non-parametric Mann-Kendall test for temporal trends, interannual variance, and pixel-based binary summation to map spatial fire recurrence. Results: Burned areas predominated in native vegetation: savannas (~ 52.8%) and wetlands (~ 19.5%), followed by grasslands (~ 9.1%), while forest formations and pasturelands each accounted for approximately 5.5% of the total burned area. Fire increased significantly in Soybean, Rice, Cotton, and Mosaics of Uses, with a sharp spike in 2024 for savannas and forests, coinciding with extreme dry-season thermal anomalies. High-recurrence hotspots were concentrated in ecotonal zones, particularly in the Ilha do Bananal and surrounding Indigenous Lands, driven by high fuel accumulation and anthropogenic ignitions. Conclusions: Fire in the Cerrado is structural but increasingly threatens fire-sensitive ecosystems like forests and wetlands. Mapping fire recurrence directly operationalizes Integrated Fire Management (IFM) by prioritizing early prescribed burns, optimizing firebreak and brigade placement, aligning intercultural burning calendars with indigenous communities, and establishing protection protocols for vulnerable habitats.

## Full text

Arabian Journal of Geosciences          (2026) 19:213 https://doi.org/10.1007/s12517-026-12621-1 

**ORIGINAL PAPER** 



# **Dynamics and recurrence of fire in the Brazilian Cerrado: spatial patterns, land cover drivers, and implications for integrated fire management** 

**Alex Mota dos Santos**<sup>**1**</sup> **· Carlos Fabricio Assunção da Silva**<sup>**2**</sup> **· Fabrizia Gioppo Nunes**<sup>**3**</sup> **· Gisele Daiane Pinha**<sup>**1**</sup> **· Clayton Alexandre do Amaral**<sup>**1**</sup> 

Received: 18 June 2026 / Accepted: 3 October 2026 © The Author(s) 2026 

#### **Abstract** 

Aims: This study analyzed the spatiotemporal distribution, interannual variability, and recurrence of burned areas across land-use and land-cover (LULC) classes in the Brazilian Cerrado from 2019 to 2024. The main objective was to evaluate how fire regimes interact with natural and human-modified landscapes to support territory-oriented management strategies. Methods: Using MapBiomas Fire (Col. 4.1) and LULC (Col. 10.1) datasets, we quantified burned proportions across LULC types using R ( _terra_ package) and QGIS. Statistical analyses included descriptive statistics, the non-parametric Mann-Kendall test for temporal trends, interannual variance, and pixel-based binary summation to map spatial fire recurrence. Results: Burned areas predominated in native vegetation: savannas (~ 52.8%) and wetlands (~ 19.5%), followed by grasslands (~ 9.1%), while forest formations and pasturelands each accounted for approximately 5.5% of the total burned area. Fire increased significantly in Soybean, Rice, Cotton, and Mosaics of Uses, with a sharp spike in 2024 for savannas and forests, coinciding with extreme dry-season thermal anomalies. High-recurrence hotspots were concentrated in ecotonal zones, particularly in the Ilha do Bananal and surrounding Indigenous Lands, driven by high fuel accumulation and anthropogenic ignitions. Conclusions: Fire in the Cerrado is structural but increasingly threatens fire-sensitive ecosystems like forests and wetlands. Mapping fire recurrence directly operationalizes Integrated Fire Management (IFM) by prioritizing early prescribed burns, optimizing firebreak and brigade placement, aligning intercultural burning calendars with indigenous communities, and establishing protection protocols for vulnerable habitats. 

**Keywords** Fire dynamics · Savanna · Tropical areas · MapBiomas · Remote sensing 

Responsible Editor: Biswajeet Pradhan 

|Carlos Fabricio Assunção da Silva<br>carlos.assuncao@ufpe.br|1<br>Center of Agroforestry Sciences and Technologies, Federal<br>University of Southern Bahia, Rodovia Ilhéus-Itabuna, Km|
|---|---|
|Alex Mota dos Santos|22, Itabuna, Bahia 45604-811, Brazil<br>|
|alexmota@ufsb.edu.br|2<br>Department of Cartographic Engineering, Center of|
|Fabrizia Gioppo Nunes<br>fabrizia@ufg.br|Technologies and Geosciences, Federal University of<br>Pernambuco, UFPE, Avenida Acadêmico Hélio Ramos,<br>Cidade Universitária, s/n, Recife, Pernambuco|
|Gisele Daiane Pinha|50740-530, Brazil|
|pinha.gd@gmail.com|3<br>Institute of Social and Environmental Studies, Federal|
|Clayton Alexandre do Amaral|University of Goiás (UFG), Avenida Esperança, s/n -|
|clayton.amaral@cja.ufsb.edu.br|Samambaia, Goiânia, Goiás 74001-970, Brazil|





<mark>213 Page 2 of 17</mark> 

Arabian Journal of Geosciences          (2026) 19:213 

## **Introduction** 

Fire is a natural component and a global evolutionary factor that has shaped landscapes for millions of years. Under the influence of historical patterns of natural burning, a vast diversity of flora and fauna has developed adaptations to this continuous selective pressure (Simon and Dantas 2025), making plant communities dependent on these events for breaking seed dormancy, suppressing invasive species, and maintaining competitive balance (Rundel et al. 2018). In tropical savannas (such as the Brazilian Cerrado), fire has become a major ecological driver (Santana et al. 2025), shaping these biomes over millennia (Pivello and Fidelis 2025). The Brazilian Cerrado is a heterogeneous region of open, fire-adapted ecosystems interspersed with patches of woody growth forms, exhibiting high levels of biodiversity and endemism (SeguraGarcia et al. 2025). 

In the Cerrado, Alvarado et al. (2017) observed that dryseason length and uneven rainfall distribution throughout the year determine the probability of fire ignition, increasing fire occurrence during dry spells. Thus, weather conditions conducive to fire, commonly referred to as fire-prone conditions, generally include high air temperatures, low soil and air moisture levels, accompanied by strong winds. These characteristics are common in the Cerrado and favor fire occurrence and rapid spread (Masson-Delmotte et al. 2021; Silva et al. 2025a). This is because the Cerrado is South America’s largest tropical savanna and globally the most biodiverse, supporting a wide range of vegetation types with varying sensitivities to fire (Spadoni et al. 2025). 

However, intensifying human activities have profoundly altered these natural ecological dynamics (Santos et al. 2021; Pivello and Fidelis 2025). In response to ongoing land-use changes, coupled with global warming and the increased severity and frequency of drought events, wildfires have intensified substantially (Oliveira et al. 2022). Excessive and uncontrolled burning of vegetation acts as a cyclical driver of environmental degradation (Oliveira et al. 2022; Petrov et al. 2023), disrupting the water balance, heat fluxes, and surface microclimate (Navarro-Rosales et al. 2025), and generating a feedback loop that leads to increasingly extreme fires (De Sales, Werner, and Ribeiro 2023; Navarro-Rosales et al. 2025). In Brazil, the scale of this problem is alarming: human activity has already caused the loss of approximately 43% of the Cerrado’s original vegetation cover (Sano et al. 2019; Luiz and Steinke 2022). This scenario threatens biodiversity, compromises essential ecosystem services (McLauchlan et al. 2020; Freire Junior et al. 2025), and is exacerbated by climate models that predict 

greater thermal and hydrological stress in South America (Viegas et al. 2022). 

Segura-Garcia et al. (2025) show that warmer, drier dryseason periods increase fire activity, while higher annual precipitation increases biomass productivity and expands fuel availability. Furthermore, the researchers identified differences in fire occurrence patterns across the Cerrado regions, with fire activity as the main distinguishing feature: some regions experienced large, numerous, and frequent fires, while others experienced small, infrequent, and few fires. Over time, fire activity in the southern Cerrado has decreased substantially, while in the central and northern regions, it has increased or remained high (Segura-Garcia et al. 2025). 

To investigate areas as vast and complex as the Cerrado, integrating remote sensing with Geographic Information Systems (GIS) has become the ideal methodological framework (Kreri et al. 2026), facilitating environmental monitoring of strategic areas (Sabljić et al. 2026; Allouche 2026). The availability of highly reliable orbital imagery and its derived products makes it possible to accurately observe fire scars, spectral marks left on the surface by the recent removal of plant biomass through combustion, as well as deforested areas, across multiple spatial and temporal scales (Scogings 2023; Feitosa Junior et al. 2024; Silva et al. 2025b). Furthermore, when analyzed with robust statistical models and methods (Martins et al. 2024), these data become key indicators of ongoing pressures on the biome, enabling modeling of ongoing degradation and mapping of high-risk areas. 

In a recent study, Fernandes et al. (2026) analyzed the association between land-use dynamics and fire regimes in transition zones and mosaics under intense pressure from the agricultural frontier in the Cerrado. The authors show that, even in protected areas, the rapid expansion of pastures and croplands in surrounding areas alters the local microclimate, increases fire incidence and recurrence, and reduces savanna and forest remnants. 

Despite advances in satellite monitoring and recognition of the biome’s vulnerability (Arruda et al. 2024; Spadoni et al. 2025), gaps persist in the integrated understanding of how fire frequency and spatiotemporal distribution relate to different land-use and land-cover classes in the Cerrado over time. Understanding the transition between natural fire regimes and fires associated with anthropogenic land-use conversion, using a combined statistical and geographic approach, remains a poorly understood but essential issue for informing precision management strategies. 

In this regard, studying the relationships between the fire regime and the dynamics of Cerrado landscapes is essential 

```
1 3
```

Arabian Journal of Geosciences          (2026) 19:213 

<mark>Page 3 of 17 213</mark> 

for a better understanding of ecological processes and the multiple anthropogenic impacts involved (Sano et al. 2010; Alves and Alvarado 2019, p. 321; Murray et al. 2025; INPE/ Queimadas 2026). Given this context and to address this gap, this study aimed to analyze burned areas and their relationships with land use and land cover in the Cerrado biome from a spatiotemporal perspective. 

This study’s novelty lies in its high-resolution, integrated spatiotemporal modeling that couples continuous firescar dynamics with multi-annual land-use and land-cover (LULC) transitions. This work is critical to distinguish it from previous research in the region. Unlike broad-scale studies such as Alves and Alvarado (2019), which evaluated fire occurrence across Brazilian biomes without pixel-level recurrence mapping or detailed LULC class-specific trend analyses, our study provides a localized, pixel-based temporal sum to identify precise recurrence hotspots in critical ecotonal zones. Furthermore, while Fanin and Van Der Werf (2015) and Carvalho et al. (2017) provided foundational insights into fire patterns in the Amazon and Tocantins State, they lacked the high-resolution, long-term (2019– 2024) systematic evaluation of LULC transitions and the robust trend modeling (Mann-Kendall) applied here across 27 distinct classes. 

This manuscript also represents a distinct advancement over the authors’ prior publications. While Feitosa Junior et al. (2024) provided a broad, systematic literature review of remote sensing methods for savanna fires Silva et al. (2025b) focused primarily on the drivers of deforestation rather than fire dynamics, this work delivers an original empirical analysis of post-fire ecosystem resilience. By integrating interannual variability metrics with high-resolution MapBiomas datasets, we transition from theoretical observations to an operational framework. This study’s primary scientific contribution is to translate spatial fire-recurrence mapping into four concrete, actionable protocols for Integrated Fire Management (IFM), bridging the gap between Remote Sensing diagnosis and territorial fire governance. 

To bridge this gap and operationalize this territorial framework, our study adopts a multi-sensor approach that integrates MapBiomas Fire (Collection 4.1) and LULC (Collection 10.1) datasets across 27 distinct land-cover classes. This 27-class scheme enables fine-grained evaluation of fire susceptibility across subtle ecotonal transitions and agricultural frontiers, which broad-scale syntheses typically mask. Furthermore, applying a pixel-based binary temporal summation framework provides a spatially explicit quantification of fire recurrence (classes 1–6) over 2019–2024, directly establishing the empirical foundation needed to inform targeted Integrated Fire Management (IFM) protocols. 

## **Materials and methods** 

### **Study area** 

The study area encompasses the Cerrado Biome, located in central Brazil (Fig. 1). Considered the world’s most biodiverse savanna, this ecosystem originally covered one-quarter of the country’s territory (Miranda et al. 2009). Currently, covering approximately 2.04 million km² (equivalent to 24% of the national land area), the Cerrado is distributed across eleven Brazilian states (Goiás, Tocantins, Mato Grosso, Mato Grosso do Sul, Minas Gerais, Bahia, Maranhão, Piauí, São Paulo, Paraná, and Rondônia), in addition to the Federal District. 

Its vegetation exhibits a complex phytophysiognomic gradient, ranging from grassland formations (Campo Limpo and Campo Sujo) and savanna formations (Cerrado stricto sensu) to forest formations (Cerradão and Matas de Galeria). Factors such as soil depth, nutrient availability, and fire regime influence this heterogeneity (Ribeiro et al. 2008; Cruz Silva et al. 2025). Native vegetation throughout the Brazilian Cerrado is highly diverse and provides important ecosystem services, including regulating the carbon balance and the water cycle. However, land use and land cover have changed extensively (Lewis et al. 2022). Uncertainty remains about the extent to which phytophysiognomic variations reflect changes in floristic composition versus alterations in community structural architecture (Cruz Silva et al. 2025). 

Among these, the typical Cerrado (strict sense) stands out as a savanna formation characterized by sparse, small, and gnarled trees with thick bark adapted to fire, accompanied by a continuous layer of herbaceous vegetation and grasses (Miranda et al. 2009; Cruz Silva et al. 2025). For thousands of years, natural fires caused by lightning at the onset of the rainy season and anthropogenic fires during the dry season have coexisted in the Cerrado region. This suggests that fire, along with rainfall seasonality and low soil nutrient availability, is one of the determinants of this biome’s vegetation physiognomy (Miranda et al. 2009). 

Most Cerrado soils are dystrophic (base saturation below 50%). The few eutrophic soils identified invariably present strong limitations to plant development, whether physical or chemical (Oliveira et al. 2023). Furthermore, except for clayey Latosols on high plateaus, virtually all other soil classes exhibit, in addition to low natural fertility, physical limitations to plant growth (Oliveira et al. 2023). Thus, clayey Latosols in the Chapadões region of the Central Plateau are preferred for high-tech grain production. Consequently, variations in soil nutrient levels largely drive the distribution and coexistence of these cropping systems (Lewis et al. 2022). 

```
1 3
```

<mark>213 Page 4 of 17</mark> 

Arabian Journal of Geosciences          (2026) 19:213 



**Fig. 1** Geographic location of the study area in the Cerrado biome, Brazil (approximate bounding box: Lat 2°19’ S to 24°41’ S; Lon 41°55’ W to 60°05’ W) 

### **Data source and processing** 

To visually summarize and structure the analytical pipeline, Fig. 2 presents a methodological flowchart. The research workflow is organized into six consecutive stages: (1) Data acquisition, consisting of retrieving multitemporal annual fire-scar data (MapBiomas Collection 4.1) and land-use and land-cover (LULC) classifications (Collection 10.1) from Google Earth Engine; (2) Data processing, performed in R using the _terra_ package to create mosaics of the 54 scenes 

and spatially combine the fire-scar and LULC layers; (3) Data extraction and quantification, to calculate cumulative annual burned areas and weighted percentages for each LULC class; (4) Statistical analysis, comprising descriptive statistics and Mann–Kendall trend tests; (5) Mapping, involving the generation of thematic maps in QGIS; and (6) Results and interpretation, integrating spatial and temporal patterns of burned areas by LULC class. 

We obtained the data for this study from the MapBiomas Project, available in Google Earth Engine for 2019–2024. 



**Fig. 2** Methodological workflow adopted in the analysis of fire scars and land use and land cover in the Brazilian Cerrado (2019–2024) 

```
1 3
```

Arabian Journal of Geosciences          (2026) 19:213 

<mark>Page 5 of 17 213</mark> 

These include fire scar data from the Fire Toolkit (Collection 4.1) and land use and land cover classifications from the LULC Toolkit (Collection 10.1). Collection 4.1 presents annual and monthly mapping of fire scars in Brazil from 1985 to 2024, containing the following informational attributes (tabular data): (a) annual burned area; (b) monthly burned area; (c) frequency of burned area; (d) cumulative burned area; (e) size of fire scars; and (f) year of the last fire occurrence (MapBiomas 2025). 

We processed the fire scar and land use and land cover data in R using the terra package. We used a script to create mosaics of the Fire Toolkit scenes (across 54 scenes) for each of the six years analyzed. Next, we multiplied the fire data by the LULC data to retain land use and land cover class values only in burned areas. 

Next, we extracted and quantified tabular data by land use and land cover class and processed them in R. This allowed us to calculate the total area of accumulated annual burning from 2019 to 2024, along with the percentage of burned area for each land use and land cover class. We weighted this percentage by the biome’s total area, following Alves and Alvarado (2019). Additionally, to evaluate fire susceptibility independently of the spatial extent of each land-cover type, we calculated the annual normalized burned proportion relative to the total area occupied by each class in the Cerrado biome (Pc,t).Pc,t).c,t).,t).t).). **𝑐**<sup>**𝑐**</sup> 

Cerrado biome (Pc,t).Pc,t).c,t).,t).t).). ) × 100 𝑃𝑃𝑐 **𝑐** 𝑐𝑐 = (<sup>𝐴𝐴burned𝑐𝑐</sup><sup>**𝑐**𝑐𝑐</sup> 𝐴𝐴total𝑐𝑐𝑐 Where 𝐴𝐴burned,𝑐𝑐,𝑐𝑐 represents the burned area detected in extent occupied by class LULC class _c_ in year _t_ , and _c_ in the Cerrado biome, derived 𝐴𝐴total,𝑐𝑐 is the total territorial from MapBiomas Collection 10.1. We created the resulting thematic maps in a Geographic Information System (GIS) using QGIS, version 3.40.9. 

We characterized the initial data using descriptive statistics. For each land-use and land-cover class, we calculated the mean, median, standard deviation (SD), coefficient of variation (CV), minimum and maximum values observed over the time series, and the cumulative percentage growth rate between the first and last years analyzed. The mean and median described the central tendency of burned areas, while the standard deviation and coefficient of variation assessed dispersion and temporal stability. The growth rate was calculated based on the relative variation between the initial and final values of the series, enabling the identification of classes with an increase or decrease in the areas affected by fire over the study period. 

Temporal trends were assessed using the nonparametric Mann-Kendall test, widely used in environmental studies to identify monotonic trends in time series. For each class, 

Kendall’s Tau coefficient, which expresses the direction and intensity of the temporal trend, and the corresponding p-value were obtained to verify its statistical significance. Positive Tau values indicate an increase in fire scar areas over time, while negative values indicate a decrease. We considered trends statistically significant when the significance level was less than 5% ( _p_ < 0.05). 

To provide more detail, we calculated descriptive statistics by land-use class using the dplyr and tidyr packages to quantify interannual variability in fire scars by land-use and land-cover class (Eq. 1). According to Siddiqui (2025), these tools are essential for reshaping complex and disorganized datasets into an ordered structure suitable for analysis. To quantify the temporal dispersion and stability of fire scars across different land-use and land-cover classes, we calculated the interannual variability of burned areas for each LULC class (Eq. 1): 



<!-- Start of picture text -->
√<br>√√ 1 − 2<br>∑𝑇𝑇 (1)<br>⎷ 𝑡 𝑡<br>𝜎𝜎 c = (𝐴𝐴𝑐 𝑐 𝑡𝑡 𝑇 𝐴𝐴𝑐𝑐)<br>𝑇𝑇𝑇1<br><!-- End of picture text -->

Where: is the interannual variability (expressed as the temporal standard deviation) of burned areas for LULC class𝜎𝜎 c c; Ac,t is the total burned area detected in LULC class c at yeart ; − Ac the historical mean annual burned area calculated for LULC class c over the entire analyzed time series; ∑ represents the summation of the squared differences from year _t_ = 1 to _T;_ T the total number of years in the analyzed time series (where T = 6, representing the period 2019–2024). Fire recurrence was mapped at the pixel level using a binary temporal sum across the 6-year series (2019–2024) (Eq. 2), adapted from Daldegan et al. (2014): 

𝑇𝑇 ∑ (2) 𝑡 𝑡 𝑅𝑅𝑖𝑖 = 𝑥𝑥𝑖 **𝑖** 𝑡𝑡 recurrence of fires in pixel _i;_ 𝑅𝑅𝑖𝑖 ranges from 0 to 6, where 0 = not burned; 1 = burned once; 2 = burned twice; 3 = burned three times; 4 = burned 𝑅𝑅𝑖𝑖 four times; 5 = burned five times; and 6 = burned in all six analyzed periods; pixel value at time t (0 = not burned; 1 = burned); _T_ 𝑥𝑥𝑖 **𝑖** 𝑖𝑖 total number of periods (in this case, 6). 

This analysis was also performed using the terra package in R. According to Hijmans et al. (2023), the terra package implements two main classes (data types): SpatRaster and 

```
1 3
```

<mark>213 Page 6 of 17</mark> 

Arabian Journal of Geosciences          (2026) 19:213 

SpatVector. SpatRaster, which is of interest to this study, supports the manipulation of large raster files that cannot be loaded entirely into memory; local, focal, zonal, and global raster operations; conversion of polygons, lines, and points to raster; integration with modeling methods to perform spatial predictions; among other features. 

To compare the spatial pattern of fire recurrence between the entire Cerrado biome and protected areas (Indigenous Lands) in the study area, we used the Chi-Square Test of Inderecommended for assessing whether the frequency distribu-pendence ( 𝜒𝜒<sup>2</sup> ). This nonparametric statistical technique is tion of a categorical or ordinal variable (in this case, recurrence classes ranging from 1 to 6 fire events) differs significantly between two or more independent groups (biome vs. protected areas). We performed the Chi-Square Test of Independence using the stats package in R (R Core Team 2021). 

To construct the contingency table, we arranged the recurrence classes in the rows and the territorial contexts in the columns, using the corresponding affected area values. The test evaluated the null hypothesis (H0) that the proportion of areas affected by different fire frequencies is homogeneous and independent of the territorial context analyzed, with a significance level set at 5% ( _p_ < 0.05). We performed all analyses and computations in R. 

## **Results** 

An assessment of the spatial and temporal distribution of burn scars in the Cerrado biome reveals a marked concentration in specific vegetation types. As shown in Fig. 3, most fire-affected land lies within a limited set of land cover classes. The Savanna Formation is the dominant class, accounting for about 52.8% of the total burned area, followed by Wetlands (~ 19.5%) and Grasslands (~ 9.1%), while Forest Formations and Pastures each accounted for about 5.5% of the burned area. 

Furthermore, forest fires have increased significantly, with a particularly sharp rise in 2024. The recurring fires in these ecosystems suggest growing pressure on plant communities less adapted to fire, which may contribute to changes in vegetation structure and composition and to environmental degradation. 

The proportion of burned areas (Fig. 4) showed little variation between 2019 and 2023, remaining highest in the Wetland, Rice, Grass, and Savanna Formation classes. In 2024, burned areas increased significantly, particularly in the Wetland (34%) and Rice (33%) classes, followed by Grass (19%) and Savanna Formation (10%). The remaining classes remained below 5%, showing more modest variations over the period. 

Overall, the fire regime in the Cerrado is strongly influenced by vegetation cover structure and composition, with a clear predominance of savanna ecosystems and notable stability throughout the time series. This regularity points to a recurrent fire dynamic, regulated by an interplay between climatic variables and anthropogenic pressures. Fire outbreaks and burn scars are not concentrated within the cores of intensive agriculture but tend to occur in edge zones and agricultural transition areas. The proportional distribution among the different classes remained stable throughout the period analyzed, with only subtle variations. This consistent pattern reinforces the existence of a structural fire regime. At the same time, the significant proportion of wetlands, which account for between 18% and 20% of the total burned area, is noteworthy and highlights the high vulnerability of these vital ecosystems, especially during years of water scarcity and severe droughts. 

Table 1 presents descriptive statistics for fire scars (km²) by land use and land cover classes in the Cerrado Biome, including measures of central tendency (mean and median), dispersion (standard deviation and coefficient of variation), minimum and maximum values observed during the period, as well as the cumulative growth rate between the years evaluated. These indicators help identify magnitude, 



**Fig. 3** Proportion of fire scars by land use and land cover classes in the Cerrado Biome 

```
1 3
```

Arabian Journal of Geosciences          (2026) 19:213 

<mark>Page 7 of 17 213</mark> 

**Fig. 4** Annual proportion of the burned area relative to the total area for each land use and land cover class from 2019 to 2024 



**Table 1** Descriptive statistics for fire scars (km²) by land-use and land-cover classes in the Cerrado Biome during the period analyzed 

|Class|Mean|Median|Standard deviation|Coefficient of variation|Minimum|Maximum|Growth rate|
|---|---|---|---|---|---|---|---|
|Rocky Outcrop|446.56|385.45|149.69|fi<br>33.52|385.43|752.12|95.14|
|Cotton (beta)|7.75|5.68|6.53|84.28|3.32|20.59|426.85|
|Hypersaline Tidal Flat|0.44|0.48|0.10|23.15|0.23|0.49|-50.51|
|Aquaculture|0.00|0.00|0.00|173.65|0.00|0.01|n/a*|
|Rice|256.57|245.31|37.30|14.54|232.67|330.76|42.16|
|Coffee|5.41|5.63|0.33|6.17|4.95|5.63|-1.15|
|f<br>Wetland|17,042.98|16,272.29|1,928.51|11.32|16,195.60|20,979.02|28.84|
|Sugar cane|558.01|421.48|354.51|63.53|381.45|1280.76|209.24|
|Citrus|1.77|0.78|2.56|144.65|0.63|6.98|768.43|
|Floodable Forest|0.00|0.00|0.00|56.60|0.00|0.01|80.00|
|Grassland|8,001.39|7,600.55|1,034.47|12.93|7,507.95|10,111.60|32.86|
|Forest Formation|4,828.65|4309.30|1613.04|33.41|3,842.32|8,085.92|81.27|
|Savanna Formation|46,226.89|44,821.10|4,453.49|9.63|43,216.64|55,189.85|21.81|
|Mangrove|0.00|0.00|0.00|59.81|0.00|0.01|n/a*|
|Mining|0.11|0.00|0.27|241.17|0.00|0.67|n/a*|
|Mosaic of Uses|2,665.16|2,461.23|1,447.85|54.33|991.97|4,542.51|357.93|
|Other Perennial Crop|5.08|6.11|1.78|35.09|1.88|6.18|113.06|
|Other Temporary Crop|231.06|229.55|29.58|12.80|198.71|273.19|-11.47|
|<br>Other non-vegetated area|89.49|85.26|14.03|15.67|78.43|117.34|-2.22|
|Pasture|4,863.14|4,874.33|187.07|3.85|4,571.52|5,078.48|-9.98|
|Beach, Dune and Sand Spot|0.00|0.00|0.00|93.04|0.00|0.01|-35.71|
|Herbaceous Sandbank Vegetation|3.98|3.63|0.89|22.26|3.61|5.79|59.70|
|River, Lake and Ocean|1.26|1.46|1.10|87.64|0.00|2.69|n/a*|
|<br>Forest Plantation|151.52|125.34|68.01|44.89|119.63|290.28|142.65|
|Soybean|2,113.29|2,075.31|148.26|7.02|1,991.24|2,392.68|20.16|
|Photovoltaic Power Plant (beta)|0.0884|0.00|0.16|181.05|0.00|0.369|n/a*|
|Urban Area|0.27|0.07|0.54|202.75|0.00|1.36|n/a*|



*n/a: Cumulative growth rate was not calculated for classes with zero or near-zero initial burned area in 2019 to avoid mathematical divisionby-zero artifacts 

temporal stability, and major changes in each class over the time series. 

In contrast, the distribution of fire scars across certain landuse classes changes significantly throughout the analyzed time series. The increase in categories such as mixed-use mosaic, 

sugarcane, forestry, and certain agricultural crops indicates a higher relative contribution of these areas to fire occurrence. At the same time, the reduction observed in other classes may reflect land-use changes, changes in the fire regime, or the limited spatial representativeness of these categories. 

```
1 3
```

<mark>213 Page 8 of 17</mark> 

Arabian Journal of Geosciences          (2026) 19:213 

**Table 2** Results of the Mann-Kendall test applied to fire scar areas across different land-use and land-cover classes in the Cerrado Biome 

|Class|Kend-<br>all’s tau|_P_value|Trend|
|---|---|---|---|
|Rocky Outcrop|0.6000|0.1329|No Trend|
|Cotton (beta)|0.8667|0.0242*|Upward|
|Hypersaline Tidal Flat|0.3333|0.4524|No Trend|
|Aquaculture|-0.8944|0.0268*|Downward|
|Rice<br>f|1.0000|0.0085*|Upward|
|Coffee|0.2760|0.5661|No Trend|
|Wetland|-0.3333|0.4524|No Trend|
|Sugar cane|-0.0667|1.0000|No Trend|
|Citrus|-0.2760|0.5661|No Trend|
|Floodable Forest|-0.2148|0.6967|No Trend|
|Grassland|-0.3333|0.4524|No Trend|
|Forest Formation|-0.3333|0.4524|No Trend|
|Savanna Formation|-0.3333|0.4524|No Trend|
|Mangrove|-0.7333|0.0603|No Trend|
|Mining|-0.2760|0.5661|No Trend|
|Mosaic of Uses|1.0000|0.0085*|Upward|
|Other Perennial Crops|-0.3333|0.4524|No Trend|
|Other Temporary Crops|-0.3333|0.4524|No Trend|
|Other non-vegetated Areas|-0.0667|1.0000|No Trend|
|Pasture|-1.0000|0.0085*|Declining|
|Beach, Dune and Sand Spot|-0.5521|0.1806|No Trend|
|Herbaceous Sandbank Vegetation|-0.2000|0.7071|No Trend|
|River, Lake and Ocean|-0.4140|0.3389|No Trend|
|Forest Plantation|0.7333|0.0603|No Trend|
|Soybean|1.0000|0.0085*|Rising|
|Photovoltaic Power Plant (beta)|0.7746|0.0712|No Trend|
|Urban Area|-0.2760|0.5661|No Trend|



To assess trends in fire scars across land-use and landcover classes in the Cerrado Biome, we applied the nonparametric Mann-Kendall test. Table 2 presents Kendall’s tau coefficients, their respective significance values, and the direction of the trends identified for each class analyzed over the time series. 

The Mann-Kendall test results indicate that most evaluated classes showed no statistically significant temporal trend in fire-scarred areas during the analyzed period. Among the exceptions, significant increasing trends were identified for Soybean, Rice, Mosaic of Uses, and Cotton (beta), indicating a progressive increase in the burned area within these classes over the time series. 

The analysis of interannual variability in burned extent (Fig. 5) reveals highly heterogeneous behavior among landuse and land-cover classes. Savanna Formation records substantially higher values than the other categories, with a high median (approximately 44,000 to 45,000 km²) and relatively low dispersion, confirming the high frequency and spatial consistency of fire in this class. In contrast, areas classified as Mosaic of Uses show a greater range of variation, reflecting greater sensitivity to human dynamics and interventions. In turn, classes associated with direct agricultural and livestock use, such as Pasture and Soybean, show interannual fluctuations but contribute less to the total burned area, reinforcing the idea that fire dynamics in the biome are predominantly structural rather than merely episodic. 

Upon examining the Savanna Formation (Fig. 6) in detail, which accounts for the largest absolute extent of 



**Fig. 5** Interannual variability of burned scar areas in relation to land use and land cover 

```
1 3
```

Arabian Journal of Geosciences          (2026) 19:213 

<mark>Page 9 of 17 213</mark> 

burn scars, a marked inflection in the temporal trend can be observed: following a period of relative stability with a downward trend between 2019 and 2023, the year 2024 saw a significant and atypical increase in the burned area. 

Regarding fire recurrence, the cumulative area reached 265,837.23 km² over the analyzed period. The Ilha do Bananal region (Fig. 7), located in Tocantins in the centralwestern portion of the biome, shows a very high spatial concentration. This zone forms part of the ecotonal transition between the Cerrado and the Amazon, harboring a unique system of seasonal wetlands whose vegetation is highly adapted to both the fire regime and local climatic variations. An analysis of fire recurrence during the period indicated that one-time fire events covered 173,126.05 km². Areas affected by recurring fires over two, three, four, five, and six years covered 71,217.33 km², 32,327.93 km², 14,761.93 km², 6,578.92 km², and 2,671.22 km², respectively; the latter corresponds to 0.13% of the total area of the Cerrado biome. In other words, 2,671.22 km² (equivalent to approximately 370,000 soccer fields) of the Cerrado biome burned each year in the period analyzed. 

Recurrence mapping shows that fire is a widespread phenomenon throughout the Cerrado, with records of at least one burning event across virtually the entire assessed area. However, high-recurrence areas are primarily located in the central-western region, within vegetation types with higher flammability, such as savanna and grassland strata. This spatial distribution of high-recurrence fire hotspots was predominantly driven by low topographic relief and high fuel continuity, rather than complex terrain barriers. The highrecurrence zones, particularly the Ilha do Bananal and surrounding ecotonal plains, are characterized by flat fluvial terrains with minimal elevation gradients. In these seasonal wetlands and adjacent flat savannas, local topographic variation is negligible and does not impose structural barriers 

to fire propagation. Instead, the regional hydrological pulse governs fire distribution by controlling wet-season biomass accumulation and rapid dry-season fuel desiccation, making fuel availability and horizontal continuity the primary drivers of fire spread. 

This pattern also appears in the analysis of Indigenous Lands (Fig. 8), highlighting the overlap between areas with high fire recurrence and protected territories in the ecotone zone. An analysis of fire recurrence within Indigenous Lands during the period under review indicated that one-time fire events covered 4,660.79 km². Areas affected by recurring fires over two, three, four, five, and six years totaled 6,061.78 km², 7,377.31 km², 6,310.06 km², 3,939.92 km², and 1,859.40 km², respectively; burned areas recurred in all years within the Savanna Formation land-use class. 

The chi-square test of independence revealed a statistically significant difference in fire recurrence distributions between the Cerrado biome and the interior of Indigenous Lands (χ² = 40.245, df = 5, _p_ < 0.001). While the biome exhibits a decreasing pattern concentrated in single fire events (57.58%), the Indigenous Lands show a concentration of affected area at intermediate recurrence frequencies (3 and 4 events, totaling more than 45% of the burned area), indicating a distinct disturbance regime in these territories. 

Finally, the low population density observed in several municipalities in the region constitutes a critical vulnerability factor. Municipalities with smaller populations tend to encompass vast areas dominated by agricultural and livestock activities and remaining natural habitats, which expands the contact zone between productive land uses and native vegetation. In the Ilha do Bananal region, this situation is exacerbated by extensive seasonal floodplain areas, savanna vegetation, and Indigenous Lands, which together form an ecosystem mosaic characterized by high susceptibility and frequent fires. 



**Fig. 6** Trend analysis of the Savanna formation class from 2019 to 2024 

```
1 3
```

<mark>213 Page 10 of 17</mark> 

Arabian Journal of Geosciences          (2026) 19:213 



**Fig. 7** Burned area recurrence in the Cerrado Biome (approximate bounding box: Lat 2°19’ S to 24°41’ S; Lon 41°55’ W to 60°05’ W) 

## **Discussion** 

The spatial and temporal distribution of fire in the Cerrado reveals heterogeneous dynamics that reflect the combined influence of vegetation structure, anthropogenic activities, and landscape occupation patterns (Pivello 2011). The results show that fire is predominantly concentrated in natural formations, particularly Savanna Formation, Wetland, Grassland, and Forest Formation, reaffirming that fire occurrence remains associated with native phytophysiognomies characterized by high biomass and extensive spatial continuity (Alves and Alvarado 2019; RAF 2026). 

This association, characterized by the predominance of Savanna Formation, aligns with structural ecological determinants such as high herbaceous biomass, marked climatic seasonality, and high natural flammability. This perspective is associated with the natural fire regime, in which naturally occurring fires (predominantly caused by lightning strikes) may occur during transitions between the dry and rainy seasons (at the beginning or end of the season), often accompanied by precipitation, which limits the intensity and extent of the event (Pausas et al. 2018). Therefore, fireaffected areas that are consolidated and exhibit high recurrence are associated with anthropogenic patterns, in which 

```
1 3
```

Arabian Journal of Geosciences          (2026) 19:213 

<mark>Page 11 of 17 213</mark> 



**Fig. 8** Spatial distribution of burned area recurrence in indigenous lands located within the transition zone between the Cerrado and Amazon biomes, highlighting the Ilha do Bananal region (approximate bounding box: Lat 9°30’ S to 13°00’ S; Lon 49°50’ W to 51°15’ W) 

human-induced fires are concentrated at the peak of the dry season (August to October) in the Cerrado, when atmospheric and soil moisture deficits are highest. This results in high-intensity, high-severity fires that eliminate the natural recovery window for vegetation and alter the phenological synchrony of native species (Arruda et al. 2024). 

Verona et al. (2026) show that the Brazilian Cerrado harbors one of the largest carbon-storage ecosystems in tropical America but is highly vulnerable to land-use change and intensified drought. In open physiognomies, higher wind speeds, higher temperatures, and lower fuel moisture 

accelerate fire spread compared with forest environments. This behavior is consistent with Alves and Alvarado (2019), who showed the predominance of fires in natural vegetation, and Martins et al. (2026), who identified recurrent fires in savanna, forest, pasture, and mosaic-of-uses physiognomies. 

Analysis of the temporal evolution of mean temperature in the hottest month of the Cerrado Biome, September, from 1985 to 2025 reveals a clear and concerning trend of continuous warming over the past four decades (Copernicus Climate Change Service 2023). September, which historically marks the peak and closing phase of the region’s 

```
1 3
```

<mark>213 Page 12 of 17</mark> 

Arabian Journal of Geosciences          (2026) 19:213 

dry season, shows a marked structural shift in its thermal regime. While mean temperatures in the 1980s and 1990s predominantly ranged from 29.5 °C to 33.0 °C, with the lowest value recorded in 1992 (approximately 29.4 °C), subsequent decades shifted progressively toward substantially higher levels. From the 2000s onward, with strong acceleration after 2010, mean values frequently exceeded 33.0 °C, culminating in an unprecedented sequence of thermal anomalies between 2019 and 2025. During this recent period, the monthly mean consistently exceeded 34.0 °C, reaching the absolute historical peak of the series in 2024, when it exceeded 35.0 °C. This end-of-dry-season temperature increase plays a determining role in biome dynamics and coincides with larger burned areas in the Savanna Formation class. 

Our observation that fire recurrence is primarily decoupled from steep topographic constraints aligns with these regional landscape characteristics. In vast fluvial plains and ecotonal depressions like the Bananal basin, the absence of prominent relief variations allows fires to spread unimpeded across extensive, continuous grassland and savanna fuels. Consequently, rather than local microclimatic variations or elevation-induced temperature gradients, the macroclimatic dry-season thermal stress, exemplified by the regional September temperature anomalies exceeding 35 °C in 2024, homogeneously desiccates the fuel bed across these plains. This widespread fuel dryness, coupled with anthropogenic ignitions, overrides local topographic influences and explains the massive spatial contagion observed in ecotonal native vegetation. 

Increased thermal stress intensifies evapotranspiration, drastically reduces soil and air moisture, and accelerates the desiccation of plant biomass and accumulated necromass. This reveals that, in the Cerrado, the heat-stress chain is characterized by greater atmospheric and soil dryness, which, in turn, results in biomass desiccation and increased wildfires (Ivo et al. 2020; Oliveira et al. 2021; Rodrigues et al. 2021). 

In contrast, fire dynamics in areas transformed by land use show distinct patterns across classes. Fire occurrence in agricultural areas suggests a greater recent contribution of the productive sector to fire-scar dynamics, possibly linked to agricultural and livestock management practices, the expansion of production frontiers, or greater exposure of these land-use matrices to fire (Arruda et al. 2024). In contrast, the Pasture class showed a significant decreasing trend in total burned area, corroborating Sano et al. (2010), which identified reduced fire occurrence in pastures as reflecting changes in land-use practices. Trends observed in classes such as Forest Plantation, Mangrove, and Aquaculture should be interpreted with caution because of their lower spatial representativeness and the limitations imposed by the data series’ temporal extent. 

However, anthropogenic changes in Pasture, combined with climate change, still create uncertainties and potential risks for the biome’s ecosystems (Segura-Garcia et al. 2025). According to Costa et al. (2023), pasture degradation in the Cerrado has resulted in the loss of more than 100 MtC of soil organic carbon over the past two decades. This degradation is further aggravated by changes in fire regimes, which promote massive CO2 release and convert areas that should act as carbon sinks into active sources of greenhouse gas emissions (Navarro-Rosales et al. 2025). 

Although native vegetation is adapted to fire and fire plays a fundamental role in nutrient cycling and ecosystem regeneration (Pivello and Fidelis 2025), the recent intensification of extreme events reflects the overlap between climate anomalies and anthropogenic burning regimes. Drought during the ignition season is among the main predictors of burned areas in the biome (Alvarado et al. 2017), while heat waves directly drive fire activity (Bezerra et al. 2025). In 2024, 97 thousand km² burned in the Cerrado, of which 85% occurred in native vegetation, a 47% increase over the average of the previous six years (MapBiomas 2026). Altered fire regimes, whether through excessive fire frequency or complete fire exclusion, compromise vegetation resilience, resulting in floristic impoverishment, structural damage, and ecosystem degradation (Gomes et al. 2018). 

Accurately identifying these temporal and spatial variations among land-cover classes has become increasingly urgent given the global increase in wildfire frequency and severity (Gonçalves et al. 2025). Recurrence analysis is essential because accumulated dead biomass and necromass from previous fires create a feedback effect that favors new combustion events (Argibay et al. 2020). 

Areas with high concentrations of one- and two-year fire recurrence coincide with the agricultural frontier expansion zone in Brazil. According to Arruda et al. (2024), this area in the northern portion of the biome exhibited significant fire clusters, with burned areas increasing as agricultural expansion progressed. 

To contextualize these findings within global savanna fire ecology, a comparison with other major savanna systems, such as those in Africa and Australia, reveals both shared structural drivers and critical ecological distinctions. Globally, tropical savannas are defined by a strongly seasonal climate that alternates between a wet season conducive to rapid grass biomass production and a dry season that desiccates this fuel bed (Miranda et al. 2009). However, the extent to which native herbivory pressures differentiate fire regimes between African savannas and the Cerrado remains a key hypothesis for future comparative research. While African savannas co-evolved with large mammalian herbivore guilds that may reduce fuel continuity, the Cerrado lacks comparable large native grazers (Pivello and Fidelis 2025). Whether 

```
1 3
```

Arabian Journal of Geosciences          (2026) 19:213 

<mark>Page 13 of 17 213</mark> 

these differences in herbivore assemblages directly influence biomass accumulation, fuel loads, or fire behavior across global savannas requires formal empirical testing. 

Furthermore, comparative management paradigms offer vital insights for operationalizing Integrated Fire Management (IFM) in Brazil. In northern Australian savannas, active fire management has shifted from reactive suppression to proactive, Indigenous-led early dry-season prescribed burning programs (such as those in Arnhem Land), which significantly reduce late dry-season wildfire extent and greenhouse gas emissions. This model closely mirrors the ecological necessity identified in our study for the Ilha do Bananal and surrounding Indigenous Lands, where aligning traditional burning calendars and implementing early prescribed burns can prevent the catastrophic fuel-driven wildfires observed in 2024. By adopting these globally validated, territory-oriented fire management strategies, Brazil can enhance the resilience of the Cerrado’s fire-sensitive forest and wetland ecotones, bridging local spatial diagnostics with international savanna conservation frameworks. This aligns with anthropogenic fire patterns, in which human-induced ignitions concentrate during the late dry season (August to October), a window Arruda et al. (2024) highlight as having shifted historically toward delayed, higher-severity burning across the biome. 

In areas with higher fire recurrence, fire is concentrated in the western portion. This result highlights the importance of an ecoregion-based analysis, which identified fire hotspots; within the Ilha do Bananal ecoregion, the biome’s largest wetland, it showed the highest fire recurrence and the largest fire-scar sizes over time. 

These analyses are particularly relevant in ecotonal and environmentally vulnerable areas, such as the transition between the Cerrado and the Amazon, where fire recurrence rates are highest. This region encompasses a unique system of seasonal wetlands adapted to climatic variability and fire (Valente et al. 2013). The Ilha do Bananal stands out as one of the country’s most complex fire hotspots because of its hydrological regime. During the rainy season, water availability promotes the accumulation of herbaceous biomass; during the falling-water and dry seasons, this material rapidly dries out, becoming continuous and highly flammable fuel (Valente et al. 2013), across which the widespread use of fire for the management of native pastures and cultural practices takes place. 

The high prevalence of fires in Bananal Island is consistent with the historical series presented by Fanin and Van der Werf (2015) and Carvalho et al. (2017), and is further confirmed by recent studies by Sousa et al. (2026). In the region, approximately 92% of fires occur in Grassland, and 75.9% are of human origin, revealing strong anthropogenic pressure on native areas and Indigenous Lands (Aragão et al. 2023). 

From a socioeconomic perspective, Carvalho et al. (2017) explain that municipalities with larger burned areas surrounding Bananal Island have higher agricultural GDP, lower services/industry GDP, and lower population density. The strong dependence on the primary sector reflects the expansion of extensive livestock farming and the use of fire as a rudimentary management tool. At the same time, limited urban infrastructure and low institutional presence in these municipalities constrain local enforcement and firefighting capacity. 

However, UNESCO recognizes Ilha do Bananal as a Biosphere Reserve, and the Ramsar Convention covers it, encompassing Araguaia National Park and Indigenous lands with approximately 15 villages of the Karajá and Javaé peoples (Toral 2004). This territory’s importance lies in its exceptionally high socio-biodiversity, which deforestation and climate change seriously threaten (Lenza et al. 2024). Uncontrolled fires in the region not only degrade biodiversity but also directly affect public health, the regional economy, and the physical and cultural survival of traditional communities (Sousa et al. 2026). 

Uncontrolled fire remains one of the most severe threats to the Cerrado (Gomes et al. 2018), making it imperative to move beyond firefighting and focus on effectively managing its impacts (Gonçalves et al. 2025). Spatial diagnosis and the identification of recurrence patterns provide vital support for Integrated Fire Management (IFM), enabling the prevention of catastrophic fires and the development of more effective conservation actions (Silva et al. 2023; Hoffmann et al. 2025). Understanding the causes and priority fire zones is fundamental to guiding public policies that reconcile biodiversity protection, risk mitigation, and respect for traditional territories (Alvarado et al. 2017). 

The chi-square test of independence revealed a statistically significant difference in fire recurrence distributions between the Cerrado biome and the interior of Indigenous Lands (χ² = 40.245, df = 5, _p_ < 2.2 × 10⁻¹⁶). While the biome exhibits a decreasing pattern concentrated in single fire events (57.58%), the Indigenous Lands (ILs) show a concentration of affected area at intermediate recurrence frequencies (3 and 4 events, totaling more than 45% of the burned area), indicating a distinct disturbance regime in these territories. This profile in Indigenous Lands (ILs), particularly in socio-environmental complexes vulnerable to external pressures, such as Ilha do Bananal, aligns directly with the principles of Integrated Fire Management (MIF), implemented by IBAMA’s Prevfogo Specialized Center in coordination with traditional communities. As Leonel (2000) and Falleiro et al. (2016) note, local ethnic groups’ use of fire should not be confused with accidental or arson fires in agricultural systems; rather, these are prescribed, controlled burns carried out in spatial and temporal mosaics 

```
1 3
```

<mark>213 Page 14 of 17</mark> 

Arabian Journal of Geosciences          (2026) 19:213 

that respect ecological return intervals. Thus, the concentration of intermediate burning frequencies reflects adaptive management that avoids both total fire suppression, which would lead to biomass accumulation and catastrophic fires, and degradation from continuous annual burning, thereby consolidating Indigenous Lands (ILs) as active conservation barriers in the Cerrado. 

### **Study limitations** 

Although this study provides a comprehensive and integrated analysis of fire dynamics and recurrence in the Cerrado Biome, some methodological and operational limitations should be considered when interpreting the results. For example, the temporal scope of the historical series was defined to update previously presented analyses. Although this period is suitable for identifying recent patterns, shortterm climate anomalies, and significant interannual fluctuations, this time window limits the analysis of the effects of the El Niño–Southern Oscillation (ENSO) cycle and longerterm global climate trends. Furthermore, the spatial resolution and detection of burned areas derived from orbital sensors (such as Landsat, with a spatial resolution of 30 m) limit the detection of small fire scars (sub-pixel burns) or understory fires (low-canopy fires) in dense forest formations and gallery forests. In these environments, canopy cover may mask the spectral signals of the burned surface. 

Additionally, attributing ignition causes through geoprocessing and remote sensing enables accurate mapping of the spatial distribution and recurrence of fire scars; however, it does not directly identify the exact origin of ignition (whether anthropogenic, intentional, accidental, or natural, caused by lightning). The association with human activity is inferred indirectly based on proximity to infrastructure, agricultural edges, and Indigenous lands. 

Furthermore, three analytical limitations must be explicitly acknowledged. First, reported raw burned-area proportions across LULC classes require careful interpretation, as unnormalized figures in dominant land cover types (e.g., savannas) may partially reflect their spatial dominance rather than fire preference alone. Second, classification errors inherent to the orbital MapBiomas LULC dataset (Collection 10.1), particularly across ecotonal transitions and mixed agricultural classes, may propagate into classspecific burned area estimates. Third, the short 6-year temporal window (2019–2024) is insufficient to definitively separate multi-decadal climate trends from short-term interannual variability. Specifically, applying the non-parametric Mann–Kendall test to only six time points yields very low statistical power, requiring observed trend statistics to be interpreted as short-term observational indicators rather than long-term trajectories. 

## **Conclusion** 

An analysis of fire scars in the Cerrado Biome revealed that fire dynamics are strongly associated with land-use and land-cover classes, with a marked predominance in savanna formations (~ 52.8%), followed by wetlands (~ 19.5%) and grasslands (~ 9.1%). This pattern confirms that fire is a structural element of the biome, recurring and consistent over time rather than an isolated phenomenon. 

Although the Cerrado is naturally adapted to fire, rising fire frequency and intensity may exceed its capacity for ecological resilience, resulting in biodiversity loss, vegetation structure changes, and environmental degradation. The significant increase in forest fires and wetland fires, especially in recent years, reinforces concerns about their spread into environments less adapted to this disturbance, possibly influenced by extreme weather events such as prolonged droughts and heat waves. 

The relative stability of the proportions of burned areas across classes over the years indicates a persistent fire regime, strongly influenced by both climatic factors and human activities. Although anthropogenic areas exhibit greater interannual variability, their total contribution is smaller, suggesting that fire in the Cerrado has a structural character but with significant human influence, especially in transition areas and land-use mosaics. 

The recurrence analysis revealed a concentration of repeatedly burned areas, notably in the Ilha do Bananal region, an ecologically sensitive area of high biodiversity importance. In these regions, fire recurrence is associated with vegetation flammability and accumulated combustible material, as well as strong anthropogenic influence, including intentionally set fires. 

Finally, the results highlight the imperative need to shift from a model focused exclusively on firefighting and suppression to effective Integrated Fire Management (IFM) strategies. To implement IFM practically, the spatial distribution of fire recurrence must directly inform decision-making through targeted actions: (1) delineating priority zones for prescribed and preventive burning at the start of the dry season, thereby reducing the accumulated fuel load in areas with high fire frequency; (2) in the spatial planning of firebreaks and the strategic allocation of fire brigades and firefighting infrastructure during the time windows of highest risk; (3) in strengthening participatory and intercultural fire management, aligning the schedules of traditional and subsistence burning by local and Indigenous communities (such as in Ilha do Bananal) with local weather conditions—while acknowledging that implementing intercultural burning calendars must navigate the complex legal, political, and institutional tensions surrounding traditional fire use and Indigenous land governance in Brazil; and (4) in establishing differentiated protection protocols for fire-sensitive ecosystems (such as forests and wetlands) adjacent to areas with high recurrence rates. In this way, fire mapping ceases to be merely a 

```
1 3
```

Arabian Journal of Geosciences          (2026) 19:213 

<mark>Page 15 of 17 213</mark> 

descriptive diagnosis and becomes a tool for adaptive, territorially oriented management aimed at conserving the Cerrado. 

**Supplementary Information** The online version contains supplementary material available at  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 2 5 1 7 - 0 2 6 - 1 2 6 2 1 - 1 . 

**Acknowledgments** This work was supported by the National Council for Scientific and Technological Development (CNPq) through a Research Productivity Fellowship awarded to Carlos Fabricio Assunção da Silva (Grant No. 304265/2026-8). 

**Author contributions Conceptualization** : Alex Mota dos Santos and Carlos Fabricio Assunção da Silva; **Methodology** : Alex Mota dos Santos; **Data curation** : Alex Mota dos Santos; **Formal analysis** : Alex Mota dos Santos and Carlos Fabricio Assunção da Silva; **Investigation** : Alex Mota dos Santos and Carlos Fabricio Assunção da Silva; **Writing – original draft** : Alex Mota dos Santos, Carlos Fabricio Assunção da Silva, Fabrizia Gioppo Nunes, Gisele Daiane Pinha and Clayton Alexandre do Amaral; **Supervision** : Carlos Fabricio Assunção da Silva; **Writing – review and editing** : Alex Mota dos Santos, Carlos Fabricio Assunção da Silva, Fabrizia Gioppo Nunes, Gisele Daiane Pinha and Clayton Alexandre do Amaral; **Supervision** : Carlos Fabricio Assunção da Silva; **Project administration** : Carlos Fabricio Assunção da Silva. 

**Funding** The authors received no specific funding for this work. 

**Data availability** Data sets generated during the current study are available from the corresponding author on reasonable request. 

### **Declarations** 

**Research involving human participants and/or animals** This study did not involve human participants, animals, or any intervention requiring ethical approval. 

**Informed consent** Not applicable. This study did not involve human participants. 

**Conflict of interest** The authors declare that they have no conflict of interest. 

##### **Clinical trial number** Not applicable. 

**Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit  h t t p : / / c r e a t i v e c o m m o n s . o r g / l i c e n s e s / b y / 4 . 0 / . 

## **References** 

Allouche FK (ed) (2026) Environmental remote sensing and GIS in MENA Region: GIS urban and rural applications geospatial 

technologies and risks. Springer Nature. pp. 1-10.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / 9 7 8 - 3 - 0 3 1 - 8 6 5 7 4 - 9 

Alvarado ST, Fornazari T, Cóstola A, Morellato LPC, Silva TSF (2017) Drivers of fire occurrence in a mountainous Brazilian cerrado savanna: Tracking long-term fire regimes using remote sensing. Ecol Indic 78:270–281. h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . e c o l i n d . 2 0 1 7 . 0 2 . 0 3 7 

Alves DB, Alvarado ST (2019) Variação espaço-temporal da ocorrência do fogo nos biomas brasileiros com base na análise de produtos de sensoriamento remoto. Geografia 44(2):321–345  h t t p s : / / d o i . o r g / 1 0 . 5 0 1 6 / g e o g r a fi  a . v 4 4 i 2 . 1 5 1 1 9 

Aragão MA, Fiedler NC, Ramalho AHC, Menezes RAS, da Silva ECG, Juvanhol RS, Lucas FMF (2023) Risk of forest fires occurrence on a transition island Amazon-Cerrado: Where to act? Ecol Manage 536:120858. https:/ /doi.or g/10.10 16/j. foreco.2023.120858 Argibay DS, Sparacino J, Espindola GM (2020) A long-term assessment of fire regimes in a Brazilian ecotone between seasonally dry tropical forests and savannah. Ecol Indic 113:106151.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . e c o l i n d . 2 0 2 0 . 1 0 6 1 5 1 

Arruda VLS, Alencar AAC, Carvalho Júnior OA, Ribeiro FF, Arruda FV, Conciani DE, Silva WV, Shimbo JZ (2024) Assessing four decades of fire behavior dynamics in the Cerrado biome (1985 to 2022). Fire Ecol 20(64).  h t t p s : / / d o i . o r g / 1 0 . 1 1 8 6 / s 4 2 4 0 8 - 0 2 4 - 0 0 2 9 8 - 4 Bezerra KF, Gomes HB, Nascimento JP, Baltaci H, Osman M, Silva MCL, Mariano GL (2025) Climate extremes and fire behavior in the Brazilian Cerrado: a multi-years assessment (2012–2023). Earth Syst Environ 1–17.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 4 1 7 4 8 - 0 2 5 - 0 0 8 0 9 - 6 

- Carvalho EV, Batista AC, Coelho MCB, Marques Neves CO, dos Santos GR, Giongo M (2017) Caracterização de áreas queimadas no Estado do Tocantins no ano de 2014. Floresta 47(3).  h t t p s : / / d o i . o r g / 1 0 . 5 3 8 0 / r f . v 4 7 i 1 . 5 0 3 5 3 

- Copernicus Climate Change Service (2023) ERA5 hourly data on single levels from 1940 to present [Data set]. Copernicus Clim Data Store (CDS). https:/ /doi.or g/10.24 381/c ds.adbb2d47 

- Costa LS, Sano EE, Ferreira ME, Munhoz CBR, Costa JVS, Rufino Alves Júnior L, da Cunha Bustamante MM (2023) Woody plant encroachment in a seasonal tropical savanna: lessons about classifiers and accuracy from UAV images. Remote Sensing 15(9):2342. https:/ /doi.or g/10.33 90/rs 15092342 

- Cruz Silva A, Veenendaal E, Van der Plas F, de Oliveira Júnior VD, Vale VS, Meira-Neto JAA (2025) Vegetation transition in the central Brazilian Cerrado is better explained by structure than tree composition differences. Plant Ecol 226(5):563–572.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 1 2 5 8 - 0 2 5 - 0 1 5 0 0 - 6 

- Daldegan GA, de Carvalho Júnior OA, Guimarães RF, Gomes RAT, de Figueiredo Ribeiro F, McManus C (2014) Spatial patterns of fire recurrence using remote sensing and GIS in the Brazilian savanna: Serra do Tombador Nature Reserve, Brazil. Remote Sens 6(10):9873–9894. https:/ /doi.or g/10.33 90/rs 6109873 

- Falleiro RM, Santana MT, Berni CR (2016) As contribuições do Manejo Integrado do Fogo para o controle dos incêndios florestais nas Terras Indígenas do Brasil. Biodiversidade brasileira 6(2):88–105. h t t p s : / / d o i . o r g / 1 0 . 3 7 0 0 2 / b i o d i v e r s i d a d e b r a s i l e i r a . v 6 i 2 . 6 5 5 

- Fanin T, Van Der Werf GR (2015) Relationships between burned area, forest cover loss, and land cover change in the Brazilian Amazon based on satellite data. Biogeosciences 12(20):6033–6043. https:/ /doi.or g/10.51 94/bg -12-6033-2015 

- Feitosa Junior FRF, dos Santos AM, Alvarado ST, da Silva CFA, Nunes FG (2024) Remote sensing applied to the study of fire in savannas: A literature review. Ecol Inf 79:102448.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . e c o i n f . 2 0 2 3 . 1 0 2 4 4 8 

- Fernandes HGP, Rodrigues TCS, Nogueira FDLD, Melo MHFD, Dalagnol R, Freire ATG, Silva-Junior CHL (2026) Land use and land cover dynamics and their association with fire in indigenous 

```
1 3
```

<mark>213 Page 16 of 17</mark> 

Arabian Journal of Geosciences          (2026) 19:213 

territories of Maranhão, Brazil (1985–2023). Land 15(1):132.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / l a n d 1 5 0 1 0 1 3 2 

- Freire Junior GB, Elias-Paiva A, Ribeiro DB, Araujo RF, Sudta C, de Araújo ES, Domingos FM (2025) Fostering biodiversity in neotropical savannahs: fire as a diversity driver for fruit-feeding butterfly assemblages in the Cerrado. Austral Ecol 50(3):e70053. https:/ /doi.or g/10.11 11/ae c.70053 

- Gomes L, Miranda HS, da Cunha Bustamante MM (2018) How can we advance the knowledge on the behavior and effects of fire in the Cerrado biome? Ecol Manage 417:281–290.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . f o r e c o . 2 0 1 8 . 0 2 . 0 3 2 

- Gonçalves J, Portela AP, Regos A, Sil Â, Marcos B, Alonso J, Honrado J (2025) Fostering post-fire research towards a more balanced wildfire science agenda to navigate global environmental change. Fire 8(2):51. https:/ /doi.or g/10.33 90/fi re8020051 

- Hijmans RJ, Bivand R, Forner K, Ooms J, Pebesma E, Sumner MD (2023) Package ‘terra’. https:/ /rspati al.gith ub.io /terra/. Accessed 5 Sep 2026. 

- Hoffmann TB, Arai E, Shimabukuro YE, Adami M (2025) Mapping burned areas in Cerrado protected areas (2000–2020): a comparative analysis of Landsat classification, Mapbiomas fire, and MCD64A1. In: 2025 Latin American GRSS & ISPRS Remote Sensing Conference (LAGIRS). IEEE, pp 1–7.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / L A G I R S 6 8 3 6 7 . 2 0 2 5 . 1 1 4 1 4 7 9 2 

- Instituto Nacional de Pesquisas Espaciais - INPE (2026) Portal do Monitoramento de Queimadas. h t t p s : / / t e r r a b r a s i l i s . d p i . i n p e . b r / q u e i m a d a s / p o r t a l / .  Accessed 5 Sep 2026 

- Ivo IO, Biudes MS, Vourlitis GL, Machado NG, Martim CC (2020) Effect of fires on biophysical parameters, energy balance and evapotranspiration in a protected area in the Brazilian Cerrado. Remote Sens Appl Soc Environ 19:100342.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . r s a s e . 2 0 2 0 . 1 0 0 3 4 2 

- Kreri S, Farhi N, Bennia A, Derdour A, Kébir LW, Alharbi KM, Arafat AA (2026) Remote sensing assessment of vegetation and moisture dynamics in semi-arid regions. Sci Rep.  h t t p s : / / d o i . o r g / 1 0 . 1 0 3 8 / s 4 1 5 9 8 - 0 2 6 - 3 7 7 8 1 - 8 

- Lenza E, Martins J, Abadia AC, Gonçalves LA, Nogueira DS, Maracahipes-Santos L, Colli GR (2024) Diversity patterns reveal the singularities of the savanna woody flora in the Cerrado-Amazonia transition. Biodivers Conserv 33(10):2791–2808.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 5 3 1 - 0 2 4 - 0 2 8 8 3 - 0 

- Leonel M (2000) O uso do fogo: o manejo indígena ea piromania da monocultura. Estudos Avançados 14(40):231–250.  h t t p s : / / d o i . o r g / 1 0 . 1 5 9 0 / S 0 1 0 3 - 4 0 1 4 2 0 0 0 0 0 0 3 0 0 0 1 9 

- Lewis K, de Barros V, Cure F, Davies MB, Furtado CA, Hill MN, Rowland TC L (2022) Mapping native and non-native vegetation in the Brazilian Cerrado using freely available satellite products. Sci Rep 12(1):1588. https:/ /doi.or g/10.10 38/s4 1598-022-05332-6 

- Luiz CHP, Steinke VA (2022) Recent environmental legislation in Brazil and the impact on Cerrado deforestation rates. Sustainability 14(13):8096. https:/ /doi.or g/10.33 90/su 14138096 

- MapBiomas (2026) Área queimada no Brasil cresce 79% em 2024 e supera os 30 milhões de hectares. h t t p s : / / b r a s i l . m a p b i o m a s . o r g / 2 0 2 5 / 0 1 / 2 2 / a r e a - q u e i m a d a - n o - b r a s i l - c r e s c e - 7 9 - e m - 2 0 2 4 - e - s u p e r a - o s - 3 0 - m i l h o e s - d e - h e c t a r e s / . Accessed 5 Sep 2026 

- MapBiomas (2025) MapBiomas Fogo. h t t p s : / / b r a s i l . m a p b i o m a s . o r g / m a p b i o m a s - f o g o / . Accessed 5 Sep 2026 

- Martins SFS, dos Santos AM, da Silva CFA, Rudke AP, Alvarado ST, da Silva Melo JL (2024) The drivers of fire in the Caatinga Biome in Brazil. Ecol Manage 572:122260.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . f o r e c o . 2 0 2 4 . 1 2 2 2 6 0 

- Martins SFS, dos Santos AM, da Silva CFA, Nunes FG, Arnhold A, Rudke AP, dos Santos Lisboa G (2026) Spatiotemporal dynamics of burned areas in the Caatinga Biome, Brazil: A GIS-based assessment. Appl Geomat 18(1):34.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 2 5 1 8 - 0 2 5 - 0 0 6 7 7 - 9 

- Masson-Delmotte V, Zhai P, Pirani A, Connors SL, Péan C, Berger S, Zhou B (2021) Climate Change 2021: The Physical Science Basis. Contribution of Working Group I to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change. Cambridge University Press, Cambridge, UK and New York, NY, USA. https:/ /doi.or g/10.10 17/97 81009157896 

- McLauchlan KK, Higuera PE, Miesel J, Rogers BM, Schweitzer J, Shuman JK, Watts AC (2020) Fire as a fundamental ecological process: Research advances and frontiers. J Ecol 108(5):2047– 2069. https:/ /doi.or g/10.11 11/13 65-2745.13403 

- Miranda HS, Sato MN, Netto WN, Aires FS (2009) Fires in the cerrado, the Brazilian savanna. In: Cochrane MA (ed.),Tropical fire ecology: climate change, land use, and ecosystem dynamics. Springer, Berlin, Heidelberg, pp 427–450 

- Murray AT, Rini D, Sweeney SS, Roberts DA, Moritz MA, Baik J, Zheng Z (2025) Geographic fire response standards emerging from human– environment interactions. Ann Am Assoc Geogr 115(9):2048–2070. h t t p s : / / d o i . o r g / 1 0 . 1 0 8 0 / 2 4 6 9 4 4 5 2 . 2 0 2 5 . 2 5 2 7 9 3 4 

- Navarro-Rosales F, Carniello MA, da Cruz WJA, de Campos Oliveira F, Zhang-Zheng H, de Oliveira Corrêa VL,de Andrade MLF, Malhi Y, Hector A, Menor IO (2025) The effect of fire on the carbon fluxes and productivity of Brazilian woodland savannas. Sci Total Environ 987:179626.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . s c i t o t e n v . 2 0 2 5 . 1 7 9 6 2 6 

- Oliveira U, Soares-Filho B, de Souza Costa WL, Gomes L, Bustamante M, Miranda H (2021) Modeling fuel loads dynamics and fire spread probability in the Brazilian Cerrado. Ecol Manage 482:118889. https:/ /doi.or g/10.10 16/j. foreco.2020.118889 

- Oliveira U, Soares-Filho B, Bustamante M, Gomes L, Ometto JP, Rajão R (2022) Determinants of fire impact in the Brazilian biomes. Front Glob Change 5:735017. h t t p s : / / d o i . o r g / 1 0 . 3 3 8 9 / f f g c . 2 0 2 2 . 7 3 5 0 1 7 

- Oliveira VA, Santos GG, Ker JC, Couto EG, Jacomine PK, Corrêa GR, Schaefer CE (2023) Soils of Cerrados, the Brazilian savannas. The Soils of Brazil. Springer, Cham, pp 129–173.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / 9 7 8 - 3 - 0 3 1 - 1 9 9 4 9 - 3 _ 5 

- Pausas JG, Lamont BB, Paula S, Appezzato-da-Glória B, Fidelis A (2018) Unearthing belowground bud banks in fire-prone ecosystems. New Phytol 217(4):1435–1448.  h t t p s : / / d o i . o r g / 1 0 . 1 1 1 1 / n p h . 1 4 9 8 2 

- Petrov M, Nikolaeva Z, Dimitrov AL (2023) Cyclical aspect of the complex factors of anthropogenic activity on the global ecosystem. Oxid Commun 46(2):509–518 

- Pivello VR (2011) The use of fire in the Cerrado and Amazonian rainforests of Brazil: Past and present. Fire Ecol 7(1):24–39.  h t t p s : / / d o i . o r g / 1 0 . 4 9 9 6 / fi  r e e c o l o g y . 0 7 0 1 0 2 4 

- Pivello VR, Fidelis A (2025) Introduction: Fire and the South American Ecosystems. Fire in the South American Ecosystems. Springer, Cham, pp 1–8. https:/ /doi.or g/10.10 07/97 8-3-031-89372-8_1 

- R Core Team (2021) R: A language and environment for statistical computing. R Foundation for Statistical Computing, Vienna, Austria. https://www.R-project.org/ 

- RAF (2025/2026) Relatório Anual do Fogo no Brasil – Coleção 5 de mapas de áreas queimadas do MapBiomas Fogo (1985 a 2025). MapBiomas, São Paulo, Brasil, p 82p.  h t t p s : / / d o i . o r g / 1 0 . 5 8 0 5 3 / M a p B i o m a s / 4 H Q A B O 

- Ribeiro JF, Walter BMB (2008) As principais fitofissionomias do bioma cerrado. In: Sano SM, Almeida SP, Ribeiro JF (eds) Cerrado: ecologia e flora. Embrapa Cerrados, Planaltina, pp 151–212. https:/ /www.al ice.cnp tia.e mbrapa.br/handle/doc/186922 

- Rodrigues CA, Zirondi HL, Fidelis A (2021) Fire frequency affects fire behavior in open savannas of the Cerrado. Ecol Manage 482:118850. https:/ /doi.or g/10.10 16/j. foreco.2020.118850 

- Rundel PW, Arroyo MT, Cowling RM, Keeley JE, Lamont BB, Pausas JG, Vargas P (2018) Fire and plant diversification in Mediterranean-climate regions. Front Plant Sci 9:370584.  h t t p s : / / d o i . o r g / 1 0 . 3 3 8 9 / f p l s . 2 0 1 8 . 0 0 8 5 1 

```
1 3
```

Arabian Journal of Geosciences          (2026) 19:213 

<mark>Page 17 of 17 213</mark> 

- Sabljić L, Bajić D, Marković SB, Adžić D, Spalevic v, Sestraș P, Lukić T (2026) Remote sensing and GIS assessment of drought dynamics in the Ukrina River Basin, Bosnia and Herzegovina. Atmosphere 17(2):124. https:/ /doi.or g/10.33 90/at mos17020124 

- De Sales F, Werner Z, de Souza Ribeiro JG (2023) Quantifying fireinduced surface climate changes in the savanna and rainforest biomes of Brazil. Fire 6(8):311.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / fi  r e 6 0 8 0 3 1 1 

- Sano EE, Rosa R, Brito JL, Ferreira LG (2010) Land cover mapping of the tropical savanna region in Brazil. Environ Monit Assess 166(1):113–124. https:/ /doi.or g/10.10 07/s1 0661-009-0988-4 

- Sano EE, Rodrigues AA, Martins ES, Bettiol GM, Bustamante MM, Bezerra AS, Bolfe EL (2019) Cerrado ecoregions: A spatial framework to assess and prioritize Brazilian savanna environmental diversity for conservation. J Environ Manage 232:818– 828. https:/ /doi.or g/10.10 16/j. jenvman.2018.11.108 

- Santana MMMD, Vasconcelos RND, Neto SVDC, Neto EM, Rocha WDJSADF (2025) Modeling plant diversity responses to fire recurrence in disjunct Amazonian savannas. Land 14(7):1455. https:/ /doi.or g/10.33 90/la nd14071455 

- Santos GL, Pereira MG, Delgado RC, Magistrali IC, da Silva CG, de Oliveira CMM, da Silva TP (2021) Degradation of the Brazilian Cerrado: Interactions with human disturbance and environmental variables. Ecol Manage 482:118875.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . f o r e c o . 2 0 2 0 . 1 1 8 8 7 5 

- Scogings PF (2023) Perspective: Monitoring global forests using only structural metrics–problems and solutions from a savanna viewpoint. Ecol Manage 546:121381.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . f o r e c o . 2 0 2 3 . 1 2 1 3 8 1 

- Segura-Garcia C, Alencar A, Arruda VL, Bauman D, Silva W, Conciani DE, Oliveras Menor I (2025) The fire regimes of the Cerrado and their changes through time. Philos Trans R Soc B Biol Sci 380(1924). https:/ /doi.or g/10.10 98/rs tb.2023.0460 

- Siddiqui N (2025) Dplyr and TidyR. Cultural Analytics in R: A Tidy Approach. Use R! Springer, Cham.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / 9 7 8 - 3 - 0 3 1 - 9 6 6 1 8 - 7 _ 3 

- Silva ACD, Juvanhol RS, Miranda JDR (2023) Variabilidade espaçotemporal de ocorrência e recorrência de fogo no Bioma Caatinga usando dados do sensor MODIS. Cienc Florest 33:e70195. https:/ /doi.or g/10.59 02/19 80509870195 

- Silva PS, Libonati R, Gonçalves LG, DaCamara CC (2025a) The climatic patterns that control regional fire activity in the Brazilian 

savanna. Agric Meteorol 374:110792.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . a g r f o r m e t . 2 0 2 5 . 1 1 0 7 9 2 

- Silva CFA, dos Santos AM, Rudke AP, Nunes FG, Alvarado ST (2025b) Insights from remote sensing for the study of deforestation drivers in savannas. J Nat Conserv 86:126918.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . j n c . 2 0 2 5 . 1 2 6 9 1 8 

- Simon MF, Dantas VL (2025) Fire as an Evolutionary Driver in South America. In: Fidelis A, Pivello VR (eds) Fire in the South American Ecosystems. Ecol. Stud, vol 250. Springer, Cham.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / 9 7 8 - 3 - 0 3 1 - 8 9 3 7 2 - 8 _ 2 

- Sousa AM, Castro FAML, Rodrigues RR (2026) Manejo integrado do fogo nas regiões da Ilha do Bananal e Araguaia (TO): planejamento de prevenção e combate a incêndios florestais. Humanit Inovacao 13(1):55–65. h t t p s : / / r e v i s t a . u n i t i n s . b r / i n d e x . p h p / h u m a n i d a d e s e i n o v a c a o / a r t i c l e / v i e w / 1 1 1 7 6 

- Spadoni GL, Moris JV, Segura-Garcia C, Pessoa AC, Jones MW, Machado MS, Menor IO (2025) Devegetation is a widespread driver of fire in the Brazilian Cerrado. J Environ Manage 385:125637. https:/ /doi.or g/10.10 16/j. jenvman.2025.125637 

- Toral AA (2004) Terras Indígenas e o Parque Nacional do Araguaia. In: Ricardo F (ed) (org) Terras Indígenas & Unidades de Conservação da natureza: o desafio das sobreposições. Instituto Socioambiental, São Paulo, pp 482–485. 

- Valente CR, Latrubesse EM, Ferreira LG (2013) Relationships among vegetation, geomorphology and hydrology in the Bananal Island tropical wetlands, Araguaia River basin, Central Brazil. J South Am Earth Sci 46:150–160.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . j s a m e s . 2 0 1 2 . 1 2 . 0 0 3 

- Verona LS, Zanne AE, Trumbore S, Bernardino PN, Alencar GM, Andreuccetti T, Oliveira RS (2026) Vast, overlooked peat, and organic soils in Brazil’s Cerrado: carbon storage, dynamics, and stability. New Phytol 250(5):2946–2965.  h t t p s : / / d o i . o r g / 1 0 . 1 1 1 1 / n p h . 7 1 0 2 7 

- Viegas LMD, Sales L, Hipólito J, Amorim C, de Pereira EJ, Ferreira P, Vale MM (2022) We’re building it up to burn it down: fire occurrence and fire-related climatic patterns in Brazilian biomes. PeerJ 10:e14276. https: //d oi. or g/10 .771 7 /peerj.14276 

**Publisher’s Note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

```
1 3
```


