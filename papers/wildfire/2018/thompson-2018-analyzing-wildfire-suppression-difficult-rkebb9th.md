---
title: Analyzing wildfire suppression difficulty in relation to protection demand
authors:
- Thompson, Matthew P
- Liu, Zhiwei
- Wei, Yu
- Caggiano, Michael D
year: '2018'
journal: Environmental Risks
doi: 10.5772/intechopen.76937
tags:
- fire risk
- fire suppression
- western united states
- wildfire
zotero_key: RKEBB9TH
item_type: journalArticle
url: https://doi.org/10.5772/intechopen.76937
source_url: 'unpaywall: https://www.intechopen.com/citation-pdf-url/61048'
fulltext_status: fulltext
synced: '2026-11-09'
---

# Analyzing wildfire suppression difficulty in relation to protection demand

## Abstract

In recent years, the field of wildfire risk management has seen dramatic advances. One notable improvement is in the realm of pre-fire suppression response planning, in particular the expansion from the assessment of risks posed by fire to the assessment of opportunities to effectively manage fire. Such proactive assessment and planning is critical to ensure that suppression response strategies and tactics are more likely to be safe and efficient. In this paper we will review the state-of-the-art in wildfire suppression planning, and illustrate application of advanced planning tools on a fire-prone landscape in Colorado, USA. Specifically we will use geospatial tools to quantify a composite index of suppression difficulty, and map this layer in relation to two key protection priorities that often drive suppression response decisions: built structures, and high value watersheds. We will discuss how our assessment results can inform planning and prioritization efforts, and offer suggestions for future research.

## Full text

**Chapter 3** 

# **Analyzing Wildfire Suppression Difficulty in Relation to Protection Demand** 

## Matthew P Thompson, Zhiwei Liu, Yu Wei and Michael D Caggiano 

Additional information is available at the end of the chapter 

http://dx.doi.org/10.5772/intechopen.76937 

### Abstract 

In recent years, the field of wildfire risk management has seen dramatic advances. One notable improvement is in the realm of pre-fire suppression response planning, in particular the expansion from the assessment of risks posed by fire to the assessment of opportunities to effectively manage fire. Such proactive assessment and planning is critical to ensure that suppression response strategies and tactics are more likely to be safe and efficient. In this paper we will review the state-of-the-art in wildfire suppression planning, and illustrate application of advanced planning tools on a fire-prone landscape in Colorado, USA. Specifically we will use geospatial tools to quantify a composite index of suppression difficulty, and map this layer in relation to two key protection priorities that often drive suppression response decisions: built structures, and high value watersheds. We will discuss how our assessment results can inform planning and prioritization efforts, and offer suggestions for future research. 

Keywords: decision support, GIS, hazard, modeling, planning, risk assessment, risk management 

## 1. Introduction 

Wildfire is an important natural process, and when it functions within acceptable parameters it can promote landscape heterogeneity, enhance forest resilience, and exhibit self-regulating characteristics [1, 2]. At the same time, wildfire can result in negative consequences, including public and firefighter fatalities, increased rates of respiratory disease, destruction of homes and timber, and impairment of critical infrastructure [3–5]. A particularly acute issue is the presence and expansion of human development in fire-prone areas [6, 7]. Increased attention to the fire 

> © 2018 The Author(s). Licensee IntechOpen. This chapter is distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/3.0), which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited. 

46 Environmental Risks 

problem coupled with improved technological capacity have spurred development of innovative mapping and assessment techniques to inform prioritization and mitigation efforts [8–10]. 

These efforts reflect broader trends of increasing sophistication of risk assessment and risk management within the global fire science and decision support communities [11–16]. One notable advancement relates to analysis of risk transmission (i.e., the analysis of ignition patterns, potential fire flow pathways, and simulated fire perimeters) in order to determine areas on the landscape that have a higher propensity to be a source of damaging fires [17–21]. Such analyses can inform demarcation of firesheds to support community wildfire planning, evaluation of comparative transmission rates across land designations and ownerships, and strategic identification of fuel treatment, ignition prevention, and suppression preparedness needs. 

A related advancement is in the realm of pre-suppression response planning, particularly the assessment of opportunities to effectively manage fire. Proactive assessment and planning can reduce time pressures and uncertainties, thereby helping ensure that suppression response strategies and tactics are more likely to be safe and efficient [22, 23]. Information from risk assessment can play a critical role in planning efforts and development of suppression objectives, for instance identifying areas where aggressive suppression would be warranted due to a high likelihood of fire transmission to developed areas, or where less aggressive suppression might be appropriate to achieve resource objectives [24, 25]. The operational relevance of presuppression planning is enhanced though consideration of factors that influence suppression effectiveness, notably the identification of areas of high suppression difficulty as well as their converse, areas of high likelihood for effective fire control [26–29]. Developing maps with such information can help fire managers forecast likely suppression resource needs, develop strategic courses of action and plans for mobilization of suppression resources, and inform tactical deployment decisions of where to send suppression resources. 

