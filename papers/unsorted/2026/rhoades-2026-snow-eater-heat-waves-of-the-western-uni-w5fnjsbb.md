---
title: Snow-eater heat waves of the western United States
authors:
- Rhoades, Alan M.
- North, Joshua S.
- Rudisill, William
- Hatchett, Benjamin J.
- Risser, Mark D.
- Beltran-Peña, Areidy Aracely
- Heggli, Anne
- Hotalling, Scott
- Huning, Laurie S.
- Joros, Andrew
- LaPlante, Matthew
- Mahesh, Ankur
- Marshall, Adrienne
- McCrary, Rachel
- McEvoy, Daniel
- Rahimi, Stefan
- Raleigh, Mark S.
- Randall, Calen
- Srivastava, Abhishekh
- Wehner, Michael
- Zhou, Yang
- Jones, Andrew D.
year: '2026'
journal: Science Advances
doi: 10.1126/sciadv.aeb3361
tags:
- united states
zotero_key: W5FNJSBB
item_type: journalArticle
url: https://openalex.org/W4414139433
source_url: 'unpaywall: https://www.researchsquare.com/article/rs-7576317/latest.pdf'
fulltext_status: fulltext
synced: '2026-11-06'
---

# Snow-eater heat waves of the western United States

## Abstract

Abrupt snowmelt, triggered by rain-on-snow events or "snow-eater heat waves," can cause flooding, initiate or accelerate snow drought, and affect water availability. However, the characteristics (e.g., area, duration, and frequency), impacts, and trends of snow-eater heat waves have received little attention. To address this gap, we developed a method to identify snow-eater heat waves and estimate their melt potential using 20th Century Reanalysis version 3 air temperature data, the TempestExtremes algorithm, and an operational snowmelt model (SNOW-17) across 1850-2015. Melt season snow-eater heat waves typically last 3 to 5 days, with three to five events, doubling snowmelt rates. Seven of 11 spring superfloods are shown to coincide with snow-eater heat waves. Since the 1850s, snow-eater heat waves have increased in area and frequency, decreased in duration, and shifted earlier in the melt season. Incorporating snow-eater heat-wave impacts into SNOW-17 enhances extreme melt estimates, improving water management support tools.

## Full text





Lawrence Berkeley National Laboratory 

Lawrence Berkeley National Laboratory 

Lawrence Berkeley National Laboratory 

Colorado State University 

Lawrence Berkeley National Laboratory 

Stanford 

Desert Research Institute 

Utah State 

California State University, Long Beach 

Utah State 

Lawrence Berkeley National Laboratory 

Colorado School of Mines 

National Center for Atmospheric Research 

Desert Research Institute 

University of Wyoming 

Oregon State University 

University of California, Davis 

University of California, Davis 

Lawrence Berkeley National Laboratory 

Lawrence Berkeley National Laboratory 

Lawrence Berkeley National Laboratory 

Snowmelt Extremes, Snow-Heatwave Interactions, Operational Modeling, Spring Floods 

d Da ~~te~~ : September 11th, 2025 

DOI: https://doi.org/10.21203/rs.3.rs-7576317/v1 

~~Li~~ cense:   This work is licensed under a Creative Commons Attribution 4.0 International License. Read Full License 

~~A~~ ddi ~~ti~~ onal Declara ~~ti~~ ons: The authors declare no competing interests. 

11 

12 

28 

29 

30 

- 1 

# Snow-eater heatwaves of the western United States 

- 2 Alan M. Rhoades<sup>1,*</sup> , Joshua Snowball North<sup>1</sup> , William Rudisill<sup>1</sup> , 3 Benjamin J. Hatchett<sup>2</sup> , Mark Risser<sup>1</sup> , Areidy Beltran-Pe˜na<sup>3</sup> , 4 Anne Heggli<sup>4</sup> , Scott Hotaling<sup>5</sup> , Laurie S. Huning<sup>6</sup> , Matthew 5 LaPlante<sup>5</sup> , Ankur Mahesh<sup>1,12</sup> , Adrienne Marshall<sup>7</sup> , Rachel 6 McCrary<sup>8</sup> , Daniel McEvoy<sup>4</sup> , Stefan Rahimi<sup>9</sup> , Mark S. Raleigh<sup>10</sup> , 7 Calen Randall<sup>11</sup> , Abhishekh Srivastava<sup>11</sup> , Michael Wehner<sup>1</sup> , Yang 8 Zhou<sup>1</sup> , Andrew D. Jones<sup>1,12</sup> 

8 

- 1Lawrence Berkeley National Laboratory, Berkeley, CA, USA. 

9 

- 2Colorado State University, Fort Collins, CO, USA. 

10 

- 3Stanford University, Stanford, CA, USA. 

- 4Desert Research Institute, Reno, NV, USA. 

13 

14 

15 

16 

17 

18 

19 

20 

21 

      - 5Utah State University, Logan, UT, USA. 

   - 6California State University, Long Beach, CA, USA. 

      - 7Colorado School of Mines, Golden, CO, USA. 

- 8National Center for Atmospheric Research, Boulder, CO, USA. 

      - 9University of Wyoming, Laramie, WY, USA. 

      - 10Oregon State University, Corvallis, OR, USA. 

   - 11University of California, Davis, Davis, CA, USA. 

   - 12University of California, Berkeley, Berkeley, CA, USA. 

      - *Corresponding author: arhoades@lbl.gov. 

22 

23 

24 

25 

26 

27 

31 

#### Abstract 

Abrupt snowmelt, triggered by rain-on-snow events or “snow-eater heatwaves”, can cause flooding, accelerate snow drought, and impact water availability. Yet the characteristics (e.g., area, duration, and frequency), impacts, and trends of snow-eater heatwaves have received relatively little attention. To address this gap, we developed a method to identify snow-eater heatwaves and estimate their melt potential using Twentieth Century Reanalysis Version 3 air temperature data, the TempestExtremes algorithm, and an operational snowmelt model (SNOW-17) across 1850–2015. Melt season snow-eater heatwaves typically last 3–5 days, with 3–5 events, doubling snowmelt rates. Seven of 11 spring superfloods can be linked 

1 

- 32 with snow-eater heatwaves. Since the 1850s, snow-eater heatwaves have increased 33 in area and frequency, decreased in duration, and shifted earlier in the melt sea34 son. Incorporating snow-eater heatwave impacts into SNOW-17 improves extreme 35 snowmelt estimates, providing additional tools to support water management. 

- 36 Keywords: Snowmelt Extremes, Snow-Heatwave Interactions, Operational Modeling, 37 Spring Floods 

- 38 

## 1 Introduction 

- 39 It is “virtually certain” that anthropogenic climate change has led to more frequent 

- 40 and intense heatwave events worldwide (Seneviratne et al, 2021). In the western United 

- 41 States (WUS), for instance, heatwave events now occur more regularly in the spring 

- 42 and early summer, and have nearly doubled in frequency and intensity since the mid- 

- 43 1990s (Reyes and Kramer, 2023). This shift in heatwave timing and frequency may 

- 44 have implications for previously rare meteorological events related to interannual vari- 

- 45 ability of the climate system (O’Brien and Deser, 2023; Srivastava et al, 2025). Among 

- 46 these phenomena are heatwaves that occur in the spring and early summer, which 

- 47 can rapidly diminish snowpacks, a phenomenon we term here as “snow-eater heat- 

- 48 waves”. We define snow-eater heatwaves as seasonally anomalous and above-freezing 

- 49 temperature conditions that are sustained for several days (both in the day and night), 

- 50 resulting in impacts to water resources (e.g., warm-season water supply allocations) 51 and increases in flood risk. 

- 52 Snow-eater heatwaves have occurred several times in the recent history of the 

- 53 WUS. These events often follow the buildup of a snowpack in the month(s) before 

- 54 the ablation event. For example, in 1983, a spring “superflood” struck northern Utah, 

- 55 where rapid snowmelt overtook low-lying communities between the Wasatch Moun- 

- 56 tains and the Great Salt Lake (Tarouilly et al, 2021). As described by Arnow (1984), 

- 57 “...major snowmelt began at the end of May, during a heat wave on the Memorial 

- 58 Day weekend; and record-breaking quantities of water flowed into the lake from many 

2 

- 59 tributary streams...” Nine streams on the Wasatch Front exceeded the 100-year flood 

- 60 mark, and downtown Salt Lake City had to construct two emergency canals to con- 

- 61 vey the flood waters away from the city center (Lindskov, 1984). In that same week 

- 62 in western Nevada, rapid and prolonged snowmelt following a near-record snowpack 

- 63 season triggered a major landslide on Slide Mountain, Nevada, causing one fatality 

- 64 and inundating a major highway (Hatchett et al, 2023). And in the immediate wake of 

- 65 that heatwave in northern Arizona, Glen Canyon Dam also experienced a rapid rise in 

- 66 water levels from June until July (180% of normal), largely due to immense snowmelt 

- 67 (Burgi, 2020). By July, the dam likely would have overtopped if water managers and 

- 68 engineers had not decided to “retrofit” the top of the dam with plywood reinforced 69 with a metal backing (Burgi, 2020). 

- 70 In 2021, a series of snow-eater heatwaves occurred in the WUS. During the first 

- 71 few weeks of April, mean air temperature anomalies exceeded +4-8<sup>◦</sup> C, with associated 

- 72 widespread declines in snowpack: 24% of snow water equivalent (SWE) measurement 

- 73 sites reported median snow loss of at least -99 mm, or -14 mm/day, with particularly 

- 74 anomalous conditions occurring in the coastal WUS (McEvoy and Hatchett, 2023). 

- 75 In the same year, the Pacific Northwest experienced another snow-eater heatwave 

- 76 between June 26th and 29th, shattering temperature records throughout the Pacific 

- 77 Northwest by up to 5<sup>◦</sup> C (Bercos-Hickey et al, 2022). The snow-covered areas of the 

- 78 Pacific Northwest were 35% above normal on April 1st; however, fell from 31% to 12% 

- 79 of normal between June 25th and 30th (Reyes and Kramer, 2023). 

- 80 Snow-eater heatwaves have been less studied than other snowmelt extremes (e.g., 

- 81 rain-on-snow events; McCabe et al, 2007; Tarouilly et al, 2021; Welty and Zeng, 2021), 

- 82 yet have the potential to increase in area, duration, frequency, and/or intensity in a 

- 83 rapidly changing climate. This is especially likely through the middle of the 21st cen- 

- 84 tury, when models suggest that WUS snowpack volumes will increasingly shift toward 

- 85 a “low-to-no snow” future under continued climate warming (Siirila-Woodburn et al, 

3 

- 86 2021). Even in years in which snowpacks remain within historical patterns of variabil- 

- 87 ity, however, those snowpacks are likely to be more susceptible to ablation (Musselman 

- 88 et al, 2021; Rhoades et al, 2022). Abrupt spring and early summer snowmelt events 

- 89 can be particularly impactful on WUS water management as these events occur dur- 

- 90 ing a time of year when water rights allocations are made (Null and Prudencio, 2016), 

- 91 often with fixed operating rules (Li et al, 2024), that can exacerbate water gaps in the 92 warm-season (Beltran-Pe˜na et al, 2025). 

- 93 Recent studies have shown that operational forecasts of reservoir inflows system- 

- 94 atically underrepresent actual reservoir inflows (particularly in the WUS in recent 

- 95 decades) owing to changes in precipitation and temperature patterns that shape 

- 96 snowmelt-contributed runoff (Lehner et al, 2017a,b). Longer-term predictions of WUS 

- 97 snowpack behavior also show that a deleterious, widespread, and persistent decrease 

- 98 in snowfall and snowpack storage is expected as the WUS continues to warm (Rhoades 

- 99 et al, 2018; Siirila-Woodburn et al, 2021; Marshall et al, 2024; Norris et al, 2025). These 

- 100 reductions will continue to alter historically assumed snowmelt-contributed runoff and 101 overall runoff efficiency (Rhoades et al, 2022). 

- 102 All of these factors may be aggravated by shifts in snow-eater heatwave area, 

- 103 frequency, duration, and/or intensity, and it is thus important to understand how 

- 104 snow-eater heatwave characteristics may have changed from historical patterns of vari- 

- 105 ability or may be changing under anthropogenic climate change. This understanding 

- 106 cannot be achieved, however, until snow-eater heatwaves are quantitatively character- 

- 107 ized. A major question remains as to whether these shifts in snowmelt characteristics 

- 108 occur gradually and/or in a punctuated fashion, shaped by snowmelt extremes such 

- 109 as snow-eater heatwaves. 

- 110 In this study, we aim to answer the following questions: 

- 111 1. What criteria should be used to define snow-eater heatwave events? 

4 

- 112 2. Does an operational snowmelt model well represent snow-eater heatwave 113 contributed melt, or are enhancements needed? 

- 114 3. What fraction of late spring and early summer snowmelt totals do the largest 115 snow-eater heatwave events in the historical record contribute? 

- 116 4. Have snow-eater heatwave characteristics (i.e., areal extent, intensity, duration, 

- 117 and frequency) changed from the 19th to the early 21st century? 

118 

## 2 Data and Methods 

- 119 The workflow developed to identify snow-eater heatwave characteristics between the 

- 120 19th and 21st centuries is summarized in Figure 1. Subsequent subsections and the 

- 121 Supplemental Material provide additional information on methodological assumptions 122 and choices made in this workflow. 

- 123 

### 2.1 Snow-eater heatwave identification and tracking 

- 124 Our end-to-end workflow can be applied to any gridded dataset that provides 

- 125 subdaily-to-daily two-meter air temperature (T2m) estimates. We chose to use the 

- 126 NOAA-CIRES-DOE 20th Century Reanalysis version 3 (20Cv3; Compo et al, 2006; 

- 127 Slivinski et al, 2019, 2021) as it provides a long spatiotemporally continuous meteo- 

- 128 rological dataset. 20Cv3 is a gridded (∼75 km grid spacing) estimate of atmospheric 

- 129 and land surface conditions that spans 1806 to 2015. To constrain its model-based 130 estimates of atmospheric and land surface conditions, 20Cv3 assimilates surface obser- 

- 131 vations of surface air pressure and prescribes lower boundary conditions of sea-surface 

- 132 temperature and sea-ice concentrations. 20Cv3 produces an 80-member ensemble to 

- 133 account for internal climate variability in regions where data are not assimilated. 

- 134 We leverage three-hourly estimates of T2m to identify and estimate the melt poten- 

- 135 tial of snow-eater heatwaves from 1850-2015 (defined and discussed in subsequent 

- 136 sections). We opted to use data beginning at 1850 onward since the data from 1806 

5 

- 137 to 1835 is experimental and might lead to trend analysis inconsistencies with data 

- 138 post-1835. This also coincides with the Intergovernmental Panel on Climate Change’s 

- 139 pre-industrial period (1850-1899) and is the earliest period at which observations were 140 near-global (Allen et al, 2018). 

- 141 Slivinski et al (2021) found that 20Cv3 demonstrates comparable skill to current 

- 142 real-time forecasting models in estimating 500 hPa geopotential height fields over the 

- 143 near-term period of 1979-2015. This provides confidence that it skillfully represents 

- 144 mid-tropospheric atmospheric circulation patterns, particularly during the mountain- 

- 145 ous WUS observational record that overlaps with 20Cv3 (1980-2015). Nolin et al 

