---
title: 'Tracking the efficacy of prescribed burns in three phases: fuel removal, wildfire mitigation, and vegetation recovery'
authors:
- Liu, Tianjia
- Otobe, Kento
- Kelp, Makoto
year: '2026'
journal: The international archives of the photogrammetry, remote sensing and spatial information sciences/International archives of the photogrammetry, remote sensing and spatial information sciences
doi: 10.5194/isprs-archives-xlix-b3-2026-987-2026
tags:
- large wildfires
- prescribed burning
- united states
zotero_key: RFANKUXI
item_type: journalArticle
url: https://openalex.org/W7171881315
source_url: 'unpaywall: https://isprs-archives.copernicus.org/articles/XLIX-B3-2026/987/2026/isprs-archives-XLIX-B3-2026-987-2026.pdf'
fulltext_status: fulltext
synced: '2026-11-06'
---

# Tracking the efficacy of prescribed burns in three phases: fuel removal, wildfire mitigation, and vegetation recovery

## Abstract

Abstract. In the United States (U.S.), aggressive suppression policies in the 20th century reduced wildfires in the short term, but accumulated fuels contributed to increased wildfire risk in the long term. Land managers are slowly reintroducing the use of fuel treatments, including prescribed (Rx) fires, to remove fuels and mitigate future wildfires. To date, efforts to systematically quantify the efficacy of fuel treatments for wildfire mitigation have been limited in spatial and temporal scope or rely on proxies, such as low-intensity wildfires. Here we use the 30-m Harmonized Landsat and Sentinel-2 (HLS) dataset to analyze timeseries of vegetation “greenness” indices, such as the Normalized Burn Ratio (NBR), with observations up to every 1.4 days. We apply a causal inference approach, difference-in-differences (DID), on HLS-derived timeseries of NBR to compare outcomes in treated and surrounding control areas in three different time phases: 1) post-treatment fuel reduction, 2) wildfire-induced burn severity, and 3) post-wildfire vegetation recovery. As a case study, we targeted 37 Rx fires that preceded and intersected the 2024 Park Fire, a large wildfire in northern California. We show statistical evidence that Rx fires reduce fuel loads (12 Rx fires), wildfire burn severity (12 Rx fires), and postwildfire vegetation recovery (14 Rx fires). Our approach requires only the spatial footprint and timing of the fuel treatments, thus enabling regional to nationwide analyses using a large number of fuel treatments to quantify the general efficacy of fuel treatments across a variety of treatment types, fuel types, and topography.

## Full text

The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences, Volume XLIX-B3-2026 XXV ISPRS Congress 2026 “From Imagery to Understanding”, Commission III, 4–11 July 2026, Toronto, Canada 

# **Tracking the efficacy of prescribed burns in three phases: fuel removal, wildfire mitigation, and vegetation recovery** 

Tianjia Liu<sup>1</sup> , Kento Otobe<sup>2</sup> , Makoto Kelp<sup>3</sup> 

1 Dept. of Geography, University of British Columbia, Vancouver, BC V6T 1Z2, Canada – tianjia.liu@ubc.ca 

2 Dept. of Geography, University of British Columbia, Vancouver, BC V6T 1Z2, Canada – kentootobe@gmail.com 3 Dept. of Atmospheric Sciences, University of Utah, Salt Lake City, UT, 84112, United States – makoto.kelp@utah.edu 

**Keywords:** Prescribed burns, Wildfires, Land management, Vegetation, Satellite data, Timeseries. 

## **Abstract** 

In the United States (U.S.), aggressive suppression policies in the 20<sup>th</sup> century reduced wildfires in the short term, but accumulated fuels contributed to increased wildfire risk in the long term. Land managers are slowly reintroducing the use of fuel treatments, including prescribed (Rx) fires, to remove fuels and mitigate future wildfires. To date, efforts to systematically quantify the efficacy of fuel treatments for wildfire mitigation have been limited in spatial and temporal scope or rely on proxies, such as low-intensity wildfires. Here we use the 30-m Harmonized Landsat and Sentinel-2 (HLS) dataset to analyze timeseries of vegetation “greenness” indices, such as the Normalized Burn Ratio (NBR), with observations up to every 1.4 days. We apply a causal inference approach, difference-in-differences (DID), on HLS-derived timeseries of NBR to compare outcomes in treated and surrounding control areas in three different time phases: 1) post-treatment fuel reduction, 2) wildfire-induced burn severity, and 3) post-wildfire vegetation recovery. As a case study, we targeted 37 Rx fires that preceded and intersected the 2024 Park Fire, a large wildfire in northern California. We show statistical evidence that Rx fires reduce fuel loads (12 Rx fires), wildfire burn severity (12 Rx fires), and postwildfire vegetation recovery (14 Rx fires). Our approach requires only the spatial footprint and timing of the fuel treatments, thus enabling regional to nationwide analyses using a large number of fuel treatments to quantify the general efficacy of fuel treatments across a variety of treatment types, fuel types, and topography. 

## **1. Introduction** 

Recent wildfire seasons in the western U.S. have posed a significant threat to public safety, air quality, and ecosystem resilience, underscoring the urgent need for effective land management solutions (Burke et al., 2023; Chung et al., 2025; Jaffe et al., 2020). While complete suppression reduces wildfires in the short term, accumulated understory fuels from the lack of frequent maintenance via fuel treatments increases wildfire risk in the long term (Kreider et al., 2024). As local, state, and federal agencies recognize the harmful, long-term impacts of full suppression policies, the increased use of fuel treatments, including prescribed (Rx) fires, cultural burning, and mechanical thinning, is slowly re-orienting land management toward beneficial fire strategies seen in Indigenous land stewardship (Schultz et al., 2019; Worsham et al., 2025). Particular barriers for widescale use of Rx fires in the western U.S. include public perceptions, policy, and funding, drawbacks of short-term smoke from Rx fires, escaped Rx fires, and climate change narrowing the time window during a given year for safely igniting Rx fires (Huber-Stearns et al., 2025; Jones et al., 2022; Li et al., 2025; Schultz et al., 2019; Swain et al., 2023). 

