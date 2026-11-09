---
title: A monthly gridded burned area database of national wildland fire data
authors:
- Gincheva, Andrina
- Pausas, Juli G.
- Edwards, Andrew
- Provenzale, Antonello
- Cerdà, Artemi
- Hanes, Chelene
- Royé, Dominic
- Chuvieco, Emilio
- Mouillot, Florent
- Vissio, Gabriele
- Rodrigo, Jesús
- Bedía, Joaquin
- Abatzoglou, John T.
- Senciales González, José María
- Short, Karen C.
- Baudena, Mara
- Llasat, Maria Carmen
- Magnani, Marta
- Boer, Matthias M.
- González, Mauro E.
- Torres-Vázquez, Miguel Ángel
- Fiorucci, Paolo
- Jacklyn, Peter
- Libonati, Renata
- Trigo, Ricardo M.
- Herrera, Sixto
- Jerez, Sonia
- Wang, Xianli
- Turco, Marco
year: '2024'
journal: Scientific Data
doi: 10.1038/s41597-024-03141-2
tags:
- burned area
- environmental impact
- fire
- natural hazards
zotero_key: 3GV338L6
item_type: journalArticle
url: https://www.nature.com/articles/s41597-024-03141-2
source_url: 'unpaywall: https://www.nature.com/articles/s41597-024-03141-2.pdf'
fulltext_status: fulltext
synced: '2026-11-09'
---

# A monthly gridded burned area database of national wildland fire data

## Abstract

We assembled the first gridded burned area (BA) database of national wildfire data (ONFIRE), a comprehensive and integrated resource for researchers, non-government organisations, and government agencies analysing wildfires in various regions of the Earth. We extracted and harmonised records from different regions and sources using open and reproducible methods, providing data in a common framework for the whole period available (starting from 1950 in Australia, 1959 in Canada, 1985 in Chile, 1980 in Europe, and 1984 in the United States) up to 2021 on a common 1° × 1° grid. The data originate from national agencies (often, ground mapping), thus representing the best local expert knowledge. Key opportunities and limits in using this dataset are discussed as well as possible future expansions of this open-source approach that should be explored. This dataset complements existing gridded BA data based on remote sensing and offers a valuable opportunity to better understand and assess fire regime changes, and their drivers, in these regions. The ONFIRE database can be freely accessed at https://zenodo.org/record/8289245.

## Full text

www.nature.com/scientificdata 



## **O�EN** 

### **DATA DESCRI�TOR** 

# **a monthly gridded burned area database of national wildland fire data** 

**andrina Gincheva** **_et al._**<sup>**_#_**</sup> 

**We assembled the first gridded burned area (BA) database of national wildfire data (ONFIRE), a comprehensive and integrated resource for researchers, non-government organisations, and government agencies analysing wildfires in various regions of the Earth. We extracted and harmonised records from different regions and sources using open and reproducible methods, providing data in a common framework for the whole period available (starting from 1950 in Australia, 1959 in Canada, 1985 in Chile, 1980 in Europe, and 1984 in the United States) up to 2021 on a common 1° × 1° grid. The data originate from national agencies (often, ground mapping), thus representing the best local expert knowledge. Key opportunities and limits in using this dataset are discussed as well as possible future expansions of this open-source approach that should be explored. This dataset complements existing gridded BA data based on remote sensing and offers a valuable opportunity to better understand and assess fire regime changes, and their drivers, in these regions. The ONFIRE database can be freely accessed at https://zenodo.org/record/8289245.** 

#### **Background & Summary** 

Humans have coexisted with wildfires for millennia, and fire has played a relevant role in maintaining ecosystem services for societies worldwide<sup>1,2</sup> . However, losses of lives and goods (i.e. natural resources and built assets) are also associated with wildfires, leading to growing concerns about increased fire activity in response to climate change<sup>3</sup> . The study of fire regime changes and their underlying causes is crucial for the development of effective fire management strategies and future prevention plans in the face of ongoing global changes<sup>4,5</sup> . Despite recent advancements in fire data availability and research efforts, much remains to be learned regarding fire trends and drivers<sup>4,6–8</sup> . 

A growing body of work uses fire statistical estimates based on satellite products<sup>9–12</sup> ; however, only recent decades (i.e., since the early 2000s<sup>13,14</sup> ) have afforded the mature technology to produce the first global Burned Area (BA) datasets<sup>14</sup> . Moreover, remote sensing-based BA estimates have some limitations, including the poor detection of understory fires, fires occurring under the presence of heavy smoke, agricultural fires, and false positives due to other sources (e.g., cloud shadows and deforested areas), and other land use changes such as clearing and intertidal movement, causing BA estimates to vary widely between different products<sup>15–18</sup> . 

Other BA information is derived from a variety of sources, including, for instance, ground-based mapping and aerial photography. For several regions, such as Australia, Canada, Chile, the European Union (Europe hereinafter), and the U.S.A., national fire inventories of BA data are generally available for a longer period than the global satellite BA products<sup>13</sup> . Although these fire datasets cannot be considered error-free “ground truth”, they represent the longest government-sourced fire information available today at the regional scale and have been widely used as reference datasets in multiple studies<sup>16,19–29</sup> . Although these regional databases are publicly available, merging them together is a time-consuming task, partly because these archives are stored in different formats and resolutions, from spreadsheets of BA data over sub-regions to shapefiles with detailed information of all mapped fires. A harmonized regional fire dataset based on regional/national archives may simplify their use in intercomparison and assessment studies and could complement and temporally extend the BA products based on satellite data. 

Here, we describe the creation of an integrated and open-access database composed of available BA records from government-sourced observations in Australia, Europe, Canada, Chile, and the U.S.A. This gridded BA 

> **_#_** A full list of authors and their affiliations appears at the end of the paper. 

Scientific **Data** | _(2024) 11:352_ | https://doi.org/10.1038/s41597-024-03141-2 

1 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



**Fig. 1** Schematic workflow for the harmonisation of BA observations from different regions to develop the ONFIRE dataset. 

