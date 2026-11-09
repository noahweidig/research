---
title: 'Developing a FARSITE wildfire simulation framework for Romania: fuel model mapping and evaluation using historical wildfires'
authors:
- Samsodan, Catalin-Vasile
- Lorenț, Adrian
- Apostol, Bogdan
- Petrila, Marius
- Capalb, Florin
- Marcu, Cristiana
- Ionac, Nicoleta
year: '2026'
journal: Annals of Forest Research
doi: 10.15287/afr.2026.4628
tags:
- fire behavior
- fuels
- modeling
- wildfire
zotero_key: UBCEEJ2T
item_type: journalArticle
url: https://openalex.org/W7213455885
source_url: 'unpaywall: https://afrjournal.org/index.php/afr/article/download/4628/1378'
fulltext_status: fulltext
synced: '2026-11-09'
---

# Developing a FARSITE wildfire simulation framework for Romania: fuel model mapping and evaluation using historical wildfires

## Abstract

Wildfire simulation can support fire-risk assessment and management, but its application depends on the availability of consistent spatial information on fuels, topography, weather, and fuel moisture. This study developed and evaluated a FARSITE-based wildfire simulation framework for Romania, with particular emphasis on generating the spatial input datasets required for its application. A national fuel-model map was produced by integrating land-cover and canopy information and assigning standard fire-behaviour fuel models according to vegetation characteristics. The framework was evaluated through retrospective simulations of four historical wildfires in western and southwestern Romania. Simulated and observed fire perimeters were compared using complementary spatial agreement metrics, while rate of spread, fireline intensity, and flame length were analysed to characterize simulated fire behaviour. Spatial agreement varied among the four case studies, with Sørensen–Dice coefficients ranging from 0.660 to 0.879 and Cohen’s Kappa values from 0.436 to 0.687. The highest agreement was obtained for the Șvinița wildfire, whereas Ilia showed the lowest agreement and the greatest overprediction. Simulated fire behaviour also varied substantially among events and fuel types, with the highest spread rates, fireline intensities, and flame lengths generally associated with grass- and shrub-dominated fuels. Overall, the results indicate that the proposed framework provides a suitable basis for further FARSITE application and development in Romania under the fuel and environmental conditions represented by the evaluated fires. Further improvements should focus on local fuel characterization, more representative meteorological and topographic inputs, incorporation of information on firefighting operations, and evaluation using a broader range of historical wildfires.

## Full text

Ann. For. Res. 69(2): 1-26, 2026 https://doi.org/10.15287/afr2026.4628 

**ANNALS OF FOREST RESEARCH** www.afrjournal.org 

**Developing a FARSITE wildfire simulation framework for Romania: Fuel model mapping and evaluation using historical wildfires** 

**Cătălin Vasile Șamșodan**<sup>**1,2**</sup> **, Adrian Lorenț**<sup>**3**</sup> **<mark>,</mark> Bogdan Apostol**<sup>**3**</sup> **, Marius Petrila**<sup>**3**</sup> **, Florin Capalb**<sup>**3,4**</sup> **, Cristiana Marcu**<sup>**3**</sup> **, Nicoleta Ionac**<sup>**2**</sup> 

**Șamșodan C.V., Lorenț A., Apostol B., Petrila M., Capalb F., Marcu C., Ionac N.,** 2026. Developing a FARSITE wildfire simulation framework for Romania: Fuel model mapping and evaluation using historical wildfires. Ann. For. Res. 69(2): 1-26. 

**Abstract** Wildfire simulation can support fire-risk assessment and management, but its application depends on the availability of consistent spatial information on fuels, topography, weather, and fuel moisture. This study developed and evaluated a FARSITE-based wildfire simulation framework for Romania, with particular emphasis on generating the spatial input datasets required for its application. A national fuel-model map was produced by integrating land-cover and canopy information and assigning standard fire-behaviour fuel models according to vegetation characteristics. The framework was evaluated through retrospective simulations of four historical wildfires in western and southwestern Romania. Simulated and observed fire perimeters were compared using complementary spatial agreement metrics, while model-derived rate of spread, fireline intensity, and flame length were analysed descriptively to characterize simulated fire behaviour. Spatial agreement varied among the four case studies, with Sørensen– Dice coefficients ranging from 0.660 to 0.879 and Cohen’s Kappa values from 0.436 to 0.687. The highest agreement was obtained for the Șvinița wildfire, whereas Ilia showed the lowest agreement and the greatest overprediction. Modelled fire behaviour varied substantially among events and fuel types, with the highest simulated spread rates, fireline intensities, and flame lengths generally associated with grass- and shrub-dominated fuels. These fire-behaviour outputs were not independently validated and should therefore be interpreted as modelled patterns. Overall, the results indicate that the proposed framework provides a suitable basis for further FARSITE application and development in Romania under the fuel and environmental conditions represented by the evaluated fires. Further improvements should focus on local fuel characterization, more representative meteorological and topographic inputs, incorporation of information on firefighting operations, and evaluation using a broader range of historical wildfires. 

**Keywords:** FARSITE; wildfire simulation; fuel models; fire behaviour; fire spread; Romania. 

**Addresses:**<sup>**1**</sup> General Inspectorate for Emergency Situations, Bucharest, Romania| 2Faculty of Geography, University of Bucharest, Bucharest, Romania| 3National Institute for Research and Development in Forestry “Marin Drăcea”, Voluntari, Romania|<sup>4</sup> Faculty of Silviculture and Forest Engineering, “Transilvania” University of Braşov, Brașov, Romania. 

**Corresponding Author:** Adrian Lorenț (adrian.lorent@icas.ro). 

**Manuscript:** received August 21, 2026; revised September 10, 2026; accepted September 15, 2026. 

1 

Ann. For. Res. 69(2): 1-26, 2026 

Research article 

# **Introduction** 

Wildfires represent an increasing environmental and socio-economic concern across Europe, with recent decades characterized by increasing fire-weather danger and changes in the spatial patterns and severity of wildfire activity (Grünig et al. 2022; Jones et al. 2022). Although wildfire activity has historically been concentrated in the Mediterranean region, changing climatic conditions are increasing fire danger across other parts of Europe, broadening the geographical extent of areas exposed to wildfire risk (Galizia et al. 2023; Hetzer et al. 2024). Romania has historically experienced lower wildfire activity than Mediterranean Europe (Lorenț et al. 2025a), but recent extreme fire seasons have demonstrated the vulnerability of its forest and non-forest ecosystems, particularly under conditions of drought, strong winds, and complex topography (Sjostromet al. 2024; Lorenț et al. 2025b). These developments highlight the need for improved tools to understand fire propagation, assess wildfire risk, and support prevention and suppression activities. 

Wildfire simulation has become an important component of fire management and research, providing spatially explicit information on potential fire growth and behaviour that can support fuel treatment planning, fire suppression operations, and post-event analysis (Price & Germino 2022; Alipour et al. 2023). Among the available fire spread models, the Fire Area Simulator (FARSITE) is one of the most widely used. Originally developed for U.S. ecosystems, FARSITE integrates surface and crown fire behaviour models with spatial information on fuels and topography and temporally varying weather conditions to simulate two-dimensional fire growth (Finney 1998). Its application has subsequently expanded beyond North America, including Mediterranean and other European environments, and numerous studies have evaluated its ability to reproduce observed 

wildfire spread under different environmental conditions (Arca et al. 2007; Jahdi et al. 2015; Paugam et al. 2025). 

Fire propagation models have been extensively tested in countries with a longer tradition of wildfire modelling, including the United States and several Mediterranean countries, with increasing efforts toward their operational application. Nevertheless, realtime implementation remains constrained by uncertainties in fuel characterization, meteorological inputs, data availability, and computational and operational requirements (e.g., Martins et al. 2025). In Central and Eastern Europe, experience with spatially explicit wildfire simulation remains comparatively limited, although applications in countries of the region indicate increasing interest in adapting established modelling systems to local environmental conditions (Dobrinkova et al. 2014; Dobrinkova 2025; Kuhnen et al. 2026). 

A critical prerequisite for reliable fire behaviour simulation is the spatial representation of fuels. Standard fire behaviour fuel models (FBFMs), including the 13 fuel models described by Anderson (1982) and the 40 fuel models developed by Scott & Burgan (2005), provide generalized descriptions of fuelbed properties used by fire spread equations. However, transferring these fuel models to ecosystems outside their original development context can introduce substantial uncertainty, particularly in heterogeneous landscapes where vegetation structure and fuel characteristics differ from those represented by the original North American fuel models (Arca et al. 2007; Jahdi et al. 2015). Previous studies have therefore emphasized the importance of locally adapted fuel mapping and, where appropriate, calibration or development of fuel models using field observations and remote-sensing information (Keane et al. 2000; Krasnow et al. 2009; Salis et al. 2016). Advances in remote sensing have progressively expanded the possibilities for detailed fuel characterization, from high-resolution optical 

2 

Samsodan et al. 

Developing a FARSITE wildfire simulation framework for Romania.... 

imagery (Mallinis et al. 2008) and LiDARderived structural information (Mutlu et al. 2008) to recent multimodal approaches integrating optical, radar, and LiDAR data (Alipour et al. 2023). 

This issue is particularly relevant in Europe, where vegetation, land-use patterns, and fire regimes vary considerably across regions. While most wildfire research and operational development have historically concentrated on the Mediterranean region, recent initiatives have sought to provide harmonized fuel information at the European scale. One important development is the European fuel classification and mapping framework produced within the FirEUrisk project, which identifies 85 fuel types through a hierarchical classification system and provides correspondence with standard Scott and Burgan fire behaviour fuel models (Aragoneses et al. 2023). Such datasets provide an important basis for transferring established fire behaviour modelling approaches to European environments, but their applicability at the scale of individual wildfire events still requires evaluation against observed fire behaviour and locally available spatial data. 

Romania has experienced substantial wildfire activity in recent decades, with forest fires occurring predominantly in hilly areas and in the southern and south-eastern lowlands, where forests frequently border agricultural land, pastures, and hayfields. Under these conditions, fires often spread from dry herbaceous vegetation and agricultural residues into neighbouring forests (Lorenț et al. 2025b). Unlike the predominantly summer fire regime of Mediterranean Europe, fire occurrence in Romania generally peaks in spring, particularly in March and April, following snowmelt and during the rapid drying of dead herbaceous vegetation, with a secondary period of increased activity during summer and early autumn (Lorenț et al. 2025a). Ignitions are overwhelmingly anthropogenic, and most forest fires develop as surface fires, whereas crown fires occur much 

less frequently. 

Recent severe fire seasons illustrate the increasing relevance of wildfire risk in Romania. In 2022, 1,021 forest fires affected approximately 13,153 ha, representing one of the most severe fire seasons in recent decades (San-Miguel-Ayanz et al. 2023). In 2024, 728 forest fires affected approximately 10,360 ha, substantially exceeding the 2014–2023 annual averages of 363 fires and 2,982 ha burned (Sedano et al. 2025). These recent events highlight the need for improved approaches to wildfire prevention, risk assessment, and firespread analysis under Romanian environmental conditions. 

In Romania, despite the recent increase in interest in wildfire risk assessment and management, the application of spatially explicit fire spread models remains largely unexplored and FARSITE has, to our knowledge, not yet been systematically evaluated against observed wildfire events in Romania. Important constraints include the absence of standardized national fuel maps specifically designed for fire behaviour modelling, limited availability of meteorological observations at appropriate spatial and temporal resolutions, and limited integration of fire behaviour modelling into operational wildfire management. Consequently, the extent to which established modelling systems such as FARSITE can reproduce fire spread under Romanian environmental conditions remains uncertain. Against this background, the present study develops and tests a methodological framework for wildfire spread and behaviour simulation using FARSITE, adapted to Romanian environmental conditions and available geospatial datasets. The proposed workflow integrates satellite-derived landcover information, European fuel classification data, canopy fuel characteristics, topographic information, and meteorological observations to generate the spatial and temporal inputs required by the model. The approach is designed to be transferable between wildfire events and to facilitate subsequent model 