The research presented in this paper builds on the aforementioned body of work in the field of pre-suppression planning, with a focus on two key analytical products and planning tools: (1) the suppression difficulty index (SDI) [29]; and (2) a network of potential wildfire operational delineations (PODs) [24]. SDI, a raster layer, is a dimensionless metric that combines variables related to fire behavior (flame length, heat per unit area) with variables related to suppression operations (road and fuelbreak density, firefighter accessibility, fireline production, and cycle time for aerial resources). All else being equal, SDI increases with more extreme fire behavior. Similarly, SDI decreases as road density and firefighter accessibility increase, for example. For our purposes here, we use a modified version of SDI called the terrestrial SDI (tSDI) that excludes air support [27]. In the 2017 fire season in the USA, tSDI products were delivered to fire managers for real-time decision support on more than a dozen large fires. 

PODs are polygons whose boundaries are relevant to fire control operations, such as roads, trails, ridgetops, drainages, and fuel transitions. In effect, PODs can be thought of as fire management units, within which risks and other fire-relevant information can be summarized. The process of POD delineation can range from full automation in a GIS environment to being handdrawn by local managers using expert judgment assisted by maps of tSDI and potential control locations [26, 27]. The POD concept has been used to support strategic response planning [24], large fire response optimization [25], and fuel treatment optimization [30]. As with tSDI, POD 

Analyzing Wildfire Suppression Difficulty in Relation to Protection Demand 47 http://dx.doi.org/10.5772/intechopen.76937 

products were utilized during the 2017 fire season in the USA, specifically on the Tonto National Forest in Arizona to support large fire planning and management decisions. 

In summary, generating maps of tSDI and PODs can provide useful information for suppression response planning and decision making. tSDI can be used to identify locations on the landscape where potential flame lengths and heat intensities may make it unsafe for direct attack tactics, scouting, or ground transportation. This might be particularly important where rapid initial response using direct attack tactics is the predominant response to ignitions that could threaten the wildland-urban interface (WUI). Similarly, summarizing tSDI along administrative boundaries could facilitate identification of areas where suppression efforts may be more or less likely to inhibit fire transmission onto adjacent ownerships. tSDI can also facilitate identification of potential control locations and their aggregation into POD polygons. POD boundaries can help answer questions of how, where, and when to engage the fire along these predetermined potential control locations. In the context of risk transmission, the objective is to replace land ownership boundaries as artificial locations for suppression effort by identifying existing built and natural barriers that could slow fire spread or provide convenience for dispatching engines and personnel. 

Here we aim to demonstrate not only the value of these geospatial planning tools as standalone products, but also how stronger integration could lead to enhanced decision support. Specifically, we summarize tSDI values within each POD. This research direction is partly inspired by recent work in wildfire risk assessment that similarly integrates raster- and polygon-based modeling approaches [31]. Further, we quantify and map tSDI and POD layers in relation to two key protection priorities that often drive suppression response decisions: built structures and high value watersheds. Relative to a raster analysis, POD polygons provide a more logical and useful analysis unit to summarize protection demands, especially when incorporating information on suppression difficulty. We perform our case study analysis on a fire-prone landscape encompassing the Arapaho and Roosevelt National Forests in the Front Range of Colorado, USA. We discuss how our assessment results can inform planning and prioritization efforts, and offer suggestions for future research. 

## 2. Case study location 

We selected a case study landscape encompassing the Arapaho and Roosevelt National Forests, which is in north-central Colorado, USA. Figure 1 provides a map of the continental USA with the state of Colorado and the National Forests identified. Figure 2 further presents a topographic basemap and county boundary as reference for the study site. The study area includes the Front Range, which is located to the west of a heavily populated urban corridor stretching from Denver north to Fort Collins. The study area is 622,222 hectares in total, which includes 292,889 hectares from the Arapaho National Forest and 329,333 hectares from the Roosevelt National Forest [32]. Elevation of the study area ranges from mesas and high prairies at 1500 meters to mountain peaks exceeding 4250 m, with steep river canyons and dramatic changes in vegetation along the elevation gradient. 

48 Environmental Risks 



Figure 1. Location of the National Forests within Colorado, USA. 

Addington et al. [33] summarize important characteristics of the Front Range that influence forest conditions and fire management concerns. A dry climate (average annual precipitation �25–50 cm) combined with shallow soils that have relatively low moisture-holding capacity leads to low site quality and slow accumulation of fuels relative to other more productive pine forests in the western USA. The highly dissected topography creates variability in productivity and fuel loadings, which tended to promote a mixed-severity fire regime. However, a legacy of fire exclusion in the Front Range has led to changes in forest composition and density, which has in turn shifted the low-mid elevation ponderosa pine and dry mixed-conifer forests from a relatively frequent, low- and mixedseverity regime to a higher-severity regime. Hence increased concern in the region over the potential for large damaging wildfires that are resistant to control. In particular, wildfire damages to structures in the wildland-urban interface (WUI) and municipal watersheds are key concerns [7, 10, 21, 31, 34, 35]. Notably, the 2012 High Park Fire in the study area resulted in 35,323 hectares burned, at least 259 homes destroyed, one casualty, and increased water treatment costs [5, 36]. Other high loss fire events from the region include the 2002 Hayman Fire (132 homes destroyed; 6 fatalities; human-caused), the 2010 Fourmile Canyon Fire (168 homes destroyed; human-caused), the 2012 Lower North Fork Fire (16 homes destroyed; 3 fatalities; human-caused), the 2012 Waldo Canyon Fire (346 homes destroyed; human-caused), and the 2013 Black Forest Fire (464 homes destroyed, 2 fatalities; human-caused) [21]. 

