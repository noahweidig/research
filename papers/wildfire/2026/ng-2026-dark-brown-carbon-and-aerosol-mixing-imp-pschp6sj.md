---
title: Dark brown carbon and aerosol mixing impacts on absorbing aerosol optical depth in the southeastern United States
authors:
- Ng, Alexandra E.
- Shrivastava, Manish
- Gaudet, Brian
- He, Cenlin
- Cheng, Zezhen
- Vizuete, William
year: '2026'
journal: null
doi: 10.5194/egusphere-2026-5534
tags:
- eastern united states
- southeastern united states
- united states
- wildfire
zotero_key: PSCHP6SJ
item_type: journalArticle
url: https://openalex.org/W7220863302
source_url: 'unpaywall: https://egusphere.copernicus.org/preprints/2026/egusphere-2026-5534/egusphere-2026-5534.pdf'
fulltext_status: fulltext
synced: '2026-11-09'
---

# Dark brown carbon and aerosol mixing impacts on absorbing aerosol optical depth in the southeastern United States

## Abstract

Abstract. Wildfires are becoming more prevalent in the southeastern United States. Wildfires emit light absorbing organic aerosols such as black carbon and dark brown carbon (tar balls) that influence regional air quality and radiative forcing. Recent experimental work has identified dark brown carbon as a potentially significant source of warming in the atmosphere. However, dark brown carbon is not typically included in air quality and climate models. We added dark brown carbon from wildfires as a species in the Weather Research and Forecasting modeling system coupled with chemistry (WRF-Chem) version 4.2 with the Quick-Fire Emissions Database (QFED). The model simulations were run over the southeastern United States from June 21st to June 30th 2013 in conjunction with in-situ measurements of aerosol extinction from the Southeast Nexus (SENEX) aircraft campaign and aerosol optical depth (AOD) measurements from the ground-based remote sensing Aerosol Robotic Network (AERONET). The impacts of imaginary refractive index, aerosol mixing, and Mie method were investigated with an offline radiation model for computationally efficient evaluation. Dark brown carbon was found to increase absorbing aerosol optical depth (AAOD) by up to 5.2 % in the simulation time and region. We derived a linear equation to estimate the correlation between modeled AAOD and columnar dark brown carbon (AAOD = 0.0023[D-BrC] + 0.0007) with core-shell considerations. Core-shell aerosol mixing and explicit Mie computation enhanced increases in AAOD from dark brown carbon at AERONET sites (up to 6.42 %). These results indicate that models omitting dark brown carbon may underestimate aerosol absorption in wildfire-influenced regions, and that including it, along with a realistic mixing state and Mie treatment, is important for estimating radiative forcing as wildfire activity increases.

## Full text

https://doi.org/10.5194/egusphere-2026-5534 Preprint. Discussion started: 7 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





# **Dark brown carbon and aerosol mixing impacts on absorbing aerosol optical depth in the southeastern United States** 

**Alexandra E. Ng**<sup>**1**</sup> **, Manish Shrivastava**<sup>**2***</sup> **, Brian Gaudet**<sup>**2**</sup> **, Cenlin He**<sup>**3**</sup> **, Zezhen Cheng**<sup>**2**</sup> **, William Vizuete**<sup>**1***</sup> 

- 5 1Department of Environmental Sciences and Engineering, Gillings School of Global Public Health, University of North Carolina at Chapel Hill, Chapel Hill, North Carolina 27514, United States 

   - 2Atmospheric, Climate, and Earth Sciences Division, Pacific Northwest National Laboratory, Richland, Washington 99354, United States 

3NSF National Center for Atmospheric Research, Research Applications Laboratory, Boulder, Colorado 

- 10 Correspondence to: William Vizuete (vizuete@unc.edu) 

**Abstract.** Wildfires are becoming more prevalent in the southeastern United States. Wildfires emit light absorbing organic aerosols such as black carbon and dark brown carbon (tar balls) that influence regional air quality and radiative forcing. Recent experimental work has identified dark brown carbon as a potentially significant source of warming in the atmosphere. 

- 15 However, dark brown carbon is not typically included in air quality and climate models. We added dark brown carbon from wildfires as a species in the Weather Research and Forecasting modeling system coupled with chemistry (WRF-Chem) version 4.2 with the Quick-Fire Emissions Database (QFED). The model simulations were run over the southeastern United States from June 21<sup>st</sup> to June 30<sup>th</sup> 2013 in conjunction with in-situ measurements of aerosol extinction from the Southeast Nexus (SENEX) aircraft campaign and aerosol optical depth (AOD) measurements from the ground-based remote sensing Aerosol 

- 20 Robotic Network (AERONET). The impacts of imaginary refractive index, aerosol mixing, and Mie method were investigated with an offline radiation model for computationally efficient evaluation. Dark brown carbon was found to increase absorbing aerosol optical depth (AAOD) by up to 5.2% in the simulation time and region. We derived a linear equation to estimate the correlation between modeled AAOD and columnar dark brown carbon (AAOD = 0.0023[D-BrC] + 0.0007) with core-shell considerations. Core-shell aerosol mixing and explicit Mie computation enhanced increases in AAOD from dark brown carbon 

- 25 at AERONET sites (up to 6.42%). These results indicate that models omitting dark brown carbon may underestimate aerosol absorption in wildfire-influenced regions, and that including it, along with a realistic mixing state and Mie treatment, is important for estimating radiative forcing as wildfire activity increases. 

### **1 Introduction** 

- 30 Carbonaceous aerosols emitted by wildfires play an important role in global and regional climate systems, directly through absorption (warming) or scattering (cooling) of solar radiation, and indirectly by acting as surfaces for clouds to form (Chylek 

1 

https://doi.org/10.5194/egusphere-2026-5534 Preprint. Discussion started: 7 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





and Wong, 1995; Dennison et al., 2014; Intergovernmental Panel on Climate Change (IPCC), 2023a; Jacobson, 2014). Many organic aerosols scatter light and cool the Earth’s surface below; however, black and brown carbon are absorbing carbonaceous aerosols contributing to global positive radiative forcing (Ackerman and Toon, 1981; Chapman et al., 2009; Chou and Suarez, 

- 35 1994; Chylek and Wong, 1995; Feng et al., 2013; Chou and Suarez, 1999). 

   - Wildfires emit a diverse mixture of carbonaceous aerosols including black carbon (BC) and brown carbon (BrC) 

   - (Abatzoglou and Williams, 2016; Dennison et al., 2014; Ichoku et al., 2008; McClure et al., 2020; Wooster et al., 2005). Black carbon absorbs solar radiation across a wide spectral range (ultraviolet to infrared) and has a well-constrained, wavelength independent imaginary refractive index ( _k_ ), which represents the absorbance of a particle (Bond and Bergstrom, 2006). BrC is 

- 40 classified as the non-BC absorbing fraction of organic aerosols. The water-soluble organic carbon (WSOC) fraction of BrC absorbs light from the visible to near-ultraviolet (300-400 nm) spectral range (Laskin et al., 2015). WSOC BrC can be measured by collecting particles on Teflon filters followed by water and methanol extraction, with insoluble compounds filtered out with in-line syringe filters (Zeng et al., 2020). Dark brown carbon (d-BrC), also known as tar balls or chromophores, is a subtype of brown carbon that is made up of water-insoluble organic carbon (WIOC), absorbs over a wide spectral range (visible and 

- 45 near-infrared), and is resistant to daytime photobleaching with atmospheric lifetimes up to 41 days (Alang and Aggarwal, 2024; R. K. Chakrabarty et al., 2010; Rajan K. Chakrabarty et al., 2023; Chelluboyina et al., 2024; Fleming et al., 2020; Laskin et al., 2015; Shrivastava, 2025; Xuan Wang et al., 2025). Dark brown carbon has been measured with aerosol collection through particle inlets followed by scanning electron microscopy (SEM) (R. K. Chakrabarty et al., 2010). 

- Dark brown carbon can contribute a direct radiative effect of +0.208 Watts m<sup>-2</sup> , which is comparable to BC direct radiative 

- 50 effect (DRE) (Xuan Wang et al., 2025). Global modeling with BrC found that direct radiative forcing (DRF) of BC may be overestimated due to previous lack of BrC DRF attributions (X. Wang et al., 2014). Adler et al., 2019 measured intermediate absorbers that could not be classified as black or brown carbon, but could potentially be dark brown carbon tar balls (Adler et al., 2019). The global annual direct radiative effect from BrC absorption was estimated to be +0.03 and -0.08 Watts m<sup>-2</sup> at the surface (Hammer et al., 2016). A study in the Mediterranean basin considered bleaching effect and estimated a DRE of 0.04 

- 55 W m<sup>-2</sup> (Methymaki et al., 2023). Brown carbon in Chiang Mai, Thailand was estimated to contribute between 33% to 40% of carbonaceous aerosol absorption at 440 nm wavelengths (Ying Zhang et al., 2021). Aerosol-snow radiative transfer studies found that d-BrC increased annual mean snow radiative forcing by 0.6 to 17.9 W m<sup>-2</sup> (Chelluboyina et al., 2024). Washenfelder et al., 2015 found that organic brown carbon aerosols contributed to approximately 9 ± 9% of organic aerosol absorption at 365 nm (Washenfelder et al., 2015). Experimental measurements of smoke particles from smoldering biomass combustion 