- 146 (2022) showed that 50-year climatological March-May T2m anomaly sign and spatial 

- 147 extent over North America in 20Cv3 correlated strongly with the Berkeley Earth and 

- 148 a tree-ring-based paleoclimate reconstruction, but with a cool bias. This was further 

- 149 corroborated by Gillespie et al (2023) for North American T2m trend analyses compar150 ing 1851-1900 to 2005-2014 in 20Cv3 (+1.19<sup>◦</sup> C) to the Global Historical Climatology 151 Network version 4 (+1.33<sup>◦</sup> C). 

- 152 We use 80-member ensemble mean three-hourly T2m estimates to identify snow- 

- 153 eater heatwave events using the following criteria: 

- 154 1. The event must occur after March 19th (spring equinox) and before July 1st 

- 155 2. The T2m must be above freezing 

- 156 3. Analogous to Reyes and Kramer (2023), a T2m anomaly of +6K should occur 

- 157 relative to a three-hourly background climatology (1980-2010) 

- 158 4. Criteria 2-3 are sustained for at least 3 days 

- 159 We selected these criteria for the following physical reasons: First, we sought to 

- 160 isolate events that occur when snowpacks approach their climatological peak and begin 

- 161 to melt out (March 19th to July 1st). Second, as sudden shifts in T2m would not 

- 162 be expected to result in rapid melt if daily average T2m remains below freezing, we 

- 163 want to ensure that the snowpack experiences sustained above-freezing conditions that 

6 

- 164 could lead to ripening and/or ablation. Third, the criteria further isolate anomalous 

- 165 T2m conditions that are not simply part of the normative transition between spring 

- 166 and summer. Finally, we want to ensure these conditions are sustained for a prolonged 

- 167 period (at least 3 days; a common heatwave duration definition - Disher et al, 2021) 

- 168 that accounts for a continuous and anomalous energy transfer from the atmosphere 

- 169 to the snowpack that depletes snowpack cold content, leading to snow loss. 

- 170 To isolate regions of snow-eater heatwaves in time and space, we use an array of 

- 171 Climate Data Operators (CDO; Schulzweida, 2023) and the TempestExtremes Stitch172 Blobs algorithm (Ullrich et al, 2021). CDO isolates the snow-eater heatwave conditions 

- 173 to generate binary (0 or 1) spatiotemporal masks. StitchBlobs is then applied to 

- 174 these binary masks to identify distinct snow-eater heatwave events and assign them 

- 175 unique identifiers. For example, the StitchBlobs flag minsize and mintime are set to 

- 176 100 gridcells and 24 hours, respectively, to assign unique identifiers to each snow- 

- 177 eater heatwave binary mask based on spatial and temporal overlap assumptions. This 

- 178 workflow allows us to generate a historical catalog of events. 

- 179 

### 2.2 Snow-eater heatwave melt potential 

- 180 To provide a more decision-relevant assessment of how snow-eater heatwave character- 

- 181 istics have changed since the 19th century, we employ an operational snowmelt model. 

- 182 The operational snow accumulation and ablation model we leverage is SNOW-17, 

- 183 which is currently used by the National Weather Service (Anderson, 1976). SNOW-17 

- 184 requires T2m and precipitation as inputs, while snowmelt and SWE are outputs (He 

- 185 et al, 2011). SNOW-17 utilizes T2m as a proxy for energy exchange across the snow-air 

- 186 interface and applies empirically based relationships to compute snowpack heat stor- 

- 187 age, snowmelt, liquid water retention, and meltwater transmission (Anderson, 2006; 

- 188 He et al, 2011). 

7 

- 189 To quantify the melt potential of snow-eater heatwaves and assess the fidelity of 

- 190 SNOW-17 in estimating both mean and extreme snowmelt, we utilize the temperature 191 index non-rain melt model within the SNOW-17 model (Equation 6 in Anderson, 1976, 

- 192 2006). Temperature index models do not explicitly account for all surface radiative 

- 193 budget terms (e.g., net solar radiation), but instead rely on the strong relationship of 194 snow-longwave radiation feedbacks (Ohmura, 2001) and a few parameters that attempt 

- 195 to account for aspect, slope, length of day, and land surface cover (discussed later). 196 Temperature index models are also practical (i.e., only require estimates of T2m), 

- 197 computationally efficient, and widely used in operational forecasting (Reis et al, 2025). 

- 198 The SNOW-17 non-rain melt potential (Mnr) is defined as 



<!-- Start of picture text -->
Mnr (d) = � Mf (h) ∗ (Ta(h) − MBASE) (1)<br>h∈d<br><!-- End of picture text -->

- 199 where d denotes the day of the year between March 19th to July 1st, h denotes the 

- 200 hour of day d at 3-hour intervals, Ta(h) is the two-meter air temperature (K) provided 

- 201 by the 20Cv3 reanalysis dataset at 3-hourly resolution, MBASE denotes the baseline 

- 202 melt temperature (equal to 273.15 K), and Mf (h) is the seasonal variation in the non- 

- 203 rain melt factor (mm/hr). Notably, melt potential is only realized if the same amount 204 of snow is present on the landscape. Therefore, melt potentials represent upper-bound 

- 205 estimates of snowmelt, analogous to the difference between actual evapotranspiration 206 and potential evapotranspiration (Eagleman, 1967). 

- 207 The seasonal variation, which accounts for the influence of the seasonal cycle of 

- 208 solar radiation and land surface feedbacks on snowmelt, is defined as 



<!-- Start of picture text -->
Mf (h) = (Sv(d) ∗ Av(d) ∗ (MFmax − MFmin) + MFmin) (2)<br><!-- End of picture text -->

8 

- 209 where Sv(d) accounts for solar variation based on the season, and MFmin < MFmax. 

- 210 MFmin and MFmax account for local radiative and temperature effects on snow- 

- 211 pack (e.g., south-facing versus north-facing slopes and forest cover types) as defined 

- 212 in a NOAA NWS technical manual for SNOW-17 (NWS, 2004). More specifically, 

- 213 Table 1 in NWS (2004) states that for coniferous forests MFmax (MFmin) should 

- 214 range between 0.5-0.8 (0.2-0.3) whereas in open areas MFmax (MFmin) should range 

- 215 between 1.3-2.0 (0.5-0.9). Traditionally, these parameters are chosen by the user based 

- 216 on local knowledge of the region of interest (e.g., land surface cover). Av(d) accounts 

- 217 for angular variation (i.e., latitude and time of year). Across the WUS, Av(d) is equal 

- 218 to 1.0. The solar variation Sv(d) accounts for the length of day (which influences 

- 219 radiative and temperature feedback on snowpack) and is defined as 



<!-- Start of picture text -->
Sv(d) = 1 + 1 (3)<br>2 sin � 2πN366 ( d ) � 2<br><!-- End of picture text -->

220 where N (d) is the number of days (d) since the spring equinox (March 19th). 

- 221 To estimate melt potential across the WUS, we developed a statistical model 222 to estimate plausible data-informed estimates of the SNOW-17 parameters. For the 

- 223 March 19th through July 1st period, MFmin has a negligible impact on snowmelt 

- 224 potential (see the Supplemental Material for more discussion). Therefore, we focus 

- 225 our attention solely on MFmax. Our proposed statistical model relates in situ 

- 226 measurements of the daily change in SWE (dSWE) provided by the Snow Teleme- 