Here we opt to focus on National Forest lands to simplify our illustration. This is not meant to diminish the importance of other federal, state, and local land and fire management agencies operating within the case study landscape (e.g., Rocky Mountain National Park). Rather, it 

Analyzing Wildfire Suppression Difficulty in Relation to Protection Demand 49 http://dx.doi.org/10.5772/intechopen.76937 



Figure 2. Study site including the Arapaho and Roosevelt National Forests. 

50 Environmental Risks 

allows us to focus particular attention on the problem of one-way risk transmission across ownership boundaries and its relevance to suppression difficulty and protection priority. Further, as of this writing, the Forests and local partners are actively involved in landscapescale prioritization and planning efforts incorporating tSDI and POD products. 

## 3. Materials and methods 

### 3.1. Analysis framework 

Table 1 presents a generalized framework for the types of variables included our analysis. The tSDI variables are calculated for every raster cell on the landscape, whereas other variables are summarized at the polygon-level for each POD. We describe the primary analytical steps in the following sub-sections. 

### 3.2. Generate POD network 

We generated PODs within our study area using GIS data and analysis techniques described in [25]. The boundaries between adjacent PODs are either major roads, streams, or ridge tops. Our assumption is that fire management activities such as enhancing natural fire breaks, constructing fireline, or conducting burn out operations could be performed along these geographic features. The geospatial layers for stream and ridge (catchment boundary) locations are acquired from the U.S. EPA and U.S. Geological Survey’s NHDPlusV2 dataset, and the road transportation layers are acquired locally from the US Forest Service. Rather than identifying PODs for every hectare on the landscape, we limited our consideration to areas within and proximal to National Forest boundaries, and attempted to maintain a fairly contiguous analysis landscape. 

The desired size distribution of PODs will vary with the scale of the planning application [22]. The process we use intentionally creates small PODs, relative to PODs created elsewhere for 

|Variable|Definition|
|---|---|
|Raster-level summaries||
|tSDI|Terrestrial suppression difficulty index|
|SDI_AR|Ratio-scale index of relative tSDI and area ratios for predefined analysis units|
|POD-level summaries||
|mSDI|Mean tSDI of all raster cells in POD|
|F2F|Forests to Faucets Surface Drinking Water Importance Score|
|dWUI|Areal density of structures in the WUI|
|PP_F2F|Protection priority for F2F|
|PP_dWUI|Protection priority for dWUI|



Table 1. Primary variables in analysis. 

Analyzing Wildfire Suppression Difficulty in Relation to Protection Demand 51 http://dx.doi.org/10.5772/intechopen.76937 

the purposes of developing broad-scale strategic wildfire response zones [24]. This allows for identification of specific locations on the landscape that are high priority for protection, and facilitates targeted scheduling of activities like hazardous fuel reductions projects. The smallscale POD network could also facilitate optimal aggregation into larger PODs that are relatively homogenous with respect to suppression difficulty and protection demand. 

### 3.3. Calculate tSDI 

We used an automated Python script to calculate the tSDI across the case study landscape. The script requires raster inputs including fuel model, flame length, heat per unit area, roads, trails, digital elevation model, slope, aspect. tSDI is calculated for each raster cell based on the equations originally developed by [29] and later modified by [27]. SDI is a sum of six sub-indices: the energy behavior sub-index (Ice, Eq. 1, a function of flame length (FL) and heat per unit area (HUA)), the accessibility sub-index (Ia), the mobility sub-index (Im), the penetrability sub-index (Ip), aerial resources sub-index (Iar) and fireline opening subindex (Ic) (Eq. 2). The first five sub-indices each has a value that ranges from 1 to 10. The last sub-index has a value between 1 and 20. Ai is the area of each fuel model and At is the size of total study area managed within each cell or pixel. In our case, tSDI values were calculated at a 30 � 30 m resolution, which is identical to the resolution of the fuel models, so in practice the area adjustment ratio in Eq. 1 is always equal to one. Further, since we did not consider aerial resources, the value of Iar is set to 0, and we quantify tSDI accordingly (Eq. 3). Based on these scaling coefficients, the final SDI values can range from 0 to 1.67 with all sub-indices included, and the final tSDI values can range from 0 to 2.5 with the aerial sub-index excluded. 



<!-- Start of picture text -->
2 � FLi � HUAi<br>Ice ¼ X � ðAi=AtÞ (1)<br>� � FLi þ HUAi � �<br>P ðIceÞ<br>SDI ¼ (2)<br>" P � Ia þ Im þ Ip þ Iar þ Ic � #<br>P ðIceÞ<br>tSDI ¼ (3)<br>" P � Ia þ Im þ Ip þ Ic � #<br><!-- End of picture text -->