database of national wildland fire data (ONFIRE database) aims to transform the authoritative fire data into a public, easily accessible, harmonized, and usable database to facilitate broad-scale fire research<sup>30,31</sup> . Owing to the format of the source inventories, the ONFIRE database resolution is constrained to a monthly, 1° grid, standardised for each area, thus reducing the likelihood of errors in the code and the effort needed to adapt it to different source formats. Although this level of aggregation may obscure the details of the variability within grids, some of the temporal and spatial noise present in the higher-resolution data may be reduced and provide a comprehensive regional-scale BA analysis. A survey of users’ needs for BA products<sup>15</sup> emphasised the importance of having a coarser-scale product to reduce the data volume and processing cost. In addition, they recommended that the BA products should be available in ASCII and netCDF formats. Taking these considerations into account, the ONFIRE dataset<sup>32</sup> is released in both these formats and is freely available in a Zenodo permanent repository (https://zenodo.org/record/8289245), which will ensure the usability of this information for a wide range of applications. In addition, the data are accompanied by the corresponding metadata with the original references and inventory sources. Finally, we explore the main opportunities and constraints related to the use of this dataset, as well as potential future extensions for this open-source solution. We specifically encourage any researcher/fire agency to share their data through the ONFIRE initiative. 

#### **Methods** 

We compiled BA observations from government agencies in Australia, Canada, Chile, Europe, and the U.S.A. then remapped the monthly BA at a common 1° × 1° grid. Finally, we validated the ONFIRE dataset (Fig. 1). The temporal and spatial BA resolution adopted by the ONFIRE dataset resulted from the availability of Europe and Chile monthly data provided with a resolution of approximately 1°. 

**Remapping methodology.** The data were effectively assigned to a 1° × 1° grid (we used the 1° grid used in the Sixth Assessment Report of the United Nations Intergovernmental Panel on Climate Change<sup>33,34</sup> ) while considering the specific conditions of the original format, i. point data (generally corresponding to fire polygon centroid), ii. fire polygons, or iii. region-level data: 

- I. Point data 

   - Assigned the BA value to the grid cell containing the point. 

   - • Determine the month for the grid cell based on the starting date of the fire. 

- II. Polygon of Fire Perimeters 

   - Calculated the centroid for the corresponding fire polygon. 

   - Assigned the BA value to the grid cell containing the centroid. 

   - • Determined the month for the grid cell based on the starting date of the fire. 

Scientific **Data** | _(2024) 11:352_ | https://doi.org/10.1038/s41597-024-03141-2 

2 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

|**Region**|**Source**|**Available period**|
|---|---|---|
|Australia|New South Wales (NSW):https://datasets.seed.nsw.gov.au/dataset/fire-history-wildfires-and-prescribed-<br>burns-1e8b6|1950–2021|
|Australia|Northern Territory (NT):https://firenorth.org.au/nafi3/|2000–2021|
|Australia|Queensland (QLD):https://qldspatial.information.qld.gov.au/catalogue/custom/|1950–2021|
|Australia|South Australia (SA):https://data.sa.gov.au/data/dataset/fire-history|1950–2021|
|Australia|Tasmania (TAS):http://listdata.thelist.tas.gov.au/opendata/|1961–2021|
|Australia|Victoria (VIC):https://discover.data.vic.gov.au/dataset/fire-history-records-of-fires-across-victoria-<br>showing-the-fire-scars2|1950–2021|
|Australia|Western Australia (WA):https://catalogue.data.wa.gov.au/dataset/dbca-fire-history|1950–2021|
|Canada|NBAC:https://cwfis.cfs.nrcan.gc.ca/datamart/metadata/nbac|1986–2020|
|Canada|NFDB:https://cwfis.cfs.nrcan.gc.ca/downloads/nfdb/fire_pnt/current_version/NFDB_point_large_fires.zip|1959–2021|
|Chile|CONAF:https://www.conaf.cl/incendios-forestales/incendios-forestales-en-chile/estadisticas-historicas/|1959–2021|
|Europe|EFFIS:https://effis.jrc.ec.europa.eu/|1980–2021 (see Table2<br>for more details)|
|U.S.A.|MTBS:https://mtbs.gov/direct-download|1984–2020|



**Table 1.** List of each regional source and their available periods included in the ONFIRE dataset. 

III. Total BA over a Region: 

- Determine the number ( _n_ ) of gridpoints at a resolution of 0.1° within the region, to ensure relatively small regions are not excluded. 

- Divided the BA value of the region by _n_ . 

- Assigned the resulting BA value to each 0.1° grid cell within the region, conserving total BA by distributing the BA proportionally across the grid cells within the region. 

- Sum all BA values at 0.1° that fall on a grid cell of the 1° grid. 

**Compilation of wildland fire data.** The BA observations and full references that composed the ONFIRE datasets are derived from government agencies in Australia, Canada, Chile, Europe, and the U.S.A. (Fig. 1, Table 1). The definition of wildland fire is inconsistent across countries and time periods. These fires are commonly referred to by different names such as wildland fires, wildfires, bushfires, biomass burning, forest fires, agricultural fires, and prescribed fires<sup>35</sup> , in addition to some similar names in Spanish (for Chile). Among these, the most extensively documented fires in our database are categorised as “wildland fires” (“incendios forestales” for Chile). This classification encompasses planned, prescribed, or controlled burning and unplanned or accidentally ignited fires known as “wildfires”, which are considered a distinct class of wildland fires, separate from prescribed or controlled burning. It is worth noting that agricultural fires, which involve burning agricultural wastes from e.g., sugar cane in South America, rice in Asia, or wheat stubble in temperate countries (south-central Chile), can affect vast areas. However, these fires are not included in our dataset (differently from remote sensing data) as they are typically not reported in (wild) fire records<sup>36</sup> . 

**Australia.** In Australia, the lack of a unified national database has led to the compilation of data from different fire management agencies in each state and territory that have provided statistics (Table 1) to obtain a complete picture of the area burned in the country<sup>19,21</sup> . Data from these agencies are available in the form of polygons in vector files that have been derived from a variety of sources, including terrestrial mapping, aerial photography, GPS boundary plotting from ground assessments, and remote sensing. Consistent burned area mapping from 2000 for north and central Australia are freely available as shapefiles and GeoTIFF files from the NAFI website<sup>37</sup> managed by Charles Darwin University funded by the Australian Government for carbon accounting. These fire scar maps are generated through a semi-automated process approximately weekly, using 250 m image bands (red and near-infrared) from the Moderate Resolution Imaging Spectroradiometer (MODIS) sensor. They are collated on a monthly basis and cover a significant portion (75%) of the Australian continent (specifically, the Northern Territory, the majority of Queensland, the West Australian rangelands and savannas, and the northern half of South Australia<sup>38,39</sup> We used NAFI scars for the following areas: the Northern Territory and Alice Springs, Barkly, Daly - Tiwi - West Arnhem, Darwin City, Darwin Suburbs, East Pilbara, Katherine, Kimberley, Litchfield, Outback - North, Outback - South, and Palmerston. 

All these data have been extensively validated and used previously as reference products in several studies<sup>21,40–43</sup> . The types of fires mapped in these datasets include both prescribed fires and wildfires. Wildfires are frequently labeled “bushfires”, in the more heavily populated regions of the south-east and south-west. In databases, or for example public warning systems, “bushfires” are “unplanned fires”, or “wildfires” as opposed to “planned fires”, “hazard reduction burns” or “prescribed fires”. 

**Canada.** There are numerous fire databases in Canada, and they each come with a different set of limitations (Hanes _et al_ ., 2019). The Canadian National Fire Database (NFDB) is best for the exploration of long-term BA using fire agency-collected data<sup>22,44–49</sup> and is most comparable to other national datasets over their common time period. The NFDB provides fire point data with longitude, latitude, size, month, and year of fire as provided by 

Scientific **Data** | _(2024) 11:352_ | https://doi.org/10.1038/s41597-024-03141-2 

3 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

|**Country**|**From**|**To**|**Comments**|
|---|---|---|---|
|Bulgaria|2005|2019||
|Cyprus|2000|2019|Only Greek part of CY|
|Croatia|1996|2019||
|Czech Republic|2004|2019||
|Estonia|2005|2020||
|Finland|2005|2020||
|France|1985|2020|Only Mediterranean regions before 1992|
|Germany|1994|2021|Some NUTS regions missing|
|Greece|1983|2011|Some NUTS regions missing|
|Hungary|2002|2020||
|Italy|1985|2015|Special status or autonomous regions (e.g., Sicily, Sardinia) often missing|
|Lithuania|2004|2021||
|Latvia|2004|2018||
|Netherland|2017|2020||
|Poland|1994|2020||
|Portugal|1980|2020||
|Romania|2004|2021||
|Spain|1985|2015|Some NUTS regions missing|
|Slovakia|2004|2018||
|Slovenia|1995|2021||
|Sweden|1996|2020||



**Table 2.** Details of the EFFIS dataset, with the starting and ending period available and possible comments. 

individual fire management agencies. Only fires greater than 200 hectares are included in the database and only data from 1959 are included in this analysis because of the data quality concerns prior to this year<sup>50</sup> . From 1959 to 2021, the dataset records consist of ~1.3 Mkm<sup>2</sup> of BA and ~18000 occurrences for the entire country. 

A second fire database has recently gained wide use in Canada: the National Burned Area Composite (NBAC) dataset<sup>51–53</sup> . The NBAC dataset is considered the most consistent and accurate wildfire polygon database in Canada. This fire polygon database is derived from 30-m Landsat imagery and high-quality agency imagery of spatial resolution <30 m since 1986<sup>51</sup> ; it has been updated regularly after it was published. Because NBAC does not cover fires before 1986, one must combine NBAC with NFDB to construct the fire database when fire records from early years are required<sup>52</sup> . From 1986 to 2020, the dataset records consist of ~750000 km<sup>2</sup> and ~35000 occurrences for the entire country. 

Recent comparisons have identified that BA estimates in Canada based on NFDB, on average may be overestimated by ~20% especially for early years (i.e., before 2000) prior to greater use of remote sensing products<sup>52</sup> . The imprecisions are primarily attributable to the limitations of the fire perimeter mapping techniques that were accessible during that period, such as sketch mapping, GPS-based digitization, and geographic coordinate point buffering. These methods often do not consider unburned islands and water bodies inside the fire perimeter<sup>54,55</sup> . Acknowledging that limitation in these datasets, we provided gridded BA for both the NFDB and NBAC datasets. In summary, we introduce two datasets for Canada, namely ONFIRE-NBAC and ONFIRE-NFDB, which are named in reference to their respective original sources. 

**Chile.** In Chile, the official fire database is the responsibility of the Chilean Forest Service (CONAF) and comprises the period between 1985 and 2021. Although there is a historical database of the number of fires and BA since 1964, only records starting in 1985 provide a reliable monthly BA for each administrative region of the country. Fire records include the number of fires and BA considering different vegetation types (natural vegetation, forest plantations, shrublands, pastures, excluding agricultural burnings of crops and grass). From 1985 to 2022, the dataset records consist of ~28000 km<sup>2</sup> of BA and ~225000 occurrences for the entire country. The CONAF dataset has been validated and used in several studies to analyse the relationships between climate (e.g., drying trends and heat waves), land use, socioeconomic factors, and wildfires<sup>4,23–25,56–61</sup> . 

**Europe.** The European Forest Fire Information System<sup>62</sup> (EFFIS), established by the Joint Research Centre and the Directorate General for the Environment of the European Commission, is the primary source of harmonised fire data and provides the official fire statistics of the European Union. Via direct consultation with the European Forest Fire Information System (EFFIS), we obtained monthly data on Burned Areas at the NUTS3 territorial level, as classified by the 2016 Nomenclature of Units for Territorial Statistics, which corresponds to aggregated municipal or provincial units<sup>63</sup> . This dataset includes several European countries that actively share data with EFFIS, as detailed in Table 2. The EFFIS dataset consists of BA (in hectares, the totals are for fires of 1 ha or greater) occurring in forests, other wooded lands, and other non-wooded lands reported by the country, while areas designated as agricultural or other artificial surfaces are not included<sup>62</sup> . The dataset records consist of ~150000 km<sup>2</sup> of BA and ~700000 occurrences for the entire region. This dataset had several limitations, 

Scientific **Data** | _(2024) 11:352_ | https://doi.org/10.1038/s41597-024-03141-2 

4 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

namely the lack of fire perimeter data because the raw data are owned by the contributing countries; EFFIS is only allowed to aggregate it by NUTS and share the resulting data at the NUTS level. Another limitation is the lack of recent data from several countries. This is because the entire data provision system is voluntary without a regulated standard for contributions. In addition, some countries do not have a national scheme in place to collect and share data, so they collect individual fire data only from certain regions or forest types (e.g., nationally owned forests), or the data are collected within the country, but these data are not shared with EFFIS. This can lead to fewer fires in the database than those registered. On the other hand, some countries may add records to the database that they do not count as forest fires in national statistics (e.g., agricultural fires). Nevertheless, this database constitutes the state-of-the-art information available today in Europe and shows high agreement with satellite products over common periods<sup>16</sup> . Moreover, several studies have used EFFIS data to assess fire evolution in Europe<sup>26,64</sup> and its drivers<sup>65,66</sup> . 

**U.S.A.** The Fire Program Analysis fire-occurrence database (FPA-FOD) dataset<sup>67</sup> provides information on wildfires that occurred in the U.S.A. between 1992 and 2020 and includes information on the location, size, and cause of the fire. This is the 6th Edition of the FPA-FOD dataset, first published in 2013<sup>68</sup> . The data were compiled from the final fire reports of federal, state, and local fire organisations and include over 2.3 million geo-referenced records, providing the most comprehensive accounting of U.S.A. wildfire activity for the time period<sup>67,68</sup> . While the FPA-FOD data does not impose a minimum fire size requirement, it is worth noting that agencies typically report the smallest fires in the dataset as being 0.04 hectares in size. The FPA-FOD dataset does not encompass prescribed/controlled burning, thereby failing to provide a comprehensive representation of the total burned area resulting from biomass burning, landscape fires, or even wildland fires as a whole. However, although inevitably incomplete in some aspects<sup>68</sup> , this dataset is widely used by researchers and practitioners to study the causes and consequences of wildfires in the U.S.A. Applications of the data include analysing the relationships between climate, land use, and wildfires, as well as developing fire management strategies to prevent and mitigate the impacts of wildfires<sup>27,69–72</sup> . 

Another fire dataset available for the U.S.A. is the Monitoring Trends in Burn Severity (MTBS) data<sup>73–75</sup> . This is a semi-automated program that employs pre-fire and post-fire Landsat imagery for the generation of estimated BA severities. The MTBS dataset aims to provide comprehensive coverage of large fire events throughout the United States, subject to the criterion that fires must surpass a specific size threshold (>2.02 km<sup>2</sup> and >4.05 km<sup>2</sup> in the eastern and western US, respectively) since 1984 and consists of ~830000 km<sup>2</sup> of BA and ~30000 occurrences for the entire country. MTBS data have been widely used by researchers to examine a variety of environmental science topics<sup>6,29,76–78</sup> . 

In summary, we introduce two datasets for the U.S.A., namely ONFIRE-FPA-FOD, and ONFIRE-MTBS, which are named in reference to their respective original sources. 

#### **Data Records** 

**Database structure.** ONFIRE data are available to the public through version-controlled releases of the database on Zenodo<sup>32</sup> , and all codes used in the development and validation of the dataset<sup>79</sup> are freely available, in line with the FAIR Guiding Principles<sup>80</sup> . ONFIRE is a 1° × 1° degree lat-long gridded dataset with, for each grid cell, the latitude and longitude of the center and the square metres burned per month. Each month’s data includes the total area in square metres for fires reported to start within that month. For instance, a fire that started on July 31 and burned for a month will be entirely reported in July. Data are stored in decimal degrees, GCS WGS84. The dataset contains fire estimates over the various recorded lengths, up to 2021, and spatial coverages (Table 1). The database is provided for each dataset and region in several formats: NetCDF<sup>81</sup> , RData<sup>82</sup> , and ASCII<sup>83</sup> . In total, we provide 21 files: 3 for each of the 5 regions, and two additional datasets are provided corresponding to the NFDB and NBAC sources for Canada, and the FPA-FOD and MTBS sources for the U.S.A. 

#### **technical Validation** 

The original records included in the database are provided by government and non-government agencies and as described in the previous section, have already been used individually in several regional studies (although not all together). We acknowledge, however, the potential limitations previously reported in national data<sup>84,85</sup> . These data commonly face various challenges, including periods of inaccessible or poor-quality data<sup>36,86</sup> , difficulties in estimating burned area from field observations<sup>13,85</sup> uncertainties arising from different fire reporting protocols between countries and/or protocol changes over time<sup>87</sup> , and high political controls on BA statistics<sup>84,88</sup> . Thus, even though they cannot clearly be considered error-free “ground truth”, these data represent the main source of authoritative fire histories available today, before and during the satellite era. In addition, users can evaluate the validity and accuracy of the original source for each regional dataset from its references (Table 1). It is also worth noting that here we provide BA data at a monthly scale and over a 1° grid resolution, therefore substantially reducing any uncertainties and noise that could be present at higher temporal and spatial resolutions. In addition, we provide information on the total BA, which is primarily influenced by the extent of large fires. These large fires are typically monitored due to their significant impacts (however it is worth noting that ONFIRE BA grid cells can also be affected by fires of less than 100 hectares<sup>89</sup> ). Also, while caution is necessary when relying solely on BA, it remains a useful tool for understanding the overall magnitude and spatial extent of fire events<sup>90</sup> as it provides a quantitative measure that can be easily compared across different fire events and regions. 

We also followed two different approaches to provide a quantitative assessment of the ONFIRE data: (1) we compared it with an independent satellite-based dataset, to examine the coherence among the datasets, and (2) we made use of the ONFIRE dataset to perform the same analysis of a previous study<sup>11</sup> , thus comparing the results. This two-step assessment process is crucial to ensure the integrity and quality of the ONFIRE data. 

Scientific **Data** | _(2024) 11:352_ | https://doi.org/10.1038/s41597-024-03141-2 

5 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



<!-- Start of picture text -->
a b<br>40�N<br>20�N<br> 0�<br>120�W  60�W 120�W  60�W<br>1 2.5 5 10 25 50 100 250 500 km 2<br><!-- End of picture text -->

**Fig. 2** Mean annual burned area (km<sup>2</sup> ) using data from various sources for Canada and the U.S.A. The different panels show the results obtained by combining different data sources: ( **a** ) ONFIRE-NBAC for Canada (1986– 2020) and ONFIRE-FPA-FOD (1992–2020) for the U.S.A.; ( **b** ) ONFIRE-NFDB for Canada (1986–2020) and ONFIRE-MTBS (1992–2020) for the U.S.A. 

**Comparison with an independent dataset.** We compared the monthly BA data from the ONFIRE dataset against the remotely sensed FireCCI51 data<sup>91</sup> , available for the period 2001–2020 at an original resolution of 250 m × 250 m. This is the most recently developed global BA dataset and complements existing global BA products using surface reflectance data from the Near Infrared (NIR) band of the MODIS instrument aboard the Terra satellite, alongside active fire detection information from the MODIS sensors on both Terra and Aqua satellites. When comparing our dataset with FireCCI51, it is important to recognize that although FireCCI51 is referenced as an independent dataset, for the Northern region of Australia, both FireCCI51 and NAFI datasets derive data from the same MODIS satellite sensor. Despite this commonality in data sources, the methodologies employed by each dataset are distinct. FireCCI51 utilizes a fully automated algorithm, whereas NAFI employs a method that combines automated analysis with visual checks and supervised classification. Consequently, despite the similarity in the input data, the significant differences in the processing approaches justify the characterization of this as an intercomparison analysis. In any case, we acknowledge a certain level of non-independence inherent in the data source, which must be carefully considered in our evaluation. A recent comparison amongst remotely sensed and inventory datasets for BA in Mediterranean Europe showed that FireCCI51 had the best agreement with EFFIS BA data overall<sup>16</sup> . To perform this comparison, a series of steps were undertaken. First, we downloaded the BA data at the grid resolution (0.25° × 0.25°) and we removed non-natural FireCCI51 BA data to align our analysis with official fire statistics, which typically exclude fires on agricultural land. The FireCCI51 dataset provides the sum of burned area for each land cover category. Therefore, we calculated the sum of the burned area by considering all land cover categories except for “cropland, rainfed”, “cropland, irrigated or post-flooding”, and “mosaic cropland (>50%) in line with other methodology”<sup>16</sup> . Then, the BA data were upscaled by summing all FireCCI51 grid points at 0.25° included in the corresponding 1° grid point of the ONFIRE dataset. Then, the mean annual aggregated BA series, calculated during the overlapping period, were compared. Finally, the temporal similarity of the monthly BA series was evaluated using Spearman correlation. 

There is a high degree of similarity between the mean annual area burned included in ONFIRE for U.S.A. and Canada (Fig. 2a,b). Indeed, the spatial (Spearman) correlation coefficient between the two patterns is 0.89 (p-value < 0.01). The total annual burned area in Canada averaged over the period 1986–2020 was approximately 17668 km<sup>2</sup> based on the ONFIRE-NBAC dataset, while the ONFIRE-NFDB dataset yielded an average value of 24125 km<sup>2</sup> . This represents a difference of 27% between the two datasets, which is similar to the findings of a study conducted in 2021<sup>54</sup> who reported a 23% difference considering fire data from 1986 to 2018. Higher similarity appears considering the annual BA in the U.S.A. averaged over the common period of 1992–2020. Specifically, the BA estimated using the ONFIRE-FPA-FOD dataset was found to be approximately 24,651 km<sup>2</sup> / year, and the ONFIRE-MTBS dataset yielded an estimate of around 24,744 km<sup>2</sup> /year, indicating a substantial agreement in the recorded values. It should be highlighted that in the northeastern United States, there are several regions without data in the ONFIRE-MTBS analysis, as indicated by the grey areas in Figs. 2b, 3b. This absence of data is likely attributable to the minimal fire activity in these regions, where the annual average burned area is generally less than 1 km², while the MTBS data in this area has a detection threshold, with the minimum identifiable burned area being over 2.02 km². The comparison of these data against FireCCI51 over the period 2001–2020 provides evidence of similarities among the datasets under examination (Fig. 3a–c). Specifically, the correlation between ONFIRE-NBAC + ONFIRE-FPA-FOD and FireCCI51 was 0.89, and between ONFIRE-NFDB + ONFIRE-MTBS and FireCCI51 was 0.89. The annual BA in Canada averaged over the common period 2001–2020, was quite similar among the three datasets: 16800, 22266, and 17525 km<sup>2</sup> /year for, 

6 

Scientific **Data** | _(2024) 11:352_ | https://doi.org/10.1038/s41597-024-03141-2 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



<!-- Start of picture text -->
a b c<br>40�N<br>20�N<br> 0�<br>120�W  60�W 120�W  60�W 120�W  60�W<br>1 2.5 5 10 25 50 100 250 500 km 2<br><!-- End of picture text -->

**Fig. 3** Mean annual burned area (km<sup>2</sup> ) averaged over the period 2001–2020 using data from various sources for Canada and the U.S.A. The different panels show the results obtained by combining different data sources: ( **a** ) ONFIRE-NBAC for Canada and ONFIRE-FPA-FOD for the U.S.A.; ( **b** ) ONFIRE-NFDB for Canada and ONFIRE-MTBS for the U.S.A.; ( **c** ) FireCCI51. Areas with no data are shown in grey. 



<!-- Start of picture text -->
a b<br>10�S<br>15�S<br>20�S<br>25�S<br>30�S<br>35�S<br>40�S<br>110�E 120�E 130�E 140�E 150�E 160�E 170�E 110�E 120�E 130�E 140�E 150�E 160�E 170�E<br>1 2.5 5 10 25 50 100 250 500 km 2<br><!-- End of picture text -->

**Fig. 4** Mean annual burned area (km<sup>2</sup> ) for the ONFIRE (panel a) and the FireCCI51 (panel b) datasets for Australia. Data for the period 2001–2020, or shorter depending on the data availability (see Tables 1, 2). Areas with no data are shown in grey. 

respectively, ONFIRE-NBAC, ONFIRE-NFDB, and FireCCI51. Again, lower differences have been found over the U.S.A., with 28660, 29997, and 30552 km<sup>2</sup> /year for ONFIRE-FPA-FOD, ONFIRE-MTBS, and FireCCI51. 

A good agreement was also observed between the annual BA averaged over the period 2001–2020, as estimated by the ONFIRE, and the BA from FireCCI51 datasets, for Australia, Chile, and Europe (Figs. 4–6). The spatial correlation is notably high over Australia, with a coefficient of 0.87 (p-value < 0.01), and the corresponding total annual BA values for the ONFIRE and FireCCI51 datasets are 469950 km<sup>2</sup> /year and 431892 km<sup>2</sup> /year, respectively. In Chile the level of agreement between the datasets is lower, with a spatial correlation coefficient of 0.62 (p-value < 0.01), and the averaged values of total annual BA are 1027 km<sup>2</sup> /year and 1848 km<sup>2</sup> /year for the ONFIRE and FireCCI51 datasets, respectively. In Europe, the spatial agreement is lower, with a correlation coefficient of 0.59 (p-value < 0.01), but the datasets provide similar estimated mean values, with the ONFIRE and FireCCI51 datasets yielding 3323 km<sup>2</sup> /year and 3498 km<sup>2</sup> /year, respectively of total annual BA. These differences may be attributed to various factors, including misinterpretations (remote sensing detects fires that are not fires), or possibly underreporting in national statistics. However, further investigation is required to gain a comprehensive understanding of these differences, which is beyond the scope of our analysis. Our primary goal here is to present these datasets in a standardised format, facilitating similar assessments in the future. In any case, these differences emphasise the importance of cautiously considering the underlying data sources and 

Scientific **Data** | _(2024) 11:352_ | https://doi.org/10.1038/s41597-024-03141-2 

7 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



<!-- Start of picture text -->
a b<br><!-- End of picture text -->



<!-- Start of picture text -->
60�N<br>50�N<br>40�N<br> 0� 20�E  0� 20�E<br>1 2.5 5 10 25 50 100 250 500 km 2<br><!-- End of picture text -->

**Fig. 5** Mean annual burned area (km<sup>2</sup> ) for the ONFIRE (panel a) and the FireCCI51 (panel b) datasets for Europe. Data for the period 2001–2020, or shorter depending on the data availability (see Tables 1, 2). Areas with no data are shown in grey. 

methodologies during the conduction of analyses with fire data. It also highlights the requirement for ongoing efforts to enhance data collection and standardisation practices. 

In addition, a correlation analysis was performed to measure the temporal similarity among the monthly burned area estimated by the different databases (Figs. 7, 8). A consistent positive significant correlation was found for the Canada region comparing ONFIRE-NBAC and ONFIRE-NFDB, and for the USA, comparing ONFIRE-FPA-FOD and ONFIRE-MTBS, both for the largest common periods and considering the 2001–2020 periods (Fig. 7a,b). The correlations between these data and the FireCCI51 are generally significant but lower. (Fig. 7c,d). 

ONFIRE and FireCCI51 data are also correlated for Australia, Chile, and Europe (Fig. 8). For the Australian region (Fig. 8a), a significant and positive correlation is observed almost everywhere, particularly in the north. It is important to note that this correlation may be partially influenced by the fact that both the ONFIRE and FireCCI51 datasets for northern territory are based on the same MODIS sensor (see the section “Technical Validation” for further details). That is, this shared data source can contribute to the observed agreement. For the Chile region (Fig. 8c), a highly significant correlation is restricted to areas where surface fire activity has been recorded in both datasets, indicating the strength and direction of the relationship of the burned area between ONFIRE and FireCCI51 is significant in these areas. In the European region (Fig. 8b), a significant and high correlation is observed where a high burned area is observed, especially in the Mediterranean and Eastern Europe (compare Fig. 5a,b, and Fig. 8b). Unlike the Chilean region, in Europe, even in areas with relatively low burned area values (such as Scandinavia), high correlations can be found. 

**Reproduction of earlier published results.** To assess the accuracy of ONFIRE data over a longer period, including years before the MODIS-era (early 2000s) we follow a similar approach inspired by a recent study<sup>92</sup> , which validated historical yields for major crops with climate data. The Canadian Fire Weather Index (FWI<sup>93</sup> ), a widely used index to assess the meteorological fire danger worldwide, exhibits a correlation with BA over most of the globe<sup>11,94</sup> . We extracted the FWI<sup>95</sup> data for the period 1979–2021 and available from the Copernicus Emergency Management Service<sup>96</sup> . In order to ensure consistency between the spatial resolution of the different datasets, the FWI data are also remapped from their original resolution (0.25° × 0.25°) to the 1° × 1° fire grid with a bilinear interpolation (using Climate Data Operators, CDO<sup>97</sup> ). Then, following a similar methodology employed in the study of Jones _et al_ .<sup>11</sup> , we calculate Spearman’s rank-order coefficient. The Spearman correlation coefficient was chosen due to the exponential relationship between climate (FWI) and fires (ONFIRE). 

This analysis is not intended to investigate the drivers of fires or discuss the importance of the FWI but to indirectly assess the ONFIRE datasets patterns using independent climate data that prior studies have shown to be related to fire variability. Despite FWI being the most commonly applied index for meteorological rating 

8 

Scientific **Data** | _(2024) 11:352_ | https://doi.org/10.1038/s41597-024-03141-2 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



<!-- Start of picture text -->
a b<br>20�S<br>30�S<br>40�S<br>50�S<br>80�W 75�W 70�W 65�W 60�W 80�W 75�W 70�W 65�W 60�W<br>1 2.5 5 10 25 50 100 250 500 km 2<br><!-- End of picture text -->

**Fig. 6** Mean annual burned area (km<sup>2</sup> ) for the ONFIRE (panel a) and the FireCCI51 (panel b) datasets for Chile. Data for the period 2001–2020, or shorter depending on the data availability (see Tables 1, 2). Areas with no data are shown in grey. 

fire danger worldwide<sup>70,98,99</sup> , it may not be the best predictor for explaining BA variability<sup>100,101</sup> . Previous studies<sup>11,94,100,102</sup> demonstrated that the connection between BA and FWI varies depending on the geographical location. The relationship is stronger in regions with high biomass, where the main constraint to fire is fuel moisture, rather than fuel availability. In contrast, BA shows less sensitivity to FWI in xeric grasslands and shrublands since these systems are more constrained by fuel productivity<sup>11</sup> . Jones _et al_ .<sup>11</sup> have shown that there is a positive and statistically significant correlation between monthly BA and monthly FWI in most regions of the world. Specifically, this relationship is particularly strong in Canadian and Alaskan forests, central Chile, the 

Scientific **Data** | _(2024) 11:352_ | https://doi.org/10.1038/s41597-024-03141-2 

9 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



<!-- Start of picture text -->
a b<br>40�N<br>20�N<br> 0�<br>c d<br>40�N<br>20�N<br> 0�<br>120�W  60�W 120�W  60�W<br>Statistical significant<br>0 0.2 0.4 0.6 0.8 1<br><!-- End of picture text -->

**Fig. 7** Spearman correlations between monthly estimates of burned area for the Canadian and U.S.A. regions, for different datasets and periods: ( **a** ) ONFIRE-NBAC against ONFIRE-NFDB in Canada for the period 1986– 2020, and ONFIRE-FPA-FOD against ONFIRE-MTBS in the U.S.A. for the period 1992–2020; ( **b** ) same as in ( **a** ) but for the more recent period 2001–2020; ( **c** ) ONFIRE-NBAC (Canada) and ONFIRE-FPA-FOD (U.S.A.) against FireCCI51; and ( **d** ) ONFIRE-NFDB (Canada) and ONFIRE-MTBS (U.S.A.) against FireCCI51 Study period in ( **b** ), ( **c** ), and ( **d** ) is 2001–2020. Areas with no data are shown in grey. 



<!-- Start of picture text -->
a b c<br>10�S<br>20�S<br>15�S 60�N<br>20�S<br>30�S<br>25�S 50�N<br>30�S 40�S<br>35�S 40�N<br>50�S<br>40�S<br>110�E 120�E 130�E 140�E 150�E 160�E 170�E  0� 20�E 80�W 75�W 70�W 65�W 60�W<br>Statistical significant<br>0 0.2 0.4 0.6 0.8 1<br><!-- End of picture text -->

**Fig. 8** Spearman correlation between monthly burned area estimates from the ONFIRE and the FireCCI51 datasets for Australia ( **a** ), Chile ( **b** ), and Europe ( **c** ), during the period 2001–2020 (or shorter, depending on the data availability; see Tables 1, 2 and Fig. 1). Areas with no data are shown in grey. 

Scientific **Data** | _(2024) 11:352_ | https://doi.org/10.1038/s41597-024-03141-2 

10 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



<!-- Start of picture text -->
a b c<br>40�N<br>20�N<br> 0�<br>120�W  60�W 120�W  60�W 120�W  60�W<br>Statistical significant<br>0 0.2 0.4 0.6 0.8 1<br><!-- End of picture text -->

**Fig. 9** Spearman correlation between monthly Fire Weather Index (FWI) and burned area (BA) as estimated by different datasets and periods: ( **a** ) ONFIRE-NBAC (1986–2020; Canada) and ONFIRE-FPA-FOD (U.S.A. 1992–2020); ( **b** ) ONFIRE-NFDB (1979–2021; Canada) and ONFIRE-MTBS (1984–2020; U.S.A.); ( **c** ) FireCCI51 (2001–2020). Areas with no data are shown in grey. 



<!-- Start of picture text -->
a b<br>10�S<br>15�S<br>20�S<br>25�S<br>30�S<br>35�S<br>40�S<br>110�E 120�E 130�E 140�E 150�E 160�E 170�E 110�E 120�E 130�E 140�E 150�E 160�E 170�E<br>Statistical significant<br>0 0.2 0.4 0.6 0.8 1<br><!-- End of picture text -->

**Fig. 10** Spearman correlation between monthly Fire Weather Index (FWI) and burned area (BA) in Australia, panel ( **a** ) for the period 1979–2021 (or shorter, Tables 1, 2) with ONFIRE data, and panel ( **b** ) for the 2001–2020 period with FireCCI51 data. Areas with no data or non-significant (p-value < 0.05) correlations are shown in grey. 

Mediterranean, north and southeast Australia, and the western U.S.A. Very similar results have been found here, as we detail in the following. 

The BA provided by the ONFIRE datasets and the FWI at the monthly scale (for the period 1979–2021 or shorter, depending on the data availability; see Tables 1, 2) are well correlated (Figures ranging from 9 to 12) and mostly resemble the assessment shown by Jones _et al_ .<sup>11</sup> . For the USA region, higher correlations over the western U.S.A. (of more than 0.75) are observed considering the ONFIRE-FPA-FOD (Fig. 9a) than considering the ONFIRE-MTBS data (Fig. 9b). Interestingly, Fig. 9c shows that FireCCI51 and ONFIRE data are on the same order of magnitude of correlations compared to FWI, except over the western U.S.A., where ONFIRE-FPA-FOD shows higher values. For Australia (Fig. 10a), a significant correlation between burned area (ONFIRE) and FWI data is shown in the north and southeast of the region. This may be explained as the limited availability of fuel plays a crucial role in shaping fire patterns in inland Australia. Conversely, in the forested regions of the eastern and southwestern coastlines, the dryness of the existing fuel further exacerbates the fire risk. Significant correlations are found in the European region (Fig. 11a), with particularly high values over the Iberian Peninsula, southern France, and Italy. In Chile (Fig. 12a), the ONFIRE data show a significant and high correlation practically throughout the region, with higher values in the central part of the country. In general, we have observed similar patterns when analysing the FireCCI51 data, albeit with slightly lower correlation values (Figs. 10b, 11b, 12b). 

Scientific **Data** | _(2024) 11:352_ | https://doi.org/10.1038/s41597-024-03141-2 

11 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



<!-- Start of picture text -->
a b<br>60�N<br>50�N<br>40�N<br> 0� 20�E  0� 20�E<br>Statistical significant<br>0 0.2 0.4 0.6 0.8 1<br><!-- End of picture text -->

**Fig. 11** Spearman correlation between monthly Fire Weather Index (FWI) and burned area (BA) in Europe, panel ( **a** ) for the period 1979–2021 with ONFIRE data, and panel ( **b** ) for the 2001–2020 period with FireCCI51 data. Areas with no data or non-significant (p-value < 0.05) correlations are shown in grey. 

#### **Usage Notes** 

**Informed user.** The use of the ONFIRE dataset comes with some caveats and users should be aware of the limitation of these data. While the original data that form this dataset represent the most comprehensive fire inventories in each considered region, these are not free from uncertainties and are not fully complete. Similar to other fire databases<sup>13,64,72,103</sup> , small fires are probably frequently missing and the minimum burned area for which a fire is recorded may not be consistent over the study period (as also noticed in other subregional datasets<sup>87</sup> . Nevertheless, since BA is generally dominated by large fires, the exclusion or inclusion of small fires (e.g., <1 ha) is not expected to significantly affect the total BA in most regions<sup>87</sup> . Also, it is important to note that in the ONFIRE dataset, certain datasets such as the MTBS and NFDB have inclusion thresholds for fires larger than 200 ha and 400 ha, respectively. While these thresholds exclude smaller fires, our comparative analysis across different datasets for northern America suggests that the exclusion of fires below these thresholds does not significantly impact the total BA estimations. This observation aligns with the general understanding that BA is predominantly influenced by larger fires, that are usually recorded, presumably because of their bigger impacts. The results presented here indicate that ONFIRE can be regarded as a reliable source of standardised information on historical fire activity, despite its inherent limitations. One notable advantage of ONFIRE is its ability to cover the longest period of monthly data compared to other available, and widely used, datasets in the scientific community. This addresses a longstanding request from the fire science community<sup>15</sup> and for the benchmarking of fire-enabled global vegetation models<sup>104</sup> . Additionally, ONFIRE complements existing databases<sup>36</sup> which only provide yearly data until 2000, and the FireCCILT11 dataset<sup>105</sup> which covers the period from 1982 to 2018 but is cautioned against applying in time series fire analyses<sup>106</sup> . Another strength of ONFIRE lies in its focus on wildland fires. The individual datasets constituting ONFIRE are curated to primarily include fires in natural landscapes, while fires over agricultural or other artificial surfaces are deliberately not included in the source data sets. This focus underscores the utility of ONFIRE in emphasising climate and vegetation-related fires, making it particularly valuable for assessments and projections of natural fire regimes. 

In any case, we recommend that end-users utilise the ONFIRE data, in tandem with other fire datasets, when available, to conduct a more thorough analysis. The growing awareness of the inherent limitation in earth observation products now relies mainly on uncertainty assessments obtained by comparing existing datasets<sup>107,108</sup> . Consequently, users are encouraged to contemplate the above limits when planning analysis based on ONFIRE. That is, fire datasets may have different levels of accuracy, coverage, and temporal resolution, so it is essential to evaluate their suitability for the specific research purpose carefully and to compare them with other available datasets when possible. An important aspect to take into account is spatial/temporal resolution. If the goal is, for instance, to study the relationship between climate and burned area, a grid resolution of 1° would likely be 

Scientific **Data** | _(2024) 11:352_ | https://doi.org/10.1038/s41597-024-03141-2 

12 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 



<!-- Start of picture text -->
a b<br>20�S<br>30�S<br>40�S<br>50�S<br>80�W 75�W 70�W 65�W 60�W 80�W 75�W 70�W 65�W 60�W<br>Statistical significant<br>0 0.2 0.4 0.6 0.8 1<br><!-- End of picture text -->

**Fig. 12** Spearman correlation between monthly Fire Weather Index (FWI) and burned area (BA) in Chile, panel ( **a** ) for the period 1979–2021 with ONFIRE data, and panel ( **b** ) for the 2001–2020 period with FireCCI51 data. Areas with no data or non-significant (p-value < 0.05) correlations are shown in grey. 

sufficient, as it provides a good balance between spatial resolution and computational efficiency. However, studies on specific regions or land use types may require a higher-resolution grid. 

**Nature of a living dataset.** Finally, we would like to acknowledge that the data contained within the ONFIRE dataset embody the collective work of fire mapping, rescue, and maintenance and required an enormous amount of time, effort, and resources to generate. ONFIRE has harmonised all these different datasets but does not claim their generation. When reusing (and when realistically feasible), we advise users to cite both ONFIRE 

Scientific **Data** | _(2024) 11:352_ | https://doi.org/10.1038/s41597-024-03141-2 

13 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

and references to the original data to ensure proper attribution. Owing to the proven utility of the regional data source that composed this dataset, a specific common repository for these data may be of significance to the research community. This database will increase the reuse of this curated information for various applications. Version-controlled releases of the dataset, additional references, and metadata can be found on Zenodo (https:// zenodo.org/record/8289245). Despite our best efforts to collect authoritative data and assess them in a common framework, it may be possible that we have overlooked errors in the data sets. We strongly encourage the users to report any issues or omissions by contacting the authors. Our intention is that any erroneous information will be updated in future releases of the dataset. Likewise, we encourage the community to contribute new data for other regions of the world so that the database can continue to grow, with the hope that ONFIRE will remain a useful resource for years to come. 

#### **Code availability** 

All codes used in the development and validation of the ONFIRE Dataset<sup>32</sup> are freely available on Zenodo<sup>79</sup> : https://zenodo.org/records/10512198. 

Received: 31 August 2023; Accepted: 14 March 2024; 

Published: xx xx xxxx 

#### **References** 

1. Pausas, J. G. & Keeley, J. E. Wildfires as an ecosystem service. _Frontiers in Ecology and the Environment_ **17** , 289–295 (2019). 

2. Pyne, S. The Ecology of Fire. _Nature Education Knowledge_ **3** (10), 30 (2010). 

3. Senande-Rivera, M., Insua-Costa, D. & Miguez-Macho, G. Spatial and temporal expansion of global wildland fire activity in response to climate change. _Nat Commun_ **13** , 1208 (2022). 

4. Bowman, D. Wildfire science is at a loss for comprehensive data. _Nature_ **560** , 7–7 (2018). 

5. Pausas, J. G. & Keeley, J. E. Wildfires and global change. _Frontiers in Ecology and the Environment_ **19** , 387–395 (2021). 

6. Abatzoglou, J. T. & Williams, A. P. Impact of anthropogenic climate change on wildfire across western US forests. _Proceedings of the National Academy of Sciences_ **113** , 11770–11775 (2016). 

7. Bilbao, B. _et al_ . Incendios forestales. En: Adaptación frente a los riesgos del cambio climático en los países iberoamericanos – Informe RIOCCADAPT. in 459–524 (2020). 

8. Fernandez-Anez, N. _et al_ . Current Wildland Fire Patterns and Challenges in Europe: A Synthesis of National Perspectives. _Air, Soil and Water Research_ **14** , 11786221211028185 (2021). 

9. Forkel, M. _et al_ . Emergent relationships with respect to burned area in global satellite observations and fire-enabled vegetation models. _Biogeosciences_ **16** , 57–76 (2019). 

10. Chuvieco, E. _et al_ . Human and climate drivers of global biomass burning variability. _Science of The Total Environment_ **779** , 146361 (2021). 

11. Jones, M. W. _et al_ . Global and Regional Trends and Drivers of Fire Under Climate Change. _Reviews of Geophysics_ **60** , e2020RG000726 (2022). 

12. Zheng, B. _et al_ . Record-high CO2 emissions from boreal fires in 2021. _Science_ **379** , 912–917 (2023). 

13. Short, K. C. Sources and implications of bias and uncertainty in a century of US wildfire activity data. _Int. J. Wildland Fire_ **24** , 883–891 (2015). 

14. Chuvieco, E. _et al_ . Historical background and current developments for mapping burned area from satellite Earth observation. _Remote Sensing of Environment_ **225** , 45–64 (2019). 

15. Mouillot, F. _et al_ . Ten years of global burned area products from spaceborne remote sensing—A review: Analysis of user needs and recommendations for future developments. _International Journal of Applied Earth Observation and Geoinformation_ **26** , 64–79 (2014). 

16. Turco, M., Herrera, S., Tourigny, E., Chuvieco, E. & Provenzale, A. A comparison of remotely-sensed and inventory datasets for burned area in Mediterranean Europe. _International Journal of Applied Earth Observation and Geoinformation_ **82** , 101887 (2019). 

17. Campagnolo, M. L., Libonati, R., Rodrigues, J. A. & Pereira, J. M. C. A comprehensive characterization of MODIS daily burned area mapping accuracy across fire sizes in tropical savannas. _Remote Sensing of Environment_ **252** , 112115 (2021). 

18. Rodrigues, J. A. _et al_ . How well do global burned area products represent fire patterns in the Brazilian Savannas biome? An accuracy assessment of the MCD64 collections. _International Journal of Applied Earth Observation and Geoinformation_ **78** , 318–331 (2019). 

19. Bowman, D. M. J. S. _et al_ . Vegetation fires in the Anthropocene. _Nat Rev Earth Environ_ **1** , 500–515 (2020). 

20. Royé, D. _et al_ . Wildfire burnt area patterns and trends in Western Mediterranean Europe via the application of a concentration index. _Land Degradation & Development_ **31** , 311–324 (2020). 

21. Canadell, J. G. _et al_ . Multi-decadal increase of forest burned area in Australia is linked to climate change. _Nat Commun_ **12** , 6921 (2021). 

22. Wang, X. _et al_ . Projected changes in fire size from daily spread potential in Canada over the 21st century. _Environ. Res. Lett._ **15** , 104048 (2020). 

23. McWethy, D. B. _et al_ . Landscape drivers of recent fire activity (2001–2017) in south-central Chile. _PLOS ONE_ **13** , e0201195 (2018). 24. Pozo, R. A., Galleguillos, M., González, M. E., Vásquez, F. & Arriagada, R. Assessing the socio-economic and land-cover drivers of wildfire activity and its spatiotemporal distribution in south-central Chile. _Science of The Total Environment_ **810** , 152002 (2022). 

25. González, M. E., Gómez-González, S., Lara, A., Garreaud, R. & Díaz-Hormazábal, I. The 2010–2015 Megadrought and its influence on the fire regime in central and south-central Chile. _Ecosphere_ **9** , e02300 (2018). 

26. Doerr, S. H. & Santín, C. Global trends in wildfire and its impacts: perceptions versus realities in a changing world. _Philosophical Transactions of the Royal Society B: Biological Sciences_ **371** , 20150345 (2016). 

27. McLauchlan, K. K. _et al_ . Fire as a fundamental ecological process: Research advances and frontiers. _Journal of Ecology_ **108** , 2047–2069 (2020). 

28. Pinto, M. M., Libonati, R., Trigo, R. M., Trigo, I. F. & DaCamara, C. C. A deep learning approach for mapping and dating burned areas using temporal sequences of satellite images. _ISPRS Journal of Photogrammetry and Remote Sensing_ **160** , 260–274 (2020). 

29. Alizadeh, M. R. _et al_ . Warming enabled upslope advance in western US forest fires. _Proceedings of the National Academy of Sciences_ **118** , e2009717118 (2021). 

30. Goldammer, J. G. _GLOBAL FOREST FIRE ASSESSMENT 1990–2000 - FRA WP 55_ . (2001). 

31. Ambrosia, V. G., San Miguel-Ayanz, J., Boschetti, L., Giglio, L. & Field, R. D. The Group on Earth Observation (GEO) Global Wildfire Information System (GEO-GWIS). **2019** , NH12A-02 (2019). 

32. Gincheva, A. & Turco, M. ONFIRE dataset: Monthly Gridded Burned Area data. _Zenodo_ https://doi.org/10.5281/zenodo.8289245 (2023). 

Scientific **Data** | _(2024) 11:352_ | https://doi.org/10.1038/s41597-024-03141-2 

14 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

33. Sixth Assessment Report — IPCC. https://www.ipcc.ch/assessment-report/ar6/. 

34. ATLAS/reference-grids at main · SantanderMetGroup/ATLAS. _GitHub_ https://github.com/SantanderMetGroup/ATLAS/tree/ main/reference-grids. 

35. Kobziar, L. N. Fire on Earth: An Introduction. 2014. By A.C. Scott, D.M.J.S. Bowman, W.J. Bond, S. J. Pyne, and M.E. Alexander. Wiley Blackwell, Hoboken, New Jersey, USA 434 pages. Paperback, US$89.95; hardcover, US$149.95. ISBN 978-1-119-95356-2. _fire ecol_ **10** , 88–91 (2014). 

36. Mouillot, F. & Field, C. B. Fire history and the global carbon budget: a 1° × 1° fire history reconstruction for the 20th century. _Global Change Biology_ **11** , 398–420 (2005). 

37. Northern Australian Fire Information. https://www.firenorth.org.au/nafi3/. 

38. Fisher, R. Fire extent mapping: procedures, validation and website application. in (2015). 

39. Jacklyn, P. _Extending NAFI Fire History Mapping_ . (2017). 

40. Russell-Smith, J. _et al_ . Bushfires ‘down under’: Patterns and implications of contemporary Australian landscape burning. _International Journal of Wildland Fire_ **16** , (2007). 

41. Reynolds, S. Flammable Australia. Fire Regimes, Biodiversity and Ecosystems in a Changing World [Book Review]. _Northern Territory Naturalist_ **24** , 89–91 (2013). 

42. Murphy, B. _et al_ . Fire regimes of Australia: A pyrogeographic model system. _Journal of Biogeography_ **40** , 1048–1058 (2013). 

43. Lindenmayer, D. B. & Taylor, C. New spatial analyses of Australian wildfires highlight the need for new fire, resource, and conservation policies. _Proceedings of the National Academy of Sciences_ **117** , 12481–12485 (2020). 

44. Amiro, B. D. _et al_ . Direct carbon emissions from Canadian forest fires, 1959–1999. _Can. J. For. Res._ **31** , 512–525 (2001). 

45. Stocks, B. J. _et al_ . Large forest fires in Canada, 1959–1997. **108** , **D1** , FFR5, 1–12 (2003). 

46. Flannigan, M., Logan, K., Amiro, B., Skinner, W. & Stocks, B. Future Area Burned in Canada. _Climatic Change_ **72** , 1–16 (2005). 47. Parisien, M.-A. _et al_ . Spatial patterns of forest fires in Canada, 1980–1999. _International Journal of Wildland Fire_ **15** , 361–374 (2006). 

48. Boulanger, Y., Parisien, M.-A. & Wang, X. Model-specification uncertainty in future area burned by wildfires in Canada. _International journal of wildland fire_ **27** , 164–175 (2018). 

49. Wang, X. _et al_ . Projected changes in daily fire spread across Canada over the next century. _Environ. Res. Lett._ **12** , 025005 (2017). 

50. Hanes, C. C. _et al_ . Fire-regime changes in Canada over the last half century. **49** , 256–269 (2019). 51. Hall, R. J. _et al_ . Generating annual estimates of forest fire disturbance in Canada: the National Burned Area Composite. **2020** , 878–891 (2020). 

52. Skakun, R., Whitman, E., Little, J. M. & Parisien, M.-A. Area burned adjustments to historical wildland fires in Canada. _Environ. Res. Lett._ **16** , 064014 (2021). 

53. Skakun, R. _et al_ . Extending the National Burned Area Composite Time Series of Wildfires in Canada. _Remote Sensing_ **14** , 3050 (2022). 

54. Kolden, C. A., Lutz, J. A., Key, C. H., Kane, J. T. & van Wagtendonk, J. W. Mapped versus actual burned area within wildfire perimeters: Characterizing the unburned. _Forest Ecology and Management_ **286** , 38–47 (2012). 

55. Meddens, A., Kolden, C. & Lutz, J. Detecting unburned areas within wildfire perimeters using Landsat and ancillary data across the northwestern United States. _Remote Sensing of Environment_ **186** , 275–285 (2016). 

56. Urrutia‐Jalabert. Climate variability and forest fires in central and south‐central Chile - Urrutia‐Jalabert - 2018 - Ecosphere - Wiley Online Library. https://esajournals.onlinelibrary.wiley.com/doi/full/10.1002/ecs2.2171 (2018). 

57. de la Barrera, F., Barraza, F., Favier, P., Ruiz, V. & Quense, J. Megafires in Chile 2017: Monitoring multiscale environmental impacts of burned ecosystems. _Science of The Total Environment_ **637–638** , 1526–1536 (2018). 

58. Gómez-González, S. _et al_ . Temperature and agriculture are largely associated with fire activity in Central Chile across different temporal periods. _Forest Ecology and Management_ **433** , 535–543 (2019). 

59. Úbeda, X. & Sarricolea, P. Wildfires in Chile: A review. _Global and Planetary Change_ **146** , 152–161 (2016). 

60. Miranda, A. _et al_ . Evidence-based mapping of the wildland-urban interface to better identify human communities threatened by wildfires. _Environ. Res. Lett._ **15** , 094069 (2020). 

61. Sarricolea, P. _et al_ . Recent wildfires in Central Chile: Detecting links between burned areas and population exposure in the wildland urban interface. _Science of The Total Environment_ **706** , 135894 (2020). 

62. San-Miguel-Ayanz, J. _et al_ . Comprehensive Monitoring of Wildfires in Europe: The European Forest Fire Information System (EFFIS). in _Approaches to Managing Disaster - Assessing Hazards, Emergencies and Disaster Impacts_ . https://doi.org/10.5772/28441 (IntechOpen, 2012). 

63. Overview - NUTS - Nomenclature of territorial units for statistics - Eurostat. https://ec.europa.eu/eurostat/web/nuts/. 64. Turco, M. _et al_ . Decreasing Fires in Mediterranean Europe. _PLOS ONE_ **11** , e0150663 (2016). 65. Urbieta, I. R. _et al_ . Fire activity as a function of fire–weather seasonal severity and antecedent climate across spatial scales in southern Europe and Pacific western USA. _Environ. Res. Lett._ **10** , 114013 (2015). 

66. Turco, M. _et al_ . Skilful forecasting of global fire activity using seasonal climate predictions. _Nature Communications_ **9** , 2718 (2018). 67. Short, K. C. Spatial wildfire occurrence data for the United States, 1992–2018 [FPA_FOD_20210617] (5th Edition). https://doi. org/10.2737/RDS-2013-0009.5. 

68. Short, K. C. A spatial database of wildfires in the United States, 1992–2011. _Earth System Science Data_ **6** , 1–27 (2014). 69. Calkin, D. E., Thompson, M. P. & Finney, M. A. Negative consequences of positive feedbacks in US wildfire management. _Forest Ecosystems_ **2** , 9 (2015). 

70. Jolly, W. M. _et al_ . Climate-induced variations in global wildfire danger from 1979 to 2013. _Nat Commun_ **6** , 7537 (2015). 71. Balch, J. K. _et al_ . Human-started wildfires expand the fire niche across the United States. _Proceedings of the National Academy of Sciences_ **114** , 2946–2951 (2017). 

72. Syphard, A. D., Keeley, J. E., Pfaff, A. H. & Ferschweiler, K. Human presence diminishes the importance of climate in driving fire activity across the United States. _Proceedings of the National Academy of Sciences_ **114** , 13750–13755 (2017). 

73. Home | MTBS. https://www.mtbs.gov/. 

74. Eidenshink, J. _et al_ . A Project for Monitoring Trends in Burn Severity. _Fire Ecology_ **3** , (2007). 

75. Picotte, J. _et al_ . Changes to the Monitoring Trends in Burn Severity program mapping production procedures and data products. _Fire Ecology_ **16** , 16 (2020). 

76. Publications | MTBS. https://www.mtbs.gov/publications. 

77. Large wildfire trends in the western United States, 1984–2011 - Dennison - 2014 - Geophysical Research Letters - Wiley Online Library. https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2014GL059576. 

78. Crockett, J. & Westerling, A. Greater Temperature and Precipitation Extremes Intensify Western U.S. Droughts, Wildfire Severity, and Sierra Nevada Tree Mortality. _Journal of Climate_ **31** , 341–354 (2018). 

79. Gincheva, A., Royé, D., Torres Vázquez, M. Á. & Turco, M. ONFIRE Dataset: Development and Validation Codebase. _Zenodo_ https://doi.org/10.5281/zenodo.8289245 (2024). 

80. The FAIR Guiding Principles for scientific data management and stewardship | Scientific Data. https://www.nature.com/articles/ sdata201618. 

81. Unidata | NetCDF. https://www.unidata.ucar.edu/software/netcdf/. 

82. Grolemund, G. D. _Loading and Saving Data in R | Hands-On Programming with R._ 

Scientific **Data** | _(2024) 11:352_ | https://doi.org/10.1038/s41597-024-03141-2 

15 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

83. Comma-separated values. _Wikipedia_ (2024). 

84. Belhadj-Khedher, C. _et al_ . A Revised Historical Fire Regime Analysis in Tunisia (1985–2010) from a Critical Analysis of the National Fire Database and Remote Sensing. _Forests_ **9** , 59 (2018). 

85. Pereira, M., Malamud, B., Trigo, R. & Alves, P. The History and Characteristics of the 1980–2005 Portuguese Rural Fire Database. _Nat. Hazards Earth Syst. Sci_ **11** , 3343–3358 (2011). 

86. Koutsias, N. _et al_ . On the relationships between forest fires and weather conditions in Greece from long-term national observations (1894–2010). _International Journal of Wildland Fire_ **22** , 493–507 (2013). 

87. Turco, M., Llasat, M. C., Tudela, A., Castro, X. & Provenzale, A. Brief communication Decreasing fires in a Mediterranean region (1970&ndash;2010, NE Spain). _Natural Hazards and Earth System Sciences_ **13** , 649–652 (2013). 

88. _Fire, Climate Change, and Carbon Cycling in the Boreal Forest_ . vol. 138 (Springer, New York, NY, 2000). 

89. Ramo, R. _et al_ . African burned area and fire carbon emissions are strongly impacted by small fires undetected by coarse resolution satellite data. _Proceedings of the National Academy of Sciences_ **118** , e2011160118 (2021). 

90. Resco de Dios, V., Yao, Y., Cunill Camprubí, À. & Boer, M. M. Fire activity as measured by burned area reveals weak effects of ENSO in China. _Nat Commun_ **13** , 4316 (2022). 

91. Lizundia-Loiola, J., Otón, G., Ramo, R. & Chuvieco, E. A spatio-temporal active-fire clustering approach for global burned area mapping at 250 m from MODIS data. _Remote Sensing of Environment_ **236** , 111493 (2020). 

92. Iizumi, T. & Sakai, T. The global dataset of historical yields for major crops 1981–2016. _Sci Data_ **7** , 97 (2020). 

93. Van Wagner, C. E. _Development and Structure of the Canadian Forest Fire Weather Index System_ . vol. 35 (1987). 

94. Bedia, J. _et al_ . Global patterns in the sensitivity of burned area to fire-weather: Implications for climate change. _Agricultural and Forest Meteorology_ **214–215** , 369–379 (2015). 

95. Vitolo, C. _et al_ . ERA5-based global meteorological wildfire danger maps. _Sci Data_ **7** , 216 (2020). 

96. Fire danger indices historical data from the Copernicus Emergency Management Service (Deprecated 2023-06-14). https://cds. climate.copernicus.eu/cdsapp#!/dataset/cems-fire-historical?tab=overview. 

97. Schulzweida, U. CDO User Guide. _Zenodo_ https://doi.org/10.5281/zenodo.3539275 (2019). 

98. Flannigan, M. _et al_ . Global wildland fire season severity in the 21st century. _Forest Ecology and Management_ **294** , 54–61 (2013). 

99. Field, R. D. _et al_ . Development of a Global Fire Weather Database. _Natural Hazards and Earth System Sciences_ **15** , 1407–1423 (2015). 

100. Abatzoglou, J. T., Williams, A. P., Boschetti, L., Zubkova, M. & Kolden, C. A. Global patterns of interannual climate-fire relationships. _Global Change Biology_ https://doi.org/10.1111/gcb.14405 (2018). 

101. Boer, M. M., Dios, V. R. D., Stefaniak, E. Z. & Bradstock, R. A. A hydroclimatic model for the distribution of fire on Earth. _Environ. Res. Commun._ **3** , 035001 (2021). 

102. Silva, P. S., Bastos, A., Libonati, R., Rodrigues, J. A. & DaCamara, C. C. Impacts of the 1.5 °C global warming target on future burned area in the Brazilian Cerrado. _Forest Ecology and Management_ **446** , 193–203 (2019). 

103. Westerling, A. Increasing western US forest wildfire activity: Sensitivity to changes in the timing of spring. _Philosophical Transactions of the Royal Society B: Biological Sciences_ **371** , 20150178 (2016). 

104. Hantson, S. _et al_ . The status and challenge of global fire modelling. _Biogeosciences_ **13** , 3359–3375 (2016). 

105. Otón, G., Pereira, J. M. C., Silva, J. M. N. & Chuvieco, E. Analysis of Trends in the FireCCI Global Long Term Burned Area Product (1982–2018). _Fire_ **4** , 74 (2021). 

106. Giglio, L. & Roy, D. P. Assessment of satellite orbit-drift artifacts in the long-term AVHRR FireCCILT11 global burned area data set. _Science of Remote Sensing_ **5** , 100044 (2022). 

107. Terrestrial ecosystems from space: a review of earth observation products for macroecology applications - Pfeifer - 2012 - Global Ecology and Biogeography - Wiley Online Library. https://onlinelibrary.wiley.com/doi/full/10.1111/j.1466-8238.2011.00712.x. 

108. Turco, M. _et al_ . DROP: A Probabilistic Drought Monitoring Tool. _Bulletin of the American Meteorological Society_ **101** , 991–994 (2020). 

#### **Acknowledgements** 

A.G. thanks to the Ministerio de Ciencia, Innovación y Universidades of Spain for Ph.D. contract FPU19/06536. A.G., M.A.T-V., S.J., and M.T. acknowledges the support of the ONFIRE project, grant PID2021-123193OB-I00, funded by MCIN/AEI/10.13039/501100011033 and by “ERDF A way of making Europe”. A.P. and M.M. acknowledge the support of the EU project FireEUrisk, grant no. 101003890. E.C. and F.M. were supported by the European Space Agency FireCCI project. F.M. was supported by FireuRisk European Union H2020 Grant Agreement no. 101003890. G.V., M.B., A.P., and M.M. acknowledge the support of the European Union - NextGenerationEU in the framework of the National Biodiversity Future Center of Italy. M.M.B. acknowledges funding from the New South Wales Government (NSW Bushfire and Natural Hazards Research Centre) and the Australian Research Council (DP 220100795). M.E.G acknowledges research support provided by ANID/ FONDECYT N° 1231573 and ANID/FONDAP 15110009; COD 1522A0001. R.L. was supported by FAPERJ (Grant E-26/200.329/2023) and CNPQ (Grant 311487/2021-1). R.M.T. was supported by the Portuguese Fundação para a Ciência e a Tecnologia (FCT) I.P./MCTES, through project DHEFEUS (https://doi. org/10.54499/2022.09185.PTDC). S.J. acknowledges funding by the MCI/AEI Ramón y Cajal Grant Reference RYC2020-029993-I. M.T. acknowledges funding by the Spanish Ministry of Science, Innovation, and Universities through the Ramón y Cajal Grant Reference RYC2019-027115-I. 

#### **author contributions** 

A.G. and M.T. conceived the idea, designed, and performed the study. All authors contributed datasets and reviewed and approved the manuscript. 

#### **Competing interests** 

The authors declare no competing interests. 

#### **additional information** 

**Correspondence** and requests for materials should be addressed to A.G. 

**Reprints and permissions information** is available at www.nature.com/reprints. 

**Publisher’s note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

16 

Scientific **Data** | _(2024) 11:352_ | https://doi.org/10.1038/s41597-024-03141-2 

www.nature.com/scientificdata 

www.nature.com/scientificdata/ 

**Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/. 

© The Author(s) 2024 

**andrina Gincheva**<sup>**1**</sup><sup>~~✉~~</sup> **, Juli G. �ausas**<sup>**2**</sup> **, Andrew Edwards**<sup>**3**</sup> **, Antonello �rovenzale**<sup>**4,5**</sup> **, Artemi Cerdà**<sup>**6**</sup> **, Chelene Hanes**<sup>**7**</sup> **, Dominic Royé**<sup>**8**</sup> **, Emilio Chuvieco**<sup>**9**</sup> **, Florent Mouillot**<sup>**10**</sup> **, Gabriele Vissio**<sup>**4,5**</sup> **, Jesús Rodrigo**<sup>**11**</sup> **, Joaquin Bedía**<sup>**12,13**</sup> **, John T. Abatzoglou**<sup>**14**</sup> **, José María Senciales González**<sup>**15**</sup> **, Karen C. Short**<sup>**16**</sup> **, Mara Baudena**<sup>**5,17**</sup> **, Maria Carmen Llasat**<sup>**18**</sup> **, Marta Magnani**<sup>**4,5**</sup> **, Matthias M. Boer**<sup>**19,20**</sup> **, Mauro E. González**<sup>**21,22**</sup> **, Miguel Ángel Torres-Vázquez**<sup>**1**</sup> **, �aolo Fiorucci**<sup>**23**</sup> **, �eter Jacklyn**<sup>**3**</sup> **, Renata Libonati**<sup>**24**</sup> **, Ricardo M. Trigo**<sup>**25**</sup> **, Sixto Herrera**<sup>**26**</sup> **, Sonia Jerez**<sup>**1**</sup> **, Xianli Wang**<sup>**27**</sup> **& Marco Turco**<sup>**1**</sup> 

1Regional Atmospheric Modelling (MAR) Group, Department of Physics, Regional campus of international excellence campus Mare nostrum (ceiR), University of Murcia, Murcia, Spain.<sup>2</sup> centro de investigaciones sobre Desertificación, Spanish National Research Council (CIDE-CSIC), Valencia, Spain.<sup>3</sup> Darwin centre for Bushfire Research, charles Darwin University, Darwin, northern territory, Australia.<sup>4</sup> institute of Geosciences and earth Resources - National Research Council of Italy (CNR-IGG), Turin, Italy.<sup>5</sup> national Biodiversity future center, Palermo, italy.<sup>6</sup> Soil Erosion and Degradation Research Group, Department of Geography, Valencia University, Valencia, Spain.<sup>7</sup> Great Lakes forestry centre, canadian forest Service, natural Resources canada, Sault Ste. Marie, Ontario, canada.<sup>8</sup> climate Research foundation (fic), Madrid, Spain.<sup>9</sup> Universidad de Alcalá, environmental Remote Sensing Research Group, Department of Geology, Geography and the environment, Alcalá de Henares, Spain.<sup>10</sup> UMR cefe, Université de Montpellier, cnRS, ePHe, iRD, Montpellier, france.<sup>11</sup> Departamento de Análisis Geográfico Regional y Geografía física, facultad de filosofía y Letras, campus Universitario de cartuja, Universidad de Granada, Granada, Spain.<sup>12</sup> Departamento Matemática Aplicada y ciencias de la computación (MAcc), Universidad de cantabria, Santander, Spain.<sup>13</sup> Grupo de Meteorología y computación, Universidad de cantabria, Unidad Asociada al cSic, Santander, Spain.<sup>14</sup> Management of complex Systems, University of california, Merced, USA.<sup>15</sup> Department of Geography, University of Málaga, Málaga, Spain.<sup>16</sup> Department of Agriculture, forest Service, Missoula fire Sciences Laboratory, Missoula, Montana, USA.<sup>17</sup> institute of Atmospheric Sciences and climate, national Research council of Italy (CNR- ISAC), Torino, Italy.<sup>18</sup> GAMA, Department of Applied Physics, Universitat de Barcelona, Barcelona, Spain. 19Hawkesbury institute for the environment, Western Sydney University, Penrith, nSW, Australia. 20NSW Bushfire and natural Hazards Research centre, Richmond, nSW, Australia.<sup>21</sup> instituto de conservación, Biodiversidad y Territorio, Facultad de Ciencias Forestales y Recursos Naturales, Universidad Austral de Chile, Valdivia, Chile.<sup>22</sup> center for Climate and Resilience Research (CR2), Santiago, Chile.<sup>23</sup> ciMA Research foundation, Savona, italy.<sup>24</sup> instituto de Geociências, Universidade federal do Rio de Janeiro, Rio de Janeiro, Brazil.<sup>25</sup> instituto Dom Luiz (iDL), faculdade de ciências, Universidade de Lisboa, Lisbon, Portugal.<sup>26</sup> Applied Mathematics and computer Science Department Universidad de cantabria, Santander, Spain.<sup>27</sup> northern forestry centre, canadian forest Service, natural Resources canada, edmonton, AB, canada.<sup>✉</sup> e-mail: andrina@um.es 

Scientific **Data** | _(2024) 11:352_ | https://doi.org/10.1038/s41597-024-03141-2 

17 
