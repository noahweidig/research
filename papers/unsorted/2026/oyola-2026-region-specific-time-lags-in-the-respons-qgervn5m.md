---
title: Region-specific time lags in the response of black carbon to ENSO from 46 years of MERRA-2 reanalysis
authors:
- Oyola, Mayra I.
year: '2026'
journal: null
doi: 10.5194/egusphere-2026-6022
tags:
- burning
- united states
zotero_key: QGERVN5M
item_type: journalArticle
url: https://openalex.org/W7223048851
source_url: 'unpaywall: https://egusphere.copernicus.org/preprints/2026/egusphere-2026-6022/egusphere-2026-6022.pdf'
fulltext_status: fulltext
synced: '2026-11-06'
---

# Region-specific time lags in the response of black carbon to ENSO from 46 years of MERRA-2 reanalysis

## Abstract

Abstract. The relationship between El Niño-Southern Oscillation (ENSO) and global black carbon (BC) loading is not described by a single timescale. Using 46 years (1980 to 2025) of MERRA-2 reanalysis, we regress BC column mass anomalies against the Oceanic Niño Index at lags of 0 to 12 months at every grid point, accounting for autocorrelation and applying false discovery rate (FDR) correction. BC responds to ENSO on region-specific lags: near zero over the Maritime Continent, about five months over Central America, and seven to eight months over the Amazon. These lags are reproduced in 1980 to 2009 and 2010 to 2025, periods driven by different biomass burning emission inventories, so the timing is not an artifact of the inventory or of the 1997 to 1998 El Niño, and it is consistent with the pan-tropical cascade of fire anomalies documented in satellite fire records. No relationship is detectable over the continental United States, central Africa, or Siberia in either period; over the continental United States, the largest full-record median correlation (0.03) is about one fifth of the smallest detectable correlation, partly because weak correlations of opposite sign in the two periods cancel. The fraction of grid points passing FDR correction changes abruptly between adjacent lags while correlation strength varies smoothly, so response timing is better read from correlation magnitude than from significance counts. Anticipating ENSO-driven aerosol loading therefore requires resolving when the relationship emerges in each region, not only whether it exists.

## Full text

https://doi.org/10.5194/egusphere-2026-6022 Preprint. Discussion started: 20 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





# **Region-specific time lags in the response of black carbon to ENSO from 46 years of MERRA-2 reanalysis** 

Mayra I. Oyola<sup>1</sup> 

1University of Wisconsin-Madison, Madison, WI 53706, USA 

**Correspondence:** Mayra I. Oyola (oyolamerced@wisc.edu) 

**Abstract.** The relationship between El Niño-Southern Oscillation (ENSO) and global black carbon (BC) loading is not described by a single timescale. Using 46 years (1980 to 2025) of MERRA-2 reanalysis, we regress BC column mass anomalies against the Oceanic Niño Index at lags of 0 to 12 months at every grid point, accounting for autocorrelation and applying false discovery rate (FDR) correction. BC responds to ENSO on region-specific lags: near zero over the Maritime Continent, about 

- 5 five months over Central America, and seven to eight months over the Amazon. These lags are reproduced in 1980 to 2009 and 2010 to 2025, periods driven by different biomass burning emission inventories, so the timing is not an artifact of the inventory or of the 1997 to 1998 El Niño, and it is consistent with the pan-tropical cascade of fire anomalies documented in satellite fire records. No relationship is detectable over the continental United States, central Africa, or Siberia in either period; over the continental United States, the largest full-record median correlation (0.03) is about one fifth of the smallest detectable 

- 10 correlation, partly because weak correlations of opposite sign in the two periods cancel. The fraction of grid points passing FDR correction changes abruptly between adjacent lags while correlation strength varies smoothly, so response timing is better read from correlation magnitude than from significance counts. Anticipating ENSO-driven aerosol loading therefore requires resolving when the relationship emerges in each region, not only whether it exists. 

## **1 Introduction** 

- 15 El Niño-Southern Oscillation (ENSO) is the dominant mode of interannual climate variability (McPhaden et al., 2006), with documented influence on fire activity and aerosol loading across multiple continents (van der Werf et al., 2004). Over the Maritime Continent, El Niño-driven drought strengthens dry-season biomass burning emissions of black carbon (BC), with the eastern Pacific type of El Niño producing a stronger response than the central Pacific type (Xie et al., 2023). BC can also feed back on ENSO itself: emissions at mid-latitudes and in the Arctic weaken meridional heat transport and increase the frequency 

- 20 of extreme ENSO events (Lou et al., 2019). 

Existing characterizations of the ENSO and BC relationship are limited in spatial or temporal scope. Pereira et al. (2024) applied cross-correlation between ENSO and MERRA-2 black carbon over the Legal Amazon, finding phase lags of four to six months, but over a single region and a five-year record spanning only four ENSO events. Hoell et al. (2026) separately established that ENSO alters the likelihood of extensive wildfire area burned across the contiguous United States by up to 

- 25 twelve months in advance, using burned-area records from 1984 to 2022; whether a comparable lagged relationship exists 

**1** 

https://doi.org/10.5194/egusphere-2026-6022 Preprint. Discussion started: 20 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





in column-integrated aerosol loading over the same region remains untested. For fire activity itself, Chen et al. (2017) used satellite burned area and fire emissions for six El Niño and six La Niña events between 1997 and 2016 to document a pantropical cascade: fire anomalies peak in equatorial Asia while El Niño is strengthening (August to October), and in Central America (March to May) and the southern Amazon (July to October) of the following year. Whether this cascade carries 30 through to atmospheric aerosol loading, and whether it holds over a record that extends before the satellite fire era, has not been examined. 

