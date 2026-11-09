---
title: Optimization of Fire Station Locations to Increase the Efficiency of Firefighting in Natural Ecosystems
authors:
- Renkas, Artur
- Popovych, Vasyl
- Rudenko, Dmytro
year: '2022'
journal: Environmental Research, Engineering and Management
doi: 10.5755/j01.erem.78.1.25581
tags:
- decision support
- ecosystems
- fire
- fire suppression
zotero_key: MSZFLSIT
item_type: journalArticle
url: https://erem.ktu.lt/index.php/erem/article/view/25581
source_url: 'unpaywall: https://erem.ktu.lt/index.php/erem/article/download/25581/15314'
fulltext_status: fulltext
synced: '2026-11-09'
---

# Optimization of Fire Station Locations to Increase the Efficiency of Firefighting in Natural Ecosystems

## Abstract

Wild fires have a catastrophic impact on the environment and lead to people’s deaths. Such fires are relevant in the global context. Many countries declare some of their territories an ecological disaster zone during fires in natural ecosystems (USA, Portugal, Greece, Spain, Italy, Australia). Fires in ecosystems occurred in southern Ukraine in 2007 and in the eastern part of Ukraine in 2021, which destroyed large tracts of pine, as well as homes, buildings and caused human casualties. In the given research, much attention is paid to fire-prevention measures in natural ecosystems. It is proposed to optimize fire stations in the territory of Male Polissya (Ukraine), where frequent grass fires and grassland forest fires occur, since existing fire stations are not able to respond to all fires in the region in a timely manner due to the lack of forces and resources. Optimization of fire station locations was carried out using Voronoi diagrams. This research has a practical aspect, ensuring the protection of human health and life by preventing destructive fires in natural ecosystems through the creation of local safety facilities. On the example of 3 administrative districts of Lviv Oblast in Ukraine, it was established that in order to respond quickly to fires in ecosystems, it is necessary to create 20 additional fire stations, which has been determined by the 20-minute drive method approved by the state authorities. The algorithm proposed in this work can be applied to rural areas in other administrative units, both in Ukraine and other countries. The next step in the development of this technique is to determine the required amount of equipment and human resources for firefighting in ecosystems taking into account the projected dynamics of fires and the time required for the delivery of fire extinguishers to epicenters of these events.

## Full text

97 

2022/78/1 

Environmental Research, Engineering and Management 

#### EREM 78/1 

Journal of Environmental Research, Engineering and Management Vol. 78 / No. 1 / 2022 pp. 97 _–_ 104 DOI 10.5755/j01.erem.78.1.25581 

|Optimization of Fire Station<br>Firefighting i|Locations to Increase the Efficiency of<br>n Natural Ecosystems|
|---|---|
|Received  2020/04|Accepted after revision  2022/01|
|http://dx.do|i.org/10.5755/j01.erem.78.1.25581|



# Optimization of Fire Station Locations to Increase the Efficiency of Firefighting in Natural Ecosystems 

### Artur Renkas*, Vasyl Popovych, Dmytro Rudenko 

Lviv State University of Life Safety, 35 Kleparivska St., 79000 Lviv, Ukraine. 

*Corresponding author: arthur.rencas@gmail.com 

Wild fires have a catastrophic impact on the environment and lead to people’s deaths. Such fires are relevant in the global context. Many countries declare some of their territories an ecological disaster zone during fires in natural ecosystems (USA, Portugal, Greece, Spain, Italy, Australia). Fires in ecosystems occurred in southern Ukraine in 2007 and in the eastern part of Ukraine in 2021, which destroyed large tracts of pine, as well as homes, buildings and caused human casualties. 

In the given research, much attention is paid to fire-prevention measures in natural ecosystems. It is proposed to optimize fire stations in the territory of Male Polissya (Ukraine), where frequent grass fires and grassland forest fires occur, since existing fire stations are not able to respond to all fires in the region in a timely manner due to the lack of forces and resources. 

