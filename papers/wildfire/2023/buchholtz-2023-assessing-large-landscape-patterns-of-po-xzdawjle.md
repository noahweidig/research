---
title: Assessing large landscape patterns of potential fire connectivity using circuit methods
authors:
- Buchholtz, Erin K.
- Kreitler, Jason
- Shinneman, Douglas J.
- Crist, Michele
- Heinrichs, Julie
year: '2023'
journal: Landscape Ecology
doi: 10.1007/s10980-022-01581-y
tags:
- connectivity
- fuel breaks
- fuel treatments
- sagebrush
- wildfire
zotero_key: XZDAWJLE
item_type: journalArticle
url: https://doi.org/10.1007/s10980-022-01581-y
source_url: 'unpaywall: https://link.springer.com/content/pdf/10.1007/s10980-022-01581-y.pdf'
fulltext_status: fulltext
synced: '2026-11-06'
---

# Assessing large landscape patterns of potential fire connectivity using circuit methods

## Abstract

Minimizing negative impacts of wildfire is a major societal objective in fire-prone landscapes. Models of fire connectivity can aid in understanding and managing wildfires by analyzing potential fire spread and conductance patterns. We define ‘fire connectivity’ as the landscape’s capacity to facilitate fire transmission from one point on the landscape to another.

## Full text

Landsc Ecol (2023) 38:1663–1676 https://doi.org/10.1007/s10980-022-01581-y 

RESEARCH ARTICLE 



# **Assessing large landscape patterns of potential fire connectivity using circuit methods** 

**Erin K. Buchholtz · Jason Kreitler · Douglas J. Shinneman · Michele Crist · Julie Heinrichs** 

Received: 18 March 2022 / Accepted: 16 December 2022 / Published online: 7 April 2023 

© This Agreement shall be governed by the federal laws of the United States of America without regards to any conflict of law provisions. If no federal law applies, then the laws of the State of New York without regard to any conflict of law provisions shall govern. The parties submit to the exclusive jurisdiction of the federal courts located in the State of New York 2023 

## **Abstract** 

_Context_ Minimizing negative impacts of wildfire is a major societal objective in fire-prone landscapes. Models of fire connectivity can aid in understanding and managing wildfires by analyzing potential fire spread and conductance patterns. We define ‘fire connectivity’ as the landscape’s capacity to facilitate fire transmission from one point on the landscape to another. 

_Objectives_ Our objective was to develop an approach for modeling fire connectivity patterns representing potential fire spread and relative flow across a broad landscape extent, particularly in the management-relevant context of fuel breaks. 

**Supplementary Information** The online version contains supplementary material available at https:// doi. org/ 10. 1007/ s10980- 022- 01581-y. 

_Methods_ We applied an omnidirectional circuit theory algorithm to model fire connectivity in the Great Basin of the western United States. We used predicted rates of fire spread to approximate conductance and calculated current densities to identify connections among areas with high spread rates. We compared existing and planned fuel breaks with fire connectivity patterns. 

_Results_ Fire connectivity and relative flow outputs were characterized by spatial heterogeneity in the landscape’s capacity to transmit fire. We found that existing fuel break networks were denser in areas with relatively diffuse and impeded flow patterns, rather than in locations with channelized flow. _Conclusions_ This approach could be paired with traditional fire behavior and risk analyses to better understand wildfire spread as well as direct strategic 

E. K. Buchholtz (*) 

U.S. Geological Survey, Fort Collins Science Center, Fort Collins, CO, USA e-mail: ebuchholtz@usgs.gov 

### D. J. Shinneman 

U.S. Geological Survey, Forest and Rangeland Ecosystem Science Center, Boise, ID, USA 

### M. Crist 

_Present Address:_ 

E. K. Buchholtz 

U.S. Geological Survey, South Carolina Cooperative Fish and Wildlife Research Unit, Clemson, USA 

J. Kreitler 

U.S. Geological Survey, Western Geographic Science Center, Boise, ID, USA 

Bureau of Land Management Fuels Management and Fire Planning, Boise, ID, USA 

### J. Heinrichs 

Natural Resource Ecology Laboratory, Colorado State University, in Cooperation with the U.S. Geological Survey, Fort Collins Science Center, Fort Collins, CO, USA 

Vol.: (0123456789) 1 3 

1664 

Landsc Ecol (2023) 38:1663–1676 

placement of individual fuel breaks within larger networks to constrain fire spread. Thus, our findings may offer local- to landscape-level support for management actions that aim to disrupt fire spread and mitigate the costs of fire on the landscape. 

**Keywords** Wildfire · Fire connectivity · Circuit theory · Fuels management · Sagebrush · Fuel breaks 

## **Introduction** 

Minimizing negative impacts of wildfire is a major societal objective in fire-prone landscapes around the globe (Gill et al. 2013). Due to a range of factors including climate change and a history of fire suppression, wildfire activity is increasing in many ecosystems and may out-pace current efforts to constrain wildfire and restore burned landscapes (Calkin et al. 2014; Dennison et al. 2014; Balch et al. 2017; Keyser and Westerling 2017; Fusco et al. 2019). For example, in the western United States, burned area from large wildfires (> 405 ha) averaged more than 1.25 million ha per year between 2010–2019 and 2.5 million ha burned in 2020 (Higuera and Abatzoglou 2020). The likelihood of very large wildfires (> 20,234 ha) is predicted to increase under changing climate conditions (Stavros et al. 2014). Wildfires spread across the landscape, responding to a suite of factors including combustible vegetation, weather, and topography, thus designing fire management strategies at the scale of a large landscape or extensive ecosystem can be a considerable challenge. Models can be used to better understand how fire spreads, how landscape characteristics and vegetative fuels facilitate or impede spread, and the ways in which pre-emptive fire management can limit fire-related losses. 