To date, empirical efforts to systematically quantify the efficacy of fuel treatments for wildfire mitigation have been limited in spatial and/or temporal scope or rely on proxies, such as lowintensity wildfires (e.g., Jain et al., 2021; Jones et al., 2025; Kelp et al., 2025, 2023; Wu et al., 2023). Because Rx fire treatments are typically small in area (~10s to 100s of hectares), many previous studies rely on Landsat and Sentinel-2 imagery for mapping and characterization, but the low temporal frequency of observations (every 5 to 16 days) have limited these analyses to using simple differences in pre-fire and post-fire image composites. However, advances in remote sensing and cloudbased geospatial computing, such as through Google Earth Engine (Gorelick et al., 2017), have greatly increased the spatial 

and temporal scale at which we can feasibly track and analyze timeseries of vegetation and land use change through spectral indices of vegetation “greenness,” such as the Normalized Difference Vegetation Index (NDVI) and Normalized Burn Ratio (NBR) (Key and Benson, 2006; Yengoh et al., 2015). High NDVI and NBR indicate healthy vegetation, while low NDVI and NBR indicate unhealthy vegetation, burned area, and exposed soil. Differences between pre- and post-fire NBR, or dNBR, is often used as an indicator of burn severity. Available through the Google Earth Engine data catalog, the HLS collection increases the effective temporal frequency of observations up to every 1.4 days, thus enabling timeseries analysis at a high spatial resolution (30-m) to more robustly track and verify effects in post-treatment fuel reduction, wildfire burn severity mitigation, and postwildfire vegetation recovery. We hypothesize that areas treated with Rx fire, when compared to untreated control areas, experience: 1) decreases in NBR and NDVI after treatment, indicating a reduction in fuels; 2) smaller differences in pre- to post-wildfire NBR and NDVI, indicating lower burn severity, and 3) higher NBR and NDVI post-wildfire, indicating faster post-wildfire vegetation recovery to baseline levels. 

Here we establish a framework for timeseries analysis of satellite-derived vegetation indices (VIs) at high spatio-temporal resolution to more robustly quantify the general efficacy of Rx fires. We focus on three time phases within the VI timeseries: post-treatment fuel reduction, wildfire-induced burn severity, and post-wildfire vegetation recovery. As a case study, we focus on 37 Rx fires that preceded and intersected with the 2024 Park Fire in northern California. 

This contribution has been peer-reviewed. https://doi.org/10.5194/isprs-archives-XLIX-B3-2026-987-2026 | © Author(s) 2026. CC BY 4.0 License. 

987 

The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences, Volume XLIX-B3-2026 XXV ISPRS Congress 2026 “From Imagery to Understanding”, Commission III, 4–11 July 2026, Toronto, Canada 

## **2. Methods** 

## **2.1 Defining Treated and Control areas** 



Figure 1. Map of the 2024 Park Fire and 37 Rx fires that intersected and preceded the wildfire. The Park Fire is denoted as the red polygon; Rx fires are divided into areas that are within (black) and outside (gray) of the Park Fire. 

In this study, we focus on Rx fires that preceded and intersected the Park Fire, a large wildfire that burned 429,603 acres (or 1,739 km<sup>2</sup> ) in northern California in 2024 (Figure 1). We use wildfire and Rx fire polygons collected by the California Department of Forestry and Fire Protection (CAL FIRE)’s Fire and Resource Assessment Program (FRAP). FRAP records the ignition and containment date for wildfires, and the treatment start and end date for Rx fires. Other Rx fire metadata include burn type (e.g., broadcast burns, machine pile burns) and the area treated within the Rx fire polygon. 

In contrast to Kelp et al. (2025), where points (i.e., longitude and latitude coordinates) with a spatial buffer are used to approximate the footprint of Rx fires due to data limitations, here we use FRAP Rx polygons to directly delineate the spatial footprint of Rx fires. We apply a spatial filter using the Park Fire perimeter and a temporal filter to account for the availability of the HLS collection (2013-present) and the ignition time of the Park Fire on 24 July 2024. This resulted in 37 Rx fire polygons of interest. We intersect the filtered set of 37 Rx fire polygons with the Park Fire perimeter boundary to create polygons that delineate treated areas within the Park Fire. 

Following Kelp et al. (2025), we define the control area as a buffered region of equal area surrounding the Rx burn footprint. If the Rx fire is represented as a point, the geometry of the control area can be constructed based on the area of circles, where the radius 𝑟 of the circle is equivalent to the buffer distance: 



<!-- Start of picture text -->
𝑟!"#$!#%*&'(!"') = √2(𝑟!"#$!#%) (3)<br><!-- End of picture text -->

where 𝐴 is the area of the geometry and 𝑟 is the radius. The treated area, 𝐴!"#$!#%, and the combined treated and control area, 𝐴!"#$!#%*&'(!"'), are concentric circles. Based on the definitions, the radius of  𝐴!"#$!#%*&'(!"') is equal to the radius of 𝐴!"#$!#% multiplied by the square root of 2. The polygon denoting the control area, 𝑃&'(!"'), can be constructed as follows: 



