---
title: Annual and 16-Day Rangeland Production Estimates for the Western United States
authors:
- Jones, Matthew O.
- Robinson, Nathaniel P.
- Naugle, David E.
- Maestas, Jeremy D.
- Reeves, Matthew C.
- Lankston, Robert W.
- Allred, Brady W.
year: '2021'
journal: Rangeland Ecology & Management
doi: 10.1016/j.rama.2021.04.003
tags:
- decision support
- rangeland
- united states
- western united states
zotero_key: L949W2BS
item_type: journalArticle
url: https://linkinghub.elsevier.com/retrieve/pii/S1550742421000464
source_url: 'unpaywall: https://www.biorxiv.org/content/biorxiv/early/2021/04/06/2020.11.06.343038.full.pdf'
fulltext_status: fulltext
synced: '2026-11-09'
---

# Annual and 16-Day Rangeland Production Estimates for the Western United States

## Abstract

Rangeland production is a foundational ecosystem service and resource on which livestock, wildlife, and people depend. Capitalizing on recent advancements in the use of remote sensing data across rangelands, we provide estimates of herbaceous rangeland production from 1986 to 2019 at 16-d and annual time steps and 30-m resolution across the western United States. A factorial comparison of this dataset and three national scale datasets is presented, and we highlight a multiple-lines-of-evidence approach when using production estimates in decision making. Herbaceous aboveground biomass at this scale and resolution provides critical information applicable for management and decision making, particularly in the face of annual grass invasion and woody encroachment of rangeland systems. These readily available data remove analytical and technological barriers allowing immediate utilization for monitoring and management.

## Full text

bioRxiv preprint doi: https://doi.org/10.1101/2020.11.06.343038; this version posted April 6, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

# **Annual and 16-day rangeland production estimates for the western United States** 

Matthew O. Jones<sup>a,b</sup> , Nathaniel P. Robinson<sup>c</sup> , David E. Naugle<sup>a</sup> , Jeremy D. Maestas<sup>d</sup> , Matthew C. Reeves<sup>e</sup> , Robert W. Lankston<sup>f</sup> , Brady W. Allred<sup>a,b</sup> 

a University of Montana, W.A. Franke College of Forestry and Conservation, Missoula, Montana, 59812. 

b Numerical Terradynamic Simulation Group, University of Montana, Missoula, Montana, 59812. c Panthera, Missoula, Montana, 59802. 

d United States Department of Agriculture, Natural Resources Conservation Service, Portland, OR, <mark>97232.</mark> 

e United States Department of Agriculture, Forest Service, Rocky Mountain Research Station, Missoula, MT, <mark>59812</mark> . 

f Lankston Consulting LLC, Seattle, WA, 98178. 

Correspondence: Matthew O. Jones, matt.jones@umontana.edu, 1-406-370-0052, 32 Campus Dr. ISB 418 Missoula, MT 59812, USA 

# **Abstract** 

Rangeland production is a foundational ecosystem service and resource upon which livestock, wildlife, and people depend. Capitalizing on recent <mark>advancements in the use of remote sensing data across rangelands we provide estimates of herbaceous rangeland production from 19862019 at 16-day and annual time steps and 30m resolution across the western United States.  A</mark> factorial comparison of this dataset and three national scale datasets is presented, and we highlight a multiple lines of evidence approach when using production estimates in decisionmaking. <mark>Herbaceous</mark> aboveground biomass <mark>at this scale and resolution provides critical information applicable for management and decision-making, particularly in the face of annual grass invasion and woody encroachment of rangeland systems. These readily available data remove analytical and technological barriers allowing immediate utilization for monitoring and management.</mark> 

**Keywords:** Production, Biomass, Rangeland Management, Remote Sensing, Primary Productivity, Conservation, Forage 

1 

bioRxiv preprint doi: https://doi.org/10.1101/2020.11.06.343038; this version posted April 6, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

# **Introduction** 

