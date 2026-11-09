---
title: An integrated wildfire event database for improved fire science research for the continental United States, 1992–2021
authors:
- Kasischke, Eric S.
- French, Nancy H. F.
year: '2026'
journal: Earth System Science Data Discussions
doi: 10.5194/essd-2026-660
tags:
- dataset
- spatial data quality
- united states
- wildfire
zotero_key: 57MFJ62G
item_type: journalArticle
url: https://openalex.org/W7223091393
source_url: 'unpaywall: https://essd.copernicus.org/preprints/essd-2026-660/essd-2026-660.pdf'
fulltext_status: fulltext
synced: '2026-11-09'
---

# An integrated wildfire event database for improved fire science research for the continental United States, 1992–2021

## Abstract

Abstract. This paper describes a wildfire event dataset that was initially created by mining information from three existing national datasets that have provided the foundation for numerous wildfire studies in the continental United States over the past two decades. The goal for creating this dataset was to address existing uncertainties and ambiguities in the the existing datasets by using information from regional reports and datasets and searches of the world wide web. Wildfire events not contained in the three datasets were added as new records. Approaches were developed to harvest information for records where there were significant differences in the size of the same fire from different datasets. Specific attention was paid to fires named as complexes, those contained multiple fires, smaller events that had merged to form larger events, events that had joined, events where the size was incorrectly reported, and duplicate events. This new wildfire event dataset provides more accurate information on the number and sizes of individual wildfires and improved information for quantifying annual area burned and changes in extreme wildfire activity over a three-decade period (1992 to 2021) at different spatial scales. Results are presented that illustrate the differences in wildfire characteristics developed from the new dataset and those currently being used by the fire science community.

## Full text

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 1 **An integrated wildfire event database for improved fire science** 2 **research for the continental United States, 1992-2021** 

- 3 

- 4 Eric S. Kasischke<sup>1</sup> , Nancy H. French<sup>1</sup> 

- 5 1Michigan Tech Research Institute, Ann Arbor, MI 48014, United States of America 

- 6 _Correspondence to_ : Eric S. Kasischke (ekasisch@umd.edu) 

- 7 

1 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 8 **Abstract.** This paper describes a wildfire event dataset that was initially created by mining 

- 9 information from three existing national datasets that have provided the foundation for 

- 10 numerous wildfire studies in the continental United States over the past two decades. The goal 

- 11 for creating this dataset was to address existing uncertainties and ambiguities in the the existing 

- 12 datasets by using information from regional reports and datasets and searches of the world wide 

- 13 web. Wildfire events not contained in the three datasets were added as new records. 

- 14 Approaches were developed to harvest information for records where there were significant 

- 15 differences in the size of the same fire from different datasets. Specific attention was paid to 

- 16 fires named as complexes, those contained multiple fires, smaller events that had merged to 

- 17 form larger events, events that had joined, events where the size was incorrectly reported, and 

- 18 duplicate events. This new wildfire event dataset provides more accurate information on the 

- 19 number and sizes of individual wildfires and improved information for quantifying annual area 

- 20 burned and changes in extreme wildfire activity over a three-decade period (1992 to 2021) at 

- 21 different spatial scales. Results are presented that illustrate the differences in wildfire 

- 22 characteristics developed from the new dataset and those currently being used by the fire 

- 23 science community. 

- 24 

2 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 



- 25 

# **1 Introduction** 



- 26 This paper describes the development of a wildfire event dataset that integrated information found in 

- 27 fire management agency reports, tables, and data repositories with satellite-derived wildfire event 28 information. This new dataset provides a comprehensive accounting of wildfire events (unplanned 29 landscape fires) for three decades (1992 to 2021) for the continental United States (CUS), which 30 includes the 48 contiguous states plus Alaska. It provides data valuable for assessing wildfire 31 occurrence and trends, and regional spatial and interannual patterns in wildfire activity. This integrated 32 dataset is being used in studies to assess the influence of extreme wildfires or mega fires (fires greater 33 than 10,000 ha in size following Linley et al., 2022) on trends in wildfire burned area, fire regimes, and 

- 34 smoke generation at regional and sub-continental scales. 

- 35 Since the late 2000s, the U.S. Forest Service (USFS) sponsored efforts to compile information from fire 36 management reports obtained from multiple sources, resulting in the publication of five versions of a 37 wildfire occurrence dataset described by Short (2014, 2017, 2021, 2022). This dataset contains records 38 of fire events of all sizes, covering the period from 1992 to 2020. These datasets have greatly facilitated 39 wildfire studies in the United States (Table S1). Recently, a new wildfire event dataset was released, 40 which was developed from wildfire events submitted through the US National Incident Management 41 System Incident Status Summary (ICS-209) forms (ICS dataset), which typically includes events larger 42 than 100 acres, but also includes smaller events where incident management teams were assigned. This 43 dataset includes records from 1999 to 2020 and has been used in a small number of studies (Table S1). 

- 44 Because methods for measuring, estimating, and reporting wildfire size have changed over time and 45 varies between fire management agencies, identification of mega fires in the USFS and ICS datasets 46 can be challenging. First, under many circumstances groups of fire events have been managed as 47 complexes, where the area burned from all the fires has been reported in a single record. The ICS dataset 48 contains more complex events than the FS20 datasets, where in some years it contains a complex plus 49 the fires within the complex as separate records. Second, fire events that had merged were often reported 50 as multiple individual events or records in fire management reports and datasets. Third, in many 51 instances, the sizes for larger wildfires are estimated, especially in rural areas where the fires are 52 managed by private landowners or local fire departments, which has resulted in under or over estimation 53 of fire size. And fourth, in regions with a high percentage of private landownership, many wildfires go 54 unreported. Finally, it is important to note that the use of GPS and GIS technologies for the mapping of 55 fire perimeters and estimating their size has increased over the three-decade timespan of the database, 56 resulting in improved size and location accuracy and a decrease in the uncertainties associated with 57 mapping wildfire occurrence, size and duration. 

3 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 58 The creation of the MTBS fire perimeter dataset (1984 to 2024) has benefited numerous studies of 

- 59 larger wildfires in the CUSA (Table S1). The MTBS program defines large fires as those greater than 60 1,000 ac (405 ha) in the western U.S. and 500 ac (202 ha) in the eastern U.S. This dataset has been 61 widely used because fire perimeters have been mapped with a consistent methodology using primarily 62 Landsat satellite imagery beginning in 1984 combined with Sentinel 2 imagery beginning in 2015. The 63 approach used to create MTBS products is based on the contrast between burned and unburned 64 vegetation using a combination of Landsat and Sentinel 2 spectral bands, providing an accurate and 65 consistent means of mapping burned vegetation under most circumstances (Sparks et al., 2015). While 66 the MTBS approach is recognized for producing accurate depictions of burned area in most situations, 67 as will be shown in this paper, there were a small number of events where the algorithm and approaches 68 used by the MTBS program did not accurately map burned area. In addition, the MTBS archive of 69 wildfire records is incomplete for several reasons. First, the unavailability of Landsat data was high in 70 some years, especially during the 1980s and 1990s (Short, 2015). And second, the production of MTBS 71 wildfire perimeters is based on the identification of the location of events from fire management records 72 and thus is dependent on the completeness of these records. 

- 73 While most studies in Table S1 were based on using a single dataset, a limited number used data from 74 two datasets. There were two studies that used the USFS and MTBS datasets separately to calculate 75 wildfire characteristics, where two studies integrated information from them. Three studies integrated 76 the ICS and MTBS datasets. 

- 77 Here, the results from the first part of ongoing research to assess unplanned fire (wildfire) 78 activity trends in the CUSA are presented: the development of an event-based wildfire dataset for the 79 CUSA for a three-decade period (1992 to 2021). In developing this integrated wildfire dataset, we 80 endeavored to correct known inconsistencies and issues associated with the various information 81 sources. The objectives for this activity were to: (1) integrate wildfire event data from multiple sources 82 (including data from the MTBS program) into a single dataset; (2) identify additional wildfires for 83 individual MTBS records through the visual interpretation of MTBS perimeters; (3) resolve 84 uncertainties and ambiguities in wildfire records reported as complexes; and (4) for matched records 85 (those containing information from the MTBS program and fire management sources) determine the 86 reasons for significant differences in the sizes reported by the two sources.. 

- 87 This new dataset has been named the integrated Wildfire Event Dataset (iWED). In this paper, the 88 approaches used to obtain and develop the information contained in the records in this dataset are first 89 described. Examples are presented to illustrate how the number and sizes of wildfire records were 90 altered during the five phases of the dataset development. The average burned area derived using events 91 from the iWED are compared to those calculated using wildfire records from the fire occurrence dataset 92 of Short (2022) as well as area burned contained in the annual reports published by the National 

4 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 93 Interagency Coordination Center (NICC) (NICC 2002-2020). The potential importance of the iWED is 94 then illustrated through examination of alterations in the number and area burned in mega and mega95 plus fires in different CUSA regions. 

- 96 

- 97 **2 Technical Approach** 

- 98 The iWED contains information for wildfire events ≥ 100 ha (247 ac) in size for the 49 states within 99 the continental U.S. from 1992 to 2021. Figure 1 provides a flowchart summarizing the datasets, tools, 

- 100 and study phases used during its development. Sect. 2.1 summarizes the variables for each record 101 contained in the iWED and its availability. Sect. 2.2 discusses the datasets and information sources used 102 for the dataset development. The web-based tools and common analysis approaches used are presented 103 in Sect. 2.3. The iWED was developed during the five phases presented in Sect. 2.4. A number of steps 104 used in the different phases used the same procedure. To avoid repetition, these common procedures 105 are presented in full the first time they are discussed and thereafter referred to by a procedure number 106 (Table 1). The comparisons of average burned area developed from the iWED to area burned from other 107 sources as well as an assessment of variations in extreme wildfire activity (mega and mega-plus fires) 108 are presented in Sect. 2.5. 

109 

110 

# **2.1 Data Availability and Dataset Contents** 

- 111 The integrated Wildfire Event Database, version 1 (iWED v1) was published in the fall of 2025 and is 112 available from the Oak Ridge National Laboratory Distributed Active Archive Center for 113 Biogeochemical Dynamics (Kasischke et al., 2025). Improvements to iWED v1 were made through the 114 addition of events from the ICS dataset, refinement of the reclassification of MTBS Unknown records 115 as Prescribed Fires, and further identification of MTBS wildfire records containing multiple perimeters. 116 These improvements are contained in version 2 of the iWED, which is currently under review for 117 publication (Kasischke et al. 2026, in review). 

- 118 The iWED v1 is held in a CSV format and contains 19 variables for each of the 45,612 records contained 119 in the dataset (see Table 2 in Kasischke et al., 2025). Variable 1 is a unique number for each record. 120 Variables 2 to 8 provide information related to the development of the iWED. An important feature of 121 iWED is the retention of information about the sources used to develop information for each record. 122 Variable 2 is an alpha-numeric code where the number identifies one of the seven primary sources 123 where the information for a record was obtained (Table 3 in Kasischke et al., 2026) The letters for this 124 variable identify records named as complexes (cx) or that were determined to be duplicates (d). The 

5 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 125 alpha-numeric codes contained in variable 3 provide a summary of the processes used to change 126 information for a record or provide additional information for the record. Variable 3 consists of thirty127 one separate alpha-numeric codes, where the number identifies twelve information sources and the 128 letters designate specific changes that occurred (Table 4 in Kasischke et al., 2026). Over 34% of the 129 records (15,742) contain additional information in variable 2. During Phase 2 of the iWED development 130 (Sect. 2.4), 1,308 MTBS events were found that contained multiple perimeters. Variables 4, 5, and 6 131 provide the number of small, medium, and large perimeters, respectively, found for these MTBS 132 records. Variables 7 and 8 provide links to notes that identify unique attributes for a record as well 133 provide discussions on the steps used to develop additional information for a specific record. These 134 notes are provided in Table 5 as separate CSV file (see Kasischke et al., 2025). In version 2 of the 135 iWED, there are 1,092 notes associated with 6,833 records. Variables 9 to 15 contain data imported 136 from fire management datasets and reports (including fire name, year, state, start day of year, end day 137 of year, ignition source, and size in acres), and Variables 16 to 18 contain data imported from the MTBS 138 dataset (MTBS perimeter size in acres, event name, event identification number) where variable 19 139 contains the MTBS fire type (Prescribed, Unknown, Wildfire) for each event and identifies those 140 Unknown or Prescribed Fires which were determined likely to be a wildfire or prescribed fire based on 141 visual interpretation of MTBS perimeter shape (Sect. 2.3) and Unknown fires that were most likely 142 Prescribed fires based on their locations. In addition, variable 19 identifies MTBS Wildfires that were 143 identified as a Prescribed Fire in a report and MTBS Unknown and Prescribed Fires that were matched 144 with a fire management event. 

- 145 The information obtained for each wildfire event contained in the iWED included the latitude and 146 longitude for the event (when available), which is typically the start location for fire management events 147 and the centroid of the perimeter(s) for an MTBS event. These positional data will be provided in a 148 subsequent version of the iWED, to be released once the authors have submitted a publication that uses 149 this information. 

- 150 

# **2.2 Data and Information Sources** 

- 151 There are three types of records in the iWED. Those where the information comes from fire 152 management records and sources (FM records), those where the information comes from the MTBS 153 dataset (MTBS records), and those where the information comes from both fire management and MTBS 154 source (matched records). Information on individual fire management events contained in the iWED 155 came from seven sources: (1) records contained in the US Forest Service fire occurrence dataset for 156 1992-2015 (Short, 2017; hereafter referred to as the FS15 dataset); (2) records contained in the US 157 Forest Service fire occurrence dataset for 1992-2018 (Short, 2021; hereafter referred to as the FS18 158 dataset); (3) records contained in the US Forest Service fire occurrence dataset for 1992-2020 (Short, 159 2022; hereafter referred to as the FS20 dataset); (4) records contained in the ICS dataset, which was 

6 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 160 created from wildfire events mined from the US National Incident Management System for 1999–2020 161 (St Denis et al., 2023; hereafter referred to as the ICS dataset); (5) records contained in datasets and 162 information contained annual reports published by state, regional, and national governmental 163 organizations (see Table 1 in Kasischke et al., 2026, which provides the URL locations for these 164 sources); (6) information harvested from daily or weekly incident management situation reports 165 (ISMRs) published online by the National Interagency Fire Center (NIFC) (NIFC, 1992 to 2021) and 166 the Alaska Interagency Coordination Center (AICC) (AICC, 1992 to 2021); and (7) data or information 167 harvested from documents or media reports found through searches of the world wide web. For each 168 fire event, information obtained from these sources included fire name, year of the event, location 169 (either latitude/longitude or a description of the location), fire start and end date, ignition source, and 170 fire size. 

- 171 The MTBS data used in this study were obtained from the Monitoring Trends in Burn Severity program 172 (Eidenshink et al., 2006; Picotte et al., 2020). Three separate MTBS products were used: (a) fire event 173 information obtained from the MTBS geographic information system (GIS) database (MTBS, 2026a) 174 (fire name, fire size, MTBS identification number, start date, latitude, longitude, and fire type); (b) fire 175 perimeters contained in the MTBS GIS database (MTBS, 2026a); and (c) false-color Landsat images 176 contained in pdf files produced by the MTBS program (MTBS 2026b). 