<!-- Start of picture text -->
𝑃&'(!"') = 𝑃!"#$!#%*&'(!"') −𝑃!"#$!#% (4)<br>𝑃&'(!"') = buffer(𝑝, 𝑟!"#$!#%*&'(!"')) −buffer(𝑝, 𝑟!"#$!#%) (5)<br><!-- End of picture text -->

where 𝑃!"#$!#%*&'(!"') is the polygon of combined treated and control buffer region, 𝑃!"#$!#% is the treated buffer region, and 𝑝 is the point geometry denoting the location of the Rx fire. 

If the Rx fire is already represented as a polygon, as in this study, this calculation must be modified to generalize across irregular shapes. We use a two-step process, wherein we first use a perfect circle assumption to approximate the buffer distance to define the control area and then adjust the buffer distance 𝑑 based on the ratio of treated area and control area from the initial guess: 



<!-- Start of picture text -->
𝑑!"#$!#%,- = 5𝐴!"#$!#%/𝜋 (6)<br>𝑑&'(!"'),- = 52(𝑑!"#$!#%) + −𝑑!"#$!#%,- (7)<br>𝑃&'(!"'),- = buffer7𝑃!"#$!#%, 𝑑&'(!"'),-8 −𝑃!"#$!#% (8)<br>𝑑&'(!"'),. = 𝑑&'(!"'),-  × 𝐴!"#$!#%/𝐴&'(!"'),- (9)<br>𝑃&'(!"'),. = buffer7𝑃!"#$!#%, 𝑑&'(!"'),.8 −𝑃!"#$!#% (10)<br><!-- End of picture text -->

where the subscript _i_ denotes the initial guess associated with the perfect circle assumption, and the subscript _f_ denotes the final estimation. 

## **2.2 Satellite-Derived Timeseries of Vegetation Indices** 

The HLS collection from the U.S. National Aeronautics and Space Administration (NASA) includes Landsat 8/9 (HLSL30) and Sentinel-2A/B (HLSS30) surface reflectance imagery at 30m spatial resolution and up to 1.4 days in temporal frequency depending on satellite availability (Ju et al., 2025). The temporal availability of HLS-Landsat is from April 2013, and the temporal availability of HLS-Sentinel-2 is from November 2015. To produce seamless imagery across HLSL30 (Operational Land Imager) and HLSS30 (Multi-Spectral Instrument), HLS processing includes atmospheric correction (to convert top-ofatmosphere to surface reflectance), quality masks (e.g., clouds, cloud shadows), geographic co-registration and common gridding (to 30-m spatial resolution), bidirectional reflectance distribution function normalization (to account for variation in view angles and illumination), and spectral bandpass adjustment (to standardize band wavelength ranges) (Ju et al., 2025). 

We use HLS surface reflectance from all available scenes to calculate the average NDVI and NBR within the treated and control polygons: 



<!-- Start of picture text -->
𝑁𝐷𝑉𝐼= 𝑁𝐼𝑅−𝑅𝑒𝑑 (11)<br>𝑁𝐼𝑅+ 𝑅𝑒𝑑<br>𝑁𝐵𝑅= 𝑁𝐼𝑅−𝑆𝑊𝐼𝑅 (12)<br>𝑁𝐼𝑅+ 𝑆𝑊𝐼𝑅<br><!-- End of picture text -->



<!-- Start of picture text -->
𝐴!"#$!#% = 𝐴&'(!"') = 𝐴!"#$!#%*&'(!') − 𝐴!"#$!#% (1)<br>𝜋(𝑟!"#$!#%) + = 𝜋(𝑟!"#$!#%*&'(!"')) + −𝜋(𝑟!"#$!#%) + (2)<br><!-- End of picture text -->

This contribution has been peer-reviewed. https://doi.org/10.5194/isprs-archives-XLIX-B3-2026-987-2026 | © Author(s) 2026. CC BY 4.0 License. 

988 

The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences, Volume XLIX-B3-2026 XXV ISPRS Congress 2026 “From Imagery to Understanding”, Commission III, 4–11 July 2026, Toronto, Canada 

where 𝑁𝐼𝑅 is the near-infrared band (0.85-0.88 µm), 𝑅𝑒𝑑 is the red band (0.64-0.67 µm), and 𝑆𝑊𝐼𝑅 is the shortwave infrared-2 band (2.11-2.29 µm). 

We classified pixels as high quality, non-cloudy “clear” pixels using two simple and consistent checks based on the red and SWIR-2 bands, following Xiang et al. (2013) and Liu et al. (2021); both criteria must be fulfilled: 



<!-- Start of picture text -->
𝑅𝑒𝑑< 0.3 (13)<br><!-- End of picture text -->



<!-- Start of picture text -->
𝑆𝑊𝐼𝑅−𝑅𝑒𝑑<br>> 0 (14)<br>𝑆𝑊𝐼𝑅+ 𝑅𝑒𝑑<br><!-- End of picture text -->

Based this binary classification, where clear pixels are assigned a 1 and cloudy pixels assigned a 0, we average these values to calculate the fraction of clear pixels within the treated and control polygons. After masking out cloudy pixels, we average NDVI and NBR within the treated and control polygons. 

## **2.3 Difference-in-Differences Estimation in Three Phases** 

Often applied in the fields of econometrics and public health, difference in differences (DID) is a quasi-experimental technique used to quantify the causal effect of an intervention by isolating time-dependent differences in a treatment group and a counterfactual control group (Baker et al., 2025). An advantage of DID is that inherent time-invariant differences between the treatment and control are accounted for. Here we apply DID on HLS-derived timeseries of NDVI and NBR to quantify the effect of Rx fires. We formulate the DID analysis as an ordinary least squares linear regression: 

𝑉𝐼-! = 𝛽/ + 𝛽0𝑡𝑟𝑒𝑎𝑡- + 𝛽+𝑡𝑖𝑚𝑒! + 𝛿(𝑡𝑟𝑒𝑎𝑡- × 𝑡𝑖𝑚𝑒!) + 𝜖-!(15) 

where 𝑉𝐼-! refers to NDVI or NBR at a specific time 𝑡 for group 𝑖 (treated or control), 𝑡𝑟𝑒𝑎𝑡- is a dummy variable that denotes the treated and control groups (1 if treated, 0 if control), 𝑡𝑖𝑚𝑒! is a dummy variable that denotes the time of the phase (1 if within phase, 0 if not), 𝛿 is the DID estimator, or coefficient of the interaction term 𝑡𝑟𝑒𝑎𝑡- × 𝑡𝑖𝑚𝑒!, 𝛽/ is the intercept, and 𝜖-! is the residuals. We also apply the fraction of clear pixels as the weights in the linear regression. 



Figure 2. Conceptual diagram of three phases for tracking the effect of Rx fires. The three phases are defined based on the start and end date of the Rx fire (orange dots) and the ignition and containment dates of the wildfire (red dots). 

We track the potential effect of Rx fires in three phases: 1) posttreatment fuel reduction, 2) wildfire burn severity mitigation, and 3) post-wildfire vegetation recovery (Figure 2). The timing of each phase is bounded by the timing of the Rx fire or the wildfire. One caveat is that the co-existence of the three phases within the same timeseries could result in confounding effects in the DID estimation. We thus split the timeseries into “in-phase,” “out-ofphase,” and “excluded data points.” Included in the linear regression for DID estimation are in-phase and out-of-phase data points. The in-phase period represents the target period for quantifying the Rx fire effect. For a given phase, we exclude data points that overlap with other phases that could bias the DID estimation. Excluded data points also extend across the potential length of post-treatment and post-wildfire effects, which we set as one year after the treatment end date and wildfire containment date, respectively. 