Two critical inputs for calculating tSDI are fuel models and modeled fire behavior metrics. Our primary source for data on fuel models was LANDFIRE 2014 [37, 38]. We then updated these data to account for treatments and other disturbances that occurred on the landscape in the intervening years up to 2016. We used two sets of treatment mosaics to reflect the changing of fuel treatments within the study area: treated areas identified through the Front Range Round Table 2016 Interagency Fuel Treatment Database, and the USDA Forest Service’s Natural Resource Manager Forest Activity Tracking System. We then distinguished the effects of different fuel treatment types (e.g., mastication, surface fuel treatment, prescribed fire, thin from below) and used rulesets to update the fuel models after corresponding treatment. To model fire behavior we used the FlamMap fire modeling system [39], using 90th percentile 

52 Environmental Risks 

weather conditions for fuel moisture conditions and wind speed/direction, drawn from the Redfeather Remote Automated Weather Station. 

Finally, we mapped tSDI at four spatial scales of decreasing size, hereafter analysis units (Table 2). The rationale for scaling down tSDI values to within National Forest boundaries is to focus on suppression difficulty in relation to risk transmission and prospects for preventing fire from spreading onto adjacent lands. To compare tSDI values across predefined analysis units it was necessary to adjust by the respective area of these units. We defined ratio-scale indices (SDI_AR, Table 1) that relate ratios of total tSDI to ratios of total area across analysis units. Eq. 4 presents an example calculation for the F and P analysis units, where AF and AP are the area of each analysis unit. These ratios are always calculated using the larger analysis unit as the denominator. Where the index is equal to 1, it suggests that the difference in suppression difficulty across analysis units is directly proportional to the difference in area. Where the index is greater than 1, it suggests that suppression difficulty is disproportionately higher in the smaller analysis unit, and vice versa. Using these four analysis units, we arrive at six possible pairwise comparisons (F_P, B5_P, B2_P, B5_F, B2_F, and B2_B5). 



<!-- Start of picture text -->
ðP tSDIF= P tSDIPÞ<br>SDI_ARF�P ¼ (4)<br>ðAF=APÞ<br><!-- End of picture text -->

### 3.4. Quantify protection demand and protection priority 

To quantify protection demand we use variables related to the WUI and to municipal watersheds (Table 1). For the WUI layer, we used high resolution built structure data derived from [10]. We summarized total count of structures by POD, and then divided by total POD area to derive an areal density measure for each POD (dWUI, Table 1). For the watersheds layer, we used data obtained from the Forest Services’s Forests to Faucets (F2F, Table 1) project [40]. Specifically we used a layer that assigns surface drinking water relative importance scores (0–100) to each 12-digit hydrologic unit code catchment. More information on this layer and its use in risk assessments can be found in [40, 41]. The data layer we use assigns each catchment a score on a range, and we use the midpoint of that range to assign each POD a unique surface drinking water importance score (e.g., 75 from 70 to 80). In cases where a POD overlapped multiple catchments, we used the importance score from the catchment that comprised the majority of POD area (across the case study landscape, on average the majority catchment selected accounted for >99% of total POD area). 

|Analysis Unit|Definition|
|---|---|
|P|Area within entire POD network|
|F|Area within National Forest boundaries|
|B5|Area within 5-km buffer internal to National Forest boundaries|
|B2|Area within 2-km buffer internal to National Forest boundaries|



Table 2. Analysis units for analyzing tSDI ratios, sorted in order of decreasing size. 

Analyzing Wildfire Suppression Difficulty in Relation to Protection Demand 53 http://dx.doi.org/10.5772/intechopen.76937 

To quantify protection priority, we merged tSDI results with protection demand layers. We created individual priority indices for F2F and dWUI, which are calculated simply as the product of each POD’s mSDI and its protection demand level. Eq. 5 presents an example of protection priority calculated for F2F. 



<!-- Start of picture text -->
PP_F2F ¼ mSDI∗F2F (5)<br><!-- End of picture text -->

To identify “high” priority PODs, we sorted PODs on the basis of protection priority and selected only those with protection priority levels in the top 10th percentile for F2F and dWUI. We further identified which PODs, if any, were included in the top 10th percentile for both F2F and dWUI. These PODs we identify as “very high” priority. 

## 4. Results 

### 4.1. POD network 

Figure 3 displays the POD network in relation to boundaries of the National Forests as well as the Forest to Faucets catchments. In total we identified 8772 PODs for further analysis, which ranged in size from <1 to 2532 hectares. The mean POD size was 125 hectares, and the median POD size was 63 hectares. For operational purposes users would likely make post-hoc adjustments to the POD network created through automation, for example eliminating very small PODs by incorporating them into adjacent PODs. 

There are a few noteworthy observations. First, POD boundaries rarely align with Forest boundaries, but often align with catchment boundaries. Second, PODs are much smaller than catchments, such that each catchment may contain multiple PODs. This reflects our analytical process that uses smaller catchment boundaries as well as the presence of roads on the landscape. The full extent of this POD network corresponds to analysis unit P (Table 2), and is used for summarizing results in the remainder of this paper. 