- 60 analyzed with SEM found that over 95% of particles were dark brown carbon tar balls (R. K. Chakrabarty et al., 2010). Chemical transport models, such as the Weather Research and Forecasting modeling system coupled with Chemistry 

- (WRF-Chem) and the Community Multiscale Air Quality modeling system (CMAQ), typically assume aerosols are externally or homogeneously mixed (Binkowski and Roselle, 2003; Chapman et al., 2009). Aerosol optical properties are calculated based on volume-averaging at each wavelength band. In reality, aerosols can be internally mixed and exist in a variety of 

- 65 morphologies. Core-shell morphologies can have a strong influence on aerosol chemistry (Anttila et al., 2006; Chen et al., 

2 

https://doi.org/10.5194/egusphere-2026-5534 Preprint. Discussion started: 7 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





2024; Farrell et al., 2026; Ng et al., 2025; J. Zhang et al., 2023; Yue Zhang et al., 2018) and aerosol optical properties (Ackerman and Toon, 1981; Bond and Bergstrom, 2006; Cheng et al., 2024; Toon and Ackerman, 1981). 

The morphology of black and dark brown carbon can vary (externally mixed spherical particles, core shell spherical particles, or aggregates of spherules). Spherical particle morphology was found to more accurately estimate direct radiative 

- 70 effect in comparison to aggregate morphology (Saleh et al., 2016). Coatings on black and dark brown carbon can enhance absorption by up to 1.7 times, known as lensing enhancement (Lack et al., 2012). Recent experiments found evidence of absorption enhancement from organic and water coatings on dark brown carbon tar balls (Cheng et al., 2024). Field measurement-based modeling of brown carbon cores with coatings found that one-third of absorption in Shanghai was attributed to brown carbon (Mao et al., 2026). 

- 75 Dark brown carbon, however, is not typically accounted for in regional-scale models, such as WRF-Chem. Measurements found that dark brown carbon contributed up to 75% of shortwave visible light absorption and half of longwave visible light absorption in western United States smoke plumes (Rajan K. Chakrabarty et al., 2023). The fate and transport of dark brown carbon in the southeast U.S. as well as its effects on radiative forcing are uncertain (Devi et al., 2016; Intergovernmental Panel on Climate Change (IPCC), 2023b). A laboratory experiment tested combustion of fuels representative of the southeastern 

- 80 United States and identified about half of BrC to be potential chromophores (Glenn et al., 2024). Although aerosol optical extinction in the southeastern United States in summer 2013 was dominated by scattering, biomass burning was found to be the dominant source of absorbance in the region (Washenfelder et al., 2015). Additionally, a significant amount of groundbased, aircraft, and remote sensing data available provides opportunity to conduct robust analysis of tar ball radiative effects in a previously uninvestigated region. 

- 85 We added dark brown carbon into WRF-Chem to assess the regional radiative effects in the southeast United States. We simulated the southeast U.S region from June 21st to June 30th, 2013 and evaluated WRF-Chem simulated chemical species and radiative forcing with in-situ aircraft measurements of aerosol extinction and remote sensing measurements of aerosol optical depth (AOD). Offline radiation sensitivity simulations were conducted on the dark brown imaginary refractive index, aerosol mixing method, and explicit Mie computation impacts on absorbing aerosol optical depth (AAOD). 

### 90 **2 Methods** 

### **2.1 WRF-Chem model configuration** 

We ran WRF-Chem version 4.2 from June 21st to June 30th 2013 with an hourly output of chemical species concentrations, transport, and feedbacks with weather. Physical processes such as wet and dry removal were applied to all species. Weather was reinitialized every three simulation days. This model was run with a 12-kilometer grid spacing, 45 vertical layers, and a 

- 95 Lambert conformal map projection. Boundary conditions were obtained from the European Centre for Medium-Range Weather Forecasts (ECMWF) Reanalysis version 5 (ERA5) with analysis nudging for weather and the Community Atmosphere Model with Chemistry (CAM-Chem) (Hersbach et al., 2020). The Model for Simulating Aerosol Interactions and Chemistry 

3 

https://doi.org/10.5194/egusphere-2026-5534 Preprint. Discussion started: 7 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





(MOSAIC) with 4 aerosol size bins was used for the aerosol treatment (Zaveri et al., 2008). MOSAIC is an aerosol model that couples chemical and microphysical processes and accounts for thermodynamic partitioning. The Statewide Air Pollution 

- 100 Research Center 1999 (SAPRC-99) chemical mechanism was used for gas-phase species (Chen et al., 2015). We used the Rapid Radiative Transfer Model for General Circulation Model Applications (RRTMG) for the longwave and shortwave radiation schemes (Iacono et al., 2008; Mlawer et al., 1997). The Morrison double-moment scheme was used for microphysics (Morrison et al., 2009). The RRTMG shortwave scheme calculates extinction based on water vapor, Rayleigh scattering, gases (carbon dioxide, ozone, oxygen, methane and nitrogen), aerosols, and clouds. RRTMG shortwave radiation flux is quantified 

- 105 for 14 spectral bands at 0.2 to 12.2 µm. The Yonsei University (YSU) scheme was used for the planetary boundary layer scheme (Hong et al., 2009). 

We used the 2014 National Emissions Inventory for anthropogenic emissions and the Model of Emissions of Gases and Aerosols from Nature (MEGAN) version 2.1 for biogenic emissions (A. Guenther et al., 2006; A. B. Guenther et al., 2012). The MEGAN model uses plant functional types to model biogenic emissions. High resolution spatial and temporal data for 

- 110 fire emissions of biomass burning species including organic carbon (OC), black carbon (BC), sulfur dioxide (SO2), fine particulate matter (PM2.5), ammonia (NH3), nitrogen oxide (NO), carbon dioxide (CO2), carbon monoxide (CO), ethane, propylene, methyl ethyl ketone, propane, n-butane, i-butane, acetone, methane, formaldehyde, and acetaldehyde were generated with the Quick Fire Emissions Dataset (QFED) (Darmenov and Silva, 2015). QFED emissions are quantified with a top-down fire radiative power method. Utilizing fire radiative power improves estimates of biomass burning emissions in 

- 115 comparison to using emission factors (Wooster et al., 2005). 

4 

https://doi.org/10.5194/egusphere-2026-5534 Preprint. Discussion started: 7 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 









**Figure 1.** Locations of aircraft flights and AERONET remote-sensing measurement site. The corresponding AERONET site labels can be found in Table S1. 

### **2.2 Aircraft measurements** 

- 120 The Southeast Nexus (SENEX) campaign conducted flights on June 22nd, 23rd, 25th, 26th, and 29th and collected aerosol, gas, and radiation measurement data aboard the National Oceanic and Atmospheric Administration (NOAA) WP-3D aircraft (Warneke et al., 2016). Dry, humidified, and thermodenuder aerosol extinction were quantified with an aerosol cavity ringdown spectrometer (Langridge et al., 2011). Aircraft CRDS measures in situ observations of aerosol extinction. Uncertainty was ±2% for dry measurements (Strawa et al., 2006). Dry aerosol extinction was measured at RH < 30%, 273.15 

- 125 K and 101,300 Pa. Aerosol concentrations for organics, sulfate, nitrate, and ammonium were measured with an aerosol mass spectrometer (AMS) with uncertainty of ±30% (Warneke et al., 2016). 

5 

https://doi.org/10.5194/egusphere-2026-5534 Preprint. Discussion started: 7 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





### **2.3 Ground-based remote sensing data** 

Aerosol optical depth (AOD) is the amount of light scattered or absorbed by aerosols in a vertical column. AOD measurements were obtained from the Aerosol Robotic Network (AERONET) version 3, Level 2.0 which is cloud screened 130 and quality-assured with 0.01 and 0.02 uncertainty at visible and ultraviolet wavelengths, respectively (O. Dubovik et al., 2000; Oleg Dubovik et al., 2001; Holben et al., 2006). AERONET is a global ground-based system of automatic sun and sky scanning radiometers that derive AOD from direct solar radiation at wavelengths between 340 and 1040 nm (Holben et al., 1998). AERONET AOD is often used as ground truth validation for remote sensing and reanalysis AOD products (Byrne et al., 2024; Z. Zhang et al., 2024). AOD at 14 AERONET locations were used to analyze model simulations (Figure 1, Table 135 S1). 

### **2.4 Modeling dark brown carbon** 