Rangeland production–specifically herbaceous aboveground biomass–is a foundational ecosystem service upon which livestock, wildlife, and people depend.  Estimates of production have long been available via field-based measurements, but such estimates are geographically and temporally limited.  Although statistical sampling techniques employed by national monitoring programs (Herrick et al., 2017; MacKinnon et al., 2011) provide means to monitor production across rangelands, such techniques and programs do not capture temporal variability or spatial heterogeneity at scales relevant to management and decision-making (e.g. within or across management units), with limited field-based plots often extrapolated to ecoregion scales (Karl et al., 2016).  Satellite and airborne remote sensing methods (Smith et al., 2019) informed by field-based data can provide spatially contiguous and temporally continuous estimates of rangeland production.  Methodologies often use empirical relationships between remote sensing indices (e.g. Normalized Difference Vegetation Index; NDVI) or terrestrial lidar retrievals, and measured or estimated biomass from field plots to map production.  This methodology is most often applied at local or regional spatial scales (Jansen et al., 2018), but has also been successfully implemented at broad national scales (Reeves et al., 2020). 

Vegetation production may also be estimated using remotely sensed data in processbased models, such as a light use efficiency model (Monteith, 1972) that calculates gross or net primary production (GPP and NPP, respectively) based on remotely sensed estimates of absorbed photosynthetically active radiation, the biophysical properties of vegetation types, and water and temperature constraints.  These GPP and NPP models are prolific (Clark et al., 2011; Running et al., 2004) but the common units of carbon (i.e., g C m<sup>-2</sup> year<sup>-1</sup> ) are not relevant to rangeland managers or practitioners.  These models also require land cover data which until recently were categorical at the pixel scale for U.S. rangelands and produced at 5-year time steps (Homer et al., 2015).  Models could therefore not account for within-pixel heterogeneity of rangeland plant functional types (PFT) (e.g., annual grasses and forbs, perennial grasses and forbs, shrubs, or trees) or PFT variation in phenology and productivity (Browning et al., 2019). Accounting for this heterogeneity is especially critical considering the prominence of large-scale woody encroachment and annual grass invasion into rangeland systems (Jones et al., 2020). Continuous land cover datasets at annual time steps are now available (Allred et al., 2021, Rigge et al., 2020) allowing models to quantify changes in production in response to encroachment and invasion at temporal intervals relevant to management. 

2 

bioRxiv preprint doi: https://doi.org/10.1101/2020.11.06.343038; this version posted April 6, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

This technical note details the development of annual and 16-day rangeland herbaceous production estimates partitioned to perennial grasses/forbs and annual grasses/forbs across western U.S. rangelands.  The data are easily accessible, account for within-pixel vegetation PFT heterogeneity, and are provided at temporal and spatial resolutions (and units) relevant to management.  We perform a factorial comparison of this new production dataset and three national scale datasets.  We highlight the value of using all data in a ‘multiple lines of evidence’ approach when implementing production estimates, where incorporating data derived from different methods into a decision-making process can spur greater data acceptance and application, and advance conservation of this valuable rangeland resource. 

# **Methods** 

# _Net primary production partitioning_ 

Detailed descriptions of the method used to calculate NPP by PFT are provided in Robinson et al., (2019); we provide an overview here.  We produced spatially contiguous 16-day Landsat NDVI composites (Robinson et al., 2017) using Landsat 5 TM, 7 ETM+, and 8 OLI surface reflectance (Vermote et al., 2016) from 1986-2019 across Western U.S. rangelands (Reeves and Mitchell, 2011).  Using the 16-day NDVI and a PFT cover dataset (Allred et al., 2021), we disaggregated pixel level NDVI using linear mixing theory to its sub-pixel PFT components.  In brief, the NDVI of a mixed pixel is disaggregated to the PFTs present in the pixel, weighted by their fractional cover and the ecoregion-scale phenology of each PFT; the mean of the PFT specific NDVI values equate to the mixed pixel NDVI.  To capture and incorporate the geographically specific PFT NDVI phenological characteristics, we built an overdetermined set of linear equations (Robinson et al., 2019) to solve for each PFT NDVI value within US EPA Level IV regions (Omernik and Griffith, 2014).  The result is PFT NDVI estimations that capture NDVI amplitudes and regional PFT phenology.  We reprojected and bilinearly resampled all Landsat imagery to a geographic coordinate system of approximately 30m resolution prior to manipulation. 