- 227 try (SNOTEL) Network (https://nwcc-apps.sc.egov.usda.gov/imap/) with collocated 

- 228 gridded estimates of T2m from 20Cv3. This creates a WUS-wide parameter ensemble 

- 229 of gridded MFmax estimates (1500 total); from this, we produce an ensemble of melt 

- 230 potential estimates (50 total) at each grid cell within the WUS. 

- 231 To account for SNOTEL measurement network spatiotemporal coverage uncer- 

- 232 tainty between 1980-2015 (and ensure SNOW-17 melt potential estimates are not 

9 

- 233 fine-tuned for performance in any particular year), we perform a weighted average of 

- 234 the SNOW-17 parameter estimates across 1980-2015 at each gridcell. The weights are 

- 235 determined based on the number of SNOTEL observations across the WUS in a given 

- 236 year (i.e., 8,254 measurements in 1980 to 39,474 measurements in 2015). The melt 

- 237 potential estimates are computed using a random selection of the 1500 MFmax esti- 

- 238 mates available, along with the fixed estimates of MFmin. We found that a 50-member 

- 239 ensemble of SNOW-17 melt potential estimates was an optimal choice between bal- 

- 240 ancing the representation of the underlying distribution of melt potential estimates 

- 241 and computational resources. The Supplemental Material contains specific details of 

- 242 this parameter estimation. 

- 243 In addition, we propose a natural log additive term to Equation 1 that captures 

- 244 enhanced melt on snow-eater heatwave days. This additive term can be scaled and 

- 245 varied in its melt strength based on a fixed parameter (k) and the snow-eater heat- 

- 246 wave presence and duration. The “out of the box” and experimental versions of the 

- 247 SNOW-17 model were intercompared and ranked to identify the top three performing 

- 248 models over the SNOTEL period of record (1980-2015). These three melt potential 

- 249 models include the “out of the box” SNOW-17 model, which has no heatwave hour 

- 250 (NHH) influence, and two experimental models, heatwave hours (HH) and accumula- 

- 251 tive heatwave hours (AHH). More details about these experimental models and their 

- 252 verification are provided in the Supplemental Material. Our hypothesis in devising an 

- 253 additive melt term in the SNOW-17 melt equation is based on the fact that during 

- 254 snow-eater heatwaves, a snowpack would experience a prolonged period (both night 

- 255 and day) of elevated temperatures and sunnier conditions leading to an increase in 

- 256 available melt energy and sustained erosion of its cold content (DeWalle and Rango, 

- 257 2008; Jennings et al, 2018). 

10 

- 258 

### 2.3 Snow-eater heatwave metrics 

- 259 We compute several metrics to add context to the snow-eater heatwave catalog. These 

- 260 metrics are computed across March 19th to July 1st and include the seasonal total 

- 261 melt potential, snow-eater heatwave contributed melt potential, and the maximum 

- 262 one-day, three-day, and five-day melt potential (Mx1day, Mx3day, and Mx5day, respec- 

- 263 tively). The percent contribution of snow-eater heatwave melt potential is computed 

- 264 by taking the melt on snow-eater heatwave-only days and dividing by the total melt 

- 265 potential across all days between March 19th to July 1st. To identify the top years for 

- 266 these metrics we take the mean of the 50-member ensemble melt potential estimates, 

- 267 sum the melt potentials over all possible periods of interest (e.g., five days), spatially 

- 268 average those periods, find the maximum across all possible periods, and then con- 

- 269 vert those estimates from mm to km<sup>3</sup> by multiplying the depth of melt potential by 

- 270 the area of the snow-eater heatwave masks. The 20Cv3-SNOW-17 melt potential esti- 

- 271 mates can be computed in regions that do not typically have ephemeral or seasonal 

- 272 snowpacks (Hatchett, 2021). To limit this bias when we intercompare the melt poten- 

- 273 tials across years throughout the WUS, we mask the melt potential estimates with 

- 274 a widely used mountain mask (K¨orner et al, 2017). We also compare our catalog of 

- 275 snow-eater heatwave dates and durations with the Tarouilly et al (2021) WUS top 100 

- 276 superflood catalog. To assess trends in snow-eater heatwave characteristics between 

- 277 1850-2015, we compute spatial average seasonal anomalies within WUS mountainous 

- 278 regions, comparing each season to a 50-year pre-industrial base period (1850-1899). 

- 279 The non-parametric Mann-Kendall and Theil-Sen tests are computed to assess the 

- 280 sign and statistical significance of the trends (Wilks, 2011). 

- 281 

## 3 Results 

- 282 In the following subsections, we will introduce storyline-based (Shepherd et al, 2018) 

- 283 and climatological-based analyses of WUS snow-eater heatwave events estimated with 

11 

- 284 our 20Cv3-SNOW-17 workflows. For the storyline event, we use the snow-eater heat- 

- 285 wave event of May 27-31, 1983, to highlight the fidelity of the 20Cv3-SNOW-17 melt 

- 286 potential models across all days and snow-eater heatwave-only days between March 

- 287 19th to July 1st. This storyline event is chosen as it was the top spring season, 

- 288 snowmelt-dominated superflood event between 1950-2010 (Tarouilly et al, 2021). We 

- 289 then climatologically contextualize this event across both the SNOTEL period of 

- 290 record (1980-2015) and the longer period of record enabled by 20Cv3 (1850-2015). 

- 291 This process allows us to build a catalog of snow-eater heatwave events and provide 

- 292 estimates of how their characteristics have changed between the 19th to 21st centuries. 

- 293 

### 3.1 The 1983 snow-eater heatwave event 

- 294 Figure 2 compares SNOTEL site measurements of dSWE with 20Cv3-SNOW-17 melt 

- 295 potential estimates for the May 1983 superflood event across the NHH, HH, and 

- 296 AHH models. Comparisons between melt potential estimates and observed dSWE 

- 297 measurements are only made with those SNOTEL sites that fall within the snow-eater 

- 298 heatwave area and up to the point at which SNOTEL SWE reaches 0 mm. Between 

- 299 March 19th to July 1st, SNOTEL site daily mean and 90th percentile dSWE was - 

- 300 10.3 mm/day and -33.0 mm/day, respectively. On snow-eater heatwave-only days, the 

- 301 mean dSWE was -37.0 mm/day, with a 90th percentile value of -66.0 mm/day. This 

- 302 more than 300% change in dSWE on snow-eater heatwave-only days was also captured 

- 303 by each of the 20Cv3-SNOW-17 model melt potential estimates. The NHH model had 

- 304 a slightly lower mean dSWE of -11.4 mm/day, with HH and AHH at -11.6 mm/day. 

- 305 More divergence between the 20Cv3-SNOW-17 models occurred on snow-eater 

- 306 heatwave-only days, due to the experimental natural log additive melt term (Equation 

- 307 4 in the Supplemental Material). The closest mean estimates of dSWE were produced 

- 308 by NHH (-36.6 mm/day), followed by HH (-52.3 mm/day) and AHH (-54.3 mm/- 

- 309 day), respectively. Although NHH had the best mean dSWE performance compared 

12 

- 310 to SNOTEL measurements overall, it failed to capture relatively extreme melt events: 

- 311 90th percentile modeled (-44.8 mm/day) melt estimates were more tightly constrained 

- 312 than observations (-66.0 mm/day). Contrastingly, HH (-60.0 mm/day) nearly reached 

- 313 the 90th percentile dSWE threshold measured at SNOTEL sites, and AHH (-67.6 314 mm/day) slightly exceeded the threshold. 

- 315 3.2 Snow-eater heatwave climatology over the SNOTEL 

### 316 period of record 

317 The three 20Cv3-SNOW-17 melt potential models are now compared over climato318 logical timescales, spanning the SNOTEL period of record (1980-2015) that overlaps 319 with 20Cv3 (Figure 3). WUS-wide SNOTEL dSWE, on average, was -9.0 mm/day 320 with the 90th percentile melt at -28.0 mm/day on all days between March 19th to July 321 1st (Table 1). Each melt potential model overestimated mean daily dSWE compared 322 with SNOTEL by -2.4 to -3.0 mm/day, with NHH most closely matching SNOTEL 323 (-11.4 mm/day). Climatological decile melt on all days was underrepresented by all 

- 324 20Cv3-SNOW-17 melt potential models. However, NHH was more constrained (-24.4 325 mm/day) than either HH (-25.9 mm/day) or AHH (-25.7 mm/day). On snow-eater 326 heatwave-only days, SNOTEL dSWE was -18.0 mm/day with the 90th and 99th per327 centile melt at -38.0 mm/day and -64.0 mm/day, respectively. Comparable to the 328 all-day results, NHH best represents mean melt on snow-eater heatwave-only days 329 (-22.0 mm/day), but was more constrained on 90th percentile melt (-33.6 mm/day) 330 and, especially, on 99th percentile melt (-43.3 mm/day). HH and AHH both overesti- 

- 331 mate mean melt (-37.8 mm/day and -39.6 mm/day) and 90th percentile melt (-50.2 

- 332 mm/day and -56.2 mm/day) on snow-eater heatwave-only days, respectively. Only 

- 333 HH and AHH reach SNOTEL-like 99th percentile melt rates (-64.4 mm/day and -67.2 

- 334 mm/day, respectively). 

13 

- 335 To contextualize the severity of the 1983 snow-eater heatwave event relative to all 

- 336 5-day maximum daily melt potential events (Mx5day), we now compare 1983 to all 337 Mx5day potential events within the SNOTEL period of record (Table S2). The 1983 

- 338 snow-eater heatwave event Mx5day ranked number 13-16 (based upon the use of NHH, 

- 339 HH, or AHH). The top five Mx5day events in the SNOTEL period of record occurred 340 in 2014 (84.1 km<sup>3</sup> ), 2015 (76.7 km<sup>3</sup> ), 1992 (72.9 km<sup>3</sup> ), 1986 (72.2 km<sup>3</sup> ), and 2013 341 (58.7 km<sup>3</sup> ). 

- 342 We now compare total snow-eater heatwave melt potential estimated for 1983 with 

- 343 all seasons between 1980-2015 using the 20Cv3-SNOW-17 NHH model over the SNO- 

- 344 TEL period of record that overlaps with 20Cv3 (1980-2015; Table S3). The highest 

- 345 mean seasonal total snow-eater heatwave-only contributed melt potential year between 346 1980-2015 was 2015 at 152 km<sup>3</sup> or 23% of the total melt potential of 652 km<sup>3</sup> between 

- 347 March 19th to July 1st (Table S4). The rest of the top five years included 2013 (131 348 km<sup>3</sup> ; 21%), 1987 (95.8 km<sup>3</sup> ; 18%), 1986 (77.2 km<sup>3</sup> ; 15%), and 2014 (74.4 km<sup>3</sup> ; 11%). 

- 349 Comparatively, 1983 had a mean seasonal total snow-eater heatwave-only contributed 

- 350 melt potential of 15.4 km<sup>3</sup> (or 6% of the seasonal total melt potential between March 351 19th to July 1st). For the overlapping SNOTEL record with 20Cv3 (1985-2015), the 

- 352 climatological mean total melt potential estimates within WUS mountainous regions 

- 353 ranged between 376±58 km<sup>3</sup> (NHH) to 387±65 km<sup>3</sup> (AHH). For context, Fang et al 

- 354 (2023) showed that WUS gridded observationally-constrained SWE products had a 

- 355 climatological (1985-2021) mean peak SWE between 210-340 km<sup>3</sup> . Notably, if accu- 

- 356 mulation season melt is also included, WUS-wide climatological mean peak SWE 357 estimates are closer to 400 km<sup>3</sup> . 

- 358 Figure 4 shows all 20Cv3-SNOW-17 identified snow-eater heatwave events duration 

- 359 and mean WUS-wide mountainous region daily intensity between 1950-2010, which 

- 360 is the same corresponding period used by Tarouilly et al (2021). A complete catalog 

- 361 from 1850-2015 is provided in Figure S3. Decadal annual average snow-eater heatwave 

14 

- 362 event frequency and duration ranged between 3.4 to 5.2 events and 3.3 to 5.2 days per 

- 363 year, respectively, between 1950-2010. The dots on the plot represent the 11 spring 

- 364 superflood events that were identified and predominantly driven by snowmelt (rather 

- 365 than rainfall-only and/or rain-on-snow). There is high correspondence between our 

- 366 20Cv3-SNOW-17-based snow-eater heatwave event identifications and the superfloods 

- 367 identified by Tarouilly et al (2021), with seven of the 11 superflood events occurring 

- 368 within 5 days of our 20Cv3-SNOW-17 identified snow-eater heatwave events. Impor- 

- 369 tantly, even in the years in which a spring, snowmelt-induced superflood was identified, 

- 370 our snow-eater heatwave event methodology identified most of the events, such as in 

- 371 1983 (one of the two snowmelt superflood events were identified; Figure 2) and 1984 

- 372 (two of the three snowmelt superflood events were identified; Figure S4). The only 

- 373 year in the SNOTEL period of record in which a complete mismatch occurred between 

- 374 the 20Cv3-SNOW-17 snow-eater heatwave identification and the Tarouilly et al (2021) 

- 375 superflood catalog was in 1997 (Figure S5). In that year, the 20Cv3-SNOW-17 method- 

- 376 ology identified mid-May as the snow-eater event occurrence, whereas Tarouilly et al 

- 377 (2021) identified a superflood event in mid-June. 

### 378 3.3 Pre-industrial to present day trends in snow-eater 

- 379 heatwave characteristics 

- 380 Given the high correspondence between our 20Cv3-SNOW-17 estimates of snow- 

- 381 eater heatwaves and their melt potential compared with SNOTEL observations of 

- 382 dSWE and close proximities between snow-eater heatwave occurrences with spring, 

- 383 snowmelt-dominated superfloods identified by Tarouilly et al (2021), we next explore 

- 384 how snow-eater heatwave characteristics (e.g., area, duration, and frequency) have 

- 385 changed across WUS mountains since the 1850s. Compared to the pre-industrial period 

- 386 of 1850-1899, T2m does not demonstrate a significant trend with a Mann-Kendall 

15 

- 387 p-value of 0.408 and Theil-Sen trend of -0.041/century (Figure S6a). Despite a non- 

- 388 significant and relatively flat trend in 20Cv3-derived spring T2m, the T2m freezing 

- 389 area in WUS mountainous areas has shown a steady and significant (Mann-Kendall 

- 390 p-value of 0.019) decline since the 1850s (Figure S6b). Thus, decreases in T2m freez- 

- 391 ing area may have led to increases in snow-eater heatwave area since the 1850s. This 

- 392 is because above-freezing temperatures for three consecutive days (day and night) 

- 393 are a component of our snow-eater heatwave identification criteria. In fact, the area 

- 394 of snow-eater heatwaves has significantly (Mann-Kendall p-value of 0.028) increased, 

- 395 on average, by 102,000 km<sup>2</sup> /century across WUS-mountainous regions (Figure 5a). 

- 396 Additionally, snow-eater heatwave frequency has significantly (Mann-Kendall p-value 

- 397 of 0.017) increased by close to one event per century (Figure 5c). The increase in 

- 398 snow-eater heatwave events could be due to the erosion of the freezing level area in 

- 399 WUS-mountainous regions earlier in the late winter to early spring (e.g., March). This 

- 400 is corroborated by the finding in 20Cv3 that the month of the first snow-eater heat- 

- 401 wave occurrence happens a month earlier per century (Mann-Kendall p-value <0.001) 

- 402 between March and July (Figure 5b). However, snow-eater heatwave durations have 

- 403 significantly decreased (Mann-Kendall p-value of 0.028) by half a day since the 1850s 

- 404 (Figure 5d). As shown in Figure S3, the 50-year annual average number of snow-eater 

- 405 heatwave events and their durations vary from 3.0 events that last 5.0 days (between 406 1850-1900) to 4.1 events that last 4.3 days (1950-2000). 

- 407 Although many snow-eater heatwave characteristics between March 19th to July 

- 408 1st have significantly changed since the 1850s (i.e., area, duration, frequency, and 

- 409 month of first-occurrence), snow-eater heatwave total melt potential intensity shows a 

- 410 weaker signal (Figure 6a). Regardless of the 20Cv3-SNOW-17 model used, snow-eater 

- 411 heatwave total melt potential intensity across WUS mountainous regions increases 

16 

- 412 (Theil-Sen trend that ranges between 0.93 to 1.94 km<sup>3</sup> /century based on 20Cv3- 

- 413 SNOW-17 model used), but these trends are consistently non-significant (Mann- 

- 414 Kendall p-values >0.05). Across the three 20Cv3-SNOW-17 melt potential models, 

- 415 the average and 90th percentile WUS mountainous region snow-eater heatwave-only 

- 416 total melt potential from 1850-2015 was 47 km<sup>3</sup> and 125 km<sup>3</sup> , respectively, which rep- 

- 417 resents 10% and 22% of the total seasonal melt potential contribution, respectively 

- 418 (Figure 6b). 20Cv3-SNOW-17 average total seasonal melt potential estimates over the 

- 419 SNOTEL period of record that overlaps with 20Cv3 (1985-2015) had NHH at 376±58 

- 420 km<sup>3</sup> , HH at 384±64 km<sup>3</sup> , and AHH at 387±65 km<sup>3</sup> . The non-significant increase in 

- 421 snow-eater heatwave-only total melt potential intensity is evenly distributed between 

- 422 both daytime and nighttime (Figure 6c,d). This is likely due to average T2m trends in 

- 423 WUS mountainous regions showing a variable, yet nearly zero trend since the 1850s 

- 424 (Figure S6a). Notably, this might also be due to the anomalous WUS drought condi- 

- 425 tions of the 1850s and 1860s (or what has been termed the “Civil War drought”; Cook 

- 426 et al, 2007; Herweijer et al, 2007), which had some of the largest snow-eater heatwave- 

- 427 only total melt potential intensity estimates (Table S5), with the largest occurring in 

- 428 1869 (the year in which John Wesley Powell began his exploration of the WUS and its 

- 429 water resources; Gilbert, 1902). Based on the 20Cv3-SNOW-17 model used, the total 

- 430 snow-eater heatwave-only melt potential contribution between March 19th to July 1st 431 of 1869 was 196-341 km<sup>3</sup> or 35-45% of the total seasonal melt potential (Table S6). 

- 432 We now explore if snow-eater heatwave melt potentials have changed on daily 433 (Mx1day) and multi-day perspectives (Mx3day and Mx5day) between March 19th 

- 434 to July 1st across 1850 to 2015. Snow-eater heatwave-only Mx1day trends since the 435 1850s have increased by 1.55 to 2.53 km<sup>3</sup> per century (based on the use of NHH, 

- 436 HH, or AHH), yet non-significantly with Mann-Kendall p-values that are all >0.05 437 (Figure 7a). This same positive, yet non-significant trend also holds for snow-eater 

- 438 heatwave-only Mx3day, and Mx5day (Figure 7b,c). Mx3day has increased more (+2.35 

17 

- 439 to +4.20 km<sup>3</sup> per century) than Mx5day (+1.51 to +3.29 km<sup>3</sup> per century). However, 

- 440 both trends are non-significant (Mann-Kendall p-values >0.05). The largest snow-eater 

- 441 heatwave-only Mx5day season occurred in 2014 with estimates of 84.2 km<sup>3</sup> to 122 

- 442 km<sup>3</sup> , based on which 20Cv3-SNOW-17 model is used (Table S7). Notably, Mx1day, 

- 443 Mx3day, and Mx5day trends are all marked by large interannual variability between 444 1850-2015. 

- 445 

## 4 Discussion and Conclusions 

- 446 Snow-eater heatwaves have received little research attention; however, these events 

- 447 play a crucial role in shaping WUS snowmelt patterns, particularly in the spring 

- 448 and early summer. For example, in late May of 1983, a five-day snow-eater heatwave 

- 449 event occurred, resulting in the largest spring season, snowmelt-dominated superflood 

- 450 event in modern WUS history (Tarouilly et al, 2021). We devised a methodology to 

- 451 identify, track, and estimate the melt potential of WUS snow-eater heatwave events, 

- 452 using the 11 spring, snowmelt-dominated superflood events (e.g., 1983) as a litmus 

- 453 test of our workflow. Our methodology was developed with a use-inspired goal as 

- 454 it can be applied to any observational or gridded product that provides daily-to- 

- 455 subdaily T2m and leverages a widely used, operational snowmelt model (SNOW-17) 

- 456 to estimate snow-eater heatwave melt potentials. The melt potentials produced by 

- 457 this operational model were assessed using an “out of the box” version and several 

- 458 experimental versions that enhance melt potential during snow-eater heatwave events. 

- 459 By using T2m estimates from the 20Cv3 reanalysis, we were able to assess how 

- 460 certain snow-eater heatwave characteristics have (or have not) changed significantly 461 between 1850-2015. Our study highlights several key findings about 19th to 21st 462 century WUS snow-eater heatwave characteristics: 

- 463 1) SNOTEL observations of dSWE on snow-eater heatwave-only days have twice 

- 464 as much melt (-18 mm/day) compared to all melt days (-9.0 mm/day) across 

18 

- 465 1980–2015. This increased melt on snow-eater heatwave days also occurs in more 

- 466 extreme moments of melt distributions (e.g., 90th percentile dSWE days increase 467 from -28 mm/day on all days to -38 mm/day on snow-eater heatwave-only days). 

- 468 2) The 20Cv3-SNOW-17 melt potential methodology represents mean melt well on 469 all days (SNOTEL, -9.0 mm/day; 20Cv3-SNOW-17, -11 mm/day) and snow-eater 470 heatwave-only days (SNOTEL, -18 mm/day; 20Cv3-SNOW-17, -22 mm/day). 

- 471 3) Without enhanced melt on snow-eater heatwave days, 20Cv3-SNOW-17 melt 472 potentials underestimate extreme melt (90th and 99th percentile -dSWE days). 473 We introduce experimental 20Cv3-SNOW-17 models that better account for 474 extreme melt on snow-eater heatwave days, although with concomitant degrada475 tion in mean daily melt performance. 

- 476 4) Since the 1950s, annual average snow-eater heatwave event counts were 3–5 events 477 per year, lasting 3–5 days each. We show that seven of the 11 spring season 478 snowmelt-dominated superfloods identified by Tarouilly et al (2021) can be linked 479 in close temporal proximity to snow-eater heatwave events. This includes the 480 largest event (since the 1950s), which lasted five days in late May 1983. 

- 481 5) Since the 1850s, snow-eater heatwave event areas have increased (+102,000 km<sup>2</sup> 482 per century), durations have decreased (-0.25 day per century), frequencies have 483 increased (+1 event per century) and the month of first occurrence has shifted 484 earlier (-1 month per century) in WUS mountains. These linear estimates may 485 underestimate rates of change in recent or future decades. 

- 486 6) Between 1850–2015, the top 25 snow-eater heatwave contributed melt seasons 487 ranged between 14-45% of the March 19th to July 1st total seasonal melt 488 potential. 

- 489 7) Melt potential rates, whether from the perspective of total seasonal melt poten490 tial, Mx1day, Mx3day, and Mx5day, show a positive, yet non-significant trend 

- 491 since the 1850s. 

19 

- 492 We next present the main sources of uncertainty in the study. These include the 

