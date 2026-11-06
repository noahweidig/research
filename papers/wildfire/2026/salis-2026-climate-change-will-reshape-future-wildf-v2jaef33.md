---
title: Climate change will reshape future wildfire danger and hazard in Sardinia, Italy
authors:
- Salis, Michele
- Giudice, Liliana Del
- Alcasena, Fermín
- Scarpa, Carla
- Bacciu, Valentina
- Pellizzaro, Grazia
- Jahdi, Roghayeh
- Duce, Pierpaolo
- Monjo, Robert
- Ribalaygua, Jaime
- Torres, Luís
- Prado‐Lopez, Carlos
- Arca, Bachisio
year: '2026'
journal: Natural Hazards
doi: 10.1007/s11069-026-08320-5
tags:
- wildfire
- wildfire occurrence
zotero_key: V2JAEF33
item_type: journalArticle
url: https://openalex.org/W7208784285
source_url: 'unpaywall: https://link.springer.com/content/pdf/10.1007/s11069-026-08320-5.pdf'
fulltext_status: fulltext
synced: '2026-11-06'
---

# Climate change will reshape future wildfire danger and hazard in Sardinia, Italy

## Abstract

Abstract Recent years have highlighted an increasing vulnerability to wildfires in Europe driven by climate, land use change, and socio-economic factors. Under future projected warming and drying patterns, Mediterranean areas emerge as one of the most wildfire-sensitive regions. This study combines high-resolution climate projections from three CMIP6 models (ACC, ECE, MPI) under three SSP scenarios with a wildfire modeling framework to assess wildfire danger and hazard for historical baseline (1985–2014) and a near-future period (2035–2064) in Sardinia, Italy. Climate variables were statistically downscaled to 1 km 2 resolution and used to calculate Fire Weather Index (FWI) and Daily Severity Rating (DSR). Then, using the Minimum Travel Time algorithm and probabilistic fire simulations, we generated spatially explicit estimates of burn probability, fire intensity and crown fire probability at 150 m resolution. Despite model-dependent differences in magnitude, all scenarios consistently point to warmer, drier, and more fire-prone conditions. Results indicate a systematic shift toward more severe fire danger under future scenarios, with a marked increase in the days reaching very high FWI and DSR values, particularly from May to October, which evidences nearly doubled frequencies under SSP5-8.5 scenarios. Similarly, simulated wildfire hazard outputs show significant increases, with hotspots expanding towards western and inland Sardinia, particularly with ECE (+ 250% of annual area burned moving from baseline to 2035–2064, under SSP5-8.5). These results provide detailed spatial assessments of future potential wildfire impacts in a fire-prone Mediterranean region and offer insights to support fire and land management in landscapes highly susceptible to wildfire occurrence.

## Full text

Natural Hazards (2026) 122:629 https://doi.org/10.1007/s11069-026-08320-5 

**<mark>ORIGINAL PAPER</mark>** 

# **Climate change will reshape future wildfire danger and hazard in Sardinia, Italy** 



**Michele Salis**<sup>**1**</sup> **· Liliana Del Giudice**<sup>**1**</sup> **· Fermin Alcasena-Urdiroz**<sup>**2**</sup> **· Carla Scarpa**<sup>**1**</sup> **· Valentina Bacciu**<sup>**1**</sup> **· Grazia Pellizzaro**<sup>**1**</sup> **· Roghayeh Jahdi**<sup>**3**</sup> **· Pierpaolo Duce**<sup>**1**</sup> **· Robert Monjo**<sup>**4,5**</sup> **· Jaime Ribalaygua**<sup>**4**</sup> **· Luis Torres**<sup>**4**</sup> **· Carlos Prado**<sup>**4**</sup> **· Bachisio Arca**<sup>**1**</sup> 

Received: 13 April 2026 / Accepted: 2 July 2026 / Published online: 4 September 2026 © The Author(s) 2026 

### **Abstract** 

Recent years have highlighted an increasing vulnerability to wildfires in Europe driven by climate, land use change, and socio-economic factors. Under future projected warming and drying patterns, Mediterranean areas emerge as one of the most wildfire-sensitive regions. This study combines high-resolution climate projections from three CMIP6 models (ACC, ECE, MPI) under three SSP scenarios with a wildfire modeling framework to assess wildfire danger and hazard for historical baseline (1985–2014) and a near-future period (2035–2064) in Sardinia, Italy. Climate variables were statistically downscaled to 1 km<sup>2</sup> resolution and used to calculate Fire Weather Index (FWI) and Daily Severity Rating (DSR). Then, using the Minimum Travel Time algorithm and probabilistic fire simulations, we generated spatially explicit estimates of burn probability, fire intensity and crown fire probability at 150 m resolution. Despite model-dependent differences in magnitude, all scenarios consistently point to warmer, drier, and more fire-prone conditions. Results indicate a systematic shift toward more severe fire danger under future scenarios, with a marked increase in the days reaching very high FWI and DSR values, particularly from May to October, which evidences nearly doubled frequencies under SSP5-8.5 scenarios. Similarly, simulated wildfire hazard outputs show significant increases, with hotspots expanding towards western and inland Sardinia, particularly with ECE (+ 250% of annual area burned moving from baseline to 2035–2064, under SSP5-8.5). These results provide detailed spatial assessments of future potential wildfire impacts in a fire-prone Mediterranean region and offer insights to support fire and land management in landscapes highly susceptible to wildfire occurrence. 

**Keywords** Wildfire modeling · Burn probability · Future conditions · Wildfire management · Mediterranean areas · MTT algorithm 

Extended author information available on the last page of the article 

**<mark>629</mark>** <mark>Page 2 of 36</mark> 

Natural Hazards (2026) 122:629 

## **1 Introduction** 

Wildfires represent one of the most significant natural hazards in southern European countries, where large events occur frequently and cause substantial impacts on environmental, social, and economic systems (Oom et al. 2022). Recent seasons have highlighted the growing vulnerability of southern Europe to large and extreme wildfire events (Rodrigues et al. 2023; Keeping et al. 2025). For instance, with more than 0.5 million hectares affected by wildfires, 2022 was one of the worst seasons in southwestern European countries (Sedano et al. 2025). Furthermore, in 2025, more than 1 million hectares burned across the EU (with Spain and Portugal accounting for most of the area burned during an intense heatwave), thus exceeding the previous record set in 2017 and marking the largest area burned since the early 2000s (European Commission, Joint Research Centre, 2025) . A body of research has evidenced that this pattern resulted from complex and spatially heterogeneous interactions among multiple drivers, including climate change, land abandonment, fuel build-up, and socio-economic changes that have reshaped, and are reshaping, rural and forest landscapes and land management practices in Southern Europe (Turco et al. 2018; Carlucci et al. 2019; Carnicer et al. 2022; Giannaros et al. 2022; Salis et al. 2022; Fernandez-Guisuraga and Calvo 2023; Moreno et al. 2023; Parente et al. 2023; Keeping et al. 2025). 

Among the factors influencing wildfire dynamics, climate change has emerged as a major concern, as projected increases in temperature, prolonged droughts, and more frequent heatwaves are expected to intensify fire danger conditions and increase the likelihood and severity of extreme wildfire seasons (Flannigan et al. 2009; Bacciu et al. 2021; Duane et al. 2021; Senande-Rivera et al. 2022; Seneviratne et al. 2021; Alvarez et al. 2024). In this context, the Mediterranean Basin is a particularly vulnerable climate change hotspot, where climatic changes can interact with socio-ecological factors to increase wildfire risk and associated losses (Lionello and Scarascia 2018; Jones et al. 2022; Lazoglou et al. 2024). To quantify climate projections of wildfire danger, several works rely on fire weather indices, such as the Canadian Forest Fire Weather Index (FWI) (van Wagner 1987) or the National Fire Danger Rating System (NFDRS) (Jolly et al. 2024). 

The FWI is widely used to assess wildfire danger across Europe under past, present and future climate conditions because it integrates key meteorological variables to estimate potential fire behavior and fuel moisture conditions (Venalainen et al. 2014; Di Giuseppe et al. 2020; Dupuy et al. 2020). Nonetheless, the FWI and other fire danger models have intrinsic limitations in explicitly representing several processes that may affect local wildfire behavior, such as pyro-convection, cold fronts, or downslope windstorms (Nauslar et al. 2018; He et al. 2025). Several studies have highlighted that wildfire danger is projected to increase in Southern Europe and the Mediterranean Basin under future climate scenarios (Fargeon et al. 2020; Cos et al. 2022; Cardoso Pereira et al. 2024; He et al. 2025). Nevertheless, uncertainties remain regarding the spatial variability of wildfire danger and the interaction of multiple drivers, highlighting the need for further studies based on high-resolution climate projections and improved wildfire modeling frameworks (Abatzoglou et al. 2021; Hetzer et al. 2024). 

Wildfire spread models provide a robust framework for analyzing the interactions among weather, topography, and vegetation that govern fire propagation, and for translating environmental and climatic conditions into spatially explicit simulations of fire growth and behavior (Balbi et al. 2009; Monedero et al. 2019; Trucchia et al. 2020; Salis et al. 2023; 

```
1 3
```

<mark>Page 3 of 36</mark> **<mark>629</mark>** 

Natural Hazards (2026) 122:629 

Cardoso et al. 2025; Kim et al. 2025). In fact, by integrating spatial and temporal information on wildfire drivers, these models allow the identification of potential wildfire paths and of areas more prone to intense fire activity or losses (Alcasena et al. 2021; Rodrigues et al. 2022; Carlson et al. 2025). Algorithms such as the Minimum Travel Time (MTT) (Finney 2002) are particularly promising because they can efficiently simulate fire spread across heterogeneous and vast landscapes while accounting for spatial variations in topography, fuels, ignition patterns, and wind conditions, as well as the likelihood of different patterns (Parisien et al. 2019). Weather and climate act as top-down drivers of wildfire regimes, as they affect extensive regions, whereas the spatial arrangement of fuels and fire ignitions serves as a bottom-up control because of their heterogeneous local variability and distribution (Parisien et al. 2010). When coupled with climate projections, wildfire spread modelling can also be used to explore how future changes in temperature, precipitations, and wind fields may influence wildfire propagation patterns and landscape-scale hazard (Conver et al. 2018; Kalabokidis et al. 2015; Lozano et al. 2017). In fact, wildfire spread modeling enables large-scale simulation of fire spread and associated behavior, thereby supporting the evaluation of multiple scenarios under changing climate and landscape conditions, the incorporation of probabilistic occurrence, and the integration with wildfire danger indices (Mitsopoulos et al. 2016; Salis et al. 2021). Furthermore, burn probability estimates enable the assessment of climate change effects on wildfire risk across large study areas at fine spatial scales, while accounting for local drivers of wildfire spread such as fuel types and slope–wind alignment (Lozano et al. 2017; Moran et al. 2025). 

In this study, we examined historical (1985–2014) and future (2035–2064) wildfire danger and hazard in Sardinia, Italy, by coupling high-resolution climate projections from three climate models (ACCESS-ESM1-5 (ACC); EC-EARTH3 (ECE); MPI-ESM1-2-HR (MPI)) and three SSP scenarios, with a wildfire modeling framework. Figure 1 summarizes the workflow of the modelling framework adopted in this study, linking climate projections, wildfire danger assessment, and wildfire spread simulations. We define wildfire danger as the weather-driven potential for wildfire occurrence, spread and difficulty of control (Sirca et al. 2018; Pagnon Eriksson et al. 2023), and wildfire hazard as the combination of the likelihood of fire occurrence and the potential wildfire intensity, which reflect the probability of burning and the energy released if a fire occurs (Brown et al. 2024).We first quantified changes in key climate variables, including temperature, winds, precipitations, and rainy days, and evaluated their effects on wildfire danger using both Fire Weather Index (FWI) and Daily Severity Rating (DSR) metrics. Then, by adopting a probabilistic approach and running a number of fire spread simulations based on the MTT algorithm, we analyzed and mapped future wildfire hazard conditions using burn probability, flame length, crown fire probability, fire size and average annual burned area as main indicators. The results evidence that future climate change will increase wildfire danger and hazard conditions in Sardinia, even if spatial patterns and magnitude vary depending on model and SSP scenario. The main novelty of this work lies in providing high-resolution, probabilistic, and spatially explicit estimates that capture the local effects of changing weather conditions on wildfire spread processes. Despite increasing concerns about the effects of climate change on wildfire regimes, previous studies conducted in Southern Europe have often been limited to coarse-resolution fire danger assessments and have not explicitly examined potential shifts in burn patterns and wildfire spread (Sullivan 2009; Dye et al. 2023). By addressing these limitations, this study explores how climate change may affect wildfire danger and proba- 

```
1 3
```

**<mark>629</mark>** <mark>Page 4 of 36</mark> 

Natural Hazards (2026) 122:629 



**Fig. 1** Workflow of the modelling framework proposed in this study to assess future changes in wildfire danger and hazard under climate change scenarios in Sardinia, Italy. Daily projections of relative humidity, temperature, wind speed, and precipitation derived from four climate models and three SSP scenarios were first used to characterize future weather conditions and to calculate the Fire Weather Index (FWI) at 8-km spatial resolution and daily scale. FWI was used to assess changes in future wildfire danger and to identify high fire danger days (average FWI > 38). The high fire danger days provided the fuel moisture and wind inputs for the MTT wildfire spread model, which was run together with fuels, topography, and fire ignition data at 150-m spatial resolution to simulate wildfire behavior. Model outputs, including burned area, burn probability, flame length, and crown fire occurrence, were then integrated to assess future wildfire hazard 

bilistic risk components under different future scenarios and discusses the implications for wildfire risk in Sardinia. Overall, the study provides detailed spatial information to support wildfire management planning, risk mitigation, and the development of more resilient landscapes in fire-prone Mediterranean areas under increasingly extreme climatic conditions, while also offering relevant evidence to inform climate change adaptation policies in the region. 

## **2 Methods** 

### **2.1 Study area** 

The study area is Sardinia (Italy), which covers about 24,000 km<sup>2</sup> and is the second-largest island of the Mediterranean Basin (Fig. 2). The orography is complex, with elevations ranging from 0 to 1850 m a.s.l., and a mean altitude of about 350 m a.s.l. The main plains are located in the western part of the island. Sardinia exhibits diverse land uses, with shrublands representing the main category (~ 24%, of which ~ 9% in thermomediterranean bioclimatic areas) (EEA 2020) (Fig. 2). This class primarily includes _Olea europaea_ var. _sylvestris_ Brot., _Pistacia lentiscus_ L., _Arbutus unedo_ L., _Erica arborea_ L., _Myrtus communis_ L., as well as Phillyrea spp., Juniperus spp., and Cistus spp.. Forested areas account for ~ 23% of the island, are mainly located in inner Sardinia, and are mostly represented by broadleaf forests (e.g.: Quercus spp.). Croplands (herbaceous, ~ 24%, and permanent, ~ 3%) and agricul- 

```
1 3
```

<mark>Page 5 of 36</mark> **<mark>629</mark>** 

Natural Hazards (2026) 122:629 