Optimization of fire station locations was carried out using Voronoi diagrams. This research has a practical aspect, ensuring the protection of human health and life by preventing destructive fires in natural ecosystems through the creation of local safety facilities. 

On the example of 3 administrative districts of Lviv Oblast in Ukraine, it was established that in order to respond quickly to fires in ecosystems, it is necessary to create 20 additional fire stations, which has been determined by the 20-minute drive method approved by the state authorities. The algorithm proposed in this work can be applied to rural areas in other administrative units, both in Ukraine and other countries. The next step in the development of this technique is to determine the required amount of equipment and human resources for firefighting in ecosystems taking into account the projected dynamics of fires and the time required for the delivery of fire extinguishers to epicenters of these events. 

Keywords: wild fires, fire station, Voronoi diagram. 

98 

2022/78/1 

Environmental Research, Engineering and Management 

## Introduction 

Finding the best firefighting unit locations is an urgent problem, especially for areas where a network of local fire brigades is being formed. Particular regions of Ukraine are examples of such areas, in which a memorandum has been signed between the State Emergency Service of Ukraine and regional state administrations to build an economically justified and effective model of civil protection, including the functioning of the local fire protection service. 

In order to justify the location of state firefighting units in Ukraine, only the criterion of the time needed for a fire engine to get to the site of a fire is taken into account. Accordingly, the maximum time for a city is 10 minutes, while for a countryside, it is 20 minutes. However, it is irrational to consider only one criterion when it comes to this issue. For example, in one study (Yang et al., 2007), the authors proposed a method for determining locations of fire and rescue units by minimizing the cost of firefighting to eliminate fire or the consequences of an accident and the costs associated with the fire development or accidents, and by reducing the longest distance to the possible site of a fire or an accident. 

In the scientific world and practice, there are a number of methods for determining the locations of fire departments, stations, etc. Most of these methods relate to large cities. In a study by Aktaş et al. (2013), a mathematical model to define new fire station locations in Istanbul has been offered. Geoinformation systems are used in the calculation. Taking into consideration the placement of the protection facilities and the 5-minute drive time, the researchers selected the optimal location. Cities of China (Chen & Ren, 2003), cities of California (USA) (Murray, 2013), Santiago city in Chile (Pérez et al., 2016), Tehran district in Iran (Bolouri et al., 2018), Los Angeles (Church & Li, 2016), cities of Karnataka in India (Tali et al., 2017), etc. have also been taken as examples to consider optimal fire station locations. According to all these works, the placement and efficiency of firefighting units around the world are an urgent problem. A network of fire stations was formed about half a century ago relying only on the experience. However, urban population and urban areas are growing and that 

requires an object-oriented approach for the selection of fire station locations. Recent studies point to the need for new methods of finding the best locations for fire stations using GIS technologies, mathematical programming, cyber search, etc. 

In a study by Zhou (2014), the planning of fire station locations is made on the basis of the assessment of fire hazard and the risk of fires. At the same time, authors focus on potentially dangerous areas with a 2-minute drive time in case of a fire. Another work (Dong et al., 2018), based on the fire hazard using GIS technologies, proposes the location of new and redevelopment of old fire stations in Linyi city, Shandong Province. In the research by Kuzyk (2008), an analysis of service areas of fire and rescue units was performed using Voronoi diagrams, based on which the construction of additional fire stations in the city of Lviv (Ukraine) was offered. 

Much less attention is paid to planning the location of fire stations in rural areas. However, a few works are relevant to solving this problem. The article by Sakellariou et al. (2019) examines the distribution of firefighting equipment in rural areas in order to respond to forest fires in a timely manner. The allocation of resources to respond to forest fires is discussed by Van der Merwe et al. (2014). A model of firefighting equipment placement has been developed taking into account cost minimization by the example of South Hobart, Tasmania, Australia. Also, the example of Maine and Massachusetts shows the optimal location of fire stations based on fire statistics (Das et al., 2015). The problem of cost minimization in response to forest fires is also considered in the literature (Donovan & Rideout, 2003; Haight & Fried, 2007). 