### 4.2. tSDI results 

Figure 4 presents tSDI values mapped to the full extent of the POD network as depicted in Figure 3. Some patterns are immediately evident. High elevation areas along the Continental Divide have zero or near-zero tSDI values due to lack of burnable vegetation. The scar from the High Park Fire in the northeast portion of the landscape similarly has very low tSDI values. This appears as a break between an otherwise largely uninterrupted corridor of high tSDI values running along the eastern edge of the analysis area. Isolated patches of high tSDI values elsewhere appear at least partially driven by steep slopes, sometimes in remote or wilderness areas with low road density (see Figure 2). 

The most notable aspect of Figure 4 is the concentration of high tSDI values located on the eastern side of the analysis area. This simultaneously highlights the importance and challenge of fire management in these areas, where aggressive suppression would likely be warranted in 

54 Environmental Risks 



Figure 3. Derived POD network, overlaid with National Forest boundaries and Forests to Faucets catchment boundaries. 

Analyzing Wildfire Suppression Difficulty in Relation to Protection Demand 55 http://dx.doi.org/10.5772/intechopen.76937 



Figure 4. tSDI values mapped to the extent of the POD network (Figure 3). 

56 Environmental Risks 

order to avoid the spread of fire onto adjacent lands where fires could threaten the WUI and other infrastructure. The vast majority of cells on the landscape have low tSDI values: 46% are <0.1, 76% are <0.2, and 89% are <0.5. By contrast, only 4% have values >1. 

Table 3 presents results for SDI_AR indices across all six analysis unit pairwise comparisons. All indices relating to the analysis unit P are >1, which reflects the spatial distribution of low tSDI values outside of National Forest boundaries (Figure 4). Buffers B5 and B2 are effectively proportional, but all have indices >1 with respect to units F and P. Findings suggest therefore that suppression would be more challenging proximal to Forest boundaries, such that the probability of failing to prevent risk transmission could be substantial. Notably, these ratios would be even higher if we limited our buffers to the eastern and southern edges of the POD network. 

### 4.3. Protection demand and protection priority 

Figure 5 displays POD-level summarization of F2F and dWUI protection demand. For F2F, importance scores ranged from 25 to 95, with a mean of 64.33 and a median of 65. For dWUI, 

|Analysis units|tSDI ratio|Area ratio|SDI-AR|
|---|---|---|---|
|F_P|0.66|0.64|1.04|
|B5_P|0.44|0.40|1.11|
|B2_P|0.22|0.20|1.12|
|B5_F|0.67|0.63|1.07|
|B2_F|0.33|0.31|1.07|
|B2_B5|0.50|0.50|1.00|



Table 3. Ratio-scale indices comparing area-adjusted tSDI values within and across various analysis units. 



Figure 5. POD-level protection demand for F2F and dWUI. 

Analyzing Wildfire Suppression Difficulty in Relation to Protection Demand 57 http://dx.doi.org/10.5772/intechopen.76937 

structure density values ranged from 0 to 9.87, with a mean of 0.12 and a median of 0. A total of 5447 PODs contained zero structures, with a total of 62,359 structures contained within the remaining 3325 PODs. For F2F, the importance values differ sharply on the western and eastern sides of the Continental Divide, with the highest values generally located in the southeastern portion of the POD network. For dWUI, the highest values similarly occur in the eastern portions of the POD network, although generally further to the east than the highest F2F values. 

Figure 6 displays a three-dimensional scatterplot of mSDI, F2F, and dWUI, along with twodimensional slices for pairwise comparisons (dWUI vs. mSDI; dWUI vs. F2F; F2F vs. mSDI). The preponderance of low mSDI values is evident in the 3D scatterplot, with a corresponding lack of points clustered in the high-mSDI, high-F2F, and high-dWUI space. In terms of pairwise comparisons, higher dWUI values tend to be align with lower mSDI values, which could in part reflect higher road densities and shallower slopes commonly associated with higher density human development. There is slight positive association with dWUI and F2F, particularly noticeable for the surface water importance scores of 85, which suggests opportunity to readily identify some PODs as very high protection demand. Referring back to Figure 5, some of these PODs are located near the community of Estes Park in the central-eastern 



Figure 6. Three-dimensional scatterplot of mSDI, dWUI, and F2F, along with two-dimensional slices for pairwise comparisons. 

58 Environmental Risks 



Figure 7. POD-level protection priority for F2F, dWUI, and both. 

Analyzing Wildfire Suppression Difficulty in Relation to Protection Demand 59 http://dx.doi.org/10.5772/intechopen.76937 

portion of the map. Lastly, F2F and mSDI values tend to show little relationship, apart from lower mSDI values tending to align with lower F2F values. 

Figure 7 displays the PODs identified as “high” and “very high” protection priority. In total 1524 PODs are identified, 646 each that correspond to the top 10th percentile for either PP_F2F or PP_dWUI (Table 1, Eq. 5), and 232 of which correspond to PODs in the top 10th percentile for both. To reiterate, the latter category is what we deem to be “very high” protection priority. Not surprisingly given results in Figures 4 and 5, the greatest levels of protection priority run along the eastern flank of the POD network, many of which are within National Forest boundaries. The joint concentration of high suppression difficulty and high protection demand highlight this area as for preventative risk management activities. 