**Fig. 2 a** Main land use classes of Sardinia, Italy, according to the EEA 2020 (AA = anthropic areas; WB = water bodies; R = rocks; HC = herbaceous crops; PC = permanent crops; AM = agricultural mosaics; NP = natural pastures; TSH = thermomediterranean shrublands; SH = shrublands; TF = thermomediterranean forests; F = forests. **b** weather zones (adapted from Sardinia Environmental Protection Agency) and bio-climatic classification (Canu et al. 2015) of Sardinia, along with the reference point (wind stations) used for the evaluation of the wind speed and direction scenarios for days with FWI _≥_ 38. LTM = lower thermomediterranean; UTM = upper thermomediterranean; LMM = lower mesomediterranean; UMM = upper mesomediterranean; SM = supramediterranean; MT = mesotemperate; ST = supratemperate. **c** Historical wildfire ignitions (study period: 2003–2022) in Sardinia as a function of the final size 

tural mosaics (~ 20%) reflect the strong influence of agricultural practices on land use, while natural pastures cover ~ 3% of Sardinia lands. Urban areas account for ~ 3% of the island. 

Climatic conditions show pronounced spatial variability. In broad terms, temperature and precipitation follow gradients from the coast to the mountainous interior regions, and from south to north. Mean annual rainfall, concentrated mainly in the autumn–winter period, ranges from about 400 mm along the southern coasts to roughly 1100 mm in the mountainous areas (Fick and Hijmans 2017). The June–August months are generally dry. Average annual temperatures vary between 7 °C and 17 °C; during summer, temperatures frequently exceed 30 °C. Bioclimatic classification identifies approximately two-thirds of the island as mesomediterranean (Canu et al. 2015) (Fig. 2). Thermomediterranean bioclimate occurs 

```
1 3
```

**<mark>629</mark>** <mark>Page 6 of 36</mark> 

Natural Hazards (2026) 122:629 

mainly along the southern and coastal zones, while supramediterranean to supratemperate conditions can be found at higher elevations. 

Regarding wildfire regime, according to Sardinia Forest Service datasets, during the 2003–2022 period Sardinia recorded on average 2900 wildfire ignitions per year, of which about 740 burned more than 1 ha of land and affected an area of about 14,680 ha (that is, about 0.65% of the island’s total surface burned each year). Approximately 60% of fires occurred in the southern plains, while the largest wildfires were mostly concentrated in northern and western Sardinia (Fig. 2). Wildfires above 100 ha were limited in number (0.6% of total ignitions) but accounted for about 57% of the total area burned. The most of fires (94%) affected areas smaller than 10 ha and accounted for only 16% of the area burned. More than 90% of wildfires occurred between June and September, with a peak in both ignitions and area burned in July. 

### **2.2 Climate scenarios and data** 

We used meteorological data from the ERA5 global atmospheric reanalysis, produced by the European Centre for Medium-Range Weather Forecasts (ECMWF). The ERA5 dataset integrates a wide range of surface, upper-air, and satellite observations with a modern numerical weather prediction model and data assimilation system to generate a physically consistent, gridded reconstruction of past weather conditions (Hersbach et al. 2020). ERA5 offers hourly data with a horizontal resolution of about 31 km; the atmosphere is resolved vertically using 137 levels extending from the surface to 80 km in height (Han and Ullrich 2025). In this study, we used ERA5 reanalysis data from January 1st 1985 to December 31st 2014, focusing on the study area. 

We then used 3 climate models (Table 1) on daily resolution, collected from the Coupled Model Intercomparison Project (CMIP)—Phase 6 (CMIP6). CMIP is a collaborative framework organized in 1995 by the Working Group on Coupled Modelling (WGCM) of the World Climate Research Programme’s (WCRP). CMIP6 has a common set of future scenarios (Shared Socio-Economic Pathways (SSPs)) of projected socioeconomic global changes up to 2100 describing alternative socio-economic developments. For each model, two temporal periods were considered: a) January 1st 1985–December 31st 2014, representing historical climate conditions, and b) January 1st 2035–December 31st 2064, representing near-future climate projections. Future projections were assessed under three SSPs: SSP1-2.6, SSP2-4.5, and SSP5-8.5. This allowed to capture a broad range of potential emission scenarios. 

**Table 1** Information about the CMIP6 climate models used in this work 

|CMIP6 models|Resolution|Responsible centre|References|
|---|---|---|---|
|ACCESS-ESM1-5 (ACC)|1.875º × 1.250º|Australian Community Climate and<br>Earth System Simulator (ACCESS),<br>Australia|Ziehn et al.<br>(2020)|
|EC-EARTH3 (ECE)|0.703º × 0.702º|EC-EARTH Consortium|EC-Earth Con-<br>sortium (2019)|
|MPI-ESM1-2-HR (MPI)|0.938º × 0.935º|Max-Planck Institute for Meteorology<br>(MPI-M),Germany|Von Storch et<br>al.(2017)|



Models were supplied by the program for climate model diagnosis and intercomparison (PCMDI) archives. The acronym of each model adopted in this work is under parenthesis 

```
1 3
```

<mark>Page 7 of 36</mark> **<mark>629</mark>** 

Natural Hazards (2026) 122:629 

For the above CMIP6 climate models and related variables, a two-step statistical downscaling was applied following the approach developed by Monjo et al. (2025). In the first step, parametric quantile mapping was applied from the daily ERA5 reanalysis fields (0.073° × 0.073° resolution) to the daily historical/SSP-driven climate projections. For each projected day, a geostatistical technique was then applied to the 0.073° × 0.073° resolution data to obtain a final 1 km × 1 km grid. This second step involved AIC-based stepwise regression using topological and geographical parameters as predictors, followed by bilinear interpolation of the residual errors. Finally, the projected value for each day was obtained by adding the results of previous steps, obtaining climate scenarios in a 1 km × 1 km grid at a daily timescale. Statistical analyses of climate variables (i.e.: maximum temperatures, cumulated precipitation, and wind speed and direction) were conducted for all calendar months as well as focusing on May–October months (see Appendix for more details). 

### **2.3 Wildfire danger modeling and projections** 

To determine wildfire danger conditions for historical and future periods, we adopted the Canadian Forest Fire Weather Index (FWI) System (van Wagner 1987). This system comprises three fuel moisture codes (Fine Fuel Moisture Code (FFMC), Duff Moisture Code (DMC), and Drought Code (DC)), which are used to calculate the Initial Spread Index (ISI), a proxy for potential rate of flame spread, and the Buildup Index (BUI), which estimates the total amount of fuel available for combustion. The FWI integrates ISI and BUI to provide a relative rating of fire intensity and overall fire danger under given weather conditions (van Wagner 1987). Several previous studies (e.g.: Sirca et al. 2018; Calheiros et al. 2021; Aparicio et al. 2022) applied this index for fire danger rating purposes in Southern Europe. Moreover, in 2007, following a five-year testing phase, the European Forest Fire Information System (EFFIS) network of the European Commission adopted the FWI System as a harmonized method for assessing fire danger levels across Europe (Copernicus Emergency Management Service 2019). 

In this paper, the daily FWI values were determined from the climate data for all pixels of the study area throughout the study periods (1985–2014 and 2035–2064), for the different climate models and SSPs. FWI for each pixel was calculated using daily maximum temperature, daily minimum relative humidity, wind speed at 10 m (at 12:00 UTC) and daily cumulated precipitation. To differentiate fire danger classes and conditions, we adopted the thresholds proposed by EFFIS for the FWI (Copernicus Emergency Management Service 2019). We also evaluated the effects of climate change as simulated by climate models on the Daily Severity Rating (DSR), which is derived from FWI and quantifies the daily potential difficulty of wildfire suppression. The DSR formulation amplifies the influence of higher FWI values, highlighting days with particularly severe fire weather conditions (Lanet et al. 2025). Both FWI and DSR were calculated considering the average conditions at the annual scale as well as for the May–October months, that is the timeframe when wildfire occurrence is typical in most Mediterranean areas. 

### **2.4 Wildfire simulation modeling** 

To characterize wildfire spread and hazard, we first built a set of input datasets, including the spatial layers needed for the landscape (LCP file) of FlamMap (Finney 2002), data on fire 

```
1 3
```

**<mark>629</mark>** <mark>Page 8 of 36</mark> 

Natural Hazards (2026) 122:629 

weather, fuel moisture content, and ignition probability grids. The LCP file was generated with ArcFuels (Ager et al. 2011; Vaillant et al. 2013) by combining topographic information, surface fuel characteristics, and forest canopy attributes. The spatial data were processed to produce a gridded dataset with a spatial resolution of 150 m. Topographic variables were derived from the 10-m digital elevation model of Sardinia (www.sardegnageoportale.it); fuel data were obtained from the CORINE Land Cover 2018 (EEA 2020). Following the methodology proposed by Salis et al. (2021), the bioclimatic map of Sardinia (Canu et al. 2015) was also used to better represent spatial variability in Sardinia fuel conditions. Each combination of forest fuel types and bioclimatic conditions was assigned to a standard or custom surface fuel model, according to Anderson (1982), Arca et al. (2009), Salis et al. (2013), and Scott and Burgan (2005), as proposed in Salis et al. (2021). Forest canopy metrics, namely canopy cover, canopy bulk density, canopy base height, and canopy height, were derived from the National Inventory of Forests and Forest Carbon Sinks (INFC, 2005) and applied to define the vertical fuel structure within forested areas. 

We estimated fuel moisture conditions for the modeling domain using the FWI as proxy of dead and live fuel moisture conditions. More specifically, this analysis focused on days with FWI ≥ 38, that are commonly associated with low to very low dead and live fuel moisture levels: large wildfire spread in Sardinia and elsewhere is typically associated with extreme weather and high wildfire danger values (e.g.: Ager et al. 2014). Dead fuel moisture values used for the simulations were derived from data reported by Salis et al. (2015, 2021, 2023), based on field observations and measurements from fuel moisture sticks collected across different areas of Sardinia, focusing on severe weather conditions. These ranged from 7 to 13% for 1h to 11–17% for 100h dead fuels, with the lowest values observed for the hottest zones of the island. Live fuel moisture content (LFMC) values were defined using a longterm dataset collected in northern Sardinia from 2003 to 2024 (Pellizzaro et al. 2007, 2009; Salis et al. 2015; Chuvieco et al. 2011; Yebra et al. 2024), focusing on the driest months of the fire season (July and August). Live fuel moisture values ranged between 65 and 100%, depending on vegetation type and location. 

To derive the wind input data for wildfire spread modeling, the study area was divided into three Weather Zones (Northern, Central, and Southern Sardinia) (Fig. 2) following the approach of Salis et al. (2021). For each zone, a representative location was selected, based on the presence of a nearby weather station operated by the Environmental Protection Agency of Sardinia. Climate data extracted from these sites were used for statistical analyses to ensure spatial representativeness and to compare observed records with historical conditions obtained from the climatic models. On days with FWI ≥ 38, for each location representative of a Weather Zone we quantified the wind conditions using a set of reference categories based on wind speed (< 10, 10–20, 20–30, and > 30 km h⁻<sup>1</sup> ) and direction (N, NE, E, SE, S, SW, W, NW). This analysis was conducted for the different combinations of climate model, SSP, and time period. Wind speed, direction, and their respective frequency distributions at the Weather Zone level were then used as input parameters for the wildfire simulations. 

Wildfire spread simulations were performed using the Minimum Travel Time fire spread algorithm (MTT; Finney 2002) as implemented in the FConstMTT command-line version, which has been used in fire prone areas including the western United States and Mediter- 

```
1 3
```

<mark>Page 9 of 36</mark> **<mark>629</mark>** 

Natural Hazards (2026) 122:629 

ranean regions (Ager et al. 2017; Palaiologou et al. 2018; Alcasena et al. 2021; Salis et al. 2021). The MTT algorithm simulates two-dimensional fire growth by identifying the pathways of minimum travel time between adjacent cell corners at a user-defined spatial resolution. Fire spread rate is computed using the Rothermel (1972) model, while crown fire initiation is determined according to Van Wagner (1977), as implemented by Scott and Reinhardt (2001). This modeling framework has been extensively described and widely applied in wildfire management and risk assessment studies worldwide (e.g., Parisien et al. 2019). 

First, a set of 50,000 fire footprints was modeled under baseline conditions using ERA5 data, burning a total area of around 2.5 million ha, corresponding to about 167.5 fire seasons based on the observed mean annual burned area in Sardinia (~ 14,700 ha yr<sup>−1</sup> ). For climate models, for both historical and future scenarios, we used the average annual number of days with FWI ≥ 38 as proxy to determine the total wildfire simulations to perform with FConstMTT. Ignition points for the fire spread model were randomly distributed across burnable fuel areas according to an ignition probability grid derived from historical fire records. Each simulation was executed independently, with weather stream data, burn durations, and wind directions randomly drawn from the frequency distributions of the Weather Zone corresponding to the ignition location. Three fire duration classes (60, 180, and 360 min) were used to reproduce the variability in wildfire size and duration observed in Sardinia. Wildfire simulations and output maps were generated at 150 m resolution, assuming constant weather conditions throughout the fire spread duration and excluding fire containment effects on burned area, as the modeled fires represent wildfires that surpass containment efforts. 

From the modeled burned areas, for each model and scenario, we generated maps of annual burn probability (aBP) and then derived the annual area burned (aAB) for baseline and projected climate change conditions. Annual burn probability was calculated as the number of times each 150 m pixel burned divided by the total number of modeled iterations, given the historical ignition patterns and the weather conditions assigned to each scenario. This metric represents the likelihood of fire exposure across the landscape for valued resources and assets. Next, for each pixel, we calculated the aAB (ha yr<sup>−1</sup> ) from the the annual burn probability and the pixel area. We also derived a fire size potential map by assigning the final burned area of each simulated fire to its ignition point and interpolating these values across the landscape using inverse distance weighting with a 5 km search radius. The resulting surface represents the expected fire size if an ignition occurs in a given pixel under each scenario. 

In addition, we generated conditional flame length (CFL) maps, defined as the probability weighted flame length expected for a pixel, given that it burns, and expressed in meters. These values were estimated from the frequency distribution of 0.5 m flame length classes recorded for each pixel across the full set of simulated fire footprints. Finally, CFL was combined with canopy base height to approximate crown fire initiation potential, assuming that crowning becomes possible when flame length exceeds the vertical gap to the canopy base. This information, together with aBP, was then used to derive crown fire probability (CFP). CFL and CFP represent spatially explicit hazard metrics and provide an approximation of the potential for loss to valued assets and forests across the landscape. 

```
1 3
```

**<mark>629</mark>** <mark>Page 10 of 36</mark> 

Natural Hazards (2026) 122:629 

## **3 Results** 

### **3.1 Changes in climate variables** 

Overall, under historical conditions (1985–2014), the three climate models closely reproduced the ERA5 climate variables, with only limited differences, particularly for maximum temperature, in both the annual and May–October periods (Table 2; Appendix). Precipitation was also reasonably well captured, although with a small positive difference in annual cumulated rain and larger divergences in the 6-month period, especially for the ACC model. Nonetheless, the main spatial gradients, with wetter conditions in central and northern sectors and drier characteristics in southern Sardinia, were well represented. 

Future projections showed a reasonable and consistent signal across climate models. In general, despite differences in magnitude, all models point toward a warmer and generally drier future climate. The rise in maximum temperatures was stronger during the May–October period than at the annual scale. From a spatial point of view, the most relevant warming variations were mostly concentrated in inland and western Sardinia. Conversely, precipitation projections consistently indicated a general reduction tendency by 2035–2064, particularly at the annual scale. In our work, the ACC model highlighted the largest decreases in 

**Table 2** Average Tmax (°C), average cumulated precipitation (mm), and number of days with average precipitation above 1 mm (RD > 1 mm) for the annual timeframe and the May–October period in Sardinia as derived from ERA5 and three climate models (ACC, ECE, MPI) over 1985–2014, and corresponding projections for 2035–2064 under SSP1-2.6, SSP2-4.5, and SSP5-8.5 scenarios 