We added primary solid-state dark brown carbon as a new species in WRF-Chem. Zhang et al., 2020 estimated 23% of d- BrC to OC, Jo et al., 2016 estimated 20% d-BrC to OC, and Park et al., 2010 estimated between 16% to 30% of d-BrC to OC (Jo et al., 2016; B. Zhang et al., 2024). In this work, primary dark brown carbon was assumed to be 20% of organic carbon 140 from biomass burning. In our online base model, d-BrC is considered non-reactive and has no chemical interactions with other species (Fleming et al., 2020). Complex refractive indices are composed of a real ( _n_ ) and imaginary ( _k_ ) refractive index. Dark brown carbon real refractive indices range from about 1.4 to 1.9 and imaginary refractive indices for dark brown carbon range from 0.01 to 0.4 (Alexander et al., 2008; R. K. Chakrabarty et al., 2010). We used a refractive index of 1.49 + 0.056i at 550 nm for dark brown carbon in our “online base” simulation (Cheng et al., 2024). For black carbon, we used a refractive index 145 of 1.95 + 0.79i at 550 nm (Bond and Bergstrom, 2006). 

### **2.5 Offline radiation simulation** 

We conducted sensitivity simulations of dark brown carbon aerosol optical properties using an offline WRF Chem radiation model that can run computationally intense radiation schemes efficiently (Barnard et al., 2010; Shrivastava et al., 2013). The offline radiation model uses online WRF-Chem chemical concentrations and aerosol optical property outputs as inputs and 150 calculates individual vertical layer AOD, single scattering albedo, and asymmetry with Mie theory (Ghan and Zaveri, 2007). We updated the offline model to include dark brown carbon and the 14 spectral bands from RRTMG. The sensitivity simulations for aerosol mixing state, Mie method, and imaginary refractive index are shown in Table 1. We used a real refractive index of 1.67 and imaginary refractive index of 0.27 at 550 nm wavelength, which is representative of the upper literature range for dark brown carbon (Alexander et al., 2008), for the high dark brown carbon absorption sensitivity. 

155 

6 

https://doi.org/10.5194/egusphere-2026-5534 Preprint. Discussion started: 7 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





**Table 1.** Offline radiation model sensitivity simulations for aerosol mixing, Mie method, and imaginary refractive index (kD-BrC) at 550 nanometer wavelength. 

|**Simulation Name**|**Aerosol Mixing**|**Mie Method**|**kD-BrC**|
|---|---|---|---|
|Base|Volume averaging|Simplified|0.00|
|D-BrC|Volume averaging|Simplified|0.27|
|Maxwell-Garnett|Maxwell-Garnett|Simplified|0.00|
|MG, D-BrC|Maxwell-Garnett|Simplified|0.27|
|Core-shell|Core-shell|Explicit|0.00|
|CS, D-BrC|Core-shell|Explicit|0.27|
|Explicit Mie|Volume averaging|Explicit|0.00|
|EM, D-BrC|Volume averaging|Explicit|0.27|



### 160 **2.6 Aerosol mixing** 

Aerosol mixing methodology impacts aerosol scattering, absorption, and single-scattering albedo. The online WRF-Chem default assumes volume-mixing for of all aerosol chemical species in a given size bin for computationally efficient calculations of aerosol optical properties. With volume-mixing, refractive indices are weighted by volume for each aerosol size bin. However, volume-mixing is not physically accurate (Bond and Bergstrom, 2006). Core-shell are computationally expensive 165 when run online. Therefore, the offline radiation model is advantageous for analyzing aerosol mixing state. The “MaxwellGarnett” mixing simulation randomly distributes black carbon in a particle (Markel, 2016). We updated the offline model to include dark brown carbon as another species for random distribution in a particle. Lesins et al., 2002 and Schuster et al., 2005 found that volume mixing calculates refractive indices 13 to 30% greater than with the Maxwell Garnett approximation. The “core-shell” simulation uses the core-shell mixing method which assumes a core of black and a shell with all other chemical 

- 170 species (Ackerman and Toon, 1981; Bond and Bergstrom, 2006). We updated the model to include dark brown carbon in the core. The “core-shell” simulation uses the full Mie code (explicit Mie method) at each time step and accounts for core-shell mixing. 

### **2.7 Mie optical property methodology** 

- Mie theory is used for predicting absorption and scattering for spherical particles. Under Mie theory computation, 

- 175 absorption and scattering are dependent on complex refractive indices, particle size, and incident light wavelength. The base simulation replicates online WRF-Chem and uses Chebyshev economization with the full Mie code called a single time for computational efficiency (Fast et al., 2006). The explicit Mie method, which is not typically used for online WRF-Chem, calls Mie code for each time step and uses Mie code from Ackermann and Toon, 1981 which allows for core-shell morphology Mie calculations (Ackerman and Toon, 1981). Aerosol optical properties (single scattering albedo, extinction, and asymmetry) are 

- 180 calculated with a two-component model from Ackerman & Toon 1981. 

7 

https://doi.org/10.5194/egusphere-2026-5534 Preprint. Discussion started: 7 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





### **2.8 Model evaluation and metrics** 

Aerosol extinction is the sum of both aerosol absorption and scattering. Single-scattering albedo (SSA) is aerosol scattering divided by extinction. SSA values close to 1 indicate that extinction is primarily from scattering while SSA less than about 0.85 indicate significant aerosol absorption (Haywood and Shine, 1995). Absorbing aerosol optical depth (AAOD) for the 

185 different offline sensitivity models were quantified with AOD and single scattering albedo (SSA) in the following equation: 

## 𝐴𝐴𝑂𝐷= 𝐴𝑂𝐷× (1 −𝑆𝑆𝐴) (1) 

AOD and AAOD (τ) were calculated at 550 nm wavelength (λ) with the Angstrom exponent (α) equation: 



<!-- Start of picture text -->
���<br>���<br>���<br>𝛼= − (2)<br>��� ��<br>��<br>��� ��<br>(3)<br>𝜏��� = 𝜏��� ���� �<br><!-- End of picture text -->

### 190 **3 Results and discussion** 

### **3.1 Model-simulated dark brown carbon and black carbon** 

Dark brown carbon from wildfires was added to QFED and WRF-Chem. The model-simulated spatial distribution of average dark brown carbon and black carbon in a column over the simulation time period are shown in Figure 2. 



> 195 **Figure 2.** Predicted average total column dark brown carbon (left) and black carbon (right) concentrations simulated by WRF-Chem between June 21st and June 30th 2013. 

8 

https://doi.org/10.5194/egusphere-2026-5534 Preprint. Discussion started: 7 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





From June 21st to June 25th, there was biomass burning in Arkansas, Tennessee, and Missouri and long-range transport of biomass burning emissions to the northeast. June 26th and 27th had biomass burning in Florida and Arkansas. On June 28th and 29th, there was biomass burning in Louisiana, Arkansas, Tennessee, and North Carolina. The average WRF-Chem 

- 200 modeled total columnar dark brown carbon during the time period was 1.64 µg m<sup>-3</sup> (standard deviation = 2.41). While the maximum dark brown carbon in a vertical column (68.7 µg m<sup>-3</sup> ) was greater than maximum columnar black carbon (30.7 µg m<sup>-3</sup> ), the average black carbon (2.09 µg m<sup>-3</sup> ) in the simulation time period was greater. 

### **3.2 Sensitivity analysis** 

The AAOD percent differences between the base simulation and the radiation sensitivity simulations for all grid cells and 

- 205 all hourly outputs during the simulation time period are shown in Table 2. 

**Table 2.** Maximum percent difference for absorbing aerosol optical depth (AAOD) between base WRF-Chem and sensitivity simulations. 

|**Simulation**<br>**Name**|**D-BrC**|**Maxwell-**<br>**Garnett**|**Maxwell-**<br>**Garnett, D-**<br>**BrC**|**Core-shell**|**Core-Shell,**<br>**D-BrC**|**Explicit**<br>**Mie**|**Explicit**<br>**Mie, D-BrC**|
|---|---|---|---|---|---|---|---|
|Maximum<br>AAOD %<br>increase|5.2%|0%|0%|29.7%|29.7%|30.2%|30.2%|
|Maximum<br>AAOD %<br>decrease|0%|-23.3%|-23.3%|-18.2%|-18.2%|-4.7%|-4.7%|



The “D-BrC” simulation increased AAOD by up to 5.2%. The “Maxwell-Garnett” and “Maxwell-Garnett, D-BrC” simulations decreased AAOD by up to 23.3%. The “Core-Shell” and “Core Shell, D-BrC” simulations increased AAOD by 

- 210 up to 29.7% and decreased AAOD by up to 18.2%. The “Explicit Mie” and “Explicit Mie, D-BrC” simulations increased AAOD by up 30.2% and decreased AAOD by up to 4.7%. The addition of D-BrC to the Maxwell-Garnett, core-shell, and explicit Mie simulations did not change the maximum AAOD percent increase or decrease. This is likely due to mixing method dominating at the locations where the maximum and minimums are located. 

### **3.3 AERONET** 

- 215 Table 3 shows the mean percent bias between AERONET measurements of AOD and the base and sensitivity simulation AOD at 550 nm wavelength. 

220 

9 

https://doi.org/10.5194/egusphere-2026-5534 Preprint. Discussion started: 7 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





**Table 3.** Percent bias between AERONET and model simulation aerosol optical depth at 550 nm wavelength. 