## 5. Discussion 

Two primary innovations we introduce here are the summarization of tSDI within various analytical units to determine differences in area-adjusted suppression difficulty, and the summarization of tSDI within PODs to determine protection priorities. Notably, we attempted to expand the concept of risk transmission to include opportunities to safely and effectively restrict fire spread across ownership boundaries. The incorporation of suppression difficulty and control opportunities has, to date, been largely absent from the literature on wildfire risk transmission. What we presented here ideally informs decisions related to the need for suppression where protection demand is high, as well as decisions related to the need for suppression where the potential for risk transmission is high. 

There are a number of foreseeable near- and long-term extensions to this work. Perhaps most immediate, the analysis could be extended across multiple ownerships to create a common operating picture for co-management of risk. Models of fire spread and containment could be updated to account for suppression difficulty, and could be used to game out various scenarios and alternative response strategies [42]. Similarly, models designed to optimize initial attack response could be updated to account for variable suppression resource needs as a function of tSDI [43]. Calculating tSDI values under different weather scenarios could be informative for gaming out how suppression opportunities change with conditions, and could further serve as the basis for prioritization of fuel treatment investments designed to enhance suppression effectiveness [44]. Analysis of tSDI values along POD boundaries could identify potential weakness in the POD network, which could also help inform prioritization of fuel treatments. 

Incorporating structure and watershed susceptibility to fire through more rigorous fire effects analysis, as well as incorporating fire likelihood, would likely allow for targeted identification of protection priority [41]. It is not necessarily the case that higher F2F importance weights imply higher potential for post-fire erosion, for example, or that higher mSDI values imply higher intensity fire leading to greater damage. Opting for more refined risk assessment of course comes with greater investment of time and resources, a tradeoff which must be evaluated in light of the marginal value that is added for decision processes [13]. This point encapsulates a common aspect of designing and delivering decision support, which is that modeling frameworks do not necessarily need to be complicated to demonstrate potential 

60 Environmental Risks 

utility, and further that not every application requires a complicated solution. Lastly, the tSDI layers, along with the basic concept of suppression difficulty, could be broadened to include factors such as safety zones, egress routes, and the impacts of other disturbances on fire behavior and resistance to control [45, 46]. 

## 6. Conclusion 

The work presented in this chapter represents incremental improvement in wildfire decision support by integrating information on suppression difficulty with information on demand for protection of important fire-susceptible assets. By summarizing tSDI within PODs, and further by summarizing area-adjusted tSDI values in different analysis units, we are able to pinpoint areas of high concern in relation to suppression opportunity and risk transmission. We identified a case study landscape where a high density of human development in areas with increased fire hazard presents significant forest and fire management challenges. More importantly, we were able to work with local managers to assimilate this information into ongoing assessment and planning processes. As of this writing, the layers we developed on tSDI, dWUI, and F2F are being incorporated into a geodatabase that will be delivered to the Arapaho and Roosevelt National Forests to facilitate landscape prioritization and support real-time fire incident response. 

In summary, we developed techniques to study the opportunity and viability of conducting fire suppression to manage fire risks at high priority locations, and to facilitate targeted identification of those high priority areas. Results can help fire managers understand how and where fire management activities could be planned and implemented to mitigate fire threats. In this chapter, we demonstrated not only proof-of-concept, but also results that delivered actionable information to local fire managers. We aim to continue to improve techniques and relevance of decision support through additional science-management partnerships, and hope this chapter inspires other fire scientists to do the same. 

## Acknowledgements 

Christopher D O’Connor shared a Python script to calculate tSDI and provided rulesets to update fuel models. Alex Masarie helped with data visualization. This research was partially funded by the Colorado Agriculture Experimental Station project COL0050 and by the 14-JV11221636-029 project between the USDA Forest Service Rocky Mountain Research Station and Colorado State University. The National Fire Decision Support Center also supported this effort. 

## Conflict of interest 

The authors declare no conflict of interest. 

Analyzing Wildfire Suppression Difficulty in Relation to Protection Demand 61 http://dx.doi.org/10.5772/intechopen.76937 

## Author details 

Matthew P Thompson<sup>1</sup> *, Zhiwei Liu<sup>2</sup> , Yu Wei<sup>2</sup> and Michael D Caggiano<sup>2</sup> 

- *Address all correspondence to: mpthompson02@fs.fed.us 

- 1 United States Department of Agriculture Forest Service, Fort Collins, CO, USA 

- 2 Colorado State University, Fort Collins, CO, USA 

## References 

- [1] Boisramé G, Thompson S, Collins B, Stephens S. Managed wildfire effects on forest resilience and water in the Sierra Nevada. Ecosystems. 2017;20(4):717-732 

- [2] Parks SA, Holsinger LM, Miller C, Nelson CR. Wildland fire as a self-regulating mechanism: The role of previous burns and weather in limiting fire progression. Ecological Applications. 2015;25(6):1478-1492 