Fire behavior models rely on physical (Sullivan 2009a), empirical (Sullivan 2009b), and mathematical (Sullivan 2009c) concepts and data to simulate the process of fire spread. The specific goals, complexity, and outputs of these fire behavior models vary widely. For example, coupled atmosphere-fire models can be used to simulate large fires and their spread in real time with the goal of supporting active firefighting and associated mitigation actions (e.g., WFS-SFIRE; Kochanski et al. 2013). Other fire simulation models characterize and summarize the potential risk and behavior of fires, and this information used in planning management actions (e.g., fuels reduction) and hazards/risk planning. 

Simulations of many possible individual fires can be used to calculate pixel-based probable rates of spread, conditional flame length estimates, and burn probability statistics (e.g., FlamMap; Finney 2006; Finney et al. 2011). These models provide insight into the interactions among fuels, weather or climatic conditions, and fire outcomes. However, it is challenging to conduct fire behavior simulations over large landscapes due to computational constraints. Further, while rate-of-spread (ROS) maps describe expected properties of fires, connectivity outputs describe the landscape and the spatial arrangement of pixels with similar properties that could facilitate contiguous fire spread. The connectivity outputs are therefore useful for visualizing the linkages among those areas with high rates of spread based on the density of potential connections. 

Because fire is a contagious process, connectivity models provide a useful lens to extend and complement existing fire behavior models (Rodriguez Gonzalez et al. 2008). Connectivity of fuels has been associated with increased wildfire size and shorter fire return intervals (Miller and Urban 2000; O’Donnell et al. 2011; Balch et al. 2013; Fernandes et al. 2016). Extending this understanding beyond fuels to also incorporate the process of fire spread, we define ‘fire connectivity’ as the landscape’s capacity to transmit fire from one point on the landscape to another. Circuit-based connectivity methods, which have been widely applied within landscape and wildlife ecology (Dickson et al. 2019), offer a compelling method for understanding the patterns of potential fire connectivity (Gray and Dickson 2015). Circuit methods provide a cumulative estimate of connection probability based on the mathematics of electrical current flow (McRae et al. 2008) and can be used to model and visualize connections across large landscapes. Current flows across a cost surface of pixels representing landscape conductance that approximates a random walk and evaluates the relative ease of moving through many possible paths of wildfire progression. Circuit-based analyses have been used to analyze local-level fire connectivity among cheatgrass patches in the Mojave Desert (Gray and Dickson 2016) and compared with empirical and simulated fires (Gray and Dickson 2015). However, circuit-based assessments of fire connectivity have not been developed at ecoregional- or biome-scales. Assessing potential paths for wildfire across such broad scales may help to identify how different fuel treatment design and placement strategies could increase fire suppression efficiency. 

Vol:. (1234567890) 

1 3 

Landsc Ecol (2023) 38:1663–1676 

1665 

Fire connectivity analyses can be used to identify opportunities for management actions to disrupt potential fire spread, and fuel breaks are a key management tool to accomplish the objective of reducing wildfire spread at landscape-scales. Fuel breaks are typically constructed as linear strips along roads in which fuels are reduced, redistributed, or enhanced (e.g., by increasing fuel moisture), with the primary goals of altering fire behavior (i.e., reduce fire-line intensity) and providing safe access for fire crews to stage or actively combat fire fronts (Agee et al. 2000; Syphard et al. 2011; Shinneman et al. 2019). The placement of fuel breaks has been historically designed to protect valued resources such as human infrastructure or ecologically important areas at high risk of fire and placed in locations that support fire suppression operations and logistics. However, the siting of new fuel breaks is often assessed at relatively local scales, typically determined by local land management offices. Although locally relevant siting is important and practical, decisions of where to develop new networks or extend existing networks could additionally be supported by fire connectivity maps. Comprehensive, broad-scale assessments of fuel-driven fire connectivity across large landscapes can help optimize designs of fuel break networks to more efficiently disconnect large tracts of flammable vegetation. 

In the western United States fuel breaks are a large component of wildfire management efforts (Hoover 2017; Bureau of Land Management 2020). The Bureau of Land Management has approved plans to significantly expand the existing fuel break network through implementation of ~ 17,700 km of new or enhanced fuel breaks across the Great Basin region over the next several years (Shinneman et al. 2019, Bureau of Land Management 2020). Future fuel break implementation plans could be supported by broad-scale pattern analyses that evaluate fuel break configuration options in the context of fire connectivity. Fuel break placement and maintenance could be prioritized, for example, in locations that optimally disconnect areas of high potential fire connectivity and contiguous, highly flammable fuels. 

We developed an approach to assess the spatial patterns for fire connectivity in and among areas with high potential rates of fire spread. To do so, we applied circuit-based analyses using an omnidirectional circuit theory algorithm (Omniscape; McRae 

et al. 2016; Landau et al. 2021) to assess fire connectivity across a large region. Specifically, we sought to identify pathways that connect areas of high rate of fire spread in the Great Basin. We expected that fire connectivity and relative flow patterns would reflect the heterogeneity of the landscape and provide insights into the variation of potential fire spread. To our knowledge, this is the first application of omnidirectional circuit theory to characterize fire connectivity and use results to identify areas where targeted management actions could disrupt key linkages among areas with high potential rates of fire spread. We developed fire connectivity pattern metrics, summaries, and examples to explore how such analyses could support spatial fuel management such as fuel reduction treatments, installing new fuel breaks and networks, and prioritizing the maintenance of existing fuel breaks. 

## **Methods** 

## Study region 