Some countries have the opposite problem. For instance, in Germany, the number of fire stations is reduced due to the decrease in the number of fire volunteers (Degel et al., 2014). At the same time, the level of protection of the population against fires should remain stable. Also, authors (Pereira et al., 2012) offer to be more focused on fire prevention than on its suppression. Thus, the article considers tools for landscape management that reduce the risk of uncontrolled wildfires. 

99 

2022/78/1 

Environmental Research, Engineering and Management 

The analysis of the publications proves that the problem of determining the location of fire stations in rural areas, which would take into account not only the statistics of fires in cities or forests, but also the statistics of steppe and peat fires, remains unsolved. 

Moreover, the statistics of fires in ecosystems in Lviv Oblast for 2019 shows that the area of some steppe and peat fires reaches more than 1 hectare, and the duration of their extinguishment exceeds 1 day. In this case, significant labor and material resources are spent. One of the reasons is a considerable distance from fire units to sites of fires and a long time required to transport the equipment to the sites of fires. 

Therefore, determining the location of fire brigades and units taking into account the statistics of fires in ecosystems is an important task. 

## Methods 

_Aim of the research._ The purpose of the study is to define optimal fire station locations taking into account fire occurrences in natural ecosystems, and minimizing the arrival time of firefighters, extinguishing costs and the negative effects of these fires. 

_Objects of the research._ The object of the study is a network of fire stations in Lviv Oblast (Ukraine), namely state firefighting stations, local volunteer fire brigades and local fire crews that are being formed. The research of the required number of fire stations in rural areas is based on the statistics of fire danger in natural ecosystems. The data on fires in forests, agricultural lands, peat lands and landfills for 2019 was taken from the Main Department of the State Emergency Service of Ukraine in Lviv Oblast. 

Lviv Oblast is located in the west of Ukraine, within the limits of 22°43'- 25°24 'E and 48°45'- 50°46' N latitude. The population amounts to 2522 thousand. The total area of the region is 2.18 million hectares. The region is located in 3 zones: forest, steppe, foothills and mountainous areas of the Carpathians. Forests cover almost one-fourth of the total region area. The climate is temperate continental, humid: soft winters with thaws, wet springs, warm summers and warm autumns. The average January temperature is −5°C, while the July temperature is +18°C in the central part 

of the region and +12°C in the mountains. Annual precipitation varies from 600 mm on the plain to 1000 mm in the mountains. 

Mathematical statistics and Voronoi diagrams are used to find the optimal fire station locations to solve the proximity problem (Okabe et al., 2009). 

Determining the optimal location of fire departments is carried out in three stages: 

- **_** the sites of fires are plotted on the map, and their coordinates in the Cartesian coordinate system are determined; 

- **_** on the basis of the received coordinates, a Voronoi diagram is constructed, where vertices of the diagram are the sites of fires; 

- **_** the obtained Voronoi diagram is plotted on the map, where the nodes of the cell edges are points equidistant from the fires; 

- **_** the locations of fire brigades are plotted on the map and the need to create additional fire units taking into account the existing ones are analyzed. 

Locations of additional fire units should be provided for in the nodes of the edges of the diagram cells if there are no fire units between the nodes of the cell edges and the diagram vertices or within the radius of 3 kilometers around the diagram vertices. 

#### Results and Discussion 

Fires in open rural areas occur quite often during the spring-summer fire hazard season. Therefore, mostly fields, peatlands and forest litter burn. The most common causes of such fires are negligence, careless handling of fire, leaving the fire unattended. Thus, the human factor plays a major role here. These fires are hazardous because they form toxic combustion products, which are released into the air and deposited in soil and water. Toxic combustion products are hazardous to human health as they contain carcinogens, and can cause respiratory and cardiovascular diseases. That is why reducing the duration of fires by responding quickly is a topical issue. In addition, fires in fields and peatlands near forests can cause largescale forest fires. 

Therefore, the location of fire stations near settlements and areas where fires occur most commonly 