- [3] Gómez-González S, Ojeda F, Fernandes PM. Portugal and Chile: Longing for sustainable forestry while rising from the ashes. Environmental Science & Policy. 2018;81:104-107 

- [4] Liu JC, Pereira G, Uhl SA, Bravo MA, Bell ML. A systematic review of the physical health impacts from non-occupational exposure to wildfire smoke. Environmental Research. 2015;136:120-132 

- [5] Writer JH, Hohner A, Oropeza J, Schmidt A, Cawley KM, Rosario-Ortiz FL. Water treatment implications after the high Park wildfire, Colorado. Journal of American Water Works Association. 2014;106(4):E189-E199 

- [6] Gill AM, Stephens SL. Scientific and social challenges for the management of fire-prone wildland–urban interfaces. Environmental Research Letters. 2009;4(3):034014 

- [7] Liu Z, Wimberly MC, Lamsal A, Sohl TL, Hawbaker TJ. Climate change and wildfire risk in an expanding wildland–urban interface: A case study from the Colorado Front Range Corridor. Landscape Ecology. 2015;30(10):1943-1957 

- [8] Bar-Massada A, Stewart SI, Hammer RB, Mockrin MH, Radeloff VC. Using structure locations as a basis for mapping the wildland urban interface. Journal of Environmental Management. 2013;128:540-547 

- [9] Scott JH, Thompson MP, Gilbertson-Day JW. Exploring how alternative mapping approaches influence fireshed assessment and human community exposure to wildfire. GeoJournal. 2017;82(1):201-215 

- [10] Caggiano MD, Tinkham WT, Hoffman C, Cheng AS, Hawbaker TJ. High resolution mapping of development in the wildland-urban interface using object based image extraction. Heliyon. 2016;2(10):e00174 

62 Environmental Risks 

- [11] Pacheco AP, Claro J, Fernandes PM, de Neufville R, Oliveira TM, Borges JG, Rodrigues JC. Cohesive fire management within an uncertain environment: A review of risk handling and decision support systems. Forest Ecology and Management. 2015;347:1-17 

- [12] Calkin DE, Cohen JD, Finney MA, Thompson MP. How risk management can prevent future wildfire disasters in the wildland-urban interface. Proceedings of the National Academy of Sciences. 2014;111(2):746-751 

- [13] Thompson MP, Haas JR, Gilbertson-Day JW, Scott JH, Langowski P, Bowne E, Calkin DE. Development and application of a geospatial wildfire exposure and risk calculation tool. Environmental Modelling & Software. 2015;63:61-72 

- [14] Papakosta P, Xanthopoulos G, Straub D. Probabilistic prediction of wildfire economic losses to housing in Cyprus using Bayesian network analysis. International Journal of Wildland Fire. 2017;26(1):10-23 

- [15] Chuvieco E, Aguado I, Jurdao S, Pettinari ML, Yebra M, Salas J, Hantson S, de la Riva J, Ibarra P, Rodrigues M, Echeverría M. Integrating geospatial information into fire risk assessment. International Journal of Wildland Fire. 2014;23(5):606-619 

- [16] Castillo ME, Molina JR, Silva FR, García-Chevesich P, Garfias R. A system to evaluate fire impacts from simulated fire behavior in Mediterranean areas of Central Chile. Science of the Total Environment. 2017;579:1410-1418 

- [17] Alcasena FJ, Salis M, Ager AA, Castell R, Vega-García C. Assessing wildland fire risk transmission to communities in northern Spain. Forests. 2017;8(2):30 

- [18] Price O, Borah R, Bradstock R, Penman T. An empirical wildfire risk analysis: The probability of a fire spreading to the urban interface in Sydney, Australia. International Journal of Wildland Fire. 2015;24(5):597-606 

- [19] Scott JH, Thompson MP, Gilbertson-Day JW. Examining alternative fuel management strategies and the relative contribution of National Forest System land to wildfire risk to adjacent homes—A pilot assessment on the Sierra National Forest, California, USA. Forest Ecology and Management. 2016;362:29-37 

- [20] Ager AA, Day MA, Finney MA, Vance-Borland K, Vaillant NM. Analyzing the transmission of wildfire exposure on a fire-prone landscape in Oregon, USA. Forest Ecology and Management. 2014;334:377-390 

- [21] Haas JR, Calkin DE, Thompson MP. Wildfire risk transmission in the Colorado Front Range, USA. Risk Analysis. 2015;35(2):226-240 

- [22] Dunn CJ, Thompson MP, Calkin DE. A framework for developing safe and effective largefire response in a new fire management paradigm. Forest Ecology and Management. 2017; 404:184-196 

- [23] Thompson MP, MacGregor DG, Calkin DE. Risk management: Core principles and practices, and their relevance to Wildland Fire. USDA Forest Service, Rocky Mountain 

Analyzing Wildfire Suppression Difficulty in Relation to Protection Demand 63 http://dx.doi.org/10.5772/intechopen.76937 

Research Station. In: General Technical Report: RMRS-GTR-350; Fort Collins, CO, USA; 2016 