No study has characterized the ENSO and BC relationship at global scale, at native reanalysis resolution, over a multi-decadal record, with lag and regional structure resolved simultaneously. This gap is consequential: if the timescale over which BC responds to ENSO varies by region, a single global or zero-lag characterization risks under- or mis-estimating the relationship 35 in exactly the regions where it matters most for anticipating aerosol loading. Because ENSO recurs on a roughly 2 to 7 year cycle, resolving this region-specific timing has recurring operational relevance for anticipating aerosol loading in advance of future events. 

Here, we use 46 years of MERRA-2 reanalysis to characterize the relationship between ENSO and global BC column mass anomalies, testing lags of 0 to 12 months at each grid point with significance assessed via an effective-sample-size correction 40 for autocorrelation (Bretherton et al., 1999) and false discovery rate correction across grid points. We show that the strength and characteristic lag of the relationship vary substantially by region, that the lags are reproduced under different biomass burning emission inventories, and that no relationship is detectable over the continental United States, central Africa, or Siberia, with a quantitative bound on how large any undetected relationship could be. 

## **2 Data and Methods** 

- 45 We use monthly-mean black carbon column mass (BCCMASS) from the MERRA-2 reanalysis aerosol product (Global Modeling and Assimilation Office (GMAO), 2015), whose aerosol assimilation system is described in Randles et al. (2017) and Buchard et al. (2017), spanning January 1980 through December 2025 (552 months) at native 0.5° _×_ 0.625° resolution, globally. At each grid point we remove the climatological monthly cycle and a linear trend fit over the full record, yielding a deseasonalized, detrended BC anomaly. We use the Oceanic Niño Index (ONI; NOAA PSL), a 3-month running-mean Niño 

- 50 3.4 SST anomaly, aligned to the BC anomaly time series by calendar year-month. ONI was chosen because it is the operational index NOAA uses to classify ENSO events and the index used by the two most directly comparable prior studies (Pereira et al., 2024; Hoell et al., 2026), and because its continuous monthly values are better suited to linear regression than binary or categorical indices such as the Southern Oscillation Index. 

- Because MERRA-2’s climatological BC background is negligible over large areas of open ocean (e.g., the Southern Ocean), 

- 55 a numerically tiny anomaly there can register as a large relative swing and pass significance testing without being physically meaningful. We therefore exclude grid points where the time-mean BC column mass falls below the 10th percentile of its global distribution (1.0 _×_ 10<sup>_−_7</sup> kg m<sup>_−_2</sup> ) from all analyses and figures, leaving 187,142 of 207,936 grid points. This magnitude mask 

**2** 

https://doi.org/10.5194/egusphere-2026-6022 Preprint. Discussion started: 20 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





altered only the Maritime Continent’s grid point count (excluding a small number of low-background oceanic edge points, 3977 to 3880) and did not change any significance fraction or null result reported in this study. 

60 We characterize the ENSO and BC relationship two ways. First, we classify each month as El Niño, La Niña, or neutral using the standard ONI criterion ( _|_ ONI _| ≥_ 0 _._ 5<sup>_◦_</sup> C for _≥_ 5 consecutive overlapping seasons), group consecutive months into discrete events, and composite the mean anomaly across El Niño and La Niña events separately at each grid point, treating each event rather than each month as one independent sample. This yields 24 El Niño and 18 La Niña events (139 and 134 months, respectively). Significance of the El Niño _−_ La Niña difference is assessed with a two-sided Mann-Whitney _U_ test 65 across event means. Second, we regress BC anomaly linearly against the full monthly ONI series at each grid point, using all available months rather than the discrete event classification. To examine the seasonal dependence of the zero-lag relationship, we repeat the regression separately for each meteorological season (DJF, MAM, JJA, SON) using only the months within that season. 

Both the ONI and BC anomaly series are strongly autocorrelated, so treating each month as an independent sample would 70 overstate significance. We correct for this using the effective-sample-size approach of Bretherton et al. (1999): the lag-1 autocorrelation of each series adjusts the degrees of freedom used in the significance test. Across the domain, median effective _N_ is approximately 180 of a raw _N_ of 552. Because both tests are performed independently at each of the domain’s grid points, we apply Benjamini-Hochberg false discovery rate (FDR) correction at _α_ = 0 _._ 05 across all grid points (Benjamini and Hochberg, 1995), controlling the expected proportion of false positives among flagged grid points rather than the per-grid-point 75 error rate. 

To account for a possible delay between ENSO forcing and BC response, we repeat the regression and significance testing with ONI shifted to lead BC anomaly by 0 to 12 months at monthly steps. A 12-month window was chosen to match the maximum lag examined in the most directly comparable prior study (Hoell et al., 2026), while remaining short enough to avoid conflating a given ENSO event’s response with the onset of a subsequent, independent event, given ENSO’s characteristic 2 to 80 7 year recurrence interval. At each grid point we identify the lag at which _|r|_ is maximized and report the regression slope and lag at that point, restricted to grid points that are FDR-significant at that lag. 

We summarize the lag structure within six regional boxes (Table 1): three biomass burning regions with a strong signal in the global maps (Maritime Continent, Central America, Amazon) and three regions examined for the absence of one (continental United States, hereafter CONUS; central Africa; Siberia/NE Asia). For each region and lag we compute the median _|r|_ and 85 median effective sample size _N_ eff across the region’s grid points and, to assess the sign of the relationship, the median signed _r_ and the fraction of grid points with _r >_ 0. We take each region’s characteristic lag as the lag at which the regional median _|r|_ peaks, and use FDR correction to determine whether the relationship at that lag is significant. We do not locate the peak from the fraction of significant grid points, because that fraction is sensitive to the adaptive Benjamini-Hochberg threshold (Sect. 3.3). 

90 Global FDR correction pools _p_ -values across a spatially heterogeneous domain, so the threshold applied in any one region depends on the strength of the signal elsewhere. We therefore repeat the FDR correction separately within each regional box and compare the number of grid points significant under region-restricted and global correction, treating the comparison as 

**3** 

https://doi.org/10.5194/egusphere-2026-6022 Preprint. Discussion started: 20 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