- 493 differences between potential and actual snowmelt, the limitations of temperature 494 index models, and the use of the 20Cv3 reanalysis T2m estimates. 

- 495 Importantly, melt potential is not actual snowmelt. This difference is analogous 

- 496 to the limitations of potential evapotranspiration compared with actual evapotran- 

- 497 spiration (Eagleman, 1967). Melt potential thus represents an upper bound of the 

- 498 amount of possible snowmelt if sufficient snow accumulated in the weeks to months 

- 499 before a given snowmelt event. This important discrepancy was shown in our top 25 

- 500 years of total seasonal melt potential, with several of the top years corresponding with 

- 501 well-documented snow droughts (e.g., 2013-2015 in California; Belmecheri et al, 2016; 

- 502 Ullrich et al, 2018). This is especially true during snow-eater heatwave events, as the 503 potential for melt can only be realized if this amount of snow is available to melt (e.g., 504 1983). 

- 505 Temperature index snowmelt models, such as SNOW-17, are the standard approach 

- 506 at operational forecasting centers due to their reliance on a single variable (T2m) that 

- 507 is more widely accessible across WUS mountains, their computational efficiency, and 

- 508 their simplicity that helps in describing causality (Reis et al, 2025). However, temper- 

- 509 ature index snowmelt models do not represent all snow-atmosphere couplings (Betts 

- 510 et al, 2014; Rudisill et al, 2021) or the full suite of energy balance contributions to 

- 511 snowmelt. For example, WUS spring and summer snowmelt rates are also affected by 

- 512 downwelling solar radiation (Musselman et al, 2017b), snow albedo (Skiles and Painter, 

- 513 2019; Koshkin et al, 2022), relative humidity (Harpold and Brooks, 2018), snowfall 

- 514 intensity (Marshall et al, 2020), and rain-on-snow events (McCabe et al, 2007). Fur- 

- 515 thermore, temperature index models do not partition snow ablation into sublimation 

- 516 and melt, which could have contributed to some of the mismatches we found between 

- 517 our snow-eater heatwave catalog and WUS superflood event occurrences. For example, 

- 518 a snow-eater heatwave event may have sublimated rather than melted the snowpack, 

20 

- 519 leading to no streamflow response. Alternatively, earlier season melt and/or rainfall 

- 520 events may have elevated soil moisture, leading to more efficient runoff later in the 

- 521 season (Haleakala et al, 2022). Future work could investigate the effects of antecedent 

- 522 conditions before snow-eater heatwave events, and how other energy balance terms 

- 523 amplify and/or diminish snow-eater heatwave impacts on snowmelt (e.g., comparing 

- 524 pre- and post-wildfire snowmelt responses during heatwaves; Smoot and Gleason, 2021; 525 Koshkin et al, 2022). 

- 526 The 20Cv3 reanalysis dataset offers a valuable long-term, ensemble-based atmo- 

- 527 spheric dataset, with global coverage, at a sub-daily temporal frequency. Yet, its 

- 528 reliance on surface pressure-only assimilation and lack of direct snowpack or temper- 

- 529 ature observations introduces uncertainties, particularly for assessing high-resolution 

- 530 snowmelt dynamics and snow-eater heatwave events in the varied geographies of the 

- 531 WUS. For example, compared to Berkeley Earth, Climatic Research Unit, and the 

- 532 Global Historical Climatology Network, T2m estimates 20Cv3 estimates have a cooler 

- 533 spring T2m warming pattern over North America, particularly in May (Nolin et al, 

- 534 2022; Gillespie et al, 2023). These spring T2m trend discrepancies could partly be 

- 535 attributed to our evaluation of WUS mountainous regions only, where WUS low-lying 

- 536 areas have shown stronger spring warming trends due to more frequent, warm mar- 

- 537 itime air intrusion (Abatzoglou and Redmond, 2007). Additionally, while the 20Cv3 

- 538 development team has continued to make adjustments to the data from 1850-2015, 

- 539 the dataset is not currently being updated forwards in time, meaning that it cannot 

- 540 be used to assess potential shifts in snow-eater heatwave characteristics over the past 

- 541 decade (which includes some of the hottest years ever recorded; Forster et al, 2024) 542 nor in a real-time forecasting context. 

- 543 Given the identified size and potential impact on water resources and natural 

- 544 hazards, additional work on snow-eater heatwave events is needed. We envision that 

- 545 this work could include the testing of the newly developed SNOW-17 experimental 

21 

- 546 melt potential models in a real-time forecasting context, exploration of subseasonal-to- 

- 547 seasonal predictability of snow-eater heatwave events with large-scale modes of climate 

- 548 variability, and exploring how different climate scenarios and/or warming levels could 

- 549 alter snow-eater heatwave characteristics in the WUS (and other global mountainous 

- 550 regions) through the 21st century. 

- 551 Results in this study suggest that it may be beneficial to adopt different SNOW-17 

- 552 parameterizations during snow-eater heatwave and non-heatwave events (analogous to 

- 553 what is done for rain-on-snow events already in SNOW-17; Equation 6 of Anderson, 

- 554 1976, 2006) Our snow-eater heatwave identification strategy and newly developed addi- 

- 555 tive melt term during snow-eater heatwave events help SNOW-17 to better represent 

- 556 extreme snowmelt (e.g., 90th to 99th percentile -dSWE at SNOTEL sites). Therefore, 

- 557 we envision that T2m estimates from real-time weather forecasts could be leveraged 

- 558 with our newly developed SNOW-17-based probabilistic framework during snow-eater 

- 559 heatwave events to estimate the cone of uncertainty of plausible extreme snowmelt 

- 560 rates. The goal of this cone of uncertainty would be to better bracket extreme snowmelt 

- 561 potentials and provide reservoir operators and flood planners with more information 

- 562 to make decisions as snow-eater heatwave events develop and persist. 

- 563 The ability to predict the area, duration, frequency, and/or intensity of snow-eater 

- 564 heatwave events at subseasonal to seasonal timescales could also be worth explor- 

- 565 ing in future work (Lang et al, 2020). To do this, we envision that composite (Wu 

- 566 et al, 2023) and cluster-based analyses (Guirguis et al, 2023; Srivastava et al, 2025) 

- 567 could be employed with our snow-eater heatwave catalog to identify the large-scale 

- 568 meteorological patterns that give rise to snow-eater heatwave events. The large-scale 

- 569 meteorological patterns could then be used in combination with information about 

- 570 their frequency and persistence under different climate modes of variability (e.g., El 

- 571 Ni˜no Longitude Index; Patricola et al, 2020) to identify the likelihood that a given 

- 572 season might have an increased or decreased chance of snow-eater heatwave event(s). 

22 

- 573 Reservoir operators and flood planners could combine this information with seasonal 

- 574 forecasts of precipitation (Huang et al, 2021) to estimate the potential risk profile of 

- 575 both an accumulation of an abundant snowpack, combined with the potential for more 576 snow-eater heatwave events. 

- 577 The flexibility of the reported snow-eater heatwave identification framework should 

- 578 be extensible to other global mountain regions. Therefore, snow-eater heatwave char- 

- 579 acteristic changes over the last two centuries could be derived and intercompared 

- 580 across mountains (K¨orner et al, 2017) and snow climates (Sturm and Liston, 2021) to 

- 581 derive a flood potential index, analogous to the water tower index (Immerzeel et al, 

- 582 2020). Similar to what occurred in the Pacific Northwest in 2021 during a snow-eater 

- 583 heatwave event (Pelto et al, 2022), rapid glacier and seasonal melt during heatwave 

- 584 events has also been observed in the European Alps (Cremona et al, 2023) and South 

- 585 American Andes (Ayala et al, 2020; Alvaro<sup>´</sup> Gonz´alez-Reyes et al, 2023). The increas- 

- 586 ing trends in snow-eater heatwave area and frequency combined with an earlier timing 

- 587 in the spring season warrant further investigation into the middle and latter portions 

- 588 of the 21st century under different, plausible warming trajectories (Hausfather, 2025). 

- 589 There is strong evidence that global seasonal snowpacks will diminish substantially 

- 590 by the end of the century (e.g., American Cordillera; Siirila-Woodburn et al, 2021; 

- 591 Bambach et al, 2022; Rhoades et al, 2022). However, between the present decade and 

- 592 the middle of the 21st century, snow-eater heatwave-induced flooding likelihoods could 

- 593 peak before declining into the end of the 21st century, analogous to the concept of 

- 594 peak rain-on-snow introduced by Heggli et al (2022). 

23 



Fig. 1 The end-to-end workflow to identify snow-eater heatwave events, estimate their melt potentials, and assess trends in their characteristics. The blue text indicates the subsections of the manuscript where specific details about the workflow can be found. 

24 



Fig. 2 Time series comparisons of 20Cv3-SNOW-17 (colored) snowmelt potential with SNOTEL (black) daily change in snow water equivalent (dSWE) for March 19th to July 1st, 1983. a) is the “out of the box” version of SNOW-17, or the no heatwave hours (NHH) effect, melt potential model. b) and c) are the experimental heatwave hours (HH) and accumulative heatwave hours (AHH) effect SNOW-17 melt potential models, respectively. The bold lines are 50 ensemble member mean estimates and the thin lines are the deciles across all sites/nearest grid cells. The gray shaded region represents the timing and duration of the snow-eater heatwave event. The map plots show the SNOTEL sites (black dots) used for the comparison (those that fall within the snow-eater heatwave region) and the heatwave day accumulative snowmelt potential estimates by the 20Cv3-SNOW-17 models between March 19th and July 1st. 

25 



Fig. 3 Time series comparisons of the daily climatological (1980-2015) average 20Cv3-SNOW-17 (colored) snowmelt potential with SNOTEL (black) daily change in snow water equivalent (dSWE) between March 19th to July 1st. Dates are given in MM-DD on the x-axis. a-c) represent all days between March 19th and July 1st, with a) being the “out of the box” version of SNOW-17, or the no heatwave hours (NHH) effect and b) and c) are the experimental heatwave hours (HH) and accumulative heatwave hours (AHH) effect SNOW-17 models, respectively. d-f) show snow-eater heatwave-only days between March 19th to July 1st. Bold lines are 50 ensemble member mean estimates, and the dotted lines are the deciles across all sites/nearest grid cells. 

26 



Fig. 4 A catalog of 20Cv3-SNOW-17 defined snow-eater heatwave events between 1950-2010. Each line represents a unique snow-eater heatwave event identified anywhere within the WUS mountainous regions. Each line length represents the snow-eater heatwave event duration, and the line colors represent the average total snow-eater heatwave intensity over its duration derived from the NHH SNOW-17 melt potential model. Overlaid dots represent the 11 spring-season, snowmelt-induced superflood events identified by Tarouilly et al (2021). If an 20Cv3-SNOW-17 identified snow-eater heatwave event falls within 5 days of the Tarouilly et al (2021)-identified superflood events, a black dot is provided, else a hollow circle. The decadal annual average snow-eater heatwave event frequency and durations are provided on the right y-axis. 

27 

Table 1 Climatological (1980-2015) summary statistics for the daily change in snow water equivalent (dSWE; mm/day) across WUS SNOTEL stations on all days between March 19th to July 1st and on snow-eater heatwave-only days. Positive dSWE values were set to 0 mm and missing values were excluded. 1,128,750 and 55,523 dSWE measurements were recorded across all stations and years, respectively, for all days and snow-eater heatwave-only days. 

|Metric|All|Snow-Eater|
|---|---|---|
|(1980-2015)|Days|Heatwave Days|
|Mean|-9.0|-18|
|Standard|||
|Deviation|13|15|
|Median|-2.0|-16|
|75th percentile|-15|-26|
|90th percentile|-28|-38|
|99th percentile|-53|-64|





Fig. 5 Seasonal (March 19th - July 1st) anomalies in 20Cv3 derived snow-eater heatwave a) area, b) month of first occurrence, c) frequency, and d) duration from 1850-2015 over WUS mountainous regions relative to a 1850-1899 climatology. The Mann-Kendall trend p-values and Theil-Sen slope values are provided at the top right of each subplot. 

29 



Fig. 6 a-d) Seasonal (March 19th - July 1st) anomalies in 20Cv3 derived snow-eater heatwave average a) total heatwave intensity, b) contribution of heatwave melt days to total seasonal melt c) total daytime intensity, and d) total nighttime intensity from 1850-2015 over WUS mountainous regions relative to a 1850-1899 climatology. Daytime and nighttime estimates of intensity are computed by converting 20Cv3-SNOW-17 melt potential estimates into local time and then accounting for time zone offsets (every 15 degrees of longitude), solar declination, and hour angle at sunrise/sunset. Colors represent different 20Cv3-SNOW-17 models, including blue (no heatwave hours, NHH), green (heatwave hours, HH), and orange (accumulative heatwave hours, AHH). The Mann-Kendall trend p-values and Theil-Sen slope values are provided at the top of each subplot. 

30 



Fig. 7 a) Mx1day, b) Mx3day and c) Mx5day anomalies in 20Cv3-SNOW-17 derived snow-eater heatwave total intensity between March 19th to July 1st from 1850-2015 over WUS mountainous regions relative to a 1850-1899 climatology. Colors represent different 20Cv3-SNOW-17 models, including blue (no heatwave hours, NHH), green (heatwave hours, HH) and orange (accumulative heatwave hours, AHH). The Mann-Kendall trend p-values and Theil-Sen slope values for each 20Cv3-SNOW-17 model are provided at the top of each subplot. 

31 

Acknowledgements. 

595 

##### 596 

## Declarations 

##### 597 

### Funding 

- 598 This study was primarily funded by the Director, Office of Science, Office of Bio- 

- 599 logical and Environmental Research of the U.S. Department of Energy Regional 

- 600 and Global Model Analysis (RGMA) and MultiSector Dynamics Program Areas. 

- 601 Authors Rhoades, North, Risser, Mahesh, Srivastava, Wehner, and Zhou were funded 

- 602 by “the Calibrated and Systematic Characterization, Attribution and Detection 

- 603 of Extremes (CASCADE)” Science Focus Area (award no. DE-AC02-05CH11231). 

- 604 Authors Rhoades, McCrary, Rahimi, Randall, Srivastava, and Jones were funded by 

- 605 the “An Integrated Evaluation of the Simulated Hydroclimate System of the Conti- 

- 606 nental US” (HyperFACETS) project (award no. DE-SC0016605). Authors Rhoades, 

- 607 Huning, and McEvoy were funded by the National Oceanic and Atmospheric Adminis- 

- 608 tration (NOAA) Climate Program Office (CPO) Modeling, Analysis, Predictions, and 

- 609 Projections (MAPP) and National Integrated Drought Information System (NIDIS) 

- 610 programs on the “Understanding Heat Wave–Snow Drought Relationships Across 

- 611 the Western United States” project (award no. NOAA-OAR-CPO-2023-2007440) and 

- 612 author Rahimi was funded by the NOAA MAPP-NIDIS project “Towards Predicting 

- 613 Drought and Subsequent Water Resource Challenges at Landscape-Resolving Scales 

- 614 Across the Western U.S.” (award no. NA23OAR4310633-T1-01). Author Rudisill was 

- 615 supported by the U.S. Department of Energy, Office of Science, Office of Biological 

- 616 and Environmental Research, and the Atmospheric System Research Program project 

- 617 “Surface Atmosphere Integrated Field Laboratory (SAIL)” under U.S. Department of 