The PFT specific NDVI values are then used in the MOD17 NPP model adapted for Landsat (Robinson et al., 2018).  Using linear interpolation we calculated daily NDVI values between each 16-day composite.  We then calculated daily NPP for each PFT present in the pixel using the daily PFT NDVI values, daily GRIDMET meteorology (Abatzoglou, 2013), and the specific PFT’s biophysical properties (Robinson et al., 2018).  We multiplied NPP estimates by the PFT fractional cover estimates, resulting in total grams of carbon assimilated per PFT per 

3 

bioRxiv preprint doi: https://doi.org/10.1101/2020.11.06.343038; this version posted April 6, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

pixel per day (g C m<sup>-2</sup> day<sup>-1</sup> ). Daily values are summed to 16-day values (g C m<sup>-2</sup> 16days<sup>-1</sup> ) and to annual values (g C m<sup>-2</sup> year<sup>-1</sup> ). 

_NPP conversion to herbaceous aboveground biomass_ 

The herbaceous NPP, partitioned to perennial grasses/forbs and annual grasses/forbs, is allocated to aboveground (ANPP) pools using the equations: 

fANPP = 0.129 * MAT + 0.171 **[1]** ANPP = fANPP * NPP **[2]** 

where fANPP is the fraction partitioned to ANPP and MAT is mean annual temperature (Hui and Jackson, 2006).  We convert ANPP (g C m<sup>-2</sup> 16 days<sup>-1</sup> ) to biomass (kg ha<sup>-1</sup> or lbs acre<sup>-1</sup> ) using the pixel area and a 47.5% carbon content of vegetation estimate (Eggleston et al., 2006); the midpoint of a 45% to 50% carbon to dry matter estimation range (Schlesinger, 2005). 

_Comparisons_ 

We calculated Pearson correlation coefficients between the herbaceous aboveground biomass (HAGB) estimates and 16,591 Natural Resources Conservation Service (NRCS) National Resources Inventory (NRI) plot-level estimates of herbaceous biomass collected on rangelands from 2004 to 2018 (NRCS, USDA, 2015).  The HAGB estimate corresponding to each plot was sampled from the same year as the plot measurement. 

We also compared HAGB estimates to United States Forest Service Rangeland Production Monitoring Service (RPMS) data, provided annually from 1984-2018 at 250m resolution (Reeves et al., 2020), and to the gridded Soil Survey Geographic (gSSURGO) database which provides fixed estimates of unfavorable, normal, and favorable annual range potential production by soil survey units at 30m resolution (Soil Survey Staff, 2017).  The RPMS and gSSURGO data estimate total rangeland productivity (not solely herbaceous) but are used here as the only available gridded productivity datasets that are specific to western U.S. rangeland systems and cover a similar time period.  To account for temporal variability, we compared the 50th percentile of the two temporally dynamic datasets using years 2000-2018, and the gSSURGO ‘normal’ data.  We calculated Pearson correlation coefficients using a subsample (5000 random rangeland locations) of each of the three datasets (RAP HAGB 50th percentile, RPMS 50th percentile, gSSURGO normal).  For all comparisons we only included rangelands identified by Reeves and Mitchell (2011) inclusive of afforested, pasture, and barren categories. We also calculated the difference between the gridded HAGB, RPMS, and gSSURGO estimates and the plot level NRI herbaceous biomass estimates; scatterplots, 

4 

bioRxiv preprint doi: https://doi.org/10.1101/2020.11.06.343038; this version posted April 6, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

correlations, and the geographic distribution of those differences are provided in supplemental information. 