a sensitivity test. To bound the size of any relationship that the test fails to detect, we compute for each region and lag the minimum detectable correlation, 

95 



<!-- Start of picture text -->
tc<br>r min = √ t 2 c  +  N eff  − 2 , (1)<br><!-- End of picture text -->

where _tc_ is the two-sided critical value of Student’s _t_ distribution at _α_ = 0 _._ 05 with _N_ eff _−_ 2 degrees of freedom and _N_ eff is the regional median effective sample size. Because no multiple-comparison correction is applied, _r_ min is the most permissive detection threshold; a regional median _|r|_ below _r_ min cannot be attributed to an overly strict significance procedure. 

Biomass burning emissions in MERRA-2 come from three inventories over the record: a scaled version of RETROv2 from 100 1980 to 1996, scaled monthly GFED version 3.1 from 1997 to 2009, and daily QFED version 2.4 from 2010 onward, with the earlier inventories scaled to QFED to reduce discontinuities between them (Randles et al., 2017). To test whether the lag structure depends on the emission inventory, we repeat the full analysis separately for 1980 to 2009 and 2010 to 2025, recomputing the climatology, trend, effective sample size, and FDR correction within each period. The magnitude mask is computed once from the full record so that all periods evaluate the same grid points. The split at 2010 separates the period 105 driven by daily QFED emissions from the earlier scaled inventories; the GFED period alone (1997 to 2009, 13 years) is too short to analyze separately. For display, we also compute area-weighted (cosine of latitude) regional mean anomalies for the three regions with a detectable relationship and compare them with ONI shifted by each region’s characteristic lag. 

**Table 1.** Regional boxes used in the analysis. 

|Region|Longitude|Latitude|
|---|---|---|
|Maritime Continent|95°E to 155°E|10°S to 10°N|
|Central America|105°W to 75°W|8°N to 25°N|
|Amazon|75°W to 50°W|15°S to 5°N|
|CONUS|125°W to 66°W|24°N to 50°N|
|Central Africa|10°E to 30°E|10°S to 5°N|
|Siberia/NE Asia|100°E to 170°E|45°N to 70°N|



## **3 Results** 

## **3.1 Zero-Lag Composite and Regression** 

- 110 The El Niño and La Niña composite BC anomalies, and their difference, show the strongest and most spatially coherent signal over the Maritime Continent, with a positive El Niño anomaly and a corresponding negative La Niña anomaly (Fig. 1). In the composite difference, significance after FDR correction is concentrated over the Maritime Continent and eastern Australia, with smaller significant areas over the Caribbean and northern South America; anomalies over central Africa and the Amazon are weaker and largely not significant at the event level. 

**4** 

https://doi.org/10.5194/egusphere-2026-6022 Preprint. Discussion started: 20 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 115 The response is not symmetric between the two phases (Fig. 1). In the El Niño composite, positive anomalies extend from the Maritime Continent into mainland Southeast Asia and eastern Australia. The La Niña composite is not a mirror image of this pattern: alongside the negative Maritime Continent anomaly, it shows positive anomalies over the Indo-Gangetic Plain and eastern China and over the southern Amazon, where the El Niño composite is weakly negative. Over central Africa, both composites show negative anomalies near the equator. None of these asymmetric features is significant in the composite 

- 120 difference. 

The zero-lag regression of BC anomaly against the continuous ONI series (Fig. 2) shows the same Maritime Continent maximum: 56,768 of the 187,142 magnitude-unmasked grid points are FDR significant at zero lag. Over the southern Amazon, zero-lag regression coefficients are negative, consistent with the La Niña composite, while coefficients over the northern Amazon are positive. 

## 125 **3.2 Seasonal Dependence** 

The zero-lag relationship depends strongly on season (Fig. 3). Over the Maritime Continent, regression coefficients are positive and FDR significant in all four seasons, with the largest and most extensive response in SON, extending from Indonesia across northern Australia. Over Central America and northern South America, positive coefficients are largest in MAM, although they are not significant after FDR correction in that season; in DJF, positive coefficients over northern South America and the 130 adjacent Caribbean are significant. Over the southern Amazon, zero-lag coefficients are negative in JJA and SON, consistent with the response there emerging at longer lags rather than concurrently (Sect. 3.3). Large coefficients over boreal North America and Siberia in JJA are not significant after FDR correction. 

## **3.3 Lag Structure** 

Repeating the regression with ONI leading BC anomaly by 0 to 12 months shows that the strength and timing of the relationship 135 vary by region (Figs. 4 and 5; Table 2). 

**5** 

https://doi.org/10.5194/egusphere-2026-6022 Preprint. Discussion started: 20 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





**Table 2.** Regional summary of the ENSO and BC lag analysis (0 to 12 month lags tested, ONI leading) for the full record and the two emission inventory periods, given as full record / 1980 to 2009 / 2010 to 2025. For the Maritime Continent, Central America, and the Amazon, values are at the lag of peak median _|r|_ in each period. For the remaining regions, which have no detectable relationship, the largest median _|r|_ across all lags is given with _r_ min at that lag. The last column gives the fraction of grid points significant under region-restricted FDR correction in the full record, at the full-record peak lag. 

|Region|Peak lag (months)|Median_|r|_|_r_min|Region-restricted|FDR|
|---|---|---|---|---|---|
|||||significant||
|Maritime Continent|0 / 0 / 0|0.41 / 0.44 / 0.39|0.15 / 0.20 / 0.22|100% (3880/3880)||
|Central America|5 / 5 / 5|0.19 / 0.23 / 0.19|0.14 / 0.19 / 0.21|70% (1205/1715)||
|Amazon|8 / 7 / 7|0.20 / 0.18 / 0.22|0.14 / 0.17 / 0.24|77% (1290/1681)||
|CONUS|none|0.03 / 0.15 / 0.14|0.14 / 0.19 / 0.20|0% at all lags||
|Central Africa|none|0.10 / 0.13 / 0.09|0.13 / 0.16 / 0.20|0% at all lags||
|Siberia/NE Asia|none|0.06 / 0.14 / 0.10|0.14 / 0.19 / 0.19|0% at all lags||