As a baseline, we set the length of phase 1 and phase 3 as 60 days and the length of the post-fire and pre-fire components of phase 2 as 30 days each. We estimate 𝛿 for each phase and consider _p_ < 0.05 to be statistically significant. For phase 1, a negative 𝛿 suggests fuel reduction in the treated area during the posttreatment period. For phase 2, we take the difference of the postfire and pre-fire 𝛿, which we denote as ∆𝛿: 



<!-- Start of picture text -->
∆𝛿= 𝛿1'2! − 𝛿1"# (15)<br><!-- End of picture text -->

∆𝛿 follows the concept of dNBR, which compares pre-fire and post-fire NBR to estimate burn severity (Key and Benson, 2006). A positive ∆𝛿 indicates mitigation of wildfire-induced burn severity by the Rx fire treatment. The 𝛿1"# component accounts for lingering post-treatment differences between the treated and control areas close to the time of wildfire ignition. We assess the statistical significance of ∆𝛿 using the 𝛿1'2! component, which represents differences in wildfire-induced burn severity. For phase 3, a positive 𝛿 suggest faster vegetation recovery in the treated area during the post-wildfire period. 

To test the persistence of post-treatment fuel reduction (phase 1) and post-wildfire vegetation recovery (phase 3), we add varying positive phase shifts to the phase time window. The baseline scenario is a phase shift of 0, and positive phase shifts represent forward temporal shifts. 

## **3. Results and Discussion** 

## **3.1 Characteristics of Rx Fires within the 2024 Park Fire** 

Using FRAP’s geospatial database of Rx fire polygons, we focus on 37 Rx fires that intersect and precede the 2024 Park Fire (1,739 km<sup>2</sup> ), which was ignited on 24 July 2024 and contained on 7 September 2024. These 37 Rx fires, which are mainly dispersed across the northern, southern, and eastern regions of the Park Fire, only overlap with 0.53% of the wildfire burned area (Figure 1). 34 Rx fires are broadcast burns, and 3 Rx fires are machine pile burns. 

|Rx Fire Characteristics|Mean<br>(1 SD)|Range<br>[min, max]|
|---|---|---|
|Area, total (km<sup>2</sup>)|0.44 (0.85)|[0.03, 4.79]|
|Area, within wildfire (km<sup>2</sup>)|0.25 (0.43)|[<0.01, 2.58]|
|Fraction overlap with wildfire|0.81 (0.35)|[<0.01, 1]|
|Fraction treated|0.95 (0.16)|[0.15, 1]|
|Duration (days)|20 (42)|[1, 175]|



Table 1. Summary of the 37 Rx fires in this study. 

This contribution has been peer-reviewed. https://doi.org/10.5194/isprs-archives-XLIX-B3-2026-987-2026 | © Author(s) 2026. CC BY 4.0 License. 

989 

The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences, Volume XLIX-B3-2026 XXV ISPRS Congress 2026 “From Imagery to Understanding”, Commission III, 4–11 July 2026, Toronto, Canada 

The Rx fires are highly variable in size, fractional overlap with the wildfire, fractional area treated within the polygon, and reported duration of the treatment (Table 1). The mean areal footprint of the Rx fires is 0.44 ± 0.85 km<sup>2</sup> on average, while the area of Rx fires within the Park Fire perimeter is 0.25 ± 0.43 km<sup>2</sup> on average. The mean fraction of overlap with the wildfire is 0.81 ± 0.35. Among those with low fractional overlap (<0.1) are two of the largest Rx fires, both of which are located on western edge of the wildfire: 2023 HWY36E Roadside (0.74 km<sup>2</sup> ) and 2019 TNC Canal Uplands Unit (4.79 km<sup>2</sup> ) (Figure 1). The fraction treated, or the reported treated area relative to the polygon area, is 0.95 ± 0.16 days on average. The mean duration, based on the reported treatment start and end dates, is 20 ± 42 days, although approximately two-thirds Rx fires have a duration of < 7 days. 

## **3.2 Effect of Rx Fires in Fuel Removal, Wildfire Mitigation, and Vegetation Recovery** 

Below we focus on DID estimation using the NBR timeseries, though we find close agreement using the NDVI timeseries. We find that the NBR timeseries is less noisy between consecutive observations, likely due to lower sensitivity to smoke and haze in the SWIR-2 band compared to red band. 