- 618 Energy Contract No. DE-AC02-05CH11231. Author Beltran-Pe˜na was funded by the 

- 619 Stanford Doerr School of Sustainability Dean’s Postdoctoral Fellowship from Stan- 

- 620 ford University. Author Hotaling was funded by the Agriculture and Food Research 

32 

- 621 Initiative Competitive Grant (award no. 2021-69012-35916) from the USDA National 

- 622 Institute of Food and Agriculture. 

### 623 Conflict of interest 

- 624 The authors do not have any financial or non-financial conflicts of interest to disclose. 

### 625 Ethical approval 

626 This declaration does not apply to this work. 

##### 627 

### Code and data availability 

- 628 The 20Cv3 post-processed data and snow-eater heatwave tracking, analysis, and 

- 629 plotting scripts can be found via a publicly accessible repository (Science Gate- 

- 630 way) through the National Energy Research Scientific Computing Center - https: 631 //portal.nersc.gov/archive/home/a/arhoades/www/NOA <mark>A S</mark> no <mark>w D</mark> rough <mark>t H</mark> eatwave 

##### 632 

## References 

- 633 Abatzoglou JT, Redmond KT (2007) Asymmetry between trends in spring 634 and autumn temperature and circulation regimes over western north amer635 ica. Geophysical Research Letters 34(18). https://doi.org/https://doi.org/10.1029/ 636 2007GL030891 

- 637 Allen M, Dube OP, Solecki W, et al (2018) Special report: Global warming of 1.5 c. 638 Intergovernmental Panel on Climate Change (IPCC) 677:393. https://doi.org/https: 639 //www.ipcc.ch/sr15/chapter/chapter-1/ 

- 640 Allen S, Bhend J, Martius O, et al (2023) Weighted verification tools to eval641 uate univariate and multivariate probabilistic forecasts for high-impact weather 

33 

- 642 events. Weather and Forecasting 38(3):499 – 516. https://doi.org/10.1175/ 

643 

WAF-D-22-0161.1 

- 644 Anderson E (1976) A point energy and mass balance model of a snow cover. National 

- 645 Weather Service, https://repository.library.noaa.gov/view/noaa/6392 

- 646 Anderson E (2006) Snow Accumulation and Ablation Model – SNOW-17. https:// 647 www.weather.gov/media/owp/oh/hrl/docs/22snow17.pdf 

- 648 Arnow T (1984) Water-level and water-quality changes in Great Salt Lake, Utah, 649 1847-1983, vol 913. US Department of the Interior, Geological Survey, https://doi. 650 org/https://doi.org/10.3133/cir913 

- 651 Ayala A, Far´ıas-Barahona D, Huss M, et al (2020) Glacier runoff variations since 1955 652 in the maipo river basin, in the semiarid andes of central chile. The Cryosphere 653 14(6):2005–2027. https://doi.org/10.5194/tc-14-2005-2020 

- 654 Baker SA, Wood AW, Rajagopalan B, et al (2022) The colorado river basin oper655 ational prediction testbed: A framework for evaluating streamflow forecasts and 

- 656 reservoir operations. JAWRA Journal of the American Water Resources Association 657 58(5):690–708. https://doi.org/https://doi.org/10.1111/1752-1688.13038 

- 658 Bambach NE, Rhoades AM, Hatchett BJ, et al (2022) Projecting climate change 659 in south america using variable-resolution community earth system model: An 660 application to chile. International Journal of Climatology 42(4):2514–2542. https: 661 //doi.org/https://doi.org/10.1002/joc.7379 

- 662 Belmecheri S, Babst F, Wahl ER, et al (2016) Multi-century evaluation of sierra 663 nevada snowpack. Nature Climate Change 6(1):2–3. https://doi.org/https://doi. 664 org/10.1038/nclimate2809 

34 

- 665 Beltran-Pe˜na AA, Rhoades A, Burakowski EA, et al (2025) Future implications 

- 666 of enhanced hydroclimate variability and reduced snowpack on california’s water 667 resources. Environmental Research: Water 1(2). https://doi.org/https://iopscience. 668 iop.org/article/10.1088/3033-4942/ade7aa 

- 669 Bercos-Hickey E, O’Brien TA, Wehner MF, et al (2022) Anthropogenic contri- 

- 670 butions to the 2021 pacific northwest heatwave. Geophysical Research Letters 671 49(23):e2022GL099396. https://doi.org/https://doi.org/10.1029/2022GL099396, 672 e2022GL099396 2022GL099396 

- 673 Betts AK, Desjardins R, Worth D, et al (2014) Coupling of winter climate transitions 674 to snow and clouds over the prairies. Journal of Geophysical Research: Atmospheres 675 119(3):1118–1139. https://doi.org/https://doi.org/10.1002/2013JD021168 

- 676 Burgi PH (2020) 1983 Flow Emergency at Glen Canyon Dam—The Fastest Boat 677 through the Grand Canyon, American Society of Civil Engineers (ASCE), pp 23– 678 33. https://doi.org/10.1061/9780784482995.003, https://ascelibrary.org/doi/pdf/ 679 10.1061/9780784482995.003 

- 680 Compo GP, Whitaker JS, Sardeshmukh PD (2006) Feasibility of a 100-year reanalysis 681 using only surface pressure data. Bulletin of the American Meteorological Society 682 87(2):175 – 190. https://doi.org/10.1175/BAMS-87-2-175, URL https://journals. 683 ametsoc.org/view/journals/bams/87/2/bams-87-2-175.xml 

- 684 Cook ER, Seager R, Cane MA, et al (2007) North american drought: Reconstructions, 

- 685 causes, and consequences. Earth-Science Reviews 81(1-2):93–134. https://doi.org/ 686 https://doi.org/10.1016/j.earscirev.2006.12.002 

35 

- 687 Cremona A, Huss M, Landmann JM, et al (2023) European heat waves 2022: contribu- 

- 688 tion to extreme glacier melt in switzerland inferred from automated ablation read689 ings. The Cryosphere 17(5):1895–1912. https://doi.org/10.5194/tc-17-1895-2023 

- 690 Cristea NC, Breckheimer I, Raleigh MS, et al (2017) An evaluation of terrain-based 691 downscaling of fractional snow covered area data sets based on lidar-derived snow 692 data and orthoimagery. Water Resources Research 53(8):6802–6820. https://doi. 693 org/https://doi.org/10.1002/2017WR020799 

- 694 DeWalle DR, Rango A (2008) Principles of Snow Hydrology. Chapter 6. Snowpack 695 energy exchange: basic theory, Cambridge University Press, p 146–181. https://doi. 696 org/10.1017/CBO9780511535673.007 

- 697 Disher B, Edwards B, Lawler T, et al (2021) Measuring Heatwaves and Their 698 Impacts, Springer US, New York, NY, pp 455–475. https://doi.org/10.1007/ 699 978-1-0716-0596- <mark>7 1</mark> 102 

- 700 Duan S, Ullrich P, Risser M, et al (2024) Using temporal deep learning 701 models to estimate daily snow water equivalent over the rocky mountains. 702 Water Resources Research 60(4):e2023WR035009. https://doi.org/https://doi.org/ 703 10.1029/2023WR035009, e2023WR035009 2023WR035009 

- 704 Eagleman JR (1967) Pan evaporation, potential and actual evapotranspiration. Jour705 nal of Applied Meteorology and Climatology 6(3):482 – 488. https://doi.org/10. 706 1175/1520-0450(1967)006⟨0482:PEPAAE⟩2.0.CO;2 

- 707 Fang Y, Liu Y, Li D, et al (2023) Spatiotemporal snow water storage uncertainty 708 in the midlatitude american cordillera. The Cryosphere 17(12):5175–5195. https: 709 //doi.org/10.5194/tc-17-5175-2023 

36 

- 710 Forster PM, Smith C, Walsh T, et al (2024) Indicators of global climate change 2023: 

- 711 annual update of key indicators of the state of the climate system and human 712 influence. Earth System Science Data 16(6):2625–2658. https://doi.org/10.5194/ 713 essd-16-2625-2024 

- 714 Gilbert GK (1902) John wesley powell. Science 16(406):561–567. https://doi.org/10. 715 1126/science.16.406.561 

- 716 Gillespie I, Haimberger L, Compo GP, et al (2023) Assessing homogeneity of land 717 surface air temperature observations using sparse-input reanalyses. International 718 Journal of Climatology 43(2):736–760. https://doi.org/https://doi.org/10.1002/joc. 719 7822 

- 720 ´Alvaro Gonz´alez-Reyes, Jacques-Coper M, Bravo C, et al (2023) Evolution of heat721 waves in chile since 1980. Weather and Climate Extremes 41:100588. https://doi. 722 org/https://doi.org/10.1016/j.wace.2023.100588 

- 723 Guirguis K, Gershunov A, Hatchett BJ, et al (2023) Subseasonal prediction of 724 impactful california winter weather in a hybrid dynamical-statistical framework. 725 Geophysical Research Letters 50(23):e2023GL105360. https://doi.org/https://doi. 726 org/10.1029/2023GL105360, e2023GL105360 2023GL105360 

- 727 Haleakala K, Brandt WT, Hatchett BJ, et al (2022) Watershed memory amplified 728 the oroville rain-on-snow flood of february 2017. PNAS Nexus 2(1):pgac295. https: 729 //doi.org/10.1093/pnasnexus/pgac295 

- 730 Harpold AA, Brooks PD (2018) Humidity determines snowpack ablation under a 

- 731 warming climate. Proceedings of the National Academy of Sciences 115(6):1215– 732 1220. https://doi.org/10.1073/pnas.1716789115 

37 

- 733 Hatchett BJ (2021) Seasonal and ephemeral snowpacks of the conterminous united 734 states. Hydrology 8(1). https://doi.org/10.3390/hydrology8010032 

- 735 Hatchett BJ, Bacon S, Brandt WT, et al (2023) Snowmelt-triggered debris flows 

- 736 in seasonal snowpacks. Proceedings of the 8th International Conference on Debris 737 Flow Hazard Mitigation (DFHM8), Torino, Italy 415:1–4. https://doi.org/10.1051/ 738 e3sconf/202341504006 

- 739 Hausfather Z (2025) An assessment of current policy scenarios over the 21st cen740 tury and the reduced plausibility of high-emissions pathways. Dialogues on Climate 741 Change 2(1):26–32. https://doi.org/10.1177/29768659241304854 

- 742 He M, Hogue TS, Franz KJ, et al (2011) Characterizing parameter sensitiv- 

- 743 ity and uncertainty for a snow model across hydroclimatic regimes. Advances 744 in Water Resources 34(1):114–127. https://doi.org/https://doi.org/10.1016/j. 745 advwatres.2010.10.002 

- 746 Heggli A, Hatchett B, Schwartz A, et al (2022) Toward snowpack runoff decision 747 support. Iscience 25(5). https://doi.org/https://doi.org/10.1016/j.isci.2022.104240 

- 748 Hersbach H (2000) Decomposition of the continuous ranked probability score for 

- 749 ensemble prediction systems. Weather and Forecasting 15(5):559 – 570. https: 750 //doi.org/10.1175/1520-0434(2000)015⟨0559:DOTCRP⟩2.0.CO;2 

- 751 Herweijer C, Seager R, Cook ER, et al (2007) North american droughts of the last 

- 752 millennium from a gridded network of tree-ring data. Journal of Climate 20(7):1353 753 – 1376. https://doi.org/10.1175/JCLI4042.1 

- 754 Huang H, Patricola CM, Bercos-Hickey E, et al (2021) Sources of subseasonal-to- 

- 755 seasonal predictability of atmospheric rivers and precipitation in the western united 

- 756 states. Journal of Geophysical Research: Atmospheres 126(6):e2020JD034053. https: 

38 

- 757 

   - //doi.org/https://doi.org/10.1029/2020JD034053, e2020JD034053 2020JD034053 

- 758 Immerzeel WW, Lutz AF, Andrade M, et al (2020) Importance and vulnerability of 

- 759 the world’s water towers. Nature 577(7790):364–369. https://doi.org/https://doi. 760 org/10.1038/s41586-019-1822-y 

- 761 Jennings KS, Kittel TGF, Molotch NP (2018) Observations and simulations of the 

- 762 seasonal evolution of snowpack cold content and its relation to snowmelt and 763 the snowpack energy budget. The Cryosphere 12(5):1595–1614. https://doi.org/10. 764 5194/tc-12-1595-2018 

- 765 K¨orner C, Jetz W, Paulsen J, et al (2017) A global inventory of mountains for bio766 geographical applications. Alpine Botany 127(1):1–15. https://doi.org/https://doi. 767 org/10.1007/s00035-016-0182-6 

- 768 Koshkin AL, Hatchett BJ, Nolin AW (2022) Wildfire impacts on western united states 769 snowpacks. Frontiers in Water Volume 4 - 2022. https://doi.org/10.3389/frwa.2022. 770 971271 

- 771 Lang AL, Pegion K, Barnes EA (2020) Introduction to special collection: “bridg- 

- 772 ing weather and climate: Subseasonal-to-seasonal (s2s) prediction”. Journal of 773 Geophysical Research: Atmospheres 125(4):e2019JD031833. https://doi.org/https: 774 //doi.org/10.1029/2019JD031833, e2019JD031833 2019JD031833 

- 775 Lehner F, Wahl ER, Wood AW, et al (2017a) Assessing recent declines in upper 

- 776 rio grande runoff efficiency from a paleoclimate perspective. Geophysical Research 777 Letters 44(9):4124–4133. https://doi.org/https://doi.org/10.1002/2017GL073253 

- 778 Lehner F, Wood AW, Llewellyn D, et al (2017b) Mitigating the impacts of climate 

- 779 nonstationarity on seasonal streamflow predictability in the u.s. southwest. Geo- 

- 780 physical Research Letters 44(24):12,208–12,217. https://doi.org/https://doi.org/10. 

39 

- 781 

1002/2017GL076043 

- 782 Li D, Chen Y, Lyu L, et al (2024) Uncovering historical reservoir operation rules 

- 783 and patterns: Insights from 452 large reservoirs in the contiguous united states. 784 Water Resources Research 60(8):e2023WR036686. https://doi.org/https://doi.org/ 785 10.1029/2023WR036686, e2023WR036686 2023WR036686 

- 786 Lindskov K (1984) Floods of may to june 1983 along the northern wasatch front, salt 787 lake city to north ogden, utah. Tech. rep., US Geological Survey, https://doi.org/ 788 https://doi.org/10.3133/ofr84456 

- 789 L´opez-Moreno JI, Revuelto J, Gilaberte M, et al (2014) The effect of slope aspect 

- 790 on the response of snowpack to climate warming in the pyrenees. Theoretical 791 and Applied Climatology 117:207–219. https://doi.org/https://doi.org/10.1007/ 792 s00704-013-0991-0 

- 793 Mahesh A, Collins W, Bonev B, et al (2025) Huge ensembles part i: Design of ensemble 794 weather forecasts using spherical fourier neural operators. URL https://arxiv.org/ 795 abs/2408.03100, 2408.03100 

- 796 Marshall AM, Link TE, Robinson AP, et al (2020) Higher snowfall intensity is asso- 

- 797 ciated with reduced impacts of warming upon winter snow ablation. Geophysical 798 Research Letters 47(4):e2019GL086409. https://doi.org/https://doi.org/10.1029/ 799 2019GL086409, e2019GL086409 2019GL086409 