Over the Maritime Continent, median _|r|_ peaks at zero lag (0.41), with all 3880 grid points significant under region-restricted FDR, and decreases monotonically to below _r_ min by lag 6. Over Central America, median _|r|_ peaks at lag 5 (0.19), with 70% of grid points significant. Over the Amazon, median _|r|_ rises from 0.08 at zero lag to a broad maximum of 0.20 at lags 7 and 8 (Fig. 5, left), with 77% of grid points significant at lag 8. 

140 The fraction of grid points passing FDR correction does not track this smooth evolution (Fig. 5, right). Over the Amazon, the region-restricted significant fraction jumps from 35% at lag 5 to 93% at lag 6, while median _|r|_ increases only from 0.15 to 0.18. Over Central America, it falls from 66% at lag 6 to zero at lag 7, although median _|r|_ at lag 7 (0.150) still exceeds _r_ min (0.139). These jumps reflect the adaptive Benjamini-Hochberg threshold, which tightens abruptly once the number of small _p_ -values in a region falls. For this reason we locate each region’s peak from median _|r|_ rather than from significance counts. 

## 145 **3.4 Relationships Away From the Source Regions** 

Significant relationships also appear far from the biomass burning regions (Figs. 2 and 4). At zero lag, significant positive coefficients cover much of the subtropical South Pacific between about 10°S and 40°S, the Indian Ocean from the Maritime Continent to northern Australia, the subtropical North Pacific, and a broad band of the Southern Ocean between about 45°S and 70°S (Fig. 2). Of the 56,768 grid points significant under global FDR correction at zero lag, 4604 (8%) lie within the six 150 regional boxes; the remaining 92% lie outside them, predominantly over the oceans. Regression coefficients over these oceanic regions are small compared with those over the source regions, mostly below 0.5 _×_ 10<sup>_−_7</sup> kg m<sup>_−_2</sup> °C<sup>_−_1</sup> . 

155 

In the lag analysis, the oceanic regions organize by lag (Fig. 4, bottom). The Indian Ocean and western Pacific around the Maritime Continent peak at lags of 0 to 1 months, matching the Maritime Continent itself. A region of the subtropical South Atlantic east of southern Brazil peaks at lags of 8 to 9 months, matching the Amazon, and a narrower region south of Africa peaks at 6 to 7 months. The subtropical South Pacific peaks at 0 to 1 months, the subtropical North Pacific at 3 to 4 months, 

**6** 

https://doi.org/10.5194/egusphere-2026-6022 Preprint. Discussion started: 20 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





and most of the Southern Ocean at 2 to 3 months. The seasonal maps show a further feature: in JJA, large positive coefficients extend westward from southern Africa over the tropical Atlantic, although they are not significant after FDR correction (Fig. 3). 

## **3.5 Regions Without a Detectable Relationship** 

Over CONUS, central Africa, and Siberia/NE Asia, no grid point is significant under region-restricted correction at any tested 160 lag (Fig. 5), although some pass the global correction at intermediate lags (up to 281 of 5035 over CONUS at lag 4, and 76 of 1023 over central Africa at lag 5). The minimum detectable correlation bounds the size of any relationship in these regions (Table 2). Over CONUS, the largest median _|r|_ at any lag (0.029) is about one fifth of _r_ min (0.137); over Siberia/NE Asia, the largest median _|r|_ (0.062) is less than half of _r_ min (0.139). Central Africa is closer to the threshold: median _|r|_ reaches 0.102 at lags 5 and 6, about three quarters of _r_ min (0.133). We therefore describe central Africa as having no relationship detectable 165 at this record length, rather than demonstrably none. Median effective sample sizes in all three regions (199 to 221) exceed the global median (177 to 180) at every lag, so the absence of significance does not reflect locally reduced sample size. 

The signs of these weak correlations differ between periods. Over CONUS, the signed median correlation at lags of 4 to 11 months is positive in 1980 to 2009, reaching +0.15 at lag 8 with 97% of grid points positive, and negative in 2010 to 2025, reaching _−_ 0.14 at lag 8 with 10% of grid points positive. The two periods largely cancel in the full record, where the signed 170 median at lag 8 is _−_ 0.01. Over Siberia/NE Asia, a positive correlation at lags of 5 to 12 months in 1980 to 2009 (+0.14 at lags 8 and 9) is absent in 2010 to 2025, where the signed median remains between _−_ 0.03 and +0.01 at all lags. Over central Africa, by contrast, the lagged correlation is positive in both periods, reaching +0.12 at lag 5 in 1980 to 2009 and +0.08 at lag 7 in 2010 to 2025, and in the full record 97% to 98% of grid points are positive at lags 5 and 6; only the zero-lag sign differs between periods. In every case the correlations remain below _r_ min. 

## 175 **3.6 Robustness Across Emission Inventory Periods** 

The regional lags are reproduced in both periods (Table 2). Median _|r|_ peaks at zero lag over the Maritime Continent in 1980 to 2009 (0.44) and 2010 to 2025 (0.39), at lag 5 over Central America (0.23 and 0.19), and at lag 7 over the Amazon (0.18 and 0.22). Peak correlations are therefore of similar magnitude in both periods, and over the Amazon slightly larger in the later period. Because the shorter periods have smaller effective sample sizes (global medians of about 104 and 91, compared with 180 180 for the full record), _r_ min is higher in each. In 2010 to 2025 the Amazon peak (0.22) falls just below its _r_ min (0.24), so no Amazon grid point is significant in that period despite a correlation as large as in the full record; Central America remains significant at 23% of grid points at lag 5. The 2010 to 2025 period excludes the 1997 to 1998 El Niño and is driven entirely by daily QFED emissions, so neither that event nor the earlier inventories account for the lags. 