# **Results** 

_Herbaceous aboveground biomass_ 

Estimates of HAGB at 30m resolution are provided annually (Fig. 1a-c) from 1986-2019, and as accumulating HAGB at 16-day intervals (Fig. 1d). The HAGB is partitioned into perennial grasses/forbs and annual grasses/forbs and accounts for variation in pixel-scale fractional cover at annual time steps (Allred et al., 2021) and the phenology of each PFT.  The data are accessible for viewing and analysis via a publicly available online application, the Rangeland Analysis Platform (https://rangelands.app/). 



Figure 1.  Herbaceous aboveground biomass (HAGB) at 30m resolution across western U.S. rangelands available via the Rangeland Analysis Platform (https://rangelands.app/).  Total 

5 

bioRxiv preprint doi: https://doi.org/10.1101/2020.11.06.343038; this version posted April 6, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

annual 2019 HAGB partitioned to (a) perennial grasses and forbs and (b) annual grasses and forbs. (c) Total yearly HAGB and portions attributable to perennials and annuals for a Bureau of Land Management grazing allotment in southwest Idaho (red point in a.) from 1986-2019. (d) For the same grazing allotment, 16-day accumulating total HAGB and partitioned contributions from perennial and annual grasses/forbs for 1986-2019. 

# _Data comparisons_ 

The HAGB data available via the Rangeland Analysis Platform (hereafter RAP HAGB) are well correlated (r = 0.63) with 16,591 NRI plot-level herbaceous biomass estimates (Fig. 2). 



Figure 2.  Density scatterplot (bin width 50 kg ha<sup>-1</sup> ) of RAP herbaceous aboveground biomass (HAGB) and 16,591 NRI plot-level biomass estimates, 1:1 line (black), and Pearson correlation coefficient (r=0.63).  NRI biomass estimates greater than 6000 kg ha<sup>-1</sup> are not displayed. 

We subtracted the RPMS 50th percentile and gSSURGO ‘normal’ gridded data from the RAP HAGB 50th percentile (as well as the gSSURGO from RPMS) which provided the 

6 

bioRxiv preprint doi: https://doi.org/10.1101/2020.11.06.343038; this version posted April 6, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

geospatial distribution of differences between the products.  Mapped differences (Fig. 3a-c) and scatterplots of 5000 randomly sampled rangeland locations (Fig. 3d-f) display strong agreement as indicated by Pearson correlation coefficients.  At lower biomass levels (< ~1500 kg ha<sup>-1</sup> ) the RAP HAGB 50th percentile is well aligned with the RPMS HAGB 50th percentile (Fig. 3d) and the gSSURGO normal (Fig. 3e).  The RAP HAGB displays generally lower estimates than the other two data sets at higher biomass levels while RPMS and gSSURGO are more evenly distributed along the 1:1 line (Fig. 3f).  These distributions are expected as RPMS and gSSURGO provide total production estimates while the RAP HAGB is herbaceous production only. 



Figure 3.   Differences (a-c) between three gridded production datasets across western U.S. rangelands using the 50th percentile of annual values (2000-2018) from RAP and RPMS data, and ‘normal’ values from gSSURGO.  Scatterplots and Pearson correlation coefficients (d-f) of production values sampled from each data set for 5000 randomly selected rangeland locations. 

Geographic distribution of the differences between the NRI herbaceous biomass estimates and the gridded HAGB, RPMS, and gSSURGO estimates (Supplemental Information) demonstrate general agreement across the western U.S. with greater differences apparent in the southern Great Plains. 

7 

bioRxiv preprint doi: https://doi.org/10.1101/2020.11.06.343038; this version posted April 6, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

# **Discussion** 

<mark>Estimates of rangeland production–specifically herbaceous aboveground biomass or forage–are now available annually and at 16-day intervals from 1986 to 2019 at 30m resolution across the western U.S. and represent five advancements specifically relevant to management. These d</mark> ata are 1) provided in units recognized by and applicable to management (i.e., kg ha<sup>-1</sup> or lbs acre<sup>-1</sup> ); 2) produced at temporal fidelities applicable to monitoring the effects of climate, disturbance, management, and other factors, 3) calculated at a spatial resolution (30m) that allows for assessment of variability both within and across management units; 4) are easily accessible where monitoring, analysis, and interpretation can be achieved without the need for specialized technical knowledge or skills; and 5) account for annual pixel-scale changes in PFT composition (e.g. annual grasses or trees encroaching rangelands) and the relative contributions of annual forbs and grasses and perennial forbs and grasses to total herbaceous biomass. <mark>The availability of these data and other rangeland wide vegetation data (R</mark> eeves et al., 2020, Rigge et al., 2020, Pastick et al., 2020 <mark>) have ushered in a new era where rangeland mapping from national to management scales is now a working reality (Jones et al., 2020).</mark> 