3 

Ann. For. Res. 69(2): 1-26, 2026 

Research article 

evaluation and calibration under contrasting environmental conditions. 

lowest values at high elevations in the Carpathians. Annual precipitation is similarly heterogeneous, exceeding 1,400 mm in parts of the southern and western Carpathians, while values below 450 mm occur along the Black Sea coast, in parts of the Danube floodplain and in some intra-Carpathian depressions (Gâștescu et al. 1975). 

The methodology is applied to four forest wildfires that occurred during 2024 and 2025 in Hunedoara and Mehedinți Counties, representing contrasting fire environments in western and south-western Romania. Simulated fire growth is compared with observed fire perimeters to quantify spatial agreement, while simulated fire behaviour characteristics are analysed to assess differences among events and identify potential sources of uncertainty. The specific objectives of the study are: (i) to develop a consistent and transferable workflow for generating FARSITE input datasets under Romanian conditions; (ii) to evaluate the ability of FARSITE to reproduce the observed spatial extent and propagation patterns of four documented wildfires; (iii) to characterize and compare simulated fire behaviour among the selected events; and (iv) to assess the applicability of the proposed workflow and identify the main sources of uncertainty and opportunities for further improvement. 

Forests cover approximately 7.05 million ha, representing about 29.6% of Romania's territory. Beech ( _Fagus sylvatica_ L.) accounts for 35.8% of the forest area. Coniferous forests, predominantly composed of _Picea abies_ L., H. Karst., _Abies alba_ Mill. and several _Pinus_ species, account for 25.2%, while oak forests ( _Quercus robur_ L. _, Quercus petraea_ (Matt.) Liebl., _Quercus cerris_ L., _Quercus frainetto_ Ten., _Quercus pubescens_ Willd. and _Quercus pedunculiflora_ K. Koch) represent 18.1%. Other hardwood broadleaved forests, including species such as _Carpinus betulus_ L., Fr _axinus excelsior_ L. and _Acer_ spp., account for 16.4%, while softwood broadleaved forests, including _Tilia cordata_ Mill. _, Tilia tomentosa_ Moench, _Populus_ spp. and _Salix_ spp., represent 4.5%. Forest distribution is strongly controlled by topography, with approximately 58.2% of the forest area located in mountain regions, 34.6% in hilly terrain and 7.2% in lowland areas (National Forest Inventory 2026). 

# **Material and methods** 

## **Study area and case-study wildfires** 

Romania is located in Central and Eastern Europe, with the Carpathian Mountains forming a natural arc across the country. The climate is predominantly temperate continental, with considerable regional variation: western Romania is generally more humid, the southwest is influenced by sub-Mediterranean conditions, while stronger continental characteristics are evident in the south and east. Mean annual temperature varies substantially with altitude and relief, with the highest values (above 11 °C) occurring in the southern lowlands, Dobruja and the Danube Delta, and the **Figure 1** 

**Figure 1** Location of the four wildfire case studies in Romania. 

4 

Developing a FARSITE wildfire simulation framework for Romania.... 

Samsodan et al. 

Four forest wildfires that occurred in Romania during the 2024 and 2025 fire seasons were selected as case studies (Figure 1). The selected fires represent contrasting topographic settings, vegetation characteristics and meteorological conditions, allowing the performance of the FARSITE simulator to be evaluated under different wildfire scenarios. The main characteristics of the case studies are summarized in Table 1, while detailed descriptions are provided below. For the Ilia and Baia de Criș wildfires, the observed burned perimeters were obtained from the European Forest Fire Information System (EFFIS) and subsequently verified against Sentinel-2 imagery. For the Dobra and Șvinița wildfires, the observed perimeters were delineated directly from cloud-free Sentinel-2 images acquired during the fire events, as described in Section 2.7. The ignition locations used in the 

simulations were reconstructed through expert interpretation by integrating information from official incident reports, satellite-derived thermal anomalies and the spatial configuration of the observed burned perimeters in order to identify the most plausible ignition point for each wildfire. The observed fire perimeters and reconstructed ignition locations for the four case studies are shown in Figure 2. 

Information on wildfire location and occurrence dates was obtained from official intervention records provided by the Hunedoara County Inspectorate for Emergency Situations (ISU Hunedoara) for the three fires in Hunedoara County and by the General Inspectorate for Emergency Situations (IGSU) for the Șvinița fire. Vegetation composition and stand characteristics were derived from the corresponding forest management plans, which were also used, together with Google Earth imagery, to characterize the local topographic setting. Google Earth was additionally used to determine the elevation of the reconstructed ignition locations. Meteorological data were obtained from Visual Crossing, as described in Section Weather data. 

## **Dobra** 

**Figure 2** Detailed maps of the four wildfire case studies showing the observed fire perimeters and reconstructed ignition points: (a) Dobra, (b) Șvinița, (c) Ilia, and (d) Baia de Criș. 

The Dobra wildfire occurred between 28 October and 3 November 2024 in the Poiana Ruscă Mountains, Hunedoara County, Romania, within the administrative territory of Dobra, in a relatively remote forested area. The nearest settlement was the village of Bujoru, located approximately 2 km north of the fire. The entire wildfire affected approximately 225 ha. For the purpose 

5 

Ann. For. Res. 69(2): 1-26, 2026 

Research article 

of fire spread simulation, only the initial fire development was considered, from ignition on 28 October 2024 at 09:00 to 29 October 2024 at 10:00, corresponding to the first cloud-free Sentinel-2 acquisition from which the observed fire extent could be delineated. At that time, the fire had affected approximately 62 ha. 