|**Simulatio**<br>**n Name**|**Base**|**D-BrC**|**Maxwell-**<br>**Garnett**|**Maxwell-**<br>**Garnett,**<br>**D-BrC**|**Core-shell**|**Core-**<br>**Shell, D-**<br>**BrC**|**Explicit**<br>**Mie**|**Explicit**<br>**Mie, D-**<br>**BrC**|
|---|---|---|---|---|---|---|---|---|
|All sites|-53.48%|-53.48%|-53.66%|-53.66%|-54.14%|-54.15%|-53.13%|-53.13%|
|App|-55.67%|-55.67%|-55.80%|-55.80%|-54.81%|-54.33%|-55.53%|-55.53%|
|Boyd|-48.45%|-48.45%|-48.63%|-48.63%|-42.51%|-42.23%|-48.27%|-48.27%|
|Cape|-68.72%|-68.72%|-68.82%|-68.82%|-68.86%|-71.28%|-68.63%|-68.63%|
|EPA|-53.54%|-53.54%|-53.69%|-53.69%|-53.15%|-53.15%|-53.33%|-53.33%|
|Geo|-46.19%|-46.19%|-46.43%|-46.43%|-47.89%|-47.80%|-45.86%|-45.86%|
|Imp|-65.24%|-65.24%|-65.38%|-65.38%|-62.79%|-62.62%|-65.04%|-65.04%|
|Lel|-41.05%|-41.05%|-41.24%|-41.24%|-37.08%|-41.79%|-41.37%|-41.37%|
|Mingo|-12.97%|-12.97%|-13.33%|-13.33%|-27.97%|-27.97%|-11.82%|-11.82%|
|SE-CTR|-52.64%|-52.64%|-52.82%|-52.82%|-50.78%|-50.66%|-52.33%|-52.33%|
|SE-OLF|-61.63%|-61.63%|-61.76%|-61.76%|-69.60%|-69.60%|-61.49%|-61.49%|
|SE-YOR|-30.64%|-30.64%|-30.97%|-30.97%|-32.78%|-39.87%|-30.01%|-30.01%|
|St Louis|-61.02%|-61.02%|-61.22%|-61.22%|-60.55%|-60.44%|-60.61%|-60.60%|
|UAH|-55.57%|-55.57%|-55.81%|-55.81%|-47.52%|-42.18%|-55.26%|-55.26%|
|UppBuf|-87.68%|-87.68%|-87.72%|-87.72%|-86.36%|-85.90%|-87.62%|-87.62%|



- The base simulation underpredicted AERONET AOD at all sites by 53.48% with an AOD mean bias of 0.128. The model 

- 225 performance varied by AERONET location. The base simulation had the lowest bias (-12.97%) at the Mingo AERONET site and the greatest bias at the Upper Buffalo AERONET site (-87.68%). The “D-BrC” sensitivity had the same average percent bias with AERONET AOD as the base simulation. The “Maxwell-Garnett” and “Maxwell-Garnett, D-BrC” sensitivity simulations slightly worsened AERONET AOD predictions by 0.18% on average for all sites in comparison to the base simulation, with the greatest change at Mingo (0.36%) and Yorkville (0.33%). The “Core-Shell” sensitivity on average for all 

- 230 sites worsened AERONET AOD predictions by 0.66% in comparison to the base simulation. However, the “Core-shell” simulation improved percent bias at App, Boyd, EPA, Imp, Lel, CTR, St. Louis, UAH, and Upper Buffalo by 0.86%, 5.94%, 0.39%, 2.62%, 1.86%, 0.47%, 9.05%, and 1.32%, respectively. The “Core Shell, D-BrC” sensitivity on average for all sites worsened percent bias by 0.67% in comparison to the base simulation. The “Core-shell, D-BrC” simulation improved percent bias at App, Boyd, EPA, Imp, Lel, CTR, St. Louis, UAH, and Upper Buffalo by 1.34%, 6.22%, 0.39%, 2.62%, 1.98%, 0.58%, 

- 235 13.39%, and 1.78%, respectively. The “Explicit Mie” and “Explicit Mie, D-BrC” sensitivity simulations slightly improved AERONET AOD predictions by 0.35% for all sites in comparison to the base simulation, with the greatest change at Mingo (1.15%) and Yorkville (0.63%). The “Explicit Mie” and “Explicit Mie, D-BrC” sensitivity simulations slightly worsened AERONET AOD predictions by at Leland (0.32%). 

The base model and all sensitivity simulations underpredicted AERONET AOD. Although QFED provides one of the most 

- 240 accurate predictions of biomass burning emissions, previous studies found that QFED still underestimates AOD and PM2.5 (Byrne et al., 2024; Wu et al., 2025) This could explain the underpredictions of AOD. Another reason for this underprediction could be the temporal resolution of AERONET. The AERONET AOD values used are daily averages while the model 

10 

https://doi.org/10.5194/egusphere-2026-5534 Preprint. Discussion started: 7 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





simulated AOD is predicted for every hour. Therefore, differences are expected. Additionally, AOD has diurnal variations. Although the diurnal effects on AERONET AOD are minimal when averaged across all AERONET sites, individual sites can 

- 245 be strongly influenced by diurnal cycles (Arola et al., 2013). Table 3.4 summarizes the percent difference between model simulated AAOD with and without D-BrC at the AERONET sites. 

**Table 4.** Percent difference between model simulations of absorbing aerosol optical depth at 550 nm wavelength with and without dark brown carbon at AERONET sites. 

|**Sensitivity**<br>**Simulation**|**Volume Mixing**|**Maxwell-Garnett**|**Core-shell**|**Explicit Mie**|
|---|---|---|---|---|
|All sites|+0.02%|0.00%|+0.64%|+0.02%|
|App|+0.01%|0.00%|+0.46%|+0.01%|
|Boyd|+0.01%|0.00%|+1.32%|+0.01%|
|Cape|+0.02%|0.00%|-4.64%|+0.02%|
|EPA|+0.01%|0.00%|0.00%|+0.01%|
|Geo|+0.01%|0.00%|+0.91%|+0.01 %|
|Imp|+0.00%|0.00%|+0.69%|+0.01 %|
|Lel|+0.03%|0.00%|-1.55%|+0.04 %|
|Mingo|+0.01%|0.00%|-0.06%|+0.01 %|
|SE-CTR|+0.02%|0.00%|+3.46%|+0.02 %|
|SE-OLF|+0.04%|0.00%|-1.31%|+0.04 %|
|SE-YOR|+0.03%|0.00%|+4.35%|+0.03 %|
|St Louis|+0.02%|0.00%|+1.56%|+0.02 %|
|UAH|+0.01%|0.00%|+6.42%|+0.02 %|
|UppBuf|+0.02%|0.00%|+3.46%|+0.02 %|



250 The addition of dark brown carbon increased AAOD by 0.02% for volume mixing, 0% for “Maxwell-Garnett”, 0.64% for core-shell, and 0.02% for explicit Mie on average for all sites. The base simulation (volume mixing) was minimally sensitive to the addition of D-BrC (maximum percent increase = 0.04%). The Maxwell-Garnett simulation was insensitive to the addition of D-BrC. The core shell mixing simulation was highly sensitive to the addition of D-BrC (maximum percent increase = 6.42%, maximum percent decrease = -4.64%), highlighting the importance of core-shell mixing in predictions of AAOD. The explicit 

- 255 Mie simulation was minimally sensitive to the addition of D-BrC (maximum percent increase = 0.04%). 

### **3.4 Aircraft measured extinction comparison with WRF-Chem** 

The WRF-Chem simulated in-situ aerosol extinction was evaluated with aircraft CRDS measurements for June 22nd, 23rd, 25th, 26th, and 29th. Figure 3 shows the WRF-Chem “Core-shell, D-BrC” extinction comparison with aircraft measurements. 

11 

https://doi.org/10.5194/egusphere-2026-5534 Preprint. Discussion started: 7 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 







260 **Figure 3.** Comparison of aerosol extinction measured by aircraft and WRF-Chem “Core-Shell, D-BrC” simulated extinction at 405, 532, and 662 nm wavelengths (left panel). The mean percent error (MPE) is also shown. Aerosol concentrations ≤0.5 µg m<sup>-3</sup> measured with an Aerosol Mass Spectrometer (AMS) on aircrafts were compared to WRF-Chem (right panel). 

Averaged over all flights, WRF-Chem “Core-Shell, D-BrC” underpredicted aircraft extinction at 405 and 532 nm by 12.0% and 10.4% respectively, and overpredicted extinction at 662 nm by 20.4%. Major differences could be attributed to model 

265 underpredictions in aerosol loading. While sulfate, organics, and ammonium were mostly underpredicted by the WRF-Chem simulation, nitrate was overpredicted at many time points. Figure 4 shows the temporal plots of measured and modeled extinction from flights conducted on June 22nd, 23rd, 25th, 26th, and 29th. 