Figure 3. The effects of Rx fires on vegetation in three phases. Violin plots show the distribution of the DID estimator 𝛿 for phases 1 and 3 and ∆𝛿 for phase 2 among the 37 Rx fires. Each dot represents one of the 37 Rx fires. Filled-in dots indicate statistical significance at _p_ < 0.05. 

On average, we observe post-treatment fuel reduction (𝛿 = -0.05 𝛿 range: [-0.21, +0.02]) in the 60 days following Rx fires and faster post-wildfire vegetation recovery (𝛿 = +0.07, 𝛿 range: [- 0.07, +0.28]) in the 60 days following containment of the Park Fire (Figure 3). Based on differences in the 30-day post-fire and pre-fire 𝛿, we also observe that Rx fires mitigate wildfire burn severity (∆𝛿 = +0.05, ∆𝛿 range: [-0.09, +0.34]). For individual Rx fires, statistical significance ( _p_ < 0.05) in the DID estimation generally align with the overall trends of negative 𝛿 in phase 1, positive ∆𝛿 in phase 2, and positive 𝛿 in phase 3. 

|Description|Phase 1|Phase 2|Phase 3|#|
|---|---|---|---|---|
|All|-𝛿|+∆𝛿|+𝛿|3|
|Phase 1+2 only|-𝛿|+∆𝛿||0|
|Phase 1+3 only|-𝛿||+𝛿|1|
|Phase 2+3 only||+∆𝛿|+𝛿|9|
|Phase 1 only|-𝛿|||8|
|Phase 2 only||+∆𝛿||0|
|Phase 3 only|||+𝛿|1|
|None||||15|



Table 2. Summary of phase-specific DID estimation by number of Rx fires with statistically significant effects in different combinations of phases 

Phase-specific DID estimation shows statistically significant post-treatment fuel reduction (phase 1: -𝛿) in 12 Rx fires, lower wildfire burn severity (phase 2: +∆𝛿) in 12 Rx fires, and faster post-wildfire vegetation recovery (phase 3: +𝛿) in 14 Rx fires (Table 2). In total, we find statistically significant effects for 22 of 37 Rx fires that follow the overall phase-specific trends during at least one phase: 9 Rx fires during one phase, 10 Rx fires during two phases, and 3 Rx fires during all three phases. Of the 22 Rx fires, most are in the phase 2+3 only (9) or phase 1 only (8) group. This suggests that post-treatment fuel reduction effects and (post)wildfire benefits and are often not observed together in the same timeseries. Potential metadata limitations, such as ambiguous or incomplete treatment duration and timing, and confounding effects, such as prior treatment history or overlap among treatments, may play a role in masking the quantified effects. For example, the treatment with statistically significant effects in the opposite direction in Phase 2 and 3, the PCSC Unit 1 RX Burn, only reported 15% of area treated within the polygon. 



Figure 4. HLS-derived NBR timeseries within treated and control areas, using the 2023 Loafer Creek Rx fire as an example. The 2023 Loafer Creek Rx fire is shown in the inset map and is located in the southern region of the 2024 Park Fire. The NBR trajectories 

This contribution has been peer-reviewed. https://doi.org/10.5194/isprs-archives-XLIX-B3-2026-987-2026 | © Author(s) 2026. CC BY 4.0 License. 

990 

The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences, Volume XLIX-B3-2026 

XXV ISPRS Congress 2026 “From Imagery to Understanding”, Commission III, 4–11 July 2026, Toronto, Canada 

within the Rx fire (purple) and control polygon (black) diverges after the Rx fire (phase 1), during the Park Fire (phase 2), and after the Park Fire (phase 3). Circles denote HLS Landsat-derived NBR, and triangles denote HLS Sentinel-derived NBR. The NBR trajectories are smoothed with cubic splines for visualization. The duration of the Rx fire (orange) and the ignition and containment dates for the wildfire (red) is denoted in vertical lines. The opacity of the points represents the fraction of high quality, non-cloudy 

pixels. 

The three Rx fires with statistically significant effects across all three phases are the 2023 Loafer Creek LLC HFR VMP (637 acres, or 2.58 km<sup>2</sup> ), 2023 Unit 1 VMP (88 acres, or 0.36 km<sup>2</sup> ), and 2024 Middle Ridge Unit C (35 acres, or 0.14 km<sup>2</sup> ) Rx fires: phase 1 (𝛿 = -0.19 to -0.08), phase 2 (∆𝛿 = +0.15 to +0.34), and phase 3 (𝛿 = +0.07 to +0.13). These Rx fires are all broadcast burns in close temporal proximity (within one year prior) to the ignition of the Park Fire. 

Figure 4 shows an example of the HLS timeseries for the 2023 Loafer Creek Rx Fire, which shows clear divergence in NBR values in each of the three phases. We observe post-treatment fuel reduction (𝛿 = -0.13) in the 60 days following the Rx fire and faster post-wildfire vegetation recovery (𝛿 = +0.1) toward baseline levels in the 60 days following containment of the Park Fire. Based on the difference in the 30-day post-fire and pre-fire 𝛿, the Rx fire reduced wildfire burn severity (∆𝛿 = +0.22), which is roughly equivalent to a decrease in burn severity by one category from moderate-high (control) to moderate-low (treated). 



<!-- Start of picture text -->
Phase 3 :<br>0.1<br>faster<br>vegetation<br>recovery<br>0.0<br>Phase 1 :<br>−0.1<br>more fuel<br>reduction<br>−0.2<br>0 100 200 300<br>Phase Shift (days)<br>2023 Unit 1 VMP Statistically significant<br>Rx fires 2023 Loafer Creek ( p  < 0.05)<br>2024 Middle Ridge Unit C Not statistically significant<br>() DID δ<br><!-- End of picture text -->