Regional mean BC anomalies illustrate the same result (Fig. 6). Correlations between the regional mean anomaly and ONI 185 shifted by the regional lag are 0.53 and 0.45 over the Maritime Continent in the two periods, 0.22 and 0.16 over Central America, and 0.29 and 0.25 over the Amazon. Over CONUS, central Africa, and Siberia/NE Asia, median _|r|_ remains below _r_ min at every lag in both periods. The global extent of significance differs more between periods than the regional results do: 67,564 grid points are significant at zero lag in 1980 to 2009, compared with 9,467 in 2010 to 2025. Of these, 4172 and 

**7** 

https://doi.org/10.5194/egusphere-2026-6022 Preprint. Discussion started: 20 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





3355, respectively, lie within the six regional boxes, so the reduction occurs almost entirely outside them, where most of the 190 significant area in the full record is oceanic. 

## **4 Discussion** 

The region-specific lag structure is broadly consistent with differences in fire season timing relative to ENSO’s seasonal cycle. ENSO events typically peak in boreal winter; a five-month lag places the Central American response in spring, during the regional burning season, and a seven to eight month lag places the Amazon response in the austral dry season. Over the 195 Maritime Continent, El Niño drought develops during the same dry season in which peatland and forest fires occur (Xie et al., 2023), consistent with a near-immediate response. These correspondences are consistent with ENSO influencing BC through the timing of each region’s fire season, possibly through precipitation anomalies that accumulate over several months before burning, but we do not test the mechanism here. The Amazon result is broadly consistent with Pereira et al. (2024), who found 4 to 6 month phase lags between ENSO and MERRA-2 black carbon over a five-year subset of the same region; our 46-year 200 record places the peak at 7 to 8 months. 

200 

The lags agree closely with the timing of fire anomalies documented by Chen et al. (2017). Their fire anomalies peak in equatorial Asia from August to October while El Niño is strengthening, matching the zero lag over the Maritime Continent, and in Central America from March to May and in the southern Amazon from July to October of the following year. Counting from an ENSO peak in boreal winter, our lags of 5 and 7 to 8 months fall in April to May and July to August, within those 205 windows. The agreement indicates that the pan-tropical fire cascade is carried into column BC loading. It is not, however, an independent confirmation over the period after 1997: from then on, MERRA-2 biomass burning emissions are scaled from GFED and QFED, which derive from satellite fire observations closely related to those analyzed by Chen et al. (2017). What the reanalysis adds is the response of the aerosol column itself, including its persistence downwind of the source regions, over a record more than twice as long. The reproduction of the lags in 1980 to 2009, a period that begins with the scaled 210 RETROv2 inventory, is consistent with the cascade operating before the satellite fire era, although we have not evaluated how much observed interannual variability that inventory contains. Over South America, Chen et al. (2011) found that ONI correlates with fire activity in the eastern Amazon, whereas tropical North Atlantic variability is more closely linked to fire in the southern and southwestern Amazon, and used both to forecast fire season severity 3 to 5 months ahead. Our Amazon box spans both areas, so part of the Amazon signal not captured by ONI may reflect Atlantic variability. 

215 The sign of the Amazon relationship depends on lag. At zero lag, the regression over the southern Amazon is negative and the La Niña composite there is positive (Figs. 1 and 2), whereas at the lag of peak correlation the coefficient over the Amazon is positive (Fig. 4). This is consistent with the austral dry season responding to the ENSO state of the preceding boreal winter rather than to concurrent conditions, and with ENSO’s tendency to change phase between consecutive years, which makes the concurrent and lagged correlations differ in sign. The same phase change appears over the Maritime Continent, 220 where the correlation becomes negative at lags of 10 to 12 months (signed median _−_ 0.05 at lag 12, with 1% of grid points 

**8** 

https://doi.org/10.5194/egusphere-2026-6022 Preprint. Discussion started: 20 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





positive), although these values are below _r_ min. A zero-lag analysis alone would therefore not only underestimate the Amazon relationship but could assign it the opposite sign. 

225 

Because the same lags appear in 2010 to 2025, driven entirely by daily QFED emissions, and in 1980 to 2009, driven by the earlier scaled inventories, they are unlikely to be artifacts of a particular emission inventory. The later period also excludes the 1997 to 1998 El Niño and the extreme Indonesian fires of that year, so the lags do not depend on that event. The larger difference between periods lies in the global extent of significance, and it arises almost entirely outside the six regional boxes (Sect. 3.6), in the remote, largely oceanic regions discussed below. We do not determine its cause. Candidates include the larger ENSO events in the earlier period (1982 to 1983 and 1997 to 1998), differences in the assimilated aerosol observations between the periods, and the sensitivity of weak remote signals to both. 

230 The relationships over the oceans are consistent in part with transport of BC away from the source regions. The region of the South Atlantic east of southern Brazil shares the Amazon lag, and the Indian Ocean and western Pacific around the Maritime Continent share its zero lag, as expected for anomalies carried downwind from those sources. Other oceanic signals do not match a single upwind source. The Southern Ocean peaks at lags of 2 to 3 months and the subtropical North Pacific at 3 to 4 months, lags that do not correspond to any of the source regions examined here. These may reflect ENSO-related changes 235 in transport pathways or in wet removal over the ocean, which can modulate low background loading without any change in emissions. Because background BC over these oceans is small, small absolute changes can produce significant correlations, and their regression coefficients are several times to an order of magnitude smaller than over the source regions. They are nevertheless most of the significant area, so global counts of significant grid points mainly reflect these remote regions rather than the source regions. 

240 The asymmetry between the El Niño and La Niña composites is not represented by a linear regression on ONI. The positive La Niña anomalies over the Indo-Gangetic Plain and eastern China, regions where anthropogenic sources dominate BC, suggest that ENSO can modulate anthropogenic BC loading through circulation or precipitation rather than through fire, although these features are not significant in the event composites. Composites stratified by phase and lag would be needed to examine this asymmetry. 

