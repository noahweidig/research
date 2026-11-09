---
title: A spatial database of wildfires in the United States, 1992-2011
authors:
- Short, Karen C.
year: '2014'
journal: Earth System Science Data
doi: 10.5194/essd-6-1-2014
tags:
- geospatial data
- united states
- wildfire
- wildfire occurrence
zotero_key: 4S48YBG7
item_type: journalArticle
url: https://essd.copernicus.org/articles/6/1/2014/
source_url: 'unpaywall: https://essd.copernicus.org/articles/6/1/2014/essd-6-1-2014.pdf'
fulltext_status: fulltext
synced: '2026-11-09'
---

# A spatial database of wildfires in the United States, 1992-2011

## Abstract

The statistical analysis of wildfire activity is a critical component of national wildfire planning, operations, and research in the United States (US). However, there are multiple federal, state, and local entities with wildfire protection and reporting responsibilities in the US, and no single, unified system of wildfire record keeping exists. To conduct even the most rudimentary interagency analyses of wildfire numbers and area burned from the authoritative systems of record, one must harvest records from dozens of disparate databases with inconsistent information content. The onus is then on the user to check for and purge redundant records of the same fire (i.e., multijurisdictional incidents with responses reported by several agencies or departments) after pooling data from different sources. Here we describe our efforts to acquire, standardize, error-check, compile, scrub, and evaluate the completeness of US federal, state, and local wildfire records from 1992–2011 for the national, interagency Fire Program Analysis (FPA) application. The resulting FPA Fire-Occurrence Database (FPA FOD) includes nearly 1.6 million records from the 20 yr period, with values for at least the following core data elements: location, at least as precise as a Public Land Survey System section (2.6 km2 grid), discovery date, and final fire size. The FPA FOD is publicly available from the Research Data Archive of the US Department of Agriculture, Forest Service (doi:10.2737/RDS-2013-0009). While necessarily incomplete in some aspects, the database is intended to facilitate fairly high-resolution geospatial analysis of US wildfire activity over the past two decades, based on available information from the authoritative systems of record.

## Full text

Earth System Science Data 

Earth Syst. Sci. Data, 6, 1–27, 2014 www.earth-syst-sci-data.net/6/1/2014/ doi:10.5194/essd-6-1-2014 © Author(s) 2014. CC Attribution 3.0 License. 



# **A spatial database of wildfires in the United States, 1992–2011** 

**K. C. Short** 

USDA Forest Service, Rocky Mountain Research Station, Missoula Fire Sciences Laboratory, 5775 US Hwy 10 W, Missoula, Montana, 59808, USA 

_Correspondence to:_ K. C. Short (kcshort@fs.fed.us) 

Received: 13 June 2013 – Published in Earth Syst. Sci. Data Discuss.: 3 July 2013 Revised: 7 December 2013 – Accepted: 10 December 2013 – Published: 3 January 2014 

**Abstract.** The statistical analysis of wildfire activity is a critical component of national wildfire planning, operations, and research in the United States (US). However, there are multiple federal, state, and local entities with wildfire protection and reporting responsibilities in the US, and no single, unified system of wildfire record keeping exists. To conduct even the most rudimentary interagency analyses of wildfire numbers and area burned from the authoritative systems of record, one must harvest records from dozens of disparate databases with inconsistent information content. The onus is then on the user to check for and purge redundant records of the same fire (i.e., multijurisdictional incidents with responses reported by several agencies or departments) after pooling data from different sources. Here we describe our efforts to acquire, standardize, error-check, compile, scrub, and evaluate the completeness of US federal, state, and local wildfire records from 1992–2011 for the national, interagency Fire Program Analysis (FPA) application. The resulting FPA Fire-Occurrence Database (FPA FOD) includes nearly 1.6 million records from the 20 yr period, with values for at least the following core data elements: location, at least as precise as a Public Land Survey System section (2.6 km<sup>2</sup> grid), discovery date, and final fire size. The FPA FOD is publicly available from the Research Data Archive of the US Department of Agriculture, Forest Service (doi:10.2737/RDS-2013-0009). While necessarily incomplete in some aspects, the database is intended to facilitate fairly high-resolution geospatial analysis of US wildfire activity over the past two decades, based on available information from the authoritative systems of record. 

## **1 Introduction** 

The statistical analysis of wildfire activity has long been a critical component of national wildfire planning, operations, and research in the United States (US) (Show and Kotok, 1923; Brown, 1959; Hardy and Hardy, 2007). The analysis of historical fire and weather records, for example, is currently integral to national fire danger rating applications (Andrews and Bradshaw, 1997; Bradshaw and McCormick, 2000; Andrews et al., 2007), fire-potential forecast models (Andrews et al., 2007), and several widely used geospatial fire modeling systems (Stratton, 2006; e.g., Sanborn, 2009; Ager et al., 2010; Finney et al., 2011). These operational systems are relied upon to generate consistent national data for risk assessment, planning, budget formulation, and decision support at multiple scales (Buckley et al., 2006; Hardy and 

Hardy, 2007; Calkin et al., 2010; Wolf and Buckley, 2010; Finney et al., 2011; Noonan-Wright et al., 2011; Thompson et al., 2011; Miller and Ager, 2012; Scott et al., 2012; WRSC, 2012). Outside of the operational realm, spatiotemporal analyses of US wildfire activity are increasingly used to characterize local, regional, and national patterns and trends as they relate to factors such as climate, population, land use, and fire policy, and to predict how wildfire activity and values at risk may be influenced by changes in those factors (e.g., McKenzie et al., 2003; Gedalof et al., 2005; Stephens, 2005; Collins et al., 2006; Westerling et al., 2006; Parisien and Moritz, 2007; Miller et al., 2008; Littel et al., 2009; Preisler et al., 2009; Davis and Miller, 2010; Miller et al., 2012; Parisien et al., 2012). 

Published by Copernicus Publications. 

K. C. Short: A spatial database of wildfires in the United States 

2 

US wildfire activity statistics have been reported in various forms since the early 20th century. State- and national-level estimates of wildfire numbers and area burned, for example, are available for circa 1912 to 1997 in US Department of Agriculture, Forest Service (USFS) wildfire statistics publications (e.g., USFS, 1998a) and from circa 1999 to present from the Predictive Services Intelligence Section at the National Interagency Coordination Center (e.g., NICC, 2012b). The USFS wildfire statistics, often referred to as “Smokey Bear Reports”, summarize wildfire activity by US state and therefore lend themselves only to analyses at the level of the state or interstate region. The NICC statistics, published in Wildland Fire Summary and Statistics Annual Reports, are based on calendar-year summaries of wildfire activity from the interagency Situation Report/209 (SIT/209) application (USFS, 2009). The Situation Report (SIT) module of the SIT/209 application keeps a running tally of wildfires and area burned by agency unit (including participating federal, state, local, and private entities) based on daily activity reports from dispatch offices during fire season and weekly reports otherwise (NIFC, 2011; NICC, 2012a). Detailed information regarding individual large fires and other significant incidents is entered separately into the Incident Command System – 209 (ICS-209) module of the SIT/209 application, generally by local dispatch personnel or by the team managing the incident (NIFC, 2011; NICC, 2012a). In sum, the ICS-209 provides detailed, incident-specific information, but only for significant events (e.g., large fires), while the SIT provides daily and cumulative (year-to-date) total fire counts and area-burned estimates for all fires reported by dispatch offices, summarized by agency unit. The SIT/209 system was designed for tactical support (e.g., to help determine firefighting priorities and resource needs), and while its estimates of wildfire numbers and area burned may be the best available at the time of need (i.e., to characterize the current “situation”), they are not necessarily complete or accurate and thus should be considered initial figures only (NFAEB, 2007; NIFC, 2011). Internal inconsistencies (i.e., in the SIT versus ICS-209 modules) and inconsistencies with other data sources (e.g., agency fire reports, described below) are not necessarily reconciled before the final NICC annual wildfire activity statistics are published (C. Leonard, personal communication, 2011). Despite their potential weaknesses, the published NICC numbers have commonly been used to characterize national, regional, and subregional (e.g., state) wildfire activity levels in recent decades (e.g., Andrews, 2005; Hammer et al., 2009; Urbanski et al., 2009; Kolden and Brown, 2010; Reid et al., 2010; Thomas and Butry, 2012). 

Incident-level wildfire reporting also occurs within each of the five major US federal agencies with wildland-firemanagement programs, as they are required to complete Individual Fire Reports for all fires under federal protection or on federal ownership and to enter that information into their respective systems of record. These “final fire reports” are intended to be the authoritative sources of wildland fire ac- 