- 800 Marshall AM, Abatzoglou JT, Rahimi S, et al (2024) California’s 2023 snow deluge: 

- 801 Contextualizing an extreme snow year against future climate change. Proceedings 802 of the National Academy of Sciences 121(20):e2320600121. https://doi.org/10.1073/ 803 pnas.2320600121 

40 

- 804 McCabe GJ, Clark MP, Hay LE (2007) Rain-on-snow events in the western united 

- 805 states. Bulletin of the American Meteorological Society 88(3):319 – 328. https:// 806 doi.org/10.1175/BAMS-88-3-319 

- 807 McEvoy DJ, Hatchett BJ (2023) Spring heat waves drive record western united states 808 snow melt in 2021. Environmental Research Letters 18(1):014007. https://doi.org/ 809 10.1088/1748-9326/aca8bd 

- 810 Musselman KN, Clark MP, Liu C, et al (2017a) Slower snowmelt in a warmer 811 world. Nature Climate Change 7(3):214–219. https://doi.org/https://doi.org/10. 812 1038/nclimate3225 

- 813 Musselman KN, Molotch NP, Margulis SA (2017b) Snowmelt response to simulated 814 warming across a large elevation gradient, southern sierra nevada, california. The 815 Cryosphere 11(6):2847–2866. https://doi.org/10.5194/tc-11-2847-2017 

- 816 Musselman KN, Addor N, Vano JA, et al (2021) Winter melt trends portend 817 widespread declines in snow water resources. Nature Climate Change 11(5):418–424. 818 https://doi.org/https://doi.org/10.1038/s41558-021-01014-9 

- 819 Nolin AF, Girardin MP, Tardif JC, et al (2022) A 247-year tree-ring reconstruction of 820 spring temperature and relation to spring flooding in eastern boreal canada. Inter821 national Journal of Climatology 42(12):6479–6498. https://doi.org/https://doi.org/ 822 10.1002/joc.7608 

- 823 Norris J, Rahimi S, Huang L, et al (2025) Uncertainty of 21st century western 824 us snowfall loss derived from regional climate model large ensemble. npj Cli- 

- 825 mate and Atmospheric Science 8(1):134. https://doi.org/https://doi.org/10.1038/ 826 s41612-025-01002-2 

41 

- 827 Null SE, Prudencio L (2016) Climate change effects on water allocations with season 

- 828 dependent water rights. Science of The Total Environment 571:943–954. https:// 829 doi.org/https://doi.org/10.1016/j.scitotenv.2016.07.081 

- 830 NWS (2004) Initial Parameter Values for the Hydro-17 Snow Model. IV.2.2-SNOW-17. 831 https://www.weather.gov/media/owp/oh/hrl/docs/422snow17.pdf 

- 832 Ohmura A (2001) Physical basis for the temperature-based melt-index method. 833 Journal of Applied Meteorology 40(4):753 – 761. https://doi.org/10.1175/ 834 1520-0450(2001)040⟨0753:PBFTTB⟩2.0.CO;2 

- 835 O’Brien JP, Deser C (2023) Quantifying and understanding forced changes to unforced 836 modes of atmospheric circulation variability over the north pacific in a coupled 837 model large ensemble. Journal of Climate 36(1):19 – 37. https://doi.org/10.1175/ 838 JCLI-D-22-0101.1 

- 839 Patricola CM, O’Brien JP, Risser MD, et al (2020) Maximizing enso as a source 840 of western us hydroclimate predictability. Climate Dynamics 54(1):351–372. https: 841 //doi.org/https://doi.org/10.1007/s00382-019-05004-8 

- 842 Pelto MS, Dryak M, Pelto J, et al (2022) Contribution of glacier runoff during 843 heat waves in the nooksack river basin usa. Water 14(7). https://doi.org/10.3390/ 844 w14071145 

- 845 Reis W, Giovando J, Bartles M, et al (2025) Snow model complexity evalu- 

- 846 ation for real-time streamflow forecasting. Journal of Hydrology 659:133197. 847 https://doi.org/https://doi.org/10.1016/j.jhydrol.2025.133197, URL https://www. 848 sciencedirect.com/science/article/pii/S0022169425005359 

42 

- 849 Reyes L, Kramer MG (2023) High-elevation snowpack loss during the 2021 

- 850 pacific northwest heat dome amplified by successive spring heatwaves. npj Cli851 mate and Atmospheric Science 6(1):208. https://doi.org/https://doi.org/10.1038/ 852 s41598-017-12520-2 

- 853 Rhoades AM, Ullrich PA, Zarzycki CM (2018) Projecting 21st century snowpack 854 trends in western usa mountains using variable-resolution cesm. Climate Dynamics 855 50(1):261–288. https://doi.org/https://doi.org/10.1007/s00382-017-3606-0 

- 856 Rhoades AM, Hatchett BJ, Risser MD, et al (2022) Asymmetric emergence of low857 to-no snow in the midlatitudes of the american cordillera. Nature Climate Change 858 12(12):1151–1159. https://doi.org/10.1038/s41558-022-01518-y 

- 859 Rudisill W, Flores A, McNamara J (2021) The impact of initial snow conditions on 

- 860 the numerical weather simulation of a northern rockies atmospheric river. Journal 

- 861 of Hydrometeorology 22(1):155 – 167. https://doi.org/10.1175/JHM-D-20-0018.1 

- 862 

   - Schulzweida U (2023) Cdo user guide. https://doi.org/10.5281/zenodo.10020800 

- 863 Seneviratne SI, Zhang X, Adnan M, et al (2021) Weather and climate extreme events 

- 864 in a changing climate (chapter 11). In: Masson-Delmotte V, Zhai P, Pirani A, et al 865 (eds) IPCC 2021: Climate Change 2021: The Physical Science Basis. Contribution 866 of Working Group I to the Sixth Assessment Report of the Intergovernmental Panel 867 on Climate Change. Cambridge University Press, Cambridge, United Kingdom and 868 New York, NY, USA, p 1513–1766, https://doi.org/10.1017/9781009157896.013, 869 URL https://www.ipcc.ch/report/ar6/wg1/ 

- 870 Shepherd TG, Boyd E, Calel RA, et al (2018) Storylines: an alternative approach 

- 871 to representing uncertainty in physical aspects of climate change. Climatic change 

- 872 151(3):555–571. https://doi.org/https://doi.org/10.1007/s10584-018-2317-9 

43 

- 873 Siirila-Woodburn E, Rhoades A, Hatchett B, et al (2021) Evidence of a low- 

- 874 to-no snow future and its impacts on water resources in the western United 875 States. Nature Reviews Earth and Environment 2:800–819. https://doi.org/10. 876 1038/s43017-021-00219-y 

- 877 Skiles SM, Painter TH (2019) Toward understanding direct absorption and grain 878 size feedbacks by dust radiative forcing in snow with coupled snow physical and 879 radiative transfer modeling. Water Resources Research 55(8):7362–7378. https: 880 //doi.org/https://doi.org/10.1029/2018WR024573 

- 881 Slivinski LC, Compo GP, Whitaker JS, et al (2019) Towards a more reli882 able historical reanalysis: Improvements for version 3 of the twentieth 883 century reanalysis system. Quarterly Journal of the Royal Meteorologi884 cal Society 145(724):2876–2908. https://doi.org/https://doi.org/10.1002/qj. 885 3598, URL https://rmets.onlinelibrary.wiley.com/doi/abs/10.1002/qj.3598, 886 https://rmets.onlinelibrary.wiley.com/doi/pdf/10.1002/qj.3598 

- 887 Slivinski LC, Compo GP, Sardeshmukh PD, et al (2021) An evaluation of the perfor888 mance of the twentieth century reanalysis version 3. Journal of Climate 34(4):1417 889 – 1438. https://doi.org/10.1175/JCLI-D-20-0505.1, URL https://journals.ametsoc. 890 org/view/journals/clim/34/4/JCLI-D-20-0505.1.xml 

- 891 Smoot EE, Gleason KE (2021) Forest fires reduce snow-water storage and advance the 892 timing of snowmelt across the western u.s. Water 13(24). https://doi.org/10.3390/ 893 w13243533 

- 894 Srivastava AK, Grotjahn R, Rhoades AM, et al (2025) Large-scale statistically mean895 ingful patterns (lsmps) associated with precipitation extremes over northern califor- 

- 896 nia. Journal of Geophysical Research: Atmospheres 130(5):e2024JD041307. https: 

- 897 //doi.org/https://doi.org/10.1029/2024JD041307, e2024JD041307 2024JD041307 

44 

- 898 Stan Development Team (2024) Stan modeling language users guide and reference 899 manual, version 2.36.0. URL https://mc-stan.org 

- 900 Sturm M, Liston GE (2021) Revisiting the global seasonal snow classification: 

- 901 An updated dataset for earth system applications. Journal of Hydrometeorology 902 22(11):2917 – 2938. https://doi.org/10.1175/JHM-D-21-0070.1 

- 903 Tarouilly E, Li D, Lettenmaier DP (2021) Western u.s. superfloods in the recent 904 instrumental record. Water Resources Research 57(9):e2020WR029287. https://doi. 905 org/https://doi.org/10.1029/2020WR029287 

- 906 Ullrich PA, Xu Z, Rhoades A, et al (2018) California’s drought of the future: A 907 midcentury recreation of the exceptional conditions of 2012–2017. Earth’s Future 908 6(11):1568–1587. https://doi.org/https://doi.org/10.1029/2018EF001007 

- 909 Ullrich PA, Zarzycki CM, McClenny EE, et al (2021) Tempestextremes v2.1: 

- 910 a community framework for feature detection, tracking, and analysis in large 911 datasets. Geoscientific Model Development 14(8):5023–5048. https://doi.org/10. 912 5194/gmd-14-5023-2021 

- 913 Welty J, Zeng X (2021) Characteristics and causes of extreme snowmelt over 914 the conterminous united states. Bulletin of the American Meteorological Society 915 102(8):E1526 – E1542. https://doi.org/10.1175/BAMS-D-20-0182.1 

- 916 Wilks DS (2011) Statistical methods in the atmospheric sciences, vol 100. Academic 917 press, https://doi.org/https://doi.org/10.1016/C2017-0-03921-6 

- 918 Wu S, Luo M, Zhao R, et al (2023) Local mechanisms for global daytime, nighttime, 919 and compound heatwaves. NPJ Climate and Atmospheric Science 6(1):36. https: 920 //doi.org/https://doi.org/10.1038/s41612-023-00365-8 

45 

- 921 

## Supplemental Material 

- 922 

### SNOW-17 parameter estimation workflow 

- 923 The SNOW-17 non-rain melt potential equation has two empirical parameters that 

- 924 dictate the strength of the relationship between two-meter air temperature (T2m) and 

- 925 the daily change in snow water equivalent (dSWE): MFmin and MFmax. Traditionally, 

- 926 these parameters are chosen by the user, based on local knowledge of the region of 

- 927 interest (e.g., land surface cover) and/or by using a NOAA technical manual (NWS, 

- 928 2004). However, to better quantify snow-eater heatwave characteristics and impacts 

- 929 across WUS, we propose a method for deriving data-driven estimates of the SNOW-17 

- 930 parameters that vary spatially across the diverse topographical and snow regimes of 931 the WUS (Hatchett, 2021). Importantly, our approach can account for the uncertainty 932 implied by using fixed values within the melt potential equation. 

- 933 Our proposed statistical model relates in situ measurements of dSWE provided 

- 934 by the SNow TELemetry (SNOTEL) Network (https://nwcc-apps.sc.egov.usda.gov/ 

- 935 imap/) with collocated gridded estimates of T2m from the NOAA-CIRES-DOE 20th 

- 936 Century Reanalysis version 3 (20Cv3; Compo et al, 2006; Slivinski et al, 2019, 2021). 

- 937 Because we are only interested in the late-spring to early-summer portion of the water 

- 938 year (March 19th to July 1st), we see in Equation 2 that the product of Sv(d)Av(d) 

- 939 is close to 1 over much of this period. This results in an almost negligible influence 

- 940 of MFmin over the late spring to early summer, with an MFmin choice of 0.2 versus 

- 941 0.5 yielding a difference in average melt rates of approximately 0.15 mm/day. There- 

- 942 fore, we fix MFmin = 0.5, the upper bound of the suggested range between 0.2-0.5 

- 943 (e.g., Table 1 in NWS (2004)). Notably, NWS (2004) mentions that MFmin = 0.5 is 

- 944 representative of a more ripened snowpack, particularly in an open area or partially 

- 945 forested, whereas MFmin = 0.2 is representative of a high-albedo snowpack in a dense 

- 946 forest. By setting MFmin = 0.5 we expect that the SNOW-17 melt potential equation 

46 

- 947 will more realistically represent WUS-wide snowmelt dynamics between March 19th 948 to July 1st. 

- 949 Our statistical model assumes that dSWE(s, d) is measured at SNOTEL station 

- 950 s on day d, and defines g as the 20Cv3 grid cell location s falls within. We model 951 dSWE(s, d) as 

dSWE(s, d) = Mnr(MFmin, MFmax(s), Ta(s, d), Sv(d), Av(d)) + ϵ(s, d) MFmax(s) = (U − MFmin) ∗ ℓ(s) + MFmin 

ℓ(s) = Φ<sup>−1</sup> (x<sup>′</sup> (s)β + ψ<sup>′</sup> (s)α) 

- 952 where Φ<sup>−1</sup> denotes the inverse cumulative normal distribution function, x<sup>′</sup> (s) is a 

- 953 length-three vector of measurable covariates (e.g., intercept, elevation and the Diurnal 

- 954 Anisotropic Heat, DAH, index) for grid s with associated regression coefficients β, U 

- 955 is the upper bound of MFmax (set to 2 based on suggestions made in NWS, 2004), 956 MFmin is set to 0.5, ψ<sup>′</sup> (g) is a length-100 vector of basis functions with associated 

- 957 basis coefficients α, and ϵ is normally distributed with mean zero and variance σ<sup>2</sup> . The 

- 958 basis functions are constructed using B-splines defined over the 20Cv3 spatial domain 

- 959 with 100 knot points spaced equally across the domain. The model is estimated in 

- 960 a Bayesian framework using Stan (Stan Development Team, 2024). We assign diffuse 

- 961 normal priors to α and β and a half-Cauchy prior to σ<sup>2</sup> . For every SNOW-17 melt 

- 962 potential parameterization, we obtain 3000 posterior draws, treating the first 1500 

- 963 as “burn-in”. Convergence is assessed graphically, with R<sup>2</sup> , and effective sample size, 

- 964 and no issues were detected. The three static covariates were chosen because they 

- 965 play a critical role in WUS snowmelt dynamics (Duan et al, 2024). In particular, the 

- 966 use of DAH incorporates the effects of aspect and slope on solar radiation loading 

- 967 on the snowpack (Cristea et al, 2017), which critically shapes snowmelt dynamics on 

- 968 south-facing slopes (L´opez-Moreno et al, 2014). 

47 

- 969 The SNOW-17 parameter estimation results in 1500 plausible estimates of MFmax 

- 970 across the WUS for each year in which SNOTEL observations and static covariates 971 are available (1980-2015). To ensure that our parameter estimates used in the melt 