100 

2022/78/1 

Environmental Research, Engineering and Management 

should be determined taking into account the time of arrival to places where the risk of fires is high. For different countries, the time of arrival to the site of a fire is set by state standards and can vary from 5 minutes to more. For rural areas, this time may be twice as long. For example, in Ukraine, state fire departments should be located in a way that would allow for the time of arrival not to exceed 10 minutes in the city, and 20 minutes in the countryside. The linear flame propagation velocity by vegetation, forest litter, etc. at the wind speed of 10–12 m/s can reach up to 83 m/ min, while on the edges, on flanks and in the rear it may be up to 14 m/min. Steppe fires with dry vegetation are especially dangerous in dry weather, since the speed of flame spread can reach 700 m/min, and they can also turn into forest fires (Timofeeva et al., 2013). 

Therefore, the free development of such fires for 20 minutes is unacceptable. 

The following limitations must be considered while determining the location of fire stations: the time to reach the site of a fire must be minimal, the operating cost of fire stations should be minimal and less than the losses resulting from the fire. The first condition can be achieved using statistical analysis of the fire dynamics in open areas, GIS-technologies and the use of Voronoi diagrams. The second condition can be ensured by introducing seasonal work of voluntary firefighting units, irregular (part-time) alternating shifts at fire station locations, the use of adapted agricultural machinery or motor trailers pump for the extinguishment of fires, etc 

Fig. 1. _Lviv Oblast: (a) fire occurrence locations in ecosystems; (b) location of fire and rescue units_ 



<!-- Start of picture text -->
(a) (b)<br><!-- End of picture text -->

101 

2022/78/1 

Environmental Research, Engineering and Management 

Considering the dynamics of fire occurrence in natural ecosystems in Lviv Oblast, in 2019 on the territory of the region, there were 1041 steppe fires, 117 peat fires, and 23 forest fires. The identified number of locations where fires most commonly occur in ecosystems is 555. These locations are plotted on the map of Lviv Oblast ( _Figure 1A)_ . 

According to the analysis of fire occurrence in natural ecosystems, the highest concentration of such fires is observed in the central part of the region, where there is forest-steppe, fewer fires occur in the territory of Lower Polissia predominated by mixed forests, and the least in the Carpathians and their foothills. Therefore, the placement of fire stations must be made taking into account the number of fires and the type of terrain. 

The existing network of fire and rescue units in Lviv Oblast is taken into consideration and is put on the map of Lviv Oblast ( _Figure 1B_ ). 

To date, there are 58 state rescue units in Lviv Oblast, which are marked in blue on the map. There are also 58 local fire crews in Lviv Oblast funded by local governments and marked in red on the map of Lviv Oblast. In the future, according to the memorandum 

on the development of an economically efficient model of civil protection in the region, the establishment of another 25 local fire crews is planned, which are marked in blue in _Fig. 2_ . 

The analysis of the existing fire station locations and those which are planned to be opened showed that the distance from these stations to the sites of fires reaches up to 12 km. Considering the preparation time of the volunteer fire brigade and the time of arrival at the sites of such fires, the total time from receiving the notification to the arrival will exceed the acceptable one. Therefore, it is necessary to analyze the expediency of fire station locations drawing on the example of some areas in Lviv Oblast and using Voronoi diagrams. The Voronoi diagrams split the plane, where each region forms a set of points. It allows us to study the greatest accumulation of fires. The nodes of the cell edges are points that are equidistant from 3 or more (depending on how many edges intersect at this point) origins of fire. It means that in the areas of the biggest concentration of fires at these points, it is necessary to place firefighting equipment in order to respond to fire in a timely manner. 

Fig. 2. _The selection of fire station locations on the example of Sokal district_ 



The optimal fire unit locations on the example of Sokal district are considered ( _Fig. 2_ ). There are 7 existing fire units and 2 planned ones on the territory of Sokal district. However, even this number of fire and 