|Model|Reference<br>years|Tmax<br>(12 months)|Tmax<br>(6 months)|Prec<br>(12 months)|Prec<br>(6 months)|RD > 1 mm<br>(12 months)|RD > 1 mm<br>(6 months)|
|---|---|---|---|---|---|---|---|
|ERA5|1985–<br>2014|19.54|25.42|532.65|168.22|99.50|33.30|
|ACC|1985–<br>2014|19.57|25.50|554.71|201.03|99.84|36.67|
|ACC<br>SSP1-2.6|2035–<br>2064|22.32|28.30|494.84|148.27|89.50|31.07|
|ACC<br>SSP2-4.5|2035–<br>2064|22.74|28.80|492.99|161.48|88.64|30.53|
|ACC<br>SSP5-8.5|2035–<br>2064|22.75|28.93|485.92|167.82|82.87|28.50|
|ECE|1985–<br>2014|19.59|25.46|561.61|169.40|98.70|29.43|
|ECE<br>SSP1-2.6|2035–<br>2064|21.87|28.15|531.60|136.39|91.50|22.70|
|ECE<br>SSP2-4.5|2035–<br>2064|22.11|28.53|530.75|137.34|90.90|21.97|
|ECE<br>SSP5-8.5|2035–<br>2064|22.86|29.31|515.98|145.88|85.30|21.70|
|MPI|1985–<br>2014|19.58|25.44|551.30|155.61|95.81|27.50|
|MPI<br>SSP1-2.6|2035–<br>2064|20.92|27.06|525.85|135.60|94.43|25.20|
|MPI<br>SSP2-4.5|2035–<br>2064|21.11|27.10|514.48|135.82|91.60|24.17|
|MPI<br>SSP5-8.5|2035–<br>2064|21.24|27.41|511.53|143.82|90.63|23.83|



```
1 3
```

<mark>Page 11 of 36</mark> **<mark>629</mark>** 

Natural Hazards (2026) 122:629 

cumulated precipitations, whereas MPI showed the smallest changes. Even if May–October precipitation exhibited a non-monotonic response across SSP scenarios, future values remain below the historical values in all climate models. It is noteworthy to evidence that all simulations revealed a decrease in the number of rainy days (> 1 mm), especially during the hottest months, with a likely increase of length and frequency of dry spells and the inherent effects, combined with increased temperatures, on fuel dryness. The analysis of future wind conditions, focusing on days with FWI ≥ 38, evidenced that the increase in very high danger days was associated to a significant increase in the occurrence of low- and moderate-wind classes, while days with strong wind speed remained limited. 

### **3.2 Changes in wildfire danger** 

During the 1985–2014 period, the distribution of Fire Weather Index (FWI) classes was mainly represented by low danger conditions, particularly for the Jan-Dec period, with low FWI values accounting for approximately 62–65% of days across all climate models (Table 3). In the May–Oct timeframe, the relative contribution of high FWI classes substantially increased, with H and VH danger conditions representing an important component (around 43–46% of days in the historical period), while the frequency of low danger days decreased. Days with very high FWI values remained relatively limited in the historical period, and basically showed double values in May–Oct compared to the annual timeframe: in other words, days with FWI ≥ 38 were almost totally concentrated in the May–Oct timeframe. Under future SSP scenarios, all climate models evidenced a systematic shift toward higher FWI classes, particularly for the May–Oct months. The frequency of days classified at H and VH danger increased, while L and M classes decreased, with the magnitude of change generally increasing from SSP1-2.6 to SSP5-8.5. 

The comparison between historical and future SSP scenarios evidenced that the increase in H and VH fire danger conditions was substantial and dependent on the climate model. For instance, in May–Oct, under the SSP5-8.5 scenario, the MPI model simulated an increase in high FWI days from approximately 40.2% (1985–2014) to 45.6%, while very high FWI days nearly doubled from 4.5% to 8.2%. Conversely, the ACC model showed similar marked changes, with high FWI days increasing from 39.8% to 44.2%, and very high FWI days moving from 4.0% to 10.1%. ECE presented the biggest increase in the frequency of both high and very high fire danger conditions, which increased from 41.5% to 49.9% and from 4.6% to 10.8%, respectively. In all cases, low and moderate FWI classes declined, with low danger days decreasing by roughly 10% in the ECE model and only by 4.5% for MPI. These trends indicated a clear shift toward more severe fire weather conditions under future climate scenarios, particularly during the drier half of the year. 

Figure 3a shows the spatial distribution of the average FWI, calculated from the ERA5 dataset, for the 1985–2014 historical period and considering the Jan-Dec timeframe. FWI values were mostly below 10 in the northern coastal areas, as well as in the highest mountains, while an increase to 12–15 can be observed for the southern and inland parts of the island. The maps of the differences in the average annual FWI between the ACC, ECE, and MPI models and ERA5 (Fig. 3b–d) for 1985–2014 showed relatively similar spatial patterns, particularly for ECE and MPI, and differ in magnitude. Overall, if compared with ERA5, ECE and MPI generally exhibited larger and more widespread positive overestimations than ACC, particularly in central and eastern Sardinia. Conversely, FWI was under- 

```
1 3
```

**<mark>629</mark>** <mark>Page 12 of 36</mark> 

Natural Hazards (2026) 122:629 

