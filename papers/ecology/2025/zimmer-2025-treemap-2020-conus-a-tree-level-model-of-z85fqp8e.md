---
title: 'TreeMap 2020 CONUS: A tree-level model of the forests of the conterminous United States circa 2020'
authors:
- Zimmer, Scott N.
- Houtman, Rachel M.
- Leatherman, Lila S. T.
- Housman, Ian W.
- Shrestha, Abhinav
- Shaw, John D.
- Riley, Karin L.
year: '2025'
journal: null
doi: 10.2737/RDS-2025-0031
tags: []
zotero_key: Z85FQP8E
item_type: dataset
url: https://www.fs.usda.gov/rds/archive/catalog/RDS-2025-0031
source_url: 'unpaywall: https://figshare.com/articles/dataset/TreeMap_2020_CONUS_A_tree-level_model_of_the_forests_of_the_conterminous_United_States_circa_2020/29614463'
fulltext_status: fulltext
synced: '2026-11-06'
---

# TreeMap 2020 CONUS: A tree-level model of the forests of the conterminous United States circa 2020

## Full text

# TreeMap 2020 CONUS: A tree-level model of the forests of the conterminous United States circa 2020

* <https://doi.org/10.2737/RDS-2025-0031>

  [Open external identifier URL](https://doi.org/10.2737/RDS-2025-0031)Copy identifier URL to clipboardIdentifier Info

CiteShare

dataset

 posted on 2025-07-23, 01:32 authored by Scott N. Zimmer, Rachel M. Houtman, Lila S. T. Leatherman, Ian W. Housman, Abhinav Shrestha, John D. Shaw, Karin L. Riley

TreeMap 2020 CONUS provides a tree-level model of the forests of the conterminous United States. Throughout the conterminous United States (CONUS), for each forested pixel in 30×30 meter (m) gridded landscape data for circa 2020, we identified and assigned the most similar Forest Inventory and Analysis (FIA) plot. We used a Random Forest machine-learning algorithm to impute the forest plot data to a set of target rasters provided by Landscape Fire and Resource Management Planning Tools (LANDFIRE) and Daymet (Daymet). Predictor variables consisted of percent forest cover, vegetation height, and vegetation type, as well as topography (slope, elevation, and aspect), location (latitude and longitude), climatic variables (precipitation, shortwave radiation, snow water equivalent, maximum temperature, minimum temperature, vapor pressure, and vapor pressure deficit), and disturbance history (time since disturbance and disturbance type).
The main output of this project (the GeoTIFF included in this data publication) is a raster map of imputed plot identifiers at 30×30 m spatial resolution for the conterminous U.S., corresponding to landscape conditions circa 2020. In the attribute table of this raster, we also present a set of attributes drawn from the FIA databases, including forest type and live basal area. The raster of plot identifiers can be linked to the FIA databases available through the FIA DataMart to map hundreds of attributes available there, or to the comma-separated file included in this data publication to access a more limited set of tree-level attributes. The data files included in this publication also contain attributes for each tree in the plots that were assigned, including the FIA plot PLT\_CN for the plot on which the tree was measured (or control number, a unique identifier for each time a plot is measured), the subplot number, the tree record number, the corresponding number of trees per acre it represents due to the study design, the status (live or dead), species, diameter, height, actual height (where broken), crown ratio and a code for cause of death where applicable. Previous versions of TreeMap have been validated for characteristics including percent live tree cover, height of the dominant trees, forest type, species of trees with most basal area, and snag hazard category. Previous versions of TreeMap are being used in both the private and public sectors for projects including fuel treatment planning, snag hazard mapping, and estimation of terrestrial carbon resources.<br>Geospatial data describing tree species or forest structure are required for many analyses and models of forest landscape dynamics. Forest data must have resolution and continuity sufficient to reflect site gradients in mountainous terrain and stand boundaries imposed by historical events, such as wildland fire and timber harvest. The TreeMap 2014 dataset (Riley et al. 2019) was the first of its kind to provide such detailed forest structure data across the forests of the conterminous United States. Prior to the TreeMap 2014 imputed forest data, assessments relied largely on forest inventory at fixed plot locations at sparse densities. The TreeMap 2016 dataset (Riley et al. 2021, Riley et al. 2022) updated the 2014 version to include disturbance as a response variable, which improved accuracy in disturbed areas. The TreeMap 2020 CONUS dataset featured here updates the TreeMap 2016 dataset to landscape conditions circa 2020 and updates the methods by 1) using a different suite of climate variables in the imputation and 2) improving species composition assignments to prevent plots being imputed to areas where their existing vegetation type was not present, an issue which affected a small number of pixels in previous TreeMap versions.<br>See the Entity and Attributes section for details regarding the relationship between the data files included in this publication and the FIA DataMart (https://doi.org/10.2737/RDS-2001-FIADB).
For more information about these data, see Riley et al. (2022).
TreeMap 2020 was originally published on 06/25/2025. On 05/11/2026, we made some minor updates to the raster attribute tables: we have replaced the binned canopy height (STANDHT) and percent canopy cover (CANOPYPCT) fields with continuous values. The original values were not incorrect, just at a lower resolution than the 2016 TreeMap, so we updated TreeMap 2020 for consistency with previous TreeMap versions.

## Funding

### USDA-FS

## History

## Related Materials

1. 1. 

   DOI - Is supplemented by [TreeMap 2022 CONUS: A tree-level model of the forests of the conterminous United States circa 2022(2025)](https://doi.org/10.2737/RDS-2025-0032)
2. 2. 

   DOI - Is supplemented by [TreeMap 2016 dataset generates CONUS-wide maps of forest characteristics including live basal area, aboveground carbon, and number of trees per acre(2022)](https://doi.org/10.1093/jofore/fvac022)
3. 3. 

   URL - Is supplemented by [TreeMap 2016 dataset generates CONUS-wide maps of forest characteristics including live basal area, aboveground carbon, and number of trees per acre(2022)(2022)](https://research.fs.usda.gov/treesearch/65597)
4. 4. 

   DOI - Is supplemented by [TreeMap, a tree-level model of conterminous US forests circa 2014 produced by imputation of FIA plot data(2021)](https://doi.org/10.1038/s41597-020-00782-x)
5. 5. 

   URL - Is supplemented by [TreeMap, a tree-level model of conterminous US forests circa 2014 produced by imputation of FIA plot data(2021)(2021)](https://research.fs.usda.gov/treesearch/61840)
6. 6. 

   DOI - Is supplemented by [TreeMap 2016: A tree-level model of the forests of the conterminous United States circa 2016(2021)](https://doi.org/10.2737/RDS-2021-0074)
7. 7. 

   DOI - Is supplemented by [Fire Lab tree list: A tree-level model of the conterminous United States landscape circa 2014(2019)](https://doi.org/10.2737/RDS-2019-0026)
8. 8. 

   DOI - Is supplemented by [Fire Lab tree list: A tree-level model of the western US circa 2009 v1(2018)](https://doi.org/10.2737/RDS-2018-0003)
9. 9. 

   DOI - Is supplemented by [Mapping forest vegetation for the western United States using modified Random Forest imputation of FIA forest plots(2016)](https://doi.org/10.1002/ecs2.1472)
10. 10. 

    URL - Is supplemented by [Mapping forest vegetation for the western United States using modified Random Forest imputation of FIA forest plots(2016)(2016)](https://research.fs.usda.gov/treesearch/53114)

## Data contact name

Karin Riley

## Data contact email

[karin.l.riley@usda.gov](mailto:karin.l.riley@usda.gov)

## Publisher

Forest Service Research Data Archive

## Use limitations

These data were collected using funding from the U.S. Government and can be used without additional permissions or fees. If you use these data in a publication, presentation, or other research product please use the following citation:
Zimmer, Scott N.; Houtman, Rachel M.; Leatherman, Lila S. T.; Housman, Ian W.; Shrestha, Abhinav; Shaw, John D.; Riley, Karin L. 2025. TreeMap 2020 CONUS: A tree-level model of the forests of the conterminous United States circa 2020. Updated 12 May 2026. Fort Collins, CO: Forest Service Research Data Archive. https://doi.org/10.2737/RDS-2025-0031

## Theme

* Not specified

## Geographic Coverage

## Geographic location - description

Forested areas in the conterminous United States.

## ISO Topic Category

* environment
* biota

## National Agricultural Library Thesaurus terms

Forestry, Wildland Management

## OMB Bureau Code

* 005:96 - Forest Service

## OMB Program Code

* 005:059 - Management Activities

## Pending citation

* No

## Public Access Level

* Public

## Identifier

RDS-2025-0031

## Usage metrics

views

downloads

citations

[Learn more about usage metrics](https://info.figshare.com/user-guide/usage-metrics-and-statistics/)



## Categories

* [Environmental sciences](/search?q=:category: "Environmental%20sciences")

## Keywords

[Forest & Plant Health](/search?q=:keyword: %22Forest%20%26%20Plant%20Health%22)[Timber](/search?q=:keyword: %22Timber%22)[Forest Inventory and Analysis](/search?q=:keyword: %22Forest%20Inventory%20and%20Analysis%22)[random forest](/search?q=:keyword: %22random%20forest%22)[Conservation](/search?q=:keyword: %22Conservation%22)[biota](/search?q=:keyword: %22biota%22)[Ecosystem services](/search?q=:keyword: %22Ecosystem%20services%22)[LANDFIRE](/search?q=:keyword: %22LANDFIRE%22)[Natural Resource Management & Use](/search?q=:keyword: %22Natural%20Resource%20Management%20%26%20Use%22)[Forest management](/search?q=:keyword: %22Forest%20management%22)[imputation](/search?q=:keyword: %22imputation%22)[tree list](/search?q=:keyword: %22tree%20list%22)[environment](/search?q=:keyword: %22environment%22)[Restoration](/search?q=:keyword: %22Restoration%22)[Wilderness](/search?q=:keyword: %22Wilderness%22)[Ecology, Ecosystems, & Environment](/search?q=:keyword: %22Ecology%2C%20Ecosystems%2C%20%26%20Environment%22)[Inventory, Monitoring, & Analysis](/search?q=:keyword: %22Inventory%2C%20Monitoring%2C%20%26%20Analysis%22)

## Licence

[![CC0](https://s3-eu-west-1.amazonaws.com/staticfigassets/images/CC-0.png)CC0](https://creativecommons.org/publicdomain/zero/1.0/)

## Export Metadata

Download