Figure 5. Post-treatment fuel reduction (phase 1) and post-wildfire vegetation recovery (phase 3) effects with varying phase shifts for three Rx fires: 2023 Unit 1 VMP, 2023 Loafer Creek, and 2024 Middle Ridge Unit C. A positive phase shift (in days) moves the time window of a given phase forward in time to quantify the persistence of the Rx fire effects. The baseline scenario is a phase shift of 0 days with a phase length of 60 days. Phase 1 scenarios where the phase window overlaps with the wildfire duration are excluded. 

By shifting the phase window, we can use DID to quantify the persistence of the post-treatment fuel reduction (phase 1) and post-wildfire vegetation recovery (phase 3) effects. Figure 5 shows an example of this calculation for the 2023 Unit 1 VMP, 2023 Loafer Creek, and 2024 Middle Ridge Unit C Rx fires. A phase shift of 0 days represents the baseline scenario with a 60day phase length. For phase 1, we observe statistically significant fuel reduction effects for each of the three Rx fires up to the time of ignition of the Park Fire. The fuel reduction effect persisted over 200 days for the 2023 Unit 1 VMP and 2023 Loafer Creek Rx fires. For phase 3, the persistence of the faster vegetation recovery effect can vary widely, to potentially over a year (e.g., 2023 Unit 1 VMP). The end of the persistence effect in phase 3 indicates the convergence of treated and control areas in vegetation state and the end of the post-wildfire recovery period. 

## **3.3 Strengths and Limitations** 

Compared to HLS, we find that moderate-resolution sensors such as MODIS and VIIRS (500 m) are often unable to capture deviations in vegetation indices within small Rx fire footprints compared to surrounding control areas. MODIS and VIIRS pixels may be larger than the Rx fire treatments, and the VI timeseries have higher day-to-day variation. While the effective temporal resolution of HLS is up to every 1.4 days, cloud cover 

and thick haze can still decrease the usability of available images. Our step of adding weights to the DID linear regression models ameliorates the influence of observations from cloud- or hazecontaminated sciences. 

Our framework can be scaled on a regional to nationwide level to quantify the general effectiveness of fuel treatments across a variety of lag times, treatment types, fuel types, and topography. Recent efforts to build regional to national databases of fuel treatments in the U.S., such as the National Fuels Treatment Initiative (NFT) geodatabase and the Treatment and Wildfire Interagency Geodatabase (TWIG), are particularly relevant for expanding our DID timeseries analysis (Call et al., 2025; Cummins et al., 2023). Other types of fuel treatments, such as mechanical thinning, hand thinning, and grazing, can be similarly assessed in our framework if there are corresponding geospatial and temporal metadata. On-the-ground surveys and reports of individual treatments, such as from CAL FIRE’s Fuels Treatment Effectiveness Reports (FTER) and the California Prescribed Fire Monitoring Program dataset, can complement remote sensing methods by contextualizing treatment history and timing and wildfire active suppression (Domènech et al., 2026). Specifically, a major limitation is poor metadata quality in Rx fire and fuels treatment datasets. For example, time ranges reported for some treatments in the FRAP dataset ambiguously spanned multiple 

This contribution has been peer-reviewed. 

https://doi.org/10.5194/isprs-archives-XLIX-B3-2026-987-2026 | © Author(s) 2026. CC BY 4.0 License. 

991 

The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences, Volume XLIX-B3-2026 XXV ISPRS Congress 2026 “From Imagery to Understanding”, Commission III, 4–11 July 2026, Toronto, Canada 

years, and only a small portion of some Rx fire polygons are reported as treated. Thus, more rigorous data cleaning is needed to validate, and possibly correct, metadata in Rx fire and fuels treatment datasets. 

We also generalize the definition of the control area to any treatment polygon, which differs from previous study designs based on points or transects (Jones et al., 2025; Kelp et al., 2025). Modifications to the control and treatment polygon definitions can be applied to account for previous treatment and wildfire history. Additional methods of defining the control polygon, such as spatial displacement of the treatment polygon in different directions, can be tested. Finally, our current framework does not quantify the ability of fuel treatments to act as a fire break, such as altering the wildfire boundary and the rate and direction of wildfire spread. Incorporating our framework with fire spread models and satellite-derived fire progression datasets may help to elucidate both the temporal and spatial effects of fuel treatments on wildfires (Andrews, 2018; Chen et al., 2022; Lautenberger, 2013; Liu et al., 2024). 

While spectral indices can be readily derived from satellite surface reflectance, converting VIs to physical biomass quantities such as aboveground biomass and leaf area index via statistical modeling can enhance the interpretability of the DID analysis (Alexandridis et al., 2020; Shendryk, 2022). Atmospheric transport modeling with air quality observations, such as from U.S. Environmental Protection Agency (EPA) monitors or low-cost PurpleAir sensors, can provide additional constraints on the timing, intensity, and emissions of Rx fires, as well as smoke-related public health assessments (Chung et al., 2025; Kelp et al., 2025, 2023; Schollaert et al., 2024). 

## **4. Conclusion** 

In summary, we introduce a framework using satellite-based timeseries analysis with DID estimation to more robustly quantify the effect of Rx fires in three time phases: posttreatment, wildfire, and post-wildfire. The HLS collection uniquely enables our analysis at 30-m spatial resolution and improved temporal frequency up to every 1.4 days. Using 37 Rx fires that preceded and intersected the 2024 Park Fire as a case study, we find evidence of increased post-treatment fuel reduction (phase 1), wildfire burn severity mitigation (phase 2), and faster post-wildfire vegetation recovery (phase 3) in treated areas compared to control areas. Our framework moves toward more robust estimation of Rx fire effects across a wide range of landscapes, ultimately benefiting land managers, policymakers, and communities in evaluating the costs and benefits of fuel treatments. 