- 972 potential equation perform well across years (rather than being fine-tuned for any 

- 973 particular year), we perform a weighted average of the 1500 estimates based on the 

- 974 number of SNOTEL sites in a given year. Due to the addition of new stations within 

- 975 the SNOTEL network between 1980-2015, SWE measurements range from 8,254 mea- 

- 976 surements in 1980 to 39,474 measurements in 2015. Therefore, parameter estimates 

- 977 in 2015 are weighted more than those produced in 1980. When we compute SNOW- 

- 978 17-based estimates of melt potential, a random selection of 50 of the 1500 WUS-wide 

- 979 parameter fields is used. The choice of 50 ensemble members is a balance between 

- 980 the representation of the underlying distribution of the melt potential estimates and 

- 981 computational resources (e.g., computational memory and post-processing feasibility). 

- 982 To incorporate the potential enhanced melt influence of snow-eater heatwaves, we 

- 983 modify the “out of the box” version of the SNOW-17 non-rain melt model (Equation 1) 984 with an additive natural log term that accounts for the snow-eater heatwave influence 985 (HWI). 



<!-- Start of picture text -->
Mnr (d) = � HWI(k, d, hw(d)) + Mf (h) ∗ (Ta(h) − MBASE) (4)<br>h∈d<br><!-- End of picture text -->

- 986 where HWI(k, d, hw(d)) denotes the heatwave influence for day d and the strength of 

- 987 the heatwave influence on melt potential is scaled based on a single parameter k and 

- 988 a measure of the heatwave presence and duration tracked using an array of Climate 

- 989 Data Operators (CDO; Schulzweida, 2023) and the TempestExtremes StitchBlobs 

- 990 algorithm (Ullrich et al, 2021), denoted hw. 

48 

- 991 For this study, we compare the performance of the “out of the box” SNOW-17 

- 992 non-rain melt, or the no heatwave hour (NHH) model, against three different experi993 mental models that utilize different forms of HWI. These experimental models include 994 the effects of heatwave hours (HH), sustained accumulative heatwave hours (SAHH), 995 and accumulative heatwave hours (AHH). The main difference between these three 996 experimental models is in how the HWI function is defined: 

- 997 

   - NHH: HWI(k, d, hw(d)) = 0 

- 998 `•` HH: HWI(k, d, hw(d)) = log(1 + k ∗ hw(d)) where hw(d) = 0 (no heatwave 999 occurrence) or 1 (heatwave occurrence) between March 19th to July 1st 

- 1000 `•` SAHH: HWI(k, d, hw(d)) = log(1 + k ∗ hw(d)) where hw(d) = 0 (no heatwave 1001 occurrence) or 1, 2, 3, ... (heatwave occurrence) and the heatwave effects are 1002 sustained throughout March 19th to July 1st 

- 1003 `•` AHH: HWI(k, d, hw(d)) = log(1 + k ∗ hw(d)) where hw(d) = 0 (no heatwave 1004 occurrence) or 1, 2, 3, ... (heatwave occurrence) and the accumulative heatwave 1005 effects are reset after the end of each heatwave event between March 19th to July 1006 1st 

- 1007 To evaluate the fidelity of the SNOW-17 experimental model’s melt potential esti1008 mates during a snow-eater heatwave event, we set the k parameter to a fixed value of 1009 either 1, 5, or 10. A back-of-the-envelope estimation of the additional melt potential 1010 that would occur during a snow-eater heatwave event with k=1 vs k=10 in the HH 1011 model would be +0.7 mm/day to +2.4 mm/day, respectively. The sensitivity of the 1012 k parameter choice in the HH, AHH, and SAHH experimental models’ melt potential 

- 1013 estimates is discussed in more detail in the next section. 

49 

- 1014 

### 20Cv3-SNOW-17 model ranking and selection 

- 1015 To identify the best-performing 20Cv3-SNOW-17 models to use for our analysis, we 

- 1016 benchmark their model estimates of daily melt potential to dSWE provided by SNO- 

- 1017 TEL stations. We compare melt potential estimates with daily dSWE observations 

- 1018 over an overlapping climatological period (1980-2015) between the 20Cv3 and the 

- 1019 SNOTEL measurement record. To ensure that the 20Cv3-SNOW-17 melt potential 

- 1020 model estimates are fairly compared with the SNOTEL measurements of dSWE (as 

- 1021 melt potentials can continue to be estimated after an snowpack has fully melted), we 

- 1022 identify the date at which SWE reaches 0 mm at a given SNOTEL site and constrain 

- 1023 the melt potential estimates that are compared to only values that occurred up to 

- 1024 that same date. We also set all positive dSWE values at SNOTEL sites to 0 mm, as 

- 1025 the SNOW-17 melt potential equation is not designed to estimate snow accumulation. 

- 1026 Therefore, the 2OCv3-SNOW-17 melt potential estimates are compared to all non- 

- 1027 zero and non-missing daily dSWE measurements between March 19th and July 1st 1028 across the WUS. 

- 1029 To quantitatively identify the best-performing models, we use two metrics com- 

- 1030 monly employed by ensemble weather forecast centers (Mahesh et al, 2025). These 

- 1031 metrics include the Continuous Ranked Probability Score (CRPS; Hersbach, 2000) 1032 and the outcome-weighted CRPS (owCRPS; Allen et al, 2023). CRPS is valuable for 

- 1033 model performance evaluations of the mean, whereas owCRPS is used to evaluate 

- 1034 model skill for particular thresholds or exceedances of interest (e.g., extreme snowmelt 

- 1035 rates of concern). These metrics are generally applied to ensemble forecasts to compare 

- 1036 their probabilistic forecasts with a single observed value. Our 20Cv3-SNOW-17 melt 

- 1037 potential framework produces 50 plausible estimates of melt potential at each grid- 

- 1038 cell, enabling the use of CRPS and owCRPS. Notably, CRPS metrics are employed by 

- 1039 the US Bureau of Reclamation to evaluate its Colorado River Basin reservoir inflow 

- 1040 model performance (Baker et al, 2022). 

50 

- 1041 The owCRPS dSWE thresholds were chosen to be -25 mm/day and -50 mm/day, 1042 representing thresholds close to the 90th (-28 mm/day) and 99th (-53 mm/day) per1043 centile daily dSWE measured between March 19th to July 1st of 1980-2015 at WUS 

- 1044 SNOTEL stations (Figure S1 and Table 1). These snowmelt percentiles were close to 1045 rates also identified as average rates across shallow-to-deep snowpacks in Musselman 1046 et al (2017a). Notably, SNOTEL record observations are quality controlled; however, 1047 we identified a few dSWE values that were measured to exceed -250 mm/day. Figure 1048 S1 shows all SNOTEL dSWE observations between 1980-2015 relative to the amount 

- 1049 of SWE available to melt by taking the daily difference between the measurement of 1050 SWE on the day of (SWEn) minus the SWE depth on the day prior (SWEn−1). These 1051 dSWE estimates indicate that, at least, -250 mm of snowmelt occurred on several 1052 days, which, in some instances, would have resulted in a halving or complete meltout 1053 of the snowpack in a single day (i.e., values of 0.5 to 1.0 in Figure S1). A back-of1054 the-envelope calculation shows that the energy needed to melt that much snow in a 1055 single day is highly unlikely, as it would require 966 W/m<sup>2</sup> of energy input consis1056 tently over the entire day (i.e., 966 W/m<sup>2</sup> = 250 kg/m<sup>2</sup> * 334,000 J/kg * 1 day / 1057 [24 hours * 3,600 s]). Therefore, we argue, the use of the 99th percentile SNOTEL 1058 observed dSWE, rather than the true dSWE minima, is likely a better benchmark of 1059 extreme 20Cv3-SNOW-17 melt potential model performance. 

- 1060 To combine metrics and systematically compare their performance across multiple 1061 years, we compute the average performance of each model for each year and then 1062 average those values across years (1980-2015) for each performance metric (CRPS and 1063 owCRPS). The metrics are computed for all days between March 19th to July 1st and 1064 snow-eater heatwave-only days. Metric performance for a given model is then rank- 

- 1065 ordered across the number of potential models, first for all days and then snow-eater 1066 heatwave-only days. The rankings of each model across metrics are then averaged 

51 

- 1067 (including all days and snow-eater heatwave days) to determine the overall model that 

- 1068 best estimates melt potential. 

- 1069 As shown in Table S1, the model that generally performed the best across these 

- 1070 metrics was the HH model (k=10), with an average ranking of 3.17, followed by the 

- 1071 AHH model (k=1), average ranking of 4.33, and, finally, the NHH model (or “out 

- 1072 of the box” SNOW-17), with an average ranking of 4.50. Therefore, these three top- 

- 1073 performing 20Cv3-SNOW-17 models are used to estimate snow-eater heatwave melt 

- 1074 potentials across the entirety of the 20Cv3 reanalysis record (1850-2015). 

52 



Fig. S1 1980-2015 WUS SNOTEL measurements of the daily change in snow water equivalent (dSWE; mm/day) versus SWE depths (mm) the day before the dSWE occurred between March 19th to July 1st. The colormap indicates the frequency of daily SWE measurements across SNOTEL sites. The lines represent the lowest (0.0) to highest (1.0) possible fractional change in dSWE. 

53 



Fig. S2 Phase diagrams comparing CRPS and owCRPS between SNOTEL stations and the 20Cv3SNOW-17 melt potential models between 1980-2015 on all days between March 19th to July 1st or only on snow-eater heatwave days. Models represented include the effects of no heatwave hours (NHH) (or “out of the box” SNOW-17), heatwave hours (HH), accumulative heatwave hours (AHH), and sustained accumulative heatwave hours (SAHH). Colors distinguish models. Symbols distinguish the magnitude of the heatwave hours effect. Ovals represent a one standard deviation excursion from the mean model performance in CRPS and owCRPS. 

54 

Table S1 Continuous Ranked Probability Score (CRPS) and outcome-weighted CRPS (owCRCPs) mean values (mm) and rankings (unitless) for snowmelt potential estimates compared to daily change in SWE (dSWE) measurements across all SNOTEL stations and years (1980-2015). The snowmelt potential models include the “out of the box” SNOW-17 model, or no heatwave hours (NHH) effects, and the three experimental SNOW-17 models, heatwave hours (HH), accumulative heatwave hours (AHH), and sustained accumulative heatwave hours (SAHH) effects. The three top-ranking models are emboldened. 

|Metric<br>(1980-2015)|NHH|HH<br>k=1|HH<br>k=5|HH<br>k=10|SAHH<br>k=1|SAHH<br>k=5|SAHH<br>k=10|AHH<br>k=1|AHH<br>k=5|AHH<br>k=10|
|---|---|---|---|---|---|---|---|---|---|---|
|CRPS<br>all days|9.51|9.59|9.87|10.1|19.2|26.8|30.4|10.1|10.6|10.9|
|owCRPS (25mm)<br>all days|10.9|10.9|11.2|11.6|12.4|21.3|26.0|11.9|13.2|13.8|
|owCRPS (50mm)|||||||||||
|all days|14.7|14.2|12.6|10.7|9.32|10.9|13.3|10.8|12.0|13.4|
|CRPS<br>heatwave days|11.8|13.5|17.9|20.9|25.0|35.8|40.9|21.0|28.8|32.5|
|owCRPS (25mm)<br>heatwave days|9.33|8.37|9.17|11.7|14.9|24.1|28.7|13.0|19.4|22.8|
|owCRPS (50mm)<br>heatwave days|16.4|14.9|12.9|10.4|10.5|12.9|15.1|11.2|12.2|14.1|
|CRPS rank<br>all days|1.00|2.00|3.00|4.00|8.00|9.00|10.0|5.00|6.00|7.00|
|owCRPS (25mm)<br>rank all days|2.00|1.00|3.00|4.00|6.00|9.00|10.0|5.00|7.00|8.00|
|owCRPS (50mm)<br>rank all days|10.0|9.00|6.00|2.00|1.00|4.00|7.00|3.00|5.00|8.00|
|CRPS rank<br>all days|1.00|2.00|3.00|4.00|6.00|9.00|10.0|5.00|7.00|8.00|
|owCRPS (25mm)<br>rank heatwave days|3.00|1.00|2.00|4.00|6.00|9.00|10.0|5.00|7.00|8.00|
|owCRPS (50mm)<br>rank heatwave days|10.0|8.00|6.00|1.00|2.00|5.00|9.00|3.00|4.00|7.00|
|Average<br>rank|4.50|3.83|3.83|3.17|4.83|7.50|9.33|4.33|6.00|7.67|



Table S2 The top 25 seasons (March 19th to July 1st) of maximum five day melt potential (Mx5day) within the SNOTEL period of record that overlaps with 20Cv3 (1980-2015). Each column represents Mx5day computed from the three different 20Cv3-SNOW-17 models, which include the effects of no heatwave hours (NHH), heatwave hours (HH), and accumulated heatwave hours (AHH). The average volumetric melt potential over the mountainous WUS in km<sup>3</sup> is provided in parentheses. The 1983 season is emboldened. 

|Ranking|NHH (km<sup>3</sup>)|HH (km<sup>3</sup>)|AHH (km<sup>3</sup>)|
|---|---|---|---|
|1|2014 (84.2)|2014 (115)|2014 (122)|
|2|2015 (76.7)<br>|2015 (104)<br>|1986 (117)<br>|
|3|1992 (72.9)|1986 (104)|2015 (109)|
|4|1986 (72.2)<br>|1992 (100)<br>|1992 (103)<br>|
|5|2013 (58.7)|2013 (82.8)|2013 (88.4)|
|6|2004 (57.1)|2007 (82.3)|1987 (87.4)|
|7|2007 (56.3)|2004 (80.9)|2007 (82.9)|
|8|1987 (49.5)|1987 (75.6)|2004 (81.7)|
|9|2006 (41.9)<br>|1997 (65.6)<br>|1997 (69.9)<br>|
|10|1997 (41.8)|2006 (63.3)|2006 (65.8)|
|11|1989 (40.2)|1989 (62.8)|1988 (59.3)|
|12|1988 (37.5)|1988 (53.1)|2012 (56.7)|
|13|1983 (33.5)|2012 (51.9)|1989 (56.6)|
|14|2012 (31.3)<br>|1994 (51.4)<br>|1998 (55.5)<br>|
|15|1994 (30.7)|1983 (49.1)|1994 (54.9)|
|16|2008 (30.1)|1998 (45.3)|1983 (50.1)|
|17|1996 (30.0)|2008 (45.0)|1980 (48.5)|
|18|1998 (28.1)|1996 (43.9)|2008 (44.3)|
|19|2003 (27.6)|1980 (42.2)|1996 (42.6)|
|20|2001 (26.8)|1981 (40.1)|1985 (41.4)|
|21|1985 (25.7)|2001 (40.1)|1981 (40.0)|
|22|1981 (23.5)|2003 (39.1)|2003 (38.2)|
|23|1980 (22.5)|1985 (37.0)|2001 (37.9)|
|24|1982 (18.5)|1993 (27.7)|1993 (28.1)|
|25|1993 (18.0)|1982 (26.2)|1982 (25.7)|



56 

Table S3 The top 25 seasons (March 19th to July 1st) of total snow-eater heatwave melt potential within the SNOTEL period of record that overlaps with 20Cv3 (1980-2015). Each column represents estimates from the three different 20Cv3-SNOW-17 models, which include the effects of no heatwave hours (NHH), heatwave hours (HH), and accumulated heatwave hours (AHH). The average volumetric melt potential over the mountainous WUS in km<sup>3</sup> is provided in parentheses. The 1983 season is emboldened. 