The sagebrush-steppe ecosystem and sagebrushdominated landscapes in the western United States are considered imperiled, due in large part to nonnative annual grass invasion that affects the frequency, severity, and size of wildfires (Noss and Peters 1995; Shinneman 2020). The Great Basin is comprised of many plant species (sagebrush, perennial grasses) that are slow to recover after fire and it supports numerous wildlife species of concern (Wisdom et al. 2005; Rottler et al. 2015). We focused on two main ecoregions of the Great Basin that are central to the planned Bureau of Land Management (BLM) (2020) fuel break expansion: the Northern Basin and Range (Ecoregion Level III, 10.1.3) and Central Basin and Range (10.1.5, Bureau of Land Management 2020). The majority of land in the Great Basin (~ 76%) is managed by federal agencies, with high potential for coordinated, broad-scale landscape management actions (e.g., among thirty-five BLM field offices that intersect the study area; Fig. 1). 

## Fire connectivity model 

We used an omnidirectional circuit theory approach to model the probability of fire spread within the 

Vol.: (0123456789) 1 3 

1666 

Landsc Ecol (2023) 38:1663–1676 

**Fig. 1** Existing and planned fuel breaks in the Great Basin. Analysis of the future fuel break network includes both the existing and planned fuel breaks. Line thickness of fuel breaks are exaggerated for visibility (most fuel breaks are less than 200 m in width; Shinneman et al. 2019). Bureau of Land Management field office administrative boundaries are delineated by white lines 



Great Basin shrub-steppe ecosystem. We performed the analysis using the Omniscape connectivity modeling algorithm (v0.5.6, Landau et al. 2021) in Julia programming language (v1.5.2, Bezanson et al. 2017). The Omniscape algorithm is designed for efficient computation over large landscapes. It uses a moving window approach to connect any pixels meeting specified thresholds, in contrast to the related Circuitscape algorithm (McRae and Shah 2009) that calculates connections among discrete patches or nodes placed in specific locations, i.e., in patches or map edges. We used the moving window approach to connect pixels within the window as sources and grounds in order to identify and characterize the pathways or linkages among areas with high rates of spread. Requirements for the Omniscape algorithm include a resistance or conductance surface, threshold value for pixels to be considered sources, and the selection of a moving window size. 