|i                (DSR) classes (low, moderate,<br>storical (1985–2014) and future<br>2.6<br>SSP 2–4.5<br>SSP 5–8.5|58.4<br>58.8<br>14.5<br>13.7<br>23.0<br>23.3<br>4.1<br>4.1<br>23.6<br>24.8<br>22.9<br>21.4<br>45.3<br>45.6<br>8.2<br>8.2|2.6<br>SSP 2–4.5<br>SSP 5–8.5<br>69.4<br>69<br>14.6<br>15<br>9.5<br>9.5<br>6.5<br>6.5<br>40<br>39.8<br>28.3<br>28.5<br>18.8<br>18.7<br>12.9<br>12.9<br>i|i            pixel, and then calculated the|
|---|---|---|---|
|i              ty rating<br>under hi<br>SSP 1–|58.9<br>13.9<br>23.5<br>3.7<br>24.5<br>21.9<br>46.3<br>7.3|SSP 1–<br>69.4<br>14.9<br>9.9<br>5.9<br>40<br>28.8<br>19.5<br>11.7<br>i|i          for each|
|i             aily severi<br>CE, MPI)<br>MPI<br>.5<br>HIST|62.5<br>14.8<br>20.4<br>2.2<br>29.4<br>25.9<br>40.2<br>4.5|MPI<br>.5<br>HIST<br>73.6<br>14.8<br>7.8<br>3.8<br>48.1<br>28.9<br>15.4<br>7.6<br>i|i        each class|
|i          high) and by d<br>tions (ACC, E<br>4.5<br>SSP 5–8|56.6<br>12.3<br>25.7<br>5.5<br>22.1<br>17.2<br>49.9<br>10.8|4.5<br>SSP 5–8<br>65.7<br>14.4<br>11.3<br>8.6<br>33.8<br>26.9<br>22.2<br>17.1<br>i|i      belonging to|
|i       h, and very<br>model simula<br>2.6<br>SSP 2–|57.7<br>12.3<br>25.3<br>4.7<br>22.5<br>18.6<br>49.6<br>9.3|2.6<br>SSP 2–<br>67<br>14<br>11.4<br>7.6<br>35.6<br>26.8<br>22.5<br>15.2<br>i|i   tage of days|
|i      erate, hig<br>climate<br>SSP 1–|57.2<br>12.6<br>25.4<br>4.8<br>23.2<br>18.0<br>49.3<br>9.5|SSP 1–<br>66.6<br>14.4<br>11.2<br>7.8<br>35.7<br>26.9<br>22<br>15.5<br>i|i  al percen|
|i    s (low, mod<br>nalysis and<br>ECE<br>8.5<br>HIST|64.0<br>12.6<br>21.0<br>2.3<br>32.6<br>21.3<br>41.5<br>4.6|ECE<br>8.5<br>HIST<br>73.5<br>13.6<br>8.7<br>4.2<br>47.8<br>26.5<br>17.3<br>8.4<br>i|ied the annu|
|i   FWI) classe<br>on ERA5 rea<br>.5<br>SSP 5–|58.1<br>14.0<br>22.8<br>5.1<br>26.9<br>18.8<br>44.2<br>10.1|.5<br>SSP 5–<br>69.2<br>12.2<br>10.5<br>8<br>40.9<br>22.5<br>20.7<br>15.9<br>i|we quantifi|
|i ather index (<br>riods, based<br>enarios<br>.6<br>SSP 2–4|59.6<br>13.0<br>22.5<br>4.9<br>26.8<br>19.2<br>44.3<br>9.7|.6<br>SSP 2–4<br>69.9<br>11.8<br>10.6<br>7.7<br>41.2<br>22.6<br>20.9<br>15.3<br>i|DSR classes,  i|
|by fire we<br>-month pe<br>SP5-8.5 sc<br>s<br>SSP 1–2|58.8<br>14.4<br>23.2<br>3.7<br>26.4<br>21.0<br>45.3<br>7.3|s<br>SSP 1–2<br>70<br>13.6<br>10.2<br>6.2<br>41.8<br>25.7<br>20.2<br>12.2<br>i|FWI and    i|
|of days  i<br>th and 6<br>5,and S<br>e model<br>ACC<br>HIST|65.5<br>12.3<br>20.2<br>2.0<br>35.3<br>20.9<br>39.8<br>4.0|e model<br>ACC<br>HIST<br>75<br>12.8<br>8.6<br>3.7<br>50.7<br>24.9<br>17<br>7.4<br>i|days by      i|
|ency (%)    i<br>r 12-mon<br>,SSP2-4.<br>Climat<br>ERA5<br>HIST|65.1<br> <br>13.1<br>19.3<br>2.5<br>34.6<br> <br>22.3<br>38.2<br>4.9|Climat<br>ERA5<br>HIST<br>75.2<br>12.2<br>8.3<br>4.3<br>51.2<br>23.7<br>16.5<br>8.5<br>i|uency of        i|
|Relative frequ     i<br>nd very high) fo<br>2064)SSP1-2.6<br>FWI class|L (< 11.2)<br>M (11.2–21.3)<br>H (21.3–38)<br>VH (> = 38)<br>L (< 11.2)<br>M (11.2–21.3)<br>H (21.3–38)<br>VH(> = 38)|DSR class<br>L (< 5)<br>M (5–10)<br>H (10–15)<br>VH (> = 15)<br>L (< 5)<br>M (5–10)<br>H (10–15)<br>VH(> = 15)<br>i|ermine the freq         i|
|**Table 3**<br>high, a<br>(2035–<br>Period|12 M<br>6 M|Period<br>12 M<br>6 M<br>i|To det           i|



```
1 3
```

<mark>Page 13 of 36</mark> **<mark>629</mark>** 

Natural Hazards (2026) 122:629 



**Fig. 3** Average FWI maps for 1985–2014 derived from the ERA5 dataset for the 12-month **a** and 6-month **e** timeframes. Panels **b** – **d** and **f** – **h** show the corresponding differences in mean FWI between the ACC, ECE, MPI models and ERA5, for 1985–2014 

estimated with respect to ERA5 in south-western Sardinia, with values roughly ranging from − 0.5 to − 2 for MPI and ECE models, whereas in the ACC model the underestimation was more evenly distributed across the southern and western parts of the island. 

Focusing on May–Oct for the historical period, Fig. 3e presents the average FWI calculated with the ERA5 dataset. Compared to the average annual values, FWI increased substantially, exceeding 18 in wide portions of central and southern Sardinia, and peaks of 22–23 in specific southern sites. Northern and coastal areas generally presented lower values, often below 13–14. As shown in Fig. 3f–h, the differences in mean FWI between the ACC, ECE, and MPI models and ERA5 were amplified during the hottest season. In this case as well, ECE and MPI showed similar spatial patterns, with most of the study area characterized by substantial and widespread overestimations relative to ERA5, generally ranging from + 1 to + 3, particularly in eastern and central Sardinia, while underestimations of FWI, ranging from −2 to −4, persisted along the south-western coastal areas. By contrast, the ACC model exhibited smaller deviations from ERA5, with the main overestimations confined to eastern areas, and slight underestimations in southern and western Sardinia. 

Moving to future projections (2035–2064), the ACC climate model indicated a progressive rise of FWI across all scenarios for both annual and six-month analyses (Fig. 4). Average annual FWI increased of about 1.5–2 units in SSP1-2.6, expanding to 2.5–3.5 under SP5-8.5, particularly in central and southeastern interior Sardinia. The May–Oct timeframe results amplified these increasing FWI patterns: ACC projected higher wildfire danger conditions, with a positive FWI variation in the range 3.5–4.5 under SSP5-8.5, which resulted in seasonal FWI values frequently above 18–20 in the central and southern parts of the island. 

```
1 3
```

**<mark>629</mark>** <mark>Page 14 of 36</mark> 

Natural Hazards (2026) 122:629 



**Fig. 4** Maps of the average FWI for the historical period (1985–2014) under different climate models (ACC, ECE, MPI), considering 12-month and 6-month timeframes. Maps of projected changes in average FWI (2035–2064 vs. 1985–2014) across models (ACC, ECE, MPI) and Shared Socioeconomic Pathways (SSP1-2.6, SSP2-4.5, SSP5-8.5) for both timeframes are also shown 

The ECE model presented a comparable spatial structure but more marked FWI variations than ACC for the six-months timeframe (Fig. 4). In fact, according to this model, during May–Oct, FWI variations reached peaks of 4–5 above the historical values under SSP5-8.5, with seasonal FWI above 20–21 in several interior sectors. The MPI model evidenced the lowest variations in future FWI for both annual and six-month timeframes. Under SSP12.6, annual increases of FWI were largely below 1.8, while some widespread but limited increments in annual FWI were observed under SSP5-8.5. This trend was confirmed for the May–Oct timeframe: MPI projections revealed the less significant increases in FWI, with respect to ACC and ECE models, with increasing FWI values above 3 only observed in few spots located in southern and central Sardinia, under SSP2-4.5 and SSP5-8.5 scenarios. 

Moving to the Daily Severity Rating (DSR) analysis, in the historical conditions DSR values were below 5 in the most of days (73–75% on annual basis, 48–51% for May–Oct) (Table 3). During the 6-month period, as expected, the percentage of low-severity days decreased, while the other DSR classes became more frequent. High DSR days were in the range 8–9% and roughly doubled in frequency in the May–Oct timeframe compared to the full year. Very high DSR values were observed in about 4% of the days in the annual timeframe of 1985–2014, with ACC and MPI underestimating these frequencies with respect to ERA5. As observed for FWI, under future scenarios, all climate models evidenced a significant increase in average DSR and a shift towards high danger classes, which was pronounced for May–Oct. The variation in the frequency of high and very high DSR days was variable depending on the climate model. Focusing on May–Oct, the worst conditions were evidenced by ECE, for which very high DSR days moved from approximately 8.4% in the historical conditions to 17.1% under SSP5-8.5. On the contrary, the MPI model was more conservative, as the simulated increases in very high DSR days were less relevant 

```
1 3
```

<mark>Page 15 of 36</mark> **<mark>629</mark>** 

Natural Hazards (2026) 122:629 

(from 7.6% for 1985–2014 to 12.9% for 2035–2064, SSP5-8.5). The frequency of low DSR classes declined from the historical to the future scenarios, with the strongest decreasing pattern evidenced by the ECE model for both 6 and 12-month timeframes. 

### **3.3 Changes in wildfire hazard** 

Table 4, and Figs. 5 and 6 summarize the fire hazard outputs under historical (1985–2014) and future (2035–2064) climate conditions for the different climate models and SSPs. Under historical conditions (1985–2014), ACC presented fewer very high fire danger days (~ 7.4 days yr<sup>−1</sup> ) than ERA-5, but a higher average annual burned area (~ 15,400 ha yr<sup>−1</sup> ), consistent with its larger average fire size (~ 63 ha). A markedly higher annual crown fire area (1060 ha yr<sup>−1</sup> ) was also observed for ACC. ECE was closer to ERA5 in terms of days with FWI ≥ 38 (~ 8.4) and total area burned area (~ 2.4 Mha), with an average annual area burned of ~ 14,400 ha yr<sup>−1</sup> and ~ 870 ha yr<sup>−1</sup> of crown fires. MPI yielded the lowest fire hazard outputs among the models, with a total area burned of ~ 1.95 Mha, an average annual area burned of ~ 11,700 ha yr<sup>−1</sup> , and ~ 730 ha yr<sup>−1</sup> crown fire area, reflecting both less large wildfires and small average fire size (~ 43 ha). 

Overall, the annual BP for 1985–2014 was generally low over most of the island (< 0.6 ha km<sup>−2</sup> ) for both ERA5 and climate models, whereas hotspots were consistently concentrated in specific areas of southern Sardinia, where values exceeded 4 ha km<sup>−2</sup> (Fig. 5) Values of aBP ranging from 0.6 to 4 ha km<sup>−2</sup> were mostly observed nearby the hot-spot zones and in western Sardinia. The spatial configuration of the zones characterized by high aBP values was quite coherent among ERA5 and the three climate model simulations. In general terms, ACC and ECE showed a slightly larger spatial extent of intermediate and high BP classes, whereas MPI and partially also ERA5 produced more spatially constrained hotspots. CFL maps (Fig. 5) of the historical baseline exhibited a more homogeneous spatial pattern across the study area. In fact, most of Sardinia presented flame lengths below 2.5 m, with only sparse and fragmented patches exceeding 2.5 m. Areas with CFL values below 1.2 m were generally associated with areas characterized by significant presence of herbaceous surface fuels. Compared to BP, the spatial differences between ERA5 and the climate models were less pronounced and patchy in some limited areas. 

The spatial distribution of annual CFP evidenced quite low values across most of the study area for all models, with large portions classified in the < 0.05 ha km<sup>−2</sup> class, thus suggesting a relatively low annual probability of facing crown fires in forest areas (Fig. 5). The highest probabilities of crown fires were generally confined to discontinuous patches, mainly located in the southern and western sectors of the island. These areas spatially correspond to high BP zones, even if the extent of high CFP was smaller and reflected the fact that not all surface fires have the potential to turn into crown fires. Moreover, intermediate CFP classes (0.1–0.5 ha km<sup>−2</sup> ) were mostly observed as scattered transition zones around the main hotspots and did not form continuous clusters. Also in this case, ERA5 and the climate models consistently captured the main crown fire areas, and the differences among models were basically related to the spatial continuity and density of low and intermediate CFP classes. For instance, MPI evidenced more fragmented and localized patterns of high CFP than the other models. 

In future years, all climate models projected strong increases in the days with FWI ≥ 38. For ACC, days with FWI ≥ 38 increased from ~ 7.4 to ~ 18.7 under SSP5-8.5, with an evi- 

```
1 3
```

**<mark>629</mark>** <mark>Page 16 of 36</mark> 

Natural Hazards (2026) 122:629 

|and climate model data|Average annual<br>AB (ha yr−1)<br>Average FL<br>(m)<br>Average<br>annual<br>CF (ha<br>yr−1)<br>14,679.3<br>1.19<br>855.9<br>15,403.3<br>1.34<br>1,060.3|23,147.8<br>1.27<br>1,457.9|30,062.6<br>1.27<br>1,834.0|30,260.4<br>1.26<br>1,779.8|14,394.9<br>1.22<br>873.3|28,308.6<br>1.19<br>1,677.2|28,838.8<br>1.20<br>1,691.5|33,584.7<br>1.21<br>2,021.1|11,662.8<br>1.22<br>726.7|17,236.4<br>1.16<br>923.1|20,463.3<br>1.17<br>1,087.9<br>19,104.3<br>1.15<br>1,018.3<br>i   ut, the total simulated area burned, the averag<br>i                 i rrence, for the reference period (1985–2014) an|
|---|---|---|---|---|---|---|---|---|---|---|---|
|ie hazard indicators derived from wildfire spread simulations|Total wildfire<br>footprints<br>Total simulated<br>AB (Mha)<br>Average simu-<br>lated FS (ha)<br>50,000<br>2.457<br>49.1<br>40,965<br>2.578<br>62.9|74,390<br>3.874<br>52.1|98,559<br>5.031<br>51.1|103,381<br>5.064<br>49.0|46,674<br>2.409<br>51.6|96,951<br>4.737<br>48.9|95,344<br>4.826<br>50.6|110,421<br>5.620<br>50.9|45,565<br>1.952<br>42.8|74,723<br>2.884<br>38.6|83,315<br>3.425<br>41.1<br>83,481<br>3.197<br>38.3<br>ays with FWI ≥ 38, the total wildfire simulations carried o<br>i         ge annual hectares of land characterized by crown fire occu<br>climate models under diverse SSP scenarios|
|ed(2035–2064)wildfir     i|Avg. days with<br>FWI ≥ 38 (# yr−1)<br>9.02<br>7.39|13.42|17.78|18.65|8.42|17.49|17.20|19.92|8.22|13.48|15.03<br>15.06<br>e annual number of d       i<br>i      burned, and the avera        i<br>d ACC, ECE and MPI|
|1985–2014)andproject|Model<br>ERA5<br>ACC|ACC–SSP1-2.6|ACC–SSP2-4.5|ACC–SSP5-8.5|ECE|ECE–SSP1-2.6|ECE–SSP2-4.5|ECE–SSP5-8.5|MPI|MPI–SSP1-2.6|MPI–SSP2-4.5<br>MPI–SSP5-8.5<br>zes the expected averag           i<br>i  the average annual area            i<br>–2064) using ERA5 an|
|**Table 4**Historical(|Reference years<br>1985–2014<br>1985–2014|2035–2064|2035–2064|2035–2064|1985–2014|2035–2064|2035–2064|2035–2064|1985–2014|2035–2064|2035–2064<br>2035–2064<br>The table summari              i<br>simulated fire size,                i<br>future period (2035|



```
1 3
```

<mark>Page 17 of 36</mark> **<mark>629</mark>** 

Natural Hazards (2026) 122:629 



**Fig. 5** Maps of average annual burn probability (BP), conditional flame length (CFL), and average annual crown fire probability (CFP) over the period 1985–2014 derived from the fire spread model simulations, considering data from ERA5 reanalysis and ACC, ECE, and MPI climate models 

dent growth related to the radiative forcing. The average annual area burned nearly doubled, reaching ~ 23,100 ha yr<sup>−1</sup> under SSP1-2.6 and exceeding 30,000 ha yr<sup>−1</sup> under the two higher-emission scenarios. Crown fire area followed a similar rising pattern and increased from ~ 1060 ha yr<sup>−1</sup> (1985–2014) to ~ 1800 ha yr<sup>−1</sup> under SSP2-4.5 and SSP5-8.5. It is interesting to evidence that the future average fire size decreased with respect to the historical ACC value (~ 63 ha), and was in the range 49–52 ha. 

```
1 3
```

**<mark>629</mark>** <mark>Page 18 of 36</mark> 

Natural Hazards (2026) 122:629 



**Fig. 6** Maps of projected annual burn probability (BP) and annual crown fire probability (CFP) for the period 2035–2064 under three emission scenarios (SSP1-2.6, SSP2-4.5, SSP5-8.5) and three climate models (ACC, ECE, MPI) 

ECE also exhibited a significant amplification of fire hazard outputs in future years. Very high fire danger days moved from ~ 8.4 of 1985–2014 to ~ 19.9 under SSP5-8.5. ECE displayed a relevant rise in the average annual area burned, which expanded from ~ 14,400 ha yr<sup>−1</sup> of the historical conditions to ~ 28,310 ha yr<sup>−1</sup> (SSP1-2.6) and up to ~ 33,590 ha yr<sup>−1</sup> (SSP58.5). Crown fire area also grew substantially, reaching ~ 2020 ha yr<sup>−1</sup> under SSP5-8.5. The average future fire size remained relatively stable across SSP scenarios (49–51 ha), and for this model the differences with respect to the 1985–2014 average values were limited. 

MPI outputs evidenced more moderate increases compared to ACC and ECE. Days with FWI ≥ 38 moved from ~ 8.2 to about 15 under both SSP2-4.5 and SSP5-8.5. The total simulated area burned peaked at ~ 3.43 Mha under SSP2-4.5 but slightly decreased to ~ 3.20 Mha under SSP5-8.5. The average annual area burned increased from ~ 11,660 ha yr<sup>−1</sup> (1985–2014) to ~ 20,460 ha yr<sup>−1</sup> under SSP2-4.5, and then declined to ~ 19,100 ha yr<sup>−1</sup> under SSP5-8.5. Crown fire area showed a similar pattern, rising from ~ 730 ha yr<sup>−1</sup> (1985–2014) to ~ 1090 ha yr<sup>−1</sup> under SSP2-4.5, and then decreasing to ~ 1020 ha yr<sup>−1</sup> under SSP5-8.5. A general increase in future aBP, in both magnitude and spatial extent, was evident across all models and scenarios relative to the historical baseline (1985–2014) (Figs. 5 and 6). Under the SSP1-2.6 scenario, the most relevant BP areas remained largely concentrated in southern Sardinia, but intermediate classes (0.6–1.2 and 1.2–4 ha km<sup>−2</sup> ) expanded across many portions of the region, remarkably in ACC and ECE models. Increases of aBP were generally lower than 1 ha km<sup>−2</sup> and mostly concentrated in the southern and western parts of Sardinia. Moving to SSP2-4.5, the shift to higher BP classes became more pronounced, with a significant growth of southern hotspots and a broader amplification of high aBP classes toward the 

```
1 3
```

<mark>Page 19 of 36</mark> **<mark>629</mark>** 

Natural Hazards (2026) 122:629 

interior and western areas. Widespread increases of aBP above 2–10 ha km<sup>−2</sup> were observed especially in ACC and ECE models. Under SSP5-8.5, this pattern was further more evident, particularly for ECE; in addition, much of the island shifted toward higher aBP levels. In broad terms, ACC and ECE simulated higher and more widespread aBP values than MPI, which maintained more limited hotspots and presented quite small variations for northern and eastern Sardinia. ACC and ECE exhibited localized peaks of aBP variation above 10 ha km<sup>−2</sup> , particularly in the main hotspot area of southern Sardinia. 

Moving to annual crown fire probability (aCFP) (Fig. 6), the projected changes for 2035– 2064 were more spatially heterogeneous but showed a similar pattern of intensification. Under the SSP1-2.6 scenario, most of Sardinia was characterized by the lowest annual class (< 0.05 ha km<sup>−2</sup> ), with higher aCFP values mainly observed in the south. Under SSP2-4.5 and SSP5-8.5 scenarios, aCFP moderate classes became slightly more frequent, and some areas reached higher aCFP values (1.5–8.5 ha km<sup>−2</sup> ); values above 8.5 ha km<sup>−2</sup> appeared in southern Sardinia. For these scenarios, ACC and ECE evidenced the most relevant increase in aCFP, even exceeding + 5 ha km<sup>−2</sup> in some parts of southern and western Sardinia. 

## **4 Discussion** 

This study aims to improve the understanding and quantification of the potential impacts of future climate change on wildfire danger and hazard in the Mediterranean Basin by combining wildfire danger modelling with a mechanistic wildfire spread modelling framework (Fig. 1). Within the Mediterranean Basin context, the proposed approach represents one of the relatively few applications combining high spatial resolution (150 m) wildfire spread simulations with climate change projections over a large study area (about 24,000 km<sup>2</sup> ) to explore future wildfire conditions. 

To isolate the potential effects of climate change on wildfire hazard and reduce uncertainties associated with possible future land-use changes and related variations in surface and crown fuel characteristics (e.g., fuel load, structure), the fuel layers were kept constant in all wildfire spread model simulations for future periods. Similarly, fire ignition patterns were assumed to remain unchanged for the future years (2035–2064), using the historical ignition probability grids derived for the period 2003–2022 as a fixed reference input in the modelling framework. This approach, commonly adopted in climate–fire spread modelling studies to isolate the role of climatic drivers, has been widely used in previous research (Moritz et al. 2012; Riley and Loehman 2016; Lozano et al. 2017; Dye et al. 2023). Conversely, wildfire danger models such as FWI and DSR, adopted in this work, are only driven by weather inputs and can account only for future climate as they do not account for fuels or fire ignitions. While holding fuels as constant layer is a common and defensible modeling assumption, it also constitutes a potential constraint, as fuel structure and continuity are inherently dynamic and influenced by the interplay of climate, land-use change, and disturbance regimes, including wildfires. Assuming a static landscape over the 2035–2064 period may therefore lead to over- or underestimation of future wildfire hazard. The direction of this bias remains uncertain: land abandonment could increase fuel accumulation and connectivity, thereby amplifying the climate-driven increase in hazard beyond that projected here, whereas more frequent wildfire activity may reduce fuel availability, leading to fuel-limited systems and other feedbacks not captured by the current modeling framework. Future work 

```
1 3
```

**<mark>629</mark>** <mark>Page 20 of 36</mark> 

Natural Hazards (2026) 122:629 

will integrate dynamic vegetation and land-use processes (such as landscape succession and disturbance feedbacks) into wildfire modeling frameworks to better constrain projections and reduce structural uncertainties (Ager et al. 2022; Prichard et al. 2023). As highlighted by Chuvieco et al. (2023), future wildfire risk emerges from the combination of wildfire hazard, exposure of people and assets, ecosystem vulnerability, and management capacity. The assumptions adopted in this study concern only the climate-driven component of future wildfire hazard, whereas wildfire risk is also influenced by ecological and socio-economic factors, which in other words mean that future changes in land use and fuels, demographic trends, governance, exposed values, and the capacity of societies to prevent, suppress, and recover from wildfire events may either amplify or mitigate the projected impacts Chuvieco et al. 2023; Preinfalk and Handmer 2024). 

The three downscaled climate models (ACC, ECE and MPI) reproduced reasonably well the main historical climatic variables and spatial patterns, as well as fire weather conditions. In fact, the spatial differences between wetter zones of central-northern Sardinia and drier southern areas were consistently captured, and deviations from ERA5 remained mostly limited. This provided a coherent baseline from which to interpret projected future changes. Notably, considering the period 1985–2014, ECE and MPI tended to show slightly higher FWI values than ERA5 in central–eastern Sardinia, while ACC exhibited weaker but more spatially distributed differences. Future projections (2035–2064) indicated a consistent signal across models toward warmer and drier conditions, with ECE generally projecting the strongest increases and MPI the most limited responses. The strongest warming signals were observed for the May–October period. 

A large number of previous works on future climate projections indicated a likely increase in temperatures and dry conditions, especially over arid regions like the southern part of Europe (i.e.: Barcikowska et al. 2020; Ruffault et al. 2020; IPCC 2022; Lazoglou et al. 2024; Crapart et al. 2026). For instance, regarding maximum temperatures, in line with previous works carried out in Mediterranean areas (Seker and Gumus 2022; Daher and Kirtman 2025), we observed an increase under all SSP scenarios, with an evident rise from SSP1-2.6 to SSP5-8.5, stronger during the May–October period than at the annual scale. The fact that summer warming would likely exceed the global annual warming pattern in Southern Europe was also evidenced in previous works (IPCC 2021; Cos et al. 2022). Furthermore, we highlighted a general reduction of precipitations by 2035–2064, particularly at the semestral scale (e.g.: -19% for MPI and ECE, under SSP1-2.6 and SSP2-4.5): several studies have reported consistent patterns under future climate change scenarios for Southern Europe (Giorgi et al. 2019; Steensen et al. 2026). 

The combination of higher maximum temperatures, lower cumulated precipitation, and the reduction in the number of rainy days (> 1 mm) suggested a potential increase in heatwave length and frequency, as well as a likely lengthening of future fire seasons, as evidenced by previous works (i.e.: Dupuy et al. 2020; El Garroussi et al. 2024; Rovitakis et al _._ 2025; Sutanto et al. 2025). Moreover, previous works (El Garroussi et al. 2024; Feng et al. 2025) pointed out that the projected increase in very high FWI days was primarily associated with a higher occurrence of low- and moderate-wind classes, suggesting that rising temperatures and reduced precipitation, rather than changes in strong or extreme winds, are likely to be the dominant drivers of the intensification of fire risk conditions. This pattern was also observed in our simulations, where wind projections remained relatively stable across the three climate models. These shifts promoted a redistribution of fire danger 

```
1 3
```

<mark>Page 21 of 36</mark> **<mark>629</mark>** 

Natural Hazards (2026) 122:629 

towards higher FWI and DSR classes, which was amplified under higher-emission SSP scenarios, especially during May–October. The increase in the occurrence of days with very high fire danger conditions (FWI > 38), especially under high-emission SSPs, is consistent with several previous works (e.g.: Cardoso Pereira et al.2024; Kostopoulou and Stavridis 2025). 

Wildfire spread simulation outputs confirmed the signals coming from climatic variables and danger conditions: as days with FWI ≥ 38 increased, the average annual BP, the average annual area burned, and the crown fire area grew consequently. However, the increase of average BP and CFP was not spatially uniform, while CFL value differences were relatively small in most of the island, even under the worst scenarios. ACC and ECE models generally simulated a more intense growth of hotspots and area burned compared to MPI, and this was due to the inherent differences among climate models in projected future data. Hotspot areas, historically concentrated in southern Sardinia, expanded in magnitude and extent, with the strongest growth observed for inland and western areas under SSP2-4.5 and SSP5-8.5. The pronounced increase in wildfire danger and hazard projected for interior and western Sardinia could further intensify risk conditions in areas already considered highly fire-prone (e.g.: Salis et al. 2021). In fact, the western sectors of northern and central Sardinia currently represent some of the zones most affected by large wildfire events (e.g., Montiferru in 2021; Bonorva and Suni in 2009): these large wildfires typically occur under specific fire-weather conditions, characterized by intense heatwaves and southern winds, which significantly boost wildfire spread and intensity (Salis et al. 2021; Scarpa et al. 2024). Previous studies showed that inland Mediterranean regions could face similar patterns under future climate change, due to a reduced marine moderation effect and stronger land–atmosphere feedbacks (Giorgi and Lionello 2008; Somot et al. 2016; Cos et al. 2022). 

Our fire spread modeling simulations evidenced that the average flame length, as well as the average fire size, did not show a consistent increase moving from historical to future periods. This result may be explained by the use of fixed fuel input layers for future years, as well as with the increase in the relative percentage of days characterized by low and moderate wind speed, and a decrease in the occurrence of strong winds, in the 2035–2064 years. Similar findings have been reported for Southern Europe by previous modeling studies, which evidenced that future climate-driven changes in wildfire behavior are often heterogeneous and that future wildfire regimes may be shaped more by shifts in the frequency of favorable fire-weather conditions than by substantial increases in fire intensity (Lozano et al. 2017; Aparicio et al. 2022; Rovithakis et al. 2025). 

Our results indicate that increases in Fire Weather Index (FWI) values do not necessarily translate into proportional increases in average flame length, average fire size, or other wildfire hazard indicators. This emphasizes the role played by stochastic wildfire spread modeling in understanding current and future wildfire dynamics: burn probability modeling reflects the integrated influence of weather, ignitions, fuels, and landscape connectivity, and therefore provides a more realistic estimate of where wildfire exposure is likely to increase. In fact, high FWI reflects favorable weather conditions for fire activity, but large wildfires only occur when an ignition takes place, the fire escapes initial suppression and spread is sustained across the landscape. Thus, extreme fire weather is necessary for large wildfire occurrence, but it is not sufficient by itself. Many studies rely on projected maps of FWI or other indices and implicitly equate them with future wildfire risk and areas burned (e.g.: Bedia et al. 2015; Khabarov et al 2016 119; He et al. 2025). However, weather is only one 

```
1 3
```

**<mark>629</mark>** <mark>Page 22 of 36</mark> 

Natural Hazards (2026) 122:629 

of the drivers of wildfire activity and should be treated as an input to the model, not as a direct measure of exposure or risk. This is also consistent with recent integrated wildfire risk frameworks (Chuvieco et al. 2023), which emphasize that wildfire danger indices describe only one component of wildfire risk. 

Even if future climate model projections were characterized by differences in magnitude and spatial patterns, the overall tendency toward increased wildfire impacts and risk has important implications for fire and land management in Sardinia and, more broadly, across Mediterranean landscapes. These results support the adoption of proactive and integrated wildfire risk management strategies rather than suppression-oriented visions (Chuvieco et al. 2023; Arango et al. 2024). In particular, landscape-scale fuel management actions, including fuel treatments, grazing, prescribed burning, and the promotion of heterogeneous land-use mosaics, may contribute to limit wildfire spread potential and areas burned in future years (Alcasena et al. 2019; Duane et al. 2019; Pais et al. 2023; Pulido et al. 2023). In addition, recent analyses of wildfire risk under the SSP framework further evidence that future wildfire trajectories will also depend on socio-economic development pathways: changes in rural abandonment, agricultural practices, urban expansion into fire-prone landscapes, demographic dynamics, governance capacity, and investments in prevention and suppression may substantially modify future wildfire risk, even under similar climatic conditions (Preinfalk and Handmer 2024). Consequently, climate adaptation strategies should be coupled with land-use planning and long-term socio-economic policies to effectively reduce future wildfire risk. 

The potential expansion of fire-prone areas also advocates that wildfire risk considerations should be progressively integrated into adequate spatial planning and objective land management policies, especially in Mediterranean regions where recent socio-economic and land-use changes have promoted fuel accumulation and increased landscape flammability (e.g., Pausas and Fernandez-Munoz 2012; Salis et al. 2022). In this context, growing attention should be devoted to the promotion of fire-resilient landscapes, which aims to design and manage landscapes able to reduce large and severe wildfire likelihood while maintaining ecological processes and ecosystem services (Viegas et al. 2024; Perez-Izquierdo et al _._ 2025; Regos 2025). Addressing these challenges will require coordinated strategies combining fuel management, land-use planning, improved governance collaborations and frameworks, community preparedness, and adaptive socio-economic policies capable of increasing landscape and societal resilience under future climate and development pathways. (Palaiologou et al. 2020; Chuvieco et al. 2023; Viegas et al. 2024; ESABCC 2026). 

## **5 Conclusions** 

This study combined fire danger indices with high-resolution wildfire spread simulations to assess the potential effects of future climate change on wildfire hazard and danger in Sardinia under multiple climate models and SSP scenarios. The proposed methodological framework can be easily extended to additional climate models and projections, alternative scenarios, different temporal windows, and other geographic contexts. Despite differences among climate projections in terms of magnitude and spatial patterns, all climate models pointed to warmer and drier conditions for Sardinia, accompanied by an increase in fire danger, burn probability, annual burned area, and crown fire activity, particularly during the 

```
1 3
```

<mark>Page 23 of 36</mark> **<mark>629</mark>** 

Natural Hazards (2026) 122:629 

May–October period. The strongest increases were generally projected under the higheremission scenarios. Another relevant outcome was that increases in fire danger were not systematically associated with proportional changes in simulated wildfire behavior metrics, thus reinforcing the value of combining climate-based fire danger indices with stochastic wildfire spread simulations when assessing future wildfire conditions. As with any climate impact assessment, the projections remain affected by uncertainties associated with climate models and assumptions on future fuels, ignitions, and socio-economic features. Our results provide a quantitative basis for supporting long-term wildfire management and climate adaptation planning in fire-prone mediterranean landscapes. 

## **Appendix** 

### **Changes in climate variables** 

As presented in Table 5, considering the average maximum temperature for the historical baseline (1985–2014), the three downscaled climate models (ACC, ECE, MPI) evidence very small differences (lower than 0.08 °C) with respect to ERA5 reanalysis for both the annual (19.54 °C) and the May–October values (25.42 °C). The maps of the historical average Tmax shows that, in both the 12-month and 6-month periods, low values are mainly observed in the Sardinia mountainous areas, while the highest values are concentrated along the coastal and southern areas (Fig. 7). 

In future periods, under all SSP scenarios, the downscaled models project a strong increase in maximum temperatures with respect to the historical period, as well as moving from SSP1-2.6 to SSP5-8.5. For instance, projected increases for the annual Tmax range between + 1.34 °C and + 3.27 °C across models and scenarios. MPI presents the lowest variations, with a peak of + 1.66 °C (SSP5-8.5). ACC and ECE outputs simulate substantially larger increases in Tmax, reaching + 3.18 °C and + 3.27 °C, respectively, under SSP5-8.5. For the May–Oct period, Tmax increases are still relevant and higher than the annual values, ranging from + 1.62 °C to + 3.85 °C. ACC evidences the strongest Tmax increases for SSP12.6 and SSP2-4.5 (+ 2.80 °C and + 3.43 °C, respectively), while ECE exhibits the highest Tmax value (29.31 °C) under SSP5-8.5. Also in this case, MPI remains more conservative and shows a comparatively limited variation among scenarios. In general terms, from a spatial point of view, the most pronounced temperature increases with respect to 1985–2014 are projected for interior and western Sardinia, even if magnitude and spatial differences vary among the climate models (Fig. 7). For instance, for both Jan-Dec and May–Oct periods, ACC and ECE outputs evidence a more pronounced and quite spatially homogeneous warming, whereas the MPI model projects a more moderate increase in Tmax, which broadly follows a southwest-northeast gradient, with the less relevant variations in eastern Sardinia. 

Regarding precipitation, according to ERA5 the average annual value of the period 1985–2014 amounts to ≈533 mm with ≈100 days above 1 mm of rain, while the May–Oct average is ≈168 mm (≈33 days above 1 mm of rain) (Table 5). The three climate models slightly overestimate the annual precipitation with respect to ERA5 (from + 18.65 mm of MPI to + 28.96 mm for ECE); in terms of days with more than 1 mm of rain, only downscaled MPI slightly underestimates the annual frequency (≈96 days), while downscaled 

```
1 3
```

**<mark>629</mark>** <mark>Page 24 of 36</mark> 

Natural Hazards (2026) 122:629 

**Table 5** Average Tmax (°C), average cumulated precipitation (mm), and number of days with average precipitation above 1 mm (RD > 1 mm) for the annual timeframe and the May–October period in Sardinia as derived from ERA5 and three climate models (ACC, ECE, MPI) over 1985–2014, and corresponding projections for 2035–2064 under SSP1-2.6, SSP2-4.5, and SSP5-8.5 scenarios 

|Model|Reference<br>years|Tmax<br>(12 months)|Tmax<br>(6 months)|Prec<br>(12 months)|Prec<br>(6 months)|RD > 1 mm<br>(12 months)|RD > 1 mm<br>(6 months)|
|---|---|---|---|---|---|---|---|
|ERA5|1985–<br>2014|19.54|25.42|532.65|168.22|99.50|33.30|
|ACC|1985–<br>2014|19.57|25.50|554.71|201.03|99.84|36.67|
|ACC<br>SSP1-2.6|2035–<br>2064|22.32|28.30|494.84|148.27|89.50|31.07|
|ACC<br>SSP2-4.5|2035–<br>2064|22.74|28.80|492.99|161.48|88.64|30.53|
|ACC<br>SSP5-8.5|2035–<br>2064|22.75|28.93|485.92|167.82|82.87|28.50|
|ECE|1985–<br>2014|19.59|25.46|561.61|169.40|98.70|29.43|
|ECE<br>SSP1-2.6|2035–<br>2064|21.87|28.15|531.60|136.39|91.50|22.70|
|ECE<br>SSP2-4.5|2035–<br>2064|22.11|28.53|530.75|137.34|90.90|21.97|
|ECE<br>SSP5-8.5|2035–<br>2064|22.86|29.31|515.98|145.88|85.30|21.70|
|MPI|1985–<br>2014|19.58|25.44|551.30|155.61|95.81|27.50|
|MPI<br>SSP1-2.6|2035–<br>2064|20.92|27.06|525.85|135.60|94.43|25.20|
|MPI<br>SSP2-4.5|2035–<br>2064|21.11|27.10|514.48|135.82|91.60|24.17|
|MPI<br>SSP5-8.5|2035–<br>2064|21.24|27.41|511.53|143.82|90.63|23.83|



ACC and ECE outputs are very similar to ERA5. Overall, the climate models present spatial patterns of precipitations similar to ERA5, as presented in Fig. 8: the most significant precipitation values are concentrated in the central and northern sectors of the island, while the lowest values are concentrated in southern Sardinia. 

Focusing on the May–Oct period, model projections differ more significantly. Downscaled ECE is close to ERA5 average values (+ 1.18 mm), whereas ACC overestimates precipitation of ≈20% (+ 32.81 mm; + 19.5%) as well as the days above 1 mm of rain (≈37 vs ≈33 days) with respect to ERA5. Both ECE (≈29 days) and MPI (≈28 days) underestimate the occurrence of days with precipitations above 1 mm. The spatial distribution of precipitations exhibits a more homogeneous pattern compared to the 12-month period, even if the gradient between north and south remains (Fig. 8). Differences among ERA5 and climate models are relatively limited, with ACC showing higher precipitation values in central and northern areas. 

A general reduction tendency in future precipitations emerges in all models for 2035– 2064, for both annual and May–Oct values (Table 5). At the annual scale, downscaled ACC evidences the strongest decrease in precipitations, with variations of ≈60–70 mm under all SSP scenarios with respect to 1985–2014. ECE displays a more gradual variation, with decreasing precipitations moving from SSP1-2.6 (≈532 mm) to SSP5-8.5 (≈516 mm). 

```
1 3
```

<mark>Page 25 of 36</mark> **<mark>629</mark>** 

Natural Hazards (2026) 122:629 



**Fig. 7** Maps of average maximum temperature (Tmax) in Sardinia. The historical baseline (1985–2014) Tmax for 12- and 6-month periods, derived from ERA5 reanalysis and three downscaled climate models (ACC, ECE, MPI), is presented in ( **a** – **h** ). The maps of projected absolute difference in average Tmax between the future period (2035–2064, SSP5-8.5 scenario) and the historical baseline, for each climate model and considering 12- and 6-months (May-Oct) periods, are also provided ( **i–n** ) 

```
1 3
```

**<mark>629</mark>** <mark>Page 26 of 36</mark> 

Natural Hazards (2026) 122:629 



**Fig. 8** Maps of average precipitations (PP) in Sardinia. The historical baseline (1985–2014) PP for 12and 6-month periods, derived from ERA5 reanalysis and three climate models (ACC, ECE, MPI), is presented in ( **a** – **h** ). The maps of projected absolute difference in average PP between the future period (2035–2064, SSP5-8.5 scenario) and the historical baseline, for each climate model and considering 12and 6-months periods, are also provided ( **i** – **n** ) 

```
1 3
```

<mark>Page 27 of 36</mark> **<mark>629</mark>** 

Natural Hazards (2026) 122:629 

MPI exhibits a similar but less relevant reduction pattern, with the maximum difference (-40 mm) between historical period and 2035–2064 values observed under SSP5-8.5. The most relevant decrease in precipitation is projected in western and central Sardinia (Fig. 8): in these areas, under SSP5-8.5, reductions in precipitations with respect to the historical baseline exceed 50 mm and locally reach values above 90 mm, particularly with ACC for north-western Sardinia. 

Regarding May–Oct, for all climate models, precipitation reaches the minimum values under SSP1-2.6, followed by a progressive increase under SSP2-4.5 and SSP5-8.5. Despite this, projected future precipitations are below the historical baseline for all models. In ACC, for instance, precipitation decreases from ≈201 mm in the historical period to ≈148 mm under SSP1-2.6, with a maximum up to ≈168 mm under SSP5-8.5. The less relevant differences between historical and future periods were observed for downscaled MPI: this model projects a reduction from ≈156 mm (1985–2014) to ≈136 mm (under SSP1-2.6 and SSP2-4.5), and again a partial increase under SSP5-8.5 (≈144 mm). For the 6-month period, projected variations in average precipitation are mostly confined to limited values, with the strongest reductions concentrated in the western sector, and observed with ACC, as presented in Fig. 8 considering the SSP5-8.5 scenario. 

All models and scenarios indicate a decrease in the number of rainy days (> 1 mm) by 2035–2064, both annually and during the May–Oct period. The pattern of frequency reduction of rainy-days (> 1 mm) is stable across scenarios, with progressively fewer rainy days from SSP1-2.6 to SSP5-8.5. At the annual scale, ACC shows the strongest difference between historical and future period (− 17% under SSP5-8.5), while downscaled MPI exhibits the less relevant variation (− 5 days under SSP5-8.5). During May–Oct, the reduction in the days with more than 1 mm of rain with respect to 1985–2014 is more pronounced in relative terms, with ECE showing the largest decrease (− s26% under SSP5-8.5) and MPI the less important decrease (− 13% under SSP5-8.5). 

We then evaluated the average wind speed conditions on days with FWI ≥ 38, for both 1985–2014 and 2035–2064, considering ERA5 and the downscaled ACC, ECE, and MPI models, and the data from three representative fire-prone areas of the island (Table 6). 

In the 1985–2014 timeframe, the average annual number of days at very high fire danger conditions is relatively limited in ERA5 (13.1 days yr<sup>−1</sup> ) and the models (14.5 days and 13.2 in ECE and MPI, with a slight overestimation with respect to ERA5, and 11.0 days in ACC). The lowest wind speed class (0–10 kph) accounts for the largest contribution in all datasets, with values ranging from a minimum of 8.3 days for ACC to 10.9 days for MPI. The discrepancies between climate models and ERA5 are mainly concentrated in the other wind speed classes, particularly for the 10–20 kph one. The > 20 kph wind speed class contributes less than one day per year in the historical simulations, with negligible values for MPI. 

In future years, the number of days with FWI ≥ 38 increases, but the variations are dependent on model and emission scenario. ECE shows the most relevant increase with respect to the historical values, moving from SSP1-2.6 (+ 14.9 days) to SSP5-8.5 (+ 19.7 days). The variation is mostly characterized by an increase in days with low wind speeds, while moderate winds (10–20 kph) increase from 4.6 days to 10.2 days; ACC also rises in all future scenarios for the highest wind speed class. ACC exhibits a similar but more moderate pattern than ECE: also in this case, the days with 0–10 kph and 10–20 kph wind speed evidence the main increases, whereas the > 20 kph class remains nearly unchanged. MPI projects smaller and less clear variations depending on SSP scenarios: the most of days 

```
1 3
```

**<mark>629</mark>** <mark>Page 28 of 36</mark> 

Natural Hazards (2026) 122:629 

||SSP 1–2.6<br>SSP 2–4.5<br>SSP 5–8.5|17.3<br>18.3<br>19.4|3.3<br>4.7<br>4.1|0.1<br>0.1<br>0.0|20.7<br>23.1<br>23.5|
|---|---|---|---|---|---|
|MPI|HIST|10.9|2.3|0.0|13.2|
||SSP 5–8.5|23.1|10.2|0.9|34.2|
||SSP 1–2.6<br>SSP 2–4.5|20.5<br>20.7|8.3<br>8.7|0.6<br>0.7|29.4<br>30.1|
|ECE|HIST|9.6|4.6|0.3|14.5|
||SSP 2–4.5<br>SSP 5–8.5|19.4<br>21.9|6.0<br>5.8|1.3<br>1.1|26.7<br>28.8|
||SSP 1–2.6|15.7|3.9|1.2|20.8|
|rios<br>models<br>ACC|HIST|8.3|2.0|0.6|11.0|
|ena<br>te<br>5||||||
|sc<br>ima<br>RA|IST|3|5|4|.1|
|8.5<br>Cl<br>E|H|9.|3.|0.|13|
|d SSP5-<br> <br> peed<br>||ph<br>|kph<br>|ph<br>||
|an<br>nd s||0 k|20|0 k|al|
|4.5,<br>Wi||0–1|10–|> 2|Tot|



```
1 3
```

<mark>Page 29 of 36</mark> **<mark>629</mark>** 

Natural Hazards (2026) 122:629 

with FWI ≥ 38 is categorized in the 0–10 kph class, which increases from 17.3 days under SSP1-2.6; to 19.4 days under SSP5-8.5. Days with wind speed above 20 kph are negligible. 

**Acknowledgements** This work was carried out in the framework of the following projects: the FirEUrisk Project (Grant agreement ID: 101003890), funded by the EU under the “H2020-EU.3.5.—SOCIETAL CHALLENGES—Climate action, Environment, Resource Efficiency and Raw Materials” Programme; the CRITERIA Project (grant no. B53D23029500001), funded by the Italian Ministry of Education, University and Research (MIUR) under the EU Next Generation Program (PNRR – PRIN); the FIRE-ADAPT Project (grant no. 101086416), funded by the EU Marie Skłodowska-Curie Action; the MED-Star2 (grant no. B83C24005570007) Project, funded by the EU under the cross-border “Programma Italia–Francia Marittimo” 2021–2027. The authors thank Stefano Arrizza, Pierpaolo Masia and Leonarda Fadda for managing the huge datasets of climate, danger and hazard modeling inputs and outputs. 

**Author contributions** Conceptualization (MS; LDG; BA); Data curation (LDG; CS; GP; RJ; RM; JR; LT; CP; BA); Formal analysis (MS; LDG; RM; JR; LT; CP; BA); Funding acquisition (MS; VB; PD; BA); Methodology (MS; LDG; VB; GP; FA-U; JR; BA); Supervision (PD; BA); Validation (VB; GP; FA-U; RJ); Visualization (CS; RJ; BA); Writing—original draft (MS; LDG); Writing—review and editing (MS; LDG; FA-U; VB; GP). 

**Funding** Open access funding provided by Consiglio Nazionale Delle Ricerche (CNR) within the CRUICARE Agreement. This work was carried out in the framework of the following projects: the FirEUrisk Project (Grant agreement ID: 101003890), funded by the EU under the “H2020-EU.3.5.—SOCIETAL CHALLENGES—Climate action, Environment, Resource Efficiency and Raw Materials” Programme; the CRITERIA Project (grant no. B53D23029500001), funded by the Italian Ministry of Education, University and Research (MIUR) under the EU Next Generation Program (PNRR – PRIN); the FIRE-ADAPT Project (grant no. 101086416), funded by the EU Marie Skłodowska-Curie Action; the MED-Star2 (grant no. B83C24005570007) Project, funded by the EU under the cross-border “Programma Italia–Francia Marittimo” 2021–2027. 

### **Declarations** 

**Conflict of interest** The authors have no relevant financial or non-financial interests to disclose. 

**Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/. 

## **References** 

> Abatzoglou JT, Juang CS, Williams AP, Kolden CA, Westerling AL (2021) Increasing synchronous fire danger in forests of the western United States. Geophys Res Lett 48:e2020GL091377.  h t t p s : / / d o i . o r g / 1 0 . 1 0 2 9 / 2 0 2 0 G L 0 9 1 3 7 7 

> Ager AA, Vaillant NM, Finney MA (2011) Integrating fire behavior models and geospatial analysis for wildland fire risk assessment and fuel management planning. J Combust 2011:572452.  h t t p s : / / d o i . o r g / 1 0 . 1 1 5 5 / 2 0 1 1 / 5 7 2 4 5 2 

> Ager AA, Preisler H, Arca B, Spano D, Salis M (2014) Wildfire risk estimation in the Mediterranean area. Environmetrics 25(6):384–396. https://doi.org/10.1002/env.2269 

> Ager AA, Evers CR, Day MA, Preisler HK, Barros AMG, Nielsen-Pincus M (2017) Network analysis of wildfire transmission and implications for risk governance. PLoS ONE 12:e0172867.  h t t p s : / / d o i . o r g / 1 0 . 1 3 7 1 / j o u r n a l . p o n e . 0 1 7 2 8 6 7 

```
1 3
```

**<mark>629</mark>** <mark>Page 30 of 36</mark> 

Natural Hazards (2026) 122:629 

- Ager AA, Barros AMG, Day MA (2022) Contrasting effects of future wildfire and forest management scenarios on a fire excluded western US landscape. Landsc Ecol 37:1091–1112.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 9 8 0 - 0 2 2 - 0 1 4 1 4 - y 

- Alcasena FJ, Vega-Garcia C, Ager A, Salis M, Nauslar N, Mendizabal F, Castell R (2019) Forest fire risk assessment and multifunctional fuel treatment prioritization methods in Mediterranean landscapes. Cuadernos De Investigación Geográfica 45(2):571–600. https://doi.org/10.18172/cig.3716 

- Alcasena F, Ager A, Le Page Y, Bessa P, Loureiro C, Oliveira T (2021) Assessing wildfire exposure to communities and protected areas in Portugal. Fire 4(4):82. https://doi.org/10.3390/fire4040082 

- Alvarez A, Lecina-Diaz J, Batllori E, Duane A, Brotons L, Retana J (2024) Spatiotemporal patterns and drivers of extreme fire severity in Spain for the period 1985–2018. Agric for Meteorol 358:110185.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . a g r f o r m e t . 2 0 2 4 . 1 1 0 1 8 5 

- Anderson HE (1982) Aids to determining fuel models for estimating fire behavior. US Department of Agriculture, Forest Service, General Technical Report INT-122, https://doi.org/10.2737/INT-GTR-122 

- Aparicio BA, Santos JA, Freitas TR, Sa ACL, Fernandes PM (2022) Unravelling the effect of climate change on fire danger and fire behaviour in the Transboundary Biosphere Reserve of Meseta Ibérica (PortugalSpain). Clim Change 173:5. https://doi.org/10.1007/s10584-022-03399-8 

- Arango E, Jimenez P, Nogal M, Sousa HS, Stewart MG, Matos JC (2024) Enhancing infrastructure resilience in wildfire management to face extreme events: insights from the Iberian Peninsula. Clim Risk Manag 44:100595. https://doi.org/10.1016/j.crm.2024.100595 

- Arca B, Bacciu V, Pellizzaro G, Salis M, Ventura A, Duce P, Spano D, Brundu G (2009) Fuel model mapping by IKONOS imagery to support spatially explicit fire simulators. In: 7th international workshop on advances in remote sensing and gis applications in forest fire management towards an operational use of remote sensing in forest fire management. Matera, Italy 

- Bacciu V, Hatzaki M, Karali A, Cauchy A, Giannakopoulos C, Spano D, Briche E (2021) Investigating the climate-related risk of forest fires for Mediterranean islands’ blue economy. Sustainability 13(18):10004. https://doi.org/10.3390/su131810004 

- Balbi JH, Morandini F, Silvani X, Filippi JB, Rinieri F (2009) A physical model for wildland fires. Combust Flame 156:2217–2230. https://doi .org/10.101 6/j.combust flame.20 09.07.010 

- Barcikowska MJ, Kapnick SB, Krishnamurty L, Russo S, Cherchi A, Folland CK (2020) Changes in the future summer Mediterranean climate: contribution of teleconnections and local factors. Earth Syst Dyn 11:161–181. https://doi.org/10.5194/esd-11-161-2020 

- Bedia J, Herrera S, Gutiérrez JM, Benali A, Brands S, Mota B, Moreno JM (2015) Global patterns in the sensitivity of burned area to fire-weather: implications for climate change. Agric for Meteorol 214– 215:369–379. https://doi .org/10.101 6/j.agrform et.2015. 09.002 

- Brown S, Calkin DE, Clark N, Cooper N, Dillon G, Finney MA, Leirfallom S, O’Connor K, Opperman T (2024) Wildfire risk (Science You Can Use 101). U.S. Department of Agriculture, Forest Service, Rocky Mountain Research Station 

- Calheiros T, Pereira MG, Nunes JP (2021) Assessing impacts of future climate change on extreme fire weather and pyro-regions in Iberian Peninsula. Sci Total Environ 754:142233.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . s c i t o t e n v . 2 0 2 0 . 1 4 2 2 3 3 

- Canu S, Rosati L, Fiori M, Motroni A, Filigheddu R, Farris E (2015) Bioclimate map of Sardinia (Italy). J Maps 11:711–718. https://doi.org/10.1080/17445647.2014.988187 

- Cardoso E, Viegas DX, Gameiro Lopes A (2025) A systematic review of models for fire spread in wildfires by spotting. Fire 8(10):392. https://doi.org/10.3390/fire8100392 

- Cardoso Pereira S, Monteiro N, Vaz R, Carvalho D (2024) High-resolution projections of future FWI conditions for Portugal according to CMIP6 future climate scenarios. Theor Appl Climatol 155:9247–9272. https://doi.org/10.1007/s00704-024-05142-y 

- Carlson AR, Hawbaker TJ, Bair LS, Hoffman CM, Meldrum JR, Baggett LS, Steblein PF (2025) Evaluating a simulation-based wildfire burn probability map for the conterminous US. Int J Wildland Fire 34:WF23196. https://doi.org/10.1071/WF23196 

- Carlucci M, Zambon I, Colantoni A, Salvati L (2019) Socioeconomic development, demographic dynamics and forest fires in Italy, 1961–2017: a time-series analysis. Sustainability 11:1305.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / s u 1 1 0 5 1 3 0 5 

- Carnicer J, Alegria A, Giannakopoulos C, Di Giuseppe F, Karali A, Koutsias N, Lionello P, Parrington M, Vitolo C (2022) Global warming is shifting the relationships between fire weather and realized fireinduced CO2 emissions in Europe. Sci Rep 12:10365. https://doi.org/10.1038/s41598-022-14480-8 

- Chuvieco E, Yebra M, Martino S, Thonicke K, Gómez-Giménez M, San-Miguel J, Oom D, Velea R, Mouillot F, Molina JR, Miranda AI, Lopes D, Salis M, Bugaric M, Sofiev M, Kadantsev E, Gitas IZ, Stavrakoudis D, Eftychidis G, Bar-Massada A, Neidermeier A, Pampanoni V, Pettinari ML, Arrogante-Funes F, Ochoa C, Moreira B, Viegas D (2023) Towards an integrated approach to wildfire risk assessment: when, where, what and how may the landscapes burn. Fire 6(5):215. https://doi.org/10.3390/fire6050215 

```
1 3
```

<mark>Page 31 of 36</mark> **<mark>629</mark>** 

Natural Hazards (2026) 122:629 

Chuvieco E, Yebra M, Jurdao S, Aguado I, Salas FJ, García M, Nieto H, De Santis A, Cocero D, Riaño D, Martínez S, Zapico E, Recondo C, Martínez-Vega J, Martín MP, Riva J, Pérez F, Rodríguez-Silva F (2011) Field fuel moisture measurements on Spanish study sites. Department of Geography, University of Alcalá, Spain. Version 1. Available online at: http://www.geogra.uah.es/emilio/FMC_UAH.html Conver JL, Falk DA, Yool SR, Parmenter RR (2018) Modeling fire pathways in montane grassland-forest ecotones. Fire Ecol 14:17–32. https://doi .org/10.499 6/fireecolo gy.14011 7031 

- Copernicus Emergency Management Service (2019) Fire danger indices historical data from the copernicus emergency management service. Copernicus Climate Change Service (C3S) Climate Data Store (CDS), https://doi.org/10.24381/cds.0e89c522 

- Cos J, Doblas-Reyes F, Jury M, Marcos R, Bretonnière PA, Samsó M (2022) The Mediterranean climate change hotspot in the CMIP5 and CMIP6 projections. Earth Syst Dyn 13:321–340.  h t t p s : / / d o i . o r g / 1 0 . 5 1 9 4 / e s d - 1 3 - 3 2 1 - 2 0 2 2 

- Crapart C, Anquetin S, Blanchet J, Diedhiou A (2026) Global projections of aridity index for mid and longterm future based on CMIP6 scenarios. Hydrol Earth Syst Sci 30:163–181.  h t t p s : / / d o i . o r g / 1 0 . 5 1 9 4 / h e s s - 3 0 - 1 6 3 - 2 0 2 6 

- Daher H, Kirtman BP (2025) Future climate assessment in the Mediterranean region using downscaled CMIP6 data. Front Clim 7:1691944. https://doi.org/10.3389/fclim.2025.1691944 

- Di Giuseppe F, Vitolo C, Krzeminski B, Barnard C, Maciel P, San-Miguel J (2020) Fire weather index: the skill provided by the European Centre for Medium-Range Weather Forecasts ensemble prediction system. Nat Hazards Earth Syst Sci 20:2365–2378. https://doi.org/10.5194/nhess-20-2365-2020 

- Duane A, Aquilué N, Canelles Q, Morán-Ordoñez A, De Cáceres M, Brotons L (2019) Adapting prescribed 

   - burns to future climate change in Mediterranean landscapes. Sci Total Environ 677:68–83.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . s c i t o t e n v . 2 0 1 9 . 0 4 . 3 4 8 

Duane A, Castellnou M, Brotons L (2021) Towards a comprehensive look at global drivers of novel extreme wildfire events. Clim Change 165:43. https://doi.org/10.1007/s10584-021-03066-4 

- Dupuy JL, Fargeon H, Martin-StPaul N, Pimont F, Ruffault J, Guijarro M, Hernando C, Madrigal J, Fernandes P (2020) Climate change impact on future wildfire danger and activity in southern Europe: a review. Ann for Sci 77:35. https://doi.org/10.1007/s13595-020-00933-5 

Dye AW, Gao P, Kim JB, Lei T, Riley KL, Yocom L (2023) High-resolution wildfire simulations reveal complexity of climate change impacts on projected burn probability for Southern California. Fire Ecol 19:20. https://doi.org/10.1186/s42408-023-00179-2 

- EC-Earth Consortium (2019) EC-Earth3-Veg model output prepared for CMIP6 ScenarioMIP. Earth System Grid Federation. https://doi.org/10.22033/ESGF/CMIP6.727 

El Garroussi S, Di Giuseppe F, Barnard C, Wetterhall F (2024) Europe faces up to tenfold increase in extreme fires in a warming climate. Npj Clim Atmos Sci 7:30. https://doi.org/10.1038/s41612-024-00575-8 ESABCC: European Scientific Advisory Board on Climate Change (2026) Strengthening resilience to climate change: recommendations for an effective EU adaptation policy framework. Publications Office of the European Union, Luxembourg. https://doi.org/10.2800/6761189 

European Commission, Joint Research Centre (2025) Current wildfire situation in Europe. Available at:  h t t p s : / / j o i n t - r e s e a r c h - c e n t r e . e c . e u r o p a . e u / p r o j e c t s - a n d - a c t i v i t i e s / n a t u r a l - a n d - m a n - m a d e - h a z a r d s / f o r e s t - fi  r e s / c u r r e n t - w i l d fi  r e - s i t u a t i o n - e u r o p e _ e n . Accessed 25 Mar 2026 

- EEA (2020) CORINE Land Cover 2018 (version 2020_20u1). Available at: Accessed 25 Mar 2026  h t t p s : / / l a 

n d . c o p e r n i c u s . e u / p a n - e u r o p e a n / c o r i n e - l a n d - c o v e r 

Fargeon H, Pimont F, Martin-StPaul N, De Caceres M, Ruffault J, Barbero R, Dupuy JL (2020) Projections of fire danger under climate change over France: where do the greatest uncertainties lie? Clim Change 160:479–493. https://doi.org/10.1007/s10584-019-02629-w 

- Feng S, Zscheischler J, Hao Z, Bevacqua E (2025) Growing human-induced climate change fingerprint in regional weekly fire extremes. Npj Clim Atmos Sci 8:152. https://doi.org/10.1038/s41612-025-01021-z 

- Fernandez-Guisuraga JM, Calvo L (2023) Fuel build-up promotes an increase in fire severity of reburned areas in fire-prone ecosystems of the western Mediterranean Basin. Fire Ecol 19(1):72.  h t t p s : / / d o i . o r g / 1 0 . 1 1 8 6 / s 4 2 4 0 8 - 0 2 3 - 0 0 2 3 2 - 0 

Fick SE, Hijmans RJ (2017) WorldClim 2: new 1-km spatial resolution climate surfaces for global land areas. Int J Climatol 37:4302–4315. https://doi.org/10.1002/joc.5086 

- Finney MA (2002) Fire growth using minimum travel time methods. Can J for Res 32:1420–1424.  h t t p s : / / d o i . o r g / 1 0 . 1 1 3 9 / x 0 2 - 0 6 8 

- Flannigan MD, Krawchuk MA, de Groot WJ, Wotton BM, Gowman LM (2009) Implications of changing climate for global wildland fire. Int J Wildland Fire 18:483–507. https://doi.org/10.1071/WF08187 

- Giannaros TM, Papavasileiou G, Lagouvardos K, Kotroni V, Dafis S, Karagiannidis A, Dragozi E (2022) Meteorological analysis of the 2021 extreme wildfires in Greece: lessons learned and implications for early warning of the potential for pyroconvection. Atmosphere (Basel) 13(3):475.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / a t m o s 1 3 0 3 0 4 7 5 

```
1 3
```

- **<mark>629</mark>** <mark>Page 32 of 36</mark> Natural Hazards (2026) 122:629 Giorgi F, Lionello P (2008) Climate change projections for the Mediterranean region. Glob Planet Change 63(2–3):90–104. https://doi .org/10.101 6/j.gloplac ha.2007. 09.005 

- Giorgi F, Raffaele F, Coppola E (2019) The response of precipitation characteristics to global warming from climate projections. Earth Syst Dyn 10:73–89. https://doi.org/10.5194/esd-10-73-2019 

- Han Y, Ullrich PA (2025) The system for classification of low-pressure systems (SyCLoPS): an all-in-one objective framework for large-scale data sets. J Geophys Res Atmos 130:e2024JD041287.  h t t p s : / / d o i . o r g / 1 0 . 1 0 2 9 / 2 0 2 4 J D 0 4 1 2 8 7 

- He Y, Zhou Z, Im ES, Kwon HH (2025) Wildfire risk in a changing climate: evaluating fire weather indices and their global patterns with CMIP6 multi-model projections. Weather Clim Extremes 48:100751. https://doi.org/10.1016/j.wace.2025.100751 

- Hersbach H, Bell B, Berrisford P, Hirahara S, Horányi A, Muñoz-Sabater J, Nicolas J, Peubey C, Radu R, Schepers D, Simmons A, Soci C, Abdalla S, Abellan X, Balsamo G, Bechtold P, Biavati G, Bidlot J, Bonavita M, De Chiara G, Dahlgren P, Dee D, Diamantakis M, Dragani R, Flemming J, Forbes R, Fuentes M, Geer A, Haimberger L, Healy S, Hogan RJ, Hólm E, Janisková M, Keeley S, Laloyaux P, Lopez P, Lupu C, Radnoti G, de Rosnay P, Rozum I, Vamborg F, Villaume S, Thépaut JN (2020) The ERA5 global reanalysis. Q J R Meteorol Soc 146(730):1999–2049. https://doi.org/10.1002/qj.3803 

- Hetzer J, Forrest M, Ribalaygua J, Prado-López C, Hickler T (2024) The fire weather in Europe: large-scale trends towards higher danger. Environ Res Lett 19(8):084017.  h t t p s : / / d o i . o r g / 1 0 . 1 0 8 8 / 1 7 4 8 - 9 3 2 6 / a d 5 b 0 9 

- INFC (2005) Inventario Nazionale delle Foreste e dei Serbatoi Forestali di Carbonio. Ministero delle Politiche Agricole Alimentari e Forestali, Ispettorato Generale Corpo Forestale dello Stato. CRA Istituto Sperimentale per l’Assestamento Forestale e per l’Alpicoltura 

- IPCC (2021) Summary for policymakers. Climate change 2021: the physical science basis. Contribution of Working Group I to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change. Cambridge University Press, Cambridge, UK and New York, USA, pp 3–32.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 7 / 9 7 8 1 0 0 9 1 5 7 8 9 6 . 0 0 1 

- IPCC (2022) Climate change 2022: impacts, adaptation, and vulnerability. Contribution of Working Group II to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change. Cambridge University Press, Cambridge, UK and New York, USA, https://doi.org/10.1017/9781009325844 

- Jolly WM, Freeborn PH, Bradshaw LS, Wallace J, Brittain S (2024) Modernizing the US national fire danger rating system (version 4): simplified fuel models and improved live and dead fuel moisture calculations. Environ Model Softw 181:106181. https://doi .org/10.101 6/j.envsoft .2024.10 6181 

- Jones MW, Abatzoglou JT, Veraverbeke S, Andela N, Lasslop G, Forkel M, Smith AJP, Burton C, Betts RA, van der Werf GR, Sitch S, Canadell JG, Santín C, Kolden C, Doerr SH, Le Quéré C (2022) Global and regional trends and drivers of fire under climate change. Rev Geophys 60(3):e2020RG000726.  h t t p s : / / d o i . o r g / 1 0 . 1 0 2 9 / 2 0 2 0 R G 0 0 0 7 2 6 

- Kalabokidis K, Palaiologou P, Gerasopoulos E, Giannakopoulos C, Kostopoulou E, Zerefos C (2015) Effect of climate change projections on forest fire behavior and values-at-risk in southwestern Greece. Forests (Basel) 6(6):2214–2240. https://doi.org/10.3390/f6062214 

- Keeping T, Garcia Garcia D, Trigo R, Santos FLM, Barnes C, Vahlberg M, Meyer R, Otto F (2025) Extreme fire weather conditions in spain and portugal now common due to climate change. Egusphere.  h t t p s : / / d o i . o r g / 1 0 . 2 5 5 6 0 / 1 2 3 5 4 7 

- Khabarov N, Krasovskii A, Obersteiner M, Swart R, Dosio A, San-Miguel-Ayanz J, Durrant T, Camia A, Migliavacca M (2016) Forest fires and adaptation options in Europe. Reg Environ Change 16:21–30. https://doi.org/10.1007/s10113-014-0621-0 

- Kim M, Pais C, Gonzalez MC (2025) Fire spread simulations using Cell2Fire on synthetic and real landscapes. Sci Rep 15:25173. https://doi.org/10.1038/s41598-025-05706-6 

- Kostopoulou E, Stavridis G (2025) Wildfire risk assessment using the fire weather index (FWI) in Greece. Climate 13:109. https://doi.org/10.3390/cli13060109 

- Lanet M, Li L, Le Treut H (2025) Substantial increase in wildfire danger conditions under anthropogenic climate change in Southwest France. Npj Nat Hazards 2:70. https://doi.org/10.1038/s44304-025-00124-0 

- Lazoglou G, Papadopoulos-Zachos A, Georgiades P, Zittis G, Velikou K, Manios EM, Anagnostopoulou C (2024) Identification of climate change hotspots in the Mediterranean. Sci Rep 14:29817.  h t t p s : / / d o i . o r g / 1 0 . 1 0 3 8 / s 4 1 5 9 8 - 0 2 4 - 8 0 1 3 9 - 1 

- Lionello P, Scarascia L (2018) The relation between climate change in the Mediterranean region and global warming. Reg Environ Change 18:1481–1493. https://doi.org/10.1007/s10113-018-1290-1 

- Lozano O, Salis M, Ager AA, Arca B, Alcasena FJ, Monteiro A, Finney MA, Del Giudice L, Scoccimarro E, Spano D (2017) Assessing climate change impacts on wildfire exposure in Mediterranean areas. Risk Anal 37:1898–1916. https://doi.org/10.1111/risa.12739 

```
1 3
```

<mark>Page 33 of 36</mark> **<mark>629</mark>** 

Natural Hazards (2026) 122:629 

Mitsopoulos I, Mallinis G, Karali A, Giannakopoulos C, Arianoutsou M (2016) Mapping fire behaviour under changing climate in a Mediterranean landscape in Greece. Reg Environ Change 16:1929–1940. https://doi.org/10.1007/s10113-015-0884-0 

Monedero S, Ramirez J, Cardil A (2019) Predicting fire spread and behaviour on the fireline: wildfire analyst pocket, a mobile app for wildland fire prediction. Ecol Model 392:103–107.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . e c o l m o d e l . 2 0 1 8 . 1 1 . 0 1 6 

Monjo R, Essa YH, Prado-López C, Kaur M, Redolat D, Paradinas C, Royé D, Ahrens B, San José R (2025) High time- and spatial-resolution climate scenarios of the DISTENDER project according to statistical and dynamical downscaling. Clim Serv 40:100623. https://doi.org/10.1016/j.cliser.2025.100623 

Moran CJ, Thompson MP, Young BA, Scott JH, Jaffe MR (2025) Benchmarking performance of annual burn probability modeling against subsequent wildfire activity in California. Sci Rep 15:23699.  h t t p s : / / d o i . o r g / 1 0 . 1 0 3 8 / s 4 1 5 9 8 - 0 2 5 - 0 7 9 6 8 - 6 

Moreno M, Bertolín C, Arlanzón D, Ortiz P, Ortiz R (2023) Climate change, large fires, and cultural landscapes in the Mediterranean basin: an analysis in southern Spain. Heliyon 9(6):e16941.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . h e l i y o n . 2 0 2 3 . e 1 6 9 4 1 

Moritz MA, Parisien MA, Batllori E, Krawchuk MA, Van Dorn J, Ganz DJ, Hayhoe K (2012) Climate change and disruptions to global fire activity. Ecosphere. https://doi.org/10.1890/ES11-00345.1 

Nauslar NJ, Abatzoglou JT, Marsh PT (2018) The 2017 North Bay and Southern California fires: a case study. Fire 1:18. https://doi.org/10.3390/fire1010018 

Oom D, De Rigo D, Pfeiffer H, Branco A, Ferrari D, Grecchi R, Artes Vivancos T, Durrant T, Boca R, Maianti P, Libertà G, San-Miguel-Ayanz J (2022) Pan-European wildfire risk assessment. EUR 31160 EN, Publications Office of the European Union, Luxembourg, https://doi.org/10.2760/9429 

Pagnon Eriksson C, Johansson N, McNamee M (2023) The performance of wildfire danger indices: a Swedish case study. Saf Sci 159:106038. https://doi.org/10.1016/j.ssci.2022.106038 

Pais S, Aquilué N, Honrado JP, Fernandes PM, Regos A (2023) Optimizing wildfire prevention through the 

integration of prescribed burning into ‘fire-smart’ land-use policies. Fire 6(12):457.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / fi  r e 6 1 2 0 4 5 7 

Palaiologou P, Ager AA, Nielsen-Pincus M, Evers CR, Kalabokidis K (2018) Using transboundary wildfire exposure assessments to improve fire management programs: a case study in Greece. Int J Wildland Fire 27:501–513. https://doi.org/10.1071/WF17119 

Palaiologou P, Kalabokidis K, Ager AA, Day MA (2020) Development of comprehensive fuel management strategies for reducing wildfire risk in Greece. Forests 11:789. https://doi.org/10.3390/f11080789 

Parente J, Tonini M, Stamou Z, Koutsias N, Pereira M (2023) Quantitative assessment of the relationship between land use/land cover changes and wildfires in southern Europe. Fire 6(5):198.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / fi  r e 6 0 5 0 1 9 8 

Parisien MA, Miller C, Ager AA, Finney MA (2010) Use of artificial landscapes to isolate controls on burn probability. Landsc Ecol 25:79–93. https://doi.org/10.1007/s10980-009-9398-9 

Parisien M-A, Dawe DA, Miller C, Stockdale CA, Bradley Armitage O (2019) Applications of simulation- 

based burn probability modelling: a review. Int J Wildland Fire 28:913–926.  h t t p s : / / d o i . o r g / 1 0 . 1 0 7 1 / W F 1 9 0 6 9 

Pausas JG, Fernandez-Munoz S (2012) Fire regime changes in the Western Mediterranean Basin: from fuel limited to drought-driven fire regime. Clim Change 110:215–226. h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 5 8 4 - 0 1 1 - 0 0 6 0 - 6 

Pellizzaro G, Duce P, Ventura A, Zara P (2007) Seasonal variations of live moisture content and ignitability in shrubs of the Mediterranean Basin. Int J Wildland Fire 16:633–641. https://doi.org/10.1071/WF05088 

Pellizzaro G, Ventura A, Arca B, Arca A, Duce P (2009) Weather seasonality and temporal pattern of live and 

dead fuel moisture content in Mediterranean shrublands. European Geosciences Union (EGU), General Assembly 2009, Vienna (Austria). http://meetings.copernicus.org/egu2009, p.12100 

Perez-Izquierdo C, Gómez Á, Pulido F (2025) Landscape-level, participatory wildfire governance reduces fire hazard and potential carbon emission. J Environ Manage 394:127308.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . j e n v m a n . 2 0 2 5 . 1 2 7 3 0 8 

Preinfalk E, Handmer J (2024) Fueling the fires–an exploration of the drivers and the scope for management of European wildfire risk under the shared socioeconomic pathways. Clim Risk Manag 45:100638. https://doi.org/10.1016/j.crm.2024.100638 

Prichard SJ, Salter RB, Hessburg PF, Povak NA, Gray RW (2023) The REBURN model: simulating systemlevel forest succession and wildfire dynamics. Fire Ecol 19:38.  h t t p s : / / d o i . o r g / 1 0 . 1 1 8 6 / s 4 2 4 0 8 - 0 2 3 - 0 0 1 9 0 - 7 

- Pulido F, Corbacho J, Bertomeu M, Gomez A, Guiomar N, Juarez E, Lucas B, Moreno G, Navalpotro J, Palomo G (2023) Fire-smart territories: a proof of concept based on Mosaico approach. Landscape Ecol 38:3353–3370. https://doi.org/10.1007/s10980-023-01618-w 

```
1 3
```

**<mark>629</mark>** <mark>Page 34 of 36</mark> Natural Hazards (2026) 122:629 Regos A (2025) A roadmap for nature-based solutions to extreme wildfires. iScience 29(1):114364.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . i s c i . 2 0 2 5 . 1 1 4 3 6 4 Riley KL, Loehman RA (2016) Mid-21st-century climate changes increase predicted fire occurrence and fire season length, Northern Rocky Mountains, United States. Ecosphere 7(11):e01543.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 2 / e c s 2 . 1 5 4 3 Rodrigues M, Zúñiga-Antón M, Alcasena F, Gelabert P, Vega-Garcia C (2022) Integrating geospatial wildfire models to delineate landscape management zones and inform decision-making in Mediterranean areas. Saf Sci 147:105616. https://doi.org/10.1016/j.ssci.2021.105616 Rodrigues M, Cunill Camprubí À, Balaguer-Romano R, Coco Megía CJ, Castañares F, Ruffault J, Fernandes PM, Resco de Dios V (2023) Drivers and implications of the extreme 2022 wildfire season in Southwest Europe. Sci Total Environ 859(2):160320. https://doi .org/10.101 6/j.scitote nv.2022. 160320 Rothermel RC (1972) A mathematical model for predicting fire spread in wildland fuels. US Department of Agriculture, Forest Service. INT-115 Rovithakis A, Burke E, Burton C, Kasoar M, Grillakis MG, Seiradakis KD, Voulgarakis A (2025) Estimating future wildfire burnt area over Greece using the JULES-INFERNO model. Nat Hazards Earth Syst Sci 25:3185–3200. https://doi.org/10.5194/nhess-25-3185-2025 Ruffault J, Curt T, Moron V, Trigo RM, Mouillot F, Koutsias N, Pimont F, Martin-StPaul N, Barbero R, Dupuy J-L, Russo A, Belhadj-Khedher C (2020) Increased likelihood of heat-induced large wildfires in the Mediterranean Basin. Sci Rep 10:13790. https://doi.org/10.1038/s41598-020-70069-z Salis M, Ager AA, Arca B, Finney MA, Bacciu V, Duce P, Spano D (2013) Assessing exposure of human and ecological values to wildfire in Sardinia, Italy. Int J Wildland Fire 22:549–565.  h t t p s : / / d o i . o r g / 1 0 . 1 0 7 1 / W F 1 1 0 6 0 Salis M, Ager AA, Alcasena F, Arca B, Finney MA, Pellizzaro G, Spano D (2015) Analyzing seasonal patterns of wildfire likelihood and intensity in Sardinia. Italy Environ Monit Assess 187:4175.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 0 6 6 1 - 0 1 4 - 4 1 7 5 - x Salis M, Arca B, Del Giudice L, Palaiologou P, Alcasena-Urdiroz F, Ager A, Fiori M, Pellizzaro G, Scarpa C, Schirru M, Ventura A, Casula M, Duce P (2021) Application of simulation modeling for wildfire exposure and transmission assessment in Sardinia, Italy. Int J Disaster Risk Reduct 58:102189.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . i j d r r . 2 0 2 1 . 1 0 2 1 8 9 

- Salis M, Del Giudice L, Jahdi R, Alcasena-Urdiroz F, Scarpa C, Pellizzaro G, Bacciu V, Schirru M, Ventura A, Casula M, Pedes F, Canu A, Duce P, Arca B (2022) Spatial patterns and intensity of land abandonment drive wildfire hazard and likelihood in Mediterranean agropastoral areas. Land (Basel) 11(11):1942. https://doi.org/10.3390/land11111942 

- Salis M, Del Giudice L, Alcasena-Urdiroz F, Jahdi R, Arca B, Pellizzaro G, Scarpa C, Duce P (2023) Assessing cross-boundary wildfire hazard, transmission, and exposure to communities in the Italy-France Maritime cooperation area. Front for Glob Change 6:1241378. https://doi.org/10.3389/ffgc.2023.1241378 

- Scarpa C, Elia M, D’Este M, Salis M, Rodrigues M, Arca B, Duce P, Fiori MAF, Pellizzaro G (2024) Modelling wildfire activity in wildland–urban interface (WUI) areas of Sardinia, Italy. Int J Wildland Fire. https://doi.org/10.1071/WF24109 

- Scott JH, Burgan R (2005) Standard Fire Behavior Fuel Models: a comprehensive set for use with rothermel's surface fire spread model. US Department of Agriculture, Forest Service. General Technical Report RMRS-GTR-153, https://doi.org/10.2737/RMRS-GTR-153 

- Scott JH, Reinhardt ED (2001) Assessing crown fire potential by linking models of surface and crown fire behavior. USDA Forest Service, Rocky Mountain Research Station, Fort Collins, CO, p 59.  h t t p s : / / d o i . o r g / 1 0 . 2 7 3 7 / R M R S - R P - 2 9 

- Sedano F, San-Miguel-Ayanz J, Broglia M, Durrant T, Boca R, Maianti P, Jacome Felix Oom D, Branco A, De Rigo D, Suarez-Moreno M, Ferrari D, Roglia E, Scionti N, Libertà G, Tistan A (2025) Forest fires in Europe, Middle East and North Africa 2024. Publications Office of the European Union.  h t t p s : / / d o i . o r g / 1 0 . 2 7 6 0 / 0 6 4 9 2 9 0 

- Seker M, Gumus V (2022) Projection of temperature and precipitation in the Mediterranean region through multi-model ensemble from CMIP6. Atmos Res 280:106440.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . a t m o s r e s . 2 0 2 2 . 1 0 6 4 4 0 

- Senande-Rivera M, Insua-Costa D, Miguez-Macho G (2022) Spatial and temporal expansion of global wildland fire activity in response to climate change. Nat Commun 13:1208.  h t t p s : / / d o i . o r g / 1 0 . 1 0 3 8 / s 4 1 4 6 7 - 0 2 2 - 2 8 8 3 5 - 2 

- Seneviratne SI, Zhang X, Adnan M, Badi W, Dereczynski C, Di Luca A, Ghosh S, Iskandar I, Kossin J, Lewis S, Otto F, Pinto I, Satoh M, Vicente-Serrano SM, Wehner M, Zhou B (2021) Weather and climate extreme events in a changing climate. In: Climate change 2021: the physical science basis. Contribution of Working Group I to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change. Cambridge University Press, Cambridge, UK and New York, USA, 1513–1766,  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 7 / 9 7 8 1 0 0 9 1 5 7 8 9 6 . 0 1 3 

```
1 3
```

<mark>Page 35 of 36</mark> **<mark>629</mark>** 

Natural Hazards (2026) 122:629 

- Sirca C, Salis M, Arca B, Duce P, Spano D (2018) Assessing the performance of fire danger indexes in a Mediterranean area. iForest 11:563–571. https://doi.org/10.3832/ifor2679-011 

- Somot S, Houpert L, Sevault F, Testor P, Bosse A, Taupier-Letage I, Bouin MN, Waldman R, Cassou C, Sanchez-Gomez E, Durrieu de Madron X, Adloff F, Nabat P, Herrmann M (2016) Characterizing, modelling and understanding the climate variability of the deep water formation in the north-western Mediterranean Sea. Clim Dyn. https://doi.org/10.1007/s00382-016-3295-0 

- Steensen BM, Myhre G, Byrom R, Gjermundsen A, Jouan C, Stjern CW (2026) European summer precipitation. Atmos Chem Phys 26:2041–2054. https://doi.org/10.5194/acp-26-2041-2026 

- Von Storch JS, Putrasahan D, Lohmann K, Gutjahr O, Jungclaus J, Bittner M, Haak H, Wieners KH, Giorgetta M, Reick C, Esch M, Gayler V, de Vrese P, Raddatz T, Mauritsen T, Behrens J, Brovkin V, Claussen M, Crueger T, Fast I, Fiedler S, Hagemann S, Hohenegger C, Jahns T, Kloster S, Kinne S, Lasslop G, Kornblueh L, Marotzke J, Matei D, Meraner K, Mikolajewicz U, Modali K, Müller W, Nabel J, Notz D, Peters-von Gehlen K, Pincus R, Pohlmann H, Pongratz J, Rast S, Schmidt H, Schnur R, Schulzweida U, Six K, Stevens B, Voigt A, Roeckner E (2017) MPI-ESM1.2-HR model output prepared for CMIP6 HighResMIP. Earth Syst Grid Fed, https://doi.org/10.22033/ESGF/CMIP6.762 

- Sullivan AL (2009) Wildland surface fire spread modelling, 1990–2007. 1: physical and quasi-physical models. Int J Wildland Fire 18(4):349–368. https://doi.org/10.1071/WF06143 

- Sutanto SJ, Duku C, Gülveren M, Dankers R, Paparrizos S (2025) Future intensification of compound and consecutive drought and heatwave risks in Europe. Nat Hazards Earth Syst Sci 25:3879–3895.  h t t p s : / / d o i . o r g / 1 0 . 5 1 9 4 / n h e s s - 2 5 - 3 8 7 9 - 2 0 2 5 

- Trucchia A, D’Andrea M, Baghino F, Fiorucci P, Ferraris L, Negro D, Gollini A, Severino M (2020) PROPAGATOR: an operational cellular-automata based wildfire simulator. Fire 3:26.  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / fi  r e 3 0 3 0 0 2 6 

- Turco M, Rosa-Cánovas JJ, Bedia J, Jerez S, Montavez JP, Llasat MC, Provenzale A (2018) Exacerbated fires in Mediterranean Europe due to anthropogenic warming projected with non-stationary climate-fire models. Nat Commun 9:3821. https://doi.org/10.1038/s41467-018-06358-z 

- Vaillant NM, Ager AA, Anderson J (2013) ArcFuels10 system overview. General Technical Report PNWGTR-875. Portland, OR: U.S. Department of Agriculture, Forest Service, Pacific Northwest Research Station. 65 pp, https://doi.org/10.2737/PNW-GTR-875 

- Van Wagner CE (1977) Conditions for the start and spread of crown fire. Can J for Res 7:23–34.  h t t p s : / / d o i . o r g / 1 0 . 1 1 3 9 / x 7 7 - 0 0 4 

- Venalainen A, Korhonen N, Hyvärinen O, Koutsias N, Xystrakis F, Urbieta IR, Moreno JM (2014) Temporal variations and change in forest fire danger in Europe for 1960–2012. Nat Hazards Earth Syst Sci 14:1477–1490. https://doi.org/10.5194/nhess-14-1477-2014 

- Viegas DX, Rodrigues T, Marrs C, Eftychidis G, Chuvieco E (2024) D4.5 – Roadmap for an integrated wildfire risk management strategy for Europe. h t t p s : / / fi  r e u r i s k . e u / w p - c o n t e n t / u p l o a d s / 2 0 2 5 / 0 5 / D 4 5 R O A 1 . p d f 

- Van Wagner CE (1987) Development and structure of the Canadian forest fire weather index system. Canadian Forestry Service, Petawawa National Forestry Institute, Ottawa, Forestry Technical Report 35 

- Yebra M, Scortechini G, Adeline K, Aktepe N, Almoustafa T, Bar-Massada A, Beget ME, Boer M, Bradstock R, Brown T, Castro FX, Chen R, Chuvieco E, Danson M, Degirmenci CU, Delgado-Davila R, Dennison P, Di Bella C, Domenech O, Feret JB, Forsyth G, Gabriel E, Gagkas Z, Gharbi F, Granda E, Griebel A, He B, Jolly M, Kotzur I, Kraaij T, Kristina A, Kutkut P, Limousin JM, Martín MP, Monteiro AT, Morais M, Moreira B, Mouillot F, Msweli S, Nolan RH, Pellizzaro G, Qi Y, Quan X, Resco de Dios V, Roberts D, Tavsanoglu C, Taylor AFS, Taylor J, Tufekcioglu I, Ventura A, Younes Cardenas N (2024) GlobeLFMC 2.0, an enhanced and updated dataset for live fuel moisture content research. Sci Data 11(1):332. https://doi.org/10.1038/s41597-024-03159-6 

- Ziehn T, Chamberlain MA, Law RM, Lenton A, Bodman RW, Dix M, Stevens L, Wang YP, Srbinovsky J (2020) The Australian Earth System Model: ACCESS-ESM1.5. J South Hemisph Earth Syst Sci 70(1): 193–214, https://doi.org/10.1071/ES19035 h t t p s : / / f o r e s t - fi  r e . e m e r g e n c y . c o p e r n i c u s . e u / a b o u t - e ffi   s / t e c h n i c a l - b a c k g r o u n d / fi  r e - d a n g e r - f o r e c a s t www.sardegnageoportale.it 

**Publisher's Note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

```
1 3
```

**<mark>629</mark>** <mark>Page 36 of 36</mark> 

Natural Hazards (2026) 122:629 

## **Authors and Affiliations** 

**Michele Salis**<sup>**1**</sup> **· Liliana Del  Giudice**<sup>**1**</sup> **· Fermin Alcasena-Urdiroz**<sup>**2**</sup> **· Carla Scarpa**<sup>**1**</sup> **· Valentina Bacciu**<sup>**1**</sup> **· Grazia Pellizzaro**<sup>**1**</sup> **· Roghayeh Jahdi**<sup>**3**</sup> **· Pierpaolo Duce**<sup>**1**</sup> **· Robert Monjo**<sup>**4,5**</sup> **· Jaime Ribalaygua**<sup>**4**</sup> **· Luis Torres**<sup>**4**</sup> **· Carlos Prado**<sup>**4**</sup> **· Bachisio Arca**<sup>**1**</sup> 

- Michele Salis michele.salis@cnr.it 

- Liliana Del Giudice 

- lilianadelgiudice@cnr.it 

- 1 Institute of BioEconomy (CNR IBE), National Research Council of Italy, Traversa La Crucca 3, 07100 Sassari, Italy 

- 2 Department of Engineering, Institute for Sustainability and Food Chain Innovation (ISFOOD), Public University of Navarre (UPNA), Arrosadia Campus, 31006 Pamplona, Spain 

- 3 University of Mohaghegh Ardabili, Ardabil 56199-11367, Iran 

- 4 Meteogrid, Calle de Modesto Lafuente 45, Office 3, 28003 Madrid, Spain 

- 5 Department of Quantitative Methods, CUNEF University, Calle de Almansa, 101, 28040 Madrid, Spain 

```
1 3
```