245 No relationship between ENSO and BC is detectable over CONUS in the full record or in either period. This does not contradict Hoell et al. (2026), who found a significant lagged relationship between ENSO and wildfire area burned across US Geographic Area Coordination Centers using a direct fire-activity metric. Two factors could make an ENSO signal in column-integrated BC weak over CONUS even where fire activity responds. First, CONUS BC loading combines a fire-driven component with a large, ENSO-insensitive anthropogenic background (traffic, industrial combustion) that is largely absent in 250 the more fire-dominated Maritime Continent, Amazon, and Central American source regions, so a fire signal would be diluted in the column. Second, ENSO’s remote influence on midlatitude circulation propagates via Rossby wave trains along the subtropical jet waveguide (Hoskins and Karoly, 1981), a mechanism that is strongest in boreal winter, when tropical forcing is near its seasonal peak and the jet is closest to the tropics, and substantially weaker in boreal summer, when the dominance of tropical easterlies and a weaker, poleward-displaced jet limit Rossby wave propagation into midlatitudes (Jong et al., 2020). 

255 Fire season over the continental United States, and over Mediterranean Europe more broadly, occurs predominantly in boreal 

**9** 

https://doi.org/10.5194/egusphere-2026-6022 Preprint. Discussion started: 20 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





summer, when this pathway is weakest. We emphasize that this argument concerns the timing and physical pathway of the ENSO teleconnection itself; it is not an argument about the cause of recent severe fire seasons in the northern midlatitudes, which this analysis is neither designed nor intended to address. 

These two factors account for a weak signal, but not for the sign reversal over CONUS (Sect. 3.5). Within each period, 260 median _|r|_ reaches about 0.14 at lags of 7 to 9 months, positive in 1980 to 2009 and negative in 2010 to 2025, so the near-zero full-record value reflects cancellation between periods as well as weakness within them. The reversal coincides with the change from the earlier scaled inventories to daily QFED emissions in 2010, so we cannot determine whether it reflects a change in how ENSO affects BC over CONUS or a change in the emissions driving MERRA-2. Neither period’s correlation reaches _r_ min, and the sign reversal remains unexplained. Siberia/NE Asia shows a related pattern, with a lagged positive correlation 265 in the earlier period that is absent in the later one. Central Africa differs: its lagged correlation is positive in both periods and across nearly all of its grid points, which makes it the null region most likely to reach detection with a longer record. 

CONUS and central Africa each have grid points that pass global FDR correction but none that pass region-restricted correction. This reflects the different power of the two procedures rather than an error in either. The Benjamini-Hochberg procedure adapts its threshold to the distribution of _p_ -values being corrected, becoming more permissive when many small 270 _p_ -values are present, as in the global domain where the Maritime Continent and Amazon contribute strong signal, and stricter when few are, as within a region with weak signal. The adaptation works in both directions: over the Maritime Continent, region-restricted correction flags slightly more grid points than global correction (3880 compared with 3873 at zero lag). The same property produces the abrupt changes in significant fraction between adjacent lags (Sect. 3.3). We recommend that global gridpoint lag analyses report both global and region-restricted corrections, and read response timing from correlation 275 magnitude, using FDR correction to establish significance. 

Several limitations warrant mention. First, our regression does not distinguish Eastern Pacific from Central Pacific El Niño flavors, which Xie et al. (2023) showed produce differential BC responses over the Maritime Continent; resolving this distinction could sharpen the lag estimates reported here. ONI also does not represent other modes that affect the same regions: over the Maritime Continent, Field et al. (2009) found the Indian Ocean Dipole to be as important as El Niño for severe burning 280 in Indonesia, and the two often co-occur, so part of the zero-lag Maritime Continent signal may reflect the Indian Ocean Dipole; over the Amazon, Atlantic variability plays a similar role (Chen et al., 2011). Second, MERRA-2’s BC fields depend on the underlying emission inventories and assimilated aerosol optical depth. The split by inventory period addresses changes between inventories but not biases common to all of them, and any bias in fire-source apportionment would propagate into the regional results. Third, the physical mechanism behind the different regional lags is not tested here and remains an open question. 

285 Because ENSO recurs on a roughly 2 to 7 year cycle, the region-specific timing identified here provides a basis for anticipating elevated BC loading in advance of future events, rather than only in hindsight after a given event has already passed. The usable lead time differs by region. Over the Maritime Continent, the response is concurrent with ENSO, so any lead time must come from ENSO prediction itself, whose skill is lowest for forecasts initialized before the middle of the year, the time when the Maritime Continent burning season approaches (Barnston et al., 2012). Over Central America and 290 the Amazon, the response follows the ENSO peak by 5 and 7 to 8 months, so once an event has matured in boreal winter, 

**10** 

https://doi.org/10.5194/egusphere-2026-6022 Preprint. Discussion started: 20 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





the observed state of ENSO already provides several months of warning without relying on a forecast. This complements fire season forecasts based on sea surface temperature anomalies (Chen et al., 2011) by extending the lead time to aerosol loading, which is what determines downwind effects on air quality, visibility, and radiation. 

## **5 Conclusions** 

- 295 Using 46 years of MERRA-2 reanalysis, we show that the relationship between ENSO and global black carbon column mass anomalies is not adequately characterized by a single global or zero-lag statistic: the characteristic lag varies by region, from zero over the Maritime Continent to about five months over Central America and seven to eight months over the Amazon. These lags are reproduced in 1980 to 2009 and 2010 to 2025, periods driven by different biomass burning emission inventories, and do not depend on the 1997 to 1998 El Niño. They are consistent with the timing of the pan-tropical fire cascade documented 