- 177 In addition to the fire perimeters in the MTBS dataset, four other datasets were used in analyzing 178 individual events and complexes of wildfires: (a) fire perimeter datasets produced by WFIGS 179 (https://data-nifc.opendata.arcgis.com/datasets/nifc::wfigs-current-interagency-fire-perimeters/about 180 last accessed on 15 June 2026), NIFS/GeoMAC (http://data-nifc.opendata.arcgis.com last accessed on 181 15 June 2026), and CalFire (https://www.fire.ca.gov/what-we-do/fire-resource-assessment182 program/fire-perimeters (last accessed on 15 June 2026); (b) the MODIS burned area product dataset 183 (MCD64A1 v.6.1; Giglio et al., 2018); (c) the Landsat BAECV product (Hawbaker et al., 2020); and 184 (d) the archive of fine-resolution, color aerial photographs available through Google Maps 185 (https://www.google.com/maps last accessed on 15 June 2026). 

- 186 

- 187 **2.3 Web-Based Applications and Visual Interpretation of Imagery** 

- 188 In addition to the worldwide web-based search engines used to access and download datasets and 

- 189 government and media-based reports, four other web-based applications were used during the 190 development of the iWED: 

- 191 1. The Wildland Fire Emissions Inventory System (WFEIS) website 192 (https://wfeis.mtri.org/calculator last accessed on 15 June 2026) was used for a variety of analyses 

7 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 193 during the creation of the iWED. The WFEIS was originally designed to calculate carbon and smoke194 product emissions from wildland and prescribed fires in the United States (French et al., 2014; Billmire 195 et al., 2025). The WFEIS is a web-based geospatial Application Programming Interface (API) that 196 integrates geospatial information on wildfire or prescribed area burned, fuel loads, and weather 

- 197 conditions to calculate biomass consumed and emission products using fuel consumption models 198 developed by the U.S. Forest Service (Prichard et al., 2006). The WFEIS user has the option to select 199 the source of burned area information, geographic area of interest, and time period of interest (where 200 the available years are based on the source of the area burned data). Alternatively, the user can select a 201 specific event from a fire perimeter dataset using the assigned name or ID number of an event. The 202 WFEIS contains fire perimeters from the MTBS, WFIGS, NFIS/GeoMAC and CalFire datasets and 203 burned area pixels created from processing of Landsat and/or MODIS data. In this application, 204 information from multiple sources are overlaid onto a base map provided by OpenStreetMap 205 (https://www.openstreetmap.org/#map=5/38.00/-101.34 last accessed on 15 Jun 2026), and provides 206 the capability to: (a) visualize the location of a fire event perimeter; (b) identify geographic features 207 within and adjacent to a perimeter; and (c) display and visually compare perimeters from multiple 208 sources as well as burned area pixels from MODIS and Landsat. 

209 

- 210 2. The OpenStreetMap website was used to display the latitude and longitude positions of fire 211 management events. Through a comparison of the WFEIS and OpenStreetMap displays, it could be 212 determined if the position of a fire management event was within an MTBS perimeter (Procedure 1 in 213 Table 1). 

- 214 3. The Google Maps website (https://www.google.com/maps last accessed on 15 June 2026) was 215 used in several ways. First, the latitude and longitude for many wildfire events were not provided, where 216 instead, a written description of the event’s location was given (typically in miles and direction from a 217 geographic feature). By locating the geographic feature (most commonly a city or town) in Google 218 Maps and using its Measure tool, a latitude and longitude could be obtained (Procedure 2 in Table 1). 219 Second, the Google Maps website was used to obtain recent, fine-resolution, color aerial photography 220 for some fire events, as well as to identify distinct topographic features (e.g., buttes, ridges, steep slopes, 221 canyons) within a fire perimeter. These images were used to identify landscape features which may 222 have contributed to the incorrect mapping of burned area in specific MTBS events (Procedure 3 in Table 223 1). 

- 224 4. The Google AI mode has recently been added to the Google search engine 225 (https://www.google.com/?zx=1779714057006 last accessed on 30 July 2026). When the ICS dataset 226 was added to the iWED, this mode was used to harvest information on all events named as complexes 

8 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 227 in the ICS dataset, where the names, sizes, or numbers of fires were identified for a number these events. 

- 228 The Google AI mode was used during a final quality control check on other events that were named as 

- 229 complexes for which information had not been previously found, as well as events for which positions 230 were not available. 

- 231 While digital processing of data from airborne and satellite remote sensors is widely used in analyses 

- 232 of geospatial data, visual interpretation of remotely-sensed imagery and other data products (e.g., 233 topographic maps and fire perimeter shapes) was an important analysis tool used during the 234 development of the iWED. Visual interpretation was used for: 

- 235 1. Identifying MTBS records or events that contained multiple fire perimeters. For MTBS events 236 containing multiple perimeters, the fraction of the total MTBS event size in each perimeter was 237 estimated using visual interpretation, which in turn was used to calculate each perimeter’s size 238 (Procedure 4 in Table 1). 

- 239 2. Distinguishing likely wildfires from planned (prescribed) fires based on MTBS perimeter 240 shape; 

241 

- 242 3. Matching of MTBS perimeters with fire management events through comparison of the 243 perimeter and fire event locations (Procedure 1 in Table 1); 

- 244 4. Identifying merged or joined fires; 

- 245 5. Comparing MTBS to fire management perimeters and/or burned area pixels to assess the 246 accuracy of MTBS fire size; and 

- 247 6. Identifying events where the algorithm used by MTBS algorithm did not correctly map the 248 burned area. 

- 249 More detailed discussions on the use of visual interpretation in the creation of the iWED are presented 

- 250 in Sect. 2.4.2, and examples are presented in the online Supplement to this article. 

- 251 

# **2.4 Dataset Development Phases** 

- 252 Each phase in the development of the iWED involved a set of steps designed to identify 253 additional wildfire events for entry into the iWED (Phases 1 and 2), resolve uncertainties that existed 254 in events named as complexes (Phase 3), and identify reasons for differences between fire management 255 and MTBS sizes in matched records (Phases 4 and 5). 

9 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





256 **2.4.1 Phase 1** 

257 The initial phase of iWED development was to combine and reconcile information from existing fire 258 management records. 

259 **_Step 1_** - The very first step in the creation of the iWED was to populate the dataset with events from 260 primary fire management sources. A preliminary version of the iWED was created in 2016 prior to the 261 release of the FS18 and FS20 datasets. Data from fires ≥ 100 ha (247 ac) were extracted from records 262 contained in the FS15 dataset, including name, year of fire, latitude, longitude, state, start date, end date, 263 ignition source, and fire size (in acres). These events represented the initial FM records contained in the 264 iWED. When the FS18 and FS20 datasets became available, comparisons were made to identify events 265 not already in the iWED, which were then added as new records. The primary source for a record in the 266 (Variable 2) in the iWED was updated if the fire event was contained in either the FS18 or FS20 dataset. 

267 **_Step 2_** - Wildfire events not contained in the iWED were identified through searches of records 268 contained in other regional and national datasets as well published reports and web pages. New events 269 were identified based on a combination of event name, size, start date and location and added to the 270 dataset as new FM records. Wildfire event data for 2021 was based on events identified in fire 271 management reports and datasets. Information for new events were used to add FM records to the 272 iWED. The names of some events that were Unnamed in the FS15/18/20 datasets found in these other 273 datasets were substituted for those records and were identified in Variable 3 of the dataset by the alpha274 numeric ‘3n’. 

275 **_Step 3_** - As part of ongoing research, the daily/weekly incident management situation reports (IMSRs) 276 from NICC were reviewed to create a daily burned area variables for each event in the iWED for all 277 western ecoregions, including the western Great Plains, but excluding Alaska. During this process, 278 additional fire events were identified that were not contained in the iWED. During this review, all events 279 > 1,000 ac not contained in the iWED were added to the dataset as new records. Based on the results of 280 this review, the IMSRs for the remaining areas in the Great Plains were reviewed, and additional events 281 > 1,000 ac were added to the iWED. For areas east of the Mississippi River, additional fires > 500 ac 282 were added to the iWED. These thresholds were selected because smaller wildfires were under-reported 283 in the IMSRs during the 1990s. One issue in obtaining information from these additional events was 284 that the IMSRs did not contain latitude and longitude information. Instead, many of these events 285 contained a written description of the fire’s location, typically the direction and distance from a town 286 or city. This information was used to obtain a latitude and longitude by using Google Maps. (Procedure 287 2, Table 1) Information on a fire’s location that was not provided in an IMSR was often obtained in a 288 report found through a search of the world wide web. Finally, some of the unnamed fires in the FS20 289 dataset were named in the IMSRs as well as other sources. These names were substituted for these 

10 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 290 events in the iWED and the source for these names noted in variable 3 of the dataset using the alpha291 numeric ‘4n’. 

292 **_Step 4 –_** The decision to add wildfire events from the ICS dataset came after version 1 of the iWED 293 was published (Kasischke et al., 2025). At this point, some of the ICS wildfire events had already been 294 obtained from spreadsheets that were available from the website hosting these events. The ICS 295 contained a more complete set of information, including more accurate latitude and longitude 296 information. The events from the ICS dataset that were added as new FM records were identified by 297 the number 12 in Variable 2 of the dataset. The primary source (variable 2) for ICS events that had 298 previously been obtained from the website was also changed. There were unnamed FS20 events that 299 were matched with ICS events. The ICS names were substitute for these events and the source for these 300 names noted in variable 3 of the dataset using the alpha-numeric code ‘12n’. 

301 **_Step 5_** - During the importing of fire management events from other sources, it became apparent that 302 there were differences in the approaches used to report wildfire complexes. Groups of wildfires were 303 often managed as complexes, where each complex was given a name. In the daily/weekly IMSRs, 304 information (including size) was frequently only reported for the complex and not for the individual 305 fires in the complex. In fire management datasets, information was sometimes reported only for the 306 complex and at other times for individual fires within the complex or a combination of the two. After 307 importing events from other sources, it became clear that overlapping or duplication of events had 308 occurred. An example is when the FS20 dataset contained a single record named a complex where the 309 individual events were contained in a regional fire management dataset or report. To resolve this issue, 310 every record named as a complex was assigned the letters ‘cx’ along with the numeric designator 311 denoting the primary source for the data in Variable 2 of the dataset. Events named as complexes were 312 carefully reviewed during Phase 3 of the dataset development (Sect. 2.4.3). 

- 313 

# **2.4.2 Phase 2** 

314 This phase focused on incorporating events contained in the MTBS dataset. First, all MTBS Wildfire, 315 Unknown, and a limited number of Prescribed Fire events were added to iWED as new records. Next, 316 MTBS events that could matched with the fire management record entered during Phase 1 were 317 identified, resulting in the creation of matched records. Finally, unmatched MTBS records with an 318 Unknown and Prescribed Fire type were examined to identify those that could be reclassified as 319 Wildfires or Prescribed Fires. 

320 **Background** - The standard procedure used by the MTBS program to create a fire perimeter from 321 satellite remote sensing data is to select Landsat and Sentinel 2 scenes based on the locations of wildfire 

- 322 and prescribed fire events from fire management reports (Eidenshink et al. 2006). For most events, the 

11 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 323 MTBS analyses resulted in a single perimeter that was associated with a single fire management or 324 prescribed fire event. Many MTBS Wildfire and Prescribed Fire records included additional perimeters 325 from fires that were immediately adjacent to the targeted event. In addition, multiple perimeters for an 326 MTBS record occurred when a fire jumped a natural (e.g., river, reservoir, lake) or man-made barriers 327 (e.g., road or railroad right-of-ways). A large number MTBS records with an Unknown type were 328 produced when analysts identified additional fire perimeters in the Landsat/Sentinel 2 scenes used for 329 mapping known wildfires and prescribed fires. This latter process also produced MTBS records that 330 contained multiple perimeters. Finally, a set of MTBS events were generated as part of a USGS program 

- 331 to map burned area in the Flint Hills ecoregion of eastern Kansas and Oklahoma, MTBS perimeters 332 were generated from 1986 to 2007 for the entire region 333 (https://burnseverity.cr.usgs.gov/products/prairieFires last accessed on 19 February 2026). While most 334 of the records from this effort were assigned an Unknown type by the MTBS program, the 311 records 335 generated in 2011 were assigned a Prescribed Fire type and were used in developing the iWED. 

- 336 **_Step 1_** – All MTBS events typed as Wildfire, Wildland Use Fire, Unknown, and Prescribed Fires from 337 2011 in the Flint Hills region were added to the iWED as new records, where Wildland Use Fires were 338 relabeled as Wildfires. Information that was imported included MTBS fire name, latitude, longitude, 339 fire start date, MTBS ID number, and the dates of the pre-fire and post-fire Landsat scenes that were 340 used to generate the MTBS products. 

341 **_Step 2 –_** The MTBS records were then matched with fire management records through comparison of 342 fire names, sizes, locations (latitude and longitude), and start date, resulting in the creation of a single, 343 matched record. For many records, the FS15/18/20 datasets provided the names and MTBS 344 Identification Numbers for events that were matched with fire management events, which aided in the 345 matching of events in the iWED. It was found that the FS15/18/20 records contained two categories of 346 MTBS events. The first category contains a non-hyphenated identifier containing 21 characters. The 347 firsttwo letters of this identifier are letters identifying the state where the fire centroid was found with 348 the latter 19 characters being  numbers based on the latitude, longitude and the start date for the fire. 349 The second category of MTBS events contained a hyphenated identifier based on different land 350 management agencies. The publicly available MTBS dataset (MTBS 2026a) only contained the first 351 category of MTBS events. Two procedures were used to confirm the matching of MTBS and fire 352 management records when an uncertainty existed. First, the WFEIS was used to display the MTBS 353 perimeter and OpenStreetMap to display the position of the fire management event. A match was 354 confirmed using Procedure 1 (Table 1) or by using the WFEIS to simultaneously display the MTBS 355 perimeters and other perimeters from the CalFire, NIFS/GeoMAC, and WFIGS datasets, where a match 356 was confirmed when there was close agreement between the two perimeters (Procedure 5 in Table 1). 357 There were 41 MTBS Prescribed Fire records and 240 MTBS Unknown records that were matched with 

12 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 358 a fire management record, indicating that the fire type for these records was incorrect. These records 359 were assigned a new variable 19 in the iWEDas either Prescribed-WF or Unknown-WF. There were 17 360 MTBS wildfire records from Alaska that were matched with prescribed fire events found in an AICC 361 IMSR. It was concluded these events had been given an incorrect type by the MTBS program and were 362 assigned a new variable 19 in the iWED as a Wildfire-PR type and identified in Variable 7 (notes). 

- 363 **_Step 3_** - There were 869 MTBS Wildfire records that could not be matched with a fire management as 364 well as 5,428 unmatched MTBS Unknown/Prescribed Fire records, prompting further examination 365 during Phase 2 of the development of the iWED. Reviewing the location of all unmatched MTBS 366 Unknown/Prescribed fire records revealed that a large number of these occurred in areas where MTBS 367 Prescribed Fire perimeters were common. These areas included National Wild Refuges, National 368 Forests, state conservation and game managent areas, state forests, military reserves, and state lands 369 containing wetlands. All unmatched MTBS Unknown records that were found in areas with a high 370 number of MTBS Prescribed fires were given an Unknown-PR type (1,800 events). A significant 371 number of the remaining unmatched events (1,836 out of 3,628 events) occurred in the Flint Hills region 372 of eastern Kansas and Oklahoma where prescribed burning is the prevalent source of landscape-scale 373 fire activity (Short 2014) (see Sect. S4 in the online Supplement to this article). 

- 374 **_Step 4 -_** By reviewing the shape and general landscape features of the perimeters for a large number of 375 MTBS Wildfire and Prescribed Fire records, a set of characteristics were compiled that were used to 376 identify the likely type of an Unknown MTBS event (see Sect. S1 in the online Supplement to this 377 article). The first step was to view the perimeter shape for each unmatched, Unknown MTBS record 378 using the WFEIS, and based on the characteristics of the perimeter’s shape, reclassify them as a 379 Wildfire, Prescribed Fire, or Unknown. The 311 MTBS Prescribed Fire records from the Flint Hills 380 region were also viewed. Variable 19 of the iWED dataset contains information on the MTBS fire type, 381 including those MTBS fires initially given an Unknown type that were reclassified as Wildfires 382 (Unknown-WF) or Prescribed (Unknown-PR) fires using visual interpretation. This step included the 383 review of the 3,628 unmatched MTBS Unknown/Prescribed fires. 

- 384 **_Step 5_** - When viewed using the WFEIS, it was discovered that many of the unmatched MTBS Unknown 385 records contained multiple fire perimeters. The existence of multiple perimeters was identified by 386 assigning ‘7mu’ to variable 3 in the dataset as well as noting the number of large, medium, and small 387 perimeters in Variables 4 to 6 of the dataset. The identification of perimeter size was based on a relative, 388 not absolute scale. Events with a single perimeter were assigned  a ‘7s’ to variable 3. For MTBS records 389 with multiple perimeters, Procedure 4 (Table 1) was used to calculate each perimeter’s size. Perimeters 390 greater than 100 ha (247 acres) were added to the iWED as a new record, where the MTBS names were 391 altered by adding “Fire 1”, “Fire 2”, etc. to the name. Because of the discovery that many of the 

13 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 392 unmatched MTBS Unknown records contained multiple perimeters, all unmatched MTBS Wildfire 393 records were also visually interpreted to identify those with multiple perimeters. 

- 394 

- 395 

# **2.4.3 Phase 3** 

- 396 Five steps were used during Phase 3 to assess the sources for uncertainties in records named as 397 complexes during Phase 1: 

- 398 **_Step 1 –_** For each unmatched fire management record named as a complex, searches of fire management 399 databases, reports, and the world wide web (Procedure 6 in Table 1) were carried out. For some events 400 where the names and sizes of the fires found for the complex were found where the total area for the 401 individual fires matched the size in the record. For these events, the individual fires were added to the 402 iWED as new records and the record for the complex event removed. In other events, the total area for 403 the fires in the complex was different than the complex size from the record. In these cases, the 404 individual fires were added as new records, where the complex size was allocated to the fires in 405 proportion to their reported sizes  (Procedure 7 in Table 1). The record for the complex event was 406 removed from the dataset. For some records, only the names or numbers of the fires within the complex 407 were found. For these events, the complex record was replaced in the iWED by multiple records (equal 408 to the number of fires within the complex) whose sizes were calculated as the complex size divided by 409 the number of fires. For complexes where the number of fires was identified with no names, the 410 individual fires were renamed by adding “Fire 1”, “Fire 2”, etc. to the complex name. For smaller 411 complexes, this approach sometimes resulted in events < 247 acres in size. These events were noted 412 column 7 of the dataset and retained in the iWED to allow calculation of total area burned by including 413 the smaller events from the complete FS20 dataset. 

- 414 **_Step 2_** – Viewing a matched record using the WFEIS often revealed a fire contained a single perimeter 415 whose MTBS size was nearly equal to the fire management size. Because of the similarity in size, it 416 was concluded that the complex contained a single fire. These records were identified by the alpha417 numeric code 7s in variable 3 as well as in variable 7 (notes) of the iWED. 

418 **_Step 3_** – Viewing MTBS event of a matched record using the WFEIS sometimes revealed a fire 419 contained multiple perimeters, where for some events Procedure 6 (Table 1) identified the names and/or 420 number of fires in the complex. Procedure 4 (Table 1) was used to estimate the size of each perimeter. 421 In addition to Procedures 1 and 5 (Table 1) were used to match fire management records with the 422 additional MTBS perimeters. 

14 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 423 **_Step 4_** – It was sometimes found for matched records that the MTBS size was considerably larger than 424 the fire management size, where viewing the MTBS event revealed this fire had a single perimeter. 

- 425 Using Procedures 1 and 8 (Table 1), it was determined that the MTBS event resulted from the merging 426 or joining of multiple fires. (Merging occurs when two fires join when both fires are still active and 427 growing. Joining occurs when two fires join after the end date for one of the fires.) Whether or not 428 multiple fires had merged or joined was determined by one of three methods. First, for some records, 429 the merging of fire events was reported in the NICC or AICC IMSRS, in other fire management reports, 430 or reports found in searches of the world wide web (Procedure 9 in Table 1). Second, if Procedure 6 431 (Table 1) identified the multiple fire management perimeters within an MTBS perimeter and the WFEIS 432 contained MODIS burned pixels that matched the perimeters, the dates for these pixels were used to 433 determine whether the fires had joined or merged (Procedure 10 in Table 1). For all other events, the 434 start and end dates for the fire management events were used, where the evidence the fires had joined 435 and not merged was when the end date for one fire was prior to the start date for the other fire (Procedure 436 11 in Table 1). 

- 437 **_Step 5_** – For some records where there was significant difference between the FS20 and MTBS size, a 438 review of other reports (including NICC and AICC IMSRs, other fire management reports, or reports 439 found through a search of the world wide web) found a fire management size for the event that was 440 closer to the MTBS. For some records, fire management perimeters were found that matched the MTBS 441 perimeter size, or Landsat or MODIS burned area pixels were used to confirm that the fire management 442 size was incorrect (Procedure 12 in Table 1). For these records, the fire management size was adjusted 443 by substituting the reported size or perimeter size for the FS20 size. For each event, this adjustment was 444 noted by adding an alpha-numeric designation in Variable 3, with a number identifying the source of 445 the information followed by ‘ad’. 

446 

# **2.4.4 Phase 4** 

447 Phase 4 focused on matched records where the difference in MTBS size was greater than 30% of the 448 size of the fire management event. The reasons for these differences were determined following Steps 449 2 to 5 in Sect. 2.4.3 plus an additional step. 

- 450 **_Step 1 -_** When multiple perimeters were found for an MTBS event using the WFEIS and it was 451 determined that the fire management size represented two or more of the perimeters. For these events, 452 the fire management sizes for the perimeters were calculated using Procedure 7 (see Table 1). For these 453 records, the individual fires were renamed by adding “Fire 1”, “Fire 2”, etc. to the fire name, adding 454 records to the iWED. 

455 

# **2.4.5 Phase 5** 

15 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 456 While fire management and MTBS sizes for the majority of matched records were within 15% of each 457 other, there remained a significant number that were not. The fifth phase of the development of the 458 iWED analyzed records where there was a 15 to 30% difference between the fire management and 459 MTBS sizes. This phase included the same steps used in Phase 4, plus two additional steps. 

- 460 **_Step 1 –_** The WFEIS was used to identify those matched records where the MTBS size was more 461 accurate based on evidence provided by fire management perimeters, Landsat burned area pixels, and/or 462 MODIS burned area pixels, with additional evidence provided through visual interpretation of false463 color Landsat images. 

464 **_Step 2 –_** Matched records where MTBS events where burned area was incorrectly mapped were 465 identified through comparisons using the WFEIS of MTBS perimeters with fire management 466 perimeters, Landsat burned area pixels, and/or MODIS burned area pixels and analyses made through 467 visual interpretation of false-color Landsat images containing the MTBS perimeter and/or fine468 resolution aerial photography obtained from Google Maps. All MTBS events where it was determined 469 that burned area was incorrectly mapped were identified in variables 3 and 7 or 8 in the iWED dataset. 

470 

# **2.4.6 Geographic Areas** 

471 To implement the development of the iWED, the CUSA was divided into twelve geographic regions 472 based on single state or groups of states (Table S1). This division allowed for a systematic review and 473 comparison of events from fire management datasets and reports as well as the MTBS dataset. These 474 regions were also used to assess how the development of the iWED altered the average burned area 475 calculated from different datasets. Some assessments were carried out for four sub-continental areas 476 using two of the regions (Southeast and Southwest), the Eastern United States (EUS; consisting of the 477 Middle South, North Central, Northeast, and Northern Plains regions) and the Western United States 478 (WUS; consisting of the Alaska, California, Great Basin, Northwest, and Southwest regions). 

- 479 

# **2.5 Assessments and comparisons** 

480 The first assessment identified the processes that resulted in changes to the number of events and sizes 481 of events during the development of the iWED (Sect. 5.1). The second assessment examined the net 482 differences in the number of fire events and annual area burned resulting from using different 483 information sources in the iWED compared to the FS20 and MTBS datasets (Sect. 2.5.2). Comparisons 484 were made based on differences in annual average burned area calculated using the events from four 485 wildfire event databases (iWED, FS20, ICS, MTBS), where the comparison of the MTBS and iWED 486 datasets also included number of events (Sect. 2.5.3). Comparisons were then made based on the number 

- 487 and area burned in extreme wildfires events (mega and mega-plus fires) (Sect. 2.5.4). These analyses 

16 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 488 provide insights into the importance of having well-curated data for studying historical wildfire activity 489 in the CUSA. 

- 490 A large number of MTBS Unknown or Prescribed fire events in the Southern Plains that were 491 reclassified as wildfires occurred in the Flint Hills ecoregion of Kansas and Oklahoma, where 492 prescribed burning is the source for landscape-scale burning. For all analyses carried out for this study, 493 only fires ≥ 10,000 acres from the Flint Hill ecoregion were used. The rationale for inclusion of these 494 fires is presented in Sect. S4 of the Supplement to this article. 

495 **2.5.1 Sources of changes to fire management and MTBS events** 

496 Through the development of the iWED, fifteen different outcomes were identified that altered 497 the number of and/or the sizes of events compared to the baseline (FS20 and MTBS) datasets. Examples 498 of the significant changes resulting from the development of the dataset are presented. 

- 499 **2.5.2 Net changes to the number of wildfire events and the percentage change in burned area** 

- 500 Two assessments were carried out for the CUSA and the four sub-continental areas. The first assessment 501 examined net changes to the number of fire management and MTBS events for 1992 to 2021 that 502 occurred as a result of the iWED development. This assessment quantified the number of matched 503 events as well unmatched MTBS and fire management events. The second assessment examined how 504 the different sources of data that contributed to the iWED increased average burned area compared to 505 the FS20 dataset. Average area burned from 1992 to 2020 was calculated for the iWED and FS20 506 datasets by using wildfires smaller than 247 acres obtained from the FS20 dataset. The second 507 assessment examined percentage changes in FS20 that resulted from: (1) removals and adjustments to 508 FS20 events; (2) retention of fire events from the FS15 and FS18 datasets; (3) addition of events from 509 other fire management datasets and reports; (4) addition of events from IMSRs; (5) addition of events 510 from reports found on the world wide web; (6) use of unmatched MTBS Wildfire events; (7) use of 511 unmatched MTBS Prescribed Fire/Unknown events reclassified as wildfires; and (8) for matched 512 records, substitution of MTBS size for fire management size. 

513 

514 

# **2.5.3 Comparisons of wildfire event datasets and reported burned area** 

- 515 Comparisons based on annual burned area were carried out among the FS20, ICS, iWED, and MTBS 516 fire event datasets as well as annual area burned reported in annual reports from the the National 517 Interagency Coordination Center (NICC, 2002 to 2020). Comparisons were made between different 518 datasets for the CUSA, the four subcontinental areas, the regions within the EUS and WUS areas (Table 

17 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 519 S1), and the 49 states in the CUSA. Comparisons were made for different time periods based on the 520 availability of data for the datasets being compared. 

- 521 The reporting system used to create the ICS dataset is based on reporting wildfire greater than 100 acres 522 or events requiring significant resources for suppression and control. As a result, this dataset contains a 523 range of fire sizes, where the number of smaller fires is not consistent. For comparison with the FS20 524 dataset, wildfires larger than 100 ha (247 acres) were used. 

- 525 Differences in burned area derived from the FS20 and ICS datasets resulted from the number of wildfire 526 events contained in each and their sizes. Under most circumstances, it was expected that the FS20 527 dataset would contain more events because it had access to more wildfire reports than were entered into 528 the national database used for the ICS dataset. Even when the number of wildfire events are the same 529 for each dataset, burned area differences (either positive or negative) can occur if the sizes of individual 530 events are different. The ICS dataset, however, includes fires named as complexes that were not entered 531 into the FS20 dataset, where for several areas and years, the individual fires from complexes as well as 532 the complex were included in the ICS dataset. To address this double-counting, the difference in burned 533 area calculated using records from the ICS and FS20 datasets were examined on an annual basis to 534 identify states and years where the burned area from ICS records was 25,000 ha or more greater than 535 burned area from FS20 records. In 19 out of 20 cases examined, it was found that the ICS burned area 536 was based on using the size of a complex as well as fires within the complex. For these cases, the burned 537 area was recalculated with the individual fires removed. Annual burned area from wildfire events 538 contained in the ICS and FS20 datasets were calculated for each year from 1999 to 2020. The statistical 539 significance of the differences between the 21-year average burned areas was evaluated using a paired540 test for means based on a one-tailed p value. Percentage differences between average annual burned 541 area were compared using data from 1999 to 2009 and 2010 to 2020. 

- 542 Annual burned area for each year between 1992 to 2020 was calculated using all wildfire events ≥ 247 543 acres from the iWED and FS20 datasets plus wildfires < 247 acres from the FS20 dataset for each (these 544 annual values were also used in comparison with the NICC annual values discussed in the next 545 paragraph). The statistical significance of the differences between the 29-year average burned areas was 546 evaluated using a paired-test for means based on a one-tailed p value. Percentage differences between 547 average annual burned area were compared using data from 1992 to 2001, 2002 to 2011, and 2012 to 548 2021. 

- 549 Annual burned area reported by the NICC is dependent on the number of wildfire events used and their 550 sizes for each state and year. The NICC reported burned area would be lower than those derived from 551 wildfire event data if it was based on a fewer number of events and/or if the sizes of the fires used 

- 552 increased in the reports used for the event datasets. Reasons NICC burned area would be higher than 

18 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 553 those generated from event databases include: (a) events used in the NICC burned area were missing 554 from the fire event datasets; (b) the sizes of the some events included in both datasets were smaller in 555 the events database; and (c) the NICC burned area included the size of a fire complex as well as the 556 individual fires in the complex. The first step in comparing area burned reported in the NICC reports 557 and those developed from the FS20 and iWED datasets was to quantify the number of years where 558 NICC burned area was higher than those calculated from a fire management dataset for each state, as 559 well as the number of years where the NICC burned area was > 25% higher. The statistical significance 560 of the differences between the 19-year average NICC burned area and those calculated using events 561 from the FS20 and iWED dataset were evaluated using a paired-test for means based on a one-tailed p 562 value. Percentage differences between average annual burned area were compared using data from 2002 563 to 2011 and 2012 to 2020. 

- 564 Numerous studies have used the MTBS dataset to analyze trends in wildfire burned area, with the 565 justification that in the western US, fires > 405 ha represent > 90% of total burned area (see, e.g., Juang 566 et al., 2022; Morton et al., 2013). This justification was evaluated by comparing burned area from all 567 fire management events from the iWED dataset plus fire management events < 247 acres from the FS20 568 dataset from 1992 to 2020 to burned area from all MTBS wildfire events from the iWED dataset. 569 Percentage differences between average annual burned area were compared using data from 1992 to 570 2001, 2002 to 2011, and 2012 to 2021. 

- 571 

- 572 

# **2.5.4 Changes to the number of and burned area in larger and extreme wildfires** 

- 573 This assessment examined the differences in larger and extreme wildfires using the records from five 574 datasets, including: (a) the initial set of fire management records imported into the iWED from the FS20 575 dataset from 1992 to 2020 and other fire management sources for 2021 (hereafter referred to as the 576 FS20-plus dataset); (b) the MTBS Wildfire records initially imported into iWED (hereafter referred to 577 as the MTBS-A dataset); (c) fire management records from the iWED dataset (hereafter referred to as 578 the iWED-F dataset; (d) MTBS wildfire events from the iWED, including all Wildfire events and 579 Unknown and Prescribed fires that were matched with fire management or reclassified as wildfires 580 (hereafter referred to as the iWED-M dataset); and (e) all fire management records from the iWED 581 where MTBS size was substituted for fire management size for matched records and all unmatched 582 MTBS wildfire records (hereafter referred to as the iWED-F/M dataset). 

- 583 These datasets were used to compare the number of and burned area in larger and extreme wildfires. 584 The thresholds used by the MTBS program for creating fire perimeters were used to identify larger 585 fires: ≥ 500 acres (202 ha) for the EUS and Southeast region and ≥ 1,000 acres (504 ha) for the WUS 

19 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





586 and the Southern Plains region. Two categories of extreme wildfires were defined. First, mega fires 587 were those ≥ 12,350 acres (5,000 ha) in the Southeast region and EUS and ≥ 24,700 acres (10,000 ha) 588 in the Southern Plains and WUS. Second, mega-plus fires were those ≥ 123,500 acres (50,000 ha) in 589 the Southeast region and EUS and ≥ 247,000 acres (100,000 ha) in the Southern Plains and WUS. 

590 From each dataset, the number of all fires, mega fires, and mega-plus fires were determined for the 591 CUSA and four sub-continental areas using the fire records from each dataset. Burned area was 592 calculated from all fires, mega fires, and mega-plus fires for each dataset. Comparisons were made 593 between: (1) the FS20-plus and MTBS-A datasets; (2) the iWED-F and FS20-Plus datasets; (3) the 594 iWED-M and MTBS-A datasets; and (4) the iWED-F/M and FS20-plus datasets. Comparisons were 595 based on the difference in the number of fire records and the percentage difference in burned area. 

- 596 

# **3 Results** 

597 

# **3.1 Alterations to wildfire events through the development of the iWED** 

598 When compared to the FS20, ICS, and MTBS datasets, the development of the iWED increased the 599 number of records of individual wildfire events. Three types of records are contained the iWED. Those 600 containing only information for a fire management event (FM records), those containing only 601 information for an MTBS event (MTBS record), and those containing information on both a fire 602 management and MTBS event (matched record). Table 2 summarizes fifteen processes used in the 603 development of the iWED that resulted in significant alterations (outcomes) to the wildfire records. 604 This table identifies whether these processes increased or decreased the number records and the average 605 size of fire management and MTBS events contained in them, increased or decreased area burned 606 calculated from all records, and increased the number matched records. This table also provides a 607 summary of changes that resulted from the 15 processes. Finally, this table provides a list of the sections 608 in the online Supplement that present examples of the changes that occurred as well as the figures 609 illustrating specific changes. 

- 610 

# **3.2 Changes to the number of records and burned area** 

611 The development of the iWED resulted in a dataset containing 45,951 fire records (Table 3). All wildfire 612 and MTBS events that were used during the development of the iWED were retained, with two 613 exceptions. First, the individual FM and MTBS records for matched records were not retained. Second, 614 the individual FM records and MTBS records for fires that had merged were not retained. 

- 615 The dataset includes 21 fire management records and six MTBS Wildfire records that are duplicates. 616 The dataset includes 44 fire management events named as complexes where, based on the number of 617 fires within the complex, it was determined that the size of each fire was less than 247 acres. There are 

20 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 618 13 MTBS records with multiple perimeters where it was determined that the size of each was less than 

- 619 247 ha. The net effect of all the alterations to events was to add 1,530 new FM records to the dataset 620 for the CUSA, increasing the number of these records by 4.3%. The largest increase occurred in the 621 Southeast (7.3%) and Southern Plains (10.2%) regions. The lowest increase occurred in the WUS 622 (1.1%) where increases from adding records were offset by the large number of records were involved 623 in merged fires. 

- 624 The option to use unmatched MTBS records assigned a Wildfire type would further increase the number 625 of wildfires by a smaller amount for the CUSA (3.4%), with the highest increases in the Southern Plains 626 (5.1%) and Southeast (7.2%) regions. The option to use unmatched, Unknown/Prescribed MTBS 627 records that were reclassified as wildfires further increased the number of events would increase the 628 number of wildfire events by 1.8% for the CUSA, with the largest increase (5.7%) in the Southeast 629 region. 

- 630 For the CUSA, the net effect of adding fire management records and adjustments to wildfire size 631 through the development of the iWED increased average annual burned area by 2.4% compared with 632 using data FM records from the FS20 dataset (Table 4). This increase ranged from 1.8% in the WUS to 633 6.0% in the Southeast. The sources for these increases varied across the different sub-continental areas 634 for the different data sources. While adjustments to FS20 size contributed to fire management changes 635 in all areas, it was a primary contributor only in the EUS, where it accounted for 23% of the total 636 increase. Additions of ICS events were a primary contributor in the EUS (35% of the increase) and the 637 Southern Plains (40% of the increase).  Fire management events harvested from reports and datasets 638 were important only in the WUS (32% of the increase). Finally, events harvested from NIFC IMSRs 639 were an important contributor in the Southeast (60% of the increase), Southern Plains (38% of the 640 increase), and WUS (31% of the increase (Table 4). 

- 641 Using unmatched MTBS events given a Wildfire type or reclassified as wildfire is a unique feature 642 available for increasing the number of events available for wildfire studies. Using the unmatched MTBS 643 Wildfire events would increase average burned area by 1.7% for the continental US, with the largest 644 increases occurring in the Southeast (4.0%) and Southern Plains (5.7%) (Table 4).  Using unmatched 645 MTBS Unknown/Prescribed fire events reclassified as wildfires would increase average burned area by 646 2.7% for the CUS, with the largest increase in the Southern Plains (18.2%) (Table 4). 

- 647 The iWED provides the opportunity to use the MTBS size instead of fire management size for matched 648 events. Using such a substitution approach did not appreciably change the calculation of average burned 649 area except in the EUS and WUS and resulted in a 0.9% increase in the Southeast (Table 4). The 4.2% 650 reduction in the Southern Plains was largely due to two mega-plus fire matched records whose FS20 651 sizes (>170,000 ha) were much higher than their MTBS sizes (120,000 ha) (Fig. S29). 

21 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





652 Using all the additional fire management and MTBS wildfire records and making MTBS adjustments 653 increased average burned area by 6.4%, with increases of greater than 13% in the Southeast and 654 Southern Plains (Table 4). 

655 One additional observation was made when reviewing annual burned area for wildfires smaller than 656 100 ha from the FS20 dataset was that these smaller fires were under-represented for periods in the 657 1990s for eight states (Table 5). During these periods average area burned in the smaller fires was 6 to 658 22 lower than in the other years. In four of the states, average burned area in these smaller fires 659 represented more than half of the total burned area from all fires. This shortcoming is meaningful when 660 analyzing longer-term trends in burned area. 

661 **3.3  Comparisons between wildfire event datasets and reported burned area** 

662 Table 6 presents the average annual burned area calculated from the records from the ICS and FS20 663 datasets for the geographic areas used in this study using data from 1999 to 2020. Those areas where 664 the paired t-tests identified statistically significant differences in annual burned area are identified. In 665 addition, this table presents the percentage difference between FS20 and ICS average burned afor three 666 periods: 1999 to 2020, 1999 to 2009 and 2010 to 2020. These last data are presented to determine if the 667 percentage of FS20 burned area remained constant between the decadal periods. 

668 ICS average burned area was 14.2% lower than FS20 average burned for the CUSA. Annual ICS burned 669 area was significantly lower for the four sub-continental areas (ranging from 31.7% in the EUS to 12.7% 670 in the WUS) and six out of the ten regions (ranging from 41.5% in the Northern Plains to 5.6% in the 671 Southwest) (Table 6). There were three states (Indiana, Ohio, and Utah) where the ICS burned area was 672 higher than the FS20 burned area, but the differences were not statistically significant. At a state level, 673 the lowest differences occurred in the WUS, where seven states had significant differences between 674 ICS and FS20 burned areas, and the ICS percentage ranged from 12.0% in Wyoming to 1.9% in Arizona 675 (Table 6). The highest significant differences occurred in the EUS states, including West Virginia 676 (68.3%), South Dakota (50.6%), and Tennessee (41.9%). Of note was the fact that the percentage of 677 ICS burned area compared with FS20 burned area increased between the two decadal periods for all 678 sub-continental areas, all regions except for the Rocky Mountain, and all but seven states (Table 6). 679 These results indicate that the ICS dataset is less suitable for studying wildfire trends than the FS20 680 dataset. 

681 Table 7 presents the average annual burned area calculated from the records from the FS20 and iWED 682 datasets for the geographic areas used in this study using data from 1992 to 2020. The structure of this 683 table is identical to that for Table 6 except that it includes three decadal time periods instead of two. 684 Average burned area calculated using records from the iWED dataset were higher than burned area 

22 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 685 calculated using those from the FS20 dataset for the CUSA, all sub-continental areas, all regions, and 686 all but two states. These differences were statistically significant in all areas except for two regions and 687 15 states (Table 7). Reasons for FS20 burned area being higher in Table 7 included substitution of 688 MTBS size for fire management size (where the MTBS size was smaller) and correction of the fire 689 management size. The results in Table 7 reveal that for the CUS, EUS, Southeast, and WUS and for all 690 but the Northern Plains region, the percentage difference between iWED and FS20 burned area 691 decreased between the 1990s and 2020s, indicating that the compilation of fire records for the FS20 692 dataset most likely improved over this time period. 

- 693 Table 8 presents the average annual burned area based on information obtained from the NICC annual 694 reports and calculated from the FS20 and iWED datasets for the geographic areas used in this study 695 using data from 2002 to 2020. Those areas where the paired t-tests identified statistically significant 696 differences in annual burned area are identified. This table also presents the percentage differences 697 between the NICC and FS20 average burned area and the NICC and iWED average burned area for 698 three time periods. Finally, this table identifies the number of times NICC burned area was greater than 699 FS20 and iWED area burned for a state, and the number of times when NICC burned area was 25% or 700 more greater. 

- 701 Over the 19 years for which information from the NICC reports and the FS20 dataset were available, 702 there were 389 instances from 42 states where the NICC burned area was higher than the burned area 

- 703 calculated from the FS20 events and 466 instances when the FS20 burned area was higher (Table 8). 704 There were 151 instances where the NICC burned area was >25% higher. As a result of the split in the 705 frequency of years where the NICC burned area was higher or lower than that from the FS20 dataset, 706 there were 22 states where the average burned area from the NICC reports was greater than that from 707 the FS20 dataset and 20 where the NICC average burned area was lower, with half of these being 708 statistically significant (Table 8). For the CUS, average NICC burned area was only 1.0% higher than 709 the FS20 burned area over the entire 19-year period, which was not statistically significant. For the 710 EUS, NICC burned area was 3.1% higher than FS20 burned area, where the lower burned areas in the 711 Middle South, North Central, and Northeast regions were offset by the higher burned areas in the 712 Northern Plains region (Table 8). While the FS20 burned area was 10.6% higher in the Southeast, this 713 difference was not statistically significant; however, there were two states in this sub-continental area 714 where NICC burned area was y higher (Table 9).  The FS20 burned area was 9.7% higher in the 715 Southern Plains, where the FS20 burned area was higher in two states and lower in one. Finally, the 716 NICC burned area in the WUS was 0.9% lower than FS20 burned area, where higher burned area in 717 California and Alaska were offset by lower burned area in the Great Basin, Northwest, Rocky Mountain 718 and Southwest regions (Table 8). 

23 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 719 The differences in burned area for the 2002 to 2011 and 2012 to 2020 time periods plus the number of 720 years where NICC burned area was > 25% higher provide indicators for identifying potential years 721 where it is likely that the FS20 dataset is missing wildfire events. For example, many of the states in 722 the EUS have low annual burned area where NICC burned area is higher than FS20 burned and have a 723 number of years where the NICC/FS20 difference is > 25% (see, e.g., North Carolina, Tennessee, 724 Virginia, Indiana, Iowa, Missouri, Wisconsin, Maine, Massachusetts, New York, Ohio, Pennsylvania, 725 and North Dakota in Table 9).  Other states where this combination exists include Kansas (from 2012 726 to 2020), Colorado (from 2002 to 2011), and New Mexico from 2002 to 2011). While the percentage 727 difference is high in Montana over all time periods, there was only one year where it was > 25%. Since 728 Montana is a state where the number of fires reported as complexes is high, it is likely that the higher 729 NICC burned area in this region may have resulted from a combination of incorrect reporting of fire 730 size and reporting of both complexes and fires within them. 

- 731 Average annual burned area calculated using records from the iWED dataset resulted in higher burned 732 area (compared to the FS20 burned area) for the majority of the geographic areas with the exception of 733 a few regions and states where substitution of MTBS for fire management size resulted in reductions 734 (see, e.g., the Northwest region and Oregon in Table 8).  Because of the higher burned areas, compared 735 to the FS20 burned area, there were ten fewer states where NICC burned area was greater than iWED 736 burned area, as well as for WUS, and the Middle South, North Central, and Great Basin regions (Table 737 8). Even though the use of the IWED dataset resulted in less situations where NICC burned area was 738 higher, there were still 332 instances where in a state for a specific year where the NICC burned area 739 was more than 25% higher than the iWED burned area, as well a number of periods  when average 740 NICC burned was higher than iWED burned area for some states. These results indicate there is a strong 741 possibility that the iWED data set is missing wildfire events. 

- 742 Table 9 presents average annual burned area calculated from MTBS wildfire events and iWED fire 743 management events plus FS20 events smaller than 247 acres for the geographic areas used in this study 744 using data from 2002 to 2020. Those areas where the paired t-tests identified statistically significant 745 differences in annual burned area are identified. Also presented area percentage of iWED burned by 746 represented in the MTBS burned area for four time periods. While studies have used the MTBS wildfire 747 events to study trends in burned area based on the observation that the area within MTBS perimeters 748 represents >90% of burned area in the WUS, this percentage was < 90% in 10 out of 15 WUS states 749 and > 90% in one Southern Plains state  (Kansas) (Table 9). In 23 EUS states, MTBS burned area 750 represented less than 50% of area burned in fire management events from the iWED dataset. Another 751 characteristic  of the MTBS burned area data is that the percentage of iWED burned area increases from 752 the 1990s to the 2010s, including 6 out of the 10 western states where the MTBS percentage for all 753 years was greater than 90%. This result means that increases in burned area detected using MTBS data 

24 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





754 are the result of a more representative sampling of wildfire activity during the 2010s relative to earlier 755 years. 756 **3.4  Differences in extreme wildfire activity** 

- 757 Through the development of the iWED, there were ten processes that changed the number and sizes of 758 mega and mega-plus records, with three changing FM records, three changing MTBS records, and four 759 changing matched records (Table 10). Three of these processes increased the number of mega and 760 mega-plus events (both fire management and MTBS), two processed decreased the number and/or size 761 of fire management and MTBS events, and five processed both increased and decreased the number 762 and sizes of events. 

763 A common result for the CUS across all five datasets used to study extreme wildfire activity was that 764 while mega fires represented only ~8% of the total number of larger wildfires, they accounted for nearly 765 50% of average area burned where mega-plus fires represented < 0.5% of the area burned but accounted 766 for nearly 15% of average area burned (Table 11). There were distinct differences in the level of extreme 767 wildfire activity in the four sub-continental areas. When mega and mega-plus fires were combined, the 768 percentage of the number of events and burned area in these events was highest in the Western US 769 (14.6% and 67.3%, respectively) and lowest in the Eastern US (2.8% and 33.8%, respectively), with 770 the Southeast and Southern Plains falling between the two (Table 12). A distinguishing feature of the 771 Eastern US is that it experienced no mega-plus fires between 1992 to 2021. Another common 772 characteristic across the five datasets was that a large majority of the number and burned area in the 773 larger wildfires occurred in the WUS. Because of this distribution, the percentage differences for the 774 CUSA largely follow those in the WUS. 

775 Table 12 contains a summary of the total number of larger wildfire records (> 202 acres in the Eastern 776 US and Southeast and > 405 ha in the Southern Plains and Western US) and the numbers of extreme 777 records (mega and mega-plus fires) and average area burned from these events for the CUS and four 778 sub-continental areas. These results are based on data from 1992 to 2021 from five different datasets 779 (Sect. 2.5.4), Additional results in Table 12 include the percentage differences in the numbers and 780 average burned area between the five datasets. 

781 To a great extent, the large differences in the total number of fires between the FS20-plus and MTBS782 A datasets explains the differences in total burned area presented in Table 9, where the largest 783 differences in percent burned area occurred in the EUS and Southeast. For the CUSA there were 44 784 more mega fires in the FS20-plus dataset, with the highest difference in number and burned area in 785 mega-plus fires occurring in the Southeast and Southern Plains (Table 12). While the FS20-plus dataset 786 contained one more mega-plus fire than the MTBS-A dataset in the Southern Plains, it contained one 

25 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 787 less mega-plus fire in the Southeast (one of the mega-plus fires in the Big Turnaround Complex that 788 was identified in an NIFC IMSR). 

789 The iWED dataset contained 848 more larger  fire management events than the FS20-plus dataset, with 790 28 of these being mega-fires and 8 being mega-plus fires. The largest increases in the number of mega 791 (17) and mega-plus (7) fires occurred in the WUS as a result of merging of fires. The largest increases 792 in burned area occurred for mega fires in the Southern Plains, and mega-plus fires in Southeast and 793 WUS. While there were large increases in the number of mega-fires, increase in the burned area for 794 these fires in the Southeast and WUS was limited by the merging of mega-fires to form mega plus fires. 

795 The development of the iWED changed the number of MTBS events as illustrated in the iWED-M 796 versus MTBS-A comparisons in Table 12. Overall, the increase in the number of larger fires was based 797 on increases through adding of Unknown and Prescribed Fires reclassified by as wildfires and decreases 798 through identification of MTBS records with multiple perimeters as well as identifying MTBS 799 perimeters that had merged. The increase of 67 mega fires and 2 mega-plus fires in the Southern Plains 800 occurred as a result of using mega and mega-plus MTBS records that had been reclassified as wildfires 801 from the Flint Hills region. In the EUS, the decrease in mega fires occurred by identifying MTBS events 802 containing multiple perimeters. In the WUSA, the decrease in mega fire number and area burned was 803 the result of identifying fires that had merged to create mega-plus fires, whose number and burned area 804 increased (Table 12). 

805 Using information from both fire management, MTBS, and merged records from the iWED increased 806 the number of mega fires by 93 and mega-plus fires by 9 compared to those contained in the FS20+ 807 data. Notable changes in mega-fire burned area occurred in the WUS (19.4% increase), mega and mega808 plus-fire burned area in the Southeast (24.5% and 10.6% increases, respectively), and mega-fire burned 809 area in the Southern Plains (80.7% increase by including MTBS wildfires from the Flint Hills ecoregion 810 (Table 12).  There was a decrease in mega-plus-fire burned area in the Southern Plains resulting from 811 substitution of MTBS size for fire management size (see Fig. S29 in the Supplement to this article). 

- 812 

- 813 **4 Discussion and Conclusions** 

814 Existing wildfire event datasets have been developed through funding provided by the federal 815 government and universities and exist only because of the dedicated efforts of scientists and researchers 816 of the U.S. Forest Service (Short, 2021), the MTBS program (Eidenshink et al., 2006; Picotte et al. 817 2020), and the University of Colorado (St. Denis et al., 2023). The development of the FS20, MTBS, 818 and ICS datasets has provided data used in a wide range of fire science research (Table S1 in the online 

- 819 Supplement). The development of the integrated Wildfire Event Dataset (iWED) provides researchers 

26 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 820 with a fourth option to study wildfires at regional to national scales in the United States. The iWED 821 development followed a systematic approach in adding and altering wildfire records (Fig. 1), resulting 822 in changes to the number and sizes of fires events, as well as identifying duplicate records (Tables 2 823 and 10). The three most important processes were further matching of fire management events with 824 MTBS events, visual interpretation of images generated from geospatial data, and review of reports 825 found on the world wide web to resolve uncertainties in fires named as complexes and differences in 826 MTBS and fire management size. 

- 827 While there were many matched MTBS and fire management records in the FS20 dataset of Short 828 (2021), a review revealed that a number were incorrect. Additional matches were identified during the 829 iWED development. A number of the matched records in the iWED included MTBS events that were 830 assigned an Unknown or Prescribed Fires in the MTBS database, identifying events that had been 831 misclassified. Many of the new matched records in the iWED occurred with fire management events 832 mined or harvested from other fire management reports and datasets, IMSRs, and reports found through 833 searches of the world wide web. A difference between fire management and MTBS size was a key 834 criteria for further investigation of fire records, as were instances where the same MTBS was matched 835 with multiple fire management events in FS20 records. 

- 836 Visual interpretation was used during the matching process to determine if the position for a fire 837 management event was within an MTBS perimeter. These position/perimeter comparisons were used 838 to identify fire management events that had merged and MTBS perimeters that resulted from joined 839 events. Visual interpretation of MTBS perimeter shape was used to identify MTBS Unknown and 840 Prescribed Fire events that were likely wildfires (Figs. S1, S2). In addition, the first stages of the iWED 841 development focused on fire management and MTBS events named as complexes and those where the 842 size difference between MTBS and fire management events was greater than 25%. Through visual 843 interpretation of the displaying MTBS events for these events, it was discovered that a number 844 contained multiple perimeters. Based on this finding, visual interpretation was used on all unmatched 845 MTBS events as well as a number of matched events, where nearly 10% contained multiple perimeters. 846 Many of the additional MTBS perimeters were matched with fire management events. Simultaneous 847 display of multiple MTBS events identified a number that shared common borders. For these events, 848 additional analyses determined that a number represented merged fires and others that were separate 849 but adjacent perimeters for a single event. Visual comparisons were also made of simultaneous displays 850 of MTBS perimeters, other fire perimeters, and MODIS and Landsat burned area pixels for a variety of 851 purposes (Figs. S12, S15, S19, S20, S22, S28). 

- 852 A review of fire management reports, datasets, and daily/weekly Incident Management Situation 853 Reports downloaded from the world wide web were used to identify fire management events for 2021 854 and events not contained in the FS20 dataset. Searches of the world wide web were used for analyses 

27 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 855 of specific events to identify additional information on fires named as complexes or matched events 856 where there were significant differences between fire management and MTBS size. Among other 857 things, these searches identified the names and sizes for many events named as complexes, fires that 858 had merged, and fires whose size had been incorrectly reported. 

859 The development of the iWED improved the fidelity of wildfire data relative to the FS20, ICS, and 860 MTBS  datasets through the identification of additional events and providing more accurate depictions 861 of the sizes of many wildfires, in particular fires that had merged or joined, fires whose size was 862 incorrectly reported, and records that represented multiple fires. The assessments carried out for this 863 study, however, concluded the FS20, ICS, and MTBS datasets did not completely account for wildfire 864 activity in all regions. For many regions, the ICS dataset contained fewer wildfire events than the FS20 865 dataset, especially during the 2000s. The ICS dataset, however, contributed a number of additional 866 frecords to the iWED. It was determined that the FS20 dataset did not contain a number of small fires 867 (< 100 ha) from the 1990s through the early 2000s for eight eastern U.S. states (Table 5). Because small 868 fires represent a significant portion of annual area burned in these states, their absence will affect studies 869 examining trends in annual area burned in eastern U.S. regions that rely on fire management data. 

- 870 The inclusion of three types of records in the iWED provides options that are not available in other 871 datasets. Combining the FS20 events with unmatched MTBS and substituting MTBS size for FM size 872 addresses many of the shortcomings of the individual datasets. In particular the combined dataset 873 provides improved estimates of annual burned area (Tables 7 and 9) and a more accurate accounting of 874 mega and mega-plus events (Table 12). 

875 Comparisons showed there were differences in burned area developed from records in the FS20 and 876 iWED datasets and those reported in the NICC annual reports, where in a number of instances the 877 average NICC burned area was greater than those the FS20 or iWED values for some states and time 878 periods (Table 8). While these differences in western states may be due to the reporting of a wildfire 879 complex size as well as the fires within the complex for some years, the difference in eastern states may 880 be due to an incomplete reporting of all wildfire events. 

- 881 The development of the first two versions of the iWED presented in this study represents the initial 882 steps in developing datasets for wildfire studies in the CUS. A third version of this dataset will add the 883 latitude/longitude positions for each record. The approach used to develop the iWED (Fig. 1) provides 884 a framework for the future updating of this dataset that is needed to extend information on wildfire 885 activity across the CUS. The authors are currently working on updating the dataset with records for the 886 WUS for the early 2020s, which would use records from newer versions of the FS20, ICS, and MTBS 887 datasets if and when they become available. Additional information that will be added to this dataset 888 includes information from fire perimeter datasets as well as daily burned area. 

28 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 889 **Data availability** 

- 890 Version 1 of the integrated Wildland Fire Event Dataset (iWED) is available from the Oak Ridge 891 National Laboratory Distributed Active Archive Center (ORNL-DAAC) 892 (https://doi.org/10.3334/ORNLDAAC/2452) (Kasischke et al., 2025). Version 2 of the iWED is 893 currently being reviewed by the ORNL-DAAC (Kasishcke et al., in review). 

- 894 

- 895 **Author Contributions** 

- 896 EK and NF contributed equally to the development of the goals and objectives for the dataset 897 development and the approaches used during this development. NF procured funding from NASA that 898 contributed to the dataset development. EK carried out the integration of data from multiple sources 899 and implemented the various steps and procedures used to refine the information for the wildfire records 

- 900 contained in the dataset. EK wrote the initial version of the manuscript which was then edited by NF. 

- 901 **Acknowledgements** 

- 902 The authors would like to thank Mike Billmire and Chris Cook for their assistance during different 903 stages of the development of the integrated Wildland Fire Event dataset and its submission for 904 publication by the Oak Ridge National Laboratory Distributed Active Archive. 

- 905 

# **Financial support** 

- 906 The development of the integrated Wildfire Event Dataset (versions 1 and 2 was supported by the 907 National Aeronautics and Space Administration through grant 80NSSC24K0299. 

- 908 **References** 

- 909 AICC, Daily Incident Situation Management Reports from 1992 to 2021 published by the Alaska 910 Interagency Coordination Center (AICC) downloaded from https://fire.ak.blm.gov/predsvcs/intel.php 911 (last accessed on 30 June 2026), 1992 to 2021. 

- 912 Billmire, M., French, N.H, McKenzie, D, Koziol, B. T. Erickson, T.: The Wildland Fire Emissions 

- 913 Inventory System, https://wfeis.mtri.org, accessed on 15 June 2026. 

- 914 Eidenshink, J., Schwind, B, Brewer, K., Zhu, Z. -L. Quayle, B., Howard, S.: A Project for Monitoring 

- 915 Trends in Burn Severity, Fire Ecol. 3, 3–21, 2007. 

- 916 French, N. H., et al.: Modeling regional-scale wildland fire emissions with the Wildland Fire Emissions 

- 917 Information System, Earth Inter. 18, 1-26, 2014. 

29 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 918 Giglio, L., Boschetti, L., Roy, D., Hoffmann, A. A., Humber, M., Hall, J. V.: Collection 6 MODIS 919 Burned Area Product User’s Guide Version 1.2, NASA: 30. https://modis920 land.gsfc.nasa.gov/pdf/MODIS_C6_BA_User_Guide_1.2.pdf, 2018 

- 921 Hawbaker, T.  J., Vanderhoof, M. K., Schmidt, G. L., Beal, Y. -P., Picotte, J. J., Takacs, J .D.. Falgout, 922 J. T., Dwyer, J. L.: The Landsat Burned Area algorithm and products for the conterminous United 923 States, Remote Sens. of Environ., 244, article no. 111801, 2020. 

- 924 Juang, C. S. Williams, A. P. Abatzoglou, J. T., Balch, J. K., Hurteau, M. D., Moritz, M. A: (Rapid 925 growth of large forest fires drives the exponential response of annual forest-fire area to aridity in the 926 western United States, Geophys. Res. Lett. 49, e2021GL097131, 2022. 

- 927 Kasischke, E. S., French, N. H., Billmire, M., Redhuis, D., Cook, C.: An integrated Wildfire Event 928 Dataset (iWED_V1), 1992-2021. ORNL DAAC, Oak Ridge, Tennessee, USA. 929 https://doi.org/10.3334/ORNLDAAC/2452, 2025. 

- 930 Kasischke, E. S., French, N. H., Billmire, M. D., Cook, C.:. An integrated Wildfire Event Dataset 931 (iWED_V2), 1992-2021. ORNL DAAC, Oak Ridge, Tennessee, USA, in review, 2026. 

- 932 Linley, G. D., et al.: What do you mean ‘megafire’?, Global Ecol. Biogeogr., 31,1906–1922, 2022 

- 933 Morton, D. C., Collatz, G. J, Wang, J. D., Randerson, J. T., Giglio, L.,. Chen, Y.. Satellite-based 934 assessment of climate controls on US burned area, Biogeosci. 10, 247–260 (2013). 

- 935 MTBS: direct download of MTBS wildfire records from https://burnseverity.cr.usgs.gov/direct936 download (last accessed on 30 June 2026), 2026a. 

- 937 MTBS: direct download of individual MTBS event from https://www.mtbs.gov/direct-download (last 

- 938 accessed on 20 February 2026).  As of 1 June 2026, this website is no longer available, 2026b. 

- 939 NICC: Wildland Fire Summary and Statistics Annual Reports, 2002 to 2001, published by the National 940 Interagency Coordinating Center, downloaded from https://www.nifc.gov/nicc/predictive941 services/intelligence (last accessed on 30 June 2026), 2002 to 2020. 

- 942 NIFC: Daily Incident Situation Management Reports from 1992 to 2021 published by the National 943 Interagency Coordination Center, downloaded from https://www.nifc.gov/nicc/incident- 

- 944 information/imsr (last accessed on 30 June 2026), 1992 to 2021. 

- 945 Picotte, J. J., et al.: Changes to the Monitoring Trends in Burn Severity program mapping production 946 procedures and data products. Fire Ecol. 6, article no. 16, 2020. 

30 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 947 Prichard, S. J., Ottmar, R. D., Anderson, G. K.: CONSUME 3.0 User's Guide. Seattle, WA, Fire and 948 Environmental Research Applications Team, USDA Forest Service, 2006 

- 949 Short, K. C.: A spatial database of wildfires in the United States, 1992–2011. Earth System Science 950 Data 6, 1–27, 2014. 

- 951 Short, K. C.: Sources and implications of bias and uncertainty in a century of US wildfire activity data, 952 Int. J. Wildland Fire, 24, article no. WF14190, 2015. 

- 953 Short, K. C.: Spatial wildfire occurrence data for the United States, 1992-2015 [FPA_FOD_20170508]. 954 4th Edition. Fort Collins, CO: Forest Service Research Data Archive. https://doi.org/10.2737/RDS955 2013-0009.4, 2017. 

- 956 Short, K. C.: Spatial wildfire occurrence data for the United States, 1992-2018 [FPA_FOD_20210617]. 957 5th Edition. Fort Collins, CO: Forest Service Research Data Archive. 2. https://doi.org/10.2737/RDS958 2013-0009.5, 2021. 

- 959 Short, K. C.: Spatial wildfire occurrence data for the United States, 1992-2020 [FPA_FOD_20221014]. 960 6th Edition. Fort Collins, CO: Forest Service Research Data Archive. https://doi.org/10.2737/RDS961 2013-0009.6, 2022. 

- 962 Sparks A. M., Boschetti, L., Smith A. M. S., Tinkham, W. T., Lannom, K. O., Newingham, B. A.: An 963 accuracy assessment of the MTBS burned area product for shrub–steppe fires in the northern Great 964 Basin, United States, Int. J. Wildland Fire, 24, 70–78, 2015. 

- 965 St. Denis, L. A.. Short, K. C., McConnell, K., Cook, M. C., Mietkiewicz, N. P., Buckland, M. Balch, J. 

- 966 K.: All-hazards dataset mined from the US National Incident Management System 1999–2020, 967 Scientific Data, 10, article no. 112, 2023. 

968 

31 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





969 **Table captions** 

|970<br>971|1. Description of common procedures used during the different phases of the development of the iWED<br>(see Fig. 1).|
|---|---|
|972|2. Summary of changes to wildfire records occurring during the development of the iWED.|
|973|3. Total number of fire management and MTBS records contained in the iWED.|
|974|4. Percentage differences in average annual area burned based on the different sources for information|
|975|used in the development of the iWED compared to the burned area calculated from the  FS20 events|
|976|imported into the dataset.|
|977|5. States where average burned area from smaller wildfires were significantly lower during periods in|
|978|the 1990s and 2000s compared to that from later periods.|
|979|6. Comparison of average burned area from the ICS and FS20 datasets using records from 1999 to 2020,|
|980|where the letter superscripts in the FS20 dataset column indicate the statistical significance for the|
|981|difference between the ICS and FS20 average burned area (a: p < 0.1; b: p < 0.05; c: p < 0.01; d: p <|
|982|0.001). % burned area difference  = [(FS20 burned area) – (ICS burned area)] / (FS20 burned area) x|
|983|100. Data from states where average burned area was less than 100 ha yr-1 are not included in this table.|
|984|The data from these years, however, was used to calculate burned area at regional, sub-continental, and|
|985|continental scales.|
|986|7. Comparison of average burned area calculated by using records from the FS20 and iWED datasets|
|987|from 1992 to 2020, where the letter superscripts in the iWED dataset column indicate the statistical|
|988|significance for the difference between the FS20 and iWED average burned area (a: p < 0.1; b: p < 0.05;|
|989|c: p < 0.01; d: p < 0.001). % burned area difference = [(iWED burned area) – (FS20 burned area)] /|
|990|(iWED burned area) x 100. Data from states where average burned area was less than 100 ha yr-1 are|
|991|not included in this table. The data from these years, however, was used to calculate burned area at|
|992|regional, sub-continental, and continental scales.|
|993|8. Comparison of average annual burned area from data from NICC reports to that calculated using|
|994|records from the FS20 and iWED datasets for 2002 to 2020, where the letter superscripts in theFS20|
|995|and iWED datasets columns indicate the statistical significance for the difference between the NICC|
|996|and the FS20 and iWED average burned area (a: p < 0.1; b: p < 0.05; c: p < 0.01; d: p < 0.001). %|
|997|difference: NICC vs. FS20 =  [(FS20 burned area) – (NICC burned area)] / (FS20 burned area) x 100.|
|998|% difference: NICC vs. iWED =  [(iWED burned area) – (NICC burned area)] / (iWED burned area) x|
|999|100. Data from states where average burned area was less than 100 ha yr-1 are not included in this table.|



32 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





1000 The data from these years, however, was used to calculate burned area at regional, sub-continental, and 1001 continental scales. 

1002 9. Comparison of average burned area from the MTBS and iWED datasets calculated using records 1003 from 1992 to 2020, where the letter superscripts in the iWED dataset column indicate the statistical 1004 significance for the difference between the MTBS and iWED average burned area (a: p < 0.1; b: p < 1005 0.05; c: p < 0.01; d: p < 0.001). % MTBS burned area difference = (MTBS burned area) / (iWED burned 1006 area) x 100. Data from states where average burned area was less than 100 ha yr-1 are not included in 1007 this table. The data from these years, however, was used to calculate burned area at regional, sub1008 continental, and continental scales. 

1009 10. Processes used during the development of the iWED that changed the number and sizes of mega 1010 and mega-plus fires. 

- 1011 11. Percentage of the total number of mega and mega-plus fires as a function of total number of larger 1012 wildfire records for different study areas and the percentage of area burned in mega and mega-plus fires. 

- 1013 12. Summary of the number of and average burned in larger fire records using different wildfire event 1014 datasets. Data are from 1992 to 2021. Also included are percentage differences between the number of 1015 and area burned for different datasets. 

33 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





1016 

# **Figure captions** 

1017 1. Flowchart illustrating the datasets, methods, steps, and phases used during the development of the 

1018 integrated Wildland Fire Dataset (iWED). 

34 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





1019 **Table 1.** Description of common procedures used during the different phases of the 1020 development of the iWED (see Figure 1). 

|**Procedure**|**Description**|
|---|---|
|1|Comparing the perimeter for an MTBS record using the WFEIS with the position of a fire<br>management record using OpenStreetMap. A matched record was confirmed when the<br>position of the fire management record was within the MTBS perimeter.|
|2|Using Google Maps to identify the latitude and longitude of fire management records when<br>theirpositions were not available from other sources.|
|3|Using Google Maps to display topographic maps or fine resolution, aerial photographs in<br>order to identify landscape features that contributed to incorrect mapping of burned<br>vegetation bythe MTBSalgorithms.|
|4|Using the WFEIS, MTBS records containing multiple perimeters were identified. For these<br>records, visual interpretation was used to estimate the fraction of total MTBS size in each<br>perimeter, which in turn was used to calculate the size of each perimeter. Perimeters whose<br>sizes were≥247 ac were added to the iWED as individual records.|
|5|Using the WFEIS to simultaneously display an MTBS perimeter and perimeters from other<br>sources (CalFIRE, NIFS/GeoMAC, WFIGS) to match the fire management record with the<br>MTBSrecord.|
|6|Searching fire management reports, NICC and AICC situation reports, and reports found on<br>the world wide web to identify the number, names, and sizes of individual fires in a complex<br>or fires that were adjacent to the event beingassessed.|
|7|Allocating the FS18 size of a complex to the fires within the complex in proportion to the<br>sizes identified through searches of reports or in proportion to the MTBS size when only the<br>names or numbers of fires in a complex were found.|
|8|Using the WFEIS to simultaneously display a single MTBS perimeter and perimeters from<br>other sources (CalFIRE, NIFS/GeoMAC, WFIGS) to determine whether multiple fire<br>management records had merged orjoined byusingProcedures 1 and 5.|
|9|The merging of fire events was reported in a NICC or AICC IMSR, in other<br>firemanagement reports, or reportsfoundinsearches of the world wide web.|
|10|Using the WFIES to simultaneously display fire management perimeters and MODIS burned<br>area pixels, where the dates for the MODIS pixels were used to determine whether fires had<br>merged orjoined.|
|11|The joining of fires was confirmed when the end date for one fire was prior<br>tothe startdatefor the other fire.|
|12|Adjusting (changing) the FS20 size for a complex or event when it was judged the size was<br>incorrect based on information found in other reports or comparisons with other geospatial<br>data (such as other fire management perimeters and/or MODIS and Landsat burned area<br>pixels).|



1021 

35 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 







<!-- Start of picture text -->
1023  1022<br>36<br>records  4. Identified matched and unmatched MTBS  3. Added information on MTBS events   other sources  2. Added information on FM events from  FS20 wildfire occurrence dataset  1. Added information on FM events from the  Outcomes<br>+  +  FM<br>+  Records<br>Number of<br>ggpPhase 1 - Im information for fire manaement events ortin MTBS<br>FM<br>Size<br>MTBS  Average Fire<br>gy of FM/MTBS records and analses of unmatched MTBS records Phase 2 - Matchin +  +  FM<br>+<br>MTBS  Area Burned<br>+<br>Records  Matched<br> Summary of changes to wildfire records occurring during the development of the iWED.  Table 2.<br>unmatched  Fire  management  matched  management  obtained<br>records  FS18 datasets.<br>gmanaement event.  with  with  from  gChanes to dataset<br>that  gmanaement sources.<br>a  sources<br>fire  were  MTBS Unknown/ Prescribed  Wildfires records and 5,322  fires. There were 906 MTBS  Fires and 221 MTBS Unknown  including 38 MTBS Prescribed  records,  fire  13,057 MTBS  records were  ,19247 MTBS events added.  records added from other fire  2021. For all years, 1,697  for  fire  Data for 919 records were  were retained from FS15 and  dataset. Data from 84 records  were imported from the FS20  Data from 35,259  records<br>Section<br>ppSulement<br>gure Fi<br><!-- End of picture text -->

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 







<!-- Start of picture text -->
1025<br><!-- End of picture text -->



<!-- Start of picture text -->
Wildfires  6.  perimeters  MTBS<br>Identified<br>records<br>Table 2 (continued).<br>g9. Identified mered events  having<br>unmatched<br>gppevents havinerimeters le  multi 8. Added records from matched MTBS  gppcomlexes havinle fires  multi 7.Added records from unmatched FM  Unknown records reclassified as  MTBS  muliple  5. Added records from unmatched<br>-  +  +<br>-  +  +  +<br>+  -<br>+  -<br>+<br>+  -<br>-  +<br>events.  358  the dataset.  dataset.  where  named as  wildfires.  were  dataset.<br>the<br>matched<br>reclassified<br>events and 416 MTBS  of 827  fire management  resulted from the merging  records  that added 657 records to  perimeters (1,859 total)  event contained multiple  records where the MTBS  There were 701  matched  adding 68 records to the  complex were identified,  individual fires within the  number, and/or sizes of  names,  complexes  fire management records  There were 38 unmatched  as  or Prescribed Fire type  records with an Unknown  3,714 Unmatched MTBS  adding 1,946 events to the  have multiple perimeters,  records were found to  551 unmatched MTBS<br>S1<br>S2.3<br>,S2.1S2.2<br>,S1S2<br>gpyPhases 3 to 5 - Resolve uncertainties and ambi sources of the differences between FM and MTBS size for matched records uities in comlexes and identif<br>,S10-S15S19  S3-S10,S14,<br>,,,,S18S19S21S23S29<br><!-- End of picture text -->

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





<!-- Start of picture text -->
38<br><!-- End of picture text -->



<!-- Start of picture text -->
1027<br><!-- End of picture text -->





<!-- Start of picture text -->
1026<br>ppmaed area burned<br>()Table 2 continued.<br>14. Identified MTBS events with incorrectly  13. Reallocated FM and MTBS sizes  12. Corrected  FM and MTBS sizes  US/Canada or US/Mexico border  11. Identified events that spanned the  j10. Identified oined events<br>-  +<br>-  -<br>+/-<br>-  -  -<br>-  -<br>+/-<br>-  -  -<br>+<br>There were  records.  Within  perimeter(s)  MTBS  where the<br>matched records.<br>ppmaed burned area.   184  matched  U.S./Canada border.  spanned  events  MTBS<br>the MTBS algorithm incorrectly  records where it was judged that  matched  size reallocated in 230 records.  records and fire management  reallocated in  27 additional  as joined, MTBS sizes were  perimeters and those identified  size for events with multiple  In addition to reallocating MTBS  records and MTBS size for 74  fire management size in 250  adjustments were made to the  records,  the  whose  the U.S./Mexico border and 26  whose perimeter(s) spanned  There were 30 MTBS events  total), increasing the number of  fire management events (178  the result of joining of mulitple  contained  perimeter that was  event  There were 82 matched records<br>S2.7  S2.6  S2.5  S2.4  S2.3<br>S34  S26<br>S24,S31- ,S27S29  S21,S23,  S14,S16- S3-S10,  S4,S23- ,S21S22  S16-S20<br><!-- End of picture text -->

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 







<!-- Start of picture text -->
1029  1028<br>Table 2 (concluded).<br>pand small fire comlexes  15. Identified duplicate FM and MTBS events<br>-<br>-<br>-<br>-<br>-<br>-<br>management<br>and<br>5<br>fire was smaller than 247 ac.  where it was determined each  records named a complex  There were 44 fire management  records that were duplicates.  MTBS  The dataset contains 19 fire<br><!-- End of picture text -->

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





1030 **Table 3.** Total number of fire management and MTBS records contained in the iWED. 

||**Continental**<br>**US**|**Eastern US**|**Southeast**|**Southern**<br>**Plains**|**Western US**|
|---|---|---|---|---|---|
|**Total events**|45,951|6,233|6,974|11,539|21,205|
|||<br>**_Fire_**|<br>**_management ev_**|<br>**_ents_**||
|**Unmatched**|24,528|4,165|3,101|6,271|10,922|
|**Matched with MTBS event**|13,434|1,329|1,115|1,559|9,431|
|||<br>**_Unm_**|<br>**_atched MTBS ev_**|<br>**_ents_**||
|**Wildfire**|1,253|224|287|371|371|
|**Wildfire-Prescribed Fire**|17||||17|
|**Unknown-Wildfire**|2,365|189|257|1,709|210|
|**Unknown**|4,354|326|2,214|1,629|185|



1031 

40 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





|1035|**Total fire management + MTBS changes**|**Total MTBS changes**|**Substitution of MTBS size for fire management size**|**Unmatched MTBS Unknown records reclassified as wildfires**|**Unmatched MTBS Wildfire records**|**Total fire management changes**|**Events from reports found on the world wide web**|**Events from Incident ManagementSituation Reports**|**Records from other fire management datasets**|**Addition of ICS records**|**Retention of records from FS15 and FS18 datasets**|**Adjustment to FS20 fire size**|to the burned area calculated from the FS20 events imported into the<br>1033<br>1034|**Table 4.**Percentage differences in average annual area burned based<br>1032|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||6.40|3.97|-0.37|2.66|1.68|2.43|0.04|0.88|0.59|0.53|0.05|0.33|dataset.<br>**Continental**<br>**US**|on the different|
||8.29|5.66|-0.22|2.71|3.17|2.63|0.02|0.43|0.60|0.93|0.06|0.60|**Eastern US**|sources for inf|
||13.78|7.76|0.94|2.79|4.03|6.03|0.39|3.60|0.19|1.36|0.02|0.46|**Southeast**|ormation use|
||24.84|20.08|-4.20|18.62|5.66|4.76|0.05|1.80|0.89|1.92|0.10|0.00|**Southern**<br>**Plains**|d in the develo|
||3.13|1.34|0.04|0.47|0.83|1.80|0.01|0.56|0.59|0.24|0.05|0.35|**Western US**|pment of the iWED compared|



https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 1036 **Table 5.** States where average burned area from smaller wildfires was significantly lower during 

- 1037 periods in the 1990s and 2000s compared to that from later periods. 

|||**Average burned area**<br>**(ha)**||**Average bur**|**ned area(ha)**|
|---|---|---|---|---|---|
|**State**|**Period**|**Fire size < 100 ha**|**Period**|**Fire size <**<br>**100 ha**|**Fire size ≥**<br>**100 ha**|
|**Alabama**|1992-1993|562|1994-2020|12,465|3,443|
|**Iowa**|1996-2005|128|2006-2020|1,659|638|
|**Kansas**|1992-1997|160|1998-2020|3,006|16,652|
|**Kentucky**|1992-1995|731|1996-2020|12,147|9,156|
|**Nebraska**|1992-1999|357|2000-2020|2,367|15,256|
|**Pennsylvania**|1992-2001|20|2002-2020|417|680|
|**Tennessee**|1992-1996|293|1997-2020|5,463|4,914|
|**Virginia**|1992-1994|216|1995-2020|2,224|4,180|



1038 

42 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





1039 **Table 6.** Comparison of average burned area from the ICS and FS20 datasets using records from 1999 1040 to 2020, where the letter superscripts in the FS20 dataset column indicate the statistical significance for 1041 the difference between the ICS and FS20 average burned area (a: _p < 0.1_ ; b: _p < 0.05_ ; c: _p < 0.01_ ; d: _p_ 1042 _< 0.001_ ). % burned area difference = [(FS20 burned area) – (ICS burned area)] / (FS20 burned area) x 1043 100. Data from states where average burned area was less than 100 ha yr<sup>-1</sup> are not included in this table. 1044 The data from these years, however, was used to calculate burned area at regional, sub-continental, and 1045 continental scales. 

||**Burned ar**|**ea(hayr**<sup>**-1**</sup>**)**|**% bu**|**rned area diff**|**erence**|
|---|---|---|---|---|---|
||**ICS dataset**|**FS20 dataset**|**1999-2020**|**_1999-2009_**|**_2010-2020_**|
|**_ContinentalUS_**|2,306,787|2,687,565<sup>d</sup>|14.2|_24.1_|_4.7_|
|**_EasternUS_**|62,669|91,763<sup>d</sup>|31.7|_41.9_|_13.7_|
|**_MiddleSouth_**|22,779|32,493<sup>b</sup>|29.9|_45.1_|_4.5_|
|**Kentucky**|6,823|9,854<sup>b</sup>|30.8|_38.1_|_6.3_|
|**Maryland**|652|970<sup>c</sup>|32.8|_34.6_|_29.1_|
|**NorthCarolina**|6,990|7,347|4.9|_18.7_|_-4.2_|
|**Tennessee**|2,772|4,774<sup>b</sup>|41.9|_58.0_|_17.6_|
|**Virginia**|3,939|4,452<sup>d</sup>|11.5|_16.3_|_6.6_|
|**WestVirginia**|1,603|5,065<sup>b</sup>|68.3|_85.9_|_1.5_|
|**_NorthCentral_**|16,841|21,140<sup>d</sup>|20.3|_23.6_|_15.0_|
|**Indiana**|141|122|-16.2|_-40.6_|_8.5_|
|**Michigan**|1,430|1,681<sup>b</sup>|14.9|_16.0_|_13.8_|
|**Minnesota**|12,465|15,016<sup>c</sup>|17.0|_22.0_|_6.5_|
|**Missouri**|2,355|3,108<sup>c</sup>|24.2|_23.3_|_25.0_|
|**Wisconsin**|357|561<sup>c</sup>|36.4|_51.3_|_14.4_|
|**_Northeast_**|2,561|3,107<sup>b</sup>|17.6|_21.1_|_13.8_|
|**NewJersey**|1,273|1,751<sup>b</sup>|27.3|_33.1_|_22.3_|
|**New York**|283|330|14.3|_31.5_|_-1.5_|
|**Ohio**|146|144|-1.7|_-10.1_|_41.6_|
|**Pennsylvania**|695|742<sup>b</sup>|6.2|_12.8_|_-2.7_|
|**_Northern Plains_**|20,488|35,023<sup>d</sup>|41.5|_51.0_|_22.5_|
|**North Dakota**|5,109|5,985<sup>a</sup>|14.6|_50.9_|_25.8_|
|**Nebraska**|10,282|16,070<sup>c</sup>|36.0|_53.1_|_23.2_|
|**South Dakota**|12,818|25,931<sup>c</sup>|50.6|_65.7_|_18.8_|



1046 

43 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





1047 **Table 6 (concluded).** 

|**_Southeast_**<br>**Alabama**|84,762<br>2,609|109,156<sup>c</sup><br>3,608<sup>c</sup>|22.3<br>27.7|_32.8_<br>_32.5_|_9.1_<br>_22.6_|
|---|---|---|---|---|---|
|**Arkansas**|2,845|3,169<sup>a</sup>|10.2|_22.3_|_-0.8_|
|**Florida**|57,284|71,670<sup>b</sup>|20.1|_30.5_|_5.8_|
|**Georgia**|13,512|18,799<sup>a</sup>|28.1|_40.6_|_15.2_|
|**Lousiana**|3,895|6,309<sup>d</sup>|38.3|_50.0_|_22.8_|
|**Mississippi **|3,188|3,835<sup>c</sup>|16.9|_26.0_|_6.5_|
|**SouthCarolina**|1,429|1,765<sup>c</sup>|19.0|_22.7_|_13.3_|
|**_Southern Plains_**|232,700|280.180<sup>d</sup>|16.9|_20.2_|_14.9_|
|**Kansas**|13,054|17,890<sup>b</sup>|27.0|_29.3_|_25.9_|
|**Oklahoma**|75,181|83,693<sup>d</sup>|10.2|_13.7_|_8.6_|
|**Texas**|144,465|178,597<sup>c</sup>|19.1|_21.8_|_17.1_|
|**_WesternUS_**|1,926,656|2,206,466<sup>c</sup>|12.7|_23.1_|_2.7_|
|**_Alaska_**|393,622|601,440<sup>b</sup>|34.6|_53.3_|_5.5_|
|**_California_**|326,035|329,480|1.0|_10.2_|_-4.8_|
|**_Great Basin_**|255,075|266,716|4.4|_12.3_|_-8.0_|
|**Nevada**|180,951|193,161|6.3|_16.3_|_-10.4_|
|**Utah**|74,124|73,555|-0.8|_0.6_|_-2.5_|
|**_Northwest_**|285,862|297,519|3.9|_5.8_|_3.0_|
|**Oregon**|177,204|184,129|3.8|_4.9_|_3.1_|
|**Washington**|108,658|113,390<sup>a</sup>|4.2|_7.5_|_2.7_|
|**_Rocky Mountain_**|449,523|482,038<sup>b</sup>|6.7|_3.6_|_9.5_|
|**Colorado**|54,211|56,499<sup>c</sup>|4.0|_4.1_|_4.0_|
|**Idaho**|226,359|238,222<sup>a</sup>|5.0|_2.6_|_7.2_|
|**Montana**|122,799|134.850<sup>a</sup>|8.9|_2.9_|_15.7_|
|**Wyoming**|46,154|52,465<sup>c</sup>|12.0|_11.2_|_12.6_|
|**_Southwest_**|216,539|229,274<sup>d</sup>|5.6|_7.9_|_3.7_|
|**Arizona**|120,153|122,540<sup>a</sup>|1.9|_3.1_|_1.2_|
|**New Mexico**|96,387|106,734<sup>c</sup>|9.7|_12.4_|_7.1_|



1048 

44 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





1049 **Table 7.** Comparison of average burned area calculated by using records from the FS20 and iWED 1050 datasets from 1992 to 2020, where the letter superscripts in the iWED dataset column indicate the 1051 statistical significance for the difference between the FS20 and iWED average burned area (a: _p < 0.1_ ; 1052 b: _p < 0.05_ ; c: _p < 0.01_ ; d: _p < 0.001_ ). % burned area difference = [(iWED burned area) – (FS20 burned 1053 area)] / (iWED burned area) x 100. Data from states where average burned area was less than 100 ha 1054 yr<sup>-1</sup> are not included in this table. The data from these years, however, was used to calculate burned area 1055 at regional, sub-continental, and continental scales. 

||**Average burn**|**ed area(hayr**<sup>**-1**</sup>**)**||**% burned**|**area differe**|**nce**|
|---|---|---|---|---|---|---|
||**FS20 dataset**|**iWED dataset**|**1992-**<br>**2020**|**1992-**<br>**2001**|**2002-**<br>**2011**|**2012-**<br>**2020**|
|**_ContinentalUS_**|2,508,022|2,693,038<sup>d</sup>|7.4|11.4|6.1|6.2|
|**_Eastern US_**|138,449|149,646<sup>d</sup>|8.1|12.4|6.4|6.8|
|**_MiddleSouth_**|53,854|60,050<sup>c</sup>|11.5|21.4|5.6|4.2|
|**Maryland**|1,030|1,300<sup>b</sup>|26.1|8.3|22.6|65.6|
|**Kentucky**|17,813|21,494<sup>b</sup>|20.7|47.7|4.3|3.0|
|**NorthCarolina**|12,295|12,671<sup>b</sup>|3.1|4.5|2.3|2.5|
|**Tennessee**|8,349|9,386<sup>c</sup>|12.4|18.8|12.4|2.7|
|**Virginia**|5,617|5,959<sup>c</sup>|6.1|9.3|4.6|7.7|
|**WestVirginia**|8,682|9,172<sup>c</sup>|5.6|6.4|4.7|3.5|
|**_NorthCentral_**|31,115|34,270<sup>c</sup>|10.1|16.9|6.9|10.7|
|**Indian**|370|428<sup>a</sup>|15.6|26.0|16.0|0.0|
|**Illinois**|431|431<sup>d</sup>|0.0|0.0|0.0|0.0|
|**Iowa**|1,342|1,358|1.2|0.0|0.1|2.0|
|**Michigan**|2,236|2,319|3.7|13.4|0.5|1.8|
|**Minnesota**|17,672|18,490|4.6|14.1|-0.8|10.5|
|**Missouri**|7,685|9,855<sup>d</sup>|28.3|24.2|47.6|20.8|
|**Wisconsin**|1,379|1,388|0.7|0.9|2.1|-1.8|
|**_Northeast_**|6,317|6,589<sup>c</sup>|4.3|12.9|1.3|-2.8|
|**Connecticut**|107|107<sup>d</sup>|0.0|0.0|0.0|0.0|
|**Massachusetts**|113|127<sup>a</sup>|12.6|0.0|35.3|0.0|
|**Maine**|218|233|6.8|12.9|-2.2|0.0|
|**NewJersey**|3,766|3,987|5.9|15.1|1.1|-7.3|
|**New York**|840|846|0.8|3.8|-2.5|0.3|
|**Ohio**|321|349<sup>a</sup>|8.6|0.0|19.5|0.0|
|**Pennsylvania**|854|842|-1.4|17.0|-5.5|2.1|
|**_Northern Plains_**|47,163|48,737|3.3|-2.7|7.3|8.5|
|**North Dakota**|6,668|7,098<sup>b</sup>|6.4|2.7|3.9|11.8|
|**Nebraska**|15,397|17,225<sup>a</sup>|11.9|7.4|18.9|13.5|
|**South Dakota**|25,098|24,414|-2.7|-9.4|0.9|1.7|



1056 

45 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





1057 **Table 7 (concluded).** 

|**_Southeast_**<br>**Alabama**|161,229<br>14,780|182,526<sup>d</sup><br>15,514<sup>c</sup>|13.2<br>5.0|16.2<br>3.3|15.5<br>8.2|3.2<br>1.2|
|---|---|---|---|---|---|---|
|**Arkansas**|8,706|11,352<sup>d</sup>|30.4|41.4|34.2|12.4|
|**Florida**|76,857|84,194<sup>b</sup>|9.5|26.2|4.7|-8.2|
|**Georgia**|24,564|32,756<sup>a</sup>|33.4|3.0|37.0|68.4|
|**Louisiana**|10,181|11,079<sup>c</sup>|8.8|7.8|13.5|0.3|
|**Mississippi **|17,691|18,787<sup>c</sup>|6.2|3.3|9.6|6.3|
|**SouthCarolina**|8,450|8,844<sup>b</sup>|4.7|3.0|8.6|0.7|
|**_Southern Plains_**|265,865|356,672<sup>d</sup>|34.2|41.5|22.2|51.5|
|**Kansas**|19,502|72,409<sup>c</sup>|271.3|7.3|320.8|318.9|
|**Oklahoma**|80,240|114,322<sup>d</sup>|42.5|39.7|45.8|38.8|
|**Texas**|166,123|169,941|2.3|51.3|-2.2|-3.1|
|**_WesternUS_**|1,942,477|2,004,195<sup>d</sup>|3.2|8.4|2.4|1.2|
|**_Alaska_**|511,714|514,914|0.6|4.6|0.2|-0.6|
|**_California_**|292,091|308,573<sup>d</sup>|5.6|8.1|6.2|4.3|
|**_Great Basin_**|239,343|255,325<sup>b</sup>|6.7|10.6|7.6|8.7|
|**Nevada**|165,872|176,714<sup>b</sup>|6.5|9.4|9.6|11.7|
|**Utah**|73,471|78,611<sup>c</sup>|7.0|13.9|4.0|2.6|
|**Northwest**|255,490|260,973|2.1|14.4|-2.9|-2.5|
|**Oregon**|158,293|160,870|1.6|17.2|-6.6|-5.0|
|**Washington**|97,198|100,103<sup>a</sup>|3.0|9.8|6.4|1.3|
|**_Rocky Mountain_**|431,052|445,458<sup>d</sup>|3.3|7.4|2.9|1.2|
|**Colorado**|47,465|49,741<sup>d</sup>|4.8|18.5|3.0|2.6|
|**Idaho**|222,322|230,989<sup>c</sup>|3.9|7.0|4.2|1.2|
|**Montana**|114,487|1,171,241<sup>a</sup>|2.3|6.2|1.9|1.1|
|**Wyoming**|46,778|47,603<sup>a</sup>|1.8|7.5|-1.1|-0.3|
|**_Southwest_**|212,787|218,951|2.9|8.4|3.4|-1.9|
|**Arizona**|109,397|114,413<sup>d</sup>|4.6|18.5|3.1|0.7|
|**New Mexico**|103,390|104,538|1.1|2.7|3.7|-6.4|



1058 

46 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





|1064<br>1065||||||||||||||||||||1063|1062|1061|1059<br>1060|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|47<br>**Wisconsin**|**Missouri**|**Minnesota**|**Michigan**|**Iowa**|**Indiana**|**Illinois**|**_North Central_**|**est rgna**|**W Viii**|**Virginia**|**Tennessee**|**North Carolina**|**Maryland**|**Kentucky**|**_Middle South_**|**_Eastern US_**|**_Continental US_**|||included in this table|NICC vs. iWED =|area (a: p < 0.1; b: p|**Table 8.**Compariso<br>the letter superscript<br>|
|1,196|8,190|18,806|2,381|2,448|880|275|34,176|,|3042|6,510|11,196|14,770|1,109|14,451|51,149|133,240|2,956,403|**NICC**<br>**reports**|**Averag**|. The data fro|[(iWED burne|< 0.05; c: p <|n of average a<br>s in theFS20 a<br>|
|1,361b|6,542|19,363|2,550a|1,970|434c|576d|32,795|,|4843c|6,283|8,024|12,745c|1,260a|16,817b|50,017|137,337|2,985,584|**FS20**<br>**dataset**|**e burned area**|m these years, h|d area) – (NIC|0.01; d: p < 0.0|nnual burned ar<br>nd iWED datas<br>|
|1,368b|8,603|19,537|2,560a|1,994|488b|576d|35,125|,|5049c|6,592|8,720|13,046b|1,644b|17,484c|52,579|145,221c|3,172,337d|**iWED**<br>**dataset**|**(ha yr-1) **|owever, was us|C burned area)]|01). % differen|ea from data fr<br>ets columns ind<br>|
|13.8|-20.1|3.0|7.1|-19.6|-50.7|109.6|-4.0|.|592|-3.5|-28.3|-13.7|13.6|16.4|-2.2|3.1|1.0|**2002 to**<br>**2020**|**% diff**|ed to calcu|/ (iWED b|ce: NICC|om NICC r<br>icate the st<br>|
|_14.2_|_-36.7_|_3.8_|_-2.2_|_12.7_|_-60.2_|_99.8_|_-6.2_|_._|_416_|_6.7_|_-7.7_|_-11.8_|_13.9_|_7.7_|_1.4_|_3.6_|_1.1_|**_2002 to_**<br>**_2011_**|**erence: NI**<br>**FS20**|late burned|urned area|vs. FS20 =|eports to th<br>atistical sig<br>|
|_13.3_|_11.1_|_-0.6_|_21.4_|_-32.4_|_5.9_|_130.8_|_1.2_|_._|_887_|_-13.6_|_-43.7_|_-16.7_|_12.0_|_30.9_|_-6.9_|_2.3_|_0.9_|**_2012 to_**<br>**_2020_**|**CC vs.**|area at reg|) x 100. Da|[(FS20 bu|at calculate<br>nificance fo<br>|
|14.4|5.0|3.9|7.5|-44.6|109.6|-18.6|2.8|.|660|1.3|-22.1|-11.7|48.3|21.0|2.8|9.0|7.3|**2002 to**<br>**2020**|**% diff**|ional, sub-c|ta from sta|rned area) –|d using rec<br>r the differ<br>|
|_16.8_|_-10.5_|_2.4_|_-2.9_|_-53.0_|_99.8_|_12.8_|_-1.0_|_._|_485_|_9.5_|_4.8_|_-9.8_|_40.4_|_12.7_|_7.2_|_8.8_|_7.5_|**_2002 to_**<br>**_2011_**|**erence: N**<br>**iWED**|ontinental,|tes where a|(NICC bu|ords from t<br>ence betwe<br>|
|_11.3_|_34.2_|_9.9_|_23.5_|_5.9_|_130.8_|_-31.1_|_12.0_|_._|_954_|_-6.9_|_-42.1_|_-14.6_|_85.4_|_34.9_|_-3.0_|_9.3_|_7.1_|**_2012 to_**<br>**_2020_**|**ICC vs.**|and contin|verage bur|rned area)]|he FS20 an<br>en the NIC<br>|
|8|11|7|11|12|13|2|64||3|7|10|18|6|8|52|214|389|**FS20**<br>**All**|**Yea**|ental scal|ned area|/ (FS20 b|d iWED<br>C and the<br>|
|0|9|0|0|4|12|1|26||1|3|3|7|0|0|14|111|151|**FS20**<br>**by >**<br>**25%**|**rs when**<br>**i**|es.|was less t|urned are|datasets f<br>FS20 and<br>|
|7|9|5|8|11|13|2|55||2|8|7|14|4|6|41|192|332|**iWED**<br>**all**|**NICC > FS**<br>**WED**||han 100 ha|a) x 100. %|or 2002 to<br>iWED av<br>|
|0|7|1|0|4|10|1|23||1|3|3|6|1|0|14|106|134|**iWED**<br>**> 25%**|**20 or**||yr-1are not|difference:|2020, where<br>erage burned<br>|



https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





## 

|**Texas**|**Oklahoma**|**Kansas**|**_Southern Plains_**|**South Carolina**|**Mississippi**|**Louisiana**|**Georgia**|**Florida**|**Arkansas**|**Alabama**|**_Southeast_**|**South Dakota**|**Nebraska**|**North Dakota**|**_Northern Plains_**|**Pennsylvania**|**Ohio**|**New York**|**New Jersey**|**Massachusetts**|**Maine**|**_Northeast_**|**Table 8 (continue**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|207,999|88,753|32,486|329,238|4,531|10,629|8,911|34,982|58,530|11,499|13,720|142,800|22,973|8,903|9,562|41,438|1,384|942|613|2,312|615|261|6,477|**d).**|
|230,500|106,864a|23,936|361,299a|6.899d|15,000b|9,944|28,141|72,276c|10,951|14,709|157,920|24,953|16,198c|7,359a|48,510b|1,188c|424c|845|3,045a|167d|146d|6,016||
|224,503|152,690d|104,260c|481,453c|7,323d|16,280c|10,880b|40,367|71,658c|14,021b|15,574a|176,104c|25,163|18,453c|7,940|51,555b|1,150c|466c|839|2,972|189d|144d|5,962||
|10.8|20.4|-26.3|9.7|52.3|41.1|11.6|-19.6|23.5|-4.8|7.2|10.6|8.6|81.9|-23.0|17.1|-14.1|-55.0|37.9|31.7|-72.8|-44.3|-7.1||
|_15.4_|_37.8_|_3.0_|_18.4_|_44.5_|_30.3_|_1.4_|_-17.1_|_6.6_|_-4.7_|_16.9_|_2.7_|_32.3_|_326.3_|_-37.7_|_24.6_|_-4.4_|_-74.3_|_-31.6_|_40.0_|_-85.9_|_-59.4_|_-21.9_||
|_-1.6_|_11.0_|_-38.1_|_-2.5_|_71.1_|_69.4_|_38.8_|_-29.0_|_53.7_|_-4.9_|_-5.8_|_27.6_|_-14.0_|_48.0_|_10.4_|_10.7_|_-22.4_|_41.0_|_108.7_|_22.6_|_-41.0_|_-23.2_|_13.0_||
|7.9|72.0|220.9|46.2|61.6|53.2|22.1|15.4|22.4|21.9|13.5|23.3|9.5|107.3|-17.0|24.4|-16.9|-50.5|36.9|28.6|-69.3|-44.8|-7.9||
|_12.6_|_105.1_|_374.3_|_45.1_|_57.2_|_42.8_|_15.7_|_14.3_|_12.0_|_31.9_|_27.1_|_19.4_|_32.7_|_390.0_|_-34.7_|_29.6_|_-12.3_|_-68.9_|_-34.1_|_42.2_|_-80.9_|_-60.3_|_-21.1_||
|_-4.6_|_54.1_|_159.2_|_47.8_|_72.4_|_80.1_|_39.2_|_19.6_|_41.1_|_6.9_|_-4.7_|_31.7_|_-12.6_|_67.9_|_23.3_|_20.1_|_-20.8_|_41.0_|_109.3_|_13.6_|_-41.0_|_-23.2_|_9.9_||
|6|7|9|22|1|5|9|5|3|13|9|45|7|0|12|19|13|14|14|7|16|15|79||
|1|2|4|7|0|4|4|4|0|1|4|17|3|0|7|10|8|11|11|3|14|14|61||
|8|3|4|15|0|5|7|5|3|5|6|31|7|0|9|16|13|14|14|8|16|15|80||
|1|0|1|2|0|2|3|1|1|1|4|12|3|0|5|8|8|11|11|3|14|14|61||



https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





|1070|**New Mexico**|**Arizona**|**_Southwest_**|**Wyoming**|**Montana**|**Idaho**|**Colorado**|**_Rocky Mountain_**|**Washington**|**Oregon**|**Northwest**|**Utah**|**Nevada**|**_Great Basin_**|**_California_**|**_Alaska_**|**_Western US_**|**Table 8 (conclud**<br>1069|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||121,318|146,107|267,425|49,250|151,906|234,367|73,244|508,766|119,250|203,321|322,571|79,808|166,260|246,069|352,589|653,704|2,351,125|**ed).**|
||113,521a|142,111a|255,632b|53,026|137,070b|238,406|64,038|492,541a|122,378|199,120|321,498|77,706|161,948|239,654|363,614a|656,090|2,329,028||
||114,098a|145,163|259,260a|52,901|138,755b|244,614b|65,954|502,224|124,258a|195,733a|319,991|80,779|169,950|250,729|382,114c|655,241|2,369,559||
||-6.4|-2.7|-4.4|7.7|-9.8|1.7|-12.6|-3.2|2.6|-2.1|-0.3|-2.6|-2.6|-2.6|3.1|0.4|-0.9||
||_-12.7_|_-4.7_|_-8.8_|_7.2_|_-9.9_|_1.1_|_-35.2_|_-6.8_|_1.2_|_-4.7_|_-2.8_|_-2.0_|_2.2_|_0.8_|_9.7_|_-0.6_|_-2.0_||
||_9.9_|_-0.2_|_3.3_|_8.0_|_-9.6_|_2.3_|_6.4_|_0.0_|_3.2_|_-0.7_|_0.8_|_-3.4_|_-7.6_|_-6.3_|_-0.3_|_2.0_|_0.1_||
||-6.0|-0.6|-3.1|7.4|-8.7|4.4|-10.0|0.2|4.2|-3.7|-0.8|1.2|2.2|1.9|8.4|0.2|0.8||
||_-9.3_|_-1.5_|_-5.5_|_7.0_|_-8.7_|_5.2_|_-32.8_|_-0.4_|_3.3_|_0.1_|_1.1_|_3.0_|_1.3_|_1.9_|_16.8_|_-0.4_|_0.2_||
||_2.8_|_0.5_|_1.3_|_7.7_|_-8.6_|_3.6_|_9.2_|_1.3_|_4.5_|_-5.7_|_-1.7_|_-0.9_|_3.1_|_1.9_|_4.0_|_1.4_|_1.3_||
||9|10|19|5|13|8|10|36|8|14|22|9|10|19|5|7|108||
||3|0|3|0|1|0|5|6|2|2|4|1|2|3|0|0|16||
||9|7|16|5|14|5|7|31|7|13|20|6|9|15|3|9|94||
||3|0|3|1|1|0|5|7|1|2|3|0|1|1|0|0|14||



https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





1071 **Table 9.** Comparison of average burned area from the MTBS and iWED datasets calculated using 1072 records from 1992 to 2020, where the letter superscripts in the iWED dataset column indicate the 1073 statistical significance for the difference between the MTBS and iWED average burned area (a: p < 0.1; 1074 b: p < 0.05; c: p < 0.01; d: p < 0.001). % MTBS burned area difference = (MTBS burned area) / (iWED 1075 burned area) x 100. Data from states where average burned area was less than 100 ha yr-1 are not 1076 included in this table. The data from these years, however, was used to calculate burned area at regional, 1077 sub-continental, and continental scales. 

||**Burned are**|**a (ha yr**<sup>**-1**</sup>**)**||**% MTBS b**|**urned are**|**a**|
|---|---|---|---|---|---|---|
||**MTBS dataset**|**iWED dataset**|**1992-**<br>**2021**|**1992-**<br>**2001**|**2002-**<br>**2011**|**2012-**<br>**2020**|
|**_Contiental US_**|2,154,017|2,554,218<sup>d</sup>|84.3|71.6|86.1|90.1|
|**_Eastern US_**|57,619|129,522<sup>d</sup>|44.5|51.1|41.8|39.7|
|**_Middle South_**|15,513|42,753<sup>d</sup>|36.3|54.5|21.2|26.2|
|**Kentucky**|6,183|18,380<sup>d</sup>|33.6|69.9|10.8|9.6|
|**Maryland**|499|1,062<sup>c</sup>|47.0|3.9|55.1|75.9|
|**Tennessee**|2,677|8,669<sup>d</sup>|30.9|36.9|23.2|32.3|
|**Virginia**|2,901|5,839<sup>d</sup>|49.7|43.1|44.0|62.0|
|**West Virginia**|3,235|8,734<sup>d</sup>|37.0|50.4|12.0|17.0|
|**_North Central_**|14,015|31,287<sup>d</sup>|44.8|34.5|60.0|27.0|
|**Indiana**|88|380<sup>d</sup>|23.3|26.0|32.0|0.0|
|**Iowa**|68|1,358<sup>d</sup>|5.0|0.0|13.2|0.0|
|**Michigan**|1,220|2,254<sup>d</sup>|54.1|56.5|62.4|42.2|
|**Minnesota**|9,337|17,566<sup>d</sup>|53.2|41.3|65.2|29.5|
|**Missouri**|3,096|7,908<sup>d</sup>|39.1|26.6|65.3|31.5|
|**Wisconsin**|205|1,390<sup>d</sup>|14.7|2.7|17.0|27.2|
|**_Northeast_**|2,155|6,539<sup>d</sup>|33.0|34.4|35.8|28.4|
|**Connecticut**|0|107<sup>d</sup>|0.0|0.0|0.0|0.0|
|**Maine**|19|232<sup>d</sup>|8.0|6.4|24.3|0.0|
|**Massachussetts**|10|128<sup>d</sup>|7.9|0.0|18.1|0.0|
|**New Jersey**|1,600|3,884<sup>d</sup>|41.2|45.8|39.6|33.5|
|**New York**|157|850<sup>d</sup>|18.4|0.0|42.2|23.7|
|**Ohio**|60|343<sup>d</sup>|17.5|0.0|39.1|0.0|
|**Pennsylvania**|310|895<sup>d</sup>|34.6|0.0|30.1|47.3|
|**_Northern Plains_**|25,937|48,943<sup>d</sup>|53.0|60.3|44.4|54.3|
|**North Dakota**|2,930|6,989<sup>d</sup>|41.9|63.9|43.0|23.4|
|**Nebraska**|11,099|16,459<sup>d</sup>|67.4|83.8|62.5|59.4|
|**South Dakota**|11,908|25,495<sup>d</sup>|46.7|46.1|39.2|58.8|



1078 

50 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





1079 **Table 9 (concluded).** 

|**_Southeast_**|77,268|170,550<sup>d</sup>|45.3|35.8|55.9|41.1|
|---|---|---|---|---|---|---|
|**Alabama**|1,645|15,047<sup>d</sup>|10.9|10.5|13.6|7.0|
|**Arkansas**|3,722|9,380<sup>d</sup>|39.7|38.9|52.4|21.3|
|**Florida**|42,746|76,992<sup>d</sup>|55.5|51.9|63.3|51.5|
|**Georgia**|20,851|32,278<sup>d</sup>|64.6|23.1|78.7|58.5|
|**Louisiana**|4,359|10,349<sup>d</sup>|42.1|35.4|52.4|33.6|
|**Mississippi **|2,495|18,009<sup>d</sup>|13.9|7.4|17.4|21.9|
|**SouthCarolina**|1,450|8,494<sup>d</sup>|17.1|10.7|24.5|18.4|
|**_Southern Plains_**|225,462|278,655<sup>b</sup>|80.9|69.5|74.5|96.2|
|**Kansas**|49,306|20,719<sup>b</sup>|238.0|112.9|304.2|245.0|
|**Oklahoma**|69,232|85,044<sup>c</sup>|81.4|54.5|71.9|94.8|
|**Texas**|106,924|172,892<sup>d</sup>|61.8|68.9|62.6|55.9|
|**_WesternUS_**|1,793,667|1,975,492<sup>d</sup>|90.8|79.1|94.0|94.2|
|**_Alaska_**|464,141|512,989<sup>b</sup>|90.5|52.4|99.5|94.7|
|**_California_**|276,829|301,735<sup>d</sup>|91.7|80.5|87.3|98.4|
|**_Great Basin_**|231,517|249,116<sup>d</sup>|92.9|90.7|93.3|95.1|
|**Nevada**|163,251|172,664<sup>d</sup>|94.5|92.0|95.7|96.2|
|**Utah**|68,267|76,452<sup>d</sup>|89.3|87.0|88.6|92.4|
|**_Northwest_**|237,692|256,427<sup>d</sup>|92.7|85.1|92.6|95.4|
|**Oregon**|146,715|157,505<sup>d</sup>|93.1|85.2|93.3|96.0|
|**Washington**|90,977|98,922<sup>d</sup>|92.0|85.0|91.0|94.4|
|**_Rocky Mountain_**|397,699|440,562<sup>d</sup>|90.3|88.5|90.8|91.0|
|**Colorado**|39,330|48,196<sup>d</sup>|81.6|72.2|79.0|84.8|
|**Idaho**|214,320|226,818<sup>d</sup>|94.5|92.9|93.8|96.5|
|**Montana**|103,685|118,361<sup>d</sup>|87.6|79.6|91.4|88.5|
|**Wyoming**|40,364|47,186<sup>d</sup>|85.5|90.2|83.5|84.2|
|**_Southwest_**|185,789|214,663<sup>d</sup>|86.5|74.4|91.3|87.9|
|**Arizona**|100,916|111,176<sup>d</sup>|90.8|79.0|95.1|90.2|
|**New Mexico**|84,872|103,487<sup>d</sup>|82.0|71.7|87.3|83.7|



1080 

51 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





|**_10. Substituting MTBS size for fire management size_**<br>1082<br>1083|**_9. Identifying matched records that had merged_**|**_8. Identifying matched records that hadjoined_**|**_7. Identifying MTBS and fire management records that spanned international borders_**|**_6. Adjusting or reallocating fire management and/or MTBS size_**|**_5 . Identifying FM records named as complexes that had multiple fires_**|**_4. Identifying MTBS records with multipleperimeters_**|**_3. Adding of fire management records_**|**_2. Reclassifying unmatched MTBS Unknown and Prescribed Fire records_**|**_1. Identifying matched MTBS Unknown and Prescribed Fire records_**|**Process**||**Table 10.**Processes used duringthe development of the iWED that changed the numbe<br>1081|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||**+/-**|**-**|**-**|**+/-**||**+/-**||**+**|**+**|**M**|**MT**<br>**num**|r and si|
||**+**|||||||**+**||**M-P**|**BS**<br>**ber**|zes of|
||**+/-**|**-**|**-**|**+/-**||**-**||||**M**|**MTBS**|mega an|
||**+**|||||**-**||||**M-P**|**size**|d meg|
|**+/-**|**+/-**|||**+/-**|**-**|**+/-**|**+**|||**M**|**FM n**|a-plus|
|**+/-**|**+**||||||**+**|||**M-P**|**umber**|fires.|
|**+/-**|**+/-**||**-**|**+/-**||**-**||||**M**|**FM**||
|**+/-**|**+**|||||**-**||||**M-P**|**size**||
|S29|S11-S14,S20|S16|S21,S22|S13,S20||S3,S4,S5,S6||||**Examples**|||



https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 

1088 





1084 **Table 11.** Percentage of the total number of mega and mega-plus fires as a function of total number of 1085 larger wildfire records for different study areas and the percentage of area burned in mega and mega1086 plus fires. 

1087 

|||**Number of records**|||**Burned area**||
|---|---|---|---|---|---|---|
||**Mega **|**Mega-plus**|**Total**|**Mega **|**Mega-plus**|**Total**|
|**ContinentalUS**|8.1|0.4|8.5|49.3|14.6|63.9|
|**EasternUS**|2.8|0.0|2.8|33.8|0.0|33.8|
|**Southeast**|3.8|0.3|4.0|32.4|18.5|50.9|
|**Southern Plains**|4.1|0.3|4.5|32.4|17.3|49.6|
|**WesternUS**|11.0|0.5|11.5|52.7|14.6|67.3|



53 

https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 



|**Western US**<br>1091<br>1092|**Southern Plains**|**Southeast**|**EasternUS**|**ContinentalUS**||**WesternUS**|**Southern Plains**|**Southeast**|**EasternUS**|**ContinentalUS**||**WesternUS**|**Southern Plains**|**Southeast**|**EasternUS**|**ContinentalUS**||||Also included are<br>1090|**Table 12.**Summar<br>1089|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|10,495|2,498|2,028|2,668|17,689||9,373|1,666|1,290|1,360|13,689||10,108|2,259|1,966|2,508|16,841||**Total**|**N**|percentage|y of the nu|
|1,126|76|77|63|1,342||1,101|59|50|60|1,270||1,108|71|74|61|1,314||**Mega **|**umber of**|differen|mber of|
|56|7|6|0|69|**_iWED-_**|49|6|6|0|61|**_MTBS-_**|49|7|5|0|61|**_FS20-pl_**|**Mega-plus**|**records**|ces between th|and average bu|
|1,881,564|206,188|90,149|78,856|2,256,757|**_F dataset_**|1,808,350|168,307|67,237|59,096|2,102,990|**_A dataset_**|1,813,424|192,371|83,888|74,378|2,164,061|**_us dataset_**|**Total**|**Bur**|e number o|rned in larg|
|979,931|56,713|28,336|25,009|1,089,989||980,223|47,415|20,901|23,749|1,072,287||967,217|54,078|28,590|24,783|1,074,668||**Mega **|**ned area(ha**|f and area b|er fire reco|
|291,599|38,549|17,320|0|347,467||258,237|33,637|15,817|0|307,690||246,273|38,549|12,622|0|297,444||**Mega-plus**|**yr-1)**|urned for di|rds using dif|
|387|239|62|160|848||735|593|676|1,148|3,152||||||||**Total**|**Diff**|fferent d|ferent w|
|18|5|3|2|28|**_i_**|7|12|24|1|44|**_F_**|||||||**Mega **|**erence in**<br>**reco**|atasets.|ildfire e|
|7|0|1|0|8|**_WED-F versus F_**|0|1|-1|0|0|**_S20-plus versus_**|||||||**Mega-plus**|**number of**<br>**rds**||vent datasets.|
|3.8|7.2|7.5|6.0|4.3|**_S20-plu_**|0.3|14.3|24.8|25.9|2.9|**_MTBS-A_**|||||||**Total**|||Data ar|
|1.3|4.9|-0.9|0.9|1.4|**_s recordsb_**|-1.3|14.1|36.8|4.4|0.2|**_recordsa_**|||||||**Mega **|**% of bur**||e from 1|
|18.4|0.0|37.2|0.0|16.8||-4.6|14.6|-20.2|0.0|-3.3||||||||**Mega-plus**|**ned area**||992 to 2021.|





https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 



|1094|
|---|



|55|
|---|





|cPositive differences<br>dPositive differences|bPositive differences|aPositive occurred w|**WesternUS**|**Southern Plains**|**Southeast**|**EasternUS**|**ContinentalUS**||**WesternUS**|**Southern Plains**|**Southeast**|**EasternUS**|**ContinentalUS**||**Table 12 (conclud**<br>1093|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|occurred whe<br>occurred whe|occurred whe|hen burrned ar|11,160|3,165|2,569|3,056|19,950||9,669|2,003|1,585|1,616|14,873||**ed).**|
|n burrned<br>n burrned|n burrned|ea from th|1,127|138|80|62|1,407||1,085|126|54|57|1,322|||
|area fr<br>area fr|area fr|e FS2|57|8|5|0|70||55|8|5||68|||
|om the iWED-M r<br>om the iWED-F/M|om the iWED-F re|0-plus records bein|1,884,041|284,202|104,413|86,647|2,359,302|**_iWED-F/M data_**|1,819,738|228,021|75,611|62,621|2,185,991|**_iWED-M datase_**||
|ecords being great<br>records being gre|cords being greate|g greater than bur|976,568|97,737|31,609|24,015|1,129,930|**_set_**|953,526|92,464|22,868|22,483|1,091,341|**_t_**||
|er than burned a<br>ater than burne|r than burned ar|ned area from M|294,043|37,432|16,155|0|347,630||281,587|37,432|16,155||335,174|||
|rea from MTBS<br>d area from FS2|ea from FS20-p|TBS-A records|1,052|906|603|548|3,109||296|337|295|256|1,184|||
|-A record<br>0-plus rec|lus record|.|19|67|6|1|93|**_iWED-F/  _**|-16|67|4|-3|52|**_iWED-_**||
|s.<br>ords.|s.||8|1|0|0|9|**_M vers_**|6|2|-1|0|7|**_M  vers_**||
||||3.9|47.7|24.5|16.5|9.0|**_us FS20-plu_**|0.6|35.5|12.5|6.0|3.9|**_us MTBS-A_**||
||||1.0|80.7|10.6|-3.1|5.1|**_s recordsd_**|-2.7|95.0|9.4|-5.3|1.8|**_recordsc_**||
||||19.4|-2.9|28.0|0.0|16.9||9.0|11.3|2.1|0.0|8.9|||



https://doi.org/10.5194/essd-2026-660 Preprint. Discussion started: 21 October 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 1095 **Figure 1.** Flowchart illustrating the datasets, methods, steps, and phases used during the 1096 development of the integrated Wildland Fire Dataset (iWED). 

- 1097 

1098 



<!-- Start of picture text -->
Web-Based Applications (Sect. 2.3)<br>1. Search Engines<br>2. Wildland Fire Emissions Inventory System<br>3. OneStreetMap<br>4. Google Maps<br>Image Interpretation (Sect. 2.3)<br>1. Identification and analysis of multiple perimeters in an<br>MTBS event<br>2. Reclassification of MTBS events<br>3. Matching MTBS and fire management events<br>4. Identification of merged perimeters<br>Datasets (Sect. 2.2) 5. Comparison of perimeters and burned area pixels<br>1. USFS 1992-2015 events 6. Identification of errors in MTBS calculation of event<br>2. USFS 1992-2018 events size<br>3. USFS 1992-2021 events<br>4. ICS events<br>5. Regional and national<br>databases and reports<br>6. Incident management  Study Phases (Sect. 2.4)<br>situation reports (NICC, AICC) 1. Import and integrate events from fire<br>7. Other government and media  management datasets and reports<br>reports (WWW searches) 2. Import, integrate, and analyze MTBS fire events<br>8. Fire management perimeters 3. Resolve uncertainties and ambiguities in wildfire<br>9. MTBS datasets and imagery complexes and individual events<br>10. Landsat burned area product 4. Determine the causes for larger (>30%)<br>11. MODIS burned area product differences between MTBS and fire management<br>12. Fine-resolution aerial  sizes<br>photography 5. Determine the causes for smaller (15-30%)<br>differences between MTBS and fire management<br>sizes<br><!-- End of picture text -->

56 