rescue units is not sufficient to provide rapid response to fires. As we can see, the 3 km radius of departure of existing and expected units covers only 16.2% of the district territory. Therefore, it is necessary to provide 

102 

2022/78/1 

Environmental Research, Engineering and Management 

a further number of fire units considering fire occurrence locations. The best way to do this is to construct a Voronoi diagram, where the vertices of the diagram are the origins of fire, and, consequently, the nodes of the edges are points that are equidistant from the fires and optimal fire station locations. 

Fig. 4. _The selection of fire station locations on the example of Brody district_ 

Thus, by analyzing the example of Sokal district, 7 places for the location of fire stations are identified (marked in yellow in _Fig. 2_ ), except for the existing ones. 

Fig. 3. _The selection of fire station locations on the example of Radekhiv district_ 

Similarly, we considered the fire station locations in Radekhiv district (Fig. 3). There are 6 existing fire units on the territory of Radekhiv district. The 3 km radius of departure of the existing units covers only 14.8% of the territory of the district. Therefore, it is necessary to provide the location of 6 more fire stations, which are marked in yellow in _Fig. 3_ . 

In Brody district, there are 6 fire units. The 3 km radius of departure of the existing units covers only 14.6% of the territory of the district. Hence, 7 more fire stations are needed, which are marked in yellow in _Fig. 4_ . Consequently, using Voronoi diagrams it is possible to define the optimal fire station locations taking into account existing fire-fighting units on any territory. 

103 

2022/78/1 

Environmental Research, Engineering and Management 

Apparently, according to the results of the study, the number of fire brigades in Lviv region should be increased by 2 times. 

## Conclusions 

The results of the study showed that for the selection of fire and rescue unit locations we should take into account the dynamics and fire occurrence locations in natural ecosystems. To ensure fire safety in rural areas and reduce the maintenance cost of these units, it is reasonable to create fire stations, firefighting units, etc. by means of seasonal and part-time work of volunteer firefighters, the use of adapted agricultural machinery or motor trailer pumps for the extinguishment of fires and the like. The study proved that the number of fire and rescue units in Lviv Oblast (Ukraine) is insufficient, since in some cases the distance to the site of a fire is 12 km, and the 3 

km radius of departure of existing units covers less than 20% of the studied areas. The results of the research conducted using Voronoi diagrams determine the optimal locations of these units in Lviv Oblast, and in particular, the fact that the number of units should be doubled. Thus, on the example of 3 districts of the region, the conclusion is the following: in order to respond quickly to fires in ecosystems, it is necessary to create 20 additional fire stations or fire extinguishing bases. 

The algorithm offered in this work can be applied to rural areas in other administrative units, both for a region and for a district. 

The next step in the development of this technique is to determine the amount of equipment and workforce required for extinguishing fires in ecosystems taking into account the anticipated dynamics of these fires and the time of delivery of firefighting means to the site of a fire. 

## References 

Aktaş E., Özaydın Ö., Bozkaya B., Ülengin F. and Önsel Ş. (2013) Optimizing fire station locations for the Istanbul metropolitan municipality. Interfaces 43(3): 240-255. https://doi. org/10.1287/inte.1120.0671 

Bolouri S., Vafaeinejad A., Alesheikh A. and Aghamohammadi H. (2018) The ordered capacitated multi-objective location-allocation problem for fire stations using spatial optimization. ISPRS International Journal of Geo-Information 7(2): 44. https:// doi.org/10.3390/ijgi7020044 

Chen C. and Ren A. (2003) Optimization of fire station locations using computer [J]. Journal of Tsinghua University (Science and Technology) 10: 25. 

Church R. L. and Li W. (2016) Estimating spatial efficiency using cyber search, GIS, and spatial optimization: a case study of fire service deployment in Los Angeles County. International Journal of Geographical Information Science 30(3): 535-553. https://doi.org/10.1080/13658816.2015.1083572 