|Ranking|NHH (km<sup>3</sup>)|HH (km<sup>3</sup>)<br>AHH|(km<sup>3</sup>)|
|---|---|---|---|
|1|2015 (152)|2015 (237)<br>2015|(246)|
|2|2013 (131)<br>|2013 (197)<br>2013 <br><br>|(204)<br>|
|3|1987 (95.8)|1987 (155)<br>1987|(169)|
|4|1986 (77.2)<br>|1986 (125)<br>1986 <br><br>|(133)<br>|
|5|2014 (74.4)|2014 (117)<br>2012|(119)|
|6|2012 (66.5)|2012 (114)<br>2014|(116)|
|7|1992 (59.5)|1992 (100)<br>1992|(103)|
|8|1989 (56.1)|1989 (92.8)<br>1989|(98.2)|
|9|2004 (50.7)<br>|2004 (87.4)<br>2004 <br><br>|(84.6)<br>|
|10|1994 (37.0)|1994 (63.4)<br>1994|(66.2)|
|11|1985 (35.6)|1985 (63.0)<br>1985|(65.2)|
|12|1997 (31.3)|1997 (48.4)<br>1997|(52.0)|
|13|2007 (27.3)|2007 (46.4)<br>2007|(45.7)|
|14|1996 (26.0)<br>|1996 (42.2)<br>1980 <br><br>|(40.9)<br>|
|15|1988 (25.7)|2001 (40.9)<br>1996|(40.4)|
|16|2001 (25.2)|1988 (40.1)<br>1988|(39.8)|
|17|2006 (23.7)|1980 (37.5)<br>2001|(39.5)|
|18|1980 (20.8)|2006 (35.9)<br>2006|(36.2)|
|19|2008 (16.0)|1981 (27.7)<br>1981|(27.1)|
|20|1981 (15.9)|1998 (23.8)<br>1998|(25.2)|
|21|1983 (15.4)|2008 (23.6)<br>1983|(22.9)|
|22|1998 (13.9)|1983 (22.5)<br>2008|(22.8)|
|23|2003 (10.1)|2003 (15.3)<br>2003|(14.5)|
|24|1993 (8.71)|1993 (14.0)<br>1993|(13.8)|
|25|1984 (7.58)|2000 (13.0)<br>2000|(12.1)|



57 

Table S4 The top 25 seasons (March 19th to July 1st) of mean total snow-eater heatwave-only melt potential contribution to the total seasonal melt potential within the SNOTEL period of record that overlaps with 20Cv3 (1980-2015). Each column represents estimates from the three different 20Cv3-SNOW-17 models, which include the effects of no heatwave hours (NHH), heatwave hours (HH), and accumulated heatwave hours (AHH). The mean percentage contribution over the mountainous WUS is provided in parentheses. The 1983 season is emboldened. 

|Ranking|NHH (%)|HH (%)|AHH (%)|
|---|---|---|---|
|1|2015 (23.4)|2015 (32.6)|2015 (33.3)|
|2|2013 (21.1)|2013 (29.5)|2013 (30.2)|
|3|1987 (17.6)|1987 (25.7)|1987 (27.1)|
|4|1986 (14.6)<br>|1986 (21.9)<br>|1986 (22.9)<br>|
|5|2012 (12.3)<br>|2012 (19.1)<br>|2012 (19.6)<br>|
|6|1992 (11.6)|1992 (18.3)|1992 (18.8)|
|7|2014 (10.6)|2014 (16.1)|2014 (15.7)|
|8|1989 (9.09)|2004 (15.1)|1989 (15.1)|
|9|2004 (8.81)<br>|1989 (14.7)<br>|2004 (14.6)<br>|
|10|1994 (7.39)|1985 (12.5)|1994 (12.9)|
|11|1997 (7.31)|1994 (12.5)|1985 (12.8)|
|12|1985 (7.25)|1997 (11.3)|1997 (11.9)|
|13|2007 (6.74)|2007 (11.1)|2007 (10.9)|
|14|2006 (6.52)<br>|2006 (9.88)<br>|1980 (10.3)<br>|
|15|1988 (6.26)<br>|1980 (9.58)<br>|2006 (9.97)<br>|
|16|2001 (5.53)|1988 (9.35)|1988 (9.23)|
|17|1980 (5.50)|2001 (9.17)|1998 (8.92)|
|18|1983 (5.47)|1996 (9.03)|2001 (8.81)|
|19|1996 (5.42)|1998 (8.54)|1996 (8.69)|
|20|2008 (5.11)<br>|1983 (8.04)<br>|1983 (8.17)<br>|
|21|1998 (5.06)|2008 (7.67)|2008 (7.38)|
|22|1993 (3.82)|1981 (6.63)|1981 (6.47)|
|23|1981 (3.71)|1993 (6.16)|1993 (6.13)|
|24|2003 (3.33)|2003 (5.15)|2003 (4.91)|
|25|1982 (2.24)|1984 (3.40)|1982 (3.21)|



58 



Fig. S3 A catalog of 20Cv3-SNOW-17 defined snow-eater heatwave events between 1850-2015 using the SNOW-17 melt potential model with no heatwave hour (NHH) effects. Each line represents a unique snow-eater heatwave event identified anywhere within the WUS mountainous regions. Each line length represents the snow-eater heatwave event duration, and the line colors represent the mean total snow-eater heatwave intensity over its duration. Overlaid dots represent the 11 springseason, snowmelt-induced superflood events identified by Tarouilly et al (2021). If an 20Cv3-SNOW17 identified snow-eater heatwave event falls within 5 days of the Tarouilly et al (2021)-identified superflood events, a black dot is provided, else a hollow circle. The 50-year annual average snow-eater heatwave event frequency and durations are provided on the right y-axis. 

59 



Fig. S4 Time series comparisons of 20Cv3-SNOW-17 (colored) snowmelt potential with SNOTEL (black) daily change in snow water equivalent (dSWE) for March 19 to July 1st, 1984. a) is the “out of the box” version of SNOW-17, or the no heatwave hours (NHH) effect, melt potential model. b) and c) are the experimental heatwave hours (HH) and accumulative heatwave hours (AHH) effect SNOW17 melt potential models, respectively. The bold lines are 50 ensemble member mean estimates, and the thin lines are the deciles across all sites/nearest grid cells. The gray shaded region represents the timing and duration of the snow-eater heatwave event. The map plots show the SNOTEL sites (black dots) used for the comparison (those that fall within the snow-eater heatwave blob) and the heatwave day accumulative snowmelt potential estimates by the 20Cv3-SNOW-17 models between March 19th and July 1st. 

60 



Fig. S5 Time series comparisons of 20Cv3-SNOW-17 (colored) snowmelt potential with SNOTEL (black) daily change in snow water equivalent (dSWE) for March 19 to July 1st, 1997. a) is the “out of the box” version of SNOW-17, or the no heatwave hours (NHH) effect, melt potential model. b) and c) are the experimental heatwave hours (HH) and accumulative heatwave hours (AHH) effect SNOW17 melt potential models, respectively. The bold lines are 50 ensemble member mean estimates, and the thin lines are the deciles across all sites/nearest grid cells. The gray shaded region represents the timing and duration of the snow-eater heatwave event. The map plots show the SNOTEL sites (black dots) used for the comparison (those that fall within the snow-eater heatwave blob) and the heatwave day accumulative snowmelt potential estimates by the 20Cv3-SNOW-17 models between March 19th and July 1st. 

61 



Fig. S6 Seasonal (March 19th - July 1st) anomalies in 20Cv3 derived a) two-meter surface air temperature (T2m) and b) freezing area from 1850-2015 over WUS mountainous regions relative to a 1850-1899 climatology. The Mann-Kendall trend p-values and Theil-Sen slope values are provided at the top right of each subplot. 

62 

Table S5 The top 25 seasons (March 19th to July 1st) of total snow-eater heatwave melt potential over 1850-2015. Each column represents estimates from the three different 20Cv3SNOW-17 models, which include the effects of no heatwave hours (NHH), heatwave hours (HH), and accumulated heatwave hours (AHH). The average volumetric melt potential over the mountainous WUS in km<sup>3</sup> is provided in parentheses. 

|Ranking|NHH (km<sup>3</sup>)|HH (km<sup>3</sup>)<br>AHH|(km<sup>3</sup>)|
|---|---|---|---|
|1|1869 (196)|1869 (280)<br>1869|(341)|
|2|2015 (152)<br>|1857 (251)<br>1857 <br><br>|(279)<br>|
|3|1857 (149)|2015 (237)<br>2015|(246)|
|4|1859 (148)<br>|1859 (207)<br>1859 <br><br>|(242)<br>|
|5|1961 (146)|1961 (204)<br>1961|(227)|
|6|2013 (131)|2013 (197)<br>1886|(210)|
|7|1886 (129)|1886 (190)<br>2013|(204)|
|8|1918 (123)|1969 (184)<br>1918|(202)|
|9|1969 (120)<br>|1897 (181)<br>1897 <br><br>|(195)<br>|
|10|1958 (116)|1918 (175)<br>1969|(192)|
|11|1897 (115)|1958 (171)<br>1958|(191)|
|12|1926 (110)|1926 (171)<br>1926|(176)|
|13|1896 (99.4)|1934 (160)<br>1987|(169)|
|14|1987 (95.8)<br>|1987 (155)<br>1934 <br><br>|(167)<br>|
|15|1934 (94.5)|1881 (144)<br>1881|(154)|
|16|1970 (91.5)|1896 (140)<br>1896|(149)|
|17|1922 (86.0)|1966 (139)<br>1966|(146)|
|18|1966 (85.2)|1970 (130)<br>1970|(140)|
|19|1881 (83.0)|1960 (125)<br>1853|(137)|
|20|1863 (80.8)|1986 (125)<br>1986|(133)|
|21|1853 (78.4)|1922 (123)<br>1863|(131)|
|22|1960 (78.0)|1863 (119)<br>1922|(126)|
|23|1986 (77.2)|1853 (117)<br>1960|(126)|
|24|1959 (76.7)|2014 (117)<br>1959|(123)|
|25|2014 (74.4)|1959 (116)<br>2012|(119)|



63 

Table S6 The top 25 seasons (March 19th to July 1st) of mean total snow-eater heatwave-only melt potential contribution to the total seasonal melt potential over 1850-2015. Each column represents estimates from the three different 20Cv3-SNOW-17 models, which include the effects of no heatwave hours (NHH), heatwave hours (HH), and accumulated heatwave hours (AHH). The mean percentage contribution over the mountainous WUS is provided in parentheses. 

|Ranking|NHH (%)|HH (%)|AHH (%)|
|---|---|---|---|
|1|1869 (35.2)|1869 (41.8)|1869 (44.7)|
|2|1859 (29.3)|1859 (36.4)|1859 (39.4)|
|3|1961 (26.9)<br>|1961 (34.1)<br>|1961 (36.2)<br>|
|4|1918 (24.7)|2015 (32.6)|1918 (34.6)|
|5|2015 (23.4)|1918 (31.9)|2015 (33.3)|
|6|1886 (23.2)|1857 (30.8)|1857 (33.0)|
|7|1970 (22.8)|1969 (30.7)|1886 (31.8)|
|8|1969 (22.4)|1886 (30.3)|1969 (31.4)|
|9|1958 (21.9)|2013 (29.5)|1958 (31.3)|
|10|1897 (21.4)|1970 (29.4)|1970 (30.6)|
|11|2013 (21.1)|1958 (29.2)|2013 (30.2)|
|12|1857 (20.7)|1897 (29.0)|1897 (29.9)|
|13|1863 (19.0)|1926 (26.7)|1926 (27.2)|
|14|1853 (19.0)|1987 (25.7)|1987 (27.1)|
|15|1926 (18.8)|1863 (25.0)|1863 (26.1)|
|16|1896 (18.4)|1896 (24.6)|1853 (25.5)|
|17|1922 (17.9)|1853 (24.0)|1896 (25.4)|
|18|1987 (17.6)|1922 (23.9)|1922 (24.3)|
|19|1850 (16.1)|1934 (23.5)|1934 (24.3)|
|20|1966 (15.3)|1966 (23.0)|1966 (23.9)|
|21|1919 (15.2)|1986 (21.9)|1986 (22.9)|
|22|1959 (15.0)|1959 (20.9)|1850 (21.9)|
|23|1934 (15.0)|1850 (20.6)|1959 (21.8)|
|24|1986 (14.6)|1949 (20.6)|1949 (21.5)|
|25|1936 (14.1)|1881 (20.5)|1881 (21.4)|



64 

Table S7 The top 25 seasons (March 19th to July 1st) of maximum five day melt potential (Mx5day) over 1850-2015. Each column represents Mx5day computed from the three different 20Cv3-SNOW-17 models, which include the effects of no heatwave hours (NHH), heatwave hours (HH), and accumulated heatwave hours (AHH). The average volumetric melt potential over the mountainous WUS in km<sup>3</sup> is provided in parentheses. 

|Ranking|NHH (km<sup>3</sup>)|HH (km<sup>3</sup>)|AHH (km<sup>3</sup>)|
|---|---|---|---|
|1<br>|2014 (84.2)<br>|2014 (115)<br>|2014 (122)<br>|
|2<br>|2015 (76.7)<br>|1969 (105)<br>|1869 (118)<br>|
|3|1969 (74.3)<br>|2015 (104)<br>|1986 (117)<br>|
|4|1961 (73.2)|1986 (104)|1961 (116)|
|5|1992 (72.9)<br>|1992 (100)<br>|1859 (112)<br>|
|6|1986 (72.2)|1961 (98.9)|1958 (111)|
|7|1958 (72.2)<br>|1857 (98.5)<br>|1918 (111)<br>|
|8|1857 (69.4)|1958 (98.5)|2015 (109)|
|9|1918 (68.7)|1918 (95.5)|1969 (109)|
|10|1859 (67.0)<br>|1869 (90.7)<br>|1992 (103)<br>|
|11|1869 (64.5)<br>|1859 (90.6)<br>|1857 (102)<br>|
|12|1970 (62.6)|1970 (87.4)|1949 (95.3)|
|13|1925 (62.2)|1925 (84.8)|1970 (93.5)|
|14|1896 (58.8)|2013 (82.8)|1896 (92.1)|
|15|2013 (58.7)<br>|2007 (82.3)<br>|1959 (91.6)<br>|
|16|1922 (58.3)<br>|1949 (82.1)<br>|2013 (88.4)<br>|
|17|1959 (58.3)|1959 (81.6)|1987 (87.4)|
|18|2004 (57.1)|1922 (81.6)|1922 (86.2)|
|19|1926 (56.5)|1896 (81.2)|1925 (86.0)|
|20|2007 (56.3)<br>|2004 (80.9)<br>|1928 (85.1)<br>|
|21|1967 (56.0)|1926 (80.7)|1957 (84.7)|
|22|1960 (55.3)|1967 (78.9)|1956 (83.9)|
|23|1863 (55.1)|1863 (78.4)|1926 (83.3)|
|24|1957 (53.5)|1957 (76.1)|2007 (82.9)|
|25|1886 (52.8)|1987 (75.6)|1863 (82.7)|



65 