We developed a conductance surface for our connectivity analysis using a modeled fire rate of spread (ROS). The ROS surface was calculated using the FlamMap fire mapping and analysis system (Finney 2006) at 30 m resolution using Scott and Burgan’s 40 fire behavior fuel models (fuel models represent classes of live/dead vegetation types for input into fire behavior models, Scott and Burgan 2005) with fuel disturbances updated to 2019 conditions from the base LANDFIRE 2016 dataset (https:// landf ire. gov/ getda ta. php). To model fire behavior that is likely to be targeted for fire suppression activities, we used 15 mph upslope winds and 97th percentile fuel moisture conditions (3%, 4%, and 5% fuel moisture for 1 h, 10 h, and 100 h fuels, respectively, and with 45% live herbaceous and 90% live woody fuel moistures; Keane 2015). We used these conditions to reflect landscape fire conditions where suppression activities are feasible; with greater winds 

Vol:. (1234567890) 

1 3 

Landsc Ecol (2023) 38:1663–1676 

1667 

suppression activities are less effective or are abandoned because they are too dangerous to firefighters. Our attempt here is to use fuel and weather conditions where fuel breaks could be used for active suppression efforts. Fuel breaks and other fuel treatments were not explicitly included in the underlying ROS calculation and so passive effects of fuel breaks (i.e., reduced current flow due to treated fuel conditions within breaks) were not considered in those calculations. Hence, results describe potential fire connectivity in the absence of fuel breaks and related fuel treatments. We aggregated the resulting ROS surface to 270 m resolution for computational efficiency. To reduce barrier effects, non-target landcover (e.g., irrigated agriculture) was assigned a value by randomly sampling the ROS values from the target landcover cells, and subsequently masked out of final outputs. We also created a buffer around the study region to reduce potential edge effects. The buffer extended to the radius of the moving window (described below) and was filled with the same distribution of values 

as the non-target landcover pixels (see Supplemental Information Fig. 1). 

Omniscape calculates linkages among pixels within a moving window by calculating the cumulative current flowing through each pixel (Landau et al. 2021). Current originates from source pixels with high rates of spread in the conductance map and flows to target pixels within the moving window. We set the source threshold parameter equal to the  75<sup>th</sup> percentile of the ROS values across the Great Basin (ROS = 39 chains/hour) to represent only those areas with high rates of spread. Any pixels greater than this threshold were considered sources and targets in the moving window analysis. To identify potential fire connectivity patterns that are relevant to the spread of large wildfires, we set the moving window radius at 78.03 km (270 m × 289 cells) to encompass the maximum radius achieved by a wildfire or wildfire complex in the study region from 2000 to 2019 (~ 78 km in 2007, Welty and Jeffries 2020). The full 

**Fig. 2** Omnidirectional circuit theory output showing potential fire connectivity in the Great Basin based on cumulative current density, visualized with 20 quantiles 



Vol.: (0123456789) 1 3 

1668 

Landsc Ecol (2023) 38:1663–1676 

Omniscape initialization file can be found in Supplemental Information (Fig. 2). 

To characterize fire connectivity in terms of the number of potential paths that connect high rateof-spread areas across the full extent, we calculated the cumulative current density across the landscape. The cumulative current density calculates the sum of potential paths over which a process can spread for each pixel on the landscape. For visualization, we conducted a standard raster log-transformation and binned the map into 20 quantiles (McRae et al. 2016; Landau et al. 2021). To differentiate paths of highly constrained flow (e.g., pinch points of flow) from those of diffuse flow (able to move among many paths), we used the normalized cumulative current density output; this output is calculated by dividing cumulative density by the current flow expected under null resistance conditions whereby sources remain the same but all resistance values are set to 1 (Landau et al. 2021). This normalized cumulative current density represents the relative flow of a process and characterizes whether it is impeded (relative flow < 1), diffuse (relative flow ~ 1), or channelized (relative flow > 1). We used the standard deviation of relative flow values (SD = 0.2362) to classify the values into five categories (Table 1) and adapted the interpretation of relative flow classes from McRae et al. (2016) to describe fire connectivity (Table 1). We also include the expected relationships between the relative flow classes and fuel break placement (Table 1). 

## Fuel break distribution and density 

To understand the current and planned fuel break network in the context of fire connectivity results, we overlaid the existing (Shinneman et al. 2018) and planned (Bureau of Land Management 2020) fuel break networks with maps of potential fire connectivity and relative flow. We used a 9 × 9 cell focal window (~ 1 km) around pixels with fuel breaks to calculate the mean connectivity value and summarize local fire connectivity around fuel breaks. We used a Spearman rank correlation test to evaluate how fuel breaks were distributed relative to the potential fire connectivity classes (Koen et al. 2014; Gray and Dickson 2015). We also considered the density of fuel breaks in a region may contribute to the effectiveness of the fuel break network, 

particularly compared with the relative flow classes that represent locally relevant patterns. We calculated local fuel break density as the number of pixels that were occupied by fuel breaks within the local neighborhood of 8 km. The neighborhood size represents the 95th percentile radius of fires or fire complexes that occurred between 2000 and 2019 (Welty and Jeffries 2020). We used polygons for hydrological units (HUC10 watersheds) and BLM field office management units (Fig. 1) to represent general ecologically and management-relevant regions within which to summarize and compare fuel break network characteristics. We compared average fuel break density and dominant relative flow class for the existing fuel break network, as well as the planned network (i.e., including both existing and planned fuel breaks). 

## **Results** 

## Regional potential fire connectivity 

The cumulative current density output illustrated spatial patterns of relatively higher and lower potential fire connectivity (Fig. 2). Distinct areas of higher fire connectivity represent many cumulative pathways for fire to spread and to connect areas with predicted high rates of spread (Buchholtz and Kreitler 2023). These well-connected areas and high rates of spread could therefore indicate greater potential for extensive wildfires. Areas with lower fire connectivity represent lower cumulative density of pathways for fire to spread. At a broad scale, these fire connectivity patterns highlight linkages among areas expected to have landscape and fuel characteristics that can support fires capable of spreading to proximate highly flammable areas. Fire connectivity results do not represent individual fires nor fire behavior explicitly, and results do not express the likelihood of ignition or risk of fire. 

We found that existing fuel breaks were evenly distributed across the twenty potential fire connectivity classes (Spearman rank correlation test: S = 1544, rho = − 0.1609, p < 0.496; Fig. 3). Local patterns varied, with the area near existing fuel breaks occurring in areas of high, moderate, as well as low potential fire connectivity patterns (Figs. 3 & 

Vol:. (1234567890) 

1 3 

Landsc Ecol (2023) 38:1663–1676 

1669 

|Class values|0.0–0.7638<br>0.7638–0.8819<br>0.8819–1.118<br>1.118–1.236<br>> 1.236|
|---|---|
|Fuel breaks interpretation|Impeded areas may be the least strategic for fuel breaks, unless<br>highly valuable resources or risk factors are present (e.g., near<br>human population)<br>Diffuse areas may require a more complex network of fuel breaks to<br>best alter the variable flow of fire<br>Channelized areas may permit strategic placement of relatively few<br>fuel breaks, given the spatially restricted nature of fire connectivity|
|Fire connectivity interpretation|Fires that burn in impeded areas face high resistance to propagation<br>due to landscape features, fuels, and their configuration. Where<br>flow potential is substantially limited, fires may appear to divert<br>around these areas by following paths of higher conductance<br>Fire exhibits intermediate propagation patterns ranging from<br>impeded to diffuse classification<br>Fires that burn in diffuse areas will have many potential directions of<br>propagation. This is indicated by widespread and largely unre-<br>stricted current flow, with few barriers or interrupted flow paths<br>among areas with high rates of spread<br>f Fire exhibits intermediate propagation patterns ranging from diffuse<br>to channelized classification<br>Fires that burn in channelized areas may be constrained by landscape<br>barriers or less flammable fuels or bordered by impeded areas.<br>Channelized areas have higher current flow than expected under<br>null conditions and indicate areas where fire potential spread direc-<br>tions may be concentrated into narrow corridors or pathways|
|(2016)<br>Relative flow class|Impeded<br>Diffuse-Impeded<br>Diffuse<br>Diffuse-channelized<br>Channelized|



Vol.: (0123456789) 1 3 

1670 

Landsc Ecol (2023) 38:1663–1676 

**Fig. 3** Distribution of area classified as within fuel breaks across potential fire connectivity classes for the existing and future fuel break networks. Note, connectivity classes are equal in area across the study region 



5). The future fuel break network, which included both existing and planned fuel breaks, showed a strong negative rank correlation with potential fire connectivity, (Spearman rank correlation S = 2654, rho = − 0.9955, p < 0.0001; Figs. 3, 5) with more fuel breaks planned in lower fire connectivity classes. 

## Regional patterns of relative flow 

Using normalized cumulative current density as a measure of potential relative flow of fire across the Great Basin, we found that the landscape is characterized by a distinct fire connectivity gradient where relative fire flow is either impeded, diffuse, or channelized (Figs. 4, 5). Relative flow patterns were highly heterogeneous and varied across watersheds and regionally (Buchholtz and Kreitler 2023). Areas with relatively impeded or channelized flow emerged as a result of the landscape configuration and spatial variation in modeled fire ROS. Some fuel breaks were placed in areas with relatively impeded flow (Fig. 5A), while others were placed or planned for areas that intersected with relatively channelized flow (Fig. 5B). 

The dominant pattern of relative flow varied across the 35 BLM field office units in the Great Basin (Figs. 3, 6, Supplemental Table 1). Impeded or diffuse-impeded flow characterized the majority of 4 field offices, indicating landscape constraint or barriers to flow. Fourteen field office regions were 

dominated by diffuse flow, indicating many directionally unconstrained potential fire paths. Six field offices were dominated by diffuse-channelized flow and eleven by channelized flow, representing where potential paths linking areas with high rate of spread were more concentrated than expected. 

Most watersheds were dominated by diffuse relative flow (n = 604). Watersheds characterized by mostly diffuse-channelized relative flow were limited (n = 24, Table 2). The highest fuel break densities were in watersheds with high amounts of diffuse-impeded relative flow areas; conversely, lower fuel break densities were in watersheds dominated by channelized relative flow (Table 2, Fig. 7). Average local (8 km) fuel break density was higher in watersheds with diffuse and diffuseimpeded flow patterns than in ones with more channelized flow patterns. However, there was a broad range of densities across the landscape, especially within the diffuse-impeded relative flow class. The maximum local fuel break density by watershed was 22.7  km<sup>2</sup> per 100  km<sup>2</sup> in the current network and was 29.0  km<sup>2</sup> per 100  km<sup>2</sup> in the future fuel break network (i.e., including both existing and planned fuel breaks). Both maximum densities occurred in watersheds dominated by diffuse-impeded relative flow. 

We summarized potential fire connectivity and relative flow patterns across BLM field office units by state (Fig. 6, Supplemental Table 1). Field offices with higher connectivity classes represent regions 

Vol:. (1234567890) 1 3 

Landsc Ecol (2023) 38:1663–1676 

1671 

**Fig. 4** Omnidirectional circuit theory output showing relative flow patterns in the Great Basin based on normalized cumulative current density. The output represents how the landscape shapes cumulative patterns, for example, by impeding or channelizing flow paths. White lines indicate Bureau of Land Management (BLM) Field Office boundaries 



with high fire ROS and strong connectivity among areas with high ROS. Field offices with lower connectivity classes represent regions that may have lower fire ROS and are distant or poorly connected to areas with high ROS. 

## **Discussion** 

Altered wildfire regimes can pose considerable social, economic, and environmental challenges, and different analytical tools are needed to understand, plan, and manage them. Our approach to modeling the contagious nature of the fire process by quantifying potential fire connectivity permitted the identification of areas on the landscape that might facilitate or impede fire spread. The spatially heterogeneous fire connectivity patterns produced by our model reflect landscape variation of fuels and topography that influence rate of fire spread, and may reveal potential concentrations of fire 

spread via pathways capable of connecting highly flammable areas. Moreover, by assessing the distribution of existing and planned fuel breaks within our model framework, we’ve provided an opportunity to examine where these fuel treatments might most effectively disrupt fire spread vis-à-vis areas with either potentially high fire connectivity or highly concentrated fire connectivity relative to surrounding conditions. 

Fire connectedness among regions with fuel and landscape characteristics that accelerate fire spread (Fig. 2) represent potential pathways that can facilitate fire spread across large portions of the study area, potentially resulting in larger fire sizes. Variation in fire connectivity patterns indicate that regions with higher or lower connectivity values may benefit from using different fuel break strategies to disconnect fuels. For example, BLM field offices in northcentral and western Nevada exhibited high fire connectivity (Figs. 2 and 6A). Areas such as these, with generally high potential fire connectivity, may require 

Vol.: (0123456789) 1 3 

1672 

Landsc Ecol (2023) 38:1663–1676 



**Fig. 5** Rate of spread, potential fire connectivity, and relative flow patterns all provide different information about how fire may spread across the landscape. These patterns can, in turn, be used to provide context for the placement of fuel breaks with the goal of efficiently limiting fire spread. A. _(left to right)_ A region of relatively moderate rate of spread. This region spans a gradient of potential fire connectivity values indicating variation in the density of linkages among high-spread areas for fire. Relative flow varies as well. Existing fuel breaks in 

this region exist primarily in the low potential fire connectivity and the already impeded areas. B. _(left to right)_ A region of heterogeneous rates of fire spread. Here, potential fire connectivity values may be relatively similar in pattern to the rates of spread, while the relative flow classes highlight areas with channelized flow where impeded regions serve to channelize the flow. There are few existing fuel breaks, and the proposed fuel breaks cross many of the channelized flow paths 



**Fig. 6** The **A** mean connectivity class and **B** dominant relative flow class for each BLM field office, grouped by state 

Vol:. (1234567890) 

1 3 

Landsc Ecol (2023) 38:1663–1676 

1673 

**Table 2** Placement of fuel breaks in the context of fire connectivity and dominant relative flow classes, summarized within watersheds 

|Relative flow class|n*|Fuel break densit<br>Mean (SD)|y  km<sup>2</sup>/100  km<sup>2</sup>|
|---|---|---|---|
|||Current density|Future density|
|Impeded|186|0.490 (1.68)|2.53 (3.43)|
|Diffuse-impeded|57|1.65 (3.78)|5.24 (6.79)|
|f<br>Diffuse|604|0.832 (1.65)|3.45 (3.66)|
|f<br>Diffuse-channelized|24|0.342 (0.889)|0.662 (1.17)|
|f<br>Channelized|43|0.0323 (0.154)|0.402 (1.03)|



*n = 914 hydrologic unit HUC10 watersheds, with mean area 494.7  km<sup>2</sup> (range 0.106–4414  km<sup>2</sup> ) 



**Fig. 7** Density of local fuel breaks in Great Basin watersheds, grouped by the dominant relative flow class for each watershed. Box plots depict the minimum, first quartile, median, third quartile, and maximum values for each relative flow class for the current and future fuel break networks 

a greater concentration of fuel breaks to reduce or disrupt fire compared to areas with lower fire connectivity (although ecological trade-offs should be considered; see Shinneman et al. 2019). In regions with lower fire connectivity, managers may consider other strategies to reduce fuels and wildfire risk, including using local patterns of relative flow (e.g., Figs. 4 and 5) combined with local expertise to spatially refine fuel treatment strategies to disrupt specific areas with 

highly concentrated fire connectivity potential on the landscape. 

Indeed, the relative flow patterns highlight the diverse ways that landscape patterns could facilitate or impede the transmission of fire. Different types of relative flow (diffuse, impeded, channelized) may indicate different levels of constraint on fire spread due to spatial configurations of landscape characteristics (e.g., topography) and fuels that either support or inhibit high rates of fire spread. In areas of diffuse flow, fire may be less directionally constrained and move primarily in response to local wind, weather, and fire conditions. Higher fuel break densities arranged in a network design may provide opportunities to access and combat active fires that could come from multiple directions in these types of environments (Maestas et al. 2016). Accordingly, we found that the density of fuel breaks was spatially correlated with diffuse or diffuse-impeded relative flow areas on average (Table 2), perhaps because these areas have gentler terrain with existing road networks that facilitated fuel break construction. By contrast, fire spread may be more directionally constrained in areas with relatively channelized flow. In these areas, the landscape configuration of fuels limits possible fire paths, and thus fewer but more strategically placed fuel breaks that bisect channelized pinch points could disconnect linkages among high ROS areas. Gray and Dickson (2016) also used a circuit model approach to suggest that the placement of a few, well-placed fuel breaks might be highly effective at reducing potential fire spread among highly flammable areas. These types of results highlight the potential utility of a circuit-based approach to inform installation locations for fuel breaks, particularly those placed in highly channelized flow areas that could yield disproportionate benefits. 

Existing fuel breaks were evenly distributed across fire connectivity classes. Future fuel breaks, though, are generally planned for areas with moderate or lower fire connectivity thus increasing the density of the fuel break network in those areas. Across our study area landscape, we estimated that the average density of fuel breaks will roughly triple with the implementation of the BLM planned fuel break network. However, based on our assessment, key areas of diffuse flow are expected to still lack fuel break networks in the future, as will many isolated locations 

Vol.: (0123456789) 1 3 

1674 

Landsc Ecol (2023) 38:1663–1676 

with channelized flow in which a few fuel breaks could be highly strategic. 

Ideally, a combination of fire modeling, local knowledge, and logistical considerations would result in the lowest fuel break density that achieves the highest possible return on reduction of wildfire, particularly to protect valued resources in areas where fire is no longer ecologically beneficial due to extensive exotic annual grass cover and dramatically decreased mean fire return intervals (Fusco et al. 2019). Although there may be reasonable ecological, logistical, or fire-risk reasons for some areas to not have fuel breaks, further work is needed to describe and understand the underlying patterns driving fuel break placement. There may be opportunities to increase effectiveness of fuel break networks by including fire connectivity as one of the criteria that informs fuel break design and placement. Fire connectivity results could be paired with fire behavior or cumulative fire risk models to enrich information used in the design of fuel break networks (Rodriguez Gonzalez et al. 2008). Precise placement will depend on many other considerations as well, including locations of existing and accessible roads, fuel break maintenance logistics, locations of cultural and natural resources, and conservation objectives (Syphard et al. 2011; Shinneman et al. 2019). 

The omnidirectional circuit theory approach can complement existing fire behavior models by assessing the spatial patterns associated with areas capable of burning with high rates of spread, but it has limitations and assumptions that must be recognized. The fire connectivity analysis does not model individual fires or their behavior and should not be interpreted to estimate fire probabilities or assess cumulative fire risk. Our approach did not explicitly incorporate likelihood of ignition or burn probability; therefore, it is possible to have areas where there would be high connectivity for fire to spread, but low probability for a fire to start, and therefore low likelihood that fire would spread across a modeled fire connectivity linkage there. However, even if likelihood of fire ignition is low, preventative actions may be appropriate in areas of higher potential fire connectivity for areas that would have substantial negative consequences from wildfire (e.g., the wildland urban interface). Ignition and burn probability could be incorporated into future research using circuit theory methods, for example, 

by using those variables to inform relevant source layers for the circuit analysis. Alternatively, our output highlighting fire connectivity potential could be combined post-hoc with maps of ignition rates (see Balch et al. 2017) and output from large fire behavior models that are often used to generate fire risk assessments and to help locate effective fuel treatments (e.g., FSim; Finney et al. 2011). For example, areas with high potential fire connectivity could be superimposed on or included in assessments of wildfire risks to highly valued resources based on burn probability and fire intensity, as well as analyses of wildfire risk transmission across landscapes (Ager et al. 2012, 2014; Calkin et al. 2011; Scott et al. 2013; Dillon et al. 2015; Gonzalez-Olabarria et al. 2019; Kreitler et al. 2020). In addition, this information could be incorporated into new developing spatial fire planning efforts for large fire containment such as Potential Wildfire Operation Delineations (PODS; Thompson et al. 2016; Wei et al. 2018). Further research is needed to understand the degree to which fire connectivity analyses can practically improve fuel break strategies and effectiveness. 

Wildfire will continue to be a considerable ecological and economic challenge in the sagebrush biome, and it requires that we develop tools to understand and mitigate wildfire from a landscape perspective. We adapted theoretical and analytical connectivity methods used to describe gene flow and animal movement, with resulting novel outputs for identifying linkages among quick-burning patches and visualizing directional constraints at larger scales that may shape how wildfires spread. Where large wildfires are common, identifying areas with high fire connectivity potential can provide insights into strategic locations for fuel treatments to intentionally disconnect and reduce fire spread. The circuit theory approach can provide a new understanding of how landscapes facilitate wildfire spread, complementing existing data and models, and offering opportunities to further investigate connectivity-based approaches to fire management. 

**Acknowledgements** Any use of trade, firm, or product names is for descriptive purposes only and does not imply endorsement by the U.S. Government. This work was partly funded by the US Department of Interior, Bureau of Land Management, in support of fuel break research. 

Vol:. (1234567890) 

1 3 

Landsc Ecol (2023) 38:1663–1676 

1675 

**Author contributions** JK modeled ROS and EB conducted the connectivity analyses. EB, JK, DS, MC & JH (all authors) participated in discussing, refining, and interpreting the approach, analyses, and results. EB led the writing of the manuscript, with all authors contributing to the writing and revising. 

**Funding** This work was partly funded by the US Department of Interior, Bureau of Land Management, in support of fuel break research. 

**Data availability** The connectivity datasets generated during the current study are publicly available as a U.S. Geological Survey data release (Buchholtz and Kreitler 2023). 

### **Declarations** 

**Competing interests** The authors have no relevant financial or non-financial interests to disclose. 

**Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http:// creat iveco mmons. org/ licen ses/ by/4. 0/. 

## **References** 

- Agee JK, Bahro B, Finney MA, Omi PN, Sapsis DB, Skinner CN, Van Wagtendonk JW, Weatherspoon CP (2000) The use of shaded fuelbreaks in landscape fire management. For Ecol Manag 127:55–66 

- Ager AA, Day MA, Finney MA, Vance-Borland K, Vaillant NM (2014) Analyzing the transmission of wildfire exposure on a fire-prone landscape in Oregon, USA. For Ecol Manag 334:377–390 

- Ager AA, Vaillant NM, Finney MA, Preisler HK (2012) Analyzing wildfire exposure and source–sink relationships on a fire prone forest landscape. For Ecol Manag 267:271–283 

- Balch JK, Bradley BA, Abatzoglou JT, Nagy RC, Fusco EJ, Mahood AL (2017) Human-started wildfires expand the fire niche across the United States. Proc Natl Acad Sci USA 114:2946–2951 

- Balch JK, Bradley BA, D’Antonio CM, Gomez-Dans J (2013) Introduced annual grass increases regional fire activity across the arid western USA (1980–2009). Glob Chang Biol 19:173–183 

- Bezanson J, Edelman A, Karpinski S, Shah VB (2017) Julia: A fresh approach to numerical computing. SIAM Rev 59:65–98 

- Buchholtz EK, Kreitler J (2023) Circuit-based potential fire connectivity and relative flow patterns in the Great Basin, United States, 270 meters: U.S. Geological Survey Data Release. https:// doi. org/ 10. 5066/ P9EA3 E00 

- Bureau of Land Management B (2020) Final programmatic EIS for fuel breaks in the Great Basin. In: United States Department of Interior Bureau of Land Management. 

- Calkin DE, Cohen JD, Finney MA, Thompson MP (2014) How risk management can prevent future wildfire disasters in the wildland-urban interface. Proc Natl Acad Sci USA 111:746–751 

- Calkin DE, Thompson MP, Finney MA, Hyde KD (2011) A real-time risk assessment tool supporting wildland fire decisionmaking. J Forest 109:274–280 

- Dennison PE, Brewer SC, Arnold JD, Moritz MA (2014) Large wildfire trends in the western United States, 1984–2011. Geophys Res Lett 41:2928–2933 

- Dickson BG, Albano CM, Anantharaman R, Beier P, Fargione J, Graves TA, Gray ME, Hall KR, Lawler JJ, Leonard PB, Littlefield CE, McClure ML, Novembre J, Schloss CA, Schumaker NH, Shah VB, Theobald DM (2019) Circuittheory applications to connectivity science and conservation. Conserv Biol 33:239–249 

- Dillon G, Menakis J, Fay F (2015) Wildland fire potential: a tool for assessing wildfire risk and fuels management needs. In: Keane RE, Jolly M, Parsons R, Riley K (eds) Proceedings of the large wildland fires conference; May 19–23, 2014; Missoula, MT. Proc. RMRS-P-73. US Department of Agriculture, Forest Service, Rocky Mountain Research Station, Fort Collins, pp 60–76. 

- Fernandes PM, Monteiro-Henriques T, Guiomar N, Loureiro C, Barros AMG (2016) Bottom-up variables govern large-fire size in Portugal. Ecosystems 19:1362–1375 

- Finney MA (2006) An overview of FlamMap fire modeling capabilities. In: Andrews PL, Butler BW, comps. 2006. Fuels Management-How to Measure Success: Conference Proceedings. 28–30 March 2006; Portland, OR. Proceedings RMRS-P-41, pp 213–220. US Department of Agriculture, Forest Service, Rocky Mountain Research Station, Fort Collins 

- Finney MA, McHugh CW, Grenfell IC, Riley KL, Short KC (2011) A simulation of probabilistic wildfire risk components for the continental United States. Stoch Env Res Risk Assess 25:973–1000 

- Fusco EJ, Finn JT, Balch JK, Nagy RC, Bradley BA (2019) Invasive grasses increase fire occurrence and frequency across US ecoregions. Proc Natl Acad Sci USA 116:23594–23599 

- Gill AM, Stephens SL, Cary GJ (2013) The worldwide “wildfire” problem. Ecol Appl 23(2):438–454 

- Gonzalez-Olabarria JR, Reynolds KM, Larranaga A, GarciaGonzalo J, Busquets E, Pique M (2019) Strategic and tactical planning to improve suppression efforts against large forest fires in the Catalonia region of Spain. For Ecol Manag 432:612–622 

- Gray ME, Dickson BG (2015) A new model of landscapescale fire connectivity applied to resource and fire. Ecol Appl 25:1099–1113 

Vol.: (0123456789) 1 3 

1676 

Landsc Ecol (2023) 38:1663–1676 

- Gray ME, Dickson BG (2016) Applying fire connectivity and centrality measures to mitigate the cheatgrass-fire cycle in the arid West, USA. Landsc Ecol 31:1681–1696 

- Higuera PE, Abatzoglou JT (2020) Record-setting climate enabled the extraordinary 2020 fire season in the western United States. Glob Chang Biol. https:// doi. org/ 10. 1111/ gcb. 15388 

- Hoover K (2017) Wildfire management funding: background, issues, and FY2018 appropriations. Congressional Research Service, Report 45005 

- Keane RE (2015) Wildland fuel fundamentals and applications. Springer, New York, pp 1–191 

- Keyser A, Westerling AL (2017) Climate drives inter-annual variability in probability of high severity fire occurrence in the western United States. Environ Res Lett 12:0655003 

- Kochanski AK, Jenkins MA, Mandel J, Beezley J, Krueger S (2013) Real time simulation of 2007 Santa Ana fires. For Ecol Manag 294:136–149 

- Koen EL, Bowman J, Sadowski C, Walpole AA, Tatem A (2014) Landscape connectivity for wildlife: development and validation of multispecies linkage maps. Methods Ecol Evol 5:626–633 

- Kreitler J, Thompson MP, Vaillant NM, Hawbaker TJ (2020) Cost-effective fuel treatment planning: a theoretical justification and case study. Int J Wildland Fire 29:42–56 

- Landau VA, Shah VB, Anantharaman R, Hall KR (2021) Omniscape.jl: software to compute omnidirectional landscape connectivity. J Open Source Softw 6(57):2829 

- Maestas J, Pellant M, Okeson L, Tilley D, Havlina D, Cracroft T, Brazee B, Williams M, Messmer D (2016) Fuel breaks to reduce large wildfire impacts in sagebrush ecosystems, vol 66. Plant Materials Technical Note, Boise 

- McRae BH, Dickson BG, Keitt TH, Shah VB (2008) Using circuit theory to model connectivity in ecology, evolution, and conservation. Ecology 89:2712–2724 

- McRae B, Popper K, Jones A, Schindel M, Buttrick S, Hall K, Unnasch RS, Platt J (2016) Conserving nature’s stage: mapping omnidirectional connectivity for resilient terrestrial landscapes in the Pacific Northwest. The Nature Conservancy, Portland 

- McRae BH, Shah VB (2009) Circuitscape user’s guide. The University of California, Santa Barbara 

- Miller C, Urban DL (2000) Connectivity of forest fuels and surface fire regimes. Landsc Ecol 15:145–154 

- Noss RF, Peters RL (1995) Endangered ecosystems: a status report on America’s vanishing habitat and wildlife. Defenders of Wildlife, Washington, DC 

- O’Donnell AJ, Boer MM, McCaw WL, Grierson PF (2011) Vegetation and landscape connectivity control wildfire intervals in unmanaged semi-arid shrublands and woodlands in Australia. J Biogeogr 38:112–124 

- Rodriguez Gonzalez J, del Barrio G, Duguy B (2008) Assessing functional landscape connectivity for disturbance propagation on regional scales—a cost-surface model approach applied to surface fire spread. Ecol Model 211:121–141 

- Scott JH, Thompson MP, Calkin DE (2013) A wildfire risk assessment framework for land and resource management. In: F. S. US Department of Agriculture (ed) Rocky mountain research station. 

- Scott J, Burgan R (2005) Standard fire behavior fuel models: a comprehensive set for use with Rothermel’s surface fire spread model. USDA Forest Service, Washington, DC 

- Shinneman DJ (2020) North American sagebrush steppe and shrubland. In: Dellasala MIGADA (ed) Encyclopedia of the world’s biomes. Elsevier, Amsterdam, pp 505–515 

- Shinneman DJ, Aldridge CL, Coates PS, Germino MJ, Pilliod DS, Vaillant NM (2018) A conservation paradox in the Great Basin—altering sagebrush landscapes with fuel breaks to reduce habitat loss from wildfire. US Geological Survey, Reston, pp 2331–1258 

- Shinneman DJ, Germino MJ, Pilliod DS, Aldridge CL, Vaillant NM, Coates PS (2019) The ecological uncertainty of wildfire fuel breaks: examples from the sagebrush steppe. Front Ecol Environ 17:279–288 

- Stavros EN, Abatzoglou JT, McKenzie D, Larkin NK (2014) Regional projections of the likelihood of very large wildland fires under a changing climate in the contiguous Western United States. Clim Chang 126:455–468 

- Sullivan AL (2009a) Wildland surface fire spread modelling, 1990–2007. 1: physical and quasi-physical models. Int J Wildland Fire 18:349–368 

- Sullivan AL (2009b) Wildland surface fire spread modelling, 1990–2007. 2: empirical and quasi-empirical models. Int J Wildland Fire 18:369–386 

- Sullivan AL (2009c) Wildland surface fire spread modelling, 1990–2007. 3: Simulation and mathematical analogue models. Int J Wildland Fire 18:387–403 

- Syphard AD, Keeley JE, Brennan TJ (2011) Factors affecting fuel break effectiveness in the control of large fires on the Los Padres National Forest, California. Int J Wildland Fire 20:764–775 

- Thompson MP, Bowden P, Brough A, Scott JH, GilbertsonDay J, Taylor A, Anderson J, Haas JR (2016) Application of wildfire risk assessment results to wildfire response planning in the Southern Sierra Nevada, California. Forests, USA, p 7 

- Wei Y, Thompson MP, Haas JR, Dillon GK, O’Connor CD (2018) Spatial optimization of operationally relevant large fire confine and point protection strategies: model development and test cases. Can J For Res 48:480–493 

- Welty J, Jeffries MI (2020) Combined wildfire polygons for the United States and certain territories, 1878–2019. U.S. Geological Survey. https:// doi. org/ 10. 5066/ P9Z2V VRT 

- Wisdom MJ, Rowland MM, Suring LH (2005) Habitat threats in the sagebrush ecosystem: methods of regional assessment and applications in the Great Basin. Alliance Communications Group, Lawrence 

**Publisher’s Note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

- Rottler CM, Noseworthy CE, Fowers B, Beck JL (2015) Effects of conversion from sagebrush to non-native grasslands on sagebrush-associated species. Rangelands 37:1–6 

Vol:. (1234567890) 1 3 