**Figure 4.** Aircraft measurement and WRF-Chem “Core-shell, D-BrC” modeled aerosol extinction at 405, 532, and 662 nm wavelengths 270 over time. The timescale is not continuous between different aircraft flights. 

Model performance varied with different flights. Overall, the model performed best at 405 nm and 532 nm. The model had excellent performance (|percent error| < 5%) at 405 nm on June 23rd and at 532 nm on June 22nd and June 23rd. The model had poor performance (|percent error| > 80%) at 662 nm on June 29th in which extinction was overpredicted by 89.66%. 

12 

https://doi.org/10.5194/egusphere-2026-5534 Preprint. Discussion started: 7 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





### **3.5 Core-shell dark brown carbon and absorbing aerosol optical depth correlation** 

- 275 We investigated the relationship between core-shell dark brown carbon and absorbing aerosol optical depth with a linear regression. The correlation between dark brown carbon and absorbing aerosol optical depth is shown in Figure 5. 



**Figure 5.** Correlation between modeled core-shell dark brown carbon concentration in column and absorbing aerosol optical depth in the full domain and simulation time period. The color bar represents the number of grid cells. 

- 280 The modeled total column core-shell dark brown carbon and absorbing aerosol optical depth had a strong positive correlation with a Pearson correlation coefficient (R) of 0.745 and an R<sup>2</sup> of 0.554, as shown in Figure 5. This indicates a strong linear correlation. The linear regression line of best fit was AAOD = 0.0023[D-BrC] + 0.0007. This equation can be used to estimate increases in AAOD given dark brown carbon concentrations with core-shell considerations and using the parameters in this work. At D BrC columnar concentrations greater than ~15 µg m-3, the correlation has reduced performance. This could 

- 285 demonstrate a non-linear relationship between D-BrC and AAOD with core-shell considerations. 

### **3.6 Uncertainties** 

In this study, we assumed 20% of organic aerosol from biomass burning. However, the emission rate of dark brown carbon from wildfires is still highly uncertain, as field measurements vary between about 15% to 80% of organic carbon classified as “dark” (R. K. Chakrabarty et al., 2010; Rajan K. Chakrabarty et al., 2023; Cheng et al., 2024). One method for identifying 

13 

https://doi.org/10.5194/egusphere-2026-5534 Preprint. Discussion started: 7 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 290 dark brown carbon requires manual identification with a scanning electron microscope (SEM), which can result in uncertainty (R. K. Chakrabarty et al., 2010; Rajan K. Chakrabarty et al., 2023; Cheng et al., 2024). Additionally, QFED has been found to underestimate organic carbon loading from biomass burning (Barnard et al., 2010; Byrne et al., 2024; Wu et al., 2025). Both black carbon and organic carbon could be underestimated in this study due to the usage of QFED. Future studies should constrain the emissions of dark brown carbon and black carbon. While this study only considered spherical particles, particles 

- 295 can exist as aggregates or fractals. Future work should investigate complex morphology impacts on AOD and AAOD. The southeastern United States during summer 2013 was dominated by scattering (Washenfelder et al., 2015) so future work should assess dark brown carbon for wildfire-specific time periods. 

### **4 Conclusions** 

- This study explored the radiative effects of dark brown carbon from wildfires in the eastern United States. Dark brown 

- 300 carbon was found to increase AAOD by up to 5.2% in this simulation time period. A linear equation was derived from the correlation between columnar core-shell dark brown carbon and absorbing aerosol optical depth that can be used to estimate AAOD increases. 

Aerosol optical depth measured at the AERONET sites was underpredicted by over 50% at all sites. Sensitivity analysis at the AERONET sites demonstrated the importance of aerosol mixing on AAOD, as dark brown carbon increased AAOD by 305 0.02% for volume mixing, 0% for Maxwell-Garnett, 0.64% for core-shell, and 0.02% for explicit Mie on average for all sites. At the AERONET sites, the core-shell simulation was the most sensitive to the addition of D-BrC out of all the mixing sensitivities (maximum percent increase = 6.42%, maximum percent decrease = -4.64%). This demonstrates that the particle mixing method for aerosol optical properties can enhance the impact of dark brown carbon on AAOD. These findings provide insight on the imaginary refractive index, aerosol mixing, and Mie method impacts on AOD and AAOD. 

310 This work emphasizes the importance of accurate particle mixing and explicit Mie calculations on AOD and AAOD. Even so, these methods are highly computationally intense, even when run offline. Future work should aim to incorporate computationally efficient methods for accurate particle mixing and explicit Mie into regional-scale methods, such as MieAI (Kumar et al., 2024). This study highlights the importance of particle mixing and improves our understanding of carbonaceous absorbing aerosols. 

315 

**Code and data availability.** Code is available upon request. Observational data from the Southeast Nexus (SENEX) 2013 field campaign was used with permission from Principal Investigators of associated instruments. Data analysis utilized WRFPython which can be found at https://doi.org/10.5065/D6W094P1. 

320 **Author contributions.** All co-authors contributed to reviewing and editing the manuscript. 

14 

https://doi.org/10.5194/egusphere-2026-5534 Preprint. Discussion started: 7 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





**Competing interests.** The authors declare that they have no competing interests. 

**Acknowledgements.** The authors thank the Principal Investigators and staff of the Southeast Nexus (SENEX) 2013 field 

- 325 campaign and of the AERONET sites used in this work for establishing and maintaining the measurements used in this analysis. 

**Financial support.** This material is based upon work supported by the U.S. Department of Energy, Office of Science, Office of Workforce Development for Teachers and Scientists, Office of Science Graduate Student Research (SCGSR) program. The 

SCGSR program is administered by the Oak Ridge Institute for Science and Education for the DOE under contract number 

- 330 DE-SC0014664. 

### **References** 

- Abatzoglou, J. T. and Williams, A. P.: Impact of anthropogenic climate change on wildfire across western US forests, Proceedings of the National Academy of Sciences of the United States of America, 113, 11770–11775, 

- 335 https://doi.org/10.1073/pnas.1607171113, 2016. 

   - Ackerman, T. P. and Toon, O. B.: Absorption of visible radiation in atmosphere containing mixtures of absorbing and nonabsorbing particles, Appl. Optics, 20, 3661–3668, https://doi.org/10.1364/AO.20.003661, 1981. 

- Adler, G., Wagner, N. L., Lamb, K. D., Manfred, K. M., Schwarz, J. P., Franchin, A., Middlebrook, A. M., Washenfelder, R. A., Womack, C. C., Yokelson, R. J., and Murphy, D. M.: Evidence in biomass burning smoke for a light-absorbing 

- 340 aerosol with properties intermediate between brown and black carbon, Aerosol Science and Technology, 53, 976–989, https://doi.org/10.1080/02786826.2019.1617832, 2019. 

   - Alang, A. K. and Aggarwal, S. G.: Atmospheric Brown Carbon: Sources, Optical Properties, and Chromophore Composition, Aerosol and Air Quality Research, 24, 240035, https://doi.org/10.4209/aaqr.240035, 2024. 

- Alexander, D. T. L., Crozier, P. A., and Anderson, J. R.: Brown Carbon Spheres in East Asian Outflow and Their Optical 

- 345 Properties, Science, 321, 833–836, https://doi.org/10.1126/science.1155296, 2008. 

   - Anttila, T., Kiendler-Scharr, A., Tillmann, R., and Mentel, T. F.: On the reactive uptake of gaseous compounds by organiccoated aqueous aerosols: Theoretical analysis and application to the heterogeneous hydrolysis of N2O5, Journal of Physical Chemistry A, 110, 10435–10443, https://doi.org/10.1021/jp062403c, 2006. 

- Arola, A., Eck, T. F., Huttunen, J., Lehtinen, K. E. J., Lindfors, A. V., Myhre, G., Smirnov, A., Tripathi, S. N., and Yu, H.: 

- 350 Influence of observed diurnal cycles of aerosol optical depth on aerosol direct radiative effect, Atmospheric Chemistry and Physics, 13, 7895–7901, https://doi.org/10.5194/acp-13-7895-2013, 2013. 

   - Barnard, J. C., Fast, J. D., Paredes-Miranda, G., Arnott, W. P., and Laskin, A.: Technical note: Evaluation of the WRF-Chem “Aerosol chemical to aerosol optical properties” module using data from the MILAGRO campaign, Atmospheric Chemistry and Physics, 10, 7325–7340, https://doi.org/10.5194/acp-10-7325-2010, 2010. 

- 355 Binkowski, F. S. and Roselle, S. J.: Models-3 Community Multiscale Air Quality (CMAQ) model aerosol component 1, Model description. Journal of Geophysical Research: Atmospheres, 108, https://doi.org/10.1029/2001jd001409, 2003. 

   - Bond, T. C. and Bergstrom, R. W.: Light absorption by carbonaceous particles: an investigative review, Aerosol Sci. Tech., 40, 27–67, https://doi.org/10.1080/02786820500421521, 2006. 

15 

https://doi.org/10.5194/egusphere-2026-5534 Preprint. Discussion started: 7 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- Byrne, B., Liu, J., Bowman, K. W., Pascolini-Campbell, M., Chatterjee, A., Pandey, S., Miyazaki, K., van der Werf, G. R., 