Das S., McCarter A., Minieri J., Damaraju N., Padmanabhan S. and Chau D. H. P. (2015) ISPARK: Interactive Visual Analytics for Fire Incidents and Station Placement. In ACM SIGKDD Workshop on Interactive Data Exploration and Analytics: 29-36. Degel D., Wiesche L., Rachuba S. and Werners B. (2014) Reorganizing an existing volunteer fire station network in Germany. 

Socio-Economic Planning Sciences 48(2): 149-157. https://doi. org/10.1016/j.seps.2014.03.001 

Dong X. M., Li Y., Pan Y. L., Huang Y. J. and Cheng X. D. (2018) Study on urban fire station planning based on fire risk assessment and GIS technology. Procedia engineering 211: 124-130. https://doi.org/10.1016/j.proeng.2017.12.129 

Donovan G. H. and Rideout D. B. (2003) An integer programming model to optimize resource allocation for wildfire containment. Forest Science 49(2): 331-335. 

Haight R. G. and Fried J. S. (2007) Deploying wildland fire suppression resources with a scenario-based standard response model. INFOR: Information Systems and Operational Research 45(1): 31-39. https://doi.org/10.3138/infor.45.1.31 

Kuzyk A. D. (2008) Analysis of service areas of fire and rescue units using Voronoi diagrams. Fire safety: Collection of scientific works 13: 73-78. 

Murray A. T. (2013) Optimising the spatial location of urban fire stations. Fire Safety Journal 62: 64-71. https://doi. org/10.1016/j.firesaf.2013.03.002 

Pereira P., Mierauskas P., Úbeda X., Mataix-Solera J. and Cerda A. (2012) Fire in Protected Areas - the Effect of Protection and Importance of Fire Management. Environmental Research, Engineering and Management 1(59): 52-62. https://doi. org/10.5755/j01.erem.59.1.856 

104 

2022/78/1 

Environmental Research, Engineering and Management 

Pérez J., Maldonado S. and Marianov V. (2016) A reconfiguration of fire station and fleet locations for the Santiago Fire Department. International Journal of Production Research 54(11): 3170-3186. https://doi.org/10.1080/00207543.2015.1071894 

Okabe A., Boots B., Sugihara K. and Chiu S. N. (2009) Spatial tessellations: concepts and applications of Voronoi diagrams. John Wiley & Sons, New York. 651. 

Sakellariou S., Samara F., Tampekis S., Sfougaris A. and Christopoulou O. (2019) Development of a Spatial Decision Support System (SDSS) for the active forest-urban fires management through location planning of mobile fire units. Environmental Hazards 19(2): 1-21. https://doi.org/10.1080/17477891.2019.1628696 

Tali J. A., Malik M. M., Divya S., Nusrath A. and Mahalingam B. (2017) Location-Allocation model applied to urban public services: Spatial analysis of fire stations in Mysore urban area Karnataka, India. International Journal of Advanced Research and Development 2(5): 795-801. 

Timofeeva S.S., Drozdova T.I., Plotnikova G.V. and Golchevsky V.F. (2013) Physico-chemical bases of development and fire extinguishing. IrGTU, Irkutsk. 178. 

Van der Merwe M., Minas J. P., Ozlen M. and Hearne J. W. (2014) A mixed integer programming approach for asset protection during escaped wildfires. Canadian Journal of forest research 45(4): 444-451. https://doi.org/10.1139/cjfr-2014-0239 

Yang L., Jones B. F. and Yang S. H. (2007) A fuzzy multi-objective programming for optimization of fire station locations through genetic algorithms. European Journal of Operational Research 181(2): 903-915. https://doi.org/10.1016/j. ejor.2006.07.003 

Zhou J. (2014) Research on Layout Optimization Method of Urban Fire Station based on Fire Risk Assessment. In Advanced Materials Research 838: 2162-2169. https://doi.org/10.4028/ www.scientific.net/AMR.838-841.2162 

This article is an Open Access article distributed under the terms and conditions of the Creative Commons Attribution 4.0 (CC BY 4.0) License (http://creativecommons.org/licenses/by/4.0/ ). 