According to the forest management plans of U.P. I Stăncești, Dobra Forest District (INCDS 2017a), the affected landscape is almost entirely covered by deciduous forest, dominated by sessile oak ( _Q. petraea_ and Turkey oak ( _Q. cerris_ ), with smaller proportions of European beech ( _F. sylvatica_ ) and European hornbeam ( _C. betulus_ ). The forest stands were approximately 90–110 years old. The terrain was dominated by a single steep hillslope with predominantly south and southwest-facing aspects and slopes generally ranging between 30° and 40°. The wildfire was classified as a surface fire. During the simulated period, air temperature ranged from 7.9 to 22.7 °C (mean 14.1 °C), while relative humidity varied between 44.5 and 98.7% (mean 79.1%). Wind conditions were generally weak, with an average speed of 3.7 km h⁻¹ and only two hourly observations exceeding 10 km h⁻¹, although maximum gusts reached 32.8 km h⁻¹. Under these conditions, wildfire spread was primarily influenced by topography, with the steep hillslope exerting a stronger control on fire propagation than wind. 

## **Svinița** 

The Șvinița wildfire occurred between 1 and 12 November 2024 in the Almăj Mountains, Mehedinți County, Romania, within the administrative territory of Șvinița, in a remote mountainous area located approximately 4 km north of the Danube River. The entire wildfire burned approximately 1,381 ha, making it the largest documented forest wildfire in Romania since the beginning of the national forest fire statistics in 1956. For the purpose of fire spread simulation, only the initial fire development was considered, from 1 November 2024 at 23:00 to 4 November 2024 at 10:00, corresponding to the first cloud-free Sentinel-2 acquisition used 6 

to delineate the observed fire perimeter. At that time, the burned area covered approximately 286.3 ha. According to the forest management plans of U.P. II Șvinița and U.P. III Baia Nouă, Orșova Forest District (INCDS 2019a, 2019b), the affected forests are dominated by deciduous forests, primarily European beech ( _F. sylvatica_ ) and sessile oak ( _Q petraea_ ), with Turkey oak ( _Q. cerris_ ), Hungarian oak ( _Q. frainetto_ ) and small proportions of black alder ( _Alnus glutinosa_ L. Gaertn.). Forest stands ranged from 75 to 170 years in age. The terrain consists of several hillslopes with predominantly south-, southeast- and eastfacing aspects, while north- and northeastfacing slopes occur in the northern part of the analysed perimeter. Slopes generally range between 15 and 33°. The southwestern boundary of the analysed perimeter coincides with a narrow valley containing a stream and a forest road, which acted as natural and anthropogenic barriers limiting fire spread in that direction. The wildfire was classified as a surface fire. 

During the simulated period, air temperature ranged from 0.6 to 18.7 °C (mean 7.7 °C), while relative humidity varied between 51.8 and 100% (mean 88.3%). Wind conditions were generally weak to moderate, with an average speed of 4.5 km h⁻¹ and seven hourly observations exceeding 10 km h⁻¹, although maximum gusts reached 58.3 km h⁻¹. Winds were predominantly west-northwesterly. Under these conditions, wildfire spread was influenced by both wind and topography, with wind becoming increasingly important during periods of stronger gusts. 

## **Ilia** 

The Ilia wildfire occurred on 9 and 10 March 2025 in the Lăpugiu Hills (Holdea), within the Poiana Ruscă Mountains, Hunedoara County, Romania, in the administrative territory of Ilia, between the villages of Săcămaș and Brânznic. The burned area covered approximately 197 ha. According to the forest management plan of U.P. II Fața Râului, Dobra Forest District 

Developing a FARSITE wildfire simulation framework for Romania.... 

Samsodan et al. 

(INCDS 2017b), the affected landscape is dominated by deciduous forests, interspersed with small grassland patches (approximately 6.5% of the study area). The ignition point was located at 45°54′14″ N, 22°39′25″ E, at an elevation of 320 m a.s.l., while the burned perimeter extended between 250 and 400 m a.s.l. The terrain consists of a complex 

system of hillslopes and shallow valleys, with average slopes of approximately 25% and predominantly shaded aspects (N, NE and NW). The wildfire was classified as a surface fire. 

During the wildfire event, air temperature ranged from −1.9 to 20.9 °C (mean 9.4 °C), while relative humidity varied between 14.9 

**Table 1.** Main characteristics of the wildfire case studies. 

|**Characteristi**c|**Dobra**|**Șvinița**|**Ilia**|**Baia de Criș**|
|---|---|---|---|---|
|County|Hunedoara|Mehedinți|Hunedoara|Hunedoara|
|Physiographic<br>region|Poiana Ruscă<br>Mountains|Almăj<br>Mountains|Lăpugiu Hills<br>(Holdea), Poiana<br>Ruscă Mountains|Brad Depression,<br>Bihor Mountains–<br>Gilău–Vlădeasa<br>orographic region|
|Ignition point|45°51′21″ N|44°31′02″ N|45°54′14″ N|46°11′52″ N,|
|(Lat., Long.)|22°37′23″ E|22°08′27″ E|22°39′25″ E|22°41′47″ E|
|Ignition elevation<br>(m a.s.l.)|525|425|320|340|
|Elevation range<br>of simulated<br>perimeter(m a.s.l.)|305–610|385–540|250–400|295–390|
|Fire period|28 Oct–3 Nov<br>2024|1–12 Nov 2024|9–10 Mar 2025|9–11 Mar 2025|
|Simulation period|28 Oct 2024<br>09:00 – 29 Oct<br>2024 10:00|1 Nov 2024<br>23:00 – 4 Nov<br>2024 10:00|9 Mar 2025 20:00 –<br>10 Mar 2025 23:00|9 Mar 2025 20:00 –<br>11 Mar 2025 16:00|
|Total burned area|225|1,381|197|188|
|(ha)|||||
|Burned area used<br>for simulation(ha)|62|286.3|197|188|
|Dominant<br>vegetation|Deciduous forest<br>(Sessile oak–<br>Turkey oak)|Deciduous forest<br>(Sessile oak–<br>European beech,<br>with Hungarian<br>oak, Turkey oak<br>and minor black<br>alder)|Deciduous forest<br>(European beech–<br>sessile oak)|Deciduous<br>forest (European<br>hornbeam–sessile<br>oak)|
|Fire type|Surface fire|Surface fire|Surface fire|Surface fire|
|Dominant fire<br>driver|Topography|Mixed (wind–<br>topography)|Topography|Mixed<br>(topography–wind)|
|Observed|Sentinel-2|Sentinel-2|EFFIS + Sentinel-2<br>i|EFFIS + Sentinel-2<br>i|
|perimeter source|delineation|delineation|verification|verification|



7 

Ann. For. Res. 69(2): 1-26, 2026 

Research article 

and 77.6% (mean 43.2%). Wind conditions were generally weak, with an average speed of approximately 3.5 km h⁻¹ and only three hourly observations exceeding 10 km h⁻¹, although maximum gusts reached 25.2 km h⁻¹. Under these conditions, the wildfire was primarily topographydriven, with the dissected terrain exerting a greater influence on fire spread than wind. 

## **Baia de Criș** 

The Baia de Criș wildfire occurred between 9 and 11 March 2025 in the Brad Depression, within the Bihor Mountains–Gilău–Vlădeasa orographic region, Hunedoara County, Romania, in the administrative territories of Baia de Criș and Tomești, approximately 1 km southeast of Rișca village. The wildfire burned approximately 188 ha, and the FARSITE simulation covered the entire fire duration, from 9 March 2025 at 20:00 to 11 March 2025 at 16:00. According to the forest management plan of U.P. II Brad, Brad Forest District (INCDS 2018), the burned area is dominated by deciduous forests, primarily European hornbeam ( _C. betulus_ ), sessile oak ( _Q. petraea_ ) and Turkey oak ( _Q. cerris_ ). Forest stands ranged from 30 to 100 years in age. The ignition point was located at 46°11′52″ N, 22°41′47″ E, on a southeast-facing hillslope at an elevation of 340 m a.s.l. The terrain is characterized by a broad ridge and its adjacent hillslopes, forming a moderately dissected landscape. Following ignition, the fire spread along the ridge crest and onto both its northeastern and southeastern flanks. Slopes generally range between 15 and 25°, while elevation within the analysed perimeter varies from 295 to 390 m a.s.l. The wildfire was classified as a surface fire. 

During the simulated period, air temperature ranged from −0.6 to 21.1 °C (mean 9.8 °C), while relative humidity varied between 15.8 and 74.4% (mean 50.5%). Wind conditions were generally weak, with an average speed of 7.0 km h⁻¹ and fourteen hourly observations exceeding 10 km h⁻¹, although maximum gusts reached 40.3 km h⁻¹. Winds were 

predominantly from the southeast (120°). Under these conditions, wildfire spread was influenced by both topography and wind, with terrain controlling the overall direction of propagation along the ridge, while wind likely contributed to local variations in fire behaviour. 

## **Generation of geospatial inputs for fire simulation** 

FARSITE (Fire Area Simulator) is a spatially and temporally explicit fire-growth simulation system that integrates several fire-behaviour models within a two-dimensional framework to simulate wildfire propagation across heterogeneous landscapes (Finney 1998). Fire growth is represented using a vector-based implementation of Huygens’ principle, in which the fire perimeter is defined by a series of vertices that propagate over successive time steps according to local fuel, topographic, and meteorological conditions. Surface-fire spread at each vertex is calculated using Rothermel’s semi-empirical fire-spread model (Rothermel 1972), with wind and slope influencing the rate and direction of propagation. The resulting one-dimensional fire-spread calculations are extended spatially through elliptical wavefront propagation, allowing the fire perimeter to evolve through space and time. In addition to surface-fire spread, FARSITE integrates models for crown-fire initiation and spread, spotting, fire acceleration, and fuel-moisture variation, thereby allowing different components of wildfire behaviour to be represented within the same simulation framework (Finney 1998). FARSITE simulations require a Landscape File (LCP) containing five mandatory spatial themes: elevation, slope, aspect, fuel model and canopy cover. The LCP format also allows the inclusion of three optional crown-fuel themes: canopy height (CH), canopy base height (CBH) and canopy bulk density (CBD). In the present study, all eight spatial themes were included in the landscape files generated for the four case-study areas. All spatial datasets were processed in the 

8 

Samsodan et al. 

Developing a FARSITE wildfire simulation framework for Romania.... 

Romanian national coordinate reference system (Stereo 1970, EPSG:3844) and aligned to a common 10 m raster grid to ensure spatial consistency among the input layers. 

## Fuel model map 

The surface fuel model map was developed using the Sentinel-2 Global Land Cover (S2GLC) 2017 product at 10 m spatial resolution (Malinowski et al. 2020) as the primary land-cover dataset. The S2GLC data covering Romania were mosaicked, clipped to the national boundary and reprojected to EPSG:3844. Land-cover classes were subsequently related to the hierarchical European fuel classification developed within the FirEUrisk project (Aragoneses et al. 2023), which provides correspondence between European fuel types and the standard fire behaviour fuel models of Scott and Burgan (2005). 

Forest classes were further differentiated according to canopy density using the Copernicus Tree Cover Density (TCD) 2021 product. Broadleaved deciduous and needleleaved evergreen forest pixels were separated into open (15–70% tree cover) and closed (≥70% tree cover) stands. This additional stratification was introduced to account for structural differences in surface fuel conditions associated with canopy openness. 

The initial fuel model map was subsequently refined using vector data from the national TopRO50 dataset, including roads, railways, canals and dikes at 1:50,000 scale (ANCPI 2026). These features were rasterized on the common 10 m grid and assigned as nonburnable areas. We explicitly incorporated them to represent linear features that may act as barriers to fire spread but may be omitted or misclassified in satellite-derived land-cover products because of their limited width or canopy obstruction. 

Finally, the resulting fuel classes were converted to the Scott and Burgan (2005) fire behaviour fuel model system using the correspondence established by Aragoneses 

et al. (2023), complemented by expert interpretation where necessary to account for Romanian vegetation and forest structural conditions. The resulting 10 m raster served as the surface fuel model layer in the FARSITE landscape files. 

## Topographic inputs 

Topographic variables—elevation, slope and aspect—were derived from the Shuttle Radar Topography Mission (SRTM v3, 1 arc-second, approximately 30 m spatial resolution) (Farr et al. 2007; NASA JPL 2013). SRTM tiles covering Romania were mosaicked, and slope and aspect were derived using GDAL terrain functions. The resulting topographic layers were resampled to the common 10 m grid to ensure exact spatial alignment with the other FARSITE landscape inputs. 

## Canopy fuels 

Canopy cover was derived from the Copernicus Tree Cover Density (TCD) 2021 dataset at 10 m spatial resolution. The dataset was aligned to the common 10 m reference grid and masked to forest classes, with values outside forested areas set to zero to ensure consistency with the fuel model map. 

Canopy height (CH) was obtained from the ETH Global Canopy Height 2020 dataset (Lang et al. 2023), a global 10 m canopy height product generated by integrating GEDI LiDAR and Sentinel-2 data using a deep-learning approach. Tiles covering the study areas were mosaicked and aligned to the common reference grid. Negative values were set to zero, while extreme values exceeding 70 m were truncated to 70 m to avoid unrealistic canopy heights under Romanian forest conditions. 

Canopy base height (CBH) and canopy bulk density (CBD) were derived from the panEuropean canopy fuels dataset of Kutchartt et al. (2025), available at 200 m spatial resolution. The original layers were resampled to the 10 m reference grid using nearestneighbour resampling. This operation ensured 

9 

Research article 

Ann. For. Res. 69(2): 1-26, 2026 

spatial compatibility with the other FARSITE inputs but did not introduce additional spatial information beyond the original 200 m resolution. Fine-scale variability was subsequently introduced using local TCD values and the fuel-type classification. CBD was adjusted according to local tree cover density using: 



<!-- Start of picture text -->
  CBD₁₀ = CBD₂₀₀ × (TCD/100)                             (Eq.1)<br><!-- End of picture text -->

where CBD₁₀ represents the adjusted canopy bulk density at 10 m, CBD₂₀₀ is the original value from the pan-European dataset, and TCD is the local tree cover density (%). 

CBH values were adjusted according to forest type, with lower values assigned to open stands and higher values to closed stands, and were constrained not to exceed canopy height minus 0.5 m. In non-forest areas, CH, CBH and CBD were set to zero. 

Consistency checks were performed to ensure spatial co-registration among the canopy layers and the fuel model map and compliance with basic physical constraints, including CBH ≤ CH and CBD ≥ 0. The resulting canopy cover, CH, CBH and CBD layers were subsequently incorporated into the FARSITE Landscape Files. 

The sources of data used to generate the input data for fire behaviour and propagation simulations are summarized in Table 2. 

Because the land-cover and canopy datasets used to derive the fuel and canopy inputs represent different reference years and predate the 2024–2025 wildfire events, their temporal mismatch with the conditions prevailing at the time of the fires was considered a potential source of uncertainty and is further addressed in the Discussion section. 

## **Forest structural changes: growth and heterogeneity** 

Dead fuel moisture values required for the FARSITE simulations were estimated using a simplified form of the McArthur Mark 5 (MK5) fuel moisture relationship reported by Noble et al. (1980). In the form applied here, fine dead fuel moisture content was estimated from air temperature and relative humidity according to: 





<!-- Start of picture text -->
(Eq.2)<br><!-- End of picture text -->

where FM is fine dead fuel moisture content (%), RH is relative humidity (%), and T is air temperature (°C). 

Hourly air temperature and relative humidity data were obtained for each wildfire event from the meteorological dataset described in Section Weather data. Initial 1-h dead fuel moisture was estimated from meteorological conditions during the periods considered most representative of active fire behaviour 

**Table 2.** Spatial datasets used to generate the FARSITE landscape inputs. 

|**Input data**|**Original**<br>**resolution,**<br>**referenceyear**|**Reference**|
|---|---|---|
|Land Cover Map of Europe (LCM) 2017|10 m, 2017|Malinowski et al. 2020|
|Tree Cover Density (TCD) 2018 - Present|10 m, 2021|European Environment Agency 2024|
|ETH Global Canopy Height 2020 v1<br>dataset|10 m, 2020|Lang et al. 2023|
|Canopy Base Height (CBH)|200 m, 2020|Kutchartt et al. 2025|
|Canopy Bulk Density (CBD)|200 m, 2020|Kutchartt et al. 2025|
|NASA Shuttle Radar Topography Mission<br>Global 1 arc second V003|30 m, 2013|Farr et al. 2007, NASA JPL 2013|
|TopRO50 topographic dataset|1:50,000, 2026|ANCPI 2026|



10 

Developing a FARSITE wildfire simulation framework for Romania.... 

Samsodan et al. 

for each event. These periods were identified from the documented timing of fire activity, available satellite active-fire detections and the corresponding meteorological conditions. 

Following the approach proposed by Hardison (2003) and applied by Jahdi et al. (2015), the calculated MK5 value was assigned to the 1-h dead fuel moisture class (0–0.6 cm particle diameter). The 10-h and 100-h classes correspond to progressively larger dead fuel particles, with diameters of 0.6–2.5 cm and 2.5–7.6 cm, respectively. Moisture content for these classes was subsequently derived by adding 2 and 4 percentage points, respectively, to the estimated 1-h value. The resulting 1-h, 10-h and 100-h dead fuel moisture values were used to initialize the FARSITE simulations. 

The 1000-h dead fuel moisture and live fuel moisture values were specified separately, as these parameters were not estimated using the MK5 relationship. In the absence of locally measured fuel moisture data, values were assigned based on expert judgement considering the season, vegetation characteristics and prevailing meteorological conditions. The 1000h dead fuel moisture was set to 16%, while live herbaceous and live woody fuel moisture were set to 60% and 90%, respectively. 

## **Weather data** 

Meteorological inputs were obtained from the Visual Crossing Weather platform (https:// www.visualcrossing.com/), providing hourly historical records of air temperature, relative humidity, precipitation, wind speed, wind direction, and cloud cover. For each wildfire event, the nearest available weather station to 

the reconstructed ignition point was selected. The selected weather stations, together with their distance from and elevation difference relative to the corresponding ignition points, are summarized in Table 3. 

The hourly records covered the complete simulation period for each event and were formatted to generate the time-dependent weather and wind input files required by FARSITE. Wind speed and direction were used as provided by the meteorological dataset, without additional wind-speed adjustment. Air temperature and relative humidity records were also used to estimate dead fuel moisture, as described in Section Fuel moisture parameterization. Summary statistics describing the meteorological conditions recorded at the selected weather stations during the simulated periods are presented in Table 4. 

## **Ignition location and burning-hour determination** 

The ignition locations used in the FARSITE simulations were reconstructed through expert interpretation, integrating information from official incident reports, satellitederived active-fire detections, and the spatial configuration of observed burned perimeters. These complementary sources were used to identify the most plausible ignition location for each wildfire rather than assigning ignition directly to the location of the first satellite detection. The resulting reconstructed ignition points were subsequently used as the starting locations for the FARSITE simulations. Satellite active-fire observations were also 

**Table 3.** Weather stations used for the FARSITE simulations and their spatial relationship to the reconstructed ignition points. 

|**Case study**|**Weather station**|**Station coordinates**<br>**Di**|**stance to ignition**<br>**(km)**|**Elevation**<br>**difference(m)**|
|---|---|---|---|---|
|Dobra|Deva|45.867°N, 22.900° E|21.5|319|
|Șvinița|Drobeta-Turnu<br>Severin|44.633° N, 22.633° E|41.0|344|
|Ilia|Deva|45.867° N, 22.900° E|21.5|114|
|Baia de Criș|Țebea|46.167° N, 22.726° E|4.1|68|



11 

Ann. For. Res. 69(2): 1-26, 2026 

Research article 

**Table 4.** Meteorological conditions during the simulated periods of the four case-study wildfires. 

|**Meteorological variable**|**Dobra**|**Șvinița**|**Ilia**|**Baia de Criș**|
|---|---|---|---|---|
|Air temperature (°C), mean<br>(min–max)|14.1<br>(7.9–22.7)|7.7<br>(0.6–18.7)|9.4<br>(−1.9–20.9)|9.8 (−0.6–21.1)|
|Relative humidity (%), mean<br>(min–max)|79.1<br>(44.5–98.7)|88.3<br>(51.8–100.0)|43.2 (14.9–77.6)|50.5 (15.8–74.4)|
|Wind speed (km h⁻¹), mean<br>(max)|3.7<br>(14.4)|4.5 (18.0)|3.5 (14.4)|7.0 (14.4)|
|Maximum windgust(km h⁻¹)|32.8|58.3|25.2|40.3|
|Prevailingwind direction|WNW|WNW|WNW|ESE|
|Totalprecipitation(mm)|0|0|0|0|
|Cloud cover(%), mean|55.1|47.3|51.8|66.4|



Note: Elevation difference represents the absolute difference between weather-station elevation and the elevation of the reconstructed ignition point. 

examined to assess the temporal persistence of fire activity and to support the definition of burning hours used in the simulations. for this purpose, active-fire detections from the Visible Infrared Imaging Radiometer Suite (VIIRS) and Moderate Resolution Imaging Spectroradiometer (MODIS) were obtained from NASA's Fire Information for Resource Management System (FIRMS), operated within the Land, Atmosphere Near real-time Capability for EOS (LANCE). VIIRS provides active-fire detections at approximately 375 m spatial resolution (Cao et al. 2013; Schroeder et al. 2014), while MODIS active-fire products provide complementary observations at approximately 1 km spatial resolution from the Terra and Aqua satellites (Justice et al. 2002; Giglio et al. 2003). 

For the Șvinița wildfire, satellite active-fire observations played a particularly important role in identifying the probable ignition area and assessing whether active burning persisted during nighttime hours. Thermal anomalies detected during nighttime overpasses indicated continued fire activity after sunset. Based on this evidence, burning was not restricted to daytime hours in the corresponding FARSITE simulation. For the other case studies, burninghour settings were established by integrating the available satellite observations with 

information from official incident reports and the documented timing of fire activity. Satellite active-fire detections were therefore used as supporting evidence for defining ignition locations and temporal constraints rather than as a continuous reconstruction of fire-front propagation. 

## **FARSITE simulation setup** 

FARSITE simulations were performed independently for the four case-study wildfires using the landscape files, fuel moisture parameters, meteorological inputs, and reconstructed ignition locations described in the previous sections. The start and end times of each simulation were defined according to the documented development of each wildfire and the availability of observed fire perimeters suitable for comparison, as summarized in Table 1. Burning periods were specified as described in Section Ignition location and burning-hour determination. 

Hourly wind speed and direction data were used as meteorological inputs to generate spatially distributed wind fields in FARSITE. Gridded winds were generated from the weather inputs using the WindNinja option integrated into the simulation environment, allowing the input wind conditions to be spatially modified according to terrain. No 

12 

Developing a FARSITE wildfire simulation framework for Romania.... 

Samsodan et al. , , 

additional wind-speed adjustment was applied to the original meteorological records. 

Common model settings were maintained across all four simulations. The perimeter resolution was set to 30 m, distance resolution to 10 m, and simulation time step to 30 min. Fire acceleration was enabled, while spotting was not simulated. No rate-of-spread adjustment factors or custom fuel models were applied. Foliar moisture content was set to 100%, and the Scott and Reinhardt (2001) method was selected for crown-fire calculations. 

For the Șvinița wildfire, additional spatial barriers were introduced to represent features known to have constrained fire propagation. In the southwestern sector, barriers corresponding to a stream and a forest road were included, as these features limited fire spread in that direction. An additional barrier was introduced in the southern sector based on operational information provided by firefighting authorities indicating the establishment of a control line. Without this constraint, the simulation produced substantial spread beyond the observed fire perimeter in this sector. No additional simulation barriers were introduced for the other three case studies. 

Simulation outputs were exported for subsequent spatial analysis in a GIS environment. The simulated final fire perimeters were used for comparison with the corresponding observed burned areas, while rate of spread (ROS), fireline intensity (FLI), and flame length (FL) were extracted to characterize and compare simulated fire behaviour among the four wildfire events. 

ROS, FLI, and FL were analysed as modelderived fire-behaviour outputs. Because independent field observations of these variables were not available for the four wildfire events, they were not included in the accuracy assessment and were not independently validated. 

No formal event-specific calibration of FARSITE was performed. In particular, rate-of-spread adjustment factors or custom fuel models were not used to optimize the simulations against the observed fire 

perimeters. The final simulations were subsequently evaluated by comparing their spatial extent with the observed fire perimeters using the metrics described in the next Section. **Accuracy assessment of wildfire spread simulations** 

Observed burned-area perimeters were used as reference data for the spatial evaluation of the FARSITE simulations. For the Baia de Criș and Ilia events, the reference perimeters were obtained from the European Forest Fire Information System (EFFIS), part of the Copernicus Emergency Management Service (CEMS) (San-Miguel-Ayanz et al. 2012). For the Șvinița and Dobra events, the simulations covered only part of the total fire duration and therefore could not be compared with the final EFFIS burned-area perimeters. For these events, reference perimeters were manually delineated from Copernicus Sentinel-2 MultiSpectral Instrument (MSI) Level-2A imagery (Drusch et al. 2012), accessed through the Copernicus Data Space Ecosystem (CDSE), and the satellite acquisition date and time were used as the end time of the corresponding FARSITE simulations. 

The accuracy of the simulated wildfire perimeters was evaluated using four complementary metrics previously applied to wildfire spread model evaluation: the Jaccard Index, Sørensen–Dice coefficient, Cohen's Kappa coefficient, and centroid size ratio (Sx) (Arca et al. 2007; Duff et al. 2012, 2016; Zhou et al. 2024). The Jaccard Index and Sørensen– Dice coefficient quantify the geometric overlap between the observed and simulated wildfire perimeters, Cohen's Kappa evaluates cell-bycell agreement while accounting for agreement expected by chance, and the centroid size ratio (Sx) quantifies differences in the overall size of the perimeter configurations independently of their spatial overlap. Additional measures of overprediction, underprediction, and relative area difference were used to characterize the direction and magnitude of spatial 

13 

Ann. For. Res. 69(2): 1-26, 2026 

Research article 

disagreement. 

The Jaccard Index (J) was used to quantify the proportion of the burned area shared by the observed and simulated wildfire perimeters relative to their combined extent. It was calculated as: 

where O and S represent the observed and (Eq.3) 

simulated wildfire perimeters, respectively. The numerator represents their area of intersection, while the denominator represents their area of union. The Jaccard Index ranges from 0 to 1, where 0 indicates no spatial overlap and 1 indicates perfect agreement between the two perimeters. 

The Sørensen–Dice coefficient (D) was also calculated as a complementary measure of spatial similarity: 





<!-- Start of picture text -->
(Eq.4)<br><!-- End of picture text -->

where O and S represent the areas of the observed and simulated wildfire perimeters, respectively. The Sørensen–Dice coefficient ranges from 0 to 1, with higher values indicating greater spatial agreement. Compared with the Jaccard Index, this coefficient places greater emphasis on the common burned area shared by the two perimeters. 

For the calculation of Cohen's Kappa coefficient, the observed and simulated wildfire perimeters were rasterized onto a common 10-m grid and compared on a cell-bycell basis within a common evaluation domain. The evaluation domain corresponded to the minimum bounding rectangle enclosing the union of the observed and simulated wildfire perimeters, expanded by one 10-m grid cell on each side. Pixels were classified as burned when their centre fell within the corresponding fire perimeter. From the resulting confusion matrix, the numbers of true positive (TP), true negative (TN), false positive (FP), and false 

negative (FN) cells were calculated. Cohen's Kappa coefficient (κ) was then calculated as: 





<!-- Start of picture text -->
(Eq.5)<br><!-- End of picture text -->

where Po is the observed agreement and Pe is the agreement expected by chance. The observed agreement was calculated as: 

where N is the total number of raster cells within the evaluation domain. The expected agreement was calculated as: 





<!-- Start of picture text -->
(Eq.6)<br><!-- End of picture text -->



<!-- Start of picture text -->
(Eq.7)<br><!-- End of picture text -->

The Cohen's Kappa coefficient theoretically ranges from −1 to 1, where a value of 1 indicates perfect agreement, 0 indicates agreement equivalent to random expectation, and negative values indicate agreement worse than expected by chance. The restricted evaluation domain was used to limit the influence of extensive areas jointly classified as unburned on the Kappa statistic. 

To complement the overlap-based metrics, differences in the overall size of the observed and simulated wildfire perimeters were quantified using the centroid size ratio (Sx), following the pseudo-landmark approach proposed by Duff et al. (2012). 

Because wildfire perimeters do not contain homologous landmarks, a set of pseudolandmarks was generated for each observed and simulated perimeter. First, the major chord was defined as the straight line connecting the ignition point to the perimeter vertex located at the maximum Euclidean distance from the ignition point. The perimeter coordinates were then reordered clockwise from the ignition point, and the major chord was used to divide the perimeter into left and right flanks. The major chord was subsequently divided into 200 equal segments, and a perpendicular transect was constructed through the midpoint of each 

14 

Developing a FARSITE wildfire simulation framework for Romania.... 

Samsodan et al. , , 

segment. The intersections of these transects with the left and right perimeter boundaries generated 400 pseudo-landmarks (200 on each flank), ensuring a one-to-one correspondence between pseudo-landmarks in the observed and simulated perimeter configurations. 

In situations where a perpendicular transect intersected the same perimeter flank more than once because of local boundary convolutions, the intersection closest to the major chord was retained. This ensured a unique pseudo-landmark pair for each transect and preserved a consistent correspondence between the observed and simulated perimeter configurations. The use of 200 transects (400 pseudo-landmarks) provided a dense representation of perimeter geometry while maintaining computational efficiency. 

The centroid of each pseudo-landmark configuration was calculated as: 





<!-- Start of picture text -->
(Eq.8)<br><!-- End of picture text -->

where xi represents the coordinates of the _i_ -th pseudo-landmark, x̄ is the centroid of the configuration, and (n) is the total number of pseudo-landmarks. 

Centroid size was then calculated as the square root of the sum of squared Euclidean distances of all pseudo-landmarks from the centroid: 





<!-- Start of picture text -->
(Eq.9)<br><!-- End of picture text -->

where (CS) represents the overall size of the pseudo-landmark configuration independently of its spatial position. 

The centroid size ratio (Sx) was computed as: 





<!-- Start of picture text -->
(Eq.10)<br><!-- End of picture text -->

where CSsim and CSobs are the centroid sizes of the simulated and observed wildfire perimeters, respectively. Values of Sx > 1 indicate that the simulated perimeter is larger than the observed perimeter, whereas values of Sx < 1 indicate that the simulated perimeter is smaller. A value of Sx = 1 represents identical overall perimeter size. 

For consistency with Duff et al. (2012), the natural logarithm of the centroid size ratio was also calculated as: 





<!-- Start of picture text -->
(Eq.11)<br><!-- End of picture text -->

Positive values of _ln(Sx)_ indicate overestimation of perimeter size by the simulation, whereas negative values indicate underestimation. A value of zero indicates identical centroid sizes. In the present study, only the size component of the method proposed by Duff et al. (2012) was used, as the objective was to quantify differences in the overall extent of simulated and observed wildfire perimeters rather than differences in perimeter shape. 

In addition to these four metrics, overprediction, underprediction, and relative area difference were calculated to characterize the direction and magnitude of spatial disagreement. Overprediction was defined as the simulated area falling outside the observed fire perimeter (S − O), whereas underprediction represented the observed area not reached by the simulation (O − S). Both were expressed as percentages of the observed burned area. Relative area difference was calculated as: 





<!-- Start of picture text -->
(Eq.12)<br><!-- End of picture text -->

where _AS_ and _AO_ are the simulated and observed burned areas, respectively. Positive values indicate an overall overestimation of burned area, whereas negative values indicate an overall underestimation. 

15 

Ann. For. Res. 69(2): 1-26, 2026 

Research article 

# **Results** 

## **Fuel model mapping** 

The workflow described in Section  Fuel model map resulted in a national 10 m fuel model map suitable for integration into FARSITE landscape files. The final correspondence applied in this study between the S2GLC landcover classes, the European fuel types defined by Aragoneses et al. (2023), and the Scott and Burgan (2005) fire behaviour fuel models is presented in Table 5. The correspondence was adapted to the vegetation and fuel 

characteristics represented by the input datasets and therefore differs from the original fuelmodel assignments proposed by Aragoneses et al. (2023). For forest vegetation, the S2GLC broadleaf and coniferous tree-cover classes were further differentiated using Tree Cover Density, resulting in separate open and closed broadleaf deciduous and needleleaf evergreen fuel types. This differentiation resulted in the assignment of SH4 (144) and TU5 (165) to open and closed broadleaf forests, respectively, and TU3 (163) and TL3 (183) to open and closed coniferous forests, respectively. Non- 

**Table 5.** Correspondence between S2GLC land-cover classes and fuel models used in the FARSITE simulation 

|**S2GLC land**<br>**cover class**|**European fuel type – Aragoneses et al.**<br>**(2023)**|**Scott & Burgan (2005) fuel model**|
|---|---|---|
|Artificial surfaces<br>and constructions|61 – Urban – Continuous fabric [≥80%]|Nonburnable (91)|
|Cultivated areas|41 – Cropland – Herbaceous|GR6 (106) – Moderate Load,<br>Humid Climate Grass(Dynamic)|
|Vineyards|42 – Cropland – Woody (shrub–tree)|GR6 (106) – Moderate Load,<br>Humid Climate Grass(Dynamic)|
|Broadleaf tree|1121 – Forest – Broadleaf – Deciduous<br>– Open[15–70%]|SH4 (144) – Low Load, Humid<br>Climate Timber-Shrub|
|cover|1122 – Forest – Broadleaf – Deciduous<br>– Closed[70–100%]|TU5 (165) – Very High Load, Dry<br>Climate Timber-Shrub|
|Coniferous tree<br>|1211 – Forest – Needleleaf – Evergreen<br>– Open [15–70%]|TU3 (163) – Moderate Load,<br>Humid Climate Timber-Grass-Shrub<br>(Dynamic)|
|cover|1212 – Forest – Needleleaf – Evergreen<br>– Closed[70–100%]|TL3 (183) – Moderate Load Conifer<br>Litter|
|Herbaceous<br>vegetation|32 – Grassland – Medium [0.3–0.7 m]|GR4 (104) – Moderate Load, Dry<br>Climate Grass(Dynamic)|
|Moors and<br>Heathland|21 – Shrubland – Low [0–0.5 m]|SH8 (148) – High Load, Humid<br>Climate Shrub|
|Marshes|53 – Wet and peat/semi-peat land –<br>Grassland|GR9 (109) – Very High Load,<br>Humid Climate Grass(Dynamic)|
|Peatbogs|53 – Wet and peat/semi-peat land –<br>Grassland|GR9 (109) – Very High Load,<br>Humid Climate Grass(Dynamic)|
|Natural material<br>surfaces|99 – NB9|Nonburnable (91)|
|Permanent snow<br>covered surfaces|92 – NB2|Nonburnable (91)|
|Water bodies|98 – NB8|Nonburnable(91)|



16 

Developing a FARSITE wildfire simulation framework for Romania.... 

Samsodan et al. 

vegetated land-cover classes were assigned to a common nonburnable class in the final FARSITE fuel model map. 



Within the four casestudy areas, the fuel-model composition differed substantially. The Dobra wildfire was dominated almost entirely by TU5 (165), corresponding to closed broadleaf deciduous forest, whereas the Șvinița fire encompassed mainly SH4 (144) and TU5 (165), representing open and closed broadleaf deciduous forest, respectively. In contrast, the Ilia and Baia de Criș fire areas included a larger proportion of grass fuels, particularly GR4 (104), together with forest fuel models. Smaller areas assigned to GR6 (106), GR9 (109), TL3 (183), and nonburnable classes occurred locally. 

**Figure 3** Comparison between observed and FARSITE simulated wildfire perimeters (perimeter resolution: 30 m; time step: 30 min) for the four case studies: (a) Dobra, (b) Șvinița, (c) Ilia, and (d) Baia de Criș. Simulation barriers used for the Șvinița case are also shown. 

among the four wildfire events. 

Șvinița showed the highest spatial agreement, with the highest Jaccard (0.784), Sørensen–Dice (0.879), and Cohen's Kappa (0.687) values. The centroid size ratio was also very close to unity (Sx = 1.009), indicating a close correspondence in overall perimeter size. Despite this high agreement, the simulation showed a net area underestimation of 13.24%, with underprediction (20.65%) exceeding overprediction (4.67%). 

## **Fire simulation accuracy** 

The spatial correspondence between the observed and simulated wildfire perimeters for the four case studies is shown in Figure 3, while the quantitative accuracy metrics are summarized in Table 6. Overall, the simulations reproduced the main spatial extent and configuration of the observed burned areas, although the degree of agreement varied 

**Table 6.** Accuracy metrics comparing observed and simulated wildfire perimeters. 

|**Fire**|**Jaccard**|**Sørensen–**<br>**Dice**|**Cohen’s**<br>**Kappa**|**Sx**|**Overprediction**<br>**(%)**|**Underpre-**<br>**diction (%)**|**Area**<br>**difference**<br>**(%)**|
|---|---|---|---|---|---|---|---|
|Baia de Criș|0.574|0.729|0.558|**1.246**|40.53|15.98|+21.17|
|Ilia|0.493|0.660|0.436|**1.302**|56.86|16.95|+34.13|
|Dobra|0.594|0.745|0.530|**0.895**|14.20|39.25|−17.99|
|Șvinița|**0.784**|**0.879**|**0.687**|**1.009**|**4.67**|20.65|−13.24|



17 

Ann. For. Res. 69(2): 1-26, 2026 

Research article 

Dobra and Baia de Criș showed intermediate levels of spatial agreement. Dobra reached Jaccard and Sørensen–Dice values of 0.594 and 0.745, respectively, with a Kappa coefficient of 0.530. Its Sx value of 0.895 was consistent with an overall tendency toward underestimation, also reflected by the negative area difference (−17.99%) and the predominance of underprediction (39.25%) over overprediction (14.20%). Baia de Criș showed similar overlap values (Jaccard = 0.574; Sørensen–Dice = 0.729), but a slightly higher Kappa coefficient (0.558). In contrast to Dobra, its Sx value of 1.246 and positive area difference (+21.17%) indicated an overall overestimation of the fire extent, with overprediction reaching 40.53%. 

## **Simulated fire behaviour Simulated fire behaviour** 

Simulated fire behaviour varied substantially among the four case studies, both in magnitude and spatial distribution. The spatial patterns of rate of spread (ROS), fireline intensity (FLI), and flame length (FL) are shown in Figure 4, while summary statistics for the fuel models occurring within each simulated burned area are presented in Table 7. 

Overall, the highest average ROS was simulated for Ilia (1.02 ± 0.93 m min⁻¹), followed by Dobra (0.67 ± 0.39 m min⁻¹), Baia de Criș (0.53 ± 0.54 m min⁻¹), and Șvinița (0.48 ± 0.68 m min⁻¹). A similar ranking was observed for FLI, with mean values of 276.45 ± 356.63 kW m⁻¹ at Ilia, 226.13 ± 141.98 kW m⁻¹ at Dobra, 117.07 ± 171.00 kW m⁻¹ at Baia de Criș, and 66.26 ± 78.27 kW m⁻¹ at Șvinița. Mean FL followed the same general pattern, ranging from 0.43 ± 0.21 m at Șvinița to 0.92 ± 0.37 m at Ilia, with intermediate values of 0.88 ± 0.26 m at Dobra and 0.60 ± 0.28 m at Baia de Criș. 

Ilia showed the lowest spatial agreement among the four simulations, with Jaccard, Sørensen–Dice, and Kappa values of 0.493, 0.660, and 0.436, respectively. It also exhibited the strongest tendency toward overestimation, with the highest Sx value (1.302), the largest positive area difference (+34.13%), and overprediction reaching 56.86% of the evaluated area, compared with 16.95% underprediction. 



Taken together, the results show that discrepancies between observed and simulated fire extent differed not only in magnitude but also in direction among the four events. The overlapbased metrics characterized the degree of spatial coincidence between the observed and simulated perimeters, whereas Sx and the overprediction, underprediction, and areadifference measures provided complementary information on the magnitude and direction of differences in simulated fire extent. 

**Figure 4** Spatial distribution of simulated fire behaviour metrics for the four casestudy wildfires: rate of spread (ROS), flame length (FL), and fireline intensity (FLI): (a) Dobra, (b) Șvinița, (c) Ilia, and (d) Baia de Criș. 

18 

Developing a FARSITE wildfire simulation framework for Romania.... 

Samsodan et al. 

**Table 7.** Burned area distribution and simulated fire behaviour metrics by fuel model for the four case studies. 

|Case|Fuel|Observed burned|Simulated burned|ROS (m min⁻¹)|<br>FLI (kW m⁻¹)|FL (m)|
|---|---|---|---|---|---|---|
|study|model|area (ha, %)|area (ha, %)|(mean ± SD)|(mean ± SD)|(mean ± SD)|
||165|56.16 (91.09%)|43.67 (86.56%)|0.65 ± 0.37|252.41 ± 148.20|0.95 ± 0.26|
||144|3.77 (6.12%)|6.78 (13.44%)|0.78 ± 0.52|56.87 ± 92.39|0.41 ± 0.26|
||106|1.20 (1.95%)|–|–|–|–|
|Dobra|104|0.26 (0.42%)|–|–|–|–|
||91|0.25 (0.41%)|–|–|–|–|
||109|0.01 (0.02%)|–|–|–|–|
||Total/<br>Average||50.45 (100%)|0.67 ± 0.39|226.13 ± 141.98|0.88 ± 0.26|
||144|165.12 (57.97%)|146.97 (58.76%)|0.34 ± 0.31|22.48 ± 49.38|0.27 ± 0.16|
||165|84.07 (29.51%)|78.32 (31.31%)|0.36 ± 0.18|131.03 ± 76.67|0.70 ± 0.21|
||104|35.04 (12.30%)|24.72 (9.88%)|1.73 ± 2.00|119.51 ± 163.74|0.56 ± 0.38|
|Șvinița|106|0.36 (0.13%)|0.02 (0.01%)|0.75 ± 0.18|98.36 ± 53.97|0.61 ± 0.17|
||91|0.15 (0.05%)|0.01 (0.00%)|0.82 ± 0.00|118.32 ± 0.00|0.70 ± 0.00|
||109|0.12 (0.04%)|0.08 (0.03%)|1.37 ± 1.50|630.47 ± 794.94|1.17 ± 0.88|
||Total/<br>Average||250.12 (100%)|0.48 ± 0.68|66.26 ± 78.27|0.43 ± 0.21|
||165|124.97 (63.56%)|157.84 (60.02%)|0.54 ± 0.47|222.56 ± 218.09|0.89 ± 0.26|
||144|37.32 (18.98%)|53.46 (20.33%)|0.78 ± 0.88|153.91 ± 323.83|0.67 ± 0.40|
||104|17.40 (8.85%)|23.49 (8.93%)|2.91 ± 1.75|355.44 ± 362.17|1.07 ± 0.41|
||106|15.25 (7.76%)|21.81 (8.29%)|2.38 ± 1.62|538.04 ± 618.69|1.25 ± 0.57|
|Ilia|109|1.61 (0.82%)|5.72 (2.18%)|3.21 ± 1.75|1479.27 ±<br>1179.37|2.00 ± 0.94|
||91|0.08 (0.04%)|0.59 (0.22%)|2.49 ± 2.04|1320.92 ±<br>1261.36|1.81 ± 1.01|
||Total/<br>Average||262.91 (100%)|1.02 ± 0.93|276.45 ± 356.63|0.92 ± 0.37|
||165|123.07 (65.66%)|124.74 (55.16%)|0.35 ± 0.16|140.50 ± 69.18|0.73 ± 0.18|
||144|43.00 (22.94%)|50.66 (22.40%)|0.40 ± 0.51|60.49 ± 190.66|0.39 ± 0.30|
||104|17.42 (9.29%)|43.78 (19.36%)|1.10 ± 0.99|94.29 ± 256.13|0.45 ± 0.39|
|Baia de|106|2.02 (1.08%)|5.23 (2.31%)|0.96 ± 0.89|177.55 ± 309.47|0.65 ± 0.48|
|Criș|91|1.40 (0.75%)|–|–|–|–|
||109|0.51 (0.27%)|1.73 (0.76%)|1.40 ± 1.39|476.90 ± 680.77|0.96 ± 0.85|
||183|0.02 (0.01%)|0.02 (0.01%)|0.51 ± 0.26|190.37 ± 91.11|0.84 ± 0.20|
||Total/<br>Average||226.16 (100%)|0.53 ± 0.54|117.07 ± 171.00|0.60 ± 0.28|



These differences occurred under contrasting meteorological and topographic conditions. 

Ilia, which showed the highest mean ROS, FLI, and FL, was characterized by the lowest 

19 

Ann. For. Res. 69(2): 1-26, 2026 

Research article 

relative humidity among the four events (mean 43.2%, minimum 14.9%) and predominantly topography-driven spread. Although mean wind speed was relatively low (3.5 km h⁻¹), the complex terrain produced pronounced spatial variability in the simulated fire behaviour. The simulated fire spread at Dobra was also predominantly influenced by topography, with the modelled propagation occurring over steep terrain, particularly along the main S–SWfacing slope, where slopes generally reached 30–40°. The event occurred under higher mean temperature (14.1 °C) and relative humidity (79.1%) than Ilia and exhibited the secondhighest mean fire-behaviour values. 

Șvinița presented a contrasting combination of meteorological conditions. Despite recording the strongest wind gusts among the four events (58.3 km h⁻¹), it had the highest mean relative humidity (88.3%) and the lowest mean ROS, FLI, and FL. The fire spread across complex mountainous terrain and was characterized by a combined wind– topography influence. Baia de Criș showed intermediate fire-behaviour values under mixed topographic and wind influence. The fire developed across moderately dissected terrain, with slopes generally between 15 and 25°, while mean wind speed (7.0 km h⁻¹) was the highest among the four events and maximum gusts reached 40.3 km h⁻¹. These contrasts show that the simulated fire-behaviour ranking did not correspond directly to wind speed alone, but occurred under different combinations of meteorological conditions, terrain configuration, and fuel composition. Differences were also pronounced among fuel models. The highest fire-behaviour values were generally associated with the grass fuel models. GR9 (109) produced mean ROS values ranging from 1.37 m min⁻¹ at Șvinița to 3.21 m min⁻¹ at Ilia. At Ilia, this fuel model also produced the highest mean FLI (1479.27 kW m⁻¹) and FL (2.00 m). GR4 (104) and GR6 (106) also showed comparatively high firebehaviour values where present; at Ilia, their 

mean ROS reached 2.91 and 2.38 m min⁻¹, respectively. 

In contrast, the forest fuel models SH4 (144) and TU5 (165) accounted for most of the simulated burned area but generally exhibited lower rates of spread than the grass fuel models. TU5 (165) alone represented 86.56% of the simulated burned area at Dobra, whereas SH4 (144) and TU5 (165) together accounted for approximately 90% at Șvinița and about 80% at Ilia and Baia de Criș. Thus, the highest simulated ROS, FLI, and FL values were concentrated mainly within comparatively limited areas occupied by grass fuel models, while most of the simulated burned area was associated with forest fuel models characterized by lower fire-behaviour values. The spatial patterns in Figure 4 further show substantial variability within individual fire perimeters, including within areas assigned to the same fuel model. This spatial heterogeneity reflects the combined inputs used by FARSITE, in which fuel properties interact with terrain and temporally varying meteorological conditions to produce spatially variable fire behaviour. 

# **Discussion** 

The results demonstrate that the proposed FARSITE-based simulation workflow can reproduce the general spatial development of forest wildfires within the range of fuel and environmental conditions represented by the four Romanian case studies. The simulations showed variable levels of agreement with the observed fire perimeters, indicating that model performance depended on the specific characteristics of each event. This variability is expected in retrospective wildfire reconstruction, where fire spread results from the interaction among fuel characteristics, terrain, meteorological conditions, and eventspecific constraints. 

The spatial agreement obtained in the four case studies varied substantially, with Sørensen–Dice coefficients ranging from 

20 

Developing a FARSITE wildfire simulation framework for Romania.... 

Samsodan et al. 

0.660 to 0.879 and Cohen’s Kappa values from 0.436 to 0.687. Șvinița showed the strongest agreement across the validation metrics, whereas Ilia produced the lowest overlap and the greatest overprediction. Comparable variability has been reported in previous retrospective FARSITE applications. Jahdi et al. (2015), in a four-fire calibration study in northern Iranian forests, reported Sørensen coefficients of 0.69–0.86 and Kappa values of 0.68–0.82 for their best-performing simulations. Their results were obtained after testing alternative standard fuel-model assignments against observed fire perimeters, highlighting the importance of local fuelmodel calibration when FARSITE is applied under environmental conditions different from those for which the underlying fuel models were originally developed. 

The differences among the individual validation metrics also illustrate the importance of evaluating fire simulations using complementary measures rather than burned area alone. Jaccard and Sørensen–Dice quantify spatial overlap, Kappa additionally accounts for agreement expected by chance, whereas Sx describes differences in overall perimeter size. Separate overprediction and underprediction measures further indicate the direction of spatial error. Similar multimetric approaches have been used in previous fire-spread evaluations (Price & Germino, 2022; Zhou et al. 2024). Zhou et al. (2024) further demonstrated that relatively high overlap scores can occasionally result from geometrically unrealistic simulations, reinforcing the need to interpret numerical metrics together with the spatial configuration of observed and simulated perimeters. Differences in both simulated fire behaviour and spatial agreement among the four cases are likely related to the combined influence of fuel representation, topography, and meteorological forcing. Previous sensitivity analyses have shown that uncertainty in wind speed and direction, ignition location, and fuel-model assignment can substantially affect simulated fire spread, although their relative importance 

varies among individual fires (Benali et al. 2017). This case dependency is also consistent with Zhou et al. (2024), who showed that the influence of individual landscape inputs depends strongly on local fire and terrain conditions. Wind deserves particular attention because FARSITE spread trajectories respond strongly to wind speed and direction, while observations from a single weather station cannot fully represent local airflow and its modification by complex terrain. 

Differences among fuel models were also apparent in the simulated fire-behaviour outputs. However, because independent observations of ROS, FLI, and flame length were not available, these differences should be interpreted as modelled patterns rather than as validated differences in actual fire behaviour. Within the simulations, the highest ROS, FLI, and flame-length values were generally associated with the less extensive grass- and shrub-dominated fuel models, whereas timber litter and timber–shrub models occupied most of the burned area. This indicates that, within the simulations, the spatial extent of a fuel model does not necessarily correspond to its contribution to the highest modelled firebehaviour values. A comparable dependence of simulated fire behaviour on fuel type was reported by Jahdi et al. (2015), who found higher spread rates and fire intensity in grassand shrub-dominated fuels and lower values in compact litter and forest-understory fuels. Sensitivity analyses have further shown that parameters such as fine-fuel loading, fuel-bed depth, and live-fuel loading can strongly influence FARSITE predictions, with changes in ROS affecting other fire-behaviour outputs (Cai et al. 2019). Price and Germino (2022) similarly demonstrated that improved representation of fuels can substantially alter both simulated fire spread and associated firebehaviour characteristics. 

Several limitations are primarily associated with the availability and spatial representativeness of input data. The national fuel-model map was derived from remotely sensed land-cover and canopy information 

21 

Ann. For. Res. 69(2): 1-26, 2026 

Research article 

and correspondence with standard Scott and Burgan fuel models rather than from fieldcalibrated fuel inventories. Consequently, local variations in fuel load, depth, and understory characteristics could not be explicitly represented. Standard fuel-model parameters may require local calibration against observed fires, as demonstrated in previous FARSITE sensitivity and calibration studies (Jahdi et al. 2015; Benali et al. 2017; Cai et al. 2019). Nevertheless, the present approach provides a consistent framework for generating spatially explicit fuel inputs at national scale in the absence of a dedicated field-calibrated fuelmodel dataset. 

An additional source of uncertainty is the temporal inconsistency among the datasets used to construct the landscape inputs and the dates of the simulated wildfires. The main land-cover dataset (S2GLC) represents conditions in 2017, while tree cover density and canopy height represent 2021 and 2020 conditions, respectively, whereas the analysed fires occurred in 2024–2025. Consequently, the resulting fuel and canopy layers may not fully represent vegetation conditions at the time of each wildfire. 

Changes occurring during this interval, including natural or anthropogenic disturbances, vegetation development, changes in canopy structure, or land-cover transitions, could result in local discrepancies between the mapped fuel characteristics and those actually present during the fires. This limitation is particularly relevant for the fuelmodel layer because fuel-model assignment was primarily derived from the 2017 landcover classification. Although the resulting landscape inputs provide a spatially consistent basis for applying the same workflow to all four case studies, their temporal mismatch with the wildfire dates represents an additional source of uncertainty in the simulated fire spread and fire-behaviour outputs. Future applications would therefore benefit from fuel and canopy datasets representing conditions as close as possible to the date of the simulated fire. 

Meteorological inputs were obtained from the nearest available weather stations and may not fully capture conditions within the fire areas, particularly in complex terrain. This is especially relevant for wind speed and direction, which strongly influence simulated fire spread and may vary considerably over short distances as a result of local topography. Fuel moisture was also estimated from meteorological observations rather than measured in situ. Similar limitations related to weather-station representativeness and the availability of high-resolution wind information have been identified in previous FARSITE applications (Jahdi et al. 2015; Benali et al. 2017). 

Topographic inputs represent another potential source of uncertainty. Elevation, slope, and aspect were derived from SRTM data, which do not represent a true bareearth terrain surface and have limited ability to capture fine-scale terrain features. This may be particularly relevant in steep and heterogeneous terrain, where local variations in slope and aspect influence fire propagation. Higher-resolution bare-earth terrain data, particularly LiDAR-derived DTMs, could therefore improve the representation of local topography in future applications. More generally, the spatial resolution of landscape inputs can affect the representation of finescale features relevant to fire spread; Hodges & Lattimer (2019), for example, showed that narrow non-burnable features such as roads and rivers may be lost when landscape data are represented at coarser resolution. 

Fire-suppression activities were not explicitly represented, although a known control line was included as a spatial barrier in the Șvinița simulation. Consequently, part of the discrepancy between simulated and observed perimeters may reflect suppression effects rather than model error alone. This issue has also been reported in previous retrospective FARSITE applications. In the reconstruction of the 2022 Razdel fire in Bulgaria, Dobrinkova (2025) found that simulated spread departed from the observed 

22 

Developing a FARSITE wildfire simulation framework for Romania.... 

Samsodan et al. 

fire development particularly in areas affected by suppression activities and emphasized the difficulty of reproducing such interventions in retrospective simulations. Similar limitations have been acknowledged in other FARSITE studies in which suppression activities could not be explicitly represented. 

Finally, the four case studies represent only a subset of Romanian fuel and ecosystem conditions. All were surface fires and were predominantly associated with broadleaf forest environments. Despite screening recent wildfire records, no sufficiently documented representative conifer-dominated wildfire was identified for reconstruction. Consequently, the fuel-model assignments developed for coniferous forests remain untested in the present study. The distinction between model evaluation and calibration is important when interpreting the present results. The spatial metrics reported here quantify the performance of the final simulation setup against the observed fire perimeters and therefore represent model evaluation. No formal eventspecific calibration was conducted, such as systematic optimization of rate-of-spread adjustment factors or development of custom fuel models against the observed fires. The current results should therefore be regarded as an initial evaluation of the proposed workflow rather than a comprehensive calibration for all Romanian forest types. Expanding the database of reconstructed historical fires across a broader range of vegetation, terrain, and meteorological conditions would provide the basis for progressive local calibration of fuelmodel assignments and FARSITE parameters. 

# **Conclusions** 

This study developed and tested a FARSITEbased workflow for wildfire simulation in Romania, integrating spatially consistent fuel, topographic, canopy, meteorological, and fuel-moisture inputs. Application to four historical wildfires showed that the workflow reproduced the observed fire perimeters with variable levels of spatial agreement among the 

case studies. The simulations also revealed substantial differences in fire behaviour among events and fuel models, with the highest spread rates, fireline intensities, and flame lengths generally associated with the less extensive grass- and shrub-dominated fuels rather than with the dominant timber litter and timber– shrub fuels. 

The results support the applicability of the proposed workflow under the fuel and environmental conditions represented by the four case studies, while also identifying aspects requiring further improvement. More representative fuel, meteorological, and topographic inputs could improve fire-spread reconstruction. Future applications could also incorporate information on firefighting operations, where such data are available, to better account for their influence on observed fire development. Because the evaluated events were surface fires occurring predominantly in broadleaf forest environments, the present study represents an initial evaluation rather than a comprehensive assessment across Romanian forest ecosystems. Further testing with additional historical wildfires, particularly in conifer-dominated forests and under a broader range of environmental and fireweather conditions, would allow progressive calibration and evaluation of the workflow 

# **Conflict of interest** 

The authors declare no financial or personal interests could influence the work presented in this paper. 

## **Acknowledgements** 

This research was made possible through the funding provided by the Romanian Ministry of Research, Innovation and Digitalization, FORCLIMSOC Nucleu Programme (Contract 12N/2023), project PN 23090204. This work was supported by a grant of the Ministry of Education and Research, CCCDI - UEFISCDI, project number PN-IV-P6-6.1CoEx-2024-0102, within PNCDI IV. 

23 

Ann. For. Res. 69(2): 1-26, 2026 

Research article 

# **References** 

- ANCPI, 2026. TopRO50 [Dataset]. National Agency for Cadastre and Land Registration, Romania. Available online: [https://geoportal. a n c p i . r o / p o r t a l / a p p s / w e b a p p v i e w e r / i n d e x . h t m l ? i d = 6 f c b d 3 3 e 7 c a 6 4 2 1 5 9 8 5 b 4 78e94cbab64&zOo2V=8MHn8.]. Date accessed: 22.05.2026. 

- Alipour M., La Puma I.P., Picotte J., Shamsaei K., Rowell E., Watts A., Kosović B., Ebrahimian H., Taciroğlu E., 2023. A multimodal data fusion and deep learning framework for large-scale wildfire surface fuel mapping. Fire 6(2): 36. https://doi.org/10.3390/fire6020036 

- Anderson H.E., 1982. Aids to determining fuel models for estimating fire behavior. General Technical Report INT-122. USDA Forest Service, Intermountain Forest and Range Experiment Station, Ogden, UT. https://doi. org/10.2737/INT-GTR-122 

- Aragoneses E., García M., Salis M., Ribeiro L., Chuvieco E., 2023. Classification and mapping of European fuels using a hierarchical, multipurpose fuel classification system. Earth System Science Data 15: 1287–1315. https://doi.org/10.5194/essd-15-1287-2023 

- Arca B., Duce P., Laconi M., Pellizzaro G., Salis M., Spanò D., 2007. Evaluation of FARSITE simulator in Mediterranean maquis. International Journal of Wildland Fire 16: 563–572. https://doi.org/10.1071/ WF06070 

- Benali A., Sá A., Ervilha A.R., Trigo R., Fernandes P., Pereira J., 2017. Fire spread predictions: Sweeping uncertainty under the rug. Science of the Total Environment 592: 187–196. https://doi.org/10.1016/j. scitotenv.2017.03.106 

- Cai L., He H.S., Liang Y., Wu Z., Huang C., 2019. Analysis of the uncertainty of fuel model parameters in wildland fire modelling of a boreal forest in north-east China. International Journal of Wildland Fire 28: 205–215. https://doi.org/10.1071/WF18083 

- Cao C., Xiong J., Blonski S., Liu Q., Uprety S., Shao X., Bai Y., Weng F., 2013. Suomi NPP VIIRS sensor data record verification, validation, and long-term performance monitoring. Journal of Geophysical Research: Atmospheres 118(20): 11664–11678. https:// doi.org/10.1002/2013JD020418 

- Dobrinkova N., Hollingsworth L., Heinsch F.A., Dillon G., Dobrinkov G., 2014. Bulgarian fuel models developed for implementation in FARSITE simulations for test cases in Zlatograd area. In Wade D.D., Fox R.L. (eds), Proceedings of the 4th Fire Behavior and Fuels Conference, 18–22 February 2013, Raleigh, NC and 1–4 July 2013, St. Petersburg, Russia. International Association of Wildland Fire, Missoula, MT, pp. 513– 521. 

- Dobrinkova N., 2025. Data accuracy challenges in wildland fire simulations. In Dobrinkova N., Fidanova S. (eds), Environmental Protection and Disaster Risks (EnviroRisks 2024). Lecture Notes in Networks and Systems, vol. 883. Springer, Cham. https://doi. org/10.1007/978-3-031-74707-6_33 

- Drusch M, Del Bello U, Carlier S, Colin O, Fernandez V, Gascon F, Hoersch B, Isola C, Laberinti P, Martimort P, Meygret A, Spoto F, Sy O, Marchese F, Bargellini P, 2012. Sentinel-2: ESA's Optical High-Resolution Mission for GMES Operational Services. Remote Sensing of Environment 120: 25–36. https://doi. 

org/10.1016/j.rse.2011.11.026. 

- Duff T.J., Chong D.M., Taylor P., Tolhurst K.G., 2012. Procrustes based metrics for spatial validation and calibration of two-dimensional perimeter spread models: A case study considering fire. Agricultural and Forest Meteorology 160: 110–117. https://doi. org/10.1016/j.agrformet.2012.03.002 

- Duff T.J., Chong D.M., Tolhurst K.G., 2016. Indices for the evaluation of wildfire spread simulations using contemporaneous predictions and observations of burnt area. Environmental Modelling & Software 83: 276– 285.https://doi.org/10.1016/j.envsoft.2016.05.005 

- European Environment Agency, 2024. Tree Cover Density 2018 Present (raster 10 m), Europe, yearly [Dataset]. Copernicus Land Monitoring Service. https://doi. org/10.2909/e677441e-fb94-431c-b4f9-304f10e4dfd8. Date accessed: 22.09.2025. 

- Farr T.G., Rosen P.A., Caro E., Crippen R., Duren R., Hensley S., Kobrick M., Paller M., Rodriguez E., Roth L., Seal D., Shaffer S., Shimada J., Umland J., Werner M., Oskin M., Burbank D., Alsdorf D., 2007. The Shuttle Radar Topography Mission. Reviews of Geophysics 45: RG2004. https://doi.org/10.1029/2005RG000183 

- Finney M.A., 1998. FARSITE: Fire Area Simulator— model development and evaluation. Research Paper RMRS-RP-4, Revised 2004. U.S. Department of Agriculture, Forest Service, Rocky Mountain Research Station, Ogden, UT, 47 p. https://doi.org/10.2737/ RMRS-RP-4 

- Hardison T., 2003. Applications of remote sensing and GIS to modeling fire for vegetative restoration in Northern Arizona. MSc Thesis, Department of Biological Sciences, University of North Texas, Denton, TX, 57 p. 

- Hetzer J., Forrest M., Ribalaygua J., Prado-López C., Hickler T., 2024. The fire weather in Europe: large-scale trends towards higher danger. Environmental Research Letters 19: 074021. https://doi.org/10.1088/1748-9326/ ad5b09. 

- Hodges J.L., Lattimer B.Y., 2019. Wildland fire spread modeling using convolutional neural networks. Fire Technology 55: 2115–2142. https://doi.org/10.1007/ s10694-019-00846-4 

- Galizia L., Barbero R., Rodrigues M., Ruffault J., Pimont F., Curt T., 2023. Global warming reshapes European pyroregions. Earth's Future 11: e2022EF003182. https://doi.org/10.1029/2022EF003182. 

- Gâștescu P., Pișota I., Ciovică N., Pătăchie I., 1975. The hydro-climatic particularities of Romania. Geoforum 6: 29–37. https://doi.org/10.1016/0016-7185(75)90009-3 

- Giglio L., Descloitres J., Justice C.O., Kaufman Y.J., 2003. An enhanced contextual fire detection algorithm for MODIS. Remote Sensing of Environment 87(2–3): 273–282. https://doi.org/10.1016/S00344257(03)00184-6 

- Grünig M., Seidl R., Senf C., 2022. Increasing aridity causes larger and more severe forest fires across Europe. Global Change Biology 29: 1648–1659. https:// doi.org/10.1111/gcb.16547 

- INCDS, 2017a. Forest Management Plan of Dobra Forest District U.P. I Stăncești. Institutul Național de CercetareDezvoltare în Silvicultură „Marin Drăcea”, Stațiunea Brașov, Brașov, Romania.[Amenajamentul Ocolului Silvic Dobra, U.P. I Stăncești. Institutul Național de Cercetare-Dezvoltare în Silvicultură „Marin Drăcea”, Stațiunea Brașov, Brașov, Romania.] 

- INCDS, 2017b. Forest Management Plan of Dobra Forest 

24 

Developing a FARSITE wildfire simulation framework for Romania.... 

Samsodan et al. 

- District U.P. II Fața Râului. „Marin Drăcea” National Institute for Research and Development in Forestry, Brașov Station, Brașov, Romania. [Amenajamentul Ocolului Silvic Dobra, U.P. II Fața Râului. Institutul Național de Cercetare-Dezvoltare în Silvicultură „Marin Drăcea”, Stațiunea Brașov, Brașov, Romania.] 

- INCDS, 2018. Forest Management Plan of Brad Forest District, U.P. II Brad. „Marin Drăcea” National Institute for Research and Development in Forestry, Brașov Station, Brașov, Romania. [Amenajamentul Ocolului Silvic Brad, U.P. II Brad. Institutul Național de Cercetare-Dezvoltare în Silvicultură „Marin Drăcea”, Stațiunea Brașov, Brașov, Romania.] 

- INCDS, 2019a. Forest Management Plan of Orșova Forest District, U.P. II Șvinița. „Marin Drăcea” National Institute for Research and Development in Forestry, Craiova, Station Craiova, Romania. [Amenajamentul Ocolului Silvic Orșova, U.P. II Șvinița. Institutul Național de Cercetare-Dezvoltare în Silvicultură „Marin Drăcea”, Stațiunea C.D.E.P. Craiova, Craiova, Romania.] 

- INCDS, 2019b. Forest Management Plan of Orșova Forest District, U.P. III Baia Nouă. „Marin Drăcea” National Institute for Research and Development in Forestry, Craiova, Station Craiova, Romania. [Amenajamentul Ocolului Silvic Orșova, U.P. III Baia Nouă. Institutul Național de Cercetare-Dezvoltare în Silvicultură „Marin Drăcea”, Stațiunea C.D.E.P. Craiova, Craiova, Romania.] 

- Jahdi R., Salis M., Darvishsefat A., Mostafavi M., Alcasena F.J., Etemad V., Lozano O., Spanò D., 2015. Calibration of FARSITE simulator in northern Iranian forests. Natural Hazards and Earth System Sciences 15: 443–459. https://doi.org/10.5194/nhess-15-443-2015 

- Jones M.W., Abatzoglou J., Veraverbeke S., Andela N., Lasslop G., Forkel M., Smith A.J.P., Burton C.A., Betts R., van der Werf G.R., Sitch S., Canadell J.G., Santín C., Kolden C., Doerr S.H., Le Quéré C., 2022. Global and regional trends and drivers of fire under climate change. Reviews of Geophysics 60: e2020RG000726. https:// doi.org/10.1029/2020RG000726. 

- Justice C.O., Townshend J.R.G., Vermote E.F., Masuoka E., Wolfe R.E., Saleous N., Roy D.P., Morisette J.T., 2002. An overview of MODIS land data processing and product status. Remote Sensing of Environment 83(1–2): 3–15. https://doi.org/10.1016/S0034-4257(02)00084-6 

- Keane R., Mincemoyer S., Schmidt K.M., Long D., Garner J., 2000. Mapping vegetation and fuels for fire management on the Gila National Forest Complex, New Mexico. General Technical Report RMRS-GTR-46. U.S. Department of Agriculture, Forest Service, Rocky Mountain Research Station. https://doi.org/10.2737/ RMRS-GTR-46 

- Krasnow K., Schoennagel T., Veblen T., 2009. Forest fuel mapping and evaluation of LANDFIRE fuel maps in Boulder County, Colorado, USA. Forest Ecology and Management 257: 1603–1612. https://doi.org/10.1016/j. foreco.2009.01.020 

- Kuhnen K., Andrade M.S., Müller M.M., Vacik H., 2026. Comparative analysis of wildfire spread models under differing environmental conditions in Central Europe. Fire 9(7): 311. https://doi.org/10.3390/fire9070311 

- Kutchartt E., González-Olabarria J.R., Trasobares A., Aquilué N., Guerra-Hernández J., Nunes L., Sequeira A.C., Botequim B., Hauglin M., Palaiologou P., Cardil A., Rogai M., Vassilev V., Pimont F., Martin-Ducup O., 

- Pirotti F., 2025. Satellite-based mapping of canopy fuels at the pan-European scale. Geo-spatial Information Science 28(4): 1465–1493. https://doi.org/10.1080/100 95020.2024.2429376 

- Lang N., Jetz W., Schindler K., Wegner J.D., 2023. A highresolution canopy height model of the Earth. Nature Ecology & Evolution 7(11): 1778–1789.https://doi. org/10.1038/s41559-023-02206-6 

- Lorenț A., Petrila M., Capalb F., Apostol B., Marcu C., Badea N.O., 2025a. Overview of the forest fires defense system in Romania. In Dobrinkova N., Fidanova S. (eds), Environmental Protection and Disaster Risks (EnviroRisks 2024). Springer, Cham, pp. 265–275. https://doi.org/10.1007/978-3-031-74707-6_29 

- Lorenț A., Petrila M., Apostol B., Capalb F., Chivulescu Ș., Șamșodan C., Marcu C., Badea O., 2025b. Assessing and mapping forest fire vulnerability in Romania using maximum entropy and extreme gradient boosting. Forests 16(7): 1156.https://doi.org/10.3390/f16071156 

- Malinowski R., Lewiński S., Rybicki M., Gromny E., Jenerowicz M., Krupiński M., Nowakowski A., Wojtkowski C., Krätzschmar E., Schauer P., 2020. Automated production of a land cover/use map of Europe based on Sentinel-2 imagery. Remote Sensing 12(21): 3523. https://doi.org/10.3390/rs12213523 

- Mallinis G., Mitsopoulos I., Dimitrakopoulos A., Gitas I., Karteris M., 2008. Local-scale fuel-type mapping and fire behavior prediction by employing high-resolution satellite imagery. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing 1: 230– 239. https://doi.org/10.1109/JSTARS.2008.2011298 

- Martins L., Almeida R.V.d., Maia A., Vieira P., 2025. Analysing fire propagation models: A case study on FARSITE for prolonged wildfires. Fire 8(5): 166. https://doi.org/10.3390/fire8050166 

- Mutlu M., Popescu S., Zhao K., 2008. Sensitivity analysis of fire behavior modeling with LIDAR-derived surface fuel maps. Forest Ecology and Management 256: 289– 294. https://doi.org/10.1016/j.foreco.2008.04.014 

- National Forest Inventory, 2026. Results of the Third National Forest Inventory Cycle (2020–2025). National Institute for Research and Development in Forestry “Marin Drăcea”, Romania. 

- NASA JPL, 2013. NASA Shuttle Radar Topography Mission Global 1 arc second [Dataset]. NASA Land Processes Distributed Active Archive Center. https:// doi.org/10.5067/MEASURES/SRTM/SRTMGL1.003 Date accessed: 22.09.2025. 

- Noble I.R., Gill A.M., Bary G.A.V., 1980. McArthur's fire-danger meters expressed as equations. Australian Journal of Ecology 5: 201–203. https://doi. org/10.1111/j.1442-9993.1980.tb01243.x 

- Paugam R., Sánchez P., González I., Carrillo C., Filippi J.-B., 2025. A comparison between FARSITE and FOREFIRE. Journal of Physics: Conference Series 3121: 012031. https://doi.org/10.1088/17426596/3121/1/012031 

- Price S.J., Germino M., 2022. Modeling of fire spread in sagebrush steppe using FARSITE: an approach to improving input data and simulation accuracy. Fire Ecology 18: 23. https://doi.org/10.1186/s42408-02200147-2 

- Rothermel R.C., 1972. A mathematical model for predicting fire spread in wildland fuels. Research Paper INT-115. USDA Forest Service, Intermountain Forest and Range Experiment Station, Ogden, UT. https://doi. 

25 

Ann. For. Res. 69(2): 1-26, 2026 

Research article 

org/10.2737/INT-RP-115 

- Salis M., Arca B., Alcasena F.J., Arianoutsou M., Bacciu V., Duce P., Duguy B., Koutsias N., Mallinis G., Mitsopoulos I., Moreno J.M., Pérez J.R., Urbieta I., Xystrakis F., Zavala G., Spanò D., 2016. Predicting wildfire spread and behaviour in Mediterranean landscapes. International Journal of Wildland Fire 25: 1015–1032. https://doi.org/10.1071/WF15081 

- San-Miguel-Ayanz J., Schulte E., Schmuck G., Camia A., Strobl P., Libertà G., Giovando C., Boca R., Sedano F., Kempeneers P., McInerney D., Withmore C., Santos de Oliveira S., Rodrigues M., Durrant T., Corti P., Oehler F., Vilar L., Amatulli G., 2012. Comprehensive monitoring of wildfires in Europe: the European Forest Fire Information System (EFFIS). In Tiefenbacher J. (ed.), Approaches to Managing Disaster – Assessing Hazards, Emergencies and Disaster Impacts. InTech, pp. 87–105. https://doi.org/10.5772/28441 

- San-Miguel-Ayanz J., Durrant T., Boca R., Maianti P., Liberta G., Artes Vivancos T., Oom D., Branco A., De Rigo D., Ferrari D., Pfeiffer H., Grecchi R., Nuijten D., Leray T., 2023. Forest fires in Europe, Middle East and North Africa 2022. Publications Office of the European Union, Luxembourg. https://doi.org/10.2760/348120 

- Schroeder W., Oliva P., Giglio L., Csiszar I.A., 2014. The new VIIRS 375 m active fire detection data product: Algorithm description and initial assessment. Remote Sensing of Environment 143: 85–96.https://doi. 

- org/10.1016/j.rse.2013.12.008 

- Scott J.H., Burgan R.E., 2005. Standard fire behavior fuel models: A comprehensive set for use with Rothermel's surface fire spread model. General Technical Report RMRS-GTR-153. USDA Forest Service, Rocky Mountain Research Station. https://doi.org/10.2737/ RMRS-GTR-153 

- Scott J.H., Reinhardt E.D., 2001. Assessing crown fire potential by linking models of surface and crown fire behavior. Research Paper RMRS-RP-29. U.S. Department of Agriculture, Forest Service, Rocky Mountain Research Station, Fort Collins, CO, 59 p. https://doi.org/10.2737/RMRS-RP-29 

- Sedano F., San-Miguel-Ayanz J., Broglia M., Durrant T., Boca R., Maianti P., Oom D.J.F., Branco A., De Rigo D., Suarez-Moreno M., Ferrari D., Roglia E., Scionti N., Liberta G., Tistan A., 2025. Forest fires in Europe, Middle East and North Africa 2024. Publications Office of the European Union, Luxembourg. https://doi. org/10.2760/0649290 

- Sjostrom J., Petrila M., Lorenț A., 2024. Fires in Romania. In Almeida M. et al. (eds), Report on the large wildfires of 2022 in Europe. Publications Office of the European Union, pp. 133–138. https://doi.org/10.2760/19760 

- Zhou J., Jiang W., Wang F., Qiao Y., Meng Q., 2024. Comparing accuracy of wildfire spread prediction models under different data deficiency conditions. Fire 7(4): 141. https://doi.org/10.3390/fire7040141 

26 