- 360 Wunch, D., Wennberg, P. O., Roehl, C. M., and Sinha, S.: Carbon emissions from the 2023 Canadian wildfires, Nature, 633, 835–839, https://doi.org/10.1038/s41586-024-07878-z, 2024. 

   - Chakrabarty, R. K., Moosmüller, H., Chen, L.-W. A., Lewis, K., Arnott, W. P., Mazzoleni, C., Dubey, M. K., Wold, C. E., Hao, W. M., and Kreidenweis, S. M.: Brown carbon in tar balls from smoldering biomass combustion, Atmospheric Chemistry and Physics, 10, 6363–6370, https://doi.org/10.5194/acp-10-6363-2010, 2010. 

- 365 Chakrabarty, R. K., Shetty, N. J., Thind, A. S., Beeler, P., Sumlin, B. J., Zhang, C., Liu, P., Idrobo, J. C., Adachi, K., Wagner, N. L., Schwarz, J. P., Ahern, A., Sedlacek III, A. J., Lambe, A., Daube, C., Lyu, M., Liu, C., Herndon, S., Onasch, T. B., and Mishra, R.: Shortwave absorption by wildfire smoke dominated by dark brown carbon, Nature Geoscience, 16, 683–688, https://doi.org/10.1038/s41561-023-01237-9, 2023. 

- Chapman, E. G., Gustafson Jr., W. I., Easter, R. C., Barnard, J. C., Ghan, S. J., Pekour, M. S., and Fast, J. D.: Coupling 

- 370 aerosol-cloud-radiative processes in the WRF-Chem model: Investigating the radiative impact of elevated point sources, Atmos. Chem. Phys., 9, 945–964, https://doi.org/10.5194/acp-9-945-2009, 2009. 

   - Chelluboyina, G. S., Kapoor, T. S., and Chakrabarty, R. K.: Dark brown carbon from wildfires: a potent snow radiative forcing agent? Npj Climate and Atmospheric Science, 7(1), https://doi.org/10.1038/s41612-024-00738-7, 2024. 

- Chen, Y., Ng, A. E., Green, J., Zhang, Y., Riva, M., Riedel, T. P., Pye, H. O. T., Lei, Z., Olson, N. E., Cooke, M. E., Zhang, 

- 375 Z., Vizuete, W., Gold, A., Turpin, B. J., Ault, A. P., and Surratt, J. D.: Applying a Phase-Separation Parameterization in Modeling Secondary Organic Aerosol Formation from Acid-Driven Reactive Uptake of Isoprene Epoxydiols under Humid Conditions, ACS ES&T Air, 1, 511–524, https://doi.org/10.1021/acsestair.4c00002, 2024. 

- Chen, Y., Sexton, K. G., Jerry, R. E., Surratt, J. D., and Vizuete, W.: Assessment of SAPRC07 with updated isoprene chemistry against outdoor chamber experiments, Atmospheric Environment, 105(x), 109–120, 

- 380 https://doi.org/10.1016/j.atmosenv.2015.01.042, 2015. 

   - Cheng, Z., Shrivastava, M., Ijaz, A., Veghte, D., Vandergrift, G. W., Tseng, K.-P., Lata, N. N., Kew, W., Suski, K., Weis, J., Kulkarni, G., Berg, L. K., Fast, J. D., Kovarik, L., Mazzoleni, L. R., Zelenyuk, A., and China, S.: Enhanced light absorption for solid-state brown carbon from wildfires due to organic and water coatings, Nature Communications, 15, 10326, https://doi.org/10.1038/s41467-024-54506-5, 2024. 

- 385 Chou, M.D. and Suarez, M.J.: An Efficient Thermal Infrared Radiation Parameterization for Use in General Circulation Models. NASA Technical Memorandum 104606, 3, 85. https://archive.org/details/nasa_techdoc_19950009331, 1994. 

   - Chou, M.-D. and Suarez, M. J.: A solar radiation parameterization for atmospheric studies, NASA Tech. Rep. Series on Global Modeling and Data Assimilation, NASA/TM–1999–104606, Vol. 15, NASA Goddard Space Flight Center, Greenbelt, MD, USA, available at: NASA Technical Reports Server, 1999. 

- 390 Chylek, P. and Wong, J.: Effect of absorbing aerosols on global radiation budget, Geophysical Research Letters, 22, 929– 931, https://doi.org/10.1029/95GL00800, 1995. 

   - Darmenov, A. S. and da Silva, A.: The Quick Fire Emissions Dataset (QFED): Documentation of versions 2.1, 2.2 and 2.4, NASA Technical Report Series on Global Modeling and Data Assimilation, Vol. 38, NASA/TM–2015–104606, 212 pp., available at: https://ntrs.nasa.gov/citations/20180005253, 2015. 

- 395 Dennison, P. E., Brewer, S. C., Arnold, J. D., and Moritz, M. A.: Large wildfire trends in the western United States, 19842011, Geophysical Research Letters, 41, 2928–2933, https://doi.org/10.1002/2014GL059576, 2014. 

   - Devi, J. J., Bergin, M. H., Mckenzie, M., Schauer, J. J., and Weber, R. J.: Contribution of particulate brown carbon to light absorption in the rural and urban Southeast US, Atmospheric Environment, 136, 95–104, https://doi.org/10.1016/j.atmosenv.2016.04.011, 2016. 

16 

https://doi.org/10.5194/egusphere-2026-5534 Preprint. Discussion started: 7 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 400 Dubovik, O., Smirnov, A., Holben, B. N., King, M. D., Kaufman, Y. J., Eck, T. F., and Slutsker, I.: Accuracy assessments of aerosol optical properties retrieved from Aerosol Robotic Network (AERONET) Sun and sky radiance measurements, Journal of Geophysical Research Atmospheres, 105(D8), 9791–9806, https://doi.org/10.1029/2000JD900040, 2000. 

- Dubovik, O., Holben, B., Eck, T. F., Smirnov, A., Kaufman, Y. J., King, M. D., Tanré, D., and Slutsker, I.: Variability of Absorption and Optical Properties of Key Aerosol Types Observed in Worldwide Locations. J. Atmos. Sci., 59, 590–608, 

- 405 https://doi.org/10.1175/1520-0469(2002)059<0590:VOAAOP>2.0.CO;2, 2002. 

- Farrell, S. L., Rasool, Q. Z., Pye, H. O. T., Zhang, Y., Li, Y., Chen, Y., Wang, C.-T., Zhang, H., Schmedding, R., Shiraiwa, M., Green, J., Budisulistiorini, S. H., Jimenez, J. L., Hu, W., Surratt, J. D., and Vizuete, W.: Simulated reductions in heterogeneous isoprene epoxydiol reactive uptake from aerosol morphology in the contiguous United States using the Community Multiscale Air Quality Model (CMAQv5.3.2), Atmospheric Chemistry and Physics, 26, 13557–13579, 

- 410 https://doi.org/10.5194/acp-26-13557-2026, 2026. 

   - Fast, J. D., Gustafson, W. I., Easter, R. C., Zaveri, R. A., Barnard, J. C., Chapman, E. G., Grell, G. A., and Peckham, S. E.: Evolution of ozone, particulates, and aerosol direct radiative forcing in the vicinity of Houston using a fully coupled meteorology-chemistry-aerosol model, Journal of Geophysical Research Atmospheres, 111, D21305, https://doi.org/10.1029/2005JD006721, 2006. 

- 415 Feng, Y., Ramanathan, V., and Kotamarthi, V. R.: Brown carbon: A significant atmospheric absorber of solar radiation, Atmospheric Chemistry and Physics, 13, 8607–8621, https://doi.org/10.5194/acp-13-8607-2013, 2013. 

   - Fleming, L. T., Lin, P., Roberts, J. M., Selimovic, V., Yokelson, R., Laskin, J., Laskin, A., and Nizkorodov, S. A.: Molecular composition and photochemical lifetimes of brown carbon chromophores in biomass burning organic aerosol, Atmospheric Chemistry and Physics, 20, 1105–1129, https://doi.org/10.5194/acp-20-1105-2020, 2020. 

- 420 Ghan, S. J. and Zaveri, R. A.: Parameterization of optical properties for hydrated internally mixed aerosol, Journal of Geophysical Research Atmospheres, 112, https://doi.org/10.1029/2006JD007927, 2007. 

- Glenn, C. K., El Hajj, O., McQueen, Z., Poland, R. P., Penland, R., Roberts, E. T., Choi, J. H., Bai, B., Shin, N., Anosike, A., Kumar, K. V., Abdurrahman, M. I., Liu, P., Amster, I. J., Smith, G. D., Flanagan, S., Callaham, M. A., Loudermilk, E. L., O'Brien, J. J., and Saleh, R.: Brown Carbon Emissions from Biomass Burning under Simulated Wildfire and 