## **Acknowledgements** 

T. Liu and K. Otobe acknowledge funding from the UBC Arts Undergraduate Research Awards (AURA) in Summer 2025. 

## **References** 

Alexandridis, T.K., Ovakoglou, G., Clevers, J.G.P.W., 2020: Relationship between MODIS EVI and LAI across time and space. _Geocarto Int._ , 35, 1385–1399. https://doi.org/10.1080/10106049.2019.1573928 

Andrews, P.L., 2018: The Rothermel Surface Fire Spread Model and Associated Developments: A Comprehensive Explanation. Gen. Tech. Rep. RMRS-GTR-371. U.S. Department of Agriculture, Forest Service, Rocky Mountain Research Station. 

Baker, A., Callaway, B., Cunningham, S., Goodman-Bacon, A., Sant’Anna, P.H.C., 2025: Difference-in-Differences Designs: A Practitioner’s Guide. _ArXiv_ . https://doi.org/10.48550/arXiv.2503.13323 

Burke, M., Childs, M.L., de la Cuesta, B., Qiu, M., Li, J., Gould, C.F., Heft-Neal, S., Wara, M., 2023: The contribution of wildfire to PM2.5 trends in the USA. _Nature_ , 622, 761-766. https://doi.org/10.1038/s41586-023-06522-6 

Call, A., Tomczyk, N., Withnall, K.A., Dappen, P.R., Heusinkveld, D., Mueller, S., Holloway, B., Shennan, K., Herring, J., Franko, A., Colavito, M.M., Kimple, A.D., Meador, A.S., Stevens-Rumann, C.S., 2025: A new geodatabase of fuel treatments across federal lands in the USA. _Sci. Data,_ 12, 1485. https://doi.org/10.1038/s41597-025-05859-z 

Chen, Y., Hantson, S., Andela, N., Coffield, S.R., Graff, C.A., Morton, D.C., Ott, L.E., Foufoula-Georgiou, E., Smyth, P., Goulden, M.L., Randerson, J.T., 2022: California wildfire spread derived using VIIRS satellite observations and an object-based tracking system. _Sci. Data_ , 9, 249. https://doi.org/10.1038/s41597-022-01343-0 

Chung, K.E., Liu, T., Kelp, M.M., Vohra, K., Skelly, D., Carroll, M.C., Schwartz, J., Mickley, L.J., 2025: Managing Smoke Risk from Wildland Fires: Northern California as a Case Study. _Environ. Sci. Technol.,_ 59, 13912–13923. https://doi.org/10.1021/acs.est.5c01914 

Cummins, K., Noble, J., Varner, J.M., Robertson, K.M., Hiers, J.K., Nowell, H.K., Simonson, E., 2023: The Southeastern US Prescribed Fire Permit Database: Hot Spots and Hot Moments in Prescribed Fire across the Southeastern USA. _Fire_ , 6, 372. https://doi.org/10.3390/fire6100372 

Domènech, R., Naimeh, A.M., Putz, T., Grupenhoff, A.R., Schlueter, M., Boynton, R.M., Williams, J., Sapsis, D.B., Restaino, J., Tase, N., Estes, B.L., Safford, H.D., 2026: California Prescribed Fire Monitoring Program: dataset 20192024. _Sci. Data_ , 13, 225. https://doi.org/10.1038/s41597-02506509-0 

Gorelick, N., Hancher, M., Dixon, M., Ilyushchenko, S., Thau, D., Moore, R., 2017: Google Earth Engine: Planetary-scale geospatial analysis for everyone. _Remote. Sens. Environ_ . 202, 18–27. https://doi.org/10.1016/j.rse.2017.06.031 

Huber-Stearns, H., Chapman, D., Downey, J., Coughlan, M.R., 2025: _Synthesizing Public Opinion on Prescribed Fire and Associated Smoke Smoke: A Review of Peer-Reviewed Literature in the Pacific Northwest United States._ Northwest Fire Science Consortium. 

Jaffe, D.A., O’Neill, S.M., Larkin, N.K., Holder, A.L., Peterson, D.L., Halofsky, J.E., Rappold, A.G., 2020: Wildfire and prescribed burning impacts on air quality in the United States. _J. Air Waste Manage. Assoc._ , 70, 583–615. https://doi.org/10.1080/10962247.2020.1749731 

Jain, T.B., Abrahamson, I., Anderson, N., Hood, S., Hanberry, B., Kilkenny, F., Mckinney, S., Ott, J., Urza, A., Chambers, J., Battaglia, M., Varner, J.M., O’Brien, J.J., 2021: Effectiveness of Fuel Treatments at the Landscape Scale: State of Understanding and Key Research Gaps. 

This contribution has been peer-reviewed. https://doi.org/10.5194/isprs-archives-XLIX-B3-2026-987-2026 | © Author(s) 2026. CC BY 4.0 License. 

992 

The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences, Volume XLIX-B3-2026 XXV ISPRS Congress 2026 “From Imagery to Understanding”, Commission III, 4–11 July 2026, Toronto, Canada 

Jones, B.A., McDermott, S., Champ, P.A., Berrens, R.P., 2022. More smoke today for less smoke tomorrow? We need to better understand the public health benefits and costs of prescribed fire _. Int. J. Wildland Fire_ , 31, 918–926 _._ https://doi.org/10.1071/WF22025 

Jones, G.M., Spannuth, A., Chongpinitchai, A., Hurteau, M.D., 2025. Prescribed fire, managed burning, and previous wildfires reduce the severity of a southwestern US gigafire. _For. Ecol. Manage._ 580, 122540. https://doi.org/10.1016/j.foreco.2025.122540 