- [24] Thompson MP, Bowden P, Brough A, Scott JH, Gilbertson-Day J, Taylor A, Anderson J, Haas JR. Application of wildfire risk assessment results to wildfire response planning in the southern Sierra Nevada, California, USA. Forests. 2016;7(3):64 

- [25] Wei Y, Thompson M, Haas JR, Dillon GK, O'Connor CD. Spatial optimization of operationally relevant large fire confine and point protection strategies: Model development and test cases. Canadian Journal of Forest Research. 2018;48(999):1-14 

- [26] O’Connor CD, Calkin DE, Thompson MP. An empirical machine learning method for predicting potential fire control locations for pre-fire planning and operational fire management. International Journal of Wildland Fire. 2017;26(7):587-597 

- [27] O’Connor CD, Thompson MP, Rodríguez y Silva F. Getting ahead of the wildfire problem: Quantifying and mapping management challenges and opportunities. Geosciences. 2016; 6(3):35 

- [28] Rodríguez y Silva F, González-Cabán A. Contribution of suppression difficulty and lessons learned in forecasting fire suppression operations productivity: A methodological approach. Journal of Forest Economics. 2016;25:149-159 

- [29] Rodríguez y Silva F, Martínez JRM, González-Cabán A. A methodology for determining operational priorities for prevention and suppression of wildland fires. International Journal of Wildland Fire. 2014;23(4):544-554 

- [30] Thompson MP, Riley KL, Loeffler D, Haas JR. Modeling fuel treatment leverage: Encounter rates, risk reduction, and suppression cost impacts. Forests. 2017;8(12):469 

- [31] Thompson MP, Gilbertson-Day JW, Scott JH. Integrating pixel-and polygon-based approaches to wildfire risk assessment: Application to a high-value watershed on the Pike and San Isabel National Forests, Colorado, USA. Environmental Modeling and Assessment. 2016;21(1):1-15 

- [32] USFS. NFS Acreage by State, Congressional District and County. 2007. Available from: https://www.fs.fed.us/land/staff/lar/2007/TABLE_6.htm 

- [33] Addington RN, Aplet GH, Battaglia MA, Briggs JS, Brown PM, Cheng AS, Dickinson Y, et al. Principles and practices for the restoration of ponderosa pine and dry mixed-conifer forests of the Colorado front range. Vol. 121, No: RMRS-GTR-373. Fort Collins, CO: US Department of Agriculture, Forest Service, Rocky Mountain Research Station; 2018. p. 373 

- [34] Warziniack T, Thompson M. Wildfire risk and optimal investments in watershed protection. Western Economics Forum. 2013;12(2):19-28 

- [35] Jones KW, Cannon JB, Saavedra FA, Kampf SK, Addington RN, Cheng AS, MacDonald LH, Wilson C, Wolk B. Return on investment from fuel treatments to reduce severe wildfire and erosion in a watershed investment program in Colorado. Journal of Environmental Management. 2017;198:66-77 

64 Environmental Risks 

- [36] High Park Burned Area Emergency Response (BAER) Report. 2012. Available from: https://www.nrcs.usda.gov/Internet/FSE_DOCUMENTS/nrcs144p2_061214.pdf 

- [37] Ryan KC, Opperman TS. LANDFIRE—A national vegetation/fuels data base for use in fuels treatment, restoration, and suppression planning. Forest Ecology and Management. 2013;294:208-216 

- [38] LANDFIRE. 2014. Available from: https://www.landfire.gov/lf_140.php 

- [39] Finney MA. An overview of FlamMap fire modeling capabilities. In: Fuels Management— How to Measure Success: Conference Proceedings; Fort Collins, CO: USDA Forest Service, Rocky Mountain Research Station; March, 2006. pp. 28-30 

- [40] USDA Forest Service. Forests to Faucets. Available online: http://www.fs.fed.us/ecosystemservices/FS_Efforts/forests2faucets.shtml 

- [41] Thompson MP, Scott J, Langowski PG, Gilbertson-Day JW, Haas JR, Bowne EM. Assessing watershed-wildfire risks on national forest system lands in the rocky mountain region of the United States. Water. 2013;5(3):945-971 

- [42] Riley KL, Thompson MP, Scott JH, Gilbertson-Day JW. A model-based framework to evaluate alternative wildfire suppression strategies. Resources. 2018;7(1):4 

- [43] Wei Y, Bevers M, Belval E, Bird B. A chance-constrained programming model to allocate wildfire initial attack resources for a fire season. Forest Science. 2015;61(2):278-288 

- [44] Wei Y. Optimize landscape fuel treatment locations to create control opportunities for future fires. Canadian Journal of Forest Research. 2012;42(6):1002-1014 

- [45] Dennison PE, Fryer GK, Cova TJ. Identification of firefighter safety zones using lidar. Environmental Modelling & Software. 2014;59:91-97 

- [46] Page WG, Alexander ME, Jenkins MJ. Wildfire’s resistance to control in mountain pine beetle-attacked lodgepole pine forests. The Forestry Chronicle. 2013;89(6):783-794 