<mark>These herbaceous biomass data provide land managers, practitioners, and decisionmakers novel, temporally continuous, and spatially contiguous data for enhanced rangeland management.  These</mark> data can be paired with local knowledge and information to better inform management strategies at the scale of a grazing allotment or pasture.  At larger scales, these biomass data shed light on persistent ecosystem threats like invasive annual grasses (Jones et al., 2020) that are contributing to the continual rise of annual grass/forb biomass on western rangelands (Fusco et al., 2019; see Fig. 1).  Differences in forage quality and phenology between annuals and perennials also have important implications for rangeland functions including accelerated wildfire return intervals (Pilliod et al., 2017).  These represent only a few of the many potential scenarios where such data can provide greater insight and better inform management of grazing, wildlife, fuel, and fire, as well as assessing outcomes of management practices. 

This technical note does not present a traditional validation of these new RAP HAGB data due to the lack of plot-level HAGB data at the scope and scale of the data product.  While NRI plot-level data do include _some_ destructive sampling (i.e., clipping, drying, and weighing), the methods also incorporate subjective estimations and correction factors.  Also, the model used to estimate RAP HAGB is process based and not empirical – it does not incorporate biomass field plots at any step.  We therefore examine ‘multiple lines of evidence’ and factorially 

8 

bioRxiv preprint doi: https://doi.org/10.1101/2020.11.06.343038; this version posted April 6, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

compare the four available broad-scale data sets of rangeland production.  This method demonstrates a best-practices approach when using these type of data in a decision-making framework; utilize all data sources, examine their similarities and discrepancies, and incorporate local knowledge to best inform a data driven decision. 

# **Implications** 