Ju, J., Zhou, Q., Freitag, B., Roy, D.P., Zhang, H.K., Sridhar, M., Mandel, J., Arab, S., Schmidt, G., Crawford, C.J., Gascon, F., Strobl, P.A., Masek, J.G., Neigh, C.S.R., 2025: The Harmonized Landsat and Sentinel-2 version 2.0 surface reflectance dataset. _Remote Sens. Environ._ 324, 114723. https://doi.org/10.1016/j.rse.2025.114723 

Kelp, M., Burke, M., Qiu, M., Higuera-Mendieta, I., Liu, T., Diffenbaugh, N., 2025: Effect of recent prescribed burning and land management on wildfire burn severity and smoke emissions in the western United States. _AGU Adv._ , 6, e2025AV001682. https://doi.org/10.1029/2025AV001682. 

Kelp, M., Carroll, M., Liu, T., Yantosca, R.M., Hockenberry, H.E., Mickley, L.J., 2023: Prescribed burns as a tool to mitigate future wildfire smoke exposures: Lessons for states and environmental justice communities. _Earth’s Future_ , 11(6), e2022EF003468. https://doi.org/10.1029/2022EF003468 

Key, C.H., Benson, N.C., 2006: Landscape Assessment (LA). In: Lutes, D.C., Keane, R.E., Caratti, J.F.; Key, C.H., Benson, N.C.; Sutherland, S., Gangi, L.J., 2006: _FIREMON: Fire effects monitoring and inventory system_ , USDA Forest Service General Technical Report RMRS-GTR-164-CD. 

Kreider, M.R., Higuera, P.E., Parks, S.A., Rice, W.L., White, N., Larson, A.J., 2024: Fire suppression makes wildfires more severe and accentuates impacts of climate change and fuel accumulation. _Nat. Commun._ , 15, 2412. https://doi.org/10.1038/s41467-024-46702-0 

Wilson, K.N., Wolff, N.H., Spector, J.T., 2024: Quantifying the smoke-related public health trade-offs of forest management. _Nat. Sustain._ , 7, 130–139. https://doi.org/10.1038/s41893-02301253-y 

Schultz, C.A., McCaffrey, S.M., Huber-Stearns, H.R., 2019: Policy barriers and opportunities for prescribed fire application in the western United States. _Int. J. Wildland Fire_ , 28, 874–884. https://doi.org/10.1071/WF19040 

Shendryk, Y., 2022. Fusing GEDI with earth observation data for large area aboveground biomass mapping. _Int. J. Appl. Earth Obs. Geoinf._ , 115, 103108. https://doi.org/10.1016/j.jag.2022.103108 

Swain, D.L., Abatzoglou, J.T., Kolden, C., Shive, K., Kalashnikov, D.A., Singh, D., Smith, E., 2023: Climate change is narrowing and shifting prescribed fire windows in western United States. _Commun. Earth Environ._ , 4, 340. https://doi.org/10.1038/s43247-023-00993-1 

Worsham, A., Armstrong, M., Coop, J.D., Signorelli, D., 2025: When the wilderness burns: an analysis of current fire management and the case for prescribed fire in designated wilderness in the United States. _Fire Ecol.,_ 21, 81. https://doi.org/10.1186/s42408-025-00414-y 

Wu, X., Sverdrup, E., Mastrandrea, M.D., Wara, M.W., Wager, S., 2023: Low-intensity fires mitigate the risk of high-intensity wildfires in California’s forests. _Sci. Adv._ , 9(45), eadi4123. https://doi.org/10.1126/sciadv.adi4123 

Xiang, H., Liu, J., Cao, C., Xu, M., 2013: Algorithms for Moderate Resolution Imaging Spectroradiometer cloud-free image compositing. _J. Appl. Remote Sens._ , 7, 073486. https://doi.org/10.1117/1.JRS.7.073486 

Yengoh, G.T., Dent, D., Olsson, L., Tengberg, A.E., Tucker, C.J., 2015: _Use of the Normalized Difference Vegetation Index (NDVI) to Assess Land Degradation at Multiple Scales: Current Status, Future Trends, and Practical Considerations_ , SpringerBriefs in Environmental Science. Springer International Publishing. https://doi.org/10.1007/978-3-319-24112-8 

Lautenberger, C., 2013: Wildland fire modeling with an Eulerian level set method and automated calibration. _Fire Saf. J._ , 62, 289– 298. https://doi.org/10.1016/j.firesaf.2013.08.014 

Li, S., Baijnath-Rodino, J.A., York, R.A., Quinn-Davidson, L.N., Banerjee, T., 2025: Temporal and spatial pattern analysis of escaped prescribed fires in California from 1991 to 2020. _Fire Ecol._ , 21, 3. https://doi.org/10.1186/s42408-024-00342-3 

Liu, T., Mickley, L.J., Gautam, R., Singh, M.K., DeFries, R.S., Marlier, M.E., 2021: Detection of delay in post-monsoon agricultural burning across Punjab, India: potential drivers and consequences for air quality. _Environ. Res. Lett._ , 16, 014014. https://doi.org/10.1088/1748-9326/abcc28 

Liu, T., Randerson, J.T., Chen, Y., Morton, D.C., Wiggins, E.B., Smyth, P., Foufoula-Georgiou, E., Nadler, R., Nevo, O., 2024: Systematically tracking the hourly progression of large wildfires using GOES satellite observations. _Earth Syst. Sci. Data_ , 16, 1395–1424. https://doi.org/10.5194/essd-16-1395-2024 

Schollaert, C.L., Jung, J., Wilkins, J., Alvarado, E., Baumgartner, J., Brun, J., Busch Isaksen, T., Lydersen, J.M., Marlier, M.E., Marshall, J.D., Masuda, Y.J., Maxwell, C., Tessum, C.W., 

This contribution has been peer-reviewed. https://doi.org/10.5194/isprs-archives-XLIX-B3-2026-987-2026 | © Author(s) 2026. CC BY 4.0 License. 

993 