- 425 Prescribed-Fire Conditions, ACS ES&T Air, 1, 1124–1136, https://doi.org/10.1021/acsestair.4c00089, 2024. 

   - Guenther, A. B., Jiang, X., Heald, C. L., Sakulyanontvittaya, T., Duhl, T., Emmons, L. K., and Wang, X.: The Model of Emissions of Gases and Aerosols from Nature version 2.1 (MEGAN2.1): an extended and updated framework for modeling biogenic emissions, Geoscientific Model Development, 5, 1471–1492, https://doi.org/10.5194/gmd-5-14712012, 2012. 

- 430 Guenther, A., Karl, T., Harley, P., Wiedinmyer, C., Palmer, P. I., and Geron, C.: Estimates of global terrestrial isoprene emissions using MEGAN (Model of Emissions of Gases and Aerosols from Nature), Atmospheric Chemistry and Physics, 6, 3181–3210, https://doi.org/10.5194/acp-6-3181-2006, 2006. 

- Hammer, M. S., Martin, R. V., Van Donkelaar, A., Buchard, V., Torres, O., Ridley, D. A., and Spurr, R. J. D.: Interpreting the ultraviolet aerosol index observed with the OMI satellite instrument to understand absorption by organic aerosols: 

- 435 Implications for atmospheric oxidation and direct radiative effects, Atmospheric Chemistry and Physics, 16, 2507–2523, https://doi.org/10.5194/acp-16-2507-2016, 2016. 

   - Haywood, J. M. and Shine, K. P.: The effect of anthropogenic sulfate and soot aerosol on the clear sky planetary radiation budget, Geophysical Research Letters, 22, 603–606, https://doi.org/10.1029/95GL00075, 1995. 

- Hersbach, H., Bell, B., Berrisford, P., Hirahara, S., Horányi, A., Muñoz-Sabater, J., Nicolas, J., Peubey, C., Radu, R., 

- 440 Schepers, D., Simmons, A., Soci, C., Abdalla, S., Abellan, X., Balsamo, G., Bechtold, P., Biavati, G., Bidlot, J., Bonavita, M., De Chiara, G., Dahlgren, P., Dee, D., Diamantakis, M., Dragani, R., Flemming, J., Forbes, R., Fuentes, M., Geer, A., Haimberger, L., Healy, S., Hogan, R. J., Hólm, E., Janisková, M., Keeley, S., Laloyaux, P., Lopez, P., Lupu, C., 

17 

https://doi.org/10.5194/egusphere-2026-5534 Preprint. Discussion started: 7 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





Radnoti, G., de Rosnay, P., Rozum, I., Vamborg, F., Villaume, S., and Thépaut, J.-N.: The ERA5 global reanalysis, Quarterly Journal of the Royal Meteorological Society, 146, 1999–2049, https://doi.org/10.1002/qj.3803, 2020. 

- 445 Holben, B. N., Eck, T. F., Slutsker, I., Smirnov, A., Sinyuk, A., Schafer, J., Giles, D., and Dubovik, O.: AERONET's Version 2.0 quality assurance criteria, in: Remote Sensing of the Atmosphere and Clouds, Proc. SPIE, 6408, 64080Q, https://doi.org/10.1117/12.706524, 2006. 

- Holben, B. N., Eck, T. F., Slutsker, I., Tanré, D., Buis, J. P., Setzer, A., Vermote, E., Reagan, J. A., Kaufman, Y. J., Nakajima, T., Lavenu, F., Jankowiak, I., and Smirnov, A.: AERONET – A Federated Instrument Network and Data 

- 450 Archive for Aerosol Characterization, Remote Sens. Environ., 66, 1–16, https://doi.org/10.1016/S0034-4257(98)00031-5, 1998. 

   - Hong, G., Yang, P., Baum, B. A., Heymsfield, A. J., and Xu, K. M.: Parameterization of shortwave and longwave radiative properties of ice clouds for use in climate models, Journal of Climate, 22, 6287–6312, https://doi.org/10.1175/2009JCLI2844.1, 2009. 

- 455 Iacono, M. J., Delamere, J. S., Mlawer, E. J., Shephard, M. W., Clough, S. A., and Collins, W. D.: Radiative forcing by longlived greenhouse gases: Calculations with the AER radiative transfer models, Journal of Geophysical Research Atmospheres, 113, https://doi.org/10.1029/2008JD009944, 2008. 

- Ichoku, C., Giglio, L., Wooster, M. J., and Remer, L. A.: Global characterization of biomass-burning patterns using satellite measurements of fire radiative energy, Remote Sensing of Environment, 112, 2950–2962, 

- 460 https://doi.org/10.1016/j.rse.2008.02.009, 2008. 

   - Intergovernmental Panel on Climate Change (IPCC): Global Carbon and Other Biogeochemical Cycles and Feedbacks, in: Climate Change 2021 – The Physical Science Basis, Cambridge University Press, Cambridge, UK, 673–816, https://doi.org/10.1017/9781009157896.007, 2023a. 

- Intergovernmental Panel on Climate Change (IPCC): Short-lived Climate Forcers, in: Climate Change 2021 – The Physical 

- 465 Science Basis, Cambridge University Press, Cambridge, UK, 817–922, https://doi.org/10.1017/9781009157896.008, 2023b. 

   - Jacobson, M. Z.: Effects of biomass burning on climate, accounting for heat and moisture fluxes, black and brown carbon, and cloud absorption effects, Journal of Geophysical Research, 119, 8980–9002, https://doi.org/10.1002/2014JD021861, 2014. 

- 470 Jo, D. S., Park, R. J., Lee, S., Kim, S. W., and Zhang, X.: A global simulation of brown carbon: Implications for photochemistry and direct radiative effect, Atmospheric Chemistry and Physics, 16, 3413–3432, https://doi.org/10.5194/acp-16-3413-2016, 2016. 

- Kumar, P., Vogel, H., Bruckert, J., Muth, L. J., and Hoshyaripour, G. A.: MieAI: a neural network for calculating optical properties of internally mixed aerosol in atmospheric models, Npj Climate and Atmospheric Science, 7, 

- 475 https://doi.org/10.1038/s41612-024-00652-y, 2024. 

   - Lack, D. A., Langridge, J. M., Bahreini, R., Cappa, C. D., Middlebrook, A. M., and Schwarz, J. P.: Brown carbon and internal mixing in biomass burning particles, Proc. Natl. Acad. Sci. USA, 109, 14802–14807, https://doi.org/10.1073/pnas.1206575109, 2012. 

- Langridge, J. M., Richardson, M. S., Lack, D., Law, D., and Murphy, D. M.: Aircraft instrument for comprehensive 

- 480 characterization of aerosol optical properties, part i: Wavelength-dependent optical extinction and its relative humidity dependence measured using cavity ringdown spectroscopy, Aerosol Science and Technology, 45, 1305–1318, https://doi.org/10.1080/02786826.2011.592745, 2011. 

   - Laskin, A., Laskin, J., and Nizkorodov, S. A.: Chemistry of Atmospheric Brown Carbon, Chemical Reviews. American Chemical Society, https://doi.org/10.1021/cr5006167, 2015. 

18 

https://doi.org/10.5194/egusphere-2026-5534 Preprint. Discussion started: 7 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 485 Mao, J., Tang, X., Cheng, Y., Chen, H., Cheng, T., Li, L., and Chen, J.: Non-Volatile Particulate Matter as Cores Driving Aerosol Mixing States and Light Absorption, Geophysical Research Letters, 53, https://doi.org/10.1029/2025GL121445, 2026. 

   - Markel, V. A.: Introduction to the Maxwell Garnett approximation: tutorial, Journal of the Optical Society of America A, 33, 1244, https://doi.org/10.1364/josaa.33.001244, 2016. 

- 490 McClure, C. D., Lim, C. Y., Hagan, D. H., Kroll, J. H., and Cappa, C. D.: Biomass-burning-derived particles from a wide variety of fuels - Part 1: Properties of primary particles, Atmospheric Chemistry and Physics, 20, 1531–1547, https://doi.org/10.5194/acp-20-1531-2020, 2020. 

- Methymaki, G., Bossioli, E., Boucouvala, D., Nenes, A., and Tombrou, M.: Brown carbon absorption in the Mediterranean basin from local and long-range transported biomass burning air masses, Atmospheric Environment, 306, 

- 495 https://doi.org/10.1016/j.atmosenv.2023.119822, 2023. 

   - Mlawer, E. J., Taubman, S. J., Brown, P. D., Iacono, M. J., and Clough, S. A.: Radiative transfer for inhomogeneous atmospheres: RRTM, a validated correlated-k model for the longwave, Journal of Geophysical Research Atmospheres, 102, 16663–16682, https://doi.org/10.1029/97jd00237, 1997. 

- Morrison, H., Thompson, G., and Tatarskii, V.: Impact of cloud microphysics on the development of trailing stratiform 