tivity statistics for the federal agencies. The USFS uses the FIRESTAT application (USFS, 2003) to transmit and archive data entered from the FS-5100-29 Individual Fire Report form (Donoghue, 1982a; USFS, 2000) into the National Interagency Fire Management Integrated Database (NIFMID) (USFS, 1998b; Bunton, 2000). The USFS fire reports in NIFMID, which is accessible via the national Fire and Aviation Management Web Applications site (FAMWEB, https: //fam.nwcg.gov/fam-web/), currently date back to 1970. The four major US Department of the Interior (USDI) agencies with wildland fire programs all use the DI-1202 Individual Fire Report form, but the Bureau of Indian Affairs (BIA), Bureau of Land Management (BLM), and National Park Service (NPS) enter and store the information in the Wildland Fire Management Information (WFMI) system, while the US Fish and Wildlife Service (FWS) archives its data using a separate application, the Fire Management Information System (FMIS). The USDI fire reports date back to the 1960s. Most state and some local entities have independent reporting systems of their own, with records for various periods. The states of California and Oregon, for example, maintain publicly accessible incident-level databases that are distinct from each other and the federal systems. In addition, there are currently two national non-federal reporting systems, which are used increasingly either in concert with, or in lieu of, a state-maintained system. The National Association of State Foresters (NASF) database is intended to be a clearinghouse of state-fire-service wildfire records, accessible via the FAMWEB data warehouse, while the National Fire Incident Reporting System (NFIRS) of the US Fire Administration (USFA) is intended to capture incident information, including wildfire data, from US fire departments (i.e., city, district, county), as overseen by state fire marshal offices (Hall and Harwood, 1989; Thomas and Butry, 2012). Although NFIRS is administered by a federal agency (USFA), we refer to it as a non-federal system, because it includes fire reports from local departments rather than from federal agencies. (Abbreviations, acronyms, and aliases used repeatedly throughout this paper are defined in Appendix A.) 

While incident-level reporting and corporate data warehousing (e.g., via FAMWEB, WFMI; see Bunton, 2000) have facilitated _intra-_ agency analyses of recent decades’ wildfire activity, data from the various disparate systems cannot be readily integrated for a true interagency analysis of historical wildfire activity from the official systems of record. Fire data from FAMWEB and WFMI, for example, can be imported in just a few steps into FireFamilyPlus (FFP), which is the analysis system commonly used for US fire danger rating and other historical fire-weather analyses (Bradshaw and McCormick, 2000), but FAMWEB has FFP-ready non-federal data (including detailed instructions for importing them) currently available for California only. Moreover, while FFP checks for duplicate fire records upon import, it will not necessarily catch redundant incident information from different systems of record. The onus, therefore, is on the user 

Earth Syst. Sci. Data, 6, 1–27, 2014 

www.earth-syst-sci-data.net/6/1/2014/ 

K. C. Short: A spatial database of wildfires in the United States 

3 

intending to analyze wildfire occurrence to check for and purge redundant records of the same fire after pooling data from different sources. The redundant records will tend to be of multijurisdictional incidents (e.g., automatic aid incidents, large fires impacting multiple ownerships) with responses reported by several firefighting entities (see Bunton, 1999; Artley, 2009). 

The problems with data compilation from the multiple wildfire systems of record affect far more than FFP users, however, and there have been repeated calls for a single fireoccurrence database to support national operations and research. In 1995, the Federal Wildland Fire Policy recognized that “accurate, organized, and accessible information about natural/cultural resources and fire activities is the basis for coordinated agency program decisions and is crucial to effective and efficient program management” and called for federal agencies to “standardize fire statistics and develop an easily accessible common database” (USDI and USDA, 1995). The necessary business analysis subsequently was performed with oversight from the National Wildfire Coordinating Group (NWCG). The resulting National Interagency Fire Statistics Information Project (NIFSIP) delivered business-process and conceptual data models for an interagency fire-reporting system that could be coordinated with non-federal cooperators and allow upward reporting of federal information to NFIRS (USFS, 1998c; Bunton, 1999), but no system was actually developed. The need for one persisted, however, and the 2001 update to the 1995 Federal Wildland Fire Policy again included a call for development of “coordinated databases for federal fire information that support fire program development and [policy] implementation” (USDI et al., 2001). By that time, however, it was becoming increasingly clear just how daunting that task would be, especially if non-federal data integration was to remain part of the ultimate goal. 

Not long after the 2001 fire policy update was released, reports from three notable and independent efforts to compile wildland fire occurrence data from the various systems of record were published. In 2002, Westerling et al. (2003) compiled more than 400 000 wildland fire records spanning 20–30 yr from the USFS, BLM, BIA, and NPS for western US fire-climate analyses. Due to “data quality [sic] concerns”, BLM reports of fires that occurred prior to 1980 were excluded from the research data set, which subsequently contained approximately 300 000 fire records from western federal lands for the period 1980–2000. The climatological analyses of Westerling et al. (2003) hinged on having fire location information more specific than state, county, or agency unit. They explained that the quality of the location data for some of the records, particularly the “older” subset, “constrains a comprehensive, regional-scale analysis to a 1- degree [approximately 111 km] grid resolution.” Westerling et al. (2003) did not indicate whether further quality-control measures were taken to remove redundant records from the resulting gridded data set of fires and area burned. 

Brown et al. (2002) reported to the NWCG specifically regarding the completeness and quality of the fire data from the US federal systems of record. They evaluated all agency firereport data from 1970–2000 but, like Westerling et al. (2003), considered the USDI fire-occurrence data to “effectively start in 1980” due to “very minimal” reporting prior. Brown et al. (2002) deemed fire records “usable” if they included apparently accurate (or correctable) values for the following data elements: (1) discovery date, (2) location (latitude/longitude), (3) total area burned, and (4) cause. Locations that could be converted to latitude/longitude from a Public Land Survey System (PLSS) section (2.6 km<sup>2</sup> grid) identifier were considered viable. Their quality-control efforts included checking for duplicate records (both intraagency and interagency). A duplicate, or identical, record was defined by Brown et al. (2002) as having “exactly the same values for all fields” as another record in the data set. Of the 657 949 federal fire records evaluated, only 538 809 could be flagged as usable and non-redundant per their criteria. While their work was invaluable in pointing out problems related to the completeness, quality, and consistency of core elements of wildfire data in the federal systems of record, Brown et al. (2002) considered the data set of Schmidt et al. (2002), which focused on a shorter period of record, to be the only “quality controlled [sic] historical observed individual federal fire occurrence set” available at the time. 

The work of Schmidt et al. (2002) was particularly remarkable because it included efforts to compile core data from 1986 through 1996 from federal _and non-federal_ fire reporting systems, further illuminating the great inconsistencies between the systems and underscoring both the need for and the challenge of building a national wildfireoccurrence database. Like Westerling et al. (2003) and Brown et al. (2002), Schmidt et al. (2002) considered fire location to be a core data element, as their intended use of the data set was for geospatial fire analysis and risk assessment. They sought the same elements as Brown et al. (2002) plus an identifying fire number and, where available, fire name and containment date. While they acquired non-federal data from all conterminous states except for Nevada, several states lacked fire records for entire years or lacked values for core data elements, including area burned. Moreover, the non-federal fire records were often georeferenced only to the county level, if at all. While they expected there to be redundant records from the federal and non-federal systems, they could not identify them “because fire locations are generally imprecise (to the nearest [PLSS] section), and not all database fields that could aid in tracking duplicates are fully populated” (Schmidt et al., 2002). They invested two and a half person-years to compile the 11 years’ worth of national fire-occurrence data and concluded that even basic estimates of total fire numbers and area burned nevertheless would be restricted to the state level in many cases and, moreover, be compromised by both missing and redundant records. 

Earth Syst. Sci. Data, 6, 1–27, 2014 

www.earth-syst-sci-data.net/6/1/2014/ 

K. C. Short: A spatial database of wildfires in the United States 

4 

Building on the initial efforts of the NIFSIP and informed to some degree by the work of Brown et al. (2002) and Schmidt et al. (2002), progress toward a national firereporting system ostensibly has been made over the last decade (see NWCG, 2003; NFAEB, 2007). Still, no such system exists. In 2003, a prototype for the national Fire Program Analysis (FPA) system was initiated, and it was recognized that several components of that system would rely on historical wildfire activity data from both federal and non-federal systems of record. FPA is a national, interagency application intended to evaluate the effectiveness of alternative firemanagement strategies and thereby support national planning activities and budget development (see Mavsar et al., 2013). FPA requires wildfire activity data as inputs to, and for evaluation of output from, its Initial Response Simulator (see Fried and Fried, 2010) and Large Fire Module (see Finney et al., 2011). For these purposes, the wildfire records must include, at minimum (1) location, at least as precise as PLSS section, (2) discovery date, and (3) final fire size. Some additional elements such as fire name, cause, and containment date are sought but not required for a record to be considered “viable”. Interagency guidance to FPA was to exclude fire records older than 1992 from consideration due to concerns about both the quality and the completeness of the data (J. Fotjik, personal communication, 2012). 

FPA was released in 2008, and the first national analysis was completed in 2009 (USDI, 2009). At that time the system drew upon a wildfire data set spanning 1992–2008 that included records from the federal systems of record as well as the NASF database and NFIRS. The data were compiled and quality-checked in a manner that expanded upon the approaches used by Brown et al. (2002) and Schmidt et al. (2002). The original process, documented in an unpublished technical guide (FPA, 2010), was adapted in 2010 to include additional non-federal data from state-maintained systems of record and to more thoroughly screen the compiled data set for redundant records. Data for 2009–2010 were added during the winter of 2011. Data for 2011 and previously absent records from prior years were acquired from the NASF database via FAMWEB and added during the winter of 2012. The resulting national spatial database of US wildfires 1992–2011, referred to as the FPA Fire-Occurrence Database (FPA FOD), is presented and described here. Only the subset of basic elements used by FPA is included, but additional attributes can be drawn from the source systems using the identifier of the original record, which is retained in the FPA FOD. Record identifiers from the ICS-209 application and the satellite-derived Monitoring Trends in Burn Severity (MTBS) national fire-perimeter data set (Eidenshink et al., 2007) are also included for a subset of the fires, providing, in essence, bridges to those information systems. We evaluate the completeness of the resulting data set by comparing estimates of wildfire numbers and area burned from the FPA FOD with published wildfire activity statistics by state and year. 

## **2 Methods** 

## 2.1 Data sources 

Wildfire records for the period 1992–2011 were acquired from federal, non-federal, and interagency systems of record (Table 1). Records were required to have values for the following attributes to be considered candidates for inclusion in the FPA FOD: (1) location at least as precise as PLSS section, (2) discovery date, and (3) final fire size. Candidate non-federal records were available from the two national, non-federal reporting systems (NASF, NFIRS) only for a subset of states and years, largely due to limited state and local participation and a lack of sufficient location information in submitted fire reports. Additional candidate non-federal data were acquired from state-maintained and interagency systems to augment the subset drawn from NASF and NFIRS. FPA staff associated with the Alabama Forestry Commission (AFC) provided AFC data for 2003– 2009, and the Texas A&M Forest Service (TFS) provided a compiled data set of state and local wildfires reported to the TFS since 2005. Due to time constraints, data were not sought directly from all other US states and territories. Instead, we drew non-federal wildfire data that were readily available online and capitalized on past and present efforts to compile non-federal fire records, obtaining multi-state data sets from the other projects. Publicly available wildfire data were downloaded from the Alaska Interagency Coordination Center (http://fire.ak.blm.gov/), the Oregon Department of Forestry (http://www.oregon.gov/ODF/GIS/gisdata. shtml), the Virginia Department of Forestry (http://www. dof.virginia.gov/gis/dwnload/index.htm), and the Wisconsin Department of Natural Resources (ftp://gomapout.dnr. state.wi.us/geodata/forestry/fire_occurrence.zip). Data from the California Department of Forestry and Fire Protection were downloaded from FAMWEB (http://fam.nwcg. gov/fam-web/weatherfirecd/fire_files.htm). Multi-state nonfederal data sets for at least part of the period of interest were obtained from Schmidt et al. (2002), the Southern Wildfire Risk Assessment (SWRA; see Buckley et al., 2006), the MTBS project, and the USFS Eastern Forest Environmental Threat Assessment Center (EFETAC) (Table 1). 

## 2.2 Data processing and quality control 

The data sought from each system of record are listed in Table 2. Only location (PLSS section or better), discovery date, and final fire size were required. Once identified, candidate records were extracted, standardized (Sect. 2.2.1), screened for obvious errors (Sect. 2.2.2), and compiled into a single database (Sect. 2.2.3), which was then checked for redundancy (Sects. 2.2.4 and 2.2.5). 

Earth Syst. Sci. Data, 6, 1–27, 2014 

www.earth-syst-sci-data.net/6/1/2014/ 

K. C. Short: A spatial database of wildfires in the United States 

5 

**Table 1.** Sources of wildfire data in the FPA FOD. Although the National Fire Incident Reporting System is administered by a federal agency (USFA), we refer to it as a non-federal system, because it includes fire reports from local departments rather than from federal agencies. We distinguish the Alaska Interagency Coordination Center and ICS-209 as interagency systems, because they are sources of federal, state, and local reports. 

|Category|Source|FOD Acronym|
|---|---|---|
|Federal|USDI Wildland Fire Management Information System<br>FWS Fire Management Information System|DOI-WFMI<br>FWS-FMIS|
||USFS Fire Statistics|FS-FIRESTAT|
|Non-federal|USFA National Fire Incident Reporting System<br>National Association of State Foresters|FA-NFIRS<br>ST-NASF|
||Alabama Forestry Commission (AFC)<sup>a,b</sup>|ST-ALALS|
||Arkansas Forestry Commission<sup>a,c</sup>|ST-ARARS|
||Arizona State Forestry Division<sup>d</sup>|ST-AZAZS|
||California Department of Forestry and Fire Protection|ST-CACDF|
||Colorado State Forest Service<sup>e</sup>|ST-COCOS|
||Connecticut Division of Forestry<sup>f</sup>|ST-CTCTS|
||Florida Forest Service<sup>g</sup>|ST-FLFLS|
||Georgia Forestry Commission<sup>h</sup>|ST-GAGAS|
||Kentucky Division of Forestry<sup>i</sup>|ST-KYKYS|
||Louisiana Office of Forestry<sup>j</sup>|ST-LALAS|
||Maine Forest Service<sup>k</sup>|ST-MEMES|
||Michigan Department of Natural Resources<sup>d,l</sup>|ST-MIMIS|
||Missouri Department of Conservation<sup>m</sup>|ST-MOMOS|
||Mississippi Forestry Commission<sup>n,o</sup>|ST-MSMSS|
||Montana Department of Natural Resources & Conservation<sup>n</sup>|ST-MTMTS|
||North Carolina Division of Forest Resources<sup>p</sup>|ST-NCNCS|
||Nebraska Department of Forestry<sup>q</sup>|ST-NENES|
||<br>New Mexico State Forestry<sup>n</sup>|ST-NMNMS|
||Oklahoma Division of Forestry<sup>a,d</sup>|ST-OKOKS|
||Oregon Department of Forestry|ST-ORORS|
||South Carolina Forestry Commission<sup>a,r</sup>|ST-SCSCS|
||South Dakota Wildland Fire Suppression Division<sup>_s_</sup>|ST-SDSDS|
||Tennessee Division of Forestry<sup>a,t</sup>|ST-TNTNS|
||Texas A&M Forest Service (TFS)<sup>u</sup>|ST-TXTXS|
||Utah Division of Forestry, Fire & State Lands<sup>v</sup>|ST-UTUTS|
||Virginia Department of Forestry (VDOF)<sup>w</sup>|ST-VAVAS|
||<br>Washington State Headquarters<sup>x</sup>|ST-WAWAS|
||Wisconsin Department of Natural Resources (WIDNR)<sup>y</sup>|ST-WIWIS|
||Wyoming State Forestry Division<sup>d</sup>|ST-WYWYS|
|Interagency|Alaska Interagency Coordination Center<sup>z</sup>|IA-AKACC|
||ICS-209 module of the SIT/209 application|IA-ICS209|



> a Data for 1997–2002; acquired from the Southern Wildfire Risk Assessment effort (SWRA). b Data for 1994–1996; acquired from MTBS. Data for 2003–2009; acquired directly from AFC. Data for 2010 acquired from the Eastern Forest Environmental Threat Assessment Center (EFETAC).<sup>c</sup> Data for 2009–2010; acquired from EFETAC.<sup>d</sup> Data for 1992–1996; acquired from Schmidt et al. (2002).<sup>e</sup> Data for 1992–1995; acquired from MTBS.<sup>f</sup> Data for 1992–2009; acquired from EFETAC.<sup>g</sup> Data for 1992–2002; acquired from SWRA.<sup>h</sup> Data for 1992–1997; acquired from EFETAC. Data for 1998–1999; acquired from SWRA. Records of fires located south of latitude 31.05 were missing from the 1998 SWRA data set and acquired from EFETAC.<sup>i</sup> Data for 1997–2001; acquired from SWRA.<sup>j</sup> Data for 1997–2002; acquired from SWRA. Data for 2009–2010; acquired from EFETAC.<sup>k</sup> Data for 1992–1993; acquired from Schmidt et al. (2002). Data for 1994–2002, 2004; acquired from MTBS.<sup>l</sup> Data for 1998–1999 (large fires only); acquired from MTBS.<sup>m</sup> Data for 1992–1997; acquired from Schmidt et al. (2002). Data for 1998–2002; acquired from MTBS.<sup>n</sup> Data for 1992–1999; acquired from MTBS.<sup>o</sup> Data for 2000–2007; acquired from SWRA.<sup>p</sup> Data for 1992–2004; acquired from SWRA. Data for 2010; acquired from EFETAC. 

> q Data for 1994–1999 (large fires only); acquired from MTBS. r Data for 1992–1996; acquired from MTBS. s Data for 1992–2002; acquired from MTBS.<sup>t</sup> Data for 2005; acquired from MTBS.<sup>u</sup> Data for 2009–2011; acquired directly from TFS. 

> v Data for 1992–2003; acquired, from MTBS, w Data for 1995–1996, 2003 acquired directly from VDOF. Data for 1997–2002; acquired from SWRA.<sup>x</sup> Data for 1992–2004; acquired from MTBS.<sup>y</sup> Data for 1992–1996; acquired from Schmidt et al. (2002). Data for 1997–2002; acquired directly from WIDNR.<sup>z</sup> Data for 1992–1995 and 2008–2010; acquired directly from the Alaska Interagency Coordination Center (AICC). 

Earth Syst. Sci. Data, 6, 1–27, 2014 

www.earth-syst-sci-data.net/6/1/2014/ 

K. C. Short: A spatial database of wildfires in the United States 

6 

## 2.2.1 Standardization 

Data were not formatted consistently across the various systems of record, and the following transformations, intended to comply as best as possible with NWCG data standards (http://www.nwcg.gov/pms/stds/standards/), were made when necessary. Of course, our ability to conform the data (see Table 2) to NWCG standards was constrained by the level of adherence to those standards within the source reporting systems throughout the period of record. 

After making any necessary geographic transformations, locations were formatted as latitude and negative longitude in decimal degrees, based on the North American Datum 1983. Precision to eight decimal places was retained, when available, for the sake of consistency with the source information. However, both the accuracy and precision of the location estimates are generally much lower than that implied by the stored coordinate information – which, for example, may have been calculated from a PLSS section centroid. Dates were formatted as mm/dd/yyyy, and time as hhmm (using the 24 h clock). Final fire size was formatted to indicate area in acres (1 acre = 0.405 hectare), which is the NWCG standard. The full precision of the estimate in the fire report was retained, which may or may not meet the NWCG standard of tenth-acre precision for all fires less than one acre. If the source database did not include a code or number that uniquely identified each record, we created one by either concatenating data elements or simply auto-numbering the records. We cross-walked the reporting agency and unit to the active NWCG Unit Identifier standard (see NWCG, 2012b), and we include the active Unit Identifier data set that we downloaded from https://www.nifc.blm.gov/unit_id/ Publish.html on 5 March 2012 and used for our cross-walk as a lookup table, _NWCG_UnitIdActive_20120305_ , in the final database. We removed any extraneous leading and trailing characters from the FireCode (https://www.firecode.gov/ index.cfm?action=login), which is a standardized four-digit federal accounting code assigned to fires and included in most federal fire reports that date back to circa 2003, providing a link to the agencies’ financial systems (USDI and USDA, 2013). Fire names were converted to uppercase, but otherwise unadjusted. Some fire names had clearly been truncated, for example, by the source system or by some data entry or transfer process, but we made no attempt to “correct” or harmonize them. The NWCG data standard for fire cause is currently pending, so we cross-walked the cause descriptions from the various systems of record to a set of codes and names (Table 3) based on those used by the USFS for statistical analysis (USFS, 2003). Values indicating landowner at the fire’s location (i.e., owner at origin) were cross-walked to a set of names and codes (Table 4) based on the NWCG standard landowner categories (http://www.nwcg.gov/pms/ stds/standards/land-owner-kind-category_v1-0.htm). While based on existing conventions, the full suite of cause and owner codes and values to which we cross-walked (Tables 3 

**Table 2.** Data elements extracted from wildfire reports and used to populate the FPA FOD. 

|Item|Description<br>i|
|---|---|
|Location<sup>∗</sup>|Point of origin of the fire, at least as<br>precise as PLSS Section.|
|Discovery Date<sup>∗</sup>|The date that the fire was discovered or<br>confirmed to exist.|
|Final Fire Size<sup>∗</sup><br>i|Area within the final perimeter of the<br>fire.|
|Record Identifier|Code or number that uniquely iden-<br>tifies the record within the source<br>database.|
|Reporting Agency|Identifier for the reporting agency.|
|Reporting Unit|Identifier for the reporting unit within<br>the agency.|
|Local Fire Report ID|Number or code that uniquely identi-<br>fies a fire report for a particular unit and<br>a particular calendar year.|
|Local Incident ID|Number or code that uniquely identi-<br>fies an incident for a particular local<br>fire-management organization within a<br>particular calendar year.|
|FireCode|Code used within the interagency wild-<br>land fire community to track and com-<br>pile cost information for emergency<br>fire suppression expenditures.|
|Fire Name|The name of the incident.|
|Discovery Time|Time of day that the fire was discov-<br>ered or confirmed to exist.|
|Fire Cause|The reported cause of the fire.|
|Contain Date|Date on which the fire was declared<br>contained.<br>i|
|Contain Time|Time of day that the fire was declared<br>contained.|
|Owner|Name of primary owner or entity re-<br>sponsible for managing the land at the<br>point of origin of the fire at the time of<br>the incident.|
|State|Name of the state in which the fire is<br>reported to have burned (or originated).|
|County|County in which the fire is reported to<br>have burned (or originated).|
|Fire Type|Type of fire, in terms of management<br>response.|
|Protection Type|Entity responsible for fire protection at<br>the point of origin.|



> ∗ Required. 

Earth Syst. Sci. Data, 6, 1–27, 2014 

www.earth-syst-sci-data.net/6/1/2014/ 

K. C. Short: A spatial database of wildfires in the United States 

7 

**Table 3.** Fire cause codes and definitions, adapted from USFS (2003). 

**Table 5.** Protection type codes and definitions (adapted from WFMI). 

|Code|Definition|Code<br>Definition|
|---|---|---|
|1|Lightning|1<br>Agency land protected by the agency|
|2<br>3|Equipment Use<br>Smoking<br>i|2<br>Agency land protected by another federal agency|
|4|Campfire|3<br>Agency land protected by a non-federal agency|
|5<br>6|Debris Burning<br>Railroad|4<br>Less than full suppression response on agency lands|
|7|Arson|5<br>Non-agency land not under agreement, memorandum|
|8|Children|<br>of understanding, or contract, where suppression ac-<br>i|
|9|Miscellaneous|<br>tion is taken by the agency to prevent fire spread to|
|10|Fireworks|i<br>agency land (i.e., threat to agency)|
|11|Power line||
|12|Structure|6<br>Other (non-agency) land protected by the agency un-|
|13|Missing/Undefined|der a cooperative agreement, memorandum of under-<br>standing, interagency mutual aid agreement, or con-|
|i|i|tract|
|es and i|definitions.|9<br>Naturally ignited wildland fire for which the appro-<br>i|
||i|priate fire-management response is based on objec-|
|Code|Definition|tives from an approved Fire Management Plan (FMP)<br>i    i   i|
|0|Foreign|(i.e., “fire used for resource benefit” or “wildland fire<br>i|
|1|BLM|use” when fire type=4)|
|2|BIA||
|3|NPS||
|4<br>5<br>6<br>7|FWS<br>USFS<br>Other Federal<br>State|only). Planned ignitions (i.e., prescribed fires), except tho<br>that escaped and ultimately required suppression respon<br>were intentionally excluded from the FPA FOD. Protecti<br>i     i|
|8|Private|type, specified only in the federal fire reports, was coded|
|9|Tribal|indicated in Table 5.|
|10|BOR<sup>∗</sup>||
|11|County|2.2.2<br>Error checking|
|12|Municipal/Local|<br>i|
|13|State or Private<br>i|Candidate fire records from each of the systems of reco|
|14|Missing/Undefined<br>i|were examined for spatial errors via overlays with ge|
|15|i<br>Undefined Federal|graphicinformationsystem(GIS)datasetsdelineating|



**Table 4.** Owner codes and definitions. 

only). Planned ignitions (i.e., prescribed fires), except those that escaped and ultimately required suppression response, were intentionally excluded from the FPA FOD. Protection type, specified only in the federal fire reports, was coded as indicated in Table 5. 

Candidate fire records from each of the systems of record were examined for spatial errors via overlays with geographic information system (GIS) data sets delineating US state boundaries (http://nationalatlas.gov/mld/statesp.html) and the boundaries of the fire planning units (FPUs) used by FPA. Some egregious spatial errors, including transposition of coordinates, were revealed through initial visual inspection of the mapped points, and, when the solution was obvious (as in the case of transposed latitude and longitude), the data were corrected. After all possible location information had been salvaged, fires that still mapped outside FPU boundaries or outside the state or territory expected from the fire report were flagged. All US states and territories are fully contained within the collective extent of the FPU boundaries, and fires outside FPU boundaries were excluded from the FPA FOD because (1) they were presumed to be located incorrectly (i.e., mapping offshore or in another country), and (2) all FPA fire analyses are FPU-based and therefore the records would be excluded de facto. Fires from the non-federal systems of record flagged because they mapped outside of the expected state were likewise presumed to be located incorrectly (or to be a large, multijurisdictional incident 

> ∗ USDI Bureau of Reclamation. 

and 4) include categories that we added in order to more fully accommodate the range of information in the original records. The US state (or territory) in which the fire occurred was not nominally designated in all fire reports. In those cases, we populated that field with the name of the state to which the reporting unit is tied, so that we obtained a nominal locality designation for all records to use for quality-control purposes (i.e., to compare with the point locations; see Sect. 2.2.2). State names were converted to standard two-letter alphabetic Federal Information Processing Standards (FIPS) codes (NIST, 1987). County (or equivalent) names were cross-walked to the three-digit FIPS county codes (NIST, 1990). Allowable fire types, in terms of management strategy, were coded as follows: 1 – actionable (i.e., suppression or appropriate management response taken), 2 – natural out, and 4 – fuels management (unplanned ignitions 

Earth Syst. Sci. Data, 6, 1–27, 2014 

www.earth-syst-sci-data.net/6/1/2014/ 

K. C. Short: A spatial database of wildfires in the United States 

8 

that would be redundantly reported in another system) and were therefore excluded from the FPA FOD. Federal fires (fires from a federal system of record) flagged for the same reason were not summarily excluded, however, because some agency units span or have fire protection responsibility or cooperative agreements in more than one state (e.g., NPS Appalachian National Scenic Trail, BLM Miles City Field Office) and some nominal state designations were based on the state designation in the unit name, which may not reflect the true state location of the fire. The flagged subset of suspect federal fires was therefore visually inspected and only records with obvious spatial errors (e.g., fires < 40 hectares mapping several states away from the expected domain) were excluded from further processing. In some cases, fires did not map within the state expected from the fire report, but did map within the domain of the interstate reporting unit (e.g., fires reported from Dinosaur National Monument mapping in Colorado and Utah, across which the unit spans) or were responded to under cooperative agreement or as a threat to the unit’s land. In other cases, fires mapped near enough to the proclaimed state or unit such that the mismatch was ostensibly due to imprecision of the reported location. We did find fires that were clearly mislocated because they mapped over water, but we retained them if they fell within the expected domain of state or FPU. 

Clearly erroneous dates (e.g., 1/1/1901, 12/6/4320) were excluded when we set our date range to 1992–2011. We checked for and omitted containment dates and times that preceded the fire discovery dates and times. 

To avoid confusion regarding the numbers 0 and 1, the FireCode system does not generate codes containing the characters “O” or “I” (USDI and USDA, 2013). However, we found codes in several hundred fire records with an O or I that had been changed from a 0 or 1 at some point in the reporting process. We changed the incorrect letters to the correct numbers in the FPA FOD so that we could fully leverage FIRE_CODE in our quality-control processes (see Sects. 2.2.4 and 2.2.5). 

## 2.2.3 Data compilation and derivation of additional elements 

All viable data extracted from each of the systems of record were compiled in a Microsoft<sup>®</sup> Access 2010 database. Records from each of the systems were appended into a single _Fires_ table with the schema shown in Table 6. As data were appended, the FOD_ID was assigned with an autonumbering function. Either the numeric FOD_ID or the alphanumeric FPA_ID can be used as the table’s primary key, as each uniquely identifies records in the database. It is the FPA_ID, however, that contains the necessary information to link back to the original data set. It consists of the unique identifier acquired (or created by concatenating elements) from the source system, with leading characters added to en- 

sure that it remained unique after being pooled with records from other systems. 

The fields SOURCE_SYSTEM and SOURCE_SYSTEM _TYPE, provide the system information summarized in Table 1 for each record. While fire year is included as an attribute separate from discovery date in most source systems, to ensure logical consistency it was populated in the _Fires_ table directly from DISCOVERY_DATE, as was day of year (DOY) for discovery and containment dates. FIRE_SIZE_CLASS was derived from FIRE_SIZE using the proposed NWCG standard class breaks and codes (http: //www.nwcg.gov/pms/stds/fire_size_class/values.pdf). 

## 2.2.4 Removing redundant records 

Once the data were consistently formatted and pooled together, we used a multistep process to identify and purge redundant fire records. In addition to the potential for multiple reports of the same fire to appear within and among the various systems of record (Bunton, 1999; Brown et al., 2002; Schmidt et al., 2002), there is also the potential for redundancy from the ways that fire complexes are handled in the reporting process. 

It is a fairly straightforward database exercise to identify fire records that are “duplicates” sensu Brown et al. (2002), because they have identical values for location, discovery date, total area burned, and cause. However, due to inconsistencies in data collection, formatting, and storage requirements, as well as information errors, the reporting systems are rife with records that are redundant but by no means identical, and there is no simple process to remove them before or after pooling the data. 

Examples of redundant fire records extracted from the reporting systems are provided in Table 7. The process of Brown et al. (2002) likely would have flagged cases 1 and 2 as intra-agency and interagency duplicates, respectively, but overlooked the others in Table 7, because their coordinates, discovery dates, and area burned values do not match _exactly_ . Fire cause is often unreported, especially in the nonfederal systems, or may differ among reports due to the information or reporting options available at the time of filing (see Donoghue, 1982b); thus, we did not enlist this field to assist in identifying redundant records. Instead, we primarily leveraged latitude, longitude, discovery date, fire size, and, when available, fire name and FireCode. We ran a series of database queries, explained as follows: we began with the most basic checks for duplicate records and progressed through steps that, as we cast a widening net, required increasing visual inspection to ensure that records flagged for exclusion from the final data set by the queries were indeed redundant with others to be retained. All records with flags that persisted to the end of the process (i.e., through step 10 below) were ultimately purged from the database. 

We readily identified sets of redundant records like cases 1 and 2 in Table 7 by querying the _Fires_ table for separate 

Earth Syst. Sci. Data, 6, 1–27, 2014 

www.earth-syst-sci-data.net/6/1/2014/ 

K. C. Short: A spatial database of wildfires in the United States 

9 

**Table 6.** FPA FOD _Fires_ table schema. 

|Field Name|Data Type|Definition|
|---|---|---|
|FOD_ID<sup>∗</sup>|Number|Global unique identifier.<br>i|
|FPA_ID<sup>∗</sup>|Text|Unique identifier that contains information necessary to track back to the<br>original record in the source data set. Can be used as primary key in lieu<br>of FOD_ID.|
|SOURCE_SYSTEM_TYPE<sup>∗</sup>|Text|Type of source database or system from which the record was drawn<br>(federal, non-federal, or interagency).<br>i|
|SOURCE_SYSTEM<sup>∗</sup>|Text|Name of or other identifier for source database or system from which the<br>record was drawn.<br>i      i|
|NWCG_REPORTING_AGENCY<sup>∗</sup>|Text|Active NWCG Unit Identifier for the agency preparing the fire report.<br>i      i|
|NWCG_REPORTING_UNIT_ID<sup>∗</sup>|Text|Active NWCG Unit Identifier for the unit preparing the fire report.<br>i|
|NWCG_REPORTING_UNIT_NAME<sup>∗</sup>|Text|Active NWCG Unit Name for the unit preparing the fire report.<br>i|
|SOURCE_REPORTING_UNIT|Text|i<br>Code for the agency unit preparing the fire report, based on code/name<br>in the source data set.<br>i|
|SOURCE_REPORTING_UNIT_NAME|Text|Name of reporting agency unit preparing the fire report, based on<br>code/name in the source data set.<br>i|
|LOCAL_FIRE_REPORT_ID|Text|Number or code that uniquely identifies an incident report for a particular<br>reporting unit and a particular calendar year.<br>i|
|LOCAL_INCIDENT_ID|Text|Number or code that uniquely identifies an incident for a particular local<br>fire-management organization within a particular calendar year.<br>i|
|FIRE_CODE|Text|i<br>Code used within the interagency wildland fire community to track and<br>compile cost information for emergency fire-suppression expenditures.<br>i|
|FIRE_NAME|Text|The name of the incident, from the fire report (primary) or ICS-209 report<br>(secondary).<br>i|
|ICS_209_INCIDENT_NUMBER<sup>∗</sup>|Text|Incident (event) identifier, from the ICS-209 report.|
|ICS_209_INCIDENT_NAME<sup>∗</sup>|Text|i<br>The name of the incident, from the ICS-209 report.<br>i|
|MTBS_ID<sup>∗</sup>|Text|Incident identifier, from the MTBS perimeter data set.|
|MTBS_FIRE_NAME<sup>∗</sup>|Text|i<br>Name of the incident, from the MTBS perimeter data set.<br>i|
|COMPLEX_NAME<sup>∗</sup>|Text|Name of the complex under which the fire was ultimately managed, when<br>discernible.<br>i    i|
|FIRE_YEAR<sup>∗</sup>|Number|Calendar year in which the fire was discovered or confirmed to exist.<br>i    i|
|DISCOVERY_DATE|Date/time|Date on which the fire was discovered or confirmed to exist.<br>i    i|
|DISCOVERY_DOY<sup>∗</sup><br>|Number<br>|Day of year on which the fire was discovered or confirmed to exist.<br>i    i|
|DISCOVERY_TIME|Text|Time of day that the fire was discovered or confirmed to exist.<br>i|
|STAT_CAUSE_CODE<sup>∗</sup>|Number|i    i<br>Code for the (statistical) cause of the fire.<br>i|
|STAT_CAUSE_DESCR<sup>∗</sup>|Text|i<br>Description of the (statistical) cause of the fire.<br>i|
|CONTAIN_DATE|Date/time|i<br>Date on which the fire was declared contained.<br>i|
|CONTAIN_DOY<sup>∗</sup>|Number|i<br>Day of year on which the fire was declared contained.<br>i|
|CONTAIN_TIME|Text|i<br>Time of day that the fire was declared contained.<br>i    i|
|FIRESIZE|Number|i<br>The estimate of acres within the final perimeter of the fire.|
|_<br>FIRE_SIZE_CLASS<sup>∗</sup>|Text|i    i<br>Code for fire size based on the number of acres within the final fire<br>perimeter.<br>i|
|LATITUDE<sup>∗</sup>|Number|Latitude (NAD83) for point location of the fire.<br>i|
|LONGITUDE<sup>∗</sup>|Number|Longitude (NAD83) for point location of the fire.|
|OWNER_CODE<sup>∗</sup>|Number|i<br>Code for primary owner or entity responsible for managing the land at<br>the point of origin of the fire at the time of the incident.|
|OWNER_DESCR<sup>∗</sup>|Text|i<br>Name of primary owner or entity responsible for managing the land at<br>the point of origin of the fire at the time of the incident.|
|STATE|Text|i<br>Two-letter alphabetic code for the state in which the fire burned (or orig-<br>inated), based on the fire report.|
|COUNTY|Text|i<br>County, or equivalent, in which the fire burned (or originated), based on<br>the fire report.|
|FIPS_CODE<sup>∗</sup>|Text|i<br>Three-digit code from the Federal Information Process Standards (FIPS)|
|||publication 6-4 for representation of counties and equivalent entities.|
|FIPS_NAME<sup>∗</sup>|Text|County name from the Federal Information Process Standards (FIPS)|
|||publication 6-4 for representation of counties and equivalent entities.|



> ∗ Element not necessarily in source system of record, but derived or obtained elsewhere for inclusion in FPA FOD. 

Earth Syst. Sci. Data, 6, 1–27, 2014 

www.earth-syst-sci-data.net/6/1/2014/ 

K. C. Short: A spatial database of wildfires in the United States 

10 

**Table 7.** Example cases of redundant records from the fire-reporting systems and steps in FPA FOD processing during which the records were flagged and all but one were removed from the final database. Fire size, shown here in hectares, is reported in the FPA FOD in acres, per the NWCG standard. 

|Processing<br>Step|Case|Source<br>System|Reporting<br>Agency|Reporting<br>Unit|Latitude|Longitude|Discovery<br>Date|Fire<br>Size|Fire<br>Name|Fire<br>Code|Cause<br>Code|
|---|---|---|---|---|---|---|---|---|---|---|---|
|1|1|FS-FIRESTAT<br>FS-FIRESTAT|FS<br>FS|MSMNF<br>MSMNF|32.36166667<br>32.36166667|−89.6<br>−89.6|3/9/2006<br>3/9/2006|3.8<br>3.8|ST. JOHN<br>ST. JOHN|B6VU<br>B6VU|5<br>5|
||2|DOI-WFMI<br>DOI-WFMI|BIA<br>BLM|AKAKA<br>AKASO|64.6403<br>64.6403|−150.4502<br>−150.4502|6/8/2002<br>6/8/2002|104 307<br>104 307|GESKAKMINA<br>GESKAKMINA|A283|1<br>1|
|2|3|FS-FIRESTAT<br>ST-MTMTS|FS<br>ST/C&L|MTBDF<br>MTCES|45.735<br>45.73798|−111.89666667<br>−111.89964|9/30/1996<br>9/30/1996|850<br>850|ANTELOPE CREEK<br>ANTELOPE CREEK||2<br>9|
|3|4|DOI-WFMI<br>DOI-WFMI|BIA<br>NPS|NCECA<br>TNGSP|35.5344<br>35.5344|−83.2764<br>−83.2764|4/27/2009<br>4/27/2009|934<br>934|STONEY RIDGE<br>STONY RIDGE|EVP1<br>EVP1|2<br>2|
||5|FA-NFIRS<br>FA-NFIRS|ST/C&L<br>ST/C&L|NDSFM<br>NDSFM|48.51<br>48.51|−100.06<br>−100.06|4/8/2007<br>4/8/2007|165<br>165|||9<br>9|
|4|6|DOI-WFMI<br>FWS-FMIS<br>ST-NASF|BLM<br>FWS<br>ST/C&L|AKASO<br>AKYFR<br>AKUYD|66.4833<br>66.48333333<br>66.483330004|−142.2<br>−142.2<br>−142.20000001|7/19/2005<br>7/19/2005<br>7/19/2005|95 864.1<br>95 864.1<br>95 864.1|SALMON FK<br>SALMON FORK|B02M<br>B02M|1<br>1<br>1|
||7|FWS-FMIS<br>ST-FLFLS|FWS<br>ST/C&L|FLFPR<br>FLFLS|26.285<br>26.29|−81.54083333<br>−81.54|5/19/1999<br>5/19/1999|0.04<br>0.04|DOF387|4494|9<br>1|
|5|8|DOI-WFMI<br>FWS-FMIS|BIA<br>FWS|CASCA<br>CATNR|32.7834<br>32.78333333|−116.8342<br>−116.83333333|9/26/1993<br>9/26/1993|9<br>4|SYCUAN<br>SYCUAN||5<br>9|
||9|FS-FIRESTAT<br>FWS-FMIS|FS<br>FWS|CACNF<br>CATNR|32.98555556<br>32.9988232|−116.7275<br>−116.7229304|10/25/2003<br>10/25/2003|113 423<br>114 643|CEDAR<br>CEDAR||2<br>2|
|6|10|FS-FIRESTAT<br>DOI-WFMI|FS<br>BLM|MTCNF<br>MTMCD|45.65083333<br>45.7292|−105.99666667<br>−105.995|9/5/2002<br>9/6/2002|4.7<br>4.7|LISCOM II<br>LISCOM II|H077|1<br>1|
|7|11|FS-FIRESTAT<br>ST-ORORS|FS<br>ST/C&L|ORRSF<br>ORORS|42.03888889<br>42.405|−123.91166667<br>−123.89233333|7/13/2002<br>7/15/2002|202 478<br>202 478|BISCUIT<br>ODF/BISCUIT|5833|1<br>1|
||12|FS-FIRESTAT<br>DOI-WFMI|FS<br>BLM|CASTF<br>CACND|37.90666667<br>37.8999|−120.14333333<br>−120.1344|8/14/1996<br>8/13/1996|8485<br>8942|ROGGE<br>ROGGE||1<br>1|
||13|FS-FIRESTAT<br>ST-NASF|FS<br>ST/C&L|FLFNF<br>FLFLS|30.35833333<br>30.404719991|−82.48333333<br>−82.500000014|3/3/2004<br>3/7/2004|13 851<br>14 037|IMPASABLE 1|A0J4|5<br>5|
||14|DOI-WFMI<br>DOI-WFMI|BLM<br>NPS|NMADO<br>NMEMP|34.9175<br>34.84778|−107.9839<br>−107.98287|7/20/2000<br>7/22/2000|840<br>810|WALL<br>WALL|L271|1<br>1|
||15|FS-FIRESTAT<br>ST-ORORS|FS<br>ST/C&L|ORWIF<br>ORORS|43.47416667<br>43.48361|−122.10194444<br>−122.32528|9/12/2009<br>9/12/2009|5897<br>5897|TUMBLEBUG<br>TUMBLEBUG ODF<br>BRANCH|EK2R|1<br>1|
|8|16|FS-FIRESTAT<br>DOI-WFMI|FS<br>BLM|NVHTF<br>NVWID|41.82805556<br>41.8279|−117.52611111<br>−117.5271|7/17/2000<br>7/18/2000|0.04<br>0.4|ALPHA<br>ALPHA|4978<br>X361|1<br>1|
|9|17|DOI-WFMI<br>FWS-FMIS<br>ST-NASF|NPS<br>FWS<br>ST/C&L|FLBCP<br>FLFPR<br>FLFLS|26.1161<br>26.11611111<br>26.11111001|−81.6836<br>−81.68361111<br>−81.676109981|4/17/2006<br>4/16/2006<br>4/18/2006|348<br>363<br>363|DOF 237<br>SPORTS PARK|CHS9<br>CHS9|9<br>9<br>9|
|10|18|DOI-WFMI<br>DOI-WFMI|BLM<br>FWS|AKASO<br>AKKNR|60.9661<br>60.57966|−149.7688<br>−149.46151|6/9/2004<br>6/9/2004|0.04<br>0.04|GULL ROCK1<br>169 GULL ROCK #1|A4NS<br>A4NS|4<br>4|
|11|19|FS-FIRESTAT|FS|AZCOF|34.47666667|−111.24722222|7/4/2009|2|PATRIOT|E02Q|1|
|||FS-FIRESTAT|FS|AZCOF|34.48583333|−111.23416667|7/4/2009|4|GENERAL|E02P|1|
|||FS-FIRESTAT|FS|AZCOF|34.48472222|−111.23388889|7/9/2009|1249|JULY 4TH COMPLEX|E1BL|1|



entries with identical values for all five of the following elements: latitude, longitude, discovery date, fire size, and name (step 1). Once the records were flagged accordingly, we selected only one from each set to retain. When we identified a set of federal and non-federal wildfire records that were redundant, we always retained a federal record, because the federal records tend to be more fully attributed (e.g., fire name and cause more consistently populated). When records from the federal reporting systems were redundant, we attempted to retain only the record from the agency unit that in- 

dicated it had protection responsibility for the fire. We based that determination on a code created by concatenating the fire type and protection type (Table 5) values in the _Fires_ table. A fire type-protection type (FTPT) code of 11, for example, indicates an actionable fire on agency land protected by that same agency. A decision matrix was generated with help from agency representatives and used to identify the FTPT code of the record to be retained in the FPA FOD from a given set including two or more redundant federal fire reports (Table 8). The matrix (Table 8) indicates that, for example, 

Earth Syst. Sci. Data, 6, 1–27, 2014 

www.earth-syst-sci-data.net/6/1/2014/ 

K. C. Short: A spatial database of wildfires in the United States 

11 

**Table 8.** Decision matrix indicating the fire type-protection type code of the record to be retained in the FPA FOD from a set including two or more redundant federal fire reports. The first digit of the code indicates fire type, where 1 = actionable (i.e., suppression or appropriate management response taken), 2 = natural out, and 4 = fuels management (unplanned ignitions only). The second digit of the code indicates protection type, as defined in Table 5. 

||11|12|13|14|15|16|19|21|22|23|25|26|49|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|11|11|11|11|11|11|11|11|11|11|11|11|11|11|
|12|11|12|12|12|12|16|19|12|12|12|12|12|49|
|13|11|12|13|14|13|16|19|21|13|13|13|13|49|
|14|11|12|14|14|14|16|14|14|14|14|14|14|14|
|15|11|12|13|14|15|16|19|21|22|23|15|26|49|
|16|11|16|16|16|16|16|19|16|16|16|16|16|49|
|19|11|19|19|14|19|19|19|19|19|19|19|19|19|
|21|11|12|13|14|21|16|19|21|21|21|21|21|49|
|22|11|12|13|14|22|16|19|21|22|22|22|26|49|
|23|11|12|13|14|23|16|19|21|22|23|23|26|49|
|25|11|12|13|14|15|16|19|21|22|23|25|26|49|
|26|11|12|13|14|26|16|19|21|26|26|26|26|49|
|49|11|49|49|14|49|49|19|49|49|49|49|49|49|



records with FTPT codes of 11 are to be retained over all others, because that code indicates that the entity with protection responsibility is the reporting entity. When redundant federal records indicated the same FTPT for the same fire (e.g., multiple federal units reporting the same fire and using FTPT = 13, because, although it burned multiple federal ownerships, it was the responsibility of a non-federal entity), or when sets included only non-federal records, we simply retained the first record of the fire as it occurred in the compiled data set, sorted in ascending order on FOD_ID. The FOD_ID was auto-assigned in ascending order as records were appended to the _Fires_ table, and federal records were appended in the following order: (1) FS-FIRESTAT, (2) DOIWFMI, (3) FWS-FMIS. The USFS records, for example, were assigned lower FOD_IDs than the DOI records and would therefore be retained in lieu of redundant DOI records with the same FTPT indicated. Records were “retained” by removing the flag that had been assigned in step 1. 

We then repeated the process (i.e., step 1), ignoring any records with a persisting flag, after rounding latitude and longitude to two decimal places to identify additional sets of redundant records illustrated by case 3 (Table 7, step 2). Fire name was not consistently populated in the systems of record, and steps 3 and 4 in our process entailed repeating steps 1 and 2, respectively, with fire name excluded from the queries to flag record sets like cases 4–7 in Table 7. Some fires flagged in steps 3 and 4, which appeared redundant because, according to the reports, they were the same size and discovered on the same date and at essentially the same location, were likely “false positives” due to imprecision in reported fire location. For example, fires located only as precisely as PLSS section generally have a reported latitude and longitude that merely represent the coordinates of the section centroid, and all fires occurring within that section are 

thereby apt to have matching location information. Therefore, PLSS section-located fires that were discovered on the same date and that reached the same final size are likely to be flagged as redundant in steps 3 and 4. We presumed, however, that fires greater than 40 hectares flagged in steps 3 and 4 were far more likely to be redundant (i.e., unlikely to occur in multiples on the same day within the same 2.6 km<sup>2</sup> section) than smaller fires, and to avoid purging potentially legitimate records from the database, we only flagged fires < 40 hectares if they matched in terms of size, date, and location, and were obtained from different agencies or systems of record (e.g., Table 7, case 7). All sets flagged in steps 3 and 4 were visually inspected for false positives before proceeding. The name and protection type of the FWS-reported fire in case 7, for example, indicated to us that the record was of a mutual aid fire that was indeed redundant with the record of an unnamed fire reported by the Florida Forest Service (FFS; formerly the Florida Division of Forestry, or DOF), and per our processing rules, only the federal record was retained. 

Step 5 was another variation on the previous steps, with coordinates for the persisting subset of data rounded to a single decimal place and records flagged if they matched in terms of name, date, and furthermore the generalized location (but not fire size). This step, again with visual confirmation, allowed us to identify sets of redundant records illustrated by cases 8 and 9 (Table 7), in which the records did not have the same reported location or fire size. 

In Step 6, we relaxed the date requirement to year and identified sets of redundant records shown in case 10 (Table 7), which matched in terms of name, year, general location (coordinates rounded to one decimal place), and fire size greater than 4 hectares. In step 7, we grouped records of fires greater than or equal to 405 hectares by (1) year and FPU and (2) year and state, and queried and visually inspected the groups to identify sets of redundant records based on matching or similar names, dates, and/or fire sizes (Table 7, cases 11–15). 

In step 8, we included fires of all sizes and based our search for redundant records only on name, year, and general location (coordinates rounded to one decimal place), which returned a list of several thousand fires, generally less than 405 hectares. This again required visual inspection to ensure that non-redundant fires were retained, as it is not uncommon for different fires, especially smaller ones, that occur in the same general location throughout the year to be repeatedly assigned the same generic place name (e.g., “Bombing Range”, “Roadside”). Case 16 (Table 7) provides an example of a set of records that was flagged in step 8 and deemed redundant after visual inspection, although they do not report the same date, size, or precise location. The protection type (5) and ownership (USFS) of the BLM-reported fire in case 16, for example, indicated to us that the BLM response was to a perceived threat and the fire report was indeed redundant with the record reported by the USFS, which 

Earth Syst. Sci. Data, 6, 1–27, 2014 

www.earth-syst-sci-data.net/6/1/2014/ 

K. C. Short: A spatial database of wildfires in the United States 

12 

indicated it had protection responsibility; per our processing rules, only the USFS record was retained. 

In the next step, step 9, which was the most laborious, we grouped all fires (regardless of size) by year and general location (coordinates rounded to one decimal place) and identified groups that included records from multiple sources (i.e., different systems of record). We then sorted the records within each group by date and fire size and visually inspected more than 150 000 records, scanning for redundant records that had passed through our screening up to that point. Case 17 (Table 7) provides an example of a set of records identified in this way that had not yet been flagged because they are reports of a < 405-hectare fire that agree only on month and location at one decimal place; but given their size (> 324 hectares) and the similar dates, we concluded that they reported the same incident. 

In step 10, we used FIRE_CODE to check for redundant reports from the federal systems of record. The formal FireCode system dates back only to 2003, and FireCode is not consistently populated for all fires from the federal systems since circa 2003, so it is of limited use in identifying potential duplicates. Moreover, FIRE_CODE alone is insufficient for this purpose, because fires in complexes (see Sect. 2.2.5) and groups of small (i.e., < 40 hectare, or “miscellaneous ABC”) fires are often assigned the same accounting code in a given fiscal year. We queried the subset of data that persisted through step 9 and generated a list of potentially redundant records based on FIRE_CODE, which was visually inspected to avoid discarding nonredundant fires grouped for accounting purposes, and those within complexes, which were dealt with separately as described in the following section. 

## 2.2.5 Fire complexes 

Operationally, a wildfire complex consists of two or more fires located in the same general vicinity and assigned to a single incident commander or unified command (NWCG, 2012a). In other words, a fire complex effectively comprises multiple fires managed as one large incident. It is not uncommon, however, to find fire reports for the complex as well as reports for all or some of its constituent, or subordinate, incidents in the systems of record. Because complexes can cover very large areas (e.g., the 2004 Taylor Highway complex in Alaska was reported at more than 500 000 hectares), estimates of total area burned from a database with records of complexes as well as their subordinate fires are apt to be highly inflated. When complexes were identified in the reporting systems, either via the incident name or by some database flag, we used that information to populate the COMPLEX_NAME field in the _Fires_ table (Table 6). While that approach identified some of the complexes in the data set, it did little to help us identify and label each of the subordinate fires within complexes when they, too, were reported. 

Because they generally are significant incidents, most federal and many non-federal fire complexes from circa 1999 

forward should have an ICS-209 report in the SIT/209 database. Individual large incidents within the complex should be named, with area burned for each reported, under _Remarks_ (NWCG, 2012a). In 2010 the SIT/209 database began including a separate incident complex table that names subordinate fires by complex. Unfortunately, the incident numbers used in the ICS-209 records (see NIFC, 2011) are not required to be included in the agency fire reports, which means that there is no straightforward way to join the records together. The LOCAL_INCIDENT_NUMBER in the _Fires_ table may contain a component of the alphanumeric ICS209 incident number (i.e., the numeric portion), but the LOCAL_INCIDENT_NUMBER rarely includes all of the information and is rarely formatted in the manner necessary to join the _Fires_ to the ICS-209 records. The formatting and information content of the incident number used in the ICS-209 reports (e.g., XX-XXX-######) is, however, generally consistent with that of the incident order number in the FireCode system, and FIRE_CODE is an attribute in our data set. We were able to acquire federal incident records for 2003–2011 from the FireCode system, and we used those to populate a temporary INCIDENT_NUMBER field in the _Fires_ table (Table 6). We intentionally excluded incident order numbers that were incomplete (e.g., XX-XXX-). 

According to recent interagency guidance, all federal wildfires within a complex are to retain their original FireCodes and incident numbers for accounting purposes (NWCG, 2011). However, when we linked our incident records into FireCode and extracted incident names, we found it not uncommon for all incidents within a complex to be assigned the same FireCode and given the complex name. Therefore, simply by linking into the FireCode system, we were able to further populate the COMPLEX_NAME field in the _Fires_ table. 

The FireCode system dates back only to 2003, and not all federal reports of wildfires from 2003–2011 were FireCodepopulated. For records that we could not populate INCIDENT_NUMBER via FireCode, we scoured the LOCAL_INCIDENT_NUMBER and FIRE_NAME fields for what appeared to be components of the ICS-209 incident numbers and, usually after some reformatting or concatenation with other elements the record (e.g., State and Unit ID), we were able to use those components to populate the INCIDENT_NUMBER field further. 

We then attempted to use the newly assigned INCIDENT_NUMBER in the _Fires_ table to link to the ICS209 records and extract additional information about complexes and subordinate incidents. We populated the field ICS_209_INCIDENT_NAME accordingly. Although we expected all federal fires > 405 hectares to have an ICS-209 report, we were unable to extract ICS-209 incident names for all records with a non-null INCIDENT_NUMBER in the _Fires_ table that met those criteria. Our inability to populate names in those cases was either due to an apparent absence of ICS-209 reports for the fires or to our inability 

Earth Syst. Sci. Data, 6, 1–27, 2014 

www.earth-syst-sci-data.net/6/1/2014/ 

K. C. Short: A spatial database of wildfires in the United States 

13 

to derive matching incident numbers from the _Fires_ table. We then scoured the ICS-209 incident records for the subset of all fires > 405 hectares from 1999 to 2011 in the _Fires_ table and populated the INCIDENT_NUMBER and ICS_209_INCIDENT_NAME fields for as many additional records as possible, partially through a series of database queries and partially through visual inspection of the data. When we located records of the same event that did not link originally due to differences in incident numbers, we overwrote the INCIDENT_NUMBER in the _Fires_ table with that from the ICS-209 system in order to ensure that INCIDENT_NUMBER could serve as a bridge to the ICS209 information, at least for most fires in the FPA FOD > 405 hectares. Due to inconsistencies in the ways that incident numbers are populated in various information systems, we determined that INCIDENT_NUMBER, as we had derived and vetted it, could only reliably be used to join to the ICS-209 records, and we therefore changed the name to ICS_209_INCIDENT_NUMBER and deleted entries that did not join, or joined incorrectly, to ICS-209 records. We then leveraged information in the ICS-209 data set to continue populating COMPLEX_NAME. 

The SIT/209 databases for 2010 and 2011 include an incident complex table that names subordinate fires by complex, and we capitalized on that information. For the years 1999–2009, however, there is no easy way to find and extract the names of individual incidents within complexes because they are listed, usually among copious other notes, in a memo field (i.e., a data type intended to store large amounts of text). It was therefore essentially a manual exercise to populate COMPLEX_NAME from the ICS-209 records (when this was possible). 

After leveraging the FireCode and ICS-209 systems, we turned to a third national data set to identify additional fires in complexes. The MTBS perimeter data set, which currently spans 1984–2011, was used to further populate COMPLEX_NAME for fires pre-dating the other two systems and for later fires that our process heretofore had missed. In addition to the FireCode and ICS-209 systems, the MTBS project consults several other sources (e.g., the Wildland Fire Decision Support System, InciWeb, field units) to determine the appropriate complex designations for the fires it has mapped, dating back to the mid-1980s (B. Quayle, personal communication, 2013). The MTBS data set identifies fires in complexes via the FIRE_NAME attribute, and in cases in which the fires within a complex remained distinct (unmerged), the complex name is listed, and the name of the subordinate (i.e. individually mapped) fire is indicated parenthetically (e.g., Canyon Complex [Bear]). It was possible to correctly derive the MTBS_ID (Table 6) for several thousand records by concatenating agency, unit, FireCode, and discovery date from the fire records. Fire names and sizes were used to verify that the correct ID had been derived. MTBS_IDs for another several thousand records were populated manually. MTBS_FIRE_NAME (Table 6) was populated once the 

records could be joined, and missing complex names were extracted from MTBS_FIRE_NAME. 

Once COMPLEX_NAME was populated as completely as possible, we used it to flag records like those illustrated by case 19 (step 11) in Table 7. In that case, the subordinate fires merged into one and continued to grow before reaching the final fire size. We therefore retained only one record of the three in that example, that of the JULY 4TH COMPLEX, in order to accurately reflect the total area burned. In cases in which the total area burned by the complex was adequately accounted for by the individual reports of subordinate fires, we preferentially retained the individual fire records in lieu of the single complex record in order to avoid losing information. 

## 2.3 Completeness evaluation 

We attempted to evaluate, at least nominally, the completeness of the resulting data set by comparing estimates of annual fire numbers and area burned, by state, from the FPA FOD with other published estimates. To avoid errors associated with mapping imprecision, the FPA FOD estimates were compiled by state based on the nominal STATE attribute, rather than the point location of the fire, although those assignments agree in 99.9 % of the records. 

Because the published estimates of annual wildfire numbers and area burned can differ considerably among sources due to inconsistencies and errors in measurement and reporting (e.g., see Urbanski et al., 2009), several sources of reference estimates were included in our assessment. We consider agreement in estimates of the same metrics from the FPA FOD and a given reference source as a proxy for “completeness” with respect to the latter. How accurately the reference estimates reflect actual wildfire activity is unknown; however, none are presumed to represent the true values, and therefore completeness, in fact, cannot be known by way of this assessment, or, indeed, at all. In other words, agreement of estimates from the different sources implies nothing about their accuracy. 

## 2.3.1 Sources of reference estimates 

Interagency estimates by state of annual fire numbers and area burned for 1992–2011 were obtained from the USFS wildfire activity statistics published until 1997 and the NICC annual wildfire statistics available for 1999–2011. (Statelevel wildfire activity statistics for 1998 are not available from the NICC, C. Leonard, personal communication, 2011). The USFS wildfire activity statistics include reported estimates of the number of wildfires and area burned on lands qualifying for federal, state, and local wildfire protection, as required by the Cooperative Forestry Assistance Act of 1978. The data were provided by the USFS, the USDI agencies (bureaus), and the state forester or equivalent state official (e.g., state fire marshal). The NICC estimates are based on 

Earth Syst. Sci. Data, 6, 1–27, 2014 

www.earth-syst-sci-data.net/6/1/2014/ 

K. C. Short: A spatial database of wildfires in the United States 

14 

year-end summaries of wildfires and area burned according to the SIT reports. During the active fire season (i.e., preparedness level > 1), SIT reports are required on a daily basis from federal units with fire protection responsibility as well as any non-federal (i.e., state, county, or local) units with protection responsibility for lands under federal ownership (per cooperative agreement). The use of the SIT reporting system is optional for non-federal units with wildfire protection responsibility for non-federal lands. Voluntary SIT reporting by non-federal units may result in considerable underestimates of total wildfire numbers and area burned appearing in the NICC annual reports. 

If the NICC estimates are low due to limited non-federal reporting through the SIT application in years and for states from which we were able to acquire viable data from the nonfederal systems of record, we would expect lack of agreement in those cases (i.e., FPA FOD estimates exceeding those from NICC), particularly for states with the majority of their wildland area under non-federal fire protection. To identify states and years for which the NICC numbers appear low due to underreporting of non-federal fires, we relied on several additional sources of published estimates of wildfire numbers and area burned, as available. 

Although the USFS ceased publication of annual wildfire reports in 1997, the agency is still required to collect wildfire activity statistics from state and local units that it supports under its State and Private Forestry Cooperative Fire Assistance Program (USFS, 2010). Each participating state’s fire marshal or other authority uses the Annual Wildfire Summary Report (AWSR), form FS-3100-8, to provide the necessary summary information, including the numbers and area burned by wildfires responded to by state and local firefighting agencies (USFS, 2010). We extracted wildfire counts and area burned estimates from all AWSRs available from the FAMWEB Data Warehouse, by state, for the period 1992– 2011. 

Finally, we extracted any all-lands estimates of wildfires and area burned that were published or otherwise made publicly available by the states themselves or other interagency groups. We were able to find such estimates, purported to be for all ownerships and spanning the entire period of interest (1992–2011), from the Alaska Interagency Coordination Center (AICC), the California Department of Forestry and Fire Protection (CDF), the Southwest Geographic Area Coordination Center (SWCC, covering Arizona and New Mexico), and the South Carolina Forestry Commission (SCFC). Wildfire activity statistics for state and local ownerships were obtained from the Texas A&M Forest Service (TFS) for 2005–2011. 

In sum, we used the USFS/NICC estimates as our default for comparison to the FPA FOD data summarized by state and year. When any of the USFS/NICC estimates appeared to underestimate wildfire numbers or area burned within a state-year based on publicly available estimates from another 

authoritative source, we used the latter for the assessment described in the following section. 

## 2.3.2 Methods of assessment 

We compared estimates of wildfire numbers and area burned from the FPA FOD to those from the reference sources; this amounted to a comparison of measurement methods, for which many statistical analyses are inappropriate (Bland and Altman, 1986). For example, given the generally high interannual variability in fire numbers and area burned, annual wildfire activity metrics from different sources can be highly correlated but have very poor agreement, making correlations irrelevant. Because we were interested in the similarity of estimates (in relative rather than absolute terms), we calculated, for each state and year, the ratio of (1) wildfire numbers and (2) wildfire area burned estimated from the FPA FOD and the same metrics from the reference source. We did not expect perfect agreement in any case, due to measurement inconsistencies and errors. However, if the FPA FOD and the national interagency statistics were based on similar levels of federal and non-federal reporting, and the FPA FOD was nominally complete in that regard, then the estimates of fires and area burned from the FPA FOD should agree with the national interagency estimates reasonably well (e.g., ±20 %) and the ratio of FPA FOD numbers to the reference (REF) estimates should be close to 1. Averaged across years, the FOD/REF ratio essentially provides an index of agreement for a given period. However, in cases in which the FPA FOD includes records from non-federal sources unaccounted for in the reference estimates (e.g., data from local fire departments) for some years and not others, the average of the ratios can be very near to 1 despite poor agreement in estimates for individual years. We therefore used the ratio simply to score states on a scale of 0–10, by limiting the maximum value of the ratio to 1 and then averaging across years and multiplying the resulting value by 10. We used the scaling factor to make the result appear less like the average of the unadjusted ratios in order to avoid confusion. Low scores indicate states for which the FPA FOD appears relatively incomplete for the period of assessment based on national published estimates of wildfire numbers or area burned, while high scores indicate states for which the FPA FOD yields estimates of those metrics that tend to meet or exceed those from the reference source(s). We used the entire 20 yr span, 1992–2011, as one period of assessment and the recent 10 yr span, 2002–2011, as a second period, because we expected differences largely due to the increased use of non-federal reporting systems in the latter period. 

## **3 Results** 

A total of nearly 2.6 million US wildland fire records were obtained from the (non-independent and generally overlapping) sources listed in Table 1 and considered for inclusion 

Earth Syst. Sci. Data, 6, 1–27, 2014 

www.earth-syst-sci-data.net/6/1/2014/ 

K. C. Short: A spatial database of wildfires in the United States 

15 



**Figure 1.** Locations of wildfire records from the conterminous US included in the FPA FOD by year. 

in the FPA FOD. The bulk of the data that we acquired were processed in 2010, at which point we limited our focus to records only from the years 1992–2008. At that time, we identified approximately 1.2 million wildfire records from that 17 yr time span that met our geospatial and information requirements, and which we compiled into a single database. Via our process, we identified approximately 120 000, or 10 %, of those records as redundant with others in the data set and subsequently purged them from the final database, thereby eliminating 22 million hectares from the original 58million hectare data set, or 38 % of the total. In other words, the redundancy we identified in the unprocessed, compiled data set inflated wildfire numbers by a factor of 1.1 and inflated the estimate of wildfire area burned by a factor of 1.6. During the winter months of 2011–2012, we processed and added data for 2009–2011 as well as newly available records from the non-federal systems that were known to be missing from the 1992–2008 data set. The resulting FPA FOD, spanning 1992–2011, includes nearly 1.6 million wildfire records, which collectively account for approximately 46 million hectares burned during the 20 yr period. The data set includes wildfire records from each of the 50 US states and from the District of Columbia and Puerto Rico. 

The years and states for which at least a subset of data from one or more of the non-federal reporting systems is included in the final database are identified by the boldface values in Tables 9 and 10. Twenty-one states, including Alaska, afforded at least some viable and non-redundant non-federal data for the entire 20 yr span. Considering just the 10 yr span, 2002–2011, the number of states affording some viable and 

non-redundant non-federal data for that entire period rises to 36. 

The maps in Fig. 1 show the locations of all of the wildfire records by year from the conterminous US included in the FPA FOD. A map of the locations of all FPA FOD records in the conterminous US is juxtaposed with a map of land mapped as burnable wildland surface-fuel types (per Scott and Burgan, 2005) in the LANDFIRE Refresh 2008 (LF_1.1.0b; see Ryan and Opperman, 2013) data set in Fig. 2. Figure 3 shows the locations of wildfires in the conterminous US, 1992–2011, reported as greater than or equal to 405 hectares in the (A) FPA FOD and (B) MTBS perimeter data set, for comparison. 

## Agreement with national estimates 

Published USFS wildfire activity statistics for 1992–1997 approximate the number of US wildfires and total area burned during that six-year period as 626 000 and 9 million hectares, respectively, averaging to about 104 000 fires and 1.5 million hectares per year. Approximations for 1998–2011 from NICC Predictive Services are 1.1 million wildfires and 38 million hectares total, averaging to about 80 000 fires and 2.7 million hectares per year for that 14 yr period. Annual estimates of US wildfire area burned from the FPA FOD align well with the national estimates for the entire 20 yr period (Fig. 4b), but annual fire numbers from the FPA FOD are generally consistent only with the numbers reported for 1998–2011 by NICC (Fig. 4a). Annual fire numbers estimated from the FPA FOD range from 65 to 70 % of the USFS estimates for the period 1992–1997 (Fig. 4a). 

Earth Syst. Sci. Data, 6, 1–27, 2014 

www.earth-syst-sci-data.net/6/1/2014/ 

K. C. Short: A spatial database of wildfires in the United States 

16 



**Figure 2.** Locations of **(A)** all wildfire records in the conterminous US included in the FPA FOD, 1992–2011, and **(B)** land mapped as burnable wildland surface-fuel types in the 30 m resolution LANDFIRE Refresh 2008 data set (LF_1.1.0b; see Ryan and Opperman, 2013). Points depicting the locations of fires are not to scale. Areas with few or no fires represented in the data set may have afforded little viable data for inclusion in the FPA FOD, or, alternatively, may be areas with little or no burnable land cover. Non-burnable fuel types are those with “insufficient wildland fuel to carry wildland fire under any condition”, and include urban or suburban development, agricultural land maintained in a non-burnable condition, snow/ice, open water, and bare ground (Scott and Burgan, 2005). 

Agreement with published estimates of wildfire numbers and area burned is generally evident for states and years from which non-federal data were available and incorporated into the FPA FOD (Tables 9 and 10). Agreement scores for the 21 states from which we acquired viable non-federal data for all 20 yr ranged from 8.1 to 9.9 for wildfire numbers (Table 9) and 7.3–9.9 for wildfire area burned (Table 10). Our index of agreement is generally high for states and regions with a large proportion of land area administered by one or more of the five primary federal agencies with wildlandfire-management programs (Figs. 5 and 6), as they are least affected by missing non-federal records. Twelve of the 17 states in the western region scored 8.2 or higher for the 20 yr period for wildfire numbers and area burned, while the region’s west-central states and Hawaii, which have less land under federal administration than Alaska and the far-western states in the conterminous US, scored the lowest of the western region (Tables 9 and 10, Fig. 5a and c). Nine of the ten US states with the lowest 20-year scores, for either metric, are 



**Figure 3.** Locations of wildfires in the conterminous US, 1992– 2011, reported as greater than or equal to 405 hectares **(A)** in the FPA FOD and **(B)** in the MTBS perimeter data set. The points in panel A are not displayed to scale, but rather at a size that makes it possible to compare the general spatial pattern of large-fire occurrence as indicated by the FPA FOD to the large-fire perimeters mapped by MTBS for the same period. 

in the northeastern region (Tables 9 and 10, Fig. 5a and c). While they are included in Tables 9 and 10, scores for the states of Iowa, Illinois, Kansas, New York, and Texas are not indicated in Fig. 5, because they are misleading due to reporting biases evident in the FPA FOD and the reference sources (which we describe in the next section and illustrate in Figs. 7–10). 

## **4 Discussion** 

Nearly 100 years ago, Show and Kotok (1923) argued that “successful [wildfire] protection depends on a critical study of past performances. For this purpose, the importance of accurate and complete records of fires cannot be overemphasized.” These sentiments have been echoed repeatedly since, including in 1959, by A. A. Brown, who contended that “the discovery of new facts ferreted out of reliable records of our day-to-day experience in [wild]fire-control operations can point the way to improvements in management, training, methods, and techniques.” More recently, Brown et al. (2002) pointedly characterized wildfire-occurrence data as “the most important data that a fire management [sic] agency can utilize.” A wealth of information is collected in federal, state, and local fire reports, but even the most 

Earth Syst. Sci. Data, 6, 1–27, 2014 

www.earth-syst-sci-data.net/6/1/2014/ 

K. C. Short: A spatial database of wildfires in the United States 

17 



**Figure 4.** Comparison of wildfire **(A)** numbers and **(B)** area burned (hectares) in the US, 1992–2011, from published national estimates (USFS/NICC) and from the FPA FOD. Estimates from the USFS wildfire activity statistics reports were used for 1992–1997 reference numbers, while those from NICC Predictive Services annual reports were used for 1998–2011. 

rudimentary interagency analyses of wildfire numbers and area burned from the systems of record have been unfortunately stymied to some degree by their disunity. While necessarily incomplete in some aspects, the database presented here is intended to facilitate fairly high-resolution geospatial analysis of US fire activity over the past two decades, based on available information from the authoritative systems of record. 

The inherent incompleteness of this data set is largely a function of the lack of viable non-federal wildfire records from certain states and years. These records are lacking for one of two reasons: (1) fire reports had not been entered into the systems of record that we accessed, or (2) the archived fire reports lacked values for one or more of the data elements required for inclusion in the FPA FOD (i.e., fire location at least as precise as PLSS section, discovery date, and final fire size). The location requirement was the primary cause for omission of non-federal records from the FPA FOD. Despite increased use of the national non-federal reporting systems 

(see Thomas and Butry, 2012), precise fire location information is not consistently required by those systems and thus not included in many of the available wildfire records. For example, about half of the wildfire records initially acquired in 2010 from the NASF database and 92 % of those from the NFIRS wildland fire module lacked location information that met our criteria. When we acquired data again in 2012 from the NASF database via the FAMWEB data warehouse, the number of records without viable location information had dropped to 24 %. Of the wildfire records acquired most recently (in 2012) from NFIRS (for the year 2010), 82 % still lacked location information that met our criteria. According to Thomas and Butry (2012), data entry into the wildland fire module of NFIRS, which is where precise location and size information can be entered for wildfires, is “not required by fire departments, so it is rarely completed.” 

The impact of missing non-federal data on the utility of the FPA FOD for analyses of wildfire activity will depend on the domain of interest and the federal, state, and local wildland firefighting roles and responsibilities in the states within that domain. Federal agencies that manage and administer large tracts of public or tribal-trust lands are also authorized to, and generally do, provide wildfire protection for those lands, either directly or indirectly through contracts and agreements with other organizations (Artley, 2009). Federal reporting of those activities has been generally consistent and complete since circa 1992 (S. Larrabee, personal communication, 2010), and those records should be relatively complete in the FPA FOD. The degree to which state entities have legislatively accepted wildfire protection responsibility for state and private lands (i.e., non-federal and nontribal lands outside incorporated municipalities) varies by state (Artley, 2009). Only fires to which the state responds, whether for initial attack or large fire support, are expected to be reported in the state systems of record. The FFS, for example, has assumed direct wildland firefighting responsibility for all state and private lands in the state of Florida, while the Washington State Department of Natural Resources (WDNR) and Oklahoma Forestry Services (OFS) are examples of state entities that provide direct protection on non-federal lands only in designated areas (Artley, 2009). Unlike records from the FFS, which should map statewide, those from WDNR and OFS are expected to cluster in certain regions (i.e., forested lands in Washington and eastern portions of Oklahoma, respectively) and indeed do (see Fig. 1). 

In certain states, including Colorado, Kansas, and Texas, the local fire departments are the official primary and initial responders to non-federal wildfires, with state (and federal) agencies authorized to provide support to the local authorities when local response capabilities are surpassed (e.g., by large fires) (Artley, 2009; TFS, 2012). The degree of protection responsibility assumed by the state firefighting entities is not necessarily consistent over time, however, and some of these role changes are evident in the availability of wildfire records for certain states. In Texas, for example, the area 

Earth Syst. Sci. Data, 6, 1–27, 2014 

www.earth-syst-sci-data.net/6/1/2014/ 

K. C. Short: A spatial database of wildfires in the United States 

18 





**Figure 5.** Maps showing agreement scores for the conterminous US for **(A)** wildfire numbers, 1992–2011, **(B)** wildfire numbers, 2002–2011, **(C)** wildfire area burned, 1992–2011, and **(D)** wildfire area burned 2002–2011 (see Tables 9 and 10). Low scores indicate states for which the FPA FOD appears relatively incomplete for the period of assessment based on national published estimates of wildfire numbers **(A, B)** or area burned **(C, D)** , while high scores indicate states for which the FPA FOD yields estimates of those metrics that tend to meet or exceed those from the reference source(s). Scores for IA, IL, KS, NY, and TX are omitted because they are misleading due to reporting biases evident in the FPA FOD and the reference sources (see Figs. 7–10). 



**Figure 6.** Locations of federal and Indian lands in the conterminous US administered by the five primary federal agencies with wildland fire-management programs (i.e., BIA, BLM, FWS, NPS, and USFS). 

for which the Texas A&M Forest Service (TFS) provides cooperative fire protection began expanding in the mid-1990s from state and private wildlands in eastern Texas (i.e., east of Interstate 45) to the entire state, per state law passed in 1993 (TFS, 2009). The TFS estimates that it still only responds to about 15 % of the wildfires that occur each year in the state, 

but because many of the incidents that it is called upon to assist with are very large, TFS records typically account for 70 % of the total area burned, including, since circa 1998, incidents in central and western Texas (TFS, 2012). For Texas and other states in which local entities bear responsibility for initial attack on non-federal wildlands, no data set purporting to represent all lands can be deemed complete, particularly with regard to wildfire numbers, without viable local wildfire records. In general, non-federal fire reporting has been on the rise over the past several decades, and users of national data sets like the FPA FOD must beware of local reporting biases in addition to those of state entities in order to avoid drawing spurious conclusions when analyzing the data. Apparent trends in the numbers and area burned by wildfires, for example, may be the result of multiple factors, including changes in climate, fuels, demographics (e.g., population density), fire-management policies (Johnston and Klick, 2012), and – as we underscore here – levels of reporting. 

While the US fire departments’ system of record, NFIRS, dates back to the mid 1970s, its use has always been voluntary and therefore subject to the vagaries of voluntary 

Earth Syst. Sci. Data, 6, 1–27, 2014 

www.earth-syst-sci-data.net/6/1/2014/ 

K. C. Short: A spatial database of wildfires in the United States 

19 



**Figure 7.** Number of wildfires in New York, 1992–2011, estimated from reference sources, per Fig. 1, and from the FPA FOD. Estimates from Annual Wildfire Summary Reports (AWSR), which should cover state and private lands only, are included as well. Viable non-federal data were available and included in the FOD for all years, and FPA FOD estimates agree well with AWSR numbers throughout the entire period. Estimates from all sources agree well for the period 1992–1999, but are based only on federal records and records from fires responded to by the state’s forest ranger force. Beginning in 2000, numbers from the AWSR and the FPA FOD increase with increased reporting from local fire departments, which remain unaccounted for by the NICC estimates throughout the entire period. 

reporting. It is estimated that, by the late 1980s, only one third of all fires – of any type – responded to by US fire departments were accounted for in the system (Hall and Harwood, 1989). That percentage is estimated to have risen to 65 % by 2010 (Thomas and Butry, 2012). Of all fires reported in NFIRS, only a fraction are indicated as involving wildland fuels. Using a national estimates approach adapted from Hall and Harwood (1989), Thomas and Butry (2012) determined that an average of nearly 117 000 fires in wildland fuels were responded to annually by US fire departments from 2002 to 2006 and that the data entered into NFIRS represented just a subset of those, growing from 11 % in 2002 to 27 % in 2006. Thus, even if all of the wildfires in the NFIRS database could be incorporated in the FPA FOD, the resulting database would provide an incomplete, and inconsistent, account of US wildfire activity from the standpoint of local responses. But, as noted above, of the growing subset of wildfires responded to by local departments and reported in NFIRS, only a small fraction met our geospatial and information standards. However, we appear to have acquired and incorporated viable records of some “local fires” for certain states and years from outside NFIRS, thereby augmenting that subset in the final FPA FOD. 

Although Thomas and Butry (2012) contend that national wildfire activity statistics based on federal and state incident reporting “do not account for wildland fires originat- 



**Figure 8.** Number of wildfires in Texas, 1992–2011, estimated from reference sources, per Fig. 1, and from the FPA FOD. Estimates from the Texas A&M Forest Service (TFS), which are based on state and local reports only, are also included for 2005–2011. Viable non-federal data were available and included in the FPA FOD for all years. The FPA FOD and USFS/NICC estimates agree relatively well for the period 1992–2004, but those numbers are based only on federal records and records of fires responded to by the TFS, which is the state fire service. FPA FOD numbers increase during the period 2005–2011 due to the availability of viable data from local fire departments, acquired for 2005–2008 from the NASF database and for 2009–2011 from the TFS directly. The local numbers appear in the NICC estimates for 2008–2010 only, as county data. The agreement in estimates from the FPA FOD and USFS/NICC for 1992–2004 is clearly misleading if used as a proxy for completeness of the data set, because wildfires responded to solely by the local fire service are abundant in this state and are unaccounted for in those reference estimates. 

ing within municipal jurisdictions (i.e., towns and communities)”, mutual aid fires and other local incidents with federal or state responders will, in fact, likely be reported in the respective agency systems of record. In other cases, however, there are clear signals in the data that indicate that local incidents, whether or not responded to by the state fire service, have been included in the state system(s) of record, and, subsequently, the FPA FOD. The number of wildfire records we acquired from the state and federal systems for New York and Texas, for example, begins to inflate at points in time, evidently corresponding to increased reporting of local incidents in the state systems (Figs. 7 and 8). According to the New York State Department of Environmental Conservation (NYDEC), its state forest ranger division reported 279 wildfires, on average, for the period 1988–2012 (NYDEC, 2013). The NYDEC distinguishes those fires from the annual average of 5500 “wildfires, brush fires, grass fires, or other outdoor fires” that the New York State (NYS) Office of Fire Prevention and Control reports that NYS fire departments responded to from 2002 to 2011 (NYDEC, 2013). The FPA FOD numbers are consistent with the NYDEC (i.e., state) 

Earth Syst. Sci. Data, 6, 1–27, 2014 

www.earth-syst-sci-data.net/6/1/2014/ 

K. C. Short: A spatial database of wildfires in the United States 

20 



**Figure 9.** Number of wildfires in **(A)** Iowa and **(B)** Illinois, 1992– 2011, estimated from reference sources and from the FPA FOD. Estimates from the USFS wildfire activity statistics reports were used for 1992–1997 reference numbers, which indicate that an average of about 1300 and 600 wildfires occurred annually in Iowa and Illinois, respectively, during that period. Estimates from NICC Predictive Services were used for 1999–2011 and estimates from Annual Wildfire Summary Reports (AWSR), which should cover state and private lands only, are included, starting in 2005 for Iowa and in 2008 for Illinois. For both states, the FPA FOD estimates for 1992–2000 are based on reports from the federal systems of record only. While we were able to incorporate some viable data from the non-federal systems for both states beginning in 2001, and the FPA FOD and NICC estimates align fairly well in certain years during the period 1999–2004 for Iowa and 1999–2006 for Illinois; those estimates are based largely, if not solely, on federal reporting. Furthermore, the number of records in the FPA FOD and the wildfire numbers reported by NICC are less than 70 % of the AWSR numbers for Iowa 2005–2007. The FPA FOD estimates agree best with the Illinois AWSR numbers 2008–2011. However, we presume that those too are underestimates of wildfire activity on all ownerships, which may be best approximated by the earlier USFS counts. An upward trend toward those earlier numbers is evident for Illinois in 2008–2010, ostensibly due to increased non-federal reporting. 

estimates prior to 2000, after which the FPA FOD wildfire count climbs to a maximum of about 7700 in 2005, with no addition of data from the NFIRS system, suggesting that the 



**Figure 10.** Number of wildfires in Kansas, 1992–2011, estimated from reference sources, per Fig. 1, and from the FPA FOD. The USFS/NICC numbers prior to 2004 indicate that an average of about 4300 wildfires occurred annually in the state during that period. While we were able to incorporate some viable data for Kansas from the non-federal systems for all but 1992 and 2009–2011 (Table 9), the resulting set of FPA FOD records for the state is clearly far from complete. Agreement with the reference estimates improves 2004– 2011 not due to acquisition of substantially more viable non-federal data, but instead due to decreased reporting of non-federal fire activity to NICC. 

NASF database, and thereby the FPA FOD, began including local (i.e., fire department) reports in 2000 (Fig. 7). In the case of Texas, fire departments began using a reporting system maintained by the TFS in 2005 (TFS, 2012), and the Texas wildfire records for 2005–2008 that we acquired from the NASF database and those for 2009–2011 that we acquired directly from the TFS evidently included at least some, if not most, of those local reports, as the annual FPA FOD numbers jump from an average of about 1500 to 13 000 starting in 2005 (Fig. 8). The pre-2005 numbers average about 12 % of the 2005–2011 numbers, which is generally consistent with the TFS (state fire service) estimate that it responds to only about 15 % of all wildfires in the state each year (TFS, 2012). The inclusion of local records for 2005– 2011 in the FPA FOD is likewise evident from changes in the spatial extent of the data for Texas: starting in 2005, coverage markedly increases in the central and western portions of the state (Fig. 1), which have effectively remained outside of the purview of TFS fire protection, except in cases of cooperative assistance for large incidents. Local numbers appear to be included in the NICC estimates for Texas only from 2008 to 2010, as county data. In the cases of both New York and Texas, the FPA FOD estimates of wildfire numbers and area burned agree fairly well with reference estimates across all years, as apparent from their relatively high scores in Tables 9 and 10. However, the overall agreement is misleading if used as a proxy for completeness of the data set, due to 

Earth Syst. Sci. Data, 6, 1–27, 2014 

www.earth-syst-sci-data.net/6/1/2014/ 

K. C. Short: A spatial database of wildfires in the United States 

21 

the fluctuations in local reporting evident during the period of record (Figs. 7 and 8). 

There are other cases in which agreement between metrics estimated from the FPA FOD and reference sources clearly does not translate to completeness, because, again, the reference estimates themselves are evidently incomplete. Most notable are the cases of Iowa, Illinois, and Kansas, which, along with New York and Texas, were omitted from the maps in Fig. 5 because their scores were misleading. As with New York and Texas, there are periods during which the FPA FOD estimates of wildfire numbers for Iowa, Illinois, and Kansas align well with reference estimates, but those estimates are based largely, if not solely, on federal reporting and therefore biased low (Figs. 9 and 10). That is indeed the case for Iowa during the period 1999–2004 and for Illinois during 1999–2007 (Fig. 9). For both states, the FPA FOD estimates likewise agree relatively well with the generally higher AWSR numbers for 2008–2011, which are non-federal estimates only. We presume that those too are underestimates of wildfire activity on all ownerships, which may be best approximated by the earlier USFS counts (Fig. 9). An upward trend toward those earlier USFS numbers is evident for Illinois in 2008–2010, ostensibly due to increased nonfederal reporting during that period (Fig. 9). For Kansas, we acquired very few non-federal records that met our criteria for inclusion in the FOD, and therefore all FPA FOD estimates for that state are biased low despite fairly good agreement with NICC numbers for the period 2004–2011, which too are based on scant non-federal reporting (Fig. 10). 

Ignoring the five states just noted, which are difficult to score due to reporting biases, we have tried to identify states and years in which there is relatively good FPA FOD agreement with numbers and area burned estimates published elsewhere (Fig. 5). Keeping in mind the inherent incompleteness of local records for most, if not all, states and years, the FPA FOD should be best suited for all-lands analyses of wildfire activity in areas within states or interstate regions (e.g., ecoregions) with relatively high scores (e.g., > 8) for wildfire numbers and/or area burned. Those high-scoring states include most of those in the Great Lakes, southeastern, and western regions (including Alaska), as well as a handful of others. Moreover, the FPA FOD should be complete or near complete in terms of data compiled from the federal systems of record, which alone lends itself to analyses that were previously limited to data from a single agency (e.g., USFS) due to difficulty compiling records from the disparate federal systems (e.g., Stephens, 2005). Regardless of its apparent appropriateness for a given analysis, users must carefully critique the FPA FOD to recognize and understand any potential limitations of data obfuscated by a relatively high score. Likewise, users may find value in at least a subset of data from low-scoring states, but the onus is on the users to critique them fully. 

Examples of questions to ask before proceeding with any analysis of wildfire activity using the FPA FOD include the following: 

1. _Are wildfire records from multiple federal agencies and_ / _or non-federal sources required to answer the question(s) at hand?_ If yes, then the scores presented here should provide a starting point for determining an appropriate spatial domain and/or identifying potential issues with a predetermined domain for analysis. If no, and the question at hand can be answered by directly consulting the system of record of a single federal agency, for example, then we recommend using that authoritative source rather than the FPA FOD. The FPA FOD is intended to facilitate interagency or all-lands analyses, not to replace or trump existing systems of record, which remain in authority. In other words, if an analysis of wildfire activity solely on USFS lands is to be performed, then the USFS system of record, FIRESTAT/NIFMID, should be consulted. 

2. _What spatial resolution is required for the analysis?_ The FPA FOD should provide point locations of wildfires at least as precise as a PLSS section (2.6 km<sup>2</sup> grid). But many non-federal records that were excluded from the database due to imprecise fire location information could be used directly from the source systems for analyses at, for example, the county level (e.g., per the Cohesive Strategy, WRSC, 2012). If the analysis does require precise wildfire location information, analysts must bear in mind that the coordinates provided in the FPA FOD may or may not represent actual ignition points, or even fall within the actual burn perimeter, due to reporting inconsistencies and imprecise georeferencing. Moreover, the spatial impacts of large fires, which, by definition, burn far from their ignition points, can be characterized imprecisely at best with this or any pointbased reporting data set. Burned-area estimates from the FPA FOD will be necessarily georeferenced to the contributing wildfires’ ostensible points of origin or nominal domains (e.g., state, reporting unit). Without fire footprints and temporal progression information, one cannot assert for a time period of interest that a given area burned, for example, in the state of Nevada; rather, an estimate from the FPA FOD would represent area burned by fires reported as starting (or having been discovered) within the specified time period and spatial domain. The FPA FOD is therefore most useful for characterizing the statistical properties of fires reported as starting at a given place and time. Supplemental information about spatial and temporal impacts of large fires can be found in the ICS-209 records and MTBS data set using the links provided in the FPA FOD. 

3. _What degree of missing data is tolerable for the analysis?_ The FPA FOD is necessarily incomplete largely 

Earth Syst. Sci. Data, 6, 1–27, 2014 

www.earth-syst-sci-data.net/6/1/2014/ 

K. C. Short: A spatial database of wildfires in the United States 

22 

**Table 9.** Ratio of the number of wildfires estimated, by US state and year, from the FPA FOD to that from the USFS/NICC reference source. Boldface indicates cases in which at least some viable and non-redundant data were available from the non-federal systems of record and were included in the final FOD. Entries of “X” indicate years and states for which no reference estimate was available. Asterisks (*) indicate cases in which the reference estimate is evidently based on incomplete reporting and therefore biased low. Scores for the full 20 yr period and the 10 yr span, 2002–2011, and the 10 yr average annual number of wildfires calculated from the reference source (REF) are also presented. States are grouped into the following regions, per the National Cohesive Wildland Fire Management Strategy: Northeast (NE), Southeast (SE), and West (W) (see USDI and USDA, 2012). Federal Information Processing Standards (FIPS) codes are used to identify states (NIST, 1987). 

||||||||||||||Year|||||||||||Score|10 yr Av<br>|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||||||(REF)|
|Regi|on<br>State|1992|1993|1994|1995|1996|1997|1|998|1999|2000|2001|2002|2003|2004|2005|2006|2007|2008|2009|2010|2011|1992<br>2011|–<br>2002–<br><br>2011||
|NE|CT|**0.77**|**0.99**|**0.91**|**X**|**0.79**|**0.93**|**X**||**1.99**|**1.38**|**0.91**|**0.82**|**0.98**|**0.98**|**0.93**|**0.96**|**0.92**|**0.85**|**0.97**|**0.99**|**0.94**|9.2|9.3|274|
|NE<br>|DE<br>|0.19<br>|0.07<br>|0.10<br>|0.13<br>|0.00<br>|0.11<br>|X<br>||0.11<br>|0.08<br>|0.00<br>|**1.26***<br>|**5.25***<br>|**0.30**<br>|**0.04**<br>|0.03<br>|0.09<br>|0.00<br>|0.00<br>|**0.07**<br>|0.00<br>|1.8<br>|2.5<br>|72<br>|
|NE|IA|0.00|0.01|0.00|0.00|0.03|0.00|X||1.18*|1.06*|**0.83***|**10.20***|**1.47***|**1.92***|**0.11**|**0.62**|**0.49**|**0.73**|**0.85**|**0.73**|**0.72**|5.3|7.3|326|
|NE|IL|0.03|0.01|0.03|0.06|0.08|0.03|X||2.04*|1.00*|**1.31***|**1.39***|**3.00***|**2.32***|**2.30***|**1.31***|**1.29***|**1.08**|**1.12**|**1.16**|**1.17**|7.0|10.0|122|
|NE|IN|0.29|0.15|0.03|0.03|0.05|0.04|X||0.09|0.06|**0.05**|**0.05**|**0.05**|**0.06**|**0.05**|**0.03**|**0.04**|**0.12**|**0.74**|**0.80**|**0.75**|1.8|2.7|2358|
|NE|MA|0.00|0.00|0.00|0.00|0.00|0.00|X||0.00|0.00|**0.01**|**0.04**|**0.04**|**0.04**|**0.01**|**0.01**|**0.02**|**0.01**|0.00|0.00|0.00|0.1|0.2|1914|
|NE|MD|0.02|0.02|0.02|0.03|0.05|0.03|X||0.08|0.06|0.03|0.02|0.04|0.09|**0.94**|**0.93**|**0.89**|**0.91**|**0.63**|**0.97**|**1.02**|3.6|6.4|430|
|NE|ME|**0.80**|**0.89**|**0.88**|**0.91**|**0.92**|**0.87**|**X**||**1.02**|**1.42**|**1.21**|**1.00**|**0.99**|**0.96**|**0.93**|**1.01**|**0.98**|**1.00**|**1.00**|**0.91**|**0.20**|9.1|9.0|520|
|NE|MI|**0.97**|**0.97**|**0.97**|**0.98**|**0.96**|0.19|**X**||**0.21**|0.18|**0.59**|**0.63**|**1.04**|**0.98**|**0.94**|**1.07**|**0.97**|**1.08**|**0.76**|**0.81**|**0.79**|7.9|8.9|556|
|NE|MN|**1.18**|**0.98**|**0.96**|**1.00**|**0.97**|**0.97**|**X**||**1.04**|**0.93**|**0.96**|**1.01**|**0.98**|**0.98**|**0.99**|**1.03**|**0.98**|**1.03**|**0.90**|**1.00**|**1.00**|9.8|9.8|1925|
|NE|MO|**0.25**|**0.29**|**0.55**|**0.59**|**0.07**|**0.53**|**X**||**4.60***|**3.45***|**0.27**|**0.87***|**0.13**|**0.12**|**0.09**|**0.09**|**0.17**|**0.09**|0.05|0.05|**0.22**|3.4|1.9|3275|
|NE|NH|**0.28**|**0.25**|**0.30**|**0.40**|**0.30**|**0.12**|**X**||0.00|**0.17**|**0.12**|**0.15**|**0.13**|**0.13**|**0.14**|**0.22**|**0.17**|**0.22**|**0.20**|**0.24**|**0.03**|1.9|1.6|477|
|NE|NJ|**0.94**|**0.55**|**0.91**|**0.90**|**0.87**|**0.89**|**X**||**0.93**|**1.87**|**0.81**|**0.79**|**0.87**|**0.87**|**0.81**|**0.83**|**0.87**|**0.92**|**0.83**|**0.29**|**0.40**|8.1|7.5|1399|
|NE|NY|**0.98***|**1.08***|**0.95***|**1.00***|**0.97***|**1.02***|**1.**|**13***|**1.07***|**1.01***|**1.01***|**1.01***|**1.00***|**1.00***|**1.00**|**1.00**|**1.00**|**1.01**|**1.00**|**0.90**|**0.98**|9.9|9.9|5662|
|NE|OH|0.04|0.03|0.04|0.04|0.02|0.02|0.|04|0.03|0.03|0.07|**0.19**|**0.12**|**0.17**|**0.16**|**0.29**|**0.45**|**0.27**|**0.20**|**0.29**|**0.33**|1.4|2.5|621|
|NE|PA|0.02|0.03|0.02|0.02|0.03|0.01|X||0.02|0.02|0.04|0.96|**1.00**|**0.91**|**0.97**|**0.95**|**0.95**|**0.89**|**1.01**|**1.00**|**0.99**|5.2|9.6|568|
|NE|RI|0.00|0.00|0.01|0.00|0.00|0.00|X||0.00|0.00|0.00|0.00|0.00|0.00|**0.19**|**0.24**|**0.21**|0.00|0.00|0.00|**1.13**|0.9|1.6|83|
|NE|VT|0.00|0.01|0.03|0.01|0.00|0.01|X||0.02|0.00|0.00|**0.05**|**0.09**|**0.19**|**0.11**|0.04|**0.05**|**0.04**|0.01|0.02|0.00|0.4|0.6|109|
|NE|WI|**0.81**|**0.88**|**0.88**|**0.86**|**0.85**|**0.84**|**X**||**0.99**|**1.00**|**1.00**|**0.99**|**0.98**|**1.00**|**0.96**|**0.97**|**1.01**|**0.91**|**0.96**|**1.00**|**1.00**|9.4|9.8|1384|
|NE|WV|**0.91**|**1.00**|**0.83**|**1.00**|**0.99**|**0.93**|**0.**|**98**|**1.00**|**1.00**|**1.00**|**1.00**|**0.99**|**1.02**|**1.01**|**0.99**|**0.99**|**1.00**|**1.02**|**1.02**|**1.02**|9.8|10.0|799|
|SE|AL|0.01|0.03|**0.73**|**0.90**|**0.86**|**0.85**|**1.**|**01**|**1.01**|**0.97**|**0.99**|**0.69**|**0.94**|**0.79**|**0.98**|**0.80**|**0.83**|**0.65**|**0.62**|**0.98**|**0.67**|7.7|8.0|3349|
|SE|AR|0.07|0.07|0.10|0.07|0.09|**0.75**|**0.**|**78**|**0.81**|**0.81**|**0.89**|**0.73**|**0.95**|**1.01**|**1.04**|**0.95**|**1.01**|**0.96**|**0.96**|**0.94**|**0.97**|6.9|9.5|1771|
|SE|FL|**0.92**|**0.91**|**0.92**|**0.91**|**0.93**|**0.92**|**X**||**0.94**|**0.98**|**0.91**|**1.03**|**1.01**|**1.06**|**1.06**|**1.06**|**0.96**|**1.06**|**1.07**|**0.75**|**0.99**|9.5|9.7|3446|
|SE|GA|**0.98**|**0.98**|**0.98**|**0.98**|**0.98**|**1.00**|**0.**|**98**|**0.98**|**1.00**|**1.00**|**0.99**|**0.98**|**0.99**|**1.00**|**1.00**|**1.00**|**0.99**|**0.99**|**0.99**|**0.99**|9.9|9.9|6892|
|SE|KY|0.04|0.07|0.09|0.08|0.07|**0.71**|**X**||**0.69**|**0.91**|**0.91**|**0.98**|**1.00**|**0.81**|**0.98**|**0.96**|**0.99**|**1.01**|**0.99**|**1.00**|**0.99**|7.0|9.7|1534|
|SE|LA|0.03|0.04|0.05|0.04|0.03|**0.66**|**X**||**0.88**|**0.93**|**0.87**|**0.92**|0.06|0.06|**1.03**|**1.04**|0.05|**0.88**|**0.98**|**1.02**|0.07|5.0|6.0|2071|
|SE|MS|**1.20**|**1.04**|**0.93**|**1.35**|**0.86**|**1.20**|**X**||**0.94**|**1.58**|**3.13***|**2.81***|**7.44***|**20.09***|**27.72***|**0.75**|**0.89**|**1.07**|**0.83**|**0.87**|**0.69**|9.3|9.0|2200|
|SE|NC|**0.98**|**0.99**|**0.98**|**0.98**|**0.98**|**0.97**|**X**||**0.64**|**0.99**|**0.99**|**0.99**|**1.00**|**0.99**|**0.97**|**0.88**|**1.00**|**0.99**|**0.99**|**0.98**|**1.03**|9.6|9.8|4655|
|SE|OK|**0.87**|**0.95**|**0.98**|**1.00**|**0.71**|**0.63**|**X**||**0.76**|**0.85**|**1.06**|**1.09**|**0.84**|**1.04**|**1.06**|**0.98**|**0.38**|**0.39**|**1.16**|**1.24**|**1.02**|8.6|8.6|2601|
|SE|SC|**0.96**|**0.96**|**0.96**|**0.96**|**0.96**|**0.93**|**0.**|**96**|**0.98**|**1.00**|**0.98**|**0.99**|**1.03**|**0.93**|**1.01**|**0.70**|**1.02**|**1.02**|**1.01**|**1.02**|**1.02**|9.6|9.6|2961|
|SE|TN|0.02|0.03|0.03|0.03|0.02|**0.94**|**X**||**0.94**|**0.91**|**0.90**|**1.01**|**0.03**|**0.05**|**1.03**|**0.90**|**1.00**|**0.98**|**0.99**|**0.98**|**1.02**|6.2|7.9|1781|
|SE|TX|**0.96***|**0.92***|**0.77***|**0.97***|**0.99***|**0.96***|**X**||**1.40***|**0.96***|**1.08***|**1.04***|**1.17***|**1.73***|**0.82**|**0.70**|**0.81**|**0.93**|**0.81**|**0.83**|**0.64**|8.9|8.5|12 289|
|SE|VA|0.03|0.06|0.05|**0.90**|**0.93**|**0.87**|**0.**|**97**|**0.84**|**0.90**|**0.82**|**0.91**|**0.80**|**0.33**|**0.95**|**0.95**|**0.93**|**0.98**|**0.49**|**1.03**|**0.98**|7.3|8.3|1153|
|W|AK|**1.01**|**0.99**|**1.00**|**0.99**|**0.99**|**0.99**|**0.**|**99**|**1.00**|**0.99**|**1.03**|**0.99**|**1.00**|**1.00**|**1.00**|**0.98**|**1.01**|**1.00**|**0.98**|**1.00**|**0.99**|9.9|9.8|525|
|W|AZ|**1.00**|**0.98**|**0.99**|**0.93**|**1.00**|0.81|0.|84|**1.02**|**1.04**|**1.01**|**0.91**|**1.00**|**0.99**|**0.91**|**1.00**|**1.01**|**1.03**|**0.98**|**1.01**|**0.96**|9.7|9.8|2667|
|W|CA|**0.92**|**0.92**|**0.88**|**0.88**|**0.89**|**0.87**|**0.**|**90**|**1.02**|**0.95**|**0.88**|**0.87**|**0.96**|**0.94**|**0.93**|**1.00**|**1.11**|**1.24**|**0.93**|**0.83**|**1.06**|9.3|9.5|7662|
|W|CO|**0.70**|**0.61**|**0.55**|**0.51**|0.37|0.32|X||0.38|0.78|0.43|0.36|**1.01**|**0.72**|**0.93**|0.40|0.52|**0.47**|0.32|**0.97**|0.18|5.5|5.9|2824|
|W|HI|018|010|007|004|004|015|**0**|**09**|**004**|**006**|004|**007**|**012**|**003**|**009**|**005**|**020**|**022**|**044***|**140***|**233***|20|32|90|
|W|ID|.<br>**1.05**|.<br>**0.96**|.<br>**0.95**|.<br>**1.09**|.<br>**1.06**|.<br>**1.18**|**X**||**.**<br>**1.12**|**.**<br>**1.18**|.<br>**1.00**|**.**<br>**0.99**|**.**<br>**0.87**|**.**<br>**0.98**|**.**<br>**0.91**|**.**<br>**0.97**|**.**<br>**1.03**|**.**<br>**0.95**|**.**<br>**1.06**|**.**<br>**1.17**|**.**<br>**1.20**|.<br>9.8|.<br>9.7|1358|
|W|KS|0.01|**0.01**|**0.01**|**0.01**|**0.01**|**0.00**|**X**||**0.01**|**0.01**|**0.02**|**0.02**|**0.04**|**1.81***|**2.28***|**2.36***|**2.61***|**2.87***|0.72*|0.80*|0.54*|3.8|7.1|991|
|W|MT|**0.90**|**0.96**|**0.91**|**0.91**|**0.70**|**0.78**|**X**||**1.11**|**0.99**|**1.06**|**1.11**|**1.05**|**1.02**|**1.10**|**1.05**|**1.05**|**1.06**|**0.96**|**1.09**|**0.89**|9.5|9.9|1648|
|W|ND|0.47|0.50|0.53|0.51|0.54|0.39|X||0.81|0.54|0.73|1.12|1.13|0.79|**2.54***|0.77|**0.92**|0.77|1.41|0.96|**1.06**|7.5|9.2|733|
|W<br>|NE<br>|0.03<br>|0.03<br>|**0.06**<br>|**0.04**<br>|**0.04**<br>|**0.05**<br>|**0.**<br>|**05**<br>|**0.05**<br>|**1.03**<br>|**1.03**<br>|**1.07**<br>|**1.05**<br>|**1.08**<br>|**1.06**<br>|**0.99**<br>|**0.99**<br>|**0.96**<br>|**1.01**<br>|**0.97**<br>|**1.00**<br>|6.1<br>|9.9<br>|1157<br>|
|W|NM|**0.71**|**0.74**|**0.98**|**1.00**|**0.98**|**0.97**|**0.**|**77**|**1.05**|**1.12**|**1.03**|**0.95**|**0.91**|**1.04**|**1.21**|**0.71**|**0.99**|0.67|**0.94**|**0.94**|**1.17**|9.1|9.1|1700|
|W|NV|0.75|0.84|0.84|0.92|0.94|1.10|X||0.94|0.91|**0.94**|**0.83**|0.83|**0.80**|**0.85**|**0.81**|**0.78**|**0.91**|**0.83**|**0.73**|**0.88**|8.6|8.3|813|
|W|OR|**0.96**|**0.98**|**0.96**|**1.01**|**0.98**|**0.98**|**X**||**0.96**|**0.97**|**1.03**|**1.04**|**1.01**|**1.00**|**0.94**|**0.98**|**0.98**|**1.25**|**1.22**|**1.47**|**1.71**|9.8|9.9|2177|
|W|SD|**0.65**|**0.83**|**0.91**|**0.60**|**0.95**|**1.29**|**X**||**1.02**|**1.04**|**1.07**|**1.04**|**1.04**|**1.05**|**1.04**|**1.13**|**1.08**|**1.03**|**1.01**|0.64|**1.15**|9.3|9.6|1487|
|W|UT|**0.90**|**0.88**|**0.89**|**0.89**|**0.89**|**0.89**|**1.**|**63***|**1.13**|**0.96**|**0.92**|**0.92**|**0.87**|**0.97**|**1.06**|**1.03**|**1.08**|**1.04**|**1.07**|**1.03**|**0.99**|9.5|9.8|1336|
|W|WA|**0.90**|**0.90**|**0.89**|**0.89**|**0.86**|**0.88**|**X**||**0.99**|**1.10**|**0.91**|**1.10**|**1.04**|**0.95**|**1.09**|**0.99**|**1.03**|**0.91**|**1.01**|**1.20**|**1.03**|9.5|9.8|1370|
|W|WY|**0.72**|**0.72**|**0.70**|**0.81**|**0.66**|0.21|X||0.42|**0.69**|**1.75***|**1.36***|**1.46***|**1.27***|**1.32***|**1.35***|**1.24***|**1.34***|**2.43***|**1.50***|**1.15***|8.4|10.0|856|



due to the lack of viable local wildfire records. Simply because so many fires responded to by local fire services go unreported (Thomas and Butry, 2012), it is impossible to characterize patterns or trends having to do with wildfire numbers on all US lands based on fire reporting. A true all-lands analysis may be possible only with the aid of satellite detections (e.g., MODIS; see Urbanski et al., 2009); however, it is difficult, if not impossible, to confidently tease apart planned from unplanned ignitions (i.e., prescribed and agricultural burns versus wildfires) in remotely sensed data. Yet, we expect that, at the very least, the FPA FOD can be used to faithfully characterize patterns of wildfire area burned within high-scoring states or interstate regions (Fig. 5c 

and d). We expect that this generally holds true regardless of missing local data, because the largest 5 % or so of all fires generally account for upwards of 85 % of total area burned (Strauss et al., 1989; Stocks et al., 2003), and these large fires tend to be multijurisdictional events that are responded to and reported by entities other than (although perhaps in addition to) local fire departments (Bunton, 1999; Artley, 2009). Even so, users should check other data sources and consult with local authorities to confirm that no significant wildfires are missing from the FPA FOD for their focal area before performing analyses of wildfire area burned. A relatively low ratio for a given state-year in Table 10 could guide analysts in this regard, keeping in mind that it is 

Earth Syst. Sci. Data, 6, 1–27, 2014 

www.earth-syst-sci-data.net/6/1/2014/ 

K. C. Short: A spatial database of wildfires in the United States 

23 

**Table 10.** Ratio of the wildfire area burned estimated, by US state and year, from the FPA FOD to that from the USFS/NICC reference source. Boldface indicates cases in which at least some viable and non-redundant data were available from the non-federal systems of record and were included in the final FOD. Entries of “X” indicate years and states for which no reference estimate was available. Asterisks (*) indicate cases in which the reference estimate is evidently based on incomplete reporting and therefore biased low. Scores for the full 20 yr period and the 10 yr span, 2002–2011, and the 10 yr average annual wildfire area burned (hectares) calculated from the reference source (REF) are also presented. States are grouped into the following regions, per the National Cohesive Wildland Fire Management Strategy: Northeast (NE), Southeast (SE), and West (W) (see USDI and USDA, 2012). Federal Information Processing Standards (FIPS) codes are used to identify states (NIST, 1987). 

|||||||||||||||Year|||||||||||Score|10 yr Av<br>(REF)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Re|gion|State|1992|1993|1994|1995|1996|1997|1|998|1999|2000|2001|2002|2003|2004|2005|2006|2007|2008|2009|2010|2011|199<br>201|2–<br>2002–<br>1<br>2011||
|N|E|CT|**0.95**|**1.15**|**0.90**|**X**|**0.71**|**0.98**|**X**||**2.20**|**0.69**|**0.90**|**0.99**|**0.99**|**0.78**|**0.97**|**0.99**|**0.95**|**2.24**|**0.99**|**0.96**|**0.90**|9.2|9.5|134|
|N|E|DE|0.77|0.00|0.63|0.83|0.00|0.05|X||7.80|0.39|0.01|**0.68**|**12.06***|**1.90**|**0.64**|0.08|0.00|0.00|0.00|0.06|0.00|3.8|3.5|147|
|N|E|IA|0.02|0.00|0.01|0.01|0.28|0.02|X||1.10*|1.01*|**1.00***|**0.26***|**0.98***|**1.90***|**0.51**|**0.55**|**0.47**|**0.70**|**0.85**|**0.70**|**0.74**|5.3|6.8|2208|
|N|E|IL|0.07|0.01|0.06|0.14|0.03|0.01|X||2.62*|1.00*|**1.03***|**1.05***|**1.19***|**1.84***|**1.34***|**0.26***|**1.36***|**1.12**|**1.18**|**1.39**|**1.00**|6.6|9.3|486|
|N|E|IN|0.16|0.20|0.03|0.03|0.04|0.03|X||0.06|0.19|**0.28**|**0.44**|**0.32**|**0.15**|**0.17**|**0.21**|**0.28**|**0.13**|**0.89**|**0.86**|**1.24**|2.9|4.5|1889|
|N|E|MA|0.00|0.00|0.00|0.00|0.00|0.00|X||0.00|0.00|**0.13**|**0.20**|**0.26**|**0.13**|**0.33**|**0.24**|**0.24**|**0.29**|0.00|0.15|0.00|1.0|1.8|832|
|N|E|MD|034|048|031|026|022|009|X||051|045|085|041|113|223|**093**|**107**|**126**|**115**|**093**|**226**|**123**|67|93|1759|
|N|E|ME|.<br>**0.97**|.<br>**0.86**|.<br>**0.99**|.<br>**0.97**|.<br>**0.96**|.<br>**0.98**|**X**||.<br>**1.00**|.<br>**1.50**|.<br>**1.15**|.<br>**1.00**|.<br>**0.99**|.<br>**0.84**|**.**<br>**0.88**|**.**<br>**1.03**|**.**<br>**1.17**|**.**<br>**1.00**|**.**<br>**0.99**|**.**<br>**0.84**|**.**<br>**0.44**|.<br>9.3|.<br>9.0|289|
|N|E|MI|**0.97**|**0.98**|**0.99**|**0.98**|**0.98**|0.21|**X**||**0.99**|0.51|**0.67**|**0.61**|**1.01**|**1.00**|**0.96**|**0.96**|**1.01**|**0.98**|**0.56**|**0.53**|**0.53**|8.1|8.1|3323|
|N|E|MN|**1.09**|**1.00**|**1.00**|**1.42**|**1.10**|**0.98**|**X**||**1.29**|**0.98**|**1.00**|**1.02**|**1.12**|**1.03**|**0.90**|**1.06**|**1.05**|**1.08**|**0.85**|**1.05**|**1.02**|9.8|9.7|28815|
|N|E|MO|**0.33**|**0.45**|**0.65**|**0.77**|**0.07**|**1.02**|**X**||**5.15***|**1.32***|**0.37**|**1.99***|**0.07**|**0.22**|**0.18**|**0.29**|**0.39**|**0.27**|0.21|0.33|**0.51**|4.8|3.5|21107|
|N|E|NH|**0.36**|**0.72**|**0.73**|**0.67**|**1.06**|**0.31**|**X**||0.03|**0.83**|**0.34**|**0.39**|**0.47**|**0.80**|**0.39**|**0.43**|**0.38**|**0.95**|**0.70**|**0.35**|**0.09**|5.2|5.0|114|
|N|E|NJ|**1.52**|**0.06**|**0.23**|**3.22**|**0.51**|**0.46**|**X**||**1.04**|**1.41**|**0.98**|**0.96**|**0.63**|**0.88**|**0.88**|**0.89**|**0.99**|**0.98**|**0.81**|**0.35**|**0.19**|7.3|7.6|2307|
|N|E|NY|**1.01***|**1.04***|**0.98***|**1.02***|**1.08***|**1.03***|**1**|**.04***|**1.00***|**0.96***|**1.00***|**1.03***|**1.01***|**0.98***|**1.00**|**1.02**|**1.02**|**1.02**|**1.00**|**0.97**|**0.92**|9.9|9.9|1835|
|N|E|OH|0.03|0.01|0.04|0.04|0.03|0.01|0|.05|0.09|0.09|0.30|**0.08**|**0.47**|**0.07**|**0.37**|**0.34**|**0.53**|**0.29**|**0.44**|**0.36**|**0.24**|1.9|3.2|1543|
|N|E|PA|0.04|0.01|0.01|0.01|0.01|0.03|X||0.06|0.08|0.10|1.08|**1.03**|**1.00**|**0.98**|**0.99**|**0.99**|**0.99**|**1.04**|**1.01**|**0.91**|5.4|9.9|1579|
|N|E|RI|0.00|0.00|0.05|0.00|0.00|0.00|X||0.00|0.00|0.00|0.00|0.00|0.00|**0.43**|**0.78**|**0.61**|0.00|0.00|0.00|**1.04**|1.5|2.8|30|
|N|E|VT|027|001|006|000|000|001|X||004|000|000|**002**|**008**|**006**|**004**|002|**005**|**011**|000|000|000|04|04|85|
|N|E|WI|.<br>**0.95**|.<br>**0.99**|.<br>**0.83**|.<br>**0.91**|.<br>**0.94**|.<br>**0.92**|**X**||.<br>**1.06**|.<br>**1.52**|.<br>**1.23**|**.**<br>**1.14**|**.**<br>**1.19**|**.**<br>**0.99**|**.**<br>**1.03**|.<br>**1.34**|**.**<br>**0.94**|**.**<br>**0.86**|.<br>**1.11**|.<br>**1.14**|.<br>**0.83**|.<br>9.6|.<br>9.6|13527|
|N|E|WV|**0.94**|**0.94**|**0.90**|**0.98**|**0.91**|**0.93**|**0**|**.99**|**1.01**|**0.99**|**0.99**|**1.01**|**0.99**|**1.00**|**1.00**|**0.99**|**0.99**|**1.00**|**1.01**|**1.00**|**0.98**|9.8|10.0|5129|
|SE||AL|0.02|0.07|**0.78**|**0.94**|**0.80**|**0.89**|**1**|**.10**|**1.07**|**1.01**|**0.96**|**0.77**|**1.25**|**1.03**|**1.17**|**1.14**|**0.76**|**0.72**|**1.06**|**1.18**|**0.73**|8.2|9.0|18 479|
|SE||AR|0.07|0.06|0.09|0.09|0.12|**0.76**|**0**|**.84**|**0.87**|**0.81**|**0.98**|**0.89**|**1.41**|**1.07**|**1.18**|**0.86**|**0.72**|**1.02**|**0.92**|**0.92**|**0.87**|6.9|9.2|13 522|
|SE||FL|**0.95**|**0.96**|**0.54**|**0.84**|**0.90**|**0.89**|**X**||**1.19**|**1.20**|**0.96**|**1.10**|**1.26**|**1.18**|**1.00**|**0.84**|**0.93**|**1.18**|**1.16**|**0.93**|**1.06**|9.3|9.7|75 330|
|SE||GA|**0.98**|**0.89**|**0.98**|**0.98**|**0.98**|**0.95**|**1**|**.11**|**1.25**|**1.00**|**1.25**|**1.04**|**0.96**|**1.00**|**0.99**|**0.94**|**1.90**|**1.14**|**1.02**|**1.00**|**2.94***|9.8|9.9|26590|
|SE||KY|0.03|0.04|0.08|0.08|0.06|**0.77**|**X**||**0.78**|**0.97**|**1.07**|**0.98**|**0.95**|**0.80**|**0.94**|**0.90**|**1.08**|**1.01**|**0.99**|**1.00**|**0.95**|7.0|9.5|17 183|
|SE||LA|0.61|0.19|0.10|0.16|0.10|**0.86**|**X**||**1.23**|**0.88**|**1.29**|**0.95**|0.96|0.59|**1.40**|**0.98**|0.07|**1.35**|**1.21**|**1.23**|0.72|6.9|8.3|12377|
|SE||MS|**1.10**|**1.37**|**1.17**|**1.52**|**1.12**|**1.22**|**X**||**1.17**|**0.74**|**1.74***|**2.11***|**5.15***|**13.93***|**10.28***|**0.73**|**1.05**|**1.33**|**0.86**|**1.05**|**0.65**|9.5|9.2|15 954|
|SE||NC|**0.93**|**0.99**|**0.84**|**1.01**|**0.98**|**1.04**|**X**||**0.75**|**1.11**|**1.27**|**0.85**|**0.25**|**0.83**|**0.96**|**0.94**|**0.93**|**0.87**|**0.77**|**0.81**|**0.92**|8.8|8.1|18 003|
|SE||OK|**1.12**|**1.16**|**1.06**|**1.01**|**0.21**|**0.52**|**X**||**0.35**|**1.38**|**0.94**|**1.17**|**1.03**|**1.19**|**1.99**|**1.28**|**0.81**|**0.70**|**2.64**|**1.33**|**1.08**|8.7|9.5|<br>59 205|
|SE||SC|**0.95**|**0.97**|**0.99**|**0.97**|**0.97**|**0.97**|**1**|**.01**|**0.98**|**1.08**|**1.01**|**1.08**|**1.46**|**0.99**|**1.02**|**0.73**|**1.03**|**1.04**|**1.04**|**1.02**|**1.16**|9.8|9.7|8565|
|SE||TN|0.02|0.05|0.12|0.05|0.02|**0.93**|**X**||**0.91**|**1.24**|**0.75**|**0.89**|**0.20**|**0.16**|**1.09**|**0.93**|**1.13**|**0.97**|**1.00**|**1.00**|**1.07**|6.3|8.1|9079|
|SE||TX|**0.92***|**1.03***|**1.03***|**1.18***|**1.15***|**1.16***|**X**||**0.48***|**0.86***|**0.83***|**1.26***|**1.17***|**1.42***|**1.12**|**0.96**|**0.91**|**0.97**|**0.79**|**0.81**|**0.99**|9.2|9.4|348 652|
|SE||VA|0.11|0.13|0.14|**1.00**|**1.00**|**0.87**|**1**|**.47**|**0.85**|**0.88**|**0.87**|**0.91**|**1.49**|**0.60**|**1.02**|**1.20**|**1.03**|**1.00**|**1.00**|**1.22**|**1.04**|8.0|9.1|6403|
|W||AK|**1.12**|**0.96**|**0.99**|**1.00**|**1.00**|**1.00**|**1**|**.00**|**1.00**|**1.00**|**1.01**|**0.99**|**1.00**|**0.98**|**0.99**|**0.96**|**0.98**|**0.89**|**1.00**|**1.00**|**0.99**|9.9|9.8|791 370|
|W||AZ|**0.94**|**1.12**|**1.00**|**1.05**|**1.00**|0.72|0|.54|**0.95**|**1.08**|**1.18**|**0.90**|**1.00**|**0.99**|**0.91**|**0.92**|**1.03**|**1.00**|**0.86**|**1.07**|**1.02**|9.4|9.6|158 703|
|W||CA|**1.05**|**1.14**|**1.05**|**1.04**|**0.95**|**1.15**|**0**|**.75**|**1.08**|**1.08**|**1.03**|**0.97**|**1.06**|**0.97**|**0.92**|**0.94**|**0.96**|**0.93**|**1.01**|**1.09**|**1.29**|9.7|9.7|255 242|
|W||CO|**1.03**|**1.48**|**0.85**|**0.50**|0.67|0.26|X||0.50|0.91|0.50|1.95*|**1.46**|**0.98**|**1.14**|0.23|0.67|**0.78**|0.75|**0.69**|0.70|7.4|7.8|40 437|
|W||HI|0.63|0.14|0.00|0.06|0.40|0.12|**0**|**.47**|**0.00**|**0.89**|0.00|**1.07**|**0.70**|**0.42**|**0.77**|**0.95**|**0.93**|**0.88**|**0.97**|**0.89**|**1.74**|5.6|8.5|4808|
|W||ID|**1.06**|**1.61**|**1.03**|**1.22**|**1.21**|**1.21**|**X**||**0.95**|**1.03**|**1.02**|**0.93**|**0.97**|**1.03**|**1.18**|**0.94**|**1.00**|**1.04**|**1.05**|**1.00**|**1.05**|9.9|9.8|217 291|
|W||KS|0.00|**0.04**|**0.25**|**0.06**|**0.50**|**0.15**|**X**||**0.18**|**0.11**|**0.08**|**0.69**|**0.15**|**0.19***|**1.11***|**0.92***|**0.69***|**1.27***|0.98*|1.02*|0.71|4.6|7.3|<br>21 425|
|W||MT|**1.08**|**1.09**|**1.01**|**1.09**|**0.96**|**1.11**|**X**||**0.89**|**0.86**|**0.88**|**1.12**|**0.97**|**1.16**|**0.91**|**0.83**|**0.93**|**0.97**|**1.10**|**1.26**|**0.85**|9.5|9.5|136 822|
|W||ND|0.35|0.34|0.50|0.46|0.31|0.33|X||0.89|0.41|0.63|0.90|0.56|0.85|**0.95***|0.26|**0.45**|0.63|1.01|0.99|**0.38**|5.9|7.0|13 742|
|W||NE|006|002|**014**|**050**|**013**|**075**|**0**|**41**|**064**|**117**|**111**|**109**|**102**|**104**|**113**|**096**|**096**|**095**|**104**|**101**|**103**|73|99|15 593|
|W||NM|.<br>**078**|.<br>**081**|**.**<br>**102**|**.**<br>**133**|**.**<br>**100**|**.**<br>**118**|**0**|**.**<br>**76**|**.**<br>**107**|**.**<br>**094**|**.**<br>**164**|**.**<br>**075**|**.**<br>**064**|**.**<br>**100**|**.**<br>**110**|**.**<br>**089**|**.**<br>**116**|**.**<br>075|**.**<br>**100**|**.**<br>**056**|**.**<br>**088**|.<br>89|.<br>85|<br>169 141|
|W||NV|**.**<br>0.96|**.**<br>1.02|**.**<br>1.05|**.**<br>1.21|**.**<br>1.10|**.**<br>1.30|X|**.**<br>|**.**<br>1.04|**.**<br>1.02|**.**<br>**0.91**|**.**<br>**0.79**|**.**<br>1.43|**.**<br>**1.04**|**.**<br>**1.07**|**.**<br>**0.95**|**.**<br>**1.06**|.<br>**0.96**|**.**<br>**0.86**|**.**<br>**0.84**|**.**<br>**1.00**|.<br>9.6|.<br>9.4|<br>161 920|
|W||OR|**1.22**|**1.09**|**1.24**|**1.12**|**1.07**|**1.23**|**X**||**0.70**|**0.77**|**1.03**|**0.80**|**1.06**|**0.97**|**0.75**|**0.92**|**0.77**|**1.73**|**0.68**|**0.95**|**0.79**|9.2|9.0|144 909|
|W||SD|**0.70**|**0.69**|**1.09**|**0.29**|**1.16**|**0.79**|**X**||**1.32**|**0.89**|**0.99**|**0.71**|**0.99**|**1.05**|**1.03**|**0.99**|**1.14**|**1.01**|**1.00**|0.45|**0.68**|8.5|8.8|33 545|
|W||UT|**0.84**|**0.68**|**0.86**|**1.21**|**0.96**|**1.08**|**1**|**.22***|**1.19**|**1.00**|**1.03**|**0.90**|**1.07**|**0.95**|**0.78**|**1.03**|**1.08**|**1.08**|**1.02**|**0.97**|**0.99**|9.5|9.6|81 087|
|W||WA|**223**|**339**|**089**|**107**|**293**|**285**|**X**||**125**|**089**|**099**|**101**|**098**|**101**|**072**|**095**|**123**|**080**|**113**|**164**|**221**|96|94|61 137|
|W||WY|**.**<br>**0.61**|**.**<br>**0.61**|**.**<br>**0.78**|**.**<br>**0.87**|**.**<br>**0.59**|**.**<br>0.29|X||**.**<br>0.47|**.**<br>**0.62**|**.**<br>**1.25***|**.**<br>**0.81***|**.**<br>**1.60***|**.**<br>**1.19***|**.**<br>**1.89***|**.**<br>**1.38***|**.**<br>**1.33***|**.**<br>**1.10***|**.**<br>**1.33***|**.**<br>**1.21***|**.**<br>**1.02**|.<br>8.2|.<br>9.8|<br>46 964|



not uncommon to find quite disparate area burned estimates for fires reported and/or mapped in the various systems and applications, indicating that there is much uncertainty inherent in those estimates (Urbanski et al., 2009). 

It is also important that users recognize that the data elements included in the FPA FOD are just a core subset of what may reside in each system of record, and additional elements may be necessary or desirable for the analysis at hand. It may be important, for example, to screen or stratify records based on fire-management objectives or initial suppression strategies (see Johnston and Klick, 2012), which are not elements in the FPA FOD, but may be indicated, albeit inconsistently, in the original, source data sets. For large or otherwise signif- 

icant wildfires occurring since 1999, the ICS-209 records in the SIT/209 databases accessible via FAMWEB should provide some of the most detailed and consistently available information regarding suppression and other management actions taken during those incidents (see NIFC, 2011; NWCG, 2012a), and where ICS_209_INCIDENT_NUMBER and ICS_209_INCIDENT_NAME are populated in the FPA FOD, those attributes, along with FIRE_YEAR, can be used to join the two data sets. Users can then define their own criteria for distinguishing different fire types, as relevant to their analyses. 

Given careful consideration of the assessment to be performed and a thorough understanding of the data and their limitations, the FPA FOD should provide unprecedented 

Earth Syst. Sci. Data, 6, 1–27, 2014 

www.earth-syst-sci-data.net/6/1/2014/ 

K. C. Short: A spatial database of wildfires in the United States 

24 

**Table A1.** Key abbreviations, acronyms, and aliases and their definitions. 

|AWSR|Annual Wildfire Summary Report|
|---|---|
|BIA|US Department of the Interior, Bureau of In-<br>dian Affairs|
|BLM|US Department of the Interior, Bureau of<br>Land Management|
|EFETAC|USFS Eastern Forest Environmental Threat<br>Assessment Center|
|FAMWEB|Fire and Aviation Management Web<br>Applications|
|FIPS|Federal Information Processing Standards|
|FIRESTAT|USFS Fire Statistics System|
|FMIS|FWS Fire Management Information System|
|FOD|Fire-occurrence database|
|FPA|Fire Program Analysis|
|FPU|Fire planning unit|
|FWS|US Department of the Interior, Fish and<br>Wildlife Service|
|ICS-209|SIT/209 module that includes data from the<br>Incident Status Summary form|
|LANDFIRE|Landscape Fire and Resource Management<br>Planning Tools Project|
|MTBS|USFS Monitoring Trends in Burn Severity<br>project|
|NASF|National Association of State Foresters|
|NFIRS|USFA National Fire Incident Reporting<br>System|
|NICC|National Interagency Coordination Center|
|NIFMID|National Interagency Fire Management<br>Integrated Database|
|NIFSIP|National Interagency Fire Statistics<br>Information Project|
|NPS|US Department of the Interior, National Park<br>Service<br>i|
|NWCG|National Wildfire Coordinating Group|
|PLSS|Public Land Survey System|
|SIT/209|Situation Report/ICS-209 application<br>i|
|SWRA|Southern Wildfire Risk Assessment|
|TFS|i<br>Texas A&M Forest Service|
|USFA|US Fire Administration|
|USFS|US Department of Agriculture, Forest Service|
|WFMI|(BIA, BLM, NPS) Wildland Fire|
||Management Information system|



one-stop access to spatially explicit US wildfire records for 1992–2011 to support statistical analyses of data from the authoritative systems of record. Acquisition, standardization, error checking, compilation, scrubbing, and evaluation of these data required a tremendous effort, but the effort was necessary for the analyses required by FPA. Assuming that the need for fully scalable US wildfire activity statistics from the systems of record will persist, efforts like those described here, which essentially expand upon similar undertakings in past decades (e.g., Brown et al., 2002; Schmidt et al., 

2002), must necessarily continue until at least the most basic elements of wildland fire reporting are truly standardized and a national system of record is established and used by federal, state, and local firefighting entities. Progress toward those goals appears promising under the auspices of the Integrated Reporting of Wildland-Fire Information (IRWIn) project, which is sponsored by the NWCG and intended to provide an “integrated and coordinated process for collecting and reporting [wildland fire] incident/event data” (USDI, 2013). In addition to enforcing NWCG data standards, IRWIn, as proposed, would provide linkages between wildland fire dispatch and reporting systems, including those of nonfederal entities, using a global unique identifier for each incident. Indeed, IRWIn may provide the ultimate way forward in national wildland fire reporting and statistical analyses. In the meantime, the FPA FOD is intended to help fulfill information needs heretofore met with great difficulty or not at all. 

**Acknowledgements.** We are grateful to Kole Berriochoa, Cal Gale, Brad Harwood, Bill Johnson, Steve Larrabee, Charlie Leonard, Steve Norman, Brad Quayle, Sharon Shepard, Curt Stripling, and Andy Tait for help in acquiring and understanding the data; to Roshelle Pederson for sharing her insights into the IRWIn project; and to Marty Ahrens, Mark Finney, Jaymee Fotjik, Isaac Grenfell, Faith Ann Heinsch, Kathy Hinds, Bill Johnson, Chuck McHugh, Karin Riley, Brent Timothy, and Garth Whitson for reviewing and providing feedback on initial drafts of this manuscript. We also thank the reviewers who provided feedback during the journal’s interactive public discussion phase; their suggestions helped to improve the paper. 

Edited by: D. Carlson 

## **References** 

- Ager, A. A., Vaillant, N. M., and Finney, M. A.: A comparison of landscape fuel treatment strategies to mitigate wildland fire risk in the urban interface and preserve old forest structure, Forest Ecol. Manag., 259, 1556–1570, doi:10.1016/j.foreco.2010.01.032, 2010. 

- Andrews, P.: Fire danger rating and fire behaviour prediction in the United States, in: Proceedings of the Fifth NRIFD Symposium, International Symposium on Forest Fire Protection, Mitaka, Tokyo, Japan, 30 November–2 December, 106–117, 2005. 

- Andrews, P. L. and Bradshaw, L. S.: FIRES: Fire Information Retrieval and Evaluation System – a program for fire danger rating analysis, USDA Forest Service, Intermountain Research Station, Ogden, UT, USA, General Technical Report INT-GTR-367, 64 pp., 1997. 

- Andrews, P., Finney, M., and Fischetti, M.: Predicting wildfires, Sci. Am., August, 47–55, 2007. 

- Artley, D. K.: Wildland fire protection and response in the United States: the responsibilities, authorities, and roles of federal, state, local, and tribal government, Report for the International 

Earth Syst. Sci. Data, 6, 1–27, 2014 

www.earth-syst-sci-data.net/6/1/2014/ 

K. C. Short: A spatial database of wildfires in the United States 

25 

- Association of Fire Chiefs, available at: http://www.iafc.org/ files/wild_MissionsProject.pdf, 2009. 

- Bland, J. M. and Altman, D. G.: Statistical methods for assessing agreement between two methods of clinical measurement, Lancet, 1, 307–310, 1986. 

- Bradshaw, L. S. and McCormick, E.: FireFamily Plus user’s guide, version 2.0, USDA Forest Service, Rocky Mountain Research Station, Ogden, UT, USA, General Technical Report RMRSGTR-67WWW, 124 pp., 2000. 

- Brown, A. A.: Reliable statistics and fire research, Fire Control Notes, 20, 101–104, 1959. 

- Brown, T. J., Hall, B. L., Mohrle, C. R., and Reinbold, H. J.: Coarse assessment of federal wildland fire occurrence data, Desert Research Institute, Program for Climate, Ecosystem and Fire Applications, Reno, NV, USA, CEFA Report 02–04, 31 pp., 2002. 

- Buckley, D., Berry, J. K., Spencer, T., and Carlton, D.: Quantifying wildland fire risk in the South, Sanborn Map Company, Colorado Springs, CO, USA, Southern Wildfire Risk Assessment Project Report, 10 pp., 2006. 

- Bunton, D. R.: Sharing information through fire reporting, Fire Management Notes, 59, 37–42, 1999. 

- Bunton, D. R.: Wildland fire and weather information data warehouse, in: Proceedings of the Seventh Symposium on Systems Analysis on Forest Resources, Traverse City, MI, USA, 28–31 May 1997, USDA Forest Service, North Central Forest Experiment Station, St. Paul, MN, USA, General Technical Report GTR-NC-205, 297–302, 2000. 

- Calkin, D. E., Ager, A. A., Gilbertson-Day, J., Scott, J. H., Finney, M. A., Schrader-Patton, C., Quigley, T. M., Strittholt, J. R., and Kaiden, J. D.: Wildfire risk and hazard: procedures for the first approximation, USDA Forest Service, Rocky Mountain Research Station, Fort Collins, CO, USA, General Technical Report RMRS-GTR-235, 62 pp., 2010. 

- Collins, B. M., Omi, P. N., and Chapman, P. L.: Regional relationships between climate and wildfire-burned area in the Interior West, Can. J. Forest Res., 36, 699–709, doi:10.1139/X05-264, 2006. 

- Davis, B. H. and Miller, C.: What if we didn’t suppress fire? in: Proceedings of the 2009 George Wright Society Biennial Conference on Parks, Protected Areas, and Cultural Sites, Portland, OR, USA, 1–6 March 2009, 131-134, 2010. 

- Donoghue, L. R.: The history and reliability of the USDA Forest Service wildfire report, USDA Forest Service, North Central Forest Experimental Station, St. Paul, MN, USA, Research Paper NC-226, 15 pp., 1982a. 

- Donoghue, L. R.: Classifying wildfire causes in the USDA Forest Service: problems and alternatives, USDA Forest Service, North Central Forest Experimental Station, St. Paul, MN, USA, Research Note NC-280, 5 pp., 1982b. 

- Eidenshink, J., Schwind, B., Brewer, K., Zhu, Z.-L., Quayle, B., and Howard, S.: A project for monitoring trends in burn severity, Fire Ecology, 3, 3–21, 2007. 

- Finney, M. A., McHugh, C. W., Grenfell, I. C., Riley, K. L., and Short, K. C.: A simulation of probabilistic wildfire risk components for the continental United States, Stoch. Env. Res. Risk A, 25, 973–1000, doi:10.1007/s00477-011-0462-z, 2011. 

- [FPA] Fire Program Analysis: FPA data processing guide: preparing clean historic fire occurrence records, Boise, ID, USA, unpublished report, 16 pp., 2010. 

- Fried, J. S. and Fried, B. D.: A foundation for initial attack simulation: Fried and Fried fire containment model, Fire Manage. Today, 70, 44–47, 2010. 

- Gedalof, Z., Peterson, D. L., and Mantua, N. J.: Atmospheric, climatic, and ecological controls on extreme wildfire years in the northwestern United States, Ecol. Appl., 15, 154–174, doi:10.1890/03-5116, 2005. 

- Hall, J. R. and Harwood, B.: The national estimates approach to U. S. fire statistics, Fire Technol., 25, 99–113, 1989. 

- Hammer, R. B., Stewart, S. I., and Radeloff, V. C.: Demographic trends, the wildland-urban interface, and wildfire management, Soc. Nat. Res.: Intl. J., 22, 777–782, doi:10.1080/08941920802714042, 2009. 

- Hardy, C. C. and Hardy, C. E.: Fire danger rating in the United States of America: an evolution since 1916, Int. J. Wildland Fire, 16, 217–231, doi:10.1071/WF06076, 2007. 

- Johnston, J. S. and Klick, J.: Fire suppression policy, weather, and Western wildfire trends, in: Wildire Policy: Law and Economics Perspectives, edited by: Bradshaw, K. M. and Leuck, D., RFF Press, New York, NY, USA, 159–177, 2012. 

- Kolden, C. A. and Brown, T. J.: Beyond wildfire: perspectives of climate, managed fire and policy in the USA, Int. J. Wildland Fire, 19, 364–373, doi:10.1071/WF08111, 2010. 

- Littel, J. S., McKenzie, D., Peterson, D. L., and Westerling, A. L.: Climate and wildfire area burned in western U.S. ecoprovinces, 1916–2003, Ecol. Appl., 19, 1003–1021, doi:10.1890/07-1183.1, 2009. 

- Mavsar, R., Caban, A. G., and Varela, E.: The state of development of fire management decision support systems in America and Europe, Forest Policy Econ., 29, 45–55, doi:10.1016/j.forpol.2012.11.009, 2013. 

- McKenzie, D., Gedalof, Z., Peterson, D. L., and Mote. P.: Climatic change, wildfire, and conservation, Conserv. Biol., 18, 890–902, doi:10.1111/j.1523-1739.2004.00492.x, 2003. 

- Miller, C. and Ager, A. A.: A review of recent advances in risk analysis for wildfire management, Int. J. Wildland Fire, 22, 1– 14, doi:10.1071/WF11114, 2012. 

- Miller, J. D., Safford, H. D., Crimmins, M., and Thode, A. E.: Quantitative evidence for increasing forest fire severity in the Sierra Nevada and Southern Cascade Mountains, California and Nevada, USA, Ecosystems, 12, 16–32, doi:10.1007/s10021-0089201-9, 2008. 

- Miller, J. D., Skinner, C. N., Safford, H. D., Knapp, E. E., and Ramirez, C. M.: Trends and causes of severity, size, and number of fires in northwestern California, USA, Ecol. Appl., 22, 184–203, doi:10.1890/10-2108.1, 2012. 

- [NFAEB] National Fire and Aviation Executive Board: Fire Occurrence Reporting System (FORS) study, Commonthread Incorporated, Boise, ID, USA, business needs analysis report, 91 pp., available at: http://www.nwcg.gov/teams/fenwt/study/, 2007. 

- [NICC] National Interagency Coordination Center: Understanding the information provided in the National Incident Managment Situation Report (IMSR), National Interagency Fire Center, Boise, ID, USA, Predictive Services Report 6-2012, 7 pp., available at: http://www.predictiveservices.nifc.gov/intelligence/ Reading_the_Situation_Report.pdf, 2012a. 

- [NICC] National Interagency Coordination Center: Wildland fire summary and statistics annual report 2012, National Interagency Fire Center, Boise, ID, USA, 72 pp., available 

Earth Syst. Sci. Data, 6, 1–27, 2014 

www.earth-syst-sci-data.net/6/1/2014/ 

K. C. Short: A spatial database of wildfires in the United States 

26 

at: http://www.predictiveservices.nifc.gov/intelligence/2012_ statssumm/annual_report_2012.pdf, 2012b. 

- [NIFC] National Interagency Fire Center: 209 Program user’s guide, National Interagency Fire Center, Boise, ID, USA, 110 pp., available at: http://gacc.nifc.gov/rmcc/predictive/209_ Program_Users_Guide.pdf, 2011. 

- [NIST] National Institute of Standards and Technology: Codes for the identification of the states, the District of Columbia, and the outlying areas of the United States, and associated areas, Federal Information Processing Standards Publication 5-2, available at: http://www.itl.nist.gov/fipspubs/fip5-2.htm, 1987. 

- [NIST] National Institute of Standards and Technology: Counties and equivalent entities of the United States, its possessions, and associated areas, Federal Information Processing Standards Publication 6-4, available at: http://www.itl.nist.gov/fipspubs/fip6-4. htm, 1990. 

- Noonan-Wright, E. K., Opperman, T. S., Finney, M. A., Zimmerman, G. T., Seli, R. C., Elenz, L. M., Calkin, D. E., and Fiedler, J. R.: Developing the US Wildland Fire Decision Support System, J. Combust., 2011, 1–14, doi:10.1155/2011/168473, 2011. 

- [NWCG] National Wildfire Coordinating Group: Fire statistics: a white paper, NWCG Fire Statistics Task Group, 76 pp., available at: http://www.wrapair.org/forums/fejf/meetings/ 040310/Fire_Statistics_White_Paper.pdf, 2003. 

- [NWCG] National Wildfire Coordinating Group: Wildland fire data and fiscal management for complexes, mergers, and splits, National Interagency Fire Center, Boise, ID, USA, Memorandum NWCG#014-2011, 5 pp., available at: http://www.nwcg.gov/ general/memos/nwcg-014-2011.pdf, 2011. 

- [NWCG] National Wildfire Coordinating Group: National Interagency Mobilization Guide, National Interagency Fire Center, Boise, ID, USA, NFES #2092, 223 pp., available at: https://www.llis.dhs.gov/sites/default/files/2012_Mobilization_ Guide.pdf, 2012a. 

- [NWCG] National Wildfire Coordinating Group: NWCG Unit Identifier, National Interagency Fire Center, Boise, ID, USA, Memorandum NWCG#012-2012, 4 pp., available at: http://www.nwcg. gov/general/memos/nwcg-012-2012.pdf, 2012b. 

- [NYDEC] New York Department of Environmental Conservation: Wildfire in New York state, http://www.dec.ny.gov/lands/42378. html, last access: 24 April 2013. 

- Parisien, M.-A. and Moritz, M.: Environmental controls on the distribution of wildfire at multiple spatial scales, Ecol. Monogr., 79, 127–154, doi:10.1890/07-1289.1, 2007. 

- Parisien, M.-A., Snetsinger, S., Greenberg, J. A., Nelson, C. A., Schoenaggel, T., Dobrowski, S. Z., and Moritz, M. A.: Spatial variability in wildfire probability across the westhern United States, Int. J. Wildland Fire, 21, 313–327, doi:10.1071/WF11044, 2012. 

- Preisler, H. K., Burgan, R. E., Eidenshink, J. C., Klaver, J. M., and Klaver, R. W.: Forecasting distributions of large federal-lands fires utilizing satellite and gridded weather information, Int. J. Wildland Fire, 18, 508–516, doi:10.1071/WF08032, 2009. 

- Reid, A. M., Fuhlendorf, S. D., and Weir, J. R.: Weather variables affecting Oklahoma wildfires, Rangeland Ecol. Manag., 63, 599– 603, doi:10.2111/REM-D-09-00132.1, 2010. 

- Ryan, K. C. and Opperman, T. S.: LANDFIRE – A national vegetation/fuels data base for use in fuels treatment, restoration, 

- and suppression planning, Forest Ecol. Manag., 294, 208–216, doi:10.1016/j.foreco.2012.11.003, 2013. 

- [Sanborn] Sanborn Map Company: Sanborn Wildland Fire Risk Assessment System (WFRAS), Colorado Springs, CO, USA, 6 pp., available at: http://www.innovativegis.com/basis/present/gw05_ wildfire/WFRAS_Jan09.pdf, 2009. 

- Schmidt, K. M., Menakis, J. P., Hardy, C. C., Hann, W. J., and Bunnell, D. L.: Development of coarse-scale spatial data for wildland fire and fuel management, USDA Forest Service, Rocky Mountain Research Station, Fort Collins, CO, USA, General Technical Report RMRS-87, 41 pp. + CD, 2002. 

- Scott, J. and Burgan, R. E.: Standard fire behavior fuel models: a comprehensive set for use with Rothermel’s surface fire spread model, USDA Forest Service, Rocky Mountain Research Station, Fort Collins, CO, USA, General Technical Report RMRS-GTR153, 72 pp., 2005. 

- Scott, J., Helmbrecht, D., Thompson, M. P., Calkin, D. E., and Marcille, K.: Probabilistic assessment of wildfire hazard and municipal watershed exposure, Nat. Hazards, 64, 707-728, doi:10.1007/s11069-012-0265-7, 2012. 

- Show, S. B. and Kotok, E. I.: Forest fires in California, 1911–1920: an analytical study, Goverment Printing Office, Washington, DC, USA, USDA Department Circular 243, 83 pp., 1923. 

- Stephens, S. L.: Forest fire cause and extent on United States Forest Service lands, Int. J. Wildland Fire, 14, 213–222, doi:10.1071/WF04006, 2005. 

- Stocks, B. J., Mason, J. A., Todd, J. B., Bosch, E. M., Wotton, B. M., Amiro, B. D., Flannigan, M. D., Hirsch, K. G., Logan, K. A., Martell, D., A., and Skinner, W. R.: Large forest fires in Canada, 1959–1997, J. Geophys. Res.-Atmos., 108, 8149–8160, doi:10.1029/2001JD000484, 2003. 

- Strauss, D., Bednar, L., and Mees, R.: Do one percent of forest fires cause ninety-nine percent of the damage?, Forest Sci., 35, 319– 328, 1989. 

- Stratton, R. D.: Guidance on spatial wildland fire analysis: models, tools, and techniques, USDA Forest Service, Rocky Mountain Research Station, Fort Collins, CO, USA, General Technical Report RMRS-GTR-183, 15 pp., 2006. 

- [TFS] Texas A&M Forest Service: Self-evaluation report, submitted to the State of Texas Sunset Advisory Commission, 175 pp., 2009. 

- [TFS] Texas A&M Forest Service: Texas Wildfire Protection Plan FY 2012–2013 Biennium, draft report released for public comment, 45 pp., revised 8 November, 2012. 

- Thomas, D. S. and Butry, D. T.: Wildland fires within municipal jurisdictions, J. Forest, 110, 34–41, doi:10.5849/jof.10-024, 2012. 

- Thompson, M. P., Calkin, D. E., Finney, M. A., Ager, A. A., and Gilbertson-Day, J. W.: Integrated national-scale assessment of wildfire risk to human and ecological values, Stoch. Env. Res. Risk A, 25, 761–780, doi:10.1007/s00477-011-0461-0, 2011. 

- Urbanski, S. P., Salmon, J. M., Nordgren, B. L., and Hao, W. M.: A MODIS direct broadcast algorithm for mapping wildfire burned area in the western United States, Remote Sens. Environ., 113, 2511–2526, doi:10.1016/j.rse.2009.07.007, 2009. 

- [USDI] US Department of the Interior: Fire Program Analysis Application, Bureau of Land Management, Washington, DC, USA, Information Bulletin No. 2009-040, available at: http: //www.blm.gov/wo/st/en/info/regulations/Instruction_Memos_ 

Earth Syst. Sci. Data, 6, 1–27, 2014 

www.earth-syst-sci-data.net/6/1/2014/ 

K. C. Short: A spatial database of wildfires in the United States 

27 

and_Bulletins/national_information/2009/IB_2009-040.html, 2009. 

- [USDI] US Department of the Interior: IRWIn, http://www.doi.gov/ pmb/owf/irwin.cfm, last access: 24 April 2013. 

- [USDI and USDA] US Department of the Interior and US Department of Agriculture: Federal wildland fire management policy and program review, Washington, DC, USA, final report, 45 pp., available at: http://www.nwcg.gov/branches/ppm/fpc/archives/fire_policy/ mission/1995_fed_wildland_fire_policy_program_report.pdf, 1995. 

- [USDI and USDA] US Department of the Interior and US Department of Agriculture: A national cohesive wildland fire management strategy, Washington, DC, USA, Phase II National Report, 78 pp., available at: http://www.forestsandrangelands.gov/strategy/documents/ reports/phase2/CSPhaseIIReport_FINAL20120524.pdf, 2012. 

- [USDI and USDA] US Department of the Interior and US Department of Agriculture: FireCode System Release 1.9 user guide, National Interagency Fire Center, Boise, ID, USA, 70 pp., available at: https://www.firecode.gov/help/User_Guide.pdf, 2013. 

- [USDI et al.] US Department of the Interior, US Department of Agriculture, Department of Energy, Department of Defense, Department of Commerce, US Environmental Protection Agency, Federal Emergency Management Agency, and National Association of State Foresters: Review and update of the 1995 Federal Wildland Fire Management Policy, Washington, DC, 86 pp., available at: http://www.nwcg.gov/branches/ppm/fpc/ archives/fire_policy/history/index.htm, 2001. 

- [USFS] US Forest Service: 1991–1997 wildland fire statistics, USDA Forest Service, Fire and Aviation Management, Washington, DC, USA, 141 pp., 1998a. 

- [USFS] US Forest Service: National Interagency Fire Management Integrated Database (NIFMID), USDA Forest Service, Fire and Aviation Management, Washington, DC, USA, draft technical guide, 110 pp., available at: http://www.fs.fed.us/fire/planning/ nist/nifmid.pdf, 1998b. 

   - [USFS] US Forest Service: Individual Fire Report Form FS5100-29, USDA Forest Service, Washington, DC, USA, available at: http://www.fs.fed.us/fire/planning/nist/fs-5100-29_v3b_ wildl.rtf, 2000. 

   - [USFS] US Forest Service: FIRESTAT User’s Guide Version 5.4, USDA Forest Service, Fire and Aviation Management, Washington, DC, USA, 145 pp., available at: http://www.fs.fed.us/fire/ planning/nist/firestat_54/firestat_users_guide_2003_1117.pdf, 2003. 

   - [USFS] US Forest Service: Interagency wildland fire incident information reporting application (SIT/209), Commonthread Incorporated, Boise, ID, USA, business requirements analysis report prepared for Fire and Aviation Management and Predictive Services, 74 pp., available at: http://www.predictiveservices.nifc. gov/intelligence/SIT-209_Bus_Req_Final_v1a.pdf, 2009. 

   - [USFS] US Forest Service: Information collection: Annual Wildfire Summary Report, Federal Register, 75, 3193, 2010. 

   - Westerling, A. L., Gershunov, A., Brown, T. J., Cayan, D. R., and Dettinger, M. D.: Climate and wildfire in the western United States, B. Am. Meteorol. Soc., 84, 595–604, doi:10.1175/BAMS-84-5-595, 2003. 

   - Westerling, A. L., Hidalgo, H. G., Cayan, D. R., and Swetnam, T. W.: Warming and earlier spring increase western U.S. forest wildfire activity, Science, 313, 940–943, doi:10.1126/science.1128834, 2006. 

   - Wolf, J. A. and Buckley, D.: West Wide Wildfire Risk Assessment project overview, unpublished report, 2 pp., 2010. 

   - [WRSC] Western Regional Strategy Committee: The national cohesive wildland fire management strategy: phase III western regional science-based risk analysis final report, Washington, DC, USA, 102 pp., available at: http: //www.forestsandrangelands.gov/strategy/documents/reports/ phase3/WesternRegionalRiskAnalysisReportNov2012.pdf, 2012. 

- [USFS] US Forest Service: National Interagency Fire Statistics Information Project, USDA Forest Service, Fire and Aviation Management, Washington, DC, USA, analysis phase report, 31 pp., available at: http://www.fs.fed.us/fire/planning/nist/ Analysis_Stage_Report.pdf, 1998c. 

Earth Syst. Sci. Data, 6, 1–27, 2014 

www.earth-syst-sci-data.net/6/1/2014/ 