- 300 in satellite fire records, and the same lags appear, at much smaller amplitude, over ocean regions downwind of the Maritime Continent and the Amazon. No relationship is detectable over the continental United States, central Africa, or Siberia/NE Asia at any tested lag; over the continental United States and Siberia/NE Asia the observed correlations in the full record are well below the smallest detectable value, while central Africa lies closer to the detection threshold. The weak CONUS correlation reverses sign between the two periods, whereas the weak central African correlation is positive at lags of 5 to 7 months in both. 

- 305 These results indicate that anticipating ENSO-driven black carbon loading requires region-specific timing rather than a uniform lag assumption, a distinction with recurring practical relevance given ENSO’s periodic recurrence. They also show that in global gridpoint lag analyses, the fraction of grid points passing FDR correction can change abruptly between adjacent lags, so response timing is better identified from correlation magnitude, with global and region-restricted corrections reported together. Future work distinguishing Eastern Pacific from Central Pacific ENSO flavors, extending the lag range for regions 

- 310 whose response may exceed 12 months, and identifying the mechanisms behind the regional differences in timing would further refine the picture presented here. Current work is also examining whether similar lag structures occur in co-emitted aerosol species such as organic carbon, helping distinguish a broader biomass-burning aerosol response from processes specific to BC. 

## **Data availability** 

- MERRA-2 monthly-mean aerosol diagnostics (M2TMNXAER, tavgM_2d_aer_Nx, V5.12.4), including the BCCMASS field 

- 315 used in this study, are produced by the NASA Global Modeling and Assimilation Office and are publicly available from the NASA Goddard Earth Sciences Data and Information Services Center (GES DISC) at https://doi.org/10.5067/FH9A0MLJPC7N (Global Modeling and Assimilation Office (GMAO), 2015). The MERRA-2 aerosol assimilation system is described in Randles et al. (2017) and Buchard et al. (2017). The Oceanic Niño Index used in this study is produced by NOAA’s Physical Sciences Laboratory and is publicly available at https://psl.noaa.gov/data/correlation/oni.data. 

**11** 

https://doi.org/10.5194/egusphere-2026-6022 Preprint. Discussion started: 20 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





## 320 **Author contributions** 

MIO designed the study, performed the analysis, prepared the figures, and wrote the manuscript. 

## **Competing interests** 

The author declares that there are no conflicts of interest. 

## **Acknowledgements** 

- 325 This work was supported by the Ned P. Smith Distinguished Chair Funds, University of Wisconsin-Madison. The author used Claude (Anthropic) to assist with editing the grammar and syntax of manuscript text, and identifying relevant literature. All analyses, results, citations, and interpretations were done and verified by the author, who takes full responsibility for the content of this article. 

**12** 

https://doi.org/10.5194/egusphere-2026-6022 Preprint. Discussion started: 20 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





## **References** 

- 330 Barnston, A. G., Tippett, M. K., L’Heureux, M. L., Li, S., and DeWitt, D. G.: Skill of Real-Time Seasonal ENSO Model Predictions during 2002–11: Is Our Capability Increasing?, Bulletin of the American Meteorological Society, 93, 631–651, https://doi.org/10.1175/BAMSD-11-00111.1, 2012. 

   - Benjamini, Y. and Hochberg, Y.: Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing, Journal of the Royal Statistical Society: Series B (Methodological), 57, 289–300, https://doi.org/10.1111/j.2517-6161.1995.tb02031.x, 1995. 

- 335 Bretherton, C. S., Widmann, M., Dymnikov, V. P., Wallace, J. M., and Bladé, I.: The Effective Number of Spatial Degrees of Freedom of a Time-Varying Field, Journal of Climate, 12, 1990–2009, https://doi.org/10.1175/1520-0442(1999)012<1990:TENOSD>2.0.CO;2, 1999. 

   - Buchard, V., Randles, C. A., da Silva, A. M., Darmenov, A., Colarco, P. R., Govindaraju, R., Ferrare, R., Hair, J., Beyersdorf, A. J., Ziemba, L. D., and Yu, H.: The MERRA-2 Aerosol Reanalysis, 1980 Onward. Part II: Evaluation and Case Studies, Journal of Climate, 30, 6851–6872, https://doi.org/10.1175/JCLI-D-16-0613.1, 2017. 

- 340 Chen, Y., Randerson, J. T., Morton, D. C., DeFries, R. S., Collatz, G. J., Kasibhatla, P. S., Giglio, L., Jin, Y., and Marlier, M. E.: Forecasting Fire Season Severity in South America Using Sea Surface Temperature Anomalies, Science, 334, 787–791, https://doi.org/10.1126/science.1209472, 2011. 

   - Chen, Y., Morton, D. C., Andela, N., van der Werf, G. R., Giglio, L., and Randerson, J. T.: A Pan-Tropical Cascade of Fire Driven by El Niño/Southern Oscillation, Nature Climate Change, 7, 906–911, https://doi.org/10.1038/s41558-017-0014-8, 2017. 

- 345 Field, R. D., van der Werf, G. R., and Shen, S. S. P.: Human Amplification of Drought-Induced Biomass Burning in Indonesia since 1960, Nature Geoscience, 2, 185–188, https://doi.org/10.1038/ngeo443, 2009. 

   - Global Modeling and Assimilation Office (GMAO): MERRA-2 tavgM_2d_aer_Nx: 2d, Monthly Mean, Time-Averaged, Single-Level, Assimilation, Aerosol Diagnostics V5.12.4, https://doi.org/10.5067/FH9A0MLJPC7N, accessed via NASA GES DISC, 2015. 

- Hoell, A., Robinson, R., Hobbins, M., Breeden, M. L., Worsnop, R. P., and Guerrero, E.: The Relationship Between the El Niño- 