<mark>The temporally dynamic herbaceous aboveground biomass data represent a culmination of advancements in utilizing remote sensing data to monitor rangelands more effectively and efficiently.  The new geospatial datasets of rangeland production provide land managers and decision-makers spatially contiguous and temporally relevant data to monitor rangeland forage, conduct meaningful comparisons of management outcomes using common data, and examine within season variability of forage to better assess management actions.  The readily available data (RAP, https://rangelands.app/; RPMS, https://www.fuelcast.net/) remove analytical and technological barriers, allowing for immediate utilization. Never before has so much data been directly available and applicable to rangeland management. We anticipate and look forward to new applications, analyses, discoveries, and innovations with these data that improve our understanding and management of rangelands.</mark> 

# **Acknowledgments** 

This work was made possible by the United States Department of Agriculture, Natural Resources Conservation Service’s Working Lands for Wildlife, the USDA’s Conservation Effects Assessment Project, and the Bureau of Land Management.  All data are freely available via the Rangeland Analysis Platform (https://rangelands.app). 

# **References** 

- Abatzoglou, J.T., 2013. Development of gridded surface meteorological data for ecological applications and modelling. Int. J. Climatol. 33, 121–131. https://doi.org/10.1002/joc.3413 

- Allred, B.W., Bestelmeyer, B.T., Boyd, C.S., Brown, C., Davies, K.W., Duniway, M.C., Ellsworth, L.M., Erickson, T.A., Fuhlendorf, S.D., Griffiths, T.V., Jansen, V., Jones, M.O., Karl, J., Knight, A., Maestas, J.D., Maynard, J.J., McCord, S.E., Naugle, D.E., Starns, H.D., Twidwell, D., Uden, D.R., 2021. Improving Landsat predictions of rangeland fractional cover with multitask learning and uncertainty. Methods Ecol. Evol. https://doi.org/10.1111/2041210x.13564 

- Browning, D.M., Snyder, K.A., Herrick, J.E., 2019. Plant Phenology: Taking the Pulse of Rangelands. Rangelands 41, 129–134. https://doi.org/10.1016/j.rala.2019.02.001 

Clark, D.B., Mercado, L.M., Sitch, S., Jones, C., Harding, R.J., 2011. The Joint UK Land 

9 

bioRxiv preprint doi: https://doi.org/10.1101/2020.11.06.343038; this version posted April 6, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

   - Environment Simulator (JULES), Model description – Part 2: Carbon fluxes and vegetation 4. https://doi.org/10.5194/gmd-4-701-2011 

- Eggleston, S., Buendia, L., Miwa, K., Ngara, T., Tanabe, K., 2006. 2006 IPCC guidelines for national greenhouse gas inventories. Institute for Global Environmental Strategies Hayama, Japan. 

- Fusco, E.J., Finn, J.T., Balch, J.K., Nagy, R.C., Bradley, B.A., 2019. Invasive grasses increase fire occurrence and frequency across US ecoregions. Proc. Natl. Acad. Sci. U. S. A. 116, 23594–23599. https://doi.org/10.1073/pnas.1908253116 

- Herrick, J.E., Van Zee, J.W., McCord, S.E., Courtright, Ericha M., Karl, Jason W., Burkett, Laura M., 2017. Monitoring Manual for Grassland, Shrubland, and Savanna Ecosystems. USDAARS Jornada Experimental Range. 

- Homer, C., Dewitz, J., Yang, L., Jin, S., Danielson, P., Xian, G., Coulston, J., Herold, N., Wickham, J., Megown, K., 2015. Completion of the 2011 National Land Cover Database for the Conterminous United States – Representing a Decade of Land Cover Change Information. Photogrammetric Engineering and Remote Sensing 81, 345–354. 

- Hui, D., Jackson, R.B., 2006. Geographical and interannual variability in biomass partitioning in grassland ecosystems: a synthesis of field data. New Phytol. 169, 85–93. https://doi.org/10.1111/j.1469-8137.2005.01569.x 

- Jansen, V.S., Kolden, C.A., Schmalz, H.J., 2018. The Development of Near Real-Time Biomass and Cover Estimates for Adaptive Rangeland Management Using Landsat 7 and Landsat 8 Surface Reflectance Products. Remote Sensing 10, 1057. https://doi.org/10.3390/rs10071057 

- Jones, M.O., Naugle, D.E., Twidwell, D., Uden, D.R., Maestas, J.D., Allred, B.W., 2020. Beyond Inventories: Emergence of a New Era in Rangeland Monitoring. Rangeland Ecol. Manage. https://doi.org/10.1016/j.rama.2020.06.009 

- Karl, S., Kachergis, E., Karl, J.W., 2016. Bureau of Land Management Rangeland Resource Assessment: 2011. US Department of the Interior, Bureau of Land Management, National Operations Center, Denver, CO. 96 pp. 

- MacKinnon, W.C., Karl, J.W., Toevs, G.R., Taylor, J.J., Karl, M.G., Spurrier, C.S., Herrick, J.E., 2011. BLM core terrestrial indicators and methods. US Department of the Interior, Bureau of Land Management, National National Operations Center, Denver, CO. 96 pp. 

- Monteith, J.L., 1972. Solar Radiation and Productivity in Tropical Ecosystems. J. Appl. Ecol. 9, 747–766. https://doi.org/10.2307/2401901 

- Omernik, J.M., Griffith, G.E., 2014. Ecoregions of the Conterminous United States: Evolution of a Hierarchical Spatial Framework. Environ. Manage. 54, 1249–1266. https://doi.org/10.1007/s00267-014-0364-1 

- Pilliod, D.S., Welty, J.L., Arkle, R.S., 2017. Refining the cheatgrass-fire cycle in the Great Basin: Precipitation timing and fine fuel composition predict wildfire trends. Ecol. Evol. 7, 8126– 8151. https://doi.org/10.1002/ece3.3414 

- Reeves, M.C., Hanberry, B.B., Wilmer, H., Kaplan, N.E., Lauenroth, W.K., 2020. An Assessment of Production Trends on the Great Plains from 1984 to 2017. Rangeland Ecol. Manage. https://doi.org/10.1016/j.rama.2020.01.011 

- Reeves, M.C., Mitchell, J.E., 2011. Extent of Coterminous US Rangelands: Quantifying Implications of Differing Agency Perspectives. Rangeland Ecol. Manage. 64, 585–597. 

10 

bioRxiv preprint doi: https://doi.org/10.1101/2020.11.06.343038; this version posted April 6, 2021. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC-ND 4.0 International license. 

https://doi.org/10.2111/REM-D-11-00035.1 

- Robinson, N.P., Allred, B.W., Jones, M.O., Moreno, A., Kimball, J.S., Naugle, D.E., Erickson, T.A., Richardson, A.D., 2017. A Dynamic Landsat Derived Normalized Difference Vegetation Index (NDVI) Product for the Conterminous United States. Remote Sensing 9, 863. https://doi.org/10.3390/rs9080863 

- Robinson, N.P., Allred, B.W., Smith, W.K., Jones, M.O., Moreno, A., Erickson, T.A., Naugle, D.E., Running, S.W., 2018. Terrestrial primary production for the conterminous United States derived from Landsat 30 m and MODIS 250 m. Remote Sensing in Ecology and Conservation 4, 264–280. 

- Robinson, N.P., Jones, M.O., Moreno, A., Erickson, T.A., Naugle, D.E., Allred, B.W., 2019. Rangeland Productivity Partitioned to Sub-Pixel Plant Functional Types. Remote Sensing 11, 1427. 

- Running, S.W., Nemani, R.R., Heinsch, F.A., Zhao, M., Reeves, M., Hashimoto, H., 2004. A Continuous Satellite-Derived Measure of Global Terrestrial Primary Production. Bioscience 54, 547–560. https://doi.org/10.1641/0006-3568(2004)054[0547:ACSMOG]2.0.CO;2 

- Schlesinger, W.H., 2005. Biogeochemistry. Elsevier. 

- Smith, W.K., Dannenberg, M.P., Yan, D., Herrmann, S., Barnes, M.L., Barron-Gafford, G.A., Biederman, J.A., Ferrenberg, S., Fox, A.M., Hudson, A., Knowles, J.F., MacBean, N., Moore, D.J.P., Nagler, P.L., Reed, S.C., Rutherford, W.A., Scott, R.L., Wang, X., Yang, J., 2019. Remote sensing of dryland ecosystem structure and function: Progress, challenges, and opportunities. Remote Sens. Environ. 233, 111401. https://doi.org/10.1016/j.rse.2019.111401 

- Soil Survey Staff, 2017 Natural Resources Conservation Service, United States Department of Agriculture. Web Soil Survey. 

- NRCS, USDA, 2015. The National Resources Inventory grazing lands on-site database. Compiled by the Resource Inventory Division; processed by the Resource Assessment Division, Conservation Effects Assessment Project - Grazing Land Component. 

- Vermote, E., Justice, C., Claverie, M., Franch, B., 2016. Preliminary analysis of the performance of the Landsat 8/OLI land surface reflectance product. Remote Sens. Environ. 185, 46–56. https://doi.org/10.1016/j.rse.2016.04.008 

11 