- 500 precipitation in a simulated squall line: Comparison of one- and two-moment schemes, Monthly Weather Review, 137, 991–1007, https://doi.org/10.1175/2008MWR2556.1, 2009. 

   - Ng, A. E., Chen, Y., Green, J., Farrell, S., Surratt, J. D., Ault, A. P., Turpin, B. J., and Vizuete, W.: Regional-Scale Modeling Parameterizations for Secondary Organic Aerosol Formation from Isoprene Epoxydiols: Experimentally Based Evaluation and Optimization, ACS ES&T Air, 2, 2625–2637, https://doi.org/10.1021/acsestair.5c00258, 2025. 

- 505 Saleh, R., Adams, P. J., Donahue, N. M., and Robinson, A. L.: The interplay between assumed morphology and the direct radiative effect of light-absorbing organic aerosol, Geophysical Research Letters, 43, 8735–8743, https://doi.org/10.1002/2016GL069786, 2016. 

- Shrivastava, M., Berg, L. K., Fast, J. D., Easter, R. C., Laskin, A., Chapman, E. G., Gustafson Jr., W. I., Liu, Y., and Berkowitz, C. M.: Modeling aerosols and their interactions with shallow cumuli during the 2007 CHAPS field study, 

- 510 Journal of Geophysical Research Atmospheres, 118, 1343–1360, https://doi.org/10.1029/2012JD018218, 2013. 

   - Shrivastava, M.: Unveiling dark brown carbon: the hidden light-absorbing aerosols from biomass burning, One Earth, 8, 101231, https://doi.org/10.1016/j.oneear.2025.101231, 2025. 

- Strawa, A. W., Elleman, R., Hallar, A. G., Covert, D., Ricci, K., Provencal, R., Owano, T., Jonsson, H. H., Schmid, B., Luu, A., Bokarius, K., and Andrews, E.: Comparison of in situ aerosol extinction and scattering coefficient measurements 

- 515 made during the Aerosol Intensive Operating Period, Journal of Geophysical Research Atmospheres, 111, D05S03, https://doi.org/10.1029/2005JD006056, 2006. 

   - Toon, O. B. and Ackerman, T. P.: Algorithms for the calculation of scattering by stratified spheres, Appl. Optics, 20, 3657– 3660, https://doi.org/10.1364/AO.20.003657, 1981. 

- Wang, X., Heald, C. L., Ridley, D. A., Schwarz, J. P., Spackman, J. R., Perring, A. E., Coe, H., Liu, D., and Clarke, A. D.: 

- 520 Exploiting simultaneous observational constraints on mass and absorption to estimate the global direct radiative forcing of black carbon and brown carbon, Atmospheric Chemistry and Physics, 14, 10989–11010, https://doi.org/10.5194/acp14-10989-2014, 2014. 

- Wang, X., Chakrabarty, R. K., Schwarz, J. P., Murphy, S. M., Levin, E. J. T., Howell, S. G., Guo, H., Campuzano-Jost, P., and Jimenez, J. L.: Dark brown carbon from biomass burning contributes to significant global-scale positive forcing, One 

- 525 Earth, 8, 101205, https://doi.org/10.1016/j.oneear.2025.101205, 2025. 

   - Warneke, C., Trainer, M., de Gouw, J. A., Parrish, D. D., Fahey, D. W., Ravishankara, A. R., Middlebrook, A. M., Brock, C. A., Roberts, J. M., Brown, S. S., Neuman, J. A., Lerner, B. M., Lack, D., Law, D., Hübler, G., Pollack, I., Sjostedt, S., 

19 

https://doi.org/10.5194/egusphere-2026-5534 Preprint. Discussion started: 7 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- Ryerson, T. B., Gilman, J. B., Liao, J., Holloway, J., Peischl, J., Nowak, J. B., Aikin, K. C., Min, K.-E., Washenfelder, R. A., Graus, M. G., Richardson, M., Markovic, M. Z., Wagner, N. L., Welti, A., Veres, P. R., Edwards, P., Schwarz, J. P., 

- 530 Gordon, T., Dube, W. P., McKeen, S. A., Brioude, J., Ahmadov, R., Bougiatioti, A., Lin, J. J., Nenes, A., Wolfe, G. M., Hanisco, T. F., Lee, B. H., Lopez-Hilfiker, F. D., Thornton, J. A., Keutsch, F. N., Kaiser, J., Mao, J., and Hatch, C. D.: Instrumentation and measurement strategy for the NOAA SENEX aircraft campaign as part of the Southeast Atmosphere Study 2013, Atmospheric Measurement Techniques, 9, 3063–3093, https://doi.org/10.5194/amt-9-3063-2016, 2016. 

- Washenfelder, R. A., Attwood, A. R., Brock, C. A., Guo, H., Xu, L., Weber, R. J., Ng, N. L., Allen, H. M., Ayres, B. R., 

- 535 Baumann, K., Cohen, R. C., Draper, D. C., Duffey, K. C., Edgerton, E., Fry, J. L., Hu, W. W., Jimenez, J. L., Palm, B. B., Romer, P., Stone, E. A., Wooldridge, P. J., and Brown, S. S.: Biomass burning dominates brown carbon absorption in the rural southeastern United States, Geophysical Research Letters, 42, 653–664, https://doi.org/10.1002/2014GL062444, 2015. 

- Wooster, M. J., Roberts, G., Perry, G. L. W., and Kaufman, Y. J.: Retrieval of biomass combustion rates and totals from fire 

- 540 radiative power observations: FRP derivation and calibration relationships between biomass consumption and fire radiative energy release, Journal of Geophysical Research Atmospheres, 110, 1–24, https://doi.org/10.1029/2005JD006318, 2005. 

- Wu, S., Kumar, R., Li, P., Kotamarthi, R., Collis, S., Shams, S., and Sharma, A.: Sensitivity of Regional WRF-Chem Air Quality and Weather Simulations to Biomass-Burning Emission Data Sets: A Case Study of the Impact of Canadian 

- 545 Wildfire on the US, Journal of Geophysical Research: Atmospheres, 130, https://doi.org/10.1029/2025JD043944, 2025. 

   - Zaveri, R. A., Easter, R. C., Fast, J. D., and Peters, L. K.: Model for Simulating Aerosol Interactions and Chemistry (MOSAIC), Journal of Geophysical Research Atmospheres, 113, https://doi.org/10.1029/2007JD008782, 2008. 

- Zeng, L., Zhang, A., Wang, Y., Wagner, N. L., Katich, J. M., Schwarz, J. P., Schill, G. P., Brock, C., Froyd, K. D., Murphy, D. M., Williamson, C. J., Kupc, A., Scheuer, E., Dibb, J., and Weber, R. J.: Global Measurements of Brown Carbon and 

- 550 Estimated Direct Radiative Effects, Geophysical Research Letters, 47, e2020GL088747, https://doi.org/10.1029/2020GL088747, 2020. 

   - Zhang, B., Tang, J., Geng, X., Mo, Y., Zhao, S., Zhong, G., Li, J., and Zhang, G.: Seasonal changes in water-soluble brown carbon (BrC) at Nanling background station in South China, Frontiers in Environmental Science, 12, 1360453, https://doi.org/10.3389/fenvs.2024.1360453, 2024. 

- 555 Zhang, J., Shrivastava, M., Zelenyuk, A., Zaveri, R. A., Surratt, J. D., Riva, M., Bell, D., and Glasius, M.: Observationally Constrained Modeling of the Reactive Uptake of Isoprene-Derived Epoxydiols under Elevated Relative Humidity and Varying Acidity of Seed Aerosol Conditions, ACS Earth and Space Chemistry, 7, 788–799, https://doi.org/10.1021/acsearthspacechem.2c00358, 2023. 

- Zhang, Y., Chen, Y., Lambe, A. T., Olson, N. E., Lei, Z., Craig, R. L., Zhang, Z., Gold, A., Onasch, T. B., Jayne, J. T., 

- 560 Worsnop, D. R., Gaston, C. J., Thornton, J. A., Vizuete, W., Ault, A. P., and Surratt, J. D.: Effect of the Aerosol-Phase State on Secondary Organic Aerosol Formation from the Reactive Uptake of Isoprene-Derived Epoxydiols (IEPOX), Environmental Science and Technology Letters, 5, 167–174, https://doi.org/10.1021/acs.estlett.8b00044, 2018. 

- Zhang, Y., Peng, Y., Song, W., Zhang, Y. L., Ponsawansong, P., Prapamontol, T., and Wang, Y.: Contribution of brown carbon to the light absorption and radiative effect of carbonaceous aerosols from biomass burning emissions in Chiang 

- 565 Mai, Thailand, Atmospheric Environment, 260, https://doi.org/10.1016/j.atmosenv.2021.118544, 2021. 

   - Zhang, Z., Xu, W., Zeng, S., Liu, Y., Liu, T., Zhang, Y., Du, A., Li, Y., Zhang, N., Wang, J., Aruffo, E., Han, P., Li, J., Wang, Z., and Sun, Y.: Secondary Organic Aerosol Formation from Ambient Air in Summer in Urban Beijing: Contribution of S/IVOCs and Impacts of Heat Waves, Environmental Science & Technology Letters, 11, 738–745, https://doi.org/10.1021/acs.estlett.4c00415, 2024. 

20 