- 350 Southern Oscillation and Extensive Wildfire Area Burned in Contiguous United States Geographic Area Coordination Centers, Journal of Geophysical Research: Atmospheres, 131, e2025JD045 436, https://doi.org/10.1029/2025JD045436, 2026. 

   - Hoskins, B. J. and Karoly, D. J.: The Steady Linear Response of a Spherical Atmosphere to Thermal and Orographic Forcing, Journal of the Atmospheric Sciences, 38, 1179–1196, https://doi.org/10.1175/1520-0469(1981)038<1179:TSLROA>2.0.CO;2, 1981. 

- Jong, B.-T., Ting, M., Seager, R., and Anderson, W. B.: ENSO Teleconnections and Impacts on U.S. Summertime Temperature during a 

- 355 Multiyear La Niña Life Cycle, Journal of Climate, 33, 6009–6024, https://doi.org/10.1175/JCLI-D-19-0701.1, 2020. 

   - Lou, S., Yang, Y., Wang, H., Lu, J., Smith, S. J., Liu, F., and Rasch, P. J.: Black Carbon Increases Frequency of Extreme ENSO Events, Journal of Climate, 32, 8323–8333, https://doi.org/10.1175/JCLI-D-19-0549.1, 2019. 

   - McPhaden, M. J., Zebiak, S. E., and Glantz, M. H.: ENSO as an Integrating Concept in Earth Science, Science, 314, 1740–1745, https://doi.org/10.1126/science.1132588, 2006. 

- 360 Pereira, A. G. C., Palácios, R., Santos, P. C. R., Pereira, R. V. S., Cirino, G., and Imbiriba, B.: Relationship between El Niño-Southern Oscillation and Atmospheric Aerosols in the Legal Amazon, Climate, 12, 13, https://doi.org/10.3390/cli12020013, 2024. 

   - Randles, C. A., da Silva, A. M., Buchard, V., Colarco, P. R., Darmenov, A., Govindaraju, R., Smirnov, A., Holben, B., Ferrare, R., Hair, J., Shinozuka, Y., and Flynn, C. J.: The MERRA-2 Aerosol Reanalysis, 1980 Onward. Part I: System Description and Data Assimilation Evaluation, Journal of Climate, 30, 6823–6850, https://doi.org/10.1175/JCLI-D-16-0609.1, 2017. 

**13** 

https://doi.org/10.5194/egusphere-2026-6022 Preprint. Discussion started: 20 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 365 van der Werf, G. R., Randerson, J. T., Collatz, G. J., Giglio, L., Kasibhatla, P. S., Arellano, A. F., Olsen, S. C., and Kasischke, E. S.: Continental-Scale Partitioning of Fire Emissions during the 1997 to 2001 El Niño/La Niña Period, Science, 303, 73–76, https://doi.org/10.1126/science.1090753, 2004. 

   - Xie, B., Yang, Y., Wang, H., Wang, P., and Liao, H.: Biomass Burning Emissions of Black Carbon over the Maritime Continent and ENSO Variability, Journal of Climate, 36, 8365–8376, https://doi.org/10.1175/JCLI-D-22-0553.1, 2023. 

**14** 

https://doi.org/10.5194/egusphere-2026-6022 Preprint. Discussion started: 20 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 







**Figure 1.** Composite BC column mass anomaly for El Niño (top, 24 events) and La Niña (middle, 18 events), and their difference (bottom). Stippling in the bottom panel indicates grid points where the El Niño _−_ La Niña difference is significant after Benjamini-Hochberg FDR correction ( _α_ = 0 _._ 05) using a two-sided Mann-Whitney _U_ test across independent event means. 

**15** 

https://doi.org/10.5194/egusphere-2026-6022 Preprint. Discussion started: 20 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 







**Figure 2.** Zero-lag regression of BC column mass anomaly against the Oceanic Niño Index at each grid point. Stippling indicates grid points significant after Benjamini-Hochberg FDR correction ( _α_ = 0 _._ 05), with significance assessed using the effective-sample-size correction of Bretherton et al. (1999) to account for autocorrelation in both series. 

**16** 

https://doi.org/10.5194/egusphere-2026-6022 Preprint. Discussion started: 20 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 







**Figure 3.** As in Fig. 2, but computed separately for DJF, MAM, JJA, and SON using only the months within each season. 

**17** 

https://doi.org/10.5194/egusphere-2026-6022 Preprint. Discussion started: 20 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 







**Figure 4.** (top) Regression slope of BC column mass anomaly against the Oceanic Niño Index at each grid point’s lag of peak _|r|_ (0 to 12 months, ONI leading). Stippling indicates grid points significant after Benjamini-Hochberg FDR correction at that lag. (bottom) The lag (months) at which _|r|_ peaks, restricted to grid points significant after FDR correction; white indicates grid points not significant at any tested lag. Colors are categorical, one per lag value, to distinguish adjacent lags rather than implying a continuous gradient between them. Boxes mark the regions in Table 1. 

**18** 

https://doi.org/10.5194/egusphere-2026-6022 Preprint. Discussion started: 20 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 







**Figure 5.** Regional diagnostics for the full record (1980 to 2025) as a function of lag (months, ONI leading). Left: regional median _|r|_ . Middle: regional median effective sample size, with the global median (dashed). Right: fraction of grid points significant under regionrestricted Benjamini-Hochberg FDR correction ( _α_ = 0 _._ 05). Shaded bands in the left panel mark median _|r|_ of 0.05 to 0.10 (gray) and 0.15 to 0.20 (orange) for reference. 

**19** 

https://doi.org/10.5194/egusphere-2026-6022 Preprint. Discussion started: 20 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 







**Figure 6.** Area-weighted regional mean BC column mass anomaly (blue, left axis) and ONI (red, right axis) shifted forward by each region’s lag for (top) the Maritime Continent (0 months), (middle) Central America (5 months), and (bottom) the Amazon (7 months). Dashed vertical lines mark changes in the MERRA-2 biomass burning emission inventory, from RETROv2 to GFEDv3.1 in 1997 and from GFEDv3.1 to QFEDv2.4 in 2010 (Randles et al., 2017). 

**20** 


