---
title: 'Deep learning for wildfire risk prediction: Integrating remote sensing and environmental data'
authors:
- Xu, Zhengsen
- Li, Jonathan
- Cheng, Sibo
- Rui, Xue
- Zhao, Yu
- He, Hongjie
- Guan, Haiyan
- Sharma, Aryan
- Erxleben, Matthew
- Chang, Ryan
- Xu, Lincoln Linlin
year: '2025'
journal: ISPRS Journal of Photogrammetry and Remote Sensing
doi: 10.1016/j.isprsjprs.2025.06.002
tags:
- Deep learning
- Remote sensing
- Review
- Risk prediction
- Wildfire
zotero_key: N5PFPRZ5
item_type: journalArticle
url: https://www.sciencedirect.com/science/article/pii/S0924271625002217
source_url: 'unpaywall: https://arxiv.org/pdf/2405.01607'
fulltext_status: fulltext
synced: '2026-11-09'
---

# Deep learning for wildfire risk prediction: Integrating remote sensing and environmental data

## Abstract

Wildfires pose a significant threat to ecosystems, wildlife, and human communities, leading to habitat destruction, pollutant emissions, and biodiversity loss. Accurate wildfire risk prediction is crucial for mitigating these impacts and safeguarding both environmental and human health. This paper provides a comprehensive review of wildfire risk prediction methodologies, with a particular focus on deep learning approaches combined with remote sensing. We begin by defining wildfire risk and summarizing the geographical distribution of related studies. In terms of data, we analyze key predictive features, including fuel characteristics, meteorological and climatic conditions, socioeconomic factors, topography, and hydrology, while also reviewing publicly available wildfire prediction datasets derived from remote sensing. Additionally, we emphasize the importance of feature collinearity assessment and model interpretability to improve the understanding of prediction outcomes. Regarding methodology, we classify deep learning models into three primary categories: time-series forecasting, image segmentation, and spatiotemporal prediction, and further discuss methods for converting model outputs into risk classifications or probability-adjusted predictions. Finally, we identify the key challenges and limitations of current wildfire-risk prediction models and outline several research opportunities. These include integrating diverse remote sensing data, developing multimodal models, designing more computationally efficient architectures, and incorporating cross-disciplinary methods—such as coupling with numerical weather-prediction models—to enhance the accuracy and robustness of wildfire-risk assessments.

## Full text

# Deep Learning for Wildfire Risk Prediction: Integrating Remote Sensing and Environmental Data 

Zhengsen Xu<sup>a,b</sup> , Jonathan Li *<sup>b,c</sup> , Sibo Cheng<sup>d</sup> , Xue Rui<sup>e</sup> , Yu Zhao<sup>f</sup> , Hongjie He<sup>b</sup> , Haiyan Guan<sup>g</sup> , Aryan Sharma<sup>h</sup> , Matthew Erxleben<sup>i</sup> , Ryan Chang<sup>c</sup> , Linlin Xu*<sup>a</sup> 

_aSchulich School of Engineering, Department of Geomatics Engineering, University of Calgary, 2500 University Dr NW, Calgary, T2N1N4, Alberta, Canada bDepartment of Geography and Environmental Management, University of Waterloo, 100 University Avenue, Waterloo, N2L3G1, Ontario, Canada_ 

- _cDepartment of Systems Design Engineering, University of Waterloo, 100 University Avenue, Waterloo, N2L3G1, Ontario, Canada_ 

   - _dCEREA, ENPC, EDF R_ & _D, Institut Polytechnique de Paris, Ile-de-France, France_ 

_eSchool of Emergency Management, Nanjing University of Information Science and Technology, 219 Ningliu Road, Nanjing, 210044, China_ 

_fDivision of Geoinformatics, KTH Royal Institute of Technology, Teknikringen 10a, Stockholm 100 44, Sweden_ 

_gSchool of Remote Sensing and Geomatics Engineering, Nanjing University of Information Science and Technology, 219 Ningliu Road, Nanjing, 210044, China_ 

_hDepartment of Software Engineering, University of Waterloo, 100 University Avenue, Waterloo, N2L3G1, Ontario, Canada_ 

_iDepartment of Management Science and Engineering, University of Waterloo, 100 University Avenue, Waterloo, N2L3G1, Ontario, Canada_ 

## **Abstract** 

Wildfires pose a significant threat to ecosystems, wildlife, and human communities, leading to habitat destruction, pollutant emissions, and biodiversity loss. Accurate wildfire risk prediction is crucial for mitigating these impacts and safeguarding both environmental and human health. This paper provides a comprehensive review of wildfire risk prediction methodologies, with a particular focus on deep learning approaches combined with remote sensing. We begin by defining wildfire risk and summarizing the geographical distribution of related studies. In terms of data, we analyze key predictive features, including fuel characteristics, meteorological and climatic conditions, socioeconomic factors, topography, and hydrology, while also reviewing publicly available wildfire prediction datasets derived from remote sensing. Additionally, we emphasize the importance of feature collinearity assessment and model interpretability to improve the understanding of prediction outcomes. Regarding methodology, we classify deep learning models into three primary categories: time-series forecasting, image segmentation, and spatiotemporal prediction, and further discuss methods for converting model outputs into risk classifications or probability-adjusted predictions. Finally, we identify the key challenges and limitations of current wildfire-risk prediction models and outline several research opportunities. These include integrating diverse remote sensing data, developing multimodal models, designing more computationally efficient architectures, and incorporating cross-disciplinary methods—such as coupling with numerical weather-prediction models—to enhance the accuracy and robustness of wildfire-risk assessments. 

_Keywords:_ Wildfire, Risk Prediction, Remote Sensing, Deep Learning, Review 

## **1. Introduction** 

Wildfires are uncontrolled fires that occur in vegetated landscapes (Huidobro et al., 2024; Glossary of Wildland Fire Terminology, 2006). They can ignite naturally or be caused by human activities and are generally classified into planned fires, which are deliberately set for ecological or experimental purposes, and accidental fires, which result from natural causes or human negligence (Fillmore et al., 2024; Huidobro et al., 2024). Wildfires occur across diverse environments, including forests, grasslands, farmlands, and peatlands, where they play a significant role in shaping global ecosystems. They influence biodiversity, air quality, human health, and carbon balance, with both beneficial and detrimental effects (Moritz et al., 2014; Stojanovic et al., 2016; Bowd et al., 2021; Holder et al., 2023; Lopez et al., 2024). On the one hand, wildfires contribute to ecosystem dynamics by promoting nutrient cycling, facilitating species turnover, and enhancing vegetation regeneration (Bond et al., 2005; Pausas and Keeley, 2019). On the other hand, their uncontrolled occurrence poses substantial risks, including bio- 

diversity loss, air pollution, threats to human settlements, and economic disruptions (Moritz et al., 2014; Bowd et al., 2021; Yang et al., 2022a; Lopez et al., 2024). 

The magnitude of wildfire-related disasters has escalated in recent decades. For instance, the 2019–2020 "Black Summer" wildfires in Australia burned approximately 18.6 million hectares, caused 34 fatalities, destroyed over 5,900 structures, and resulted in an estimated economic loss exceeding $110 billion (Naderpour et al., 2020; Haque et al., 2021). In North America, the 2018 Camp Fire in California led to 85 fatalities and the destruction of nearly 19,000 structures, while the 2023 Maui wildfires resulted in nearly 100 deaths and $550 million in damages (Marris, 2023; Hertelendy et al., 2024). In Canada, wildfire frequency, size, and intensity have been increasing since the mid-20th century due to climate warming (Cunningham et al., 2024; Mulverhill et al., 2024). From 1959 to 2015, the total burned area and the number of large wildfires (over 200 hectares) have significantly risen, and the wildfire season has extended by approximately two weeks (Hanes 

_Preprint submitted to Elsevier_ 

_June 17, 2025_ 

et al., 2019; Jain et al., 2024). The 2023 wildfire season set a record, with 18.5 million hectares burned nationwide, displacing 232,000 people, destroying hundreds of homes, and releasing 647 Tg C into the atmosphere (Erni et al., 2024; Byrne et al., 2024; Jain et al., 2024). Investigations suggest that climate change will further shorten fire return intervals and expand burned areas in vulnerable regions (Parks and Abatzoglou, 2020; Holdrege et al., 2024). 

In response to these challenges, wildfire risk prediction has garnered increasing attention from governments, academia, and industry. Risk prediction involves delineating research scope, selecting and processing data, establishing methodologies, and understanding predictions. Despite the growing reliance on machine learning for wildfire risk prediction, a systematic review of these components remains lacking. This paper addresses this gap by providing a comprehensive review of the multi-source data and deep learning methods used in wildfire risk prediction, with a particular emphasis on feature attribution techniques and emerging deep learning models. 

First, wildfire ignition and spread result from complex interactions among multiple factors, including fuel conditions, climate, weather, socio-economic variables, terrain, hydrology, and historical wildfire occurrences (Fuller, 1991). This study systematically examines the definitions, proxies, frequency of use, and calculations (see Appendix) of these features, alongside an overview of publicly available datasets relevant to wildfire prediction. 

Second, an essential consideration in wildfire risk modeling is the evaluation of feature collinearity and model interpretability. Highly correlated features can obscure individual contributions and degrade model performance, especially for linear models (Li et al., 2022a), while model interpretability enhances the understanding of ignition and spread dynamics (Abdollahi and Pradhan, 2023). This paper introduces key techniques for assessing collinearity and improving interpretability in machine learning-based wildfire models. 

Third, the development of predictive algorithms varies widely, ranging from traditional wildfire danger rating systems and statistical models to modern machine learning and deep learning approaches. While previous studies have reviewed conventional machine learning techniques (Jain et al., 2020), this paper focuses on deep learning, which has seen rapid adoption and is emerging as a crucial tool for wildfire prediction. We categorize deep learning-based models into three primary task types: time-series forecasting, image segmentation and classification, and spatiotemporal prediction. A structured review of these models is presented, highlighting their applications and limitations. 

Finally, integrating multi-source geospatial data with deep learning models for wildfire risk prediction presents both opportunities and challenges. This paper discusses the limitations of existing algorithms and explores potential advancements in multimodal and architecturally efficient models, as well as the possible potential of new data sources (such as microwave, LiDAR, and nightlight data) and cross-domain weather forecasting models. The fusion of these diverse datasets with deep learning techniques has the potential to enhance predictive ac- 



Figure 1: The generalized wildfire risk framework proposed by Miller and Ager (2012) 

curacy and improve early warning systems. Given the increasing wildfire risk under climate change, developing robust, interpretable, and computationally efficient models is crucial for informing mitigation strategies, resource allocation, and adaptive management policies (Erni et al., 2024; Mulverhill et al., 2024). 

## **2. Wildfire Risk Definition** 

In the majority of published wildfire risk methodology studies, the concept of wildfire risk is not clearly defined, leading to instances of confusion regarding the interchangeable use of terms such as risk, hazard, and danger. Consequently, this paper initiates by presenting a definition of wildfire risk. Miller and Ager (2012), based on the Society for Risk Analysis’s definition of risk, proposed a comprehensive fire risk framework (Fig. 1), which divides wildfire risk into three components: likelihood, intensity, and effects. This framework emphasizes the impact of wildfires on human activities and the environment rather than solely considering the probability of occurrence. For instance, low-intensity and low-impact wildfires might not significantly affect areas of concern, meaning that a high likelihood of wildfire occurrence does not necessarily equate to high wildfire risk. Notably, this framework does not explicitly incorporate the stochastic ignition caused by topographic and socioeconomic factors, which slightly diverges from the trends observed in the latest research. 

Additionally, their study distinguishes between commonly used terms in wildfire risk research, such as risk, hazard, exposure, threats, vulnerability, and fire danger. When summarizing related work, we focus only on studies concerning wildfire risk 

2 

and danger, excluding those on hazard, exposure, and threats. The former primarily describes the outlook for fire occurrence over a certain period, while the latter tends to evaluate the hazard of wildfires (Fig 1). 

Consequently, if wildfire risk is defined solely based on the likelihood of fire occurrence without accounting for its potential harm, it can be simplified to the probability of wildfire ignition or spread at a given location and time (Deeming, 1972). This interpretation aligns with the approach taken by many past studies, where risk has often been described as the probability of wildfire occurrence. Moreover, this definition is consistent with the wildfire risk framework established by the European Commission (Depicker et al., 2020). 

More specifically, these studies often treat wildfire risk assessment as a conditional probability, where wildfire risk is defined as the probability of a wildfire igniting or spreading under the influence of factors such as fuel, terrain, and weather conditions. In this context, wildfire risk equates to wildfire probability (Yang et al., 2004). In addition, some definitions emphasize the role of causal agents and their frequency in influencing wildfire risk (Hardy, 2005). The importance of "causal agents" is highlighted—without these agents, the existing hazard would have zero potential to cause harm. Causal probability refers to the conditions that trigger wildfires, such as lightning or human activities (Deeming, 1972). 

Based on these definitions, the specific form of wildfire risk varies across studies. This paper categorizes wildfire risk definitions into four types based on the algorithms used and the research objectives: explicit definitions, implicit definitions, wildfire ignition risk, and wildfire burning risk. On the one hand, definitions are categorized according to whether they explicitly represent various wildfire influencing factors and the contributions of historical wildfire records. These categories include explicit definitions based on historical observed wildfire occurrence data, influencing factors, and simulation data, as well as data-driven machine learning implicit definitions. On the other hand, wildfire prediction research is generally divided into studies on wildfire ignition risk and wildfire burning risk. Wildfire ignition risk is typically estimated using ignition data, while wildfire burning risk refers to the risk of a fire encountering a particular place. Although this risk partly depends on ignition, it is also influenced by subsequent wildfire spread and fire suppression efforts and is generally derived from historical burn data or simulation methods (Miller and Ager, 2012). 

In this survey, it is important to note that the aforementioned definitions of wildfire risk differ from the concept of wildfire detection. Wildfire risk refers to the probability of a wildfire occurring, whereas wildfire detection focuses on identifying already ignited wildfires. Nevertheless, accurate wildfire detection can provide valuable insights for wildfire risk prediction, particularly by serving as historical fire occurrence data for constructing risk assessment or prediction models. Additionally, near-real-time wildfire detection (Hu et al., 2024; Zhang et al., 2024b) can offer crucial guidance for predicting fire spread and ignition risk. 

## _2.1. Explicit and Implicit Definition Methods_ 

This subsection focuses on explicit definition methods, which include directly using historical observation data to define wildfire risk, defining wildfire risk based on the weights of influencing factors, and combining these factors to simulate wildfire distribution and define risk through simulation results. It is worth noting that this subsection does not cover the details of the simulation algorithms, but rather how to convert simulation results into wildfire risk. 

Firstly, the simplest and most direct method in wildfire risk estimation is using historical fire occurrences to predict future risk. For example, Rubí and Gondim (2023) classified regions where one or more fires occurred within an hour as "high risk," while other areas were classified as "low risk." Similarly, Umunnakwe et al. (2022) estimated the spatiotemporal ignition probability using a similar function. 



<!-- Start of picture text -->
mg ,  j ≈ ng ,  j (1)<br>N<br><!-- End of picture text -->

where _mg_ , _j_ represents the fire ignition probability in grid cell _g_ during period _j_ ; _ng_ , _j_ and _N_ are the total number of wildfires and the total number of considered periods, respectively. Lall and Mathibela (2016) assessed wildfire risk in Cape Town, South Africa, by defining daily risk ratings based on the average number of wildfires per day and their corresponding standard deviation over seven years. Specifically, fire occurrences below the average were rated as 1 or lower, those between the average and one standard deviation above were rated as 2 or moderate, those between one and two standard deviations above were rated as 3 or higher, and occurrences more than two standard deviations above the average were rated as 4 or extreme. An artificial neural network (ANN) model was then established using temperature, humidity, wind speed, and precipitation as inputs to predict wildfire risk. 

The above models based on historical data do not consider the conditions for wildfire ignition or spread, thus having poor robustness and generalization ability. Consequently, some studies have begun to incorporate or solely use factors such as fuel, terrain, weather conditions, and wildfire triggers as proxies to estimate ignition risk. Essentially, these methods can be defined as the contributions of various drivers to wildfire occurrence at specific times and locations. For example, Castro et al. (2003) used shrub moisture content, specifically live fuel moisture, as a proxy variable for wildfire risk in Spain. More complexly, the probability of wildfire occurrence can be defined as a conditional probability, representing the likelihood of a wildfire occurring given specific temporal, spatial, and environmental influencing factors. A typical example is the logistic model proposed by Preisler et al. (2004): 



<!-- Start of picture text -->
exp(θ x , y , t )<br>p 1 = Prob( Nx , y , t = 1| Ux , y , t ) = (2)<br>1 + exp(θ x , y , t )<br><!-- End of picture text -->

where _Nx_ , _y_ , _t_ and _Ux_ , _y_ , _t_ represent, respectively, whether a wildfire occurs and the collection of explanatory variables at location ( _x_ , _y_ ) and time _t_ . θ _x_ , _y_ , _t_ is a parameter estimated based on the explanatory variables, incorporating spatial and temporal dependencies. Considering the spatial, temporal, and nonlinear 

3 

correlations of the explanatory variables, θ _x_ , _y_ , _t_ can be expressed as a combination of linear and nonlinear terms: 



<!-- Start of picture text -->
θ x , y , t = logit( p 1 k ) = fuel k  +  g 1( xk ,  yk ) +  g 2(day k ) +  g 3(elev k )<br>+  g 4(BI k ) +  g 5(FP k ) +  g 6(KB k ) +  g 7(TH k )<br>+  g 8(Wspeed k ) +  g 9(RH k ) +  g 10(DBT k )<br>+ Weather<br><!-- End of picture text -->



<!-- Start of picture text -->
(3)<br><!-- End of picture text -->

here, _gi_ (·) are nonparametric smoothing functions, typically estimated through generalized additive models, to capture nonlinear relationships. Variables such as fuel _k_ and elev _k_ represent explanatory factors, including fuel models, weather conditions (e.g., relative humidity, temperature), and fire danger indices (e.g., Burning Index (BI), Fire Potential Index (FP)), while ( _xk_ , _yk_ ) are spatial coordinates, with _g_ 1( _xk_ , _yk_ ) as a bivariate smoothing function for spatial nonlinear effects. In this context, _k_ denotes a unique spatiotemporal unit, corresponding to a specific location ( _x_ , _y_ ) and time _t_ , representing an individual voxel (e.g., a 1 km<sup>2</sup> grid cell) and a specific day where wildfire occurrence probability is modeled. 

Several other models have been employed to quantify the relationships between wildfire drivers and wildfire risk as well. For example, Sadasivuni et al. (2013) defined wildfire risk as the interaction between human activity and fuel distribution, integrating population and fuel layers through additive operations as inputs for a gravity model within a spatial interaction framework, with predictions classified into five risk levels. Similarly, Gentilucci et al. (2024) used a weight-of-evidence model to categorize wildfire drivers and classify wildfire risk into low and high levels based on regression of factor weights. Additionally, Oliveira et al. (2021a) and Bergonse et al. (2021) classified land use, land cover, slope, elevation, and aspect, calculated likelihood ratios for each category, and assessed fire susceptibility by summing weighted values across categories. This process can be mathematically expressed as follows: 



<!-- Start of picture text -->
Lri = N S i i / / N S , (4)<br> Lr j = � i n =0 XijLri<br><!-- End of picture text -->

where _Lri_ represents the likelihood ratio of the variable corresponding to category _i_ ; _S i_ and _S_ represent the number of burning pixels associated with category _i_ and the total number of burning pixels; _Ni_ and _N_ represent the number of pixels belonging to category _i_ and the total number of pixels in the study area; the total likelihood ratio _Lr j_ of each grid cell _j_ is obtained by summing the _Lri_ values of all _n_ variables. Similarly, South Africa’s official wildfire danger rating system, the Lowveld model (Meikle and Heine, 1987; Lall and Mathibela, 2016), defines wildfire risk using the burning index, wind correction factor (WCF), and rain correction factor (RCF), where BI is a function of dry-bulb temperature (T) and relative humidity (RH): 



<!-- Start of picture text -->
BI = (( T − 35) − ( 35 30 − T )) + ((100 − RH ) × 0.37) + 30<br>(5)<br>FDI = ( BI  +  WCF ) ×  RCF<br><br><!-- End of picture text -->

here, FDI refers to the fire danger index, while WCF and RCF are specified in Notice 1099 of 2013, issued in compliance with South Africa’s National Veld and Forest Fire Act (Department of Agriculture Forestry and Fisheries South Africa, 2013). Srivastava et al. (2014) differed from the aforementioned studies by simultaneously considering both causal and anti-causal factors, including the distribution of check dams, firelines, and fire water towers, using an expert knowledge system to quantify the likelihood of forest fires. 

Simulation methods based on the above influencing factors are also commonly used in wildfire risk modeling. For instance, Ager et al. (2010) utilized the minimum travel time (MTT) fire spread algorithm, calculating the burn probability of each pixel through the burn frequency in 10,000 simulations. The simulation results defined wildfire risk as burn probability. Similarly, Salis et al. (2021) used MTT but calculated burn probability through a combination of different simulation results rather than frequency. Ujjwal et al. (2022) used the Spark model and parameters such as temperature, relative humidity, wind speed, and wind direction to model wildfire risk in Tasmania, Australia, defining risk categories as low or high based on the spread area of wildfires at different locations. Another typical example of a simulation method is the Monte Carlo algorithm. For example, Adhikari et al. (2021) defined wildfire risk through the overlap of multiple Monte Carlo algorithm predictions. Specifically, they predicted wildfire boundaries within 30 hours of ignition under various random weather and fuel moisture conditions using the Monte Carlo algorithm. The spatial overlap of all Monte Carlo predictions then generated risk levels. 

On the other hand, wildfire ignition and spread are highly random and exhibit a strong nonlinear relationship with various factors (Leuenberger et al., 2018). Data-driven machine learning methods are frequently employed in wildfire risk prediction research due to their capability to effectively model nonlinear functions using large-scale datasets (Jain et al., 2020). While these methods are powerful for prediction, they do not explicitly quantify the contribution of individual factors to overall wildfire risk, unlike the explicit definition methods discussed earlier. As a result, they are classified as implicit definition methods. Further details on these methods will be provided in Section 6. 

It is important to note that the wildfire risk defined by these machine learning models represents a pseudo-probability rather than a true probability density (Pelletier et al., 2023). This pseudo-probability arises from the models’ limitations in explicitly defining risk. For example, in XGBoost, the predicted pseudo-probability is derived from the inverse log transformation of the sum of terminal leaf weights. In SVM, it is estimated by calculating the distance to the classification decision boundary and using these distances for probability estimation. In Random Forest, it is the average of the voting outcomes from multiple decision trees. For models such as Multilayer Perceptron (MLP), Long Short-Term Memory (LSTM), and Convolutional Neural Network (CNN), it is typically the probability estimate from the activation function of the final layer. 

In addition to the influence of method selection on predicted probabilities, these models are highly sensitive to the construc- 

4 

tion of the label sample set. Various preprocessing strategies—such as historical resampling of wildfire data—can substantially affect the resulting probability estimates. Therefore, it is essential to first establish a clear definition of wildfire risk rather than relying solely on binary labels. Furthermore, the application of post-processing techniques, such as linking explicit and implicit definitions of risk, can improve both the interpretability and accuracy of model outputs. This aspect will be further discussed in Section 6.1. 

## _2.2. Wildfire Ignition and Burning Risk_ 

Wildfire ignition refers to the first occurrence of a fire event during a wildfire. According to Badia-Perpinyà and PallaresBarbera (2006), to combat forest fires most effectively, the importance of assessing wildfire ignition risk should be emphasized. Similarly, Catry et al. (2009) highlighted that it is not sufficient to consider only factors influencing wildfire spread and suppression difficulty, such as fuel, weather, and terrain. They cited the definitions provided by the Food and Agriculture Organization and the Glossary of Wildland Fire Terminology, which define wildfire risk as fire ignition risk, meaning "the chance of a fire starting as determined by the presence and activity of any causative agent." Furthermore, estimating wildfire ignition risk is crucial for wildfire management, as it guides decisions related to fuel treatment and the allocation of suppression resources. Generally, wildfire ignition risk can be modeled using historical ignition data (Miller and Ager, 2012) and used to generate broader or spatially continuous ignition risk maps. Therefore, the following section will focus on how various studies have identified or defined ignition points and converted these records into probability values or modeled dependent variables. 

In the study of wildfire ignition risk in Central Spain, Romero-Calcerrada et al. (2008) utilized wildfire records provided by the Sección de Defensa Contra Incendios Forestales of the Madrid regional government. These records included the coordinates of ignition points, land cover of the burned area, and the time of the fire. The researchers then defined the probability of wildfire ignition during the fire season as a prior probability and calculated the posterior probability based on this prior probability. Finally, they generated predicted wildfire risk levels by comparing the ratio of prior to posterior probabilities. 

In the study by Catry et al. (2009), they first cleaned and corrected a dataset of 137,204 ignition points selected from the official wildfire dataset provided by Portuguese Forest Services, ultimately retaining 127,409 fire ignition locations. To construct a balanced dataset, they randomly selected a number of non-ignition points across the country, 1.5 times the number of fire ignition locations. The ignition and non-ignition points were then encoded as binary variables, forming the final dependent variable dataset for fire ignition. The researchers used frequency analysis and the natural breaks method to convert the historical fire locations dataset into observed and expected frequencies, which were used to train a logistic regression model. In this model, the expected frequency of fire ignition was calculated proportionally to the land area of each observed frequency interval. The output of the logistic regression model was classified into six risk levels. Similarly, Ager et al. (2014b), in their 

study of wildfire ignition and burning risk in Sardinia, Italy, and Corsica, France, defined the dependent variable of their regression model as the frequency of wildfire ignition on a daily basis, using wildfire ignition area as a condition for burning risk. It is noteworthy that ignition points in Corsica were assumed to be the centroids of burned areas. Braun et al. (2010) used forest inventory data from Ontario’s Ministry of Natural Resources to identify wildfire ignition areas and employed generalized additive models, coordinate offsets, and cubic spline interpolation to generate spatially continuous wildfire ignition probability maps, i.e., risk maps. 

In the study of wildfires in Belgium, Depicker et al. (2020) defined the probability of wildfire occurrence in a given area as the average probability of ignition within a calendar year: 



<!-- Start of picture text -->
P ( I | Ci ) = P ( I ) P ( Ci | I ) (6)<br>P ( Ci )<br><!-- End of picture text -->

where _P_ ( _Ci_ ) and _P_ ( _Ci_ | _I_ ) represent the ratio of the area of ignition unit _Ci_ to the total study area and the ratio of the number of ignitions to the total study area, respectively, while _P_ ( _I_ | _Ci_ ) denotes the ratio of the number of ignitions to the number of units over a one-year span. To mitigate the issue of class imbalance, smaller areas were merged into larger ones: 



<!-- Start of picture text -->
PA = 1 − � n i =1 (1 − P ( I | Ci )) Ni (7)<br><!-- End of picture text -->

where _n_ and _Ni_ represent the number of environments within a larger area _A_ and the number of grid cells within environment _i_ , respectively. In the study of wildfire ignition risk in Galicia, Spain, Calviño-Cancela et al. (2017) analyzed the differences between historical ignition points obtained from the Spanish Forest Fire Statistics and an equal number of randomly selected locations, examining the relationships between wildfire occurrences and factors such as the wildland-urban interface (WUI), land use/land cover (LULC), and elevation. Similarly, Ying et al. (2021), in their analysis of wildfire ignition causes in Yunnan Province, China, used historical records from the Yunnan Forestry Bureau for the period 2003-2015. These records, like those in previous studies, included information on the date, location, size, and cause of each ignition. In total, 5,145 ignition events were recorded, and approximately 1.5 times as many non-ignition points were randomly selected. The relationship between wildfire risk and influencing factors was modeled based on the presence or absence of ignition, rather than frequency. 

It is important to note that the studies mentioned above utilized ground-based wildfire databases rather than the more commonly used MODIS or VIIRS fire/hotspot data in wildfire risk prediction research. This may be due to the relatively low spatiotemporal resolution of these data, making it difficult to detect ignition points with very low intensity and duration. Benali et al. (2016); Barber et al. (2024) compared the consistency of wildfire field records in Portugal, Greece, Alaska, California, and southeastern Australia with MODIS active fire products (MCD14ML). They proposed a clustering algorithm to calculate the ignition and end dates of a wildfire in the MCD14ML product and used the Nash–Sutcliffe Model 

5 



Figure 2: The spatial distribution of included research. 

Efficiency Index to estimate the consistency between satelliteestimated fire dates and ground records. The study found that satellite data could not estimate the start and end dates of most fires smaller than 500 ha. Similarly, Coskuner (2022) compared the performance of MODIS and S-NPP VIIRS active fire or hotspot detection products—specifically, MCD14ML V6 and VNP14IMG—in detecting wildfires across five different land cover types in Turkey. These detections were compared with records from Turkey’s ground-based wildfire database. The authors found that both MODIS and VIIRS had very low detection capabilities for small fires (<1 ha) (<3.5%). They also cited studies by Fusco et al. (2019) and Ying et al. (2019) showing that MODIS fire products had high omission rates in the United States and China. Specifically, Fusco et al. (2019) reported detection rates for MODIS products in the United States ranging from 3.5% to 23.4%, with detection rates increasing with fire size. Similarly, Ying et al. (2019) found that in Yunnan Province, China, only 11.10% of 5,145 ground-recorded wildfire events were detected by MODIS fire products, with most omissions attributed to the small size of the fires. These analyses suggest that the commonly used MODIS and VIIRS fire and hotspot products are not suitable for estimating ignition locations and events, nor for corresponding ignition risk estimation. 

In contrast to wildfire ignition risk, wildfire burning risk is more broadly defined as the risk of a fire encountering a particular location, influenced by both ignition and spread. Therefore, most studies do not distinguish between ignition and spread when defining wildfire burning risk but consider both simultaneously. In general, there are two methods for defining wildfire burning risk: using historical burn data through explicit or implicit methods, or defining it based on simulation or spread models (Finney, 1998, 2002; Scheller et al., 2007; Miller et al., 2008; Tolhurst et al., 2008; Tymstra et al., 2010; Chen et al., 

2024c). These methods have been discussed in the previous sections of this chapter, so they will not be repeated here. It is important to note that in choosing between these two methods, Miller and Ager (2012) suggest that for smaller fire extents (e.g., 1-10 hectares), ignition risk assessment can accurately reflect the likelihood of fire occurrence. However, for larger fire extents (e.g., 20-50 _km_<sup>2</sup> ), it is necessary to consider using burning risk to represent wildfire risk. 

## **3. Research Area distribution** 

This paper reviews 138 recent wildfire risk prediction studies conducted globally using data-driven methods. Figure 2 illustrates the geographic distribution and quantity of these studies. Among these, 18 studies address global-scale wildfire risks, while 6 focus specifically on the Mediterranean basin. 

At the continental scale, North America and Asia exhibit the highest levels of research activity. In North America, the United States accounts for 71 studies, followed by Canada with 11. In Asia, China leads with 18 studies, followed by Iran and India with 14 and 6 studies, respectively. In Europe, wildfire research is concentrated in the western and southern regions, with notable contributions from Spain, Portugal, Greece, and France, while smaller-scale studies have been conducted in Italy, Sweden, Serbia, and Turkey. In contrast, Africa has seen limited wildfire research, with only one study each from South Africa, Algeria, Morocco, and Senegal. Similarly, South America contributes minimally, with one study each from Brazil and Chile. In Oceania, research is dominated by Australia, which accounts for 18 studies, while no other countries in the region are represented. 

The geographic concentration of wildfire research raises critical questions about whether these efforts align with global 

6 

wildfire trends, particularly in terms of frequency, burned area, and carbon emissions. Africa, often referred to as the "continent of fire," has accounted for 70% of the global burned area over the past two decades, contributing approximately 29% of global carbon emissions (Giglio et al., 2013, 2018; de Oliveira-Júnior et al., 2024). Despite its prominence, Africa remains underrepresented in wildfire risk prediction studies, as shown in Figure 3. Similarly, South America, which contains approximately 864 million hectares of forest—accounting for 21% of the global forest area and 57% of the world’s primary forests (Food and Agriculture Organization of the United Nations (FAO), 2011; Keenan et al., 2015)—has experienced a rising trend in wildfire frequency and burned area. This increase is primarily driven by deforestation and climate change. During the 2023–2024 wildfire season, the Amazon region, encompassing Brazil, Bolivia, Peru, and Colombia, experienced historically high burned areas, particularly in Amazonas, Loreto, La Paz, and Beni. Fire activity in June and October 2023 was the highest recorded since 1998. Southern South America, including Chile, also recorded significant wildfire activity during the same season. The burned area exceeded 4,000 square kilometers, marking the second largest in 20 years (Jones et al., 2024a). Despite these critical developments, data-driven wildfire research in South America remains sparse, as shown in Figure 3. 

In northern boreal regions, Canada has been a focal point of wildfire research. However, studies on wildfire risk in Russia remain scarce, despite estimates suggesting that Siberian wildfire emissions surpass those of Canada (de Groot et al., 2013). Between 1998 and 2010, Russia’s average annual burned area and carbon emissions were 8.23 million hectares and 121 teragrams of carbon per year, respectively (Shvidenko et al., 2011). Recent studies indicate a growing prevalence of high-intensity, late-season fires in Siberian boreal forests, including the Arctic, with projections suggesting annual fire emissions may reach 325 teragrams of carbon by 2027 (Ponomarev et al., 2023). These findings underscore the urgent need to advance wildfire risk prediction in Russia’s northern regions. 

In conclusion, the geographic distribution of wildfire research highlights significant disparities. While North America and Asia dominate wildfire studies, critical regions such as Africa, South America, and parts of Russia remain underrepresented. Addressing these gaps is vital to reducing geographic inequalities and advancing climate justice (Jones et al., 2024b). Expanding research to underrepresented regions, fostering cross-regional studies, and strengthening international collaboration are crucial to understanding wildfire behavior across diverse ecosystems and climates. Additionally, the reliance on localized datasets limits the generalizability of existing predictive models. Future efforts should prioritize the development of unified data platforms, facilitate open data sharing, and rigorously validate models across diverse regions to enhance their reliability and applicability. 

## **4. Data** 

Essentially, wildfires are uncontrolled processes involving the continuous combustion of organic matter in landscapes 

(Duff et al., 2017). The ignition and burning processes of wildfires are influenced by factors such as fuel conditions, meteorological and climatic conditions, human interventions, topographical and hydrological characteristics, and historical wildfire occurrences (Fuller, 1991). Therefore, in this section, the data used in wildfire risk prediction are categorized into these types, and their components, definitions, and proxy methods are introduced. 

It is important to note that most existing wildfire risk prediction studies rely on proxies, which can only indirectly reflect the state of driving factors. Therefore, in Section 8, we provide an overview of recent advancements in the calculation methods for these driving factors, with a particular focus on fuel conditions. 

## _4.1. Fuel Conditions_ 

Duff et al. (2017) suggests that wildfire behavior is largely dependent on the characteristics of the fuel that sustains it. Unlike other factors influencing wildfire ignition and spread, such as meteorological conditions, climate, topography, and hydrology, fuel can be more easily controlled (Chuvieco et al., 2012). Some studies even propose that fuel is the only landscape element that can be managed to directly affect fire behavior (Thompson et al., 2013; Fernandes and Botelho, 2003), emphasizing the importance of fuel conditions in wildfire risk evaluations. Fuel refers to any combustible material, including live and dead vegetation (McLauchlan et al., 2020; Leite et al., 2024), with four main variables affecting wildfire: Fuel Moisture Content (FMC), fuel load, fuel type, and fuel continuity. These parameters directly influence fire ignition, intensity, and spread rate. 

## _4.1.1. Fuel Moisture Content_ 

FMC refers to the ratio of the weight of water to the dry weight of a sample, as shown in Eq. 8 (Mbow et al., 2004; Chuvieco et al., 1999). FMC can be divided into Live Fuel Moisture Content (LFMC) and Dead Fuel Moisture Content (DFMC), both critical for determining fuel combustibility (Yebra et al., 2013b). 



<!-- Start of picture text -->
FMC = Wei Dry weight of the sample ght of water in sample × 100% (8)<br><!-- End of picture text -->

LFMC is influenced by plant ecophysiological factors and environmental conditions such as soil moisture and humidity, which regulate water uptake and transpiration (Castro et al., 2003). DFMC, on the other hand, is determined by fuel size, weather, and microclimate (Nolan et al., 2016), as well as the fuel’s biochemical composition (Viney, 1991). Dead fuel, unlike live fuel, cannot regulate moisture actively and reaches an equilibrium with the surrounding atmosphere known as Equilibrium Moisture Content (EMC). The time needed to reach EMC depends on the fuel size, which is classified into fine fuels like twigs and leaves (1-hour fuels), coarser branches (10-hour and 100-hour fuels), large trunks (1000-hour fuels), and surface litter (Catchpole et al., 2001). Soil moisture is also considered in some cases (Rothermel et al., 1986). DFMC plays a crucial 

7 

role in fire ignition and rapid spread early in the fire season, while LFMC significantly impacts the persistence and spread of fires. 

It is important to note that estimating FMC remains a significant challenge due to the complexity of real-world conditions. For example, accurately isolating the effects of vegetation dry matter, soil moisture, and atmospheric and canopy structural interference on backscatter, optical reflectance, and emissivity remains difficult. Additionally, the availability of in situ FMC measurements is still limited, with sparse spatial distribution, which constrains the development of data-driven algorithms. 

To address these challenges, practical wildfire risk prediction systems often employ proxy parameters to represent DFMC and LFMC. For DFMC, these proxies include drought indices such as the Keetch-Byram Drought Index, meteorological variables like temperature and relative humidity, and composite indices such as the Fire Weather Index (FWI). These alternatives are easier to obtain and integrate into predictive models, while still capturing the indirect effects of DFMC on fire behavior (Vitolo et al., 2020; Rothermel et al., 1986). 

For LFMC, proxy parameters such as vegetation indices (e.g., NDVI and its variants), meteorological variables (e.g., fuel moisture code, meteorological drought indices, and temperature), and composite indices (e.g., the Fire Weather Index) are commonly used, as shown in Figure 3. These proxies provide easier-to-obtain and more consistent inputs while indirectly capturing LFMC’s influence on wildfire behavior, thus offering a practical alternative for large-scale, long-term modeling efforts (Chuvieco et al., 2002; Dasgupta et al., 2007; Ruffault et al., 2018; Vinodkumar et al., 2021a; Krueger et al., 2022; Balaguer-Romano et al., 2022; Guk et al., 2024). 

## _4.1.2. Fuel Load_ 

Fuel load refers to the amount of combustible biomass available per unit area which influences wildfire intensity and spread (McNorton and Di Giuseppe, 2024). It can be classified as live or dead, or by size into fine fuels (e.g., grass, shrubs, twigs) and coarse fuels (e.g., trunks, logs) (Gould et al., 2011). Dead fine fuel plays a critical role in fire ignition and spread, while canopy fuel load fuels crown fires, increasing both fire intensity and spread rate (Cruz et al., 2003; Arellano-Pérez et al., 2018; Walker et al., 2020). Fuel load measurements are typically obtained through direct sampling, physical models, or remote sensing techniques. The integration of SAR, LiDAR, and multispectral data has significantly enhanced the accuracy of fuel load estimation. 

In practical wildfire risk prediction, directly estimating fuel load is often challenging due to its inherent complexity and data limitations, which may lead to inaccurate estimations. Consequently, the use of proxies rather than direct fuel load estimation is more common in wildfire risk prediction, as it simplifies the process and avoids the accumulation of errors. 

First, due to its definitional similarity to fuel load, particularly its emphasis on above-ground biomass, some studies have employed above-ground biomass as a proxy for fuel load (Eames et al., 2021; Vega et al., 2022; McNorton and Di Giuseppe, 2024). Additionally, other studies have utilized 

alternative proxies for fuel load. For instance, Su et al. (2021), in their study on wildfire driving factors in certain tropical rainforest regions of southern China, used fractional vegetation cover (FVC) as a proxy for fuel load. FVC represents the percentage of an area covered by green vegetation relative to the total statistical area. In practical applications, MODIS NDVI products are often used as proxies for FVC. Furthermore, Helman et al. (2015) applied time-series analysis to MODIS NDVI data to distinguish between woody and herbaceous vegetation in Mediterranean forest regions. Their findings suggested that the long-term mean woody NDVI and its trend could serve as alternative indicators for wildfire fuel assessment. 

## _4.1.3. Fuel Types_ 

Fuel types categorize fuels based on shared characteristics, such as vegetation type, canopy height, fuel load, and biomass, which influence wildfire behavior under specific conditions (Arroyo et al., 2008). Classification systems for fuel types vary globally. For instance, the U.S. National Fire Danger Rating System (NFDRS), Northern Forest Fire Laboratory (NFFL), and Canada’s Fire Behaviour Prediction (FBP) system are widely used for wildfire risk prediction and management (Cohen, 1985; Albini, 1976; Group et al., 1992). 

Table 1 presents a comparison of major fuel classification systems. The NFDRS includes 20 fuel types, NFFL defines 13 types, and the U.S. Fuel Characteristics Classification System (FCCS) has 216 fuel types. In Australia, McArthur’s system categorizes fuel into three types, while the FBP system in Canada uses 16 fuel types. The Prometheus system, applied in Mediterranean Europe, defines seven types (Arroyo et al., 2008). 

Table 1: Comparison of Fuel Classification Systems (Arroyo et al., 2008) 

|**Fuel classification system**|**Number of fuel types**|**Country of application**|
|---|---|---|
|NFDRS fuel types|20|USA|
|NFFL fuel types|13<sup>a</sup>|USA|
|FCCS|216<sup>b</sup>|USA|
|McArthur fuel types|3|Australia|
|FBP fuel types|16|Canada|
|Prometheus fuel types|7|Europe<sup>c</sup>|



> a Option of developing custom fuel types. 

> b New fuelbeds added periodically. 

> c Mediterranean countries. 

In addition to the detailed classification of fuel types, most wildfire risk assessment studies based on multi-source remote sensing data utilize simplified LULC maps as proxies for fuel type to analyze the influence of different land cover types and human activities on wildfire risk. For instance, Jaafari et al. (2019) employed logistic regression to assess the influence of various explanatory variables—including topography, elevation, Topographic Wetness Index (TWI), meteorological factors, and land use—on wildfire risk in the Zagros ecological zone of western Iran. The study identified land use as the most significant factor, with dry farmland and forests being the areas most susceptible to wildfires. Moreover, the type and continuity of vegetation were found to be critical determinants of large fire occurrences. 

8 

Similarly, Ager et al. (2014b) analyzed wildfire occurrence and scale in Sardinia (Italy) and Corsica (France). Their research revealed that, at the beginning of the the fire season, the probability of large fires occurring in agricultural lands in southern Sardinia was ten times higher than in forested and shrubland areas near roads. However, as the fire season progressed, the latter exhibited a higher wildfire probability. Conversely, Calviño-Cancela et al. (2016) investigated the relationship between WUI and LULC in northern Spain and found that primary forests and agricultural areas exhibited the lowest wildfire risk. 

Likewise, Donovan et al. (2020) considered five land use types—grasslands, woody vegetation, croplands, rangelands and hayfields, and developed areas—in an assessment of wildfire occurrence risk in the Great Plains ecoregion of the United States. Their findings indicated that woody vegetation and grasslands were most prone to both wildfire ignition and large fires, whereas other land use types exhibited lower susceptibility. Among them, croplands had the lowest probability of large fires, and as crop coverage increased, the likelihood of large fire occurrences decreased. 

## _4.1.4. Fuel Continuity_ 

Since fire lines spread both horizontally and vertically, fuel continuity is generally considered in terms of both vertical and horizontal directions. Vertical canopy continuity primarily refers to the vertical structure of fuels, also known as ladder fuels. These are composed of low-lying shrubs, seedlings, upper canopy trees, and intermediate understory vegetation. In areas where vertical fuels are present, this structure can cause low-intensity surface fires to escalate into severe crown fires (Agee and Skinner, 2005; Menning and Stephens, 2007). There has been significant research on ladder fuels, including methods for precise field measurements of fuel structure (Kilgore and Sando, 1975; Pye et al., 2003) and approaches combining field measurements with expert knowledge (Menning and Stephens, 2007). However, due to the complexity of field measurement, the more common proxy for vertical fuel continuity is the estimation of canopy base height (CBH) (Scott, 2001). 

CBH is defined as the height above which there is sufficient canopy fuel per unit volume to support vertical fire spread into the canopy (Scott, 2001). It has widespread application in various wildfire behavior models (Hall and Burke, 2006). CBH can be estimated using allometric equations based on species, diameter at breast height (DBH), and tree height, or it can be retrieved from remote sensing data. However, due to the limitations of passive optical remote sensing signals and synthetic aperture radar (SAR) in penetrating the canopy, studies using multi-angle observations or bidirectional reflectance distribution function (BRDF) retrievals to obtain three-dimensional vegetation structure information are rare in wildfire prediction (Pisek et al., 2015; Canisius and Chen, 2007). More commonly, LiDAR is used to estimate CBH at the individual tree or local scale (Andersen et al., 2005; Luo et al., 2018; Wang et al., 2022a). Some studies suggest that while the definition of CBH is clear, its practical application is complicated by the lack of a clear fuel threshold per unit volume and the potential neglect 

of fine fuels, which can lead to errors in modeling canopy fire risk (Cruz et al., 2004; Kramer et al., 2014). As a result, a quick and simple method to estimate ladder fuels is by estimating the coverage area or coverage rate of low-lying fuels as a representation of ladder fuel (Clark et al., 2009; Wing et al., 2012). 

In addition to vertical continuity, horizontal fuel continuity is also crucial. There are various definitions of horizontal continuity. For example, Frandsen et al. (1979) defines horizontal continuity as the degree of variation in the physical characteristics of fuels within a given area, with an emphasis on the impact of fuel type. Conversely, a more commonly used definition in describing horizontal continuity focuses on the spacing between fuels (Ritter et al., 2023). Tree spacing significantly affects the intensity and scale of wildfires (Kim et al., 2016). For instance, Qadir et al. (2021) showed in a study on wildfire risk prediction in Nepal that areas with high forest cover density have a higher risk of fires. In contrast, when there is canopy discontinuity, fire spread may slow down or even be extinguished (Taneja et al., 2021). For example, Kim et al. (2016) used the Fire Dynamics Simulator (WFDS) to model fire behavior in Korean pine (Pinus densiflora) and found that when the spacing between trees is 6 meters or more, most crown fires stop spreading within 100 meters. Therefore, fuel management techniques that fragment fuels can be used to suppress wildfires (Srivastava et al., 2014; Harrison et al., 2021). 

Despite the demonstrated importance of horizontal fuel continuity, our review indicates that it has received comparatively less attention than vertical continuity. This discrepancy is likely due to the frequent use of proxies rather than direct measurements. For example, many crown fire spread models rely on canopy bulk density to approximate horizontal fuel continuity (Wagner, 1993; Cruz et al., 2005). Additional proxies, such as fractional vegetation cover, canopy cover, vegetation cover density, and various vegetation indices, are also commonly employed. 

In summary, fuel conditions play a crucial role in wildfire risk modeling. However, directly using fuel condition descriptors derived from remote sensing or multi-source geospatial data in large-scale and long-term wildfire risk prediction models is uncommon. Instead, as illustrated in Figure 3, most models rely on raw multispectral or microwave data and meteorological parameters, or indices derived from these sources, which have been shown to correlate with fuel conditions. This practice is driven by several considerations: 

First, accurately assessing fuel conditions is inherently complex and often requires integrating data from multiple sensors. Models designed for this purpose frequently exhibit poor generalization, making them applicable only to specific regions or temporal scales. Additionally, the availability of certain sensors poses a limitation. For instance, estimating vertical canopy structure relies heavily on LiDAR data. However, satellitebased LiDAR canopy measurements are constrained by spatial and temporal resolution, while airborne LiDAR is limited by coverage and high costs. 

Second, most wildfire risk assessment studies necessitate long-term time-series data, which are typically sourced from low-cost, widely available datasets such as multispectral or mi- 

9 

crowave satellite data. Due to constraints in spatial resolution and canopy penetration, these data often fail to accurately retrieve detailed fuel condition descriptors. Consequently, inaccuracies in inversion processes may lead to cumulative errors, further impacting prediction accuracy. 

Finally, the growing popularity of data-driven wildfire risk prediction algorithms reduces the reliance on explicitly defined fuel condition descriptors. These algorithms, capable of bypassing manual feature engineering, directly learn the necessary abstractions from raw data or features. This adaptability minimizes the need for explicit fuel condition parameters while maintaining high predictive performance. 

## _4.2. Weather and Climate Conditions_ 

Weather and climate factors are major drivers of wildfire activity, influencing the occurrence, burned area, and fire behavior (Swetnam and Betancourt, 1990; Bessie and Johnson, 1995; Abatzoglou and Kolden, 2013). Weather conditions are central to almost all global fire danger risk systems. High temperatures, low relative humidity, insufficient precipitation, and strong winds have been proven to be key factors in the ignition of fires in the short term (Keane et al., 2001; Zacharakis and Tsihrintzis, 2023), and they also affect fire size and spread (Abatzoglou and Kolden, 2011). On the other hand, climate conditions generally refer to the long-term weather conditions of a region and their variations. Some studies specifically define these as the collective atmospheric conditions months or even years before the start of the fire season, emphasizing the use of prior climate conditions to convert fuel conditions into wildfire potential (Abatzoglou and Kolden, 2013). This approach enables predictions of large-scale fire risks over seasonal, annual, or even multi-decadal time scales. 

## _4.2.1. Weather Conditions_ 

Short-term weather conditions focus primarily on predicting the impact of weather conditions over quarters, months, weeks, or days on fire risk. These include short-term temperature, wind, relative humidity, soil moisture, precipitation, and lightning, as well as corresponding indices like the Palmer Drought Severity Index (PDSI) and the FWI. Temperature and various humidity conditions affect fuel conditions, such as evapotranspiration and moisture content, which in turn influence the wildfire risk. Wind direction, wind speed, and other related metrics like Mean Wind Power Density (MWPD) and Mean Wind Speed (MWS) affect fire spread and intensity, making them commonly used parameters in wildfire prediction. Unlike other parameters, lightning can act as an ignition factor for wildfires. 

Short-term weather parameters are widely used in wildfire risk prediction. For example, Tavakkoli Piralilou et al. (2022) used temperature, precipitation, MWPD, and MWS as parameters in their wildfire prediction model for the forested areas of Gilan Province, Iran. In another study conducted in Pakistan, Kanwal et al. (2023) utilized 16 meteorological parameters, including monthly average precipitation, evapotranspiration, wind speed, soil temperature, humidity, heat flux, albedo, 

average land surface temperature, soil moisture, actual evapotranspiration, moisture deficit, downward surface shortwave radiation, precipitation accumulation, minimum/maximum temperature, and vapor pressure. An assessment of their importance indicated that heat flux, evapotranspiration, and vapor pressure were relatively more important compared to other meteorological parameters, although the differences in importance were not significant. Bergado et al. (2021) used seven meteorological factors in their wildfire prediction study for Victoria, Australia: daily maximum temperature, daily minimum relative humidity, daily total solar radiation, daily total precipitation, daily average wind speed, daily average wind direction, and lightning frequency. The lightning data was derived from an annual lightning climatology dataset that provided estimates of lightning density for each day of the year. Their study found that total precipitation, lightning density, and surface temperature consistently held high weight in all models. In contrast, Quan et al. (2023) used various meteorological variables from the ERA5 dataset, including precipitation, relative humidity, temperature, wind speed, and the Keetch-Byram Drought Index, to predict wildfire risk in parts of the western Tibetan Plateau in China. The study revealed that relative humidity was the most critical factor in the occurrence of forest and grassland fires in the region. Higher relative humidity leads to higher DFMC, thereby reducing the likelihood of ignition. 

## _4.2.2. Climate Conditions_ 

Climate conditions primarily refer to annual or multi-year meteorological parameters such as temperature, humidity, precipitation, and evaporation. Unlike short-term meteorological conditions that affect fuel status temporarily, climate conditions play a crucial role in determining fuel types, distribution, life cycles, and other factors that influence fuel characteristics, such as fuel load, type, and continuity (Aldersley et al., 2011; Jaafari et al., 2017; Tavakkoli Piralilou et al., 2022). These fuel characteristics respond to climatic patterns accumulated before the start of the fire season (Chen et al., 2016). Consequently, climate variables are often the primary drivers of long-term wildfire activity (Pollina et al., 2013; Jain et al., 2020). Furthermore, climate conditions explain strong seasonal variations in wildfire risk in certain regions (Martell et al., 1989). Intensified climate change in recent years has raised concerns about its long-term impacts on large-scale wildfires (Prior and Eriksen, 2013; Jolly et al., 2015; Jain et al., 2024). 

Climate conditions are widely used in wildfire risk prediction. Specifically, Chen et al. (2016) used large-scale sea surface temperature anomalies to predict the severity of the fire season in South America on a seasonal time scale. Their study found that using a single ocean climate index could predict about 48% of the burned area globally for up to three months or longer before the peak burning month. In a study by Jaafari et al. (2019) in the Zagros ecoregion of western Iran, they used three climate conditions: annual temperature, rainfall, and wind effects. However, the results showed that only the annual temperature parameter was relatively important. Similarly, Naderpour et al. (2020) studied the northern beaches of New South Wales, Australia, using three climate factors: annual rainfall, 

10 

annual humidity, and annual wind speed. Holdrege et al. (2024) studied the Great Basin sagebrush regions across 13 western U.S. states and used three climate factors: annual mean temperature, annual precipitation, and the proportion of summer (June to August) precipitation to total annual precipitation. The study found that areas with low summer precipitation proportion, medium to high annual precipitation, and high temperatures had the highest wildfire probability. Similarly, Aldersley et al. (2011) used annual cumulative precipitation, annual lightning frequency, monthly precipitation frequency, monthly average temperature, and climate data from the British Atmospheric Data Centre (BADC) to study the drivers of monthly fire area on a global and regional scale. They found that climate factors such as high temperatures, moderate precipitation, and drought were the most important drivers globally. Mansuy et al. (2019) conducted a study across the U.S. and Canada. They found that climate variables were the primary control factors controlling burned area in most ecoregions, both inside and outside protected areas, surpassing landscape and anthropogenic factors. The climate data used in their study included annual average precipitation, annual average relative humidity, the Hargreaves climate moisture deficit (an annual measure of energy and moisture), and degree days below 18°C. Abdollahi and Pradhan (2023) conducted a wildfire prediction study in the Gippsland region of Victoria, Australia, and found that humidity, wind speed, and rainfall were the most influential factors in wildfire prediction. Zhao and Liu (2021) used data from over 600 meteorological stations in forest, grassland, and shrubland areas to calculate two drought indices, the Keetch-Byram Drought Index and the Standardized Precipitation Index. They then used global-scale PDSI data to mask these indices and assess long-term wildfire risk in China. The results showed that drought indices had a stronger correlation with seasonal and annual fire occurrences compared to climate indicators such as temperature and precipitation. 

From the analysis above, it is evident that various forms of temperature, wind, humidity, and evaporation data are commonly used as meteorological or climate variables in wildfire prediction models. A few studies have combined both meteorological and climate factors to analyze their roles in the occurrence, spread, and scale of wildfires. For example, Abatzoglou and Kolden (2011) found in their study on the influence of weather and climate factors on the occurrence and scale of individual wildfires in Alaska that prior climate conditions had no significant effect on the final fire size, whereas post-ignition weather conditions, such as precipitation, had a greater impact over days to weeks. Thus, the authors suggest using short-term weather factors in wildfire risk assessment models and spread models. From another perspective, weather variables are more important than climate variables for small-scale and short-term wildfire risk and spread assessments. 

## _4.3. Socio-Economic Factors_ 

In the early development stages of wildfire risk assessment, considerable attention was given to factors influencing wildfire spread and suppression difficulty (McArthur, 1958, 1966; Hollis et al., 2024). However, numerous studies have shown that 

the proportion of fires caused directly or indirectly by human activities surpasses those triggered by natural factors, such as lightning (FAO, 2006). Indirect human activities typically refer to the impact of human actions on climate change, which in turn influences wildfire risk. This effect can be modeled by analyzing the influence of climate on wildfire risk. Furthermore, the impact of indirect human activities on wildfire risk also includes changes in vegetation types, land use patterns, and landscape fragmentation, as well as alterations in fuel load and fuel continuity due to activities like grazing, planting, and harvesting (Harris et al., 2023). These changes can significantly affect local wildfire risk. Direct human activities, on the other hand, primarily involve ignition and suppression. 

The risk of wildfires caused by direct human ignition is particularly significant. For instance, from 1992 to 2012, 84% of wildfires in the United States were human-induced (Balch et al., 2017). Similarly, Vilar et al. (2016) found that 95% of wildfires in Mediterranean Europe between the 1980s and 2010s were caused by human activities. Notably, human factors not only increase the frequency of fires but also extend the fire season and lead to more random distributions of fire locations (Balch et al., 2017). This randomness introduces greater uncertainty into wildfire risk prediction, as wildfires may occur in areas with infrequent lightning or where lightning does not coincide with high temperatures, dryness, and strong winds (Abatzoglou et al., 2016). 

Chuvieco and Congalton (1989) first introduced human activity variables into wildfire risk research by considering proximity to road networks and areas with high human activity, such as recreational zones. Since then, an increasing number of studies have incorporated human activity variables into wildfire risk prediction models. These variables include the distance of various locations from nearby roads, power lines, villages, and cities, as well as road density, population density, and land use. The assumption underlying the inclusion of these variables is that wildfire frequency is negatively correlated with distance from human infrastructure and positively correlated with road density and population size (Gilreath, 2006; Martínez et al., 2009). In addition to these easily describable features, there are more complex factors influencing wildfire risk, such as the potential for urban development to increase fuel loads in rural areas, or the possibility that controlled burns for agricultural purposes in remote areas may increase the likelihood of uncontrolled wildfires (Martínez et al., 2009). Several studies have confirmed these assumptions. For example, Jaafari et al. (2019) found a strong correlation between high wildfire probability and road network density in the Zagros ecoregion of western Iran. Ghorbanzadeh et al. (2019), in their study of the forest areas in Amol County, Mazandaran Province, northern Iran, similarly found that human activities near major roads significantly influenced wildfire risk. The interaction between human settlements and vulnerable infrastructure in areas with high or moderate forest fire susceptibility leads to the emergence of high-risk zones on wildfire risk maps. 

Therefore, most wildfire risk prediction studies consider the socio-economic factors mentioned above. For instance, Sadasivuni et al. (2013) generated a population interaction map 

11 

based on forest resources and human settlement patterns and studied wildfire risk in Mississippi, southeastern United States. They found that areas with dense fuel and sparse populations were most likely to experience wildfires. Malik et al. (2021) mapped wildfire risk in a densely vegetated area of approximately 63 _km_<sup>2</sup> between Monticello and Winters, California, using the location of power lines as a proxy for socio-economic factors, given that power lines can serve as ignition sources during high wind events. Nami et al. (2018) considered LULC and proximity to roads and settlements when mapping wildfire risk in the Hyrcanian ecoregion of northern Iran. They found that the probability of fire occurrence was highly dependent on human infrastructure and related activities. Additionally, the study revealed a positive correlation between fire occurrence and landscapes within 4,000 meters of human settlements, and a negative correlation for areas beyond 4 kilometers. Rubí and Gondim (2023) conducted a study in Brazil’s Federal District, dividing the region into zones based on the coverage of different weather stations and calculating the distance from each zone’s center to the nearest road and building as proxies for socioeconomic factors. Bergado et al. (2021) carried out a wildfire prediction study in Victoria, Australia, and found that land cover categories (such as farmland, forests, mines, and quarries) and distance from power lines were relatively low in importance. In their wildfire risk assessment in Guangdong Province, China, Jiang et al. considered socio-economic factors such as gross domestic product (GDP), distance from roads, and population density. The results showed that, aside from meteorological factors, GDP was the most significant factor in wildfire risk. Similarly, Jiang et al. (2024b) in their wildfire risk assessment in Guangdong Province, China, also utilized GDP, distance to highways, and population density as socio-economic factors. However, their results indicated that the contribution of socio-economic factors to wildfire risk was not significant. Furthermore, in a study conducted in the western part of the Tibetan Plateau in China, Quan et al. (2023) found that although government reports indicated that the majority (about 95%) of wildfires in the region were caused by human activities, the importance of distance from roads and residential areas was relatively low compared to meteorological factors. 

Current research on the impact of human activities on wildfire risk primarily focuses on using the distribution density of population, roads, and other infrastructure. It also utilizes the straight-line distance of different locations within the study area from infrastructure as input features for models. However, the consideration of these distances is typically limited to simple linear measurements, without accounting for human accessibility. This limitation may reduce model performance in regions with rugged terrain. Additionally, current research on human factors mainly focuses on human-induced wildfires, with little consideration given to the mitigating effects of firefighting facilities, such as fire stations, firebreaks, and lookout towers. 

## _4.4. Terrain and Hydrological Features_ 

Terrain factors used in wildfire prediction studies include elevation, slope, aspect, hill shade, and planar curvature. Terrain 

indirectly determines mesoscale and microscale climate and airflow (Coen et al., 2013), thereby impacting fuel conditions and wildfire propagation. For example, to some extent, an increase in slope leads to faster fire spread (Ghorbanzadeh and Blaschke, 2018). Steeper slopes result in faster fuel preheating and ignition rates, and compared to flat terrain, the rate of fire spread on a 20° slope increases by about four times (Lecina-Diaz et al., 2014). The slope aspect influences prevailing winds, humidity, solar radiation, and plant species distribution. In many regions of the Northern Hemisphere, north-facing slopes are typically cooler and more moist than south-facing slopes, making southfacing slopes at higher risk of forest fires (Sayad et al., 2019). Curvature and valley depth are geomorphic indicators of soil moisture and vegetation distribution (Kalantar et al., 2020). In larger valleys, downslope-driven cold air pooling has a significant impact on vegetation density and composition (Kiefer and Zhong, 2015). Additionally, elevation can also influence human activities, as lower elevations tend to have higher human population density and are more prone to wildfires compared to higher elevation areas (Guo et al., 2016). In addition, the main hydrological feature is the distance between fuel and water bodies, soil moisture, and the TWI. TWI represents soil saturation and surface runoff rates. Land with higher TWI is more saturated, and high moisture content can prevent fire ignition (Achu et al., 2021). 

In addition, Ghorbanzadeh et al. (2019) studied the forestry area of Amol County in the Mazandaran province of northern Iran and used slope, slope aspect, and altitude as terrain factors. They found that steep areas were generally more prone to forest fires. Nami et al. (2018) considered terrain factors such as slope, slope aspect, altitude, planar curvature, TWI, and topographic roughness index (TRI) when mapping wildfire risk in the Hyrcanian ecological region in northern Iran. Their further collinearity analysis revealed significant collinearity between TWI and slope with other parameters, leading to their exclusion from subsequent modeling tasks. A study conducted by Tran et al. (2023) on the island of Oahu in the Hawaiian Islands also utilized terrain and hydrological features such as elevation, slope, aspect, plan curvature, profile curvature, valley depth, TWI, and proximity to rivers. The assessment of their significance indicates that slope, elevation, and TWI are of secondary importance compared to proximity to roads and temperature in relation to fire risk. Gentilucci et al. (2024) also used TWI in a study in the Marche region of central Italy. Their research shows that areas of the terrain with less accumulation of moisture are most susceptible to fires. 

Soil moisture information can serve as a complement or substitute for drought indices and is commonly used in wildfire risk prediction models. It can be utilized in modeling fuel moisture and other related factors (Krueger et al., 2022). For example, Bakke et al. (2023) conducted a study in Fennoscandia, Finland, to explore the primary hydro-meteorological factors influencing wildfire occurrence. They found that shallow soil moisture anomalies were the main influencing factor. Similarly, in the study by Vissio et al. (2023) on the prediction of summer burning area in Italy, the ERA5 soil moisture reanalysis data product was used. The research found that using only a single variable, 

12 

namely surface soil moisture, for predicting wildfire burn area yielded good results. This is because surface soil moisture can serve as a proxy for the combined effects of temperature and precipitation. In the study by Nur et al. (2023) focusing on Sydney, Australia, the MODIS Terra Climate dataset was used, which provided drought indices and soil moisture data. However, due to the low resolution of the dataset (4 km), the importance of soil moisture as a factor was not fully reflected. In research conducted by Yahia et al. (2023), to improve the resolution of soil moisture, temperature vegetation dryness index (TVDI), perpendicular drought index (PDI), optical trapezoid model (OPTRM), and modified normalized difference water index (MNDWI) were used as proxies for soil moisture. These variables, along with a Gaussian Naive Bayes (GNB) classifier, were employed to generate wildfire risk maps. Additionally, the NDVI can be used to estimate soil moisture anomalies (Tucker, 1979; Liu et al., 2010). However, when modeling moisture anomalies using NDVI, it can only directly detect surface soil moisture. To obtain deep soil moisture, a physical or empirical relationship must be employed. In addition, it is worth noting that the estimation of soil moisture based on optical or SAR remote sensing imagery still faces significant challenges. This is due to the influence of factors such as tree canopy obstruction, absorption, reflection, and scattering, which result in a mixed signal received by the sensor containing information on both soil and fuel moisture (Pelletier et al., 2023). 

## _4.5. Wildfire Historical Records_ 

Wildfire historical records are indispensable in all studies and form the data foundation for wildfire risk prediction models. The sources and scales of wildfire historical records vary widely. For example, in Canada, many provinces, cities, or forestry management agencies maintain their own wildfire historical records. Additionally, the Canadian Natural Resources Department maintains its wildfire information data system, such as the Canadian Wildfire Information System. Commonly used public global or regional scale wildfire historical records include the National Burned Area Composite dataset (NBAC), the Canadian National Fire Database (CNFDB), the National Institute for Space Research database (INPE), the Fire Planning and Analysis Fire Occurrence Database (FPA-FOD), the Global Fire Emissions Database (GFED), and FireCCI. In regions without systematic wildfire records, most studies use satellite-derived thermal anomalies or wildfire products from MODIS, Suomi-National Polar-orbiting Partnership (S-NPP), National Oceanic and Atmospheric Administration (NOAA) VIIRS, GOES, AVHRR, Sentinel, Landsat, Himawari, FY-4, among others. 

Specifically, Pelletier et al. (2023) used the NBAC dataset from the Canadian Forest Service for their study on the northern Canadian forest peatlands. Liang et al. (2019) utilized the CNFDB dataset for wildfire research in Alberta, Canada, which includes fire location (latitude and longitude points), ignition date, extinguishment date, burned area, and cause of fire provided by provincial, regional, and the Canadian Parks Service firefighting agencies. Rubí and Gondim (2023) employed the INPE database for their study in the Federal District of Brazil. 

The INPE fire database is primarily based on thermal anomaly data collected from satellites such as AQUA, TERRA, NOAAs15, 16, 17, 18, and 19, METEOSAT-02, and GOES-12. It covers the geographic location and timing of fires (latitude, longitude, and date/time) since the year 2000. Wang et al. (2021) used the FPA-FOD dataset to assess the drivers of wildfires in the continental United States, which includes discovery date, burned area, and geographical location (longitude and latitude) of wildfires from 1992 to 2020. The dataset intentionally excludes prescribed fires that escaped and required suppression response. Despite the possibility of missing data on smaller fires, the omission is tolerable for analytical purposes since the largest 5% of all fires account for the majority of the burned area. Song and Wang (2020) utilized the Global Fire Emissions Database version 4.1 (GFEDv4) for predicting global monthly wildfire risks throughout the year. This dataset covers monthly wildfire areas globally from 1997 to 2016, with a spatial resolution of 0.25° x 0.25°. It also includes daily burned area data globally from August 2000 to 2015. Bakke et al. (2023) employed the FireCCI dataset in their study in Fenno-Scandinavia, Finland, which provides global-scale pixel products at spatial resolutions of 250m or 300m, or gridded products at a resolution of 0.25 x 0.25 degrees, with a temporal resolution equal to or less than one month. 

Satellite thermal anomaly products, such as MODIS MCD14 and MCD64A1 products (Giglio et al., 2003, 2016) are commonly used in wildfire risk prediction studies. The MCD14 series dataset has a spatial and temporal resolution of 1km and one day, respectively, offering a long time series (from 2006 to present) and providing near-real-time wildfire hotspot maps. The MCD64A1 dataset has a higher spatial resolution of 500m, although it does not offer near-real-time products. In specific studies, Abdollahi and Pradhan (2023) used MODIS fire and thermal anomaly data in their wildfire prediction research in the Gippsland region of Victoria, Australia, along with the NPWS Fire History - Wildfire and Prescribed Burning dataset provided by the New South Wales Department of Climate Change, Energy, the Environment, and Water. Ghorbanzadeh et al. (2019) acquired polygon data for 34 wildfire areas through field surveys and assessed data for the forested regions of Amol County, Mazandaran Province, northern Iran using MODIS data. Jaafari et al. (2019) and Nami et al. (2018) also employed historical data, field surveys, and validated using MODIS hotspot products in their studies in the western Zagros ecoregion and the northern Hyrcanian ecoregion of Iran, respectively, to enhance the reliability of historical data. Kanwal et al. (2023) in their study in Pakistan used MODIS data from the Fire Information for Resource Management System (FIRMS) as wildfire historical data, setting a 60% confidence threshold to reduce false alarm errors. 

Additionally, some studies argue that MODIS products may overlook fires that are smaller in scale or shorter in duration (Hantson et al., 2013; Benali et al., 2016; Fusco et al., 2019; Ying et al., 2019). Therefore, other satellite data are also used either in conjunction with MODIS data or independently for fire hotspot detection or burned area mapping, and the generation of historical datasets. For instance, the study 

13 



Figure 3: Feature utilization frequencies is classified into four categories: weather and climate conditions, fuel conditions, terrain and hydrological attributes, and socio-economic variables. The color scheme in this visual representation signifies the prevalence of these features, with red, purple, and blue denoting utilization frequencies exceeding 20, 10, and 0 occurrences, respectively. 

by Zhang et al. (2021a) used the GFED dataset, which utilizes the MODIS MCD64A1 dataset and VNPIMG14ML dataset (Schroeder et al., 2014; Hall et al., 2024), to mitigate errors of commission and omission in agricultural fire detection in the MODIS dataset. Moreover, some studies have begun to explore using other high temporal resolution data to build global or regional wildfire detection datasets, such as the Sea and Land Surface Temperature Radiometer (SLSTR) sensor on Sentinel3A/B (Xu and Wooster, 2023). 

## _4.6. Frequency of Di_ ff _erent Data Utilization_ 

In the "Fuel Conditions" category, the NDVI is the most frequently utilized variable, with a frequency of 27, underscoring NDVI’s critical role in assessing vegetation health and fuel availability. Other significant variables include Tree Species, which appears 8 times, and LAI and Vegetation Type, each with a frequency of 6. These variables are essential for understanding the characteristics of biomass that contribute to wildfire risk. The presence of numerous variables with lower frequencies, such as Enhanced Vegetation Index (EVI) and NDWI, each used only once, highlights the complexity of this category. This diversity of variables reflects the multifaceted nature of fuel dynamics, requiring a broad range of factors to be considered in fire risk modeling, as depicted in Fig. 3. 

In the "Climate and Weather Conditions" category, Temperature emerges as the dominant variable, with a frequency of 65. Precipitation follows closely with 53 occurrences, and Wind is also significantly utilized, with a frequency of 42. These variables are fundamental in understanding fire behavior, particularly in their influence on fire ignition, spread, and intensity. Humidity, used 27 times, and Moisture, used 16 times, further contribute to this category, reflecting the central role of at- 

mospheric conditions in fire risk assessments. Other variables, such as Fuel Moisture Code, utilized 11 times, and Vapor Pressure, with 9 occurrences, are less frequently employed but remain crucial in specific contexts. The data presented in Fig. 3 emphasizes that climate variables, particularly Temperature and Precipitation, are among the most critical factors in fire dynamics, with a wide array of related variables also contributing to detailed climatic modeling. 

Land Use and Land Cover stands out as the most frequently utilized socio-economic variable, appearing 32 times, underscoring its importance in assessing how human activities and changes in land use influence fire risk. Road Proximity, with 23 occurrences, and Settlement Proximity, with 18, follow, indicating the significance of infrastructure and human settlement patterns in fire studies. Population Density, appearing 16 times, and Road Density, with a frequency of 4, also play roles, although to a lesser extent. The data in Fig. 3 suggest that while variables like Gross Domestic Product (GDP) and Distance to Cropland—each used 5 times—are relevant, they are more context-specific. This analysis indicates that socio-economic factors are essential for understanding the human impact on fire dynamics, particularly in areas where land use and human infrastructure intersect with natural landscapes. 

In the "Terrain and Hydrological Features" category, Slope is the most frequently used variable, appearing 46 times. This reflects the critical role of slope in influencing fire spread and intensity. Aspect, with a frequency of 34, and Elevation, with 32, are also key factors in understanding how topography affects fire behavior. These variables are particularly important in regions with complex terrain, where physical landscape features significantly impact fire dynamics. Plan Curvature, used 11 times, and TWI, used 10 times, are less frequently applied 

14 

Table 2: Open-access Wildfire Spread Prediction Datasets 

|**Dataset**|**Spatial-temporal**<br>**Coverage**<br>**and**<br>**Resolution**|**Fuel Conditions**|**Climate and Weather Conditions**|**Socio-economic**<br>**Fac-**<br>**tors**|**Terrain**<br>**and**<br>**Hydrological**<br>**Features**|**Historical**<br>**Records**|
|---|---|---|---|---|---|---|
|FireCube|Greece<br>and<br>Eastern Mediter-<br>ranean<br>(1<br>km),<br>2009-2021<br>(Daily)|MODIS: EVI (MOD13A2, 16d,<br>1 km), LAI (MOD12A2H, 500<br>m, 8d), NDVI (16d, 1 km)|ERA5-Land: Avg, max, min of dew point temper-<br>ature, relative humidity, surface pressure, air tem-<br>perature, total precipitation, U and V wind com-<br>ponents (1d, 9 km); MODIS: Total evapotranspira-<br>tion (MOD16A2, 8d, 500 m), day and night LST<br>(MOD11A1, 1d, 1 km), FPAR (8d, 500 m);Europe-<br>EDO: Soil moisture index anomaly, Soil moisture<br>(10d, 5 km)|Corine<br>Land<br>Cover:<br>LULC<br>(2006,<br>2012,<br>2018);<br>WorldPop:<br>Population<br>density<br>(2009-2021),<br>distance<br>from<br>roads,<br>distance<br>from waterways|EU-DEM:<br>Ele-<br>vation,<br>aspect,<br>roughness,<br>slope<br>(2016, 30m)|EFFIS & MODIS:<br>Ignition<br>points,<br>burn area, daily fire<br>count|
|Next Day Wild-<br>fire Spread|USA<br>(1<br>km),<br>2012-2020<br>(Daily)|VIIRS: NDVI (VNP13A1) (8d,<br>500 m)|GRIDMET: Wind direction and speed, minimum<br>and maximum temperatures, humidity, precipita-<br>tion (1d, 4 km), drought index, energy release com-<br>ponent (ERC) (5d, 4 km)|GPWv4:<br>Population<br>density (1 km)|SRTM: Elevation<br>(30 m)|MODIS:<br>MOD14A1<br>V6<br>(1d, 1 km)|
|WildfireDB|California,<br>USA<br>(375<br>m),<br>2012-<br>2018 (Daily)|LANDFIRE: Canopy base den-<br>sity, base height, cover, canopy<br>height, and existing vegetation<br>cover, height, and type (2012,<br>2014, 2016, 30 m)|NOAA Ground Station Data: Temperature (avg,<br>min, max), total precipitation, atmospheric pres-<br>sure, and wind speed (1d, 5787 stations)||Elevation<br>and<br>slope (2016,<br>30<br>m)|VIIRS: Active Fire<br>(1d, 375 m)|
|WildfireSpreadTS|USA<br>(375m),<br>2018-2021<br>(Daily)|VIIRS: EVI (VNP13A1) and<br>NDVI (8d, 500 m)|GRIDMET: Surface temperature (min, max), total<br>precipitation, wind speed and direction, specific hu-<br>midity, PDSI (1d, 4.6 km);Global Forecast System:<br>Temperature and wind (avg, direction, speed) (1d,<br>27.83 km)|MODIS: Land Cover<br>Type<br>Yearly<br>Global<br>product<br>(MCD12Q1,<br>1y, 500 m)|SRTM: Elevation,<br>slope, and aspect<br>(2013, 30m)|VIIRS: Active Fire<br>(1d, 375 m)|
|CFSDS|Canada<br>(180m),<br>2002-2021<br>(Daily)|SCNFI: Percentage deciduous<br>component, percentage conif-<br>erous component, biomass in<br>tonnes/ha, and crown closure<br>percentage<br>(30m);<br>Peatland<br>presence<br>and<br>class<br>(250m);<br>ERA5-Land:<br>FFMC, DMC,<br>DC, ISI, BUI (1d, 0.1deg)|ERA5-Land: The maximum daily temperature, 24<br>hr precipitation, noon wind speed, noon relative hu-<br>midity, and 24hr maximum vapour pressure deficit<br>(1d, 0.1deg)|CanVec Transport Fea-<br>tures:<br>Road density,<br>distance to road|ASTER:<br>Ele-<br>vation,<br>slope,<br>aspect, and TWI;<br>National Ecolog-<br>ical<br>Framework<br>for<br>Canada:<br>Ecozones|National<br>Burned<br>Area<br>Compos-<br>ite;<br>VIIRS:<br>VNP14IMGT<br>and<br>VJ114IMGTDL_NRT<br>(375m);<br>MODIS:<br>MCD14ML (1km)|
|SeasFire Cube|Global (0.25deg),<br>2001-2021 (8d)|MODIS:<br>NDVI<br>(MCD15A2,<br>8d, 500m), LAI (MOD13C1,<br>16d, 5600m)|ERA5: Mean sea level pressure, total precipita-<br>tion, relative humidity, vapor pressure deficit, sea<br>surface temperature, skin temperature, wind speed,<br>2m temperature (mean, min, max), surface net so-<br>lar radation, surface net solar radation, surface solar<br>radation downward, volumetric soil water (level1-<br>4), land-sea mask (0.25deg); Copernicus CEMS:<br>Drought code (max, avg), fire weather index (max,<br>avg) (1d, 0.25deg); CAMS: Carbon dioxide emmi-<br>sion from wildfire, fire radative power (1d, 0.1deg);<br>MODIS: LST (MOD11C1, 1d, 0.05deg); NOAA<br>climate indices|GPWv4:<br>Population<br>density<br>(1km);<br>ESA<br>CCI:<br>LULC<br>(7d,<br>300m/1km);Biomes||FireCCI:<br>Burned<br>areas<br>(area,<br>mask,<br>fraction)<br>(250m/300m);<br>GFED:<br>Burned<br>areas (area, mask)<br>(1month, 0.25deg);<br>GWIS:<br>Burned<br>areas (area, mask)|



but remain relevant in specific contexts, often related to hydrological modeling. Other variables like Latitude, used 5 times, and Landform, with 3 occurrences, indicate their more specialized application. The analysis of these features highlights that, while terrain and hydrological factors are crucial for understanding the physical environment’s impact on fires, certain variables like Slope, Aspect, and Elevation consistently prove to be more influential. 

Overall, when comparing the categories, climate and weather conditions emerge as the most frequently utilized, with Temperature and Precipitation leading the way. Fuel conditions follow closely, with NDVI being the most prominent indicator of vegetation health and fuel availability. Socio-economic factors, while important, are used more selectively, with LULC, Road Proximity, and Settlement Proximity being the primary variables. Finally, terrain and hydrological features, particularly Slope, Aspect, and Elevation, are critical for understanding how the physical landscape influences fire behavior. However, it is worth noting that the frequency of use of the aforementioned features is not solely dependent on their importance but also on their ease of availability. For example, in the "Fuel Conditions" category, NDVI is more readily accessible compared to other features; similarly, variables like Temperature, LULC, Slope, Aspect, and Elevation are also more easily obtained. 

## _4.7. Open-Source Wildfire Spread Prediction Datasets_ 

With the growing reliance on machine learning methods for wildfire risk prediction, the need for standardized datasets to establish, evaluate, and compare models has become evident. To address this, several open-source wildfire spread datasets have been released, providing varying spatial, temporal, and thematic coverage for research. These datasets support the development of machine learning-based wildfire risk prediction models and offer standardized benchmarks for evaluating model generalization. 

The datasets presented in Table 2, including FireCube (Prapas et al., 2022; Kondylatos et al., 2023), Next Day Wildfire Spread (Huot et al., 2022), WildfireDB (Singla et al., 2020), WildfireSpreadTS (Gerard et al., 2023), CFSDS (Barber et al., 2024), and SeasFire Cube (Alonso et al., 2023), encompass various factors critical to wildfire spread prediction. These factors include spatial-temporal coverage of fuel conditions, climate and weather conditions, socio-economic factors, terrain, and historical records. Each dataset differs in the spatial-temporal coverage, and resolution of these factors, providing diverse perspectives and data for wildfire modeling. 

First, the datasets vary significantly in their spatial and temporal resolutions. For instance, FireCube and Next Day Wildfire Spread focus on coarse-resolution data with a spatial resolution of 1 km for daily observations. WildfireDB offers more localized coverage at 375 m but over a broader temporal range (2012-2018). The CFSDS dataset provides highly detailed data at 180m resolution, though its temporal span is longer (20022021). SeasFire Cube offers the broadest coverage globally, albeit at a coarser resolution of 0.25 degrees and 8-day intervals. 

Regarding fuel conditions, the datasets primarily utilize vegetation indices such as MODIS EVI and NDVI. FireCube com- 

bines MODIS EVI, LAI, and NDVI to provide a detailed view of vegetation. Similarly, Next Day Wildfire Spread and WildfireSpreadTS rely on VIIRS NDVI, offering 8-day data at 500m resolution. WildfireDB stands out by incorporating LANDSFIRE data, which includes specific details like canopy base density and height, providing a more comprehensive fuel description, although at a lower temporal resolution. CFSDS uses specialized Canadian forest inventory data, adding complexity by considering forest composition and peatland presence. 

For climate and weather conditions, most datasets rely on reanalysis products. FireCube integrates ERA5-Land data, covering a broad range of climatic variables, including temperature, precipitation, and soil moisture. Next Day Wildfire Spread and WildfireSpreadTS use GRIDMET data for similar parameters, with WildfireSpreadTS further incorporating Global Forecast System data for temperature and wind predictions. WildfireDB uses NOAA Ground Station data, focusing on ground-based observations, which may offer more accuracy but less spatial coverage. 

The inclusion of socio-economic factors varies widely among the datasets. FireCube incorporates multiple socioeconomic variables, including LULC, population distribution, and proximity to roads and waterways, offering a comprehensive view of human impact on wildfire spread. Next Day Wildfire Spread and SeasFire Cube focus solely on population density, while WildfireSpreadTS considers only LULC. WildfireDB does not include socio-economic factors, limiting its ability to account for human influences on wildfire ignition. 

Terrain and hydrological features are primarily derived from DEM products, providing data on elevation, slope, and aspect. FireCube uses the EU-DEM, while Next Day Wildfire Spread and WildfireSpreadTS rely on SRTM products. CFSDS employs ASTER data for terrain variables, while WildfireDB and SeasFire Cube use various unspecified sources for elevation data. Despite different products, all datasets achieve similar resolutions of around 30m. 

Historical wildfire records are crucial for validating wildfire spread and risk prediction models. FireCube incorporates both MODIS and EFFIS records, offering detailed fire occurrence accounts. Next Day Wildfire Spread relies on the MOD14A1 product, while WildfireDB and WildfireSpreadTS use VIIRS data at 375m resolution. SeasFire Cube integrates multiple sources, including FireCCI, GWIS, and MODIS, to provide a comprehensive historical dataset, though at a coarser resolution. 

It is important to note that we only consider time series wildfire observation datasets stored in a spatially explicit format and encompassing multiple wildfire impact factors. Datasets that do not have a clearly defined spatial distribution (Sayad et al., 2019), datasets containing only historical wildfire extent (Short, 2014; Andela et al., 2019; Artés et al., 2019; Lizundia-Loiola et al., 2020; Hargrove et al., 2022; Gincheva et al., 2024), fire detection datasets (Chino et al., 2015; Toulouse et al., 2017; Shamsoshoara et al., 2020; Mou et al., 2020; El-Madafri et al., 2023), and simulation datasets (Wang et al., 2024), are not included. 

It is worth noting that, as shown in Table 2, the number of 

16 

available open-source wildfire spread datasets is limited, with most coverage concentrated in the United States and Mediterranean, while other regions, such as the wildfire-prone Canada and Australia, are underrepresented. Additionally, some studies using these datasets have overly simplistic considerations of fuel conditions, such as relying solely on vegetation indices as proxies. This approach fails to accurately and comprehensively describe the state of fuel load, moisture content, and continuity. Similarly, using MODIS or VIIRS to record historical burned areas lacks precision. These datasets may may overlook small fire spots, offer low spatial and temporal resolution, and be prone to false alarms (Zubkova et al., 2024). Furthermore, there is a lack of quantitative evaluation of how the accuracy of different products impacts the accuracy of wildfire spread predictions. 

## **5. Features Collinearity and Attribution** 

The relationship between wildfire risk and its driving factors has long been a focal point in wildfire prediction research. Understanding the interactions between wildfire occurrence and factors such as fuel conditions, climate, meteorological variables, terrain characteristics, and human activities is critical for model design, data selection, and supporting wildfire management decisions (Aldersley et al., 2011). However, the inherent "black-box" nature of deep learning models poses significant challenges in interpreting the contribution of individual factors to wildfire risk predictions (Castelvecchi, 2016). This section systematically reviews commonly used feature attribution methods in deep learning-based wildfire risk prediction models, highlighting their potential and limitations. 

Furthermore, wildfire risk prediction models often incorporate multiple driving factors, some of which may exhibit a high degree of multicollinearity. Highly correlated independent variables can introduce redundancy, complicating the isolation and interpretation of their individual contributions to the dependent variable (Chen et al., 2019). Systematically assessing multicollinearity and quantifying the individual contributions of these factors are essential for improving model reliability and providing actionable insights for effective wildfire management. Additionally, commonly used features in wildfire risk prediction models—such as precipitation, temperature, wind speed, terrain attributes, and vegetation indices—often overlap across studies. Investigating whether these features share inherent collinearity, independent of spatial and temporal distributions, is particularly valuable. This analysis could guide feature selection in future research, especially in data-constrained scenarios, ultimately enhancing the efficiency and accuracy of model development. 

## _5.1. Assessment of Feature Collinearity_ 

Multicollinearity refers to the presence of approximate linear dependencies among two or more predictor variables, meaning that one predictor can be linearly represented by a combination of others (Senawi et al., 2017). This phenomenon leads to several issues, including inflated standard errors of coefficients, coefficients with signs inconsistent with theoretical expectations, 

statistically insignificant parameters despite strong correlations between predictor variables and the outcome, and excessively large correlation coefficients relative to the explanatory power of the model (Chan et al., 2022). 

Under multicollinearity, regression methods often produce redundant, unstable models with poor generalization performance, making it difficult to isolate the marginal effects of individual predictors (Katrutsa and Strijov, 2017; Chan et al., 2022). Although deep learning models—which do not rely on linear parameter estimation—are less affected in terms of predictive performance, multicollinearity can still adversely impact the accuracy and stability of interpretability in predictive analysis. This, in turn, reduces the overall efficiency of model interpretation and analysis (Salih et al., 2024). 

To evaluate collinearity in wildfire risk prediction, common metrics such as the Variance Inflation Factor (VIF) and tolerance are widely employed (Hair Jr et al., 1986; Liao and Valliant, 2012). VIF measures the extent to which the variance of a regression coefficient is inflated due to collinearity, while tolerance quantifies the proportion of variance in a predictor that is not explained by other predictors in the model. These metrics are critical for identifying and mitigating collinearity-related issues, ensuring robust model development and interpretation. The formulas for these metrics are as follows: 



<!-- Start of picture text -->
VIF = 1<br>Tolerance (9)<br>Tolerance = 1 − R 2<br><br><!-- End of picture text -->

where _R_<sup>2</sup> is the coefficient of determination when the predictor is regressed against all other predictors. A high VIF value (typically above 10) or a low tolerance value (below 0.1) indicates significant collinearity, suggesting that one predictor is largely explained by others. 

VIF had been widely used in wildfire risk predictions. For example, Nami et al. (2018) conducted a collinearity analysis using VIF and tolerance in their study on wildfire risk mapping in the northern Hyrcanian ecoregion of Iran. They found significant collinearity between the TWI and slope with other parameters, leading to their exclusion from subsequent modeling efforts. In contrast, Jaafari et al. (2019) assessed the collinearity of various predictors using VIF and tolerance in their study in the western Zagros ecoregion of Iran. They discovered that the VIF values for TWI and slope were below 5, and tolerance values were above 0.2, indicating insignificant collinearity with other predictors (Liao and Valliant, 2012). Hong et al. (2019), in their modeling of wildfire susceptibility in Huichang County, China, used VIF and tolerance to assess the collinearity of multiple predictors and found no significant collinearity between slope and other features. 

In another study, Li et al. (2022a) examined the drivers of forest fires in Yunnan Province, China, and found that six meteorological factors (daily average atmospheric pressure, daily minimum atmospheric pressure, daily average temperature, daily minimum temperature, daily average surface temperature, and daily minimum surface temperature) had VIF values exceeding 10 and tolerance values below 0.1, indicating significant correlations. The study also used the Pearson correlation algorithm 

17 

to analyze the correlations of the remaining variables, finding a correlation coefficient of 0.77 between surface temperature and air temperature. 

Similarly, in their wildfire prediction model for Maui Island in Hawaii, Rezaie et al. (2023) analyzed the correlation and collinearity among independent variables (altitude, slope, aspect, valley depth, TWI, slope length, plan curvature, distance from rivers, distance from roads, NDVI, average monthly rainfall, average annual wind speed, and average annual temperature) using Pearson correlation coefficients, VIF, and tolerance. They found the strongest correlations between average annual temperature and altitude, and the most significant collinearity between average annual temperature and distance from roads. However, the collinearity and correlations among all variables were not statistically significant. 

In summary, various studies have revealed differing levels of multicollinearity among features, highlighting the challenge of drawing consistent conclusions about the relationships between specific features in wildfire risk prediction models. Nevertheless, feature multicollinearity analysis remains critical as it facilitates dimensionality reduction, thereby accelerating model training and inference. More importantly, addressing multicollinearity can significantly improve the accuracy, reliability, and stability of feature attribution, particularly when employing attribution methods that assume feature independence (Salih et al., 2024). 

## _5.2. Feature Attribution_ 

In wildfire risk prediction algorithms, explicit methods can predict wildfire risk by defining the contributions of different features to the ignition and spread of wildfires. However, these methods often have poor fitting capabilities and struggle to handle the nonlinearity and randomness characteristic of wildfire risk prediction tasks. On the other hand, machine learning models, such as deep learning and ensemble learning models, can extract patterns from highly complex datasets and demonstrate superior predictive performance. However, their decision-making processes are opaque, earning them the label of "black box models." 

In wildfire risk prediction, this lack of transparency undermines the credibility of the predictions and makes it difficult for researchers and fire management agencies to understand the factors inducing wildfire ignition and spread. This, in turn, hinders the understanding of wildfire mechanisms and the prevention and management of wildfires. The interpretation of the decision-making process in machine learning models is generally referred to as explainable AI (XAI). In this paper, we define XAI as the attribution of causal responsibility or feature attribution (Josephson and Josephson, 1996), as XAI in wildfire risk prediction algorithms mainly focuses on explaining the influence of different wildfire risk factors on model predictions. Currently, common XAI methods in wildfire risk prediction include Permutation Feature Importance (PFI), Explainable Feature Engineering (Ali et al., 2023), and SHapley Additive exPlanations (SHAP). 

Firstly, PFI quantitatively analyzes feature importance by randomly permuting each feature and evaluating the change in 

model performance. For example, Rubí and Gondim (2023) used PFI to assess the contributions of meteorological, fuel, terrain, and socioeconomic factors in models such as ANN, SVM, NB, KNN, LR, LogLR, and AdaBoost in their study in the Federal District of Brazil. They found that analyzing individual variables might lead to contradictory results. For instance, NDVI was more important for models like AdaBoost and ANN, whereas its influence was relatively low or nonexistent in other models such as LR and SVM. This finding highlights the necessity of considering multiple variables in predictive modeling and the varying importance of different models. Additionally, Shadrin et al. (2024) evaluated the impact of specific feature values on the final test results by setting them to zero during model testing. Similarly, Chen et al. (2024b) calculated the importance of each feature by measuring the variation in prediction error when feature values were perturbed. 

Secondly, Explainable Feature Engineering (Ali et al., 2023) methods have also been applied to wildfire risk prediction. For example, Rezaie et al. (2023) used the Information Gain Ratio (IGR) to select the optimal subset of variables in their wildfire prediction model for Maui, Hawaii. They found that the distance to roads had the highest IGR value of 0.903, indicating its significant impact on mapping fire-prone areas. The next important variables were annual average temperature (0.724), elevation (0.715), and slope (0.665). Similarly, Zhang et al. (2019) used IGR to evaluate the importance of different factors in assessing forest fire risk in Yunnan Province, China. They found that temperature and wind speed contributed the most to the risk, while the importance of distance to roads and rivers was the lowest. In another example, Hong et al. (2019) modeled the spatial distribution of wildfire susceptibility in Huichang County, China, using the Analytic Hierarchy Process to assign weights to a logistic regression model and found that elevation was the most influential indicator of fire occurrence, followed by land use, NDVI, and distance to human settlements. 

Finally, SHAP analysis (Shapley, 1953), which is based on game theory, is more commonly used, especially for explaining complex models, because it considers both feature importance and feature interactions while offering higher computational efficiency. SHAP explains the impact of each feature on model predictions by assigning SHAP values to them. Common SHAP methods include Kernel SHAP, Deep SHAP, and Tree SHAP (Lundberg and Lee, 2017). For instance, to address the challenge of explaining deep learning models, Abdollahi and Pradhan (2023) introduced SHAP to study the contribution of different features to the model. The authors found that relatively high NDVI, temperature, and elevation, as well as relatively low NDMI and precipitation, increased wildfire risk, while relatively high humidity reduced this risk. They also identified elevation, NDMI, and precipitation as the three most critical factors influencing wildfire occurrence. 

Similarly, Wang et al. (2021) used SHAP to evaluate the drivers of large-scale wildfires in the contiguous United States and found that coordinate variables (including longitude and latitude) and local meteorological variables (such as ERC, RH, temperature, and VPD) were important predictors of burned area across the domain. This is because coordinate variables 

18 

carry crucial geographic information that broadly reflects climate, land use, human activity, and other key geographic factors, helping to distinguish temporal characteristics of different fire regimes and thus aiding in predicting burned areas. Using SHAP’s local interpretability, they also explained the driving factors of large burned areas in different regions and months within the contiguous United States. For example, ERC was identified as the most important indicator of large burned areas in the western US. 

Iban and Aksu (2024) conducted a local SHAP importance analysis in the<sup>˙</sup> Izmir region of Turkey and found that wind speed, LULC, slope, temperature, and NDVI were the five most important influencing factors. Wind speeds above 3.5 m/s, forests in LULC, slopes greater than 8 degrees, annual average temperatures above 14 degrees, and NDVI values below 0.2 all promoted wildfires, while higher NDVI reduced the likelihood of wildfire occurrence. In the wildfire risk assessment for Hawai’i Island, Tran et al. (2024) considered 14 factors, including meteorological, topographic, anthropogenic, and vegetation-related variables: elevation, slope, aspect, plan curvature, profile curvature, TWI, valley depth, annual average wind speed, NDVI, annual average precipitation, annual average temperature, distance to roads, distance to rivers, and land use. SHAP analysis revealed that the distance from a road, annual temperature, and elevation were the most influential factors, with wildfire risk increasing as distance from roads decreased and temperature increased. Additionally, low- to midelevation areas were generally associated with a higher likelihood of fire occurrence due to their relatively high temperatures and accessibility. 

Kondylatos et al. (2022) conducted a SHAP analysis for the Eastern Mediterranean region and found that soil moisture index, humidity indicators, temperature variables, NDVI, and wind speed were the most important factors influencing wildfire risk. Notably, the study found that the relationship between NDVI and fire risk was U-shaped, meaning that both very low and very high NDVI levels were associated with lower wildfire risk. 

Currently, explainability analysis in wildfire prediction faces several challenges, such as insufficient exploration of alternative explainability methods, dependency on models and explanation techniques, unclear attribution analysis, and the uncertainty of the explanations provided. 

Firstly, techniques like activation maximization analysis (Erhan et al., 2009), Partial Dependence Plot (Greenwell et al., 2017), Integrated Gradients, and other additive feature attribution methods beyond SHAP—such as Local Interpretable Model-agnostic Explanations (LIME), DeepLIFT, and LayerWise Relevance Propagation—have not been adequately explored in the context of wildfire risk prediction. The limited application of these XAI methods leaves gaps in our understanding of how different approaches might enhance model transparency in this domain. 

Secondly, many studies select the best-performing model through comparative experiments and then conduct explainability analysis based on that model. The explanations provided by these methods often estimate how a specific ML model derives 

predictions from input data (Good and Hardin, 2012). However, treating these analyses as direct insights into real-world phenomena can lead to misleading or erroneous conclusions, particularly if the model’s learned decision rules do not align with the actual underlying data relationships (Jiang et al., 2024a). For instance, using a single explainability method to interpret different ML models, or using different explainability methods to interpret the same ML model, might result in varying or even contradictory observations. Therefore, any inferences drawn from these post-hoc explanations should be approached with caution (Ploton et al., 2020). 

Furthermore, wildfire prediction studies often employ multiple input variables and model the relationships between these variables and wildfire risk. While such models may perform well, they do not necessarily explain whether causal relationships exist between independent and dependent variables, as the modeled relationships often result from correlations among various features (Rogger et al., 2017; Molnar et al., 2020). An example of this is multicollinearity among features, which is very common in Earth sciences due to the highly complex interactions and interdependencies between geological, meteorological, ecological, and additional factors in the Earth system (Jiang et al., 2024a). For instance, features commonly used in wildfire risk prediction, such as NDVI, soil moisture, precipitation, temperature, and evapotranspiration, often exhibit complex interrelationships. A crucial condition for ML models to produce valid causal effect estimates is that their input variables must be independent of unobserved confounders. Therefore, in most cases, ML should not be considered a definitive source of causal knowledge (Jiang et al., 2024a). This highlights the need for further research into the application of causal ML (Tesch et al., 2023) in wildfire risk prediction. 

Lastly, while explainability analysis enhances model transparency, these explanations are still subject to uncertainty, unreliability, and low robustness due to the influence of model selection, choice of explainability method, and the correlations within input data (Jiang et al., 2024a). Thus, it is important to explore how insights from related fields can be applied to quantitatively assess the validity of explainability analysis results in wildfire risk assessment models (Bommer et al., 2024). 

## **6. Deep Learning Methods for Wildfire Risk Prediction** 

Currently, methods for wildfire risk prediction include fire rating systems, statistical models, traditional machine learning, and deep learning approaches. Fire rating systems, extensively applied in regions like Canada, the USA, and Australia, combine empirical and mathematical modeling based on fluid dynamics, combustion, energy transfer, and factors like fuel, weather, and terrain conditions (Rezaie et al., 2023; Mell et al., 2007). These models are interpretable and generalizable, especially when training data is limited. However, their reliance on assumptions regarding soil moisture, fuel load, landscape structure, and other factors can reduce prediction accuracy (Bar Massada et al., 2011). 

For more specific analyses, statistical models use regression to establish relationships between wildfire risks and influenc- 

19 

ing factors such as fuel conditions, meteorology, and terrain. While simple and interpretable, they have limited capacity for handling the nonlinearity and randomness typical in wildfire prediction tasks (Li et al., 2022a). Traditional machine learning methods (e.g., Random Forests, SVM, ensemble models, and Bayesian methods) improve upon statistical models by using data-driven techniques and manual feature engineering to identify patterns in historical fire data. These methods operate non-parametrically and are better suited for non-linearities (Oliveira et al., 2021b), yet they present challenges in variable interpretation compared to statistical approaches. Over the past decade, the focus in wildfire modeling has shifted from statistical algorithms to machine learning (Jain et al., 2020; Oliveira et al., 2021b). Decision tree methods, such as Random Forests (RF), are particularly popular due to their accuracy and interpretability, as highlighted in studies like Malik et al. (2021). Nevertheless, some researchers argue that no single model is universally superior, suggesting a need for model combinations to enhance accuracy (Jaafari et al., 2019; Razavi Termeh et al., 2018). 

Traditional machine learning methods often use shallow architectures that fail to exploit spatial patterns effectively, limiting feature extraction and classification accuracy (Zhang et al., 2018). In contrast, deep learning models, despite their higher data requirements, can automatically extract complex features through hierarchical structures, reducing the need for manual feature engineering and enhancing generalizability. Their larger parameter capacity also allows them to manage large datasets and minimize overfitting risks. Although deep learning has become increasingly popular for wildfire risk prediction, reviews such as Jain et al. (2020) and Zacharakis and Tsihrintzis (2023) have only partially covered models like Recurrent Neural Networks (RNNs) and CNNs without a comprehensive systematization. 

This section reviews the latest advancements in deep learning-based wildfire risk prediction models, which are typically framed as segmentation or classification tasks. These models use historical wildfire data and influencing factors as inputs, with future wildfire occurrences or risk levels as ground truth. Models are categorized into time series prediction, image semantic segmentation and classification, and spatio-temporal prediction. Time series models (RNN, LSTM, Gated recurrent unit (GRU), Transformers) predict wildfire risks using 1D feature vectors, while semantic segmentation and classification models (CNNs, Transformers) employ 2D feature maps to produce 2D risk predictions. Spatio-temporal models integrate these approaches using 2D time series data. 

Deep learning models for spatio-temporal prediction often combine CNNs, Transformers, GCNs, and graph neural networks (GNNs) with RNNs, LSTMs, or GRUs, enhancing resolution with higher-resolution data over extended sequences. Despite advances in GPU technology supporting larger data scales, these models still struggle with efficiency and large spatiotemporal scales compared to newer models like Mamba (Gu and Dao, 2023). Additionally, many models use multi-branch networks that rely solely on images or nodes, missing the benefits of multimodal approaches like incorporating textual infor- 

mation. 

While previous reviews (e.g., Jain et al. (2020); Zacharakis and Tsihrintzis (2023)) have examined machine learning in wildfire science, they often omit post-processing techniques essential for converting model outputs into actionable risk information. Directly using these outputs can be misleading due to class imbalances and variability between models. This section also introduces methods for classifying and calibrating deep learning wildfire risk predictions to address these challenges. 

## _6.1. Wildfire Risk Rating and Probability Calibration_ 

Although Jain et al. (2020); Zacharakis and Tsihrintzis (2023) systematically reviewed the application of various machine learning methods in wildfire risk research, they did not provide a description of the post-processing techniques required to convert the predictions of machine learning models into actual wildfire risk. Directly using the output of these models as the probability of wildfire risk may lack theoretical foundation and stability. This is because wildfire historical data sets typically suffer from severe class imbalance, where the spatial and temporal scope of fire occurrences is considerably smaller compared to non-fire events. To expedite model convergence, many machine learning datasets are often constructed with a balanced class ratio, typically 1:1, 1:1.5, or 1:2 (Huot et al., 2021; Kondylatos et al., 2022) between fire and non-fire instances. This may lead to an overestimation of false positives during model evaluation (Phelps and Woolford, 2021b,a; Bakke et al., 2023). However, actual wildfire risk probabilities are usually much lower. For example, in wildfire risk assessments for the Mediterranean region and the United States, Ager et al. (2014a) and Preisler et al. (2004) used probabilities in the thousandths range, respectively. 

Using the probability output of machine learning models as an indicator of wildfire risk could be misleading to non-experts. Therefore, many studies convert continuous wildfire risk probabilities into risk levels to support wildfire management, such as conveying public warnings and guiding fire suppression measures. Among the methods for risk level classification, the Jenks natural breaks classification (Jenks and Caspall, 1971) is most commonly used. For instance, Xie et al. (2022b) trained an ensemble machine learning model using binary wildfire ignition records and then classified the predicted probabilities into five groups using the Jenks method. Similarly, Iban and Sekertekin (2022) and Moayedi and Khasmakhi (2023) also classified the hazard maps generated by machine learning models into five categories using the Jenks method. Along the same lines, Chen et al. (2024b) used the Jenks method to divide the estimated potential rate of spread and fire radiative power into five levels for wildfire risk assessment. 

Other methods have also been employed for risk level classification. For example, Liang et al. (2019) used the KennardStone method combined with standardized duration and fire size to categorize the wildfire risk predicted by an RNN into five levels. Jalilian and Jouibary (2023) applied natural discontinuity classification methods to group the probabilities predicted by machine learning models into three classes. Bjånes 

20 

et al. (2021) and Chicas et al. (2022) divided the wildfire ignition probability maps produced by the models into five levels using an equal-interval method, with intervals of 0.2. Similarly, Trucchia et al. (2022) manually defined five risk levels. 

In comparison to methods that predict risk classifications or directly utilize confidence levels from deterministic models as risk indicators, there remains a paucity of research focused on recalibrating probability outputs to obtain actual wildfire risk probabilities through post-processing and pre-processing of model predictions and inputs. For instance, Pelletier et al. (2023) constructed a semi-balanced dataset for model training, in which the numbers of burned and never-burned sites were 3,268 and 60,146, respectively. They then used the method proposed by Elkan (2001) (Eq. (10)) to convert the wildfire probabilities predicted by a time series XGBoost model into actual probability values: 



<!-- Start of picture text -->
BR 2 × ( p  − p  ×  BR 1)<br>p ′ = (10)<br>BR 1 − p  ×  BR 1 +  p  ×  BR 2 − BR 1 ×  BR 2<br><!-- End of picture text -->

where _p_<sup>′</sup> represents the revised probability for a prediction, _BR_ 1 is the base rate of the predicted probability estimates (the average of predicted probabilities for that class), and _BR_ 2 denotes the base rate of the actual probability estimates derived from the target population. Here, the target population refers to the average probability of fires across all observations within the training dataset, including the unburned observations that were not utilized in model training. After comparing the fire probabilities before and after calibration, they found that the calibrated probabilities more accurately reflected the true likelihood of wildfire occurrence. 

Similarly, Phelps and Woolford (2021a) used the function proposed by Dal Pozzolo et al. (2015) to correct the neural network’s probability output: 



<!-- Start of picture text -->
πγ k<br>pk = (11)<br>πγ k  − γ k  + 1<br><!-- End of picture text -->

where _pk_ and γ _k_ represent the wildfire probabilities modeled from the original and sampled distributions, respectively, and π denotes the proportion of non-fire observations sampled. Furthermore, this study also employed Platt Scaling and Offset methods to calibrate tree-based methods (bagged classification trees/random forest) and statistical models (logistic regression and logistic generalised additive models), respectively. The research ultimately found that uncalibrated machine learning models severely overestimate fire probabilities (e.g., predicted values several orders of magnitude higher than actual probabilities). 

Caron et al. (2024) propose a preprocessing method for calibrating wildfire ignition prediction probabilities. The core concept involves transforming binary fire events (occurrence or non-occurrence) into continuous fire risk intensity curves during the preprocessing phase, then mapping these through logistic regression models to produce calibrated probability predictions. This approach addresses class imbalance issues in wildfire risk prediction while avoiding the overestimation problems caused by sampling and uncalibrated models. Specifically, the 

research first applies a Laplacian convolution kernel to diffuse daily fire event sequences, thereby reducing the significance of isolated fire events while enhancing risk values for dates adjacent to continuous fire events. Subsequently, the authors calculate fire influence values for a given day using multi-scale sliding windows (Eq. (12)), incorporating both short-term and long-term trends. 



<!-- Start of picture text -->
T<br>1<br>Influence( J ) = � 2 t  + 1 � t Fires J + i (12)<br>t =1  i =− t <br><!-- End of picture text -->

where, _T_ and _J_ represent the maximum time window length and the current day, respectively, while Fires _J_ + _i_ indicates the number of fire events on day _J_ + _i_ . Subsequently, Influence( _J_ ) serves as input to a logistic regression model, which learns the relationship between this value and actual fire occurrences (0/1), yielding calibrated probability outputs. Evaluation of this method demonstrates excellent calibration performance. Assessment metrics include Log Loss and Expected Calibration Error (ECE). Compared to uncalibrated traditional classification models, this approach significantly reduces ECE (from approximately 10% to 2%–4%) while maintaining low Log Loss, proving that its predictions achieve a favorable balance between accuracy and reliability (Caron et al., 2024). 

In addition to the aforementioned methods, Zhang et al. (2025) introduced a two-stage parametric calibration framework specifically designed to address distributional shifts in deep learning-based drought detection, which is conceptually transferable to wildfire probability calibration. This two-step process corrects overconfident predictions by explicitly addressing spatial heterogeneity and sampling-induced class imbalance. In the first stage, they divided the study area into _N_ climate zones and fitted zone-specific logistic calibration functions to mitigate label prior shift. For each zone _Ki_ , the calibrated probability _p_ ˆ is computed as: 



<!-- Start of picture text -->
1<br>p ˆ = 1 + exp(− ai  · log 1− pp − bi ) , (13)<br><!-- End of picture text -->

where _p_ is the original model output (logit), and ( _ai_ , _bi_ ) are the learned parameters optimized by minimizing negative loglikelihood on zone-specific training samples. In the second stage, to correct likelihood shift across unseen validation data, they introduced a bias-corrected transformation: 



<!-- Start of picture text -->
β ˆ p<br>p ˜ = (14)<br>β ˆ p  − p ˆ + 1 ,<br><!-- End of picture text -->

where β is tuned by minimizing the ECE over binned confidence intervals. Experimental results demonstrated that this method achieved the lowest calibration error (ECE reduced from 4.06% to 0.31%), outperforming common techniques such as temperature scaling and Platt scaling. 

Notably, research on calibrating confidence scores from deterministic models into well-calibrated probability predictions remains limited in deep learning-based wildfire risk studies. This may be attributed to the growing preference for probabilistic deep learning methods—such as Bayesian neural networks—that inherently estimate predictive distributions. Com- 

21 

pared to deterministic models, probabilistic approaches typically exhibit superior calibration performance. They yield outputs that more accurately approximate true event probabilities while simultaneously quantifying both data-related (aleatoric) and model-related (epistemic) uncertainties. Related research on uncertainty estimation will be discussed in Section 7.1.3. 

## _6.2. Time Series Prediction_ 

## _6.2.1. Recurrent Neural Networks_ 

As discussed in previous sections, the occurrence and spread of wildfires are influenced by various factors, including meteorological conditions, fuel status, and historical wildfire data. These factors exhibit cumulative effects (Flannigan et al., 2013). Therefore, utilizing time series data enables models to capture the gradual changes in influencing factors, thus facilitating the prediction of future wildfire risks. The most classical methods in time series prediction tasks are RNNs, which include RNN, LSTM, and GRU. 

RNN is a basic neural network structure with recurrent connections, designed to process sequential data. RNN integrates input from the current time step with output from the previous time step to model and predict sequence data. A simple RNN structure consists of an input layer, hidden layer, and output layer. Input data are time series data, i.e., feature vectors with dimensions _f_ × _d_ . The hidden layer includes several hidden units, where each hidden unit outputs **h** _t_ − _m_ , the ’memory’ at any intermediate time _t_ − _m_ ( _m_ < _n_ ), as a weighted sum of its previous ’memory’ and current time step’s input features: 



<!-- Start of picture text -->
h t − m = σ h ( W IN x t − m  +  W HH h t −( m +1) +  b h )<br>(15)<br> y t − m = σ o ( W HO h t − m  +  b o )<br><!-- End of picture text -->

where **W** _IN_ and **W** _HH_ represent weight matrices for processing input to the hidden layer and from hidden layer to hidden layer, respectively; **x** _t_ − _m_ and **h** _t_ −( _m_ +1) represent the input feature vector at time _t_ − _m_ and ’memory’ from the previous time step, respectively; **b** _h_ and **b** _o_ represent bias vectors for the hidden units and output layer, respectively. Ultimately, the output **y** _t_ at time ( _t_ − _m_ ( _m_ < _n_ )) is a weighted sum of all hidden units. By iteratively repeating the above process, each timestep of the entire time series data ( _t_ − _n_ , _t_ − ( _n_ − 1), ..., _t_ − 1) is predicted. Finally, a loss function (Eq. 16) estimates the discrepancy between the prediction and labels, and model weight parameters are iteratively updated through backpropagation. 



<!-- Start of picture text -->
ι( y ,  GT ) = � t t − − 1 n ι t (( y t ,  GT t ) (16)<br><!-- End of picture text -->

where **GT** _t_ represents the label value at time _t_ . 

Classic RNN networks and their variants have been employed in wildfire risk prediction. For instance, Cheng and Wang (2008) designed a spatiotemporal Elman RNN-based prediction framework integrating historical wildfire and weather data to predict the annual average burned area in Canadian forests. Experiments demonstrated a prediction error of less than 0.5ha on areas of 500ha, validating the feasibility of using RNN for fire prediction. Similarly, a comparative study of ten ANNs based on meteorological data for predicting wildfire incidence in Australia found that Elman RNN exhibited the best 

performance, with average accuracy, sensitivity, and specificity exceeding 93% (Dutta et al., 2013). Furthermore, a network composed of a dynamic autoencoder and RNN was used to predict the next month’s burned area in five U.S. regions, where the dynamic autoencoder was employed to transform multidimensional time series data into RNN input features, and dual decoders were used for predicting fire spot likelihood over different time spans, i.e., one week and one month. Experiments showed that their method was slightly superior to comparative methods, generative network, and GRU (Chavalithumrong et al., 2021). 

While Jain et al. (2020) and others have highlighted the limited use of classical RNNs, our findings are consistent with these observations. The underutilization of RNNs may be attributed to their difficulties in handling long sequence data, where they are prone to gradient vanishing or exploding, making it challenging to capture long-term dependencies (Hochreiter, 1997; Gers et al., 2000). To address these issues, LSTM networks were developed. LSTMs incorporate three gating units: input gate, forget gate, and output gate, which control the flow and retention of information. These gates have trainable weights and decide whether to pass, forget, or output information based on the current input and the output from the previous time steps. This gating mechanism effectively resolves the issues of vanishing and exploding gradients, thereby enabling better handling of long sequences and capturing of long-term dependencies. Consequently, LSTMs are more prevalently applied in wildfire risk prediction than classical RNNs. 

Studies utilizing LSTM for wildfire risk prediction often model various risk factors, including weather and climate conditions, fuel conditions, and socio-economic factors. For instance, Liang et al. (2019) found that LSTM outperformed RNN and Back Propagation Neural Network (BPNN) in predicting the class of wildfires in Alberta, Canada, based on meteorological conditions, achieving an overall accuracy of 90.9%. Similar findings were reported by Natekar et al. (2021), who assessed the wildfire risk in Indian forests using meteorological parameters and LSTM methods. The accuracy and RMSE were 94.77% and 37.5%, respectively, surpassing other benchmark methods like CNN and SVM. Additionally, Kondylatos et al. (2022) compared RF, XGBoost, and deep learning methods (LSTM and ConvLSTM) and found that deep learning significantly outperformed traditional machine learning methods in predicting next day wildfires in the Mediterranean using ERA5Land meteorological data, MODIS NDVI, and diurnal LST data along with soil moisture, terrain data, land cover types, and distances from infrastructure. Li et al. (2023b) further integrated attention mechanisms and deep learning interpretability into an LSTM network, using monthly-scale climate, socio-economic, fuel variables, and oceanic indices to predict short-term (1–4 months) and long-term (5–8 months) wildfire burning areas in tropical regions. Experimental results demonstrated that the enhanced LSTM model outperformed traditional machine learning methods and the baseline LSTM model. Furthermore, Cheng et al. (2022, 2024) have combined LSTM with reduced order modeling techniques to improve the prediction accuracy for both regional and global scale wildfire systems. Addition- 

22 

ally, interpretability analysis revealed that precipitation and vapor pressure deficit were critical driving factors, while oceanic indices provided more significant contributions to long-term wildfire burning area predictions. 

Moreover, some studies use only historical wildfire occurrence data combined with LSTM to predict future regional wildfire risks. For example, Kadir et al. (2023) used historical MODIS wildfire data combined with LSTM to predict the spatiotemporal distribution of wildfires in Indonesia for the following year, with a success rate exceeding 90% and an error rate of only 6.94%. Notably, to reduce the amount of data, this study grouped several days’ worth of data into single days for training and testing. Furthermore, Hu et al. (2023a) combined LSTM with autoencoders, using historical wildfire data from 1992-2018 to predict the level of wildfire occurrence in highrisk areas such as California. The autoencoder was employed to generalize wildfire events from the overall dataset, enhancing the accuracy of anomaly event predictions through reconstruction errors. 

Similar to the LSTM, the GRU addresses the challenges of gradient vanishing and explosion inherent in traditional RNNs through its gating mechanisms. GRU reduces the number of gating units found in LSTM, containing only a reset gate and an update gate which simplifies the model architecture and enhances computational efficiency (Chung et al., 2014). Despite its simpler configuration, GRU retains the capability to model long-term dependencies with performance comparable to that of LSTM (Jin et al., 2020a). 

Studies such as Dzulhijjah et al. (2023) have compared the performance of LSTM, BiLSTM, CNN-LSTM, StackedLSTM, and GRU in predicting wildfire risk in the Indonesian region of Kalimantan, finding that GRU slightly outperformed the other models, though the advantage is not significant. In contrast, Gopu et al. (2023) observed better results with LSTM in a comparative study of wildfire prediction in the Montesinho Natural Park, Portugal. Additionally, Chavalithumrong et al. (2021) found that models integrating a dynamic autoencoder with RNN outperformed standard GRU models, suggesting that enhanced RNN architectures can offer superior performance. 

_6.2.2. Transformers for Wildfire Risk Prediction_ 

Transformers utilize multi-head self-attention mechanisms to calculate attention scores, enabling them to capture dependencies at any position within the sequence (Vaswani et al., 2017). The attention mechanism is defined as: 



<!-- Start of picture text -->
Attention( Q ,  K ,  V ) = softmax V (17)<br>� Q √ KdTk �<br><!-- End of picture text -->

where _dk_ represents the dimensionality of the key. The architecture of a Transformer comprises encoders, decoders, positional encoding, and multiple attention mechanisms. 

Transformers operate on sequences transformed into tokens, which are then embedded with positional encoding to maintain the sequence order absent in traditional RNNs. The sequence of embedded tokens is processed by the encoder, which transforms it into a context vector using layers of multi-head self-attention 

and feed-forward networks. The decoder similarly processes the context vector to predict the output sequence. The ability of Transformers to process sequence data without relying on sequential processing allows for parallel computation during training, significantly speeding up the learning process compared to RNNs (Vaswani et al., 2017). This makes them particularly effective for long-sequence predictions or complex scenarios requiring modelling of long-range dependencies (Zerveas et al., 2021; Prapas et al., 2023). 

Transformers been adapted for several predictive tasks in wildfire risk prediction. For example, Miao et al. (2023) developed a Transformer model with a window-based attention mechanism to predict forest fire risks in Chongli District, Beijing, China, using time-series data of meteorological, topographical, vegetation, and anthropogenic factors. The window mechanism confines attention to a fixed-size window centered on each element, reducing computational complexity and memory usage. Similarly, Cao et al. (2024) employed a Transformer to predict next-day wildfire risks in Quanzhou County, Guangxi Province, China, based on three days of meteorological, topographical, and human activity data. The model’s performance, analyzed using IGR, outperformed LSTM, RNN, and SVM in terms of generalization, noise resistance, and overfitting mitigation. 

From the analysis above, it is evident that both RNNs and GRUs are less frequently used in wildfire risk prediction, which includes forecasting occurrences, susceptibility, and spread. In contrast, LSTM networks have a relatively higher usage rate. RNNs, compared to LSTMs, are particularly challenged by issues such as vanishing and exploding gradients and exhibit weaker capabilities in modeling long-distance dependencies. Furthermore, although some studies argue that GRUs perform comparably to LSTMs (Viswanathan et al., 2019; Gao et al., 2020; Liu et al., 2021a; Gao et al., 2021; Zarzycki and Ławry´nczuk, 2022), the simplified structure of GRUs may result in inferior performance when processing highly complex sequences or capturing intricate relationships (Cahuantzi et al., 2023), especially in wildfire risk prediction tasks that do not require high real-time processing capabilities or are intended for edge computing devices. Recently, however, with the advent of Transformers, these models are gaining popularity in wildfire risk prediction due to their complex architecture, larger parameter capacity, and the advantages of parallel computation. 

## _6.3. Image Semantic Segmentation and Classification Methods_ 

Although RNNs and Transformers excel at capturing temporal dependencies for sequence-to-sequence learning tasks, these methods primarily classify individual pixels’ temporal sequence data. However, wildfire occurrences are not only influenced by local conditions but also by neighboring areas (e.g., wind propagation). When RNNs use 1D data inputs, the spatial structure of the image is often lost (Hu et al., 2020). Consequently, several studies have explored the use of image semantic segmentation and classification methods, such as CNNs, GNNs, and Transformers, to predict wildfire risk at time _t_ using the influencing factors (e.g., fuel, weather) from time _t_<sup>′</sup> < _t_ . These methods rely on 2D image inputs, which explicitly model 

23 

the spatial dependencies of input features, while also implicitly modeling the influence of current driving factors on future wildfire risk by having different input features and predicted time steps. In wildfire risk prediction, CNNs are commonly used, with GNNs and Transformers increasingly adopted in recent studies. 

## _6.3.1. Convolutional Neural Networks_ 

CNNs are foundational network structures in deep learning, designed to extract local spatial features through convolution operations, making them well-suited for capturing the spatial information necessary for wildfire risk prediction, as shown in Fig 4. For example, Zhang et al. (2019) employed a modified AlexNet (Krizhevsky et al., 2012) using annual fire point maps and springtime mean influencing factors for Yunnan Province, China, to classify image patches as wildfire-prone areas. The model outputs a probability map of wildfire risk through softmax mapping in the final CNN layer. When comparing the CNN model’s performance with RF, SVM, MLP, and kernel logistic regression models, the authors found that CNN achieved the highest overall accuracy. They also analyzed the contributions of various wildfire drivers using the information gain ratio, identifying temperature, wind speed, surface roughness, precipitation, and elevation as the most influential factors. 

Building upon this, the authors extended the modified AlexNet to generate a global quarterly wildfire susceptibility map (Zhang et al., 2021a). They compared its performance with MLP-2D, CNN-1D, and MLP-1D models, finding that CNN2D and MLP-1D models outperformed CNN-1D and MLP-2D. Additionally, they applied an improved permutation importance (PI) method and partial dependence plots (PDPs) to investigate the interpretability of the CNN-2D model. The PI analysis highlighted that maximum monthly temperature, soil temperature, NDVI, and soil moisture were significant factors affecting the model. Furthermore, PDP analysis revealed a negative relationship between cumulative precipitation and wildfire probability, while maximum monthly temperature and soil temperature positively influenced wildfire occurrence. 

Moreover, using a similar CNN approach, they predicted the spatiotemporal variation of wildfire risk under different climate scenarios, discovering that global warming would lead to an increase in burned areas and a northward shift of wildfire-prone regions (Zhang et al., 2024a). In another study, Kanwal et al. 



Figure 4: The architecture of CNN classification network where the center pixel is classified using surrounding information (Zhang et al., 2019). 

(2023) explored CNN-1D and CNN-2D classification models along with other machine learning algorithms for evaluating seasonal wildfire risks in Pakistan, finding that CNN-2D outperformed CNN-1D and other machine learning algorithms. 

In addition, some studies have employed deeper or structurally optimized CNN networks. For instance, Oak et al. (2024) utilized VGG16 with ReLU, BatchNorm, Dropout, and a sigmoid layer to predict wildfire susceptibility in Quebec, Canada. Comparative experiments demonstrated that this model outperformed other architectures like Xception, VGG16, ResNet50, and Inception V3. Similarly, Nur et al. (2022) applied a meta-heuristic optimization algorithm to fine-tune the hyperparameters of a CNN model for wildfire susceptibility mapping in the Plumas National Forest, USA. Their IGR analysis revealed that land use, drought index, and maximum temperature had the greatest impact on wildfire susceptibility, and the model’s performance improved significantly after optimization. 

Beyond classification-based methods, some studies have implemented end-to-end models for higher-resolution predictions. For example, Hodges and Lattimer (2019) proposed a deep convolutional inverse graphic network comprising convolution and deconvolution layers to simulate wildfire spread over homogeneous and heterogeneous landscapes for 6-hour and 24-hour intervals, demonstrating the high efficiency of CNNs in wildfire spread prediction. Similarly, Santopaolo et al. (2021) employed an end-to-end CNN-based image segmentation model to predict wildfire risk in Sicily, Italy, and California, USA, using the average values of driving factors over the preceding eight days. 

Furthermore, Allaire et al. (2021) developed a hybrid architecture combining convolutional and fully connected layers to emulate the output of a numerical fire spread simulator based on the Rothermel model of fire propagation. Similarly, Bergado et al. (2021) designed an AllConvNet, a fully convolutional network, to predict wildfire burn probability for the next 7 days in Victoria, Australia. This model achieved higher prediction accuracy compared to logistic regression, SegNet, and MLP models. Feature extraction and normalization of logistic regression coefficients revealed that total rainfall, lightning density, and surface temperature were among the most influential variables. 

Additionally, Li et al. (2023c) introduced spatial and channel attention mechanisms to enhance an end-to-end CNN model’s focus on critical features while suppressing irrelevant ones for predicting the next moment’s wildfire spread. This model also incorporated the burning map from the previous time step, outperforming other CNN models and ConvLSTM. Similarly, Shadrin et al. (2024) used the MA-Net segmentation model, which includes position attention and multi-scale attention blocks, to predict wildfire extent for the next 1-5 days. Unlike previous studies, they included short-term weather forecasts along with various wildfire drivers. Experimental results showed that their model accurately predicted wildfire spread within 3 days, with the wind components, land cover, NDVI, EVI, and LAI being the most influential factors. 

Lastly, Marjani et al. (2024a) combined CNN with atrous spatial pyramid pooling to model wildfires at different scales and shapes, adopting an end-to-end approach for next-day wildfire spread prediction. They used linear regression and Grad- 

24 

CAM heatmap correlations to demonstrate how different dilation rates help extract both large-scale and small-scale wildfires. Similarly, Jiang et al. (2023) employed a three-branch network to process static DEM and fuel data, dynamic wind speed, temperature, humidity data, and the previous time step’s wildfire status. Their experiments showed that this model’s inference efficiency significantly surpassed that of cellular automata and Farsite models, accurately predicting burned areas in real wildfire scenarios. 

## _6.3.2. Other Methods_ 

In addition to CNNs, other image segmentation methods, such as GNNs and Transformers, have also been applied to wildfire risk prediction. GNNs, compared to CNNs, are better suited for handling non-Euclidean structured data (Asif et al., 2021), while Transformers’ multi-head self-attention mechanisms are more effective in modeling long-range semantic dependencies within images (Vaswani et al., 2017). For example, Jiang et al. (2022) proposed using an irregular graph network to simulate wildfire spread in variable-scale landscapes, addressing the issue of fixed-grid data being unable to adaptively differentiate landscape heterogeneity. The model adjusts graph node density based on terrain complexity to achieve uniformity in nodes and edges at varying scales. Comparative experiments with cellular automata and FARSITE demonstrated that the proposed model exhibits competitive accuracy and efficiency. 

Additionally, Chen et al. (2022) incorporated a GNN into the knowledge graph framework proposed by Ge et al. (2022) to enable automated learning and prediction of burn areas. Specifically, the model first constructs a knowledge graph in triples and uses RotaE to compute representation vectors for each entity. These entity vectors are associated with nodes in the graph, and the vectors are subsequently fed into the GNN to facilitate automatic updates. Finally, link prediction algorithms are employed to predict the burn areas associated with the recorded nodes. Experiments conducted in Portugal’s Montesinho Natural Park demonstrated that this algorithm significantly outperformed traditional machine learning algorithms such as RF, SVM, and MLP. 

Moreover, Li and Rad (2024) introduced spatial attention mechanisms and focal modulation into a U-shaped encoderdecoder network based on Transformers, known as Swin Unet. This end-to-end image segmentation approach utilizes wildfire risk driving factors from the previous day to predict wildfire risk for the following day across the continental United States. Comparative experiments using the extended Next Day Wildfire Spread dataset (Huot et al., 2022) showed that this model outperforms baseline models, including the standard UNet and Swin Unet. In addition, Prapas et al. (2023) introduced a TeleViT model that incorporates teleconnections to model longrange spatial interactions globally, aiming to predict subseasonal to seasonal wildfire patterns. This model combines fine-grained local-scale inputs with coarse-grained global-scale data, improving prediction accuracy for global wildfire patterns up to four months in advance. 

While deep learning-based wildfire risk prediction methods often overlap in their reliance on similar wildfire driving data, 

they do not typically distinguish between wildfire spread simulation and broader wildfire risk prediction, as defined in Section 2.2 of this manuscript. Wildfire spread simulation models are generally tailored to specific scenarios, such as predicting the dynamics of fire spread from known or predefined ignition points in localized regions like parks or mountainous areas (Kondylatos et al., 2023; Jiang et al., 2023; Li et al., 2023c; Marjani et al., 2024a). In contrast, wildfire risk prediction models aim to identify areas with potential ignition points or high susceptibility to fire spread, explicitly incorporating the stochastic nature of ignition events. This approach allows for a comprehensive assessment of fire risk by considering both ignition probability and subsequent spread potential. Moreover, wildfire risk prediction accommodates a wider range of spatial scales, from local parks to provincial, national, continental, or even global levels (Santopaolo et al., 2021; Bergado et al., 2021; Chen et al., 2022; Prapas et al., 2023). This adaptability, coupled with the ability to model stochastic ignition events, highlights the broader applicability and versatility of risk prediction models for large-scale wildfire management. 

Additionally, the training process for deep learning-based spread simulation models often involves datasets of discrete historical wildfire events combined with associated driving data, which can limit generalization across diverse wildfire scenarios (Huot et al., 2022; Prapas et al., 2022; Kondylatos et al., 2023). Consequently, while spread simulation methods offer precise fire spread modeling for individual events, their predictive performance tends to be less robust when applied to large-scale wildfire risk assessments (Gerard et al., 2023). This distinction underlines the need for improved methodologies explicitly designed for large-scale and long-term wildfire risk prediction, ensuring scalability and reliability across varying geographies and timeframes. 

## _6.4. Spatiotemporal Prediction Methods_ 

The previously discussed time series prediction methods and image segmentation/classification methods each have their strengths in capturing temporal and spatial dependencies, respectively. However, they are unable to simultaneously handle both spatial and temporal dependencies and capture the complex cross-spatiotemporal interaction patterns. For instance, Prapas et al. (2021) pointed out that focusing only on spatial scale modeling could overestimate a model’s real-world performance. To integrate spatial structure and time series data, many studies have attempted to combine CNN, GNN, and Transformer models with RNN, LSTM, and GRU methods. This transforms the task of time series prediction or spatially localized optimization between consecutive wildfire states (Jiang et al., 2023) into spatiotemporal sequence prediction tasks. There are three primary approaches to achieving this combination: separated spatial and temporal modeling, coupled spatiotemporal modeling, and spatially enhanced coupled spatiotemporal modeling. 

Specifically, separated spatial and temporal modeling involves abstracting spatial features into 1D feature vectors using spatial modeling methods, which are then input into temporal prediction models. Coupled spatiotemporal modeling con- 

25 

verts the 1D tensors in RNNs into 3D tensors, incorporating spatial dimensions (rows and columns) and using convolutions or graphs (instead of weight matrix multiplication) to determine a grid cell’s future state based on its neighbors’ current and past states. Lastly, spatially enhanced coupled spatiotemporal modeling introduces CNNs or graph-based methods to extract spatial features before the spatiotemporal modeling stage. 

_6.4.1. Separated Spatial and Temporal Modeling Methods_ 

The approach of separately extracting spatial and temporal features is widely adopted in wildfire risk prediction. A typical architecture of such a spatiotemporal model is illustrated in Fig. 5. The model takes as input spatial data composed of multiple driving factors across _n_ time steps ( _T_ 1 through _Tn_ ), represented as tensors with dimensions height ( _H_ ), width ( _W_ ), and number of drivers ( _C_ ). Each temporal slice is processed by parallel spatial feature extraction modules, either with shared or independent weights. The resulting spatial features are then aggregated through a multi-temporal feature fusion stage, during which the original spatial resolution _H_ × _W_ is typically reduced to a global representation (e.g., 1×1). This fused representation is then passed through a temporal feature extraction module to capture dynamic patterns across the time sequence. Finally, the integrated spatiotemporal features are input into a prediction head to produce the final wildfire risk assessment. 



Figure 5: The diagram of the separated spatial and temporal modeling method. 

Typically, multiple CNNs are employed to process multidimensional spatial images at each time step, with dimensionality reduction applied before feeding the data into the LSTM. Finally, the output from the LSTM is mapped to output probabilities using a CNN, or directly without it, along with the application of a sigmoid function. This architecture effectively leverages both the spatial pattern recognition capabilities of CNNs and the sequential modeling strengths of LSTMs to capture the complex spatiotemporal dynamics inherent in wildfire systems. 

This method is widely used in wildfire risk prediction. For example, Jin et al. (2020b) proposed enhancing spatial feature extraction by employing CNNs and GCNs to extract spatial information, which is then passed through a feed-forward network to unify the data into a 1D vector before being input into a GRU. The output 1D vector is then restored to its original 

size using deconvolution layers, performing urban fire situation prediction through an end-to-end semantic segmentation approach. Compared to traditional machine learning methods like RF and XGBoost, as well as GRUN and Conv-GRUN, this model showed significant performance improvements. 

Similarly, Huot et al. (2021) used the Next Day Wildfire Spread dataset and categorized wildfire risk prediction into two tasks: next-day wildfire probability prediction and final burning area prediction. They experimented with four models: convolutional autoencoder and residual UNet for segmentation, and convolutional autoencoder and residual UNet combined with LSTM for temporal prediction. The results showed that, among the segmentation models, the convolutional autoencoder outperformed UNet. When combining the two models with LSTM for final burning area prediction, there was no significant performance difference between the models. 

Zhang et al. (2022) designed and compared four deep neural networks with identical structures but different depths, combining 2D CNN and LSTM models to predict global monthly burned area maps using seven meteorological and two biophysical predictors from the previous 12 months. Each model reduced spatial dimensions through convolution and max-pooling operations and used fully connected layers to flatten the input patches into 1D features before feeding them into LSTM layers. The primary difference among the models was the number of CNN and LSTM layers. Ultimately, the CNN-LSTM network with two convolutional layers and two LSTM layers was selected for its balance of performance and efficiency. The results showed that the combination of convolution and LSTM methods outperformed standalone LSTM and CNN models. 

Furthermore, Marjani et al. (2024b) combined CNN with bidirectional LSTM (BiLSTM) for a study in Australia, using wildfire driving factors from the previous four days and wildfire masks to predict next-day wildfire spread. The method first employed four CNN layers to extract spatial features, which were then flattened and input into a three-layer BiLSTM. The model produced binary outputs through dilated convolution, dense layers, and sigmoid activation functions. Comparative experiments demonstrated that this approach outperformed LSTM and Conv-LSTM methods, and the study also confirmed that using longer time steps improved prediction capabilities. In another study, Li et al. (2021c) not only introduced a CNN before the LSTM but also incorporated an attention mechanism within the LSTM to assign different weights to the hidden states, reducing information loss and improving prediction accuracy. Applied in Portugal’s Montesinho Natural Park, the model used various meteorological factors from the FWI, historical burned areas, and time and location data to predict future wildfire risk. Comparisons with SVM, XGBoost, neural networks, RNN, and basic LSTM showed that deep learning models significantly outperformed machine learning models, with LSTM surpassing RNN and the CNN-attention LSTM performing best overall. 

Rösch et al. (2024) applied graph convolution combined with GRU to develop Spatiotemporal Graph Neural Networks (ST-GNNs) for predicting wildfire spread in Portugal and the Mediterranean region. These models used an H3 grid system 

26 

built from weather data, land cover, fuel types, DEM, and fire weather indices. However, the models exhibited high false positive rates. 

In another study, Bhowmik et al. (2023) proposed a U-shaped LSTM network combining UNet and LSTM, using seven days of meteorological, environmental, vegetation, and geological data to predict wildfire risk. The U-shaped LSTM network first used a three-layer UNet encoder to extract semantic information, which was then flattened and input into an LSTM. The LSTM output was passed through a UNet decoder to produce end-to-end pixel-level predictions of wildfire heatmaps for the next 24 hours to two weeks. This model achieved over 97% accuracy in predicting large-scale wildfires in California, outperforming CNN models. 

Similarly, Yoon and Voulgaris (2022) conducted research on wildfire risk prediction in the western United States, using a convolutional encoder to reduce the dimensionality of input time series data into vectors, which were then fed into a GRU model. A dual deconvolution decoder was designed to restore image size, predicting wildfire risk at different time steps (one, two, three, and four weeks). Compared to logistic regression, generative networks, and GRU, the combination of CNN and GRU showed significant performance improvement. 

Lastly, Marjani et al. (2023) developed a spatiotemporal prediction model combining CNNs and RNNs to predict wildfire spread at time step _t_ + 1, using environmental variables and burned areas from time steps _t_ and _t_ − 1. Data were divided into three blocks: hourly block (6-hour averaged wind speed and direction), daily block (temperature, precipitation, and wildfire burning map), and constant variables (land cover type, population, terrain, etc.). Each block was processed by CNNs and flattened into 1D features, then fed into RNNs with 64 and 31 neurons, respectively. Constant variables were similarly processed and flattened. The RNN outputs were concatenated with the constant variables and passed through convolution, reshape, dropout, and sigmoid layers to produce a burning probability map. Comparative results showed the superiority of this spatiotemporal modeling approach over CNN and the deep convolutional inverse graphics network proposed by Hodges and Lattimer (2019). Additionally, experiments assessing data availability, noise addition, and Monte Carlo dropout were conducted to evaluate model uncertainty. 

## _6.4.2. Coupled Spatiotemporal Modeling Methods_ 

Compared to the separated spatial and temporal modeling methods, time-series prediction algorithms like ConvLSTM are also widely used. For instance, Burge et al. (2021) evaluated the feasibility of using ConvLSTM to simulate wildfire propagation dynamics on three simulated datasets with varying terrain, wind, humidity, and vegetation density distributions. The experiments demonstrated that ConvLSTM’s predictive capability surpassed that of CNN. In the study by Prapas et al. (2021), which compared traditional machine learning models (RF), time series prediction algorithms (LSTM), image classification methods (CNN), and spatiotemporal modeling methods (ConvLSTM) for next-day wildfire danger prediction across 

Greece, several key findings emerged. For the RF model, training data was constructed by averaging each driving factor for the 10 days preceding the prediction date at each spatial location, resulting in a dataset with dimensions _f_ × 1, where _f_ is the number of driving factors. The LSTM model used time series input, with data dimensions of _f_ × _t_ , where _t_ represents the time series length (10 days). For the image classification task, the spatial data was constructed as spatial patches centered on the target point, with dimensions _f_ × _h_ × _w_ , where _h_ and _w_ are the height and width of the image. Lastly, for the spatiotemporal prediction task using ConvLSTM, the dataset dimensions were 

_f_ × _h_ × _w_ × _t_ . The results showed that LSTM and ConvLSTM performed better than RF and CNN. Evaluating the binary classification results, LSTM outperformed ConvLSTM overall, but when using the area under the ROC curve as the evaluation metric, ConvLSTM slightly surpassed LSTM, with AUC scores of 0.926 and 0.920, respectively. 

Similarly, Khalaf et al. (2024) compared ConvLSTM with cellular automata and FlamMap in simulating wildfire spread in Iran’s Golestan National Park. The results indicated that ConvLSTM had the highest accuracy in predicting burned areas, but for spread rate evaluation, the CA algorithm performed better than the other models. In another study, Michail et al. (2024) compared temporally-enabled GNN, GRU, and ConvLSTM using the SeasFire Datacube (Alonso et al., 2023), finding that GNN was better at capturing global information, thus improving the understanding of complex patterns. The study also emphasized the importance of long time series information and a large receptive field in global wildfire risk prediction, especially for seasonal forecasts. It showed that longer input sequences provided more reliable predictions, and integrating spatial information to capture the spatiotemporal dynamics of wildfires improved model performance. Therefore, to improve predictions over longer forecast horizons, it is essential to consider a larger spatial receptive field. 

Masrur and Yu (2023); Masrur et al. (2024) further proposed two ConvLSTM models based on spatiotemporal attention to predict wildfire spread over the next 10 days using the previous 10 days’ NDVI, wind components, and soil moisture. These models were designed to capture local-to-global and short-to-long-term spatiotemporal dependencies. The models were trained and tested on both simulated and real-world datasets. Pairwise self-attention was used to calculate attention scores for input variables, while patchwise self-attention replaced convolution operations in ConvLSTM. Comparisons on simulated datasets showed that the pairwise self-attention model performed better, while the standard ConvLSTM outperformed the patchwise self-attention model. Moreover, they employed integrated gradients (Sundararajan et al., 2017) to enhance the interpretability of the contributions of time steps and driving factors to the model’s predictions. The spatial patterns from integrated gradients confirmed the importance of capturing both local and global spatial dependencies. However, in real-world scenarios, replacing ConvLSTM’s convolution operations with patchwise self-attention significantly improved the standard ConvLSTM’s prediction accuracy and model transferability, surpassing even the pairwise self-attention ConvLSTM 

27 

in both aspects. 

Finally, Eddin et al. (2023) designed two separate convolutional branches to process dynamic variables (those changing over time) and static variables (those remaining constant throughout the study period). To address the causal effects of static variables on dynamic ones, they incorporated a locationaware adaptive normalization layer that adjusts the activation maps in the dynamic branch based on static features. They also employed sinusoidal encoding of Julian days to provide the model with explicit temporal information. Their experiments on the FireCube dataset (Prapas et al., 2022; Kondylatos et al., 2023), which covers parts of the Mediterranean, demonstrated that the proposed model’s predictions of wildfire spread at time _t_ + 1 outperformed baseline models, including LSTM, ConvLSTM, RF, and XGBoost. In a similar vein, Dong et al. (2024) proposed an architecture that models dynamic and static variables separately during the encoding phase, leading to improved accuracy in predicting fire radiative power. 

_6.4.3. Spatially Enhanced Coupled Spatiotemporal Modeling Methods_ 

In addition, there are studies that combine convolutional layers with ConvLSTM to further emphasize spatial feature extraction. Similar to the separated spatial and temporal sequence wildfire risk prediction models, the spatially enhanced coupled spatiotemporal wildfire risk prediction method, as shown in Fig. 6, first extracts spatial features using methods such as convolution operations. Dimensionality reduction is then applied before feeding the data into a temporal model, such as ConvLSTM. The output of the temporal model can then be processed by a convolutional block followed by a sigmoid mapping, or directly mapped using a sigmoid function, depending on the specific design. Compared to the separated spatial and temporal modeling approach, this method tends to preserve a certain level of spatial information throughout the modeling process, which may help retain finer-grained spatial patterns in the final prediction. 



Figure 6: A typical spatial feature-enhanced coupled spatiotemporal wildfire risk prediction model diagram. 

For example, Deng et al. (2023) used terrain, vegetation, climate, and human activity factors in Yunnan Province, China, 

to build a 3D CNN and ConvLSTM hybrid model for next-day wildfire prediction. During data preprocessing, Pearson correlation analysis was used to exclude the minimum and average temperatures from the dataset. Variance inflation factors and tolerance were then employed to assess multicollinearity among wildfire driving factors. Information gain ratio analysis revealed that precipitation and slope had the highest impact. In the proposed model, 3D CNN was primarily responsible for extracting spatial features and reducing the input patch’s spatial dimensions, which were then fed into a many-to-many ConvLSTM for prediction. The results showed that the combined 3D CNN and ConvLSTM model outperformed both standalone ConvLSTM and 3D CNN models. 

Similarly, Burge et al. (2023) built upon the model proposed by Hodges and Lattimer (2019) by introducing fuel embedding layers and inserting ConvLSTM between the encoder and decoder for end-to-end wildfire spread simulation. The experimental results demonstrated that incorporating LSTM improved prediction accuracy. 

Furthermore, Ji et al. (2024b), following a similar branch structure to Eddin et al. (2023) and Jiang et al. (2023), proposed a static location-aware model based on ConvLSTM. This model aimed to integrate global static features (sine and cosine values of longitude and latitude, along with climate variables) with dynamic variables (e.g., meteorological, human, and vegetation cover factors) to predict global wildfire probability on sub-seasonal to seasonal scales. In this model, global static features were first convolved and max-pooled, and the resulting feature maps were multiplied with climate variables for data fusion. SKNet was then employed to extract higher-order features, which were upsampled and merged with the static features generated by the encoder. Finally, upsampling and skip connections were used to restore the image size and supplement the spatial details of global static location variables. The dynamic and static variables were concatenated and input into ConvLSTM. The hidden state output from the last time step of ConvLSTM was combined with the static and global features, and a 1×1 convolution was applied to produce the final wildfire probability prediction. Comparing accuracy, recall, F1 score, precision, and Kappa coefficient with different variants of Vision Transformer and ConvLSTM demonstrated the effectiveness of incorporating global location information and climate variables for enhancing predictive capabilities. 

Similarly, He et al. (2024) developed a next-day wildfire risk prediction model for eastern China by combining CNN, ConvLSTM, and Vision Transformer models, also employing a branch structure. In this model, eight CNN modules were used to model eight meteorological variables, while another CNN module modeled terrain, vegetation, and anthropogenic factors from the last day of each time step. The sequence feature maps generated by the temporal meteorological variables were input into LSTM, and its output was merged with the other variables’ CNN outputs. Channel attention, spatial attention, and CNN were used to extract higher-order features. To emphasize the high-resolution structural features of vegetation and scattered small settlements, Landsat data were used to generate 30-meter monthly high-resolution NDVI products, 

28 

and a Vision Transformer was applied to extract these structural features. The flattened outputs from the Vision Transformer and CNN were concatenated and classified using an ANN binary classifier. Ablation studies demonstrated the effectiveness of incorporating attention mechanisms, high-resolution spatial structure features, and Vision Transformer. Sensitivity analysis also confirmed that meteorological factors were the most important among wildfire drivers. 

Finally, Chen et al. (2024a) designed an end-to-end encoderdecoder network structure similar to that of Bhowmik et al. (2023) and Yoon and Voulgaris (2022), combining GCN and ConvLSTM. The GCN component was introduced to model the long-distance spatial dependencies required for global wildfire risk prediction, while mitigating the impact of missing data from ocean regions. Explicitly modeling information flow through the graph edges improved the interpretability of the prediction results. Specifically, the Earth’s land surface pixels, as simulated by the JULES-INFERNO model, were treated as graph nodes, and the correlation coefficients between nodes were used to establish the graph’s edges. Spatial dependencies were modeled using a spatial graph convolution model, followed by LSTM for long-term temporal dependencies. The model was trained and validated using 30 years of simulated data from 1961 to 1990 in the JULES-INFERNO dataset, and its performance was compared against LSTM, ConvLSTM, and convolutional autoencoder with LSTM. The proposed model demonstrated superior performance, with ConvLSTM being the best among the comparative models. Additionally, the study used the Louvain method to identify potential wildfire communities, and integrated gradient analysis revealed that short-term (one-month) wildfire risk is primarily driven by lightning, while long-term (11-month) risk is more influenced by temperature, followed by lightning. Node importance analysis also showed that even geographically distant locations could have strong interactions regarding wildfire risk. Similarly, Zhao et al. (2024) aimed to improve model interpretability by combining causal GNN with LSTM, comparing its performance with LSTM and GRU in predicting future wildfire risk. 

This section reviews recent advancements in deep learning methods applied to wildfire risk prediction, emphasizing their evolution from temporal and spatial modeling to spatiotemporal sequence modeling and the integration of emerging technologies. Due to their hierarchical structures and flexible architectures (LeCun et al., 2015), deep learning models excel at capturing nonlinear relationships, enabling them to model the complex interactions and latent patterns within highdimensional spatiotemporal data sourced from meteorological variables, vegetation indices, topographical features, and socioeconomic factors. Unlike traditional statistical models that rely on explicit feature engineering and linear assumptions, deep learning models uncover intricate dependencies that are difficult to detect using linear or shallow frameworks. This capability is particularly crucial in wildfire risk prediction, where the interdependencies among driving factors often exhibit nonlinear behaviors that vary dynamically across both temporal and spatial scales (Jain et al., 2020). 

The evolution of deep learning models in this domain demon- 

strates significant strides in both predictive accuracy and computational efficiency (Cheng et al., 2024). Early applications relied on RNNs and LSTM networks to process wildfire time series data, while CNNs and GCNs were used to extract spatial features. Recent innovations have merged these approaches into hybrid spatiotemporal models, enabling simultaneous analysis of spatial and temporal dependencies. These advancements have been accompanied by the introduction of unique design elements tailored to address specific challenges in wildfire risk prediction. For example, dynamic-static feature separation enables models to distinguish between temporally varying inputs, such as meteorological variables, and static attributes, such as topography and land cover, improving prediction efficiency (Eddin et al., 2023; Shadrin et al., 2024; Jiang et al., 2023; Dong et al., 2024). Explicit modeling of temporal and spatial dependencies, often through attention mechanisms and spatiotemporal encoding, allows these models to capture complex interactions across time steps or spatially distant regions, thereby enhancing their ability to predict wildfire propagation over large areas (Ji et al., 2024b). Additionally, graph-based representations of geographical regions, where nodes correspond to areas and edges represent interactions such as wind patterns or vegetation continuity, provide a new framework for modeling longrange dependencies and spatial interactions inherent in wildfire dynamics (Jiang et al., 2022; Chen et al., 2022, 2024a). 

## **7. Promising Deep Learning Methods and Data** 

In recent years, the model architectures and the types and quantity of driving features employed in wildfire risk prediction have largely stabilized. From a modeling perspective, given the complex nonlinear and spatiotemporal relationships between various driving factors and wildfire occurrence and spread, a key trend in deep learning-based wildfire prediction is enhancing the capability to model long-range spatiotemporal dependencies. This aims to capture subtle and weak correlations effectively. More specifically, wildfire risk prediction has evolved from purely temporal sequence forecasting to spatiotemporal sequence prediction and spatially enhanced spatiotemporal modeling. These advancements focus on increasing both the temporal and spatial scales of the model, enabling the incorporation of higher-resolution data over longer time sequences while expanding the dataset size. Current research has explored wildfire risk prediction models based on RNNs, CNNs, transformers, and GNNs. 

However, compared to more recent models such as Mamba (Gu and Dao, 2023), these approaches still suffer from inefficiencies or limited capability in modeling large-scale spatiotemporal relationships. Additionally, many of these models rely on multi-branch networks that primarily use imagebased or node-based representations to capture long-range semantic dependencies, without exploring the potential efficiency gains offered by multimodal approaches, such as incorporating textual descriptions. Furthermore, the applicability of crossdisciplinary solutions in addressing the inherent challenges of existing wildfire risk prediction models—such as data dependency, poor interpretability, difficulty in uncertainty quantifica- 

29 

tion, and challenges in handling stochasticity, multi-source heterogeneous data, and complex factor interactions—remains an open question. 

From a data perspective, large-scale wildfire risk prediction studies primarily prioritize data availability, commonality, and ease of processing. This has resulted in an over-reliance on meteorological data from various sources, particularly ground station measurements, ERA-5 reanalysis data, and multiple MODIS-derived products. While MODIS provides high temporal resolution and long-term large-scale observations, its passive optical remote sensing capabilities are inherently limited in penetrating vegetation canopies. Consequently, MODISbased assessments of fuel conditions are often imprecise, and the sensor’s inability to capture data under all-weather, all-day conditions significantly constrains the applicability of wildfire risk prediction models trained on such data. A key question that remains is whether alternative data sources can improve the accuracy of wildfire risk prediction, particularly given the fundamental reality that data acquisition capabilities in Earth sciences far exceed current data processing capacities (Karniadakis et al., 2021). 

In response to these challenges, this section systematically reviews recent advancements in deep learning methods—particularly those employing multimodal approaches—for segmentation, classification, and prediction tasks. Additionally, it provides a brief overview of the Mamba model, a parameter-efficient deep learning framework, to facilitate the development of computationally efficient wildfire risk prediction models in future research. Given the similarities between meteorological forecasting and wildfire risk prediction—both of which involve multiple driving factors, nonlinear coupling, and dynamic spatiotemporal modeling—this section also summarizes recent developments in meteorological forecasting models. The goal is to explore whether cross-disciplinary methodologies can enhance deep learning-based wildfire risk prediction by introducing physical constraints, improving uncertainty quantification, and incorporating lightweight model designs to enhance reliability and accuracy. Furthermore, this section discusses underutilized remote sensing data types in wildfire risk prediction, particularly microwave and LiDAR data, which offer penetrative capabilities, as well as high-spatial-resolution nighttime light data, which can enable dynamic nighttime wildfire monitoring. These discussions aim to provide a broader data reference for future wildfire risk research. 

## _7.1. Promising Deep Learning Models_ 

## _7.1.1. Multimodal Models_ 

Multimodal learning is a universal approach to building AI models, enabling the extraction and association of information from various sources, such as different sensors (Baltrušaitis et al., 2018). Unlike unimodal image-based learning, multimodal learning can acquire, interpret, and reason across multiple information sources, resembling human perception (Xu et al., 2023a). A key advantage of multimodal learning over unimodal approaches is its ability to more easily embed domain knowledge or abstract, knowledge-driven perspectives 

(Baltrušaitis et al., 2018). Currently, multimodal learning has been extensively studied in image segmentation and classification (Roy et al., 2023; Yao et al., 2023; Nasir et al., 2023; Chng et al., 2024; Wang and Ke, 2024; Xu et al., 2023b), data fusion (Khan et al., 2023; Kalamkar et al., 2023), generation, and visual-language pretraining models (Liu et al., 2023; Li et al., 2023a; Oquab et al., 2024). Given that this research focuses on exploring the potential applications of segmentation and classification methods in wildfire risk prediction, we will delve into Referring Image Segmentation (RIS) in subsequent sections. 

RIS refers to models that understand natural language descriptions and correspond them to specific objects in images at the pixel level, outputting an object mask (Wu et al., 2024). RIS requires processing both text and visual modalities, with the latter typically being high-dimensional and exhibiting strong spatial characteristics encapsulating attributes such as color, texture, shape, and size. In contrast, natural language is generally low-dimensional and continuous, abstractly describing these visual features (Ji et al., 2024a). The key challenge of RIS lies in designing appropriate multimodal fusion methods to establish a relationship between language and visual modalities, thereby bridging the modality gap between the two (Chng et al., 2024). Generally, fusion methods can be categorized into early fusion and late fusion, commonly known as decoder-fusion and encoder-fusion, respectively (Wu et al., 2024). 

Decoder fusion extracts visual and language features separately using different encoders, such as CNNs for visual data and LSTMs for language data, and designs specific fusion modules to combine these features at the decoder stage. For example, Jain and Gandhi (2022) utilized CNNs to extract multi-stage image features and LSTMs for text feature extraction, integrating these features through a hierarchical crossmodal aggregation module. In another approach, Wang et al. (2022b) designed a knowledge transfer method to adapt imagelevel knowledge from Contrastive Language-Image Pretraining (CLIP) into RIS for pixel-level segmentation tasks, implementing a Neck module to fuse outputs from both the text and image encoders. Similarly, Yan et al. (2023) introduced a Fusion Neck module to combine image and text encoding information, alongside a multi-query generator module to aid segmentation. 

Encoder fusion, in contrast, integrates multimodal features at the encoder stage using auxiliary losses or alignment modules (Chng et al., 2024). This method is considered more effective (Feng et al., 2021; Yang et al., 2022b) and has gained traction in recent studies (Wu et al., 2024). For example, Xu et al. (2023b) introduced a Bridger module, based on self-attention and cross-attention mechanisms, to facilitate cross-modal information exchange between each level of the text encoder and image encoder. Furthermore, the study designed a task decoder with hierarchical and global alignment to further fuse multimodal information and generate the mask prediction. Similarly, Yuan et al. (2024) employed BERT (Devlin et al., 2019) for text feature extraction and Swin Transformer (Liu et al., 2021b) for image feature extraction, combining them with a self-attention-based language-guided cross-scale enhancer and a pixel-word attention module for feature fusion. Moreover, Shah et al. (2024) incorporated a Gaussian Enhancement Mod- 

30 

ule between textual and visual encoders to extract both local and global visual-language relationships, enhancing overall representation. In a similar vein, Chng et al. (2024) designed a Cross-modal Alignment Module between multiple layers of text and image encoders, addressing the granularity mismatch between the two modalities through bidirectional interactions. Additionally, they introduced a mask encoder branch and a Transformer-based masked token decoder to predict the mask. 

In summary, multimodal tasks offer greater flexibility and intuitive interaction by incorporating natural language to guide the model, compared to unimodal tasks. Multimodal information provides additional contextual data that unimodal models often lack, allowing the language encoder to construct a relation graph for numerical geospatial relations (Yuan et al., 2024). Therefore, multimodal models, especially RIS, hold significant potential in wildfire risk prediction by capturing subtle spatiotemporal semantic dependencies that are difficult to model using existing methods. 

## _7.1.2. E_ ffi _cient Deep Learning Models_ 

The aforementioned deep learning-based methods for spatial, temporal, and spatiotemporal modeling face challenges in capturing long-term and spatial dependencies. As a result, when these methods are applied to wildfire risk prediction on a regional scale, they often neglect the influence of climate factors outside the study area. Furthermore, global-scale wildfire risk prediction is limited by computational capacity, resulting in relatively low spatial resolution in the predictions. Additionally, whether modeling wildfire risk on a regional or global scale, the time series of driving factors considered is often short (a few days) or constructed using monthly or yearly averages for longterm sequences. This calls for more efficient models capable of handling longer temporal scales and higher spatial resolution. 

One potential solution is Mamba: linear time sequence modeling with selective state spaces (Gu and Dao, 2023), a parameter-efficient model designed to handle long sequence modeling (Xu et al., 2024) such as videos or remote sensing imagery over long temporal scales. Mamba’s proposal is primarily aimed at addressing the computational complexity found in prevalent transformer-based networks. Specifically, the selfattention mechanism in transformers involves a computational complexity of _O_ ( _n_<sup>2</sup> ), where _n_ represents the sequence length. Mamba reduces this complexity from _O_ ( _n_<sup>2</sup> ) to _O_ ( _n_ ). Compared to the Transformer network, which uses the self-attention mechanism, the RNN—a previously dominant approach to sequence modeling—suffers from short memory when handling long sequences. Moreover, while RNNs are efficient in the inference stage, they are less efficient during the training phase. Mamba is built on top of the State Space Model (SSM), which, similar to RNNs, is used for sequence modeling. The state-space model can be represented as: 



<!-- Start of picture text -->
State Equation: xt = Axt −1 +  But  +  wt (18)<br><!-- End of picture text -->



<!-- Start of picture text -->
Observation Equation: yt =  Cxt  +  Dut  +  vt (19)<br><!-- End of picture text -->

Where _xt_ is the state vector at time _t_ , _ut_ is the control/input vector, _yt_ is the observation/output vector, _A_ is the state transition 

matrix, _B_ is the input matrix, _C_ is the observation matrix, _D_ is the direct transmission matrix (optional, sometimes set to 0), and _wt_ and _vt_ are process and observation noise, respectively, often assumed to be Gaussian noise and were often removed from most SSM equations. 

By revising the vanilla State Space Model (SSM), as shown in Eq. 18 and 19, the Structured State Space Model for Sequences (S4) was proposed by Gu et al. (2021). Specifically, since the data used in language and image processing are discrete, the SSM needed to be adapted into a discretized version. The zero-order hold technique was applied to discretize the SSM. Furthermore, the SSM equations were reformulated into a combination of recurrent and convolutional structures. This allows the S4 models to be trained in a CNN manner while being tested in a RNN manner, thus improving efficiency in both the training and inference stages. 

To address the short memory issue typically found in RNNs, S4 employs the HiPPO matrix to replace matrix _A_ in Eq. 18. This modification enables the model to store long sequence information in a compact and sparse matrix format. However, one limitation of the S4 models is that the matrices _A_ , _B_ , and _C_ are not data-dependent, which restricts their adaptability — this property is known as Linear Time Invariance (LTI). 

To enhance flexibility, a gate-like operation was introduced to matrix _A_ , allowing it to become data-dependent in a parameter-efficient manner. Similarly, matrices _B_ , _C_ , and the time step were adapted to be data-dependent using linear projection functions. Since all parameters are now data-dependent or dynamic, Gu and Dao (2023) proposed a parallel scan algorithm to efficiently operate the model on GPUs, enabling SSM models to scale for parallel computation. 

While Mamba demonstrated effectiveness, especially with longer sequence lengths, it still did not fully capitalize on the power of GPUs. To address this, Gu and Dao (2023) introduced Mamba2, which applies a state-space duality approach. This new model leverages GPU capabilities more effectively, further improving the computational efficiency while maintaining high performance in long sequence modeling. 

## _7.1.3. Numerical Weather Prediction Models_ 

Wildfire risk prediction is a complex forecasting system that necessitates the consideration of multiple interacting driving factors. Similarly, numerical weather prediction (NWP) is a highly nonlinear, multiscale system requiring the integration of diverse influencing variables. Early NWP models, such as the Integrated Forecast System (IFS) developed by the European Centre for Medium-Range Weather Forecasts (ECMWF) and the Weather Research and Forecasting (WRF) model from the National Center for Atmospheric Research (NCAR), were primarily based on physical equations supplemented by empirical parameterization schemes. These models exhibit strong capabilities in handling cross-scale atmospheric dynamics, including global circulation and local weather interactions, multiscale numerical simulations (ranging from hourly nowcasting to seasonal forecasting), stochastic process modeling, and multiphysical coupling analyses (e.g., the interactions between temperature, humidity, and wind fields). 

31 

With the recent breakthroughs in deep learning, the meteorological forecasting community has increasingly explored data-driven approaches to reduce computational complexity, enhance efficiency, and improve predictive accuracy by continuously integrating newly available data (Sønderby et al., 2020; Lam et al., 2023; Kurth et al., 2023; Waqas et al., 2024). Notably, as in other Earth science applications, deep learning circumvents the need to solve partial differential equations (PDEs) or radiative transfer equations by directly learning statistical relationships from historical weather data. This enables predictions to be generated in a single forward pass, significantly reducing computational demands (Lam et al., 2023). Furthermore, the parallel processing capabilities of GPUs allow for substantial acceleration in model inference (Sønderby et al., 2020). Another notable trend in meteorological forecasting is the emergence of hybrid modeling paradigms that integrate physical mechanisms with data-driven intelligence. By replacing traditional parameterization schemes (e.g., subgridscale turbulence closure, cloud microphysics, and computationally intensive radiative transfer modules) with neural networks, these hybrid models achieve substantial improvements in computational efficiency and predictive performance while preserving physical constraints. 

Intuitively, both meteorological forecasting and wildfire risk prediction share fundamental similarities as complex systems driven by multiple interacting factors. Consequently, insights from physical and deep learning-based meteorological models could provide valuable guidance for developing physicsinformed, data-driven wildfire risk prediction models. This is particularly relevant since existing studies integrating physicsbased constraints with data-driven methodologies in wildfire risk prediction remain limited. Therefore, this section reviews the latest advancements in NWP modeling and their potential implications for wildfire risk prediction. Specifically, it highlights key developments in autoregressive modeling, lightweight architectures, uncertainty quantification, and hybrid models that integrate physics-based constraints with datadriven approaches. 

_Autoregressive Modeling in Meteorological Forecasting._ Atmospheric evolution is inherently dynamic and time-dependent, making meteorological forecasting a temporal sequence prediction task reliant on past weather conditions to estimate future states. Due to the chaotic nature of atmospheric motion, endto-end forecasting models tend to exhibit error accumulation over time. To mitigate this issue, autoregressive (AR) strategies are commonly employed, wherein forecasts are iteratively propagated to predict future states. For instance, GraphCast generates global weather predictions at 6-hour intervals for up to 10 days (Lam et al., 2023). Similarly, the diffusion modelbased GenCast adopts an iterative denoising approach to forecast weather conditions 15 days in advance, using a 12-hour prediction interval. To alleviate error accumulation inherent in autoregressive methods, Pangu-Weather introduces a Hierarchical Temporal Aggregation strategy, training four sub-models to predict weather at varying time scales (1, 3, 6, and 12 hours) rather than employing a fixed prediction step, thereby reducing 

accumulated forecasting errors (Bi et al., 2023). 

_Lightweight Model Designs in Meteorological Forecasting._ Similar to wildfire risk prediction, meteorological forecasting requires extensive input variables to predict large-scale future states, leading to substantial computational costs. Traditional uncertainty quantification in NWP relies on ensemble forecasting, which involves generating multiple weather trajectories under different initial conditions—an approach that significantly increases computational demands. Consequently, various lightweight model designs have been proposed, including specialized Transformer architectures, graph neural networks, and Fourier neural operators. 

For instance, MetNet first applies CNNs and pooling layers to downscale past 90-minute meteorological radar (MRMS) and satellite (GOES-16) data, reducing computational complexity. Subsequently, ConvLSTM processes temporal sequences, while an axial self-attention module captures large-scale spatial dependencies while mitigating the quadratic computational burden of traditional Transformer architectures. Notably, this model is primarily applicable to short-range precipitation forecasting, limiting its broader utility. To address this, MetNet-2 introduces a Context Aggregation Module and Lead Time Conditioning, expanding its spatial coverage from 1024 × 1024 km over an 8-hour forecast period to 2048 × 2048 km over 12 hours (Espeholt et al., 2022). Despite these improvements, MetNet-2 remains constrained to short-term, localized forecasts. 

To enable global medium-range forecasting of multiple meteorological variables and extreme weather events, GraphCast leverages a graph-based approach (Lam et al., 2023). With 36.7 million parameters, GraphCast produces 10-day global forecasts within one minute using a single Google Cloud TPU V4. Algorithmically, GraphCast follows a classic encoderprocessor-decoder architecture: the encoder maps past 6-hour reanalysis or forecast data onto a multi-scale graph structure (where each node represents spatially distinct scales), the processor employs a 16-layer GNN to model both local and longrange dependencies, and the decoder transforms graph features back to geospatial grids for final weather predictions. While GraphCast outperforms ECMWF’s HRES NWP model on 90.3% of 1,380 evaluation targets, it remains computationally expensive. 

To further enhance efficiency, FourCastNet incorporates Adaptive Fourier Neural Operators (AFNO) for global 7-day weather forecasting and extreme event simulation (Kurth et al., 2023). Similar to Transformers, AFNO initially partitions input data into patches and assigns positional encodings to preserve spatial information. To mitigate the quadratic complexity of standard Transformers, AFNO employs 2D fast Fourier transforms to transition patches into the frequency domain, where global spatial dependencies are modeled, followed by fully connected layers to facilitate cross-channel interactions. Additionally, AFNO introduces Spectral Mixing MLP and an adaptive gating mechanism to dynamically adjust frequency components and optimize feature mixing. 

32 

_Uncertainty Quantification in Meteorological Forecasting._ Given uncertainties in observations, model formulations, and the chaotic nature of weather systems, uncertainty quantification (UQ) is fundamental to meteorological forecasting, particularly for probabilistic predictions. UQ provides reliable confidence estimates and enhances early warnings for extreme weather events (Waqas et al., 2024). Traditional NWP models frequently employ stochastic differential equations (SDEs) to model random processes such as precipitation probabilities and temperature fluctuations. A similar approach can be adapted for wildfire risk modeling by formulating ignition probability as a stochastic process: 



<!-- Start of picture text -->
dP ignition( x ,  t ) = µ( x ,  t ) dt  + σ( x ,  t ) dWt  + λ( x ,  t ) dNt (20)<br><!-- End of picture text -->

where _P_ ignition( _x_ , _t_ ) represents the wildfire ignition probability at location _x_ and time _t_ . The deterministic term µ( _x_ , _t_ ) _dt_ accounts for predictable factors such as fuel conditions, wind speed, temperature, and humidity, while the stochastic fluctuation term σ( _x_ , _t_ ) _dWt_ incorporates random disturbances modeled as Wiener processes (standard Brownian motion). Additionally, the jump process term λ( _x_ , _t_ ) _dNt_ captures discrete, abrupt events such as lightning strikes or explosions, represented as a Poisson process. 

Beyond stochastic differential equations, several other methods are widely used for uncertainty quantification in meteorological forecasting. Ensemble prediction, a common approach in both deep learning-based and traditional NWP models, generates multiple weather trajectories using perturbed initial conditions (PICs). The spread among these trajectories, along with confidence intervals and probability density estimations, provides a measure of uncertainty. Ensemble forecasting only accounts for variations in initial conditions and does not capture uncertainties in the underlying dynamical system. 

To address this limitation, GenCast employs generative AI (diffusion models) for probabilistic weather prediction. Its core idea is to generate multiple plausible weather trajectories via noise injection and refine them progressively using a 3D Graph Transformer denoising network. This approach not only eliminates the high computational cost of multiple inference runs in ensemble forecasting but also simultaneously captures uncertainties in both initial conditions and weather dynamics. Additionally, the 3D Graph Transformer employs sparse computations, mitigating the substantial computational burden associated with grid-based data processing in conventional Transformers. Through different denoising stages, GenCast directly produces probabilistic weather distributions along with uncertainty assessments. 

Furthermore, Waqas et al. (2024) highlighted several other techniques for uncertainty quantification in meteorological forecasting, including Bayesian neural networks, Gaussian processes, Monte Carlo methods, and probabilistic loss functions such as negative log-likelihood. They also recommended statistical post-processing methods, such as Quantile Regression Forests (QRF) and variational Bayesian techniques, to reduce systematic biases. Moreover, Generative Adversarial Networks 

(GANs) have been proposed to learn error distributions, thereby improving confidence interval estimations in weather prediction models. 

_Hybrid Physics-Guided and Data-Driven Models._ Despite significant advancements in modeling multiphysical and multiscale atmospheric systems using PDEs and Navier-Stokes equations, the computational cost remains prohibitively high. For example, traditional medium-range (7–10 days) weather forecasting using conventional NWP models requires hours of computation on supercomputers (Bi et al., 2023; Price et al., 2025). In contrast, deep learning-based approaches can achieve comparable accuracy within seconds (Bi et al., 2023; Lam et al., 2023). Data-driven methods are particularly advantageous in addressing the challenge of abundant observational data yet limited processing capabilities in Earth science. However, purely data-driven models often suffer from poor generalization due to limited modeling capacity or observational biases, leading to reduced interpretability and potential inconsistencies with physical laws (Karniadakis et al., 2021; Shi et al., 2025). 

To address these challenges, hybrid models integrating physics-based constraints with data-driven learning have been proposed. These models leverage prior knowledge from physics and mathematics to ensure physically consistent predictions, enhance interpretability, improve robustness, and potentially reduce data dependency. Generally, three types of inductive biases can be introduced into data-driven models: observational bias, inductive bias, and learning bias. These biases incorporate physical principles either implicitly or explicitly through observational data, architectural design, or loss function constraints (Karniadakis et al., 2021). 

A common approach to incorporating physics-based constraints is the use of ERA-5 reanalysis data as input for deep learning-based forecasting models, representing an example of observational bias. Since observational data inherently encapsulate physical laws, training deep learning models on these datasets enables the learning of physically constrained functions or operators. In addition to ERA-5 data, the AI Forecasting System (AIFS) also utilizes ECMWF 4D-Var data for high-quality initialization states (Lang et al., 2024). Compared to random initialization, this approach integrates multitemporal observations with numerical model simulations. It reduces inconsistencies and minimizes errors introduced by single-source observations, thereby ensuring that the initial state of the weather model closely represents real-world atmospheric conditions. 

Beyond these specific examples, data assimilation techniques can also be considered as a form of observational or learning bias. Data assimilation algorithms refine state variable estimates by integrating prior model simulations with observational data (Cheng et al., 2022). Traditional NWP models frequently employ multi-source heterogeneous datasets, combining surface station data, radiosonde measurements, short-term NWP outputs, and satellite observations. However, these datasets are often sparse, incomplete, and contain noise. Directly using such observations without refinement can introduce errors. Data assimilation techniques enable the integration of these heteroge- 

33 

neous datasets with numerical models by performing spatial and temporal interpolation, optimizing initial conditions, and reducing forecast uncertainty, thereby improving prediction accuracy. Common data assimilation methods in meteorology include Kalman filtering, 4D-Var, and particle filtering, which facilitate the fusion of observational data with model predictions (Rabier, 2005). Similarly, data assimilation techniques can be applied in wildfire risk prediction to supplement or correct missing data. 

Notably, data assimilation is not a one-time operation but a continuous process. By periodically assimilating new observations, models can iteratively refine their state estimates at each time step, thereby mitigating the accumulation of initial errors and maintaining accuracy in dynamic environments (Cheng et al., 2022). In this context, data assimilation can be interpreted as a form of learning bias. Wildfire prediction models could adopt a similar approach by integrating heterogeneous data sources such as satellite fire detections (e.g., MODIS/VIIRS thermal anomalies), UAV monitoring, groundbased sensors, and social media reports to dynamically update wildfire conditions. For instance, SAR radar data could be used to estimate fuel moisture, while UAV-based infrared imaging could assess fuel distribution, enabling high-frequency updates of fuel conditions and improving short-term prediction accuracy. In wildfire prediction tasks, Cheng et al. (2022) demonstrated that data assimilation significantly reduced systematic biases in background forecasts and improved long-term reliability by incorporating real-time observations. Their experimental results indicated that data assimilation reduced the relative rootmean-square error (R-RMSE) by approximately 50%, leading to substantial improvements in long-term prediction accuracy. 

A notable example of inductive bias in deep learningbased meteorological forecasting is the NeuralGCM model, which employs differentiable physics solvers to resolve largescale fluid dynamics and thermodynamic processes in the atmosphere, including gravitational forces and Coriolis effects (Kochkov et al., 2024). Additionally, NeuralGCM is designed with neural network modules dedicated to single-column physical processes such as cloud formation, radiative transfer, and precipitation, while maintaining a clear separation between horizontal dynamics and local physical processes. This architectural design ensures that the neural network focuses on smallscale physical interactions, while large-scale atmospheric dynamics remain strictly governed by physical equations, preventing inconsistencies commonly observed in purely data-driven models. 

In future wildfire risk prediction models, additional forms of inductive and learning biases could be explored. For example, constraints on fire spread speed based on wind velocity, temperature, humidity, and fuel load could be imposed to prevent physically unrealistic fire propagation rates. Alternatively, classical fire behavior models, such as the Rothermel model (fireline intensity equation) or PDE-based fire propagation models (e.g., level-set methods), could be incorporated as regularization terms to ensure that neural network outputs comply with energy release rates and fire spread direction constraints. Another approach involves leveraging physics-informed neural 

networks to directly solve fire propagation equations, such as using combustion rate equations as learning constraints. Additionally, techniques from large-eddy simulation (LES) in meteorological modeling could be adapted to develop hybrid models for wildfire turbulence diffusion, potentially integrating deep reinforcement learning to optimize turbulence parameterization. 

## _7.2. Promising Multi-source Remote Sensing Data_ 

From a data perspective, the majority of wildfire risk prediction studies predominantly rely on satellite-based multispectral data, particularly various MODIS-derived products, to obtain real-time or near-real-time information on fuel conditions, wildfire status, and human activities. The primary advantage of multispectral data lies in its ability to provide long-term observational data across extensive spatial scales. However, these products are inherently limited by their spatial and temporal resolution, as well as their inability to penetrate through vegetation canopies, clouds, fog, and smoke. Consequently, they struggle to deliver precise fuel condition assessments and wildfire state parameters crucial for risk prediction, creating significant obstacles particularly for short time-scale forecasting tasks such as next-day wildfire risk prediction. To overcome these limitations, integrating ground-based or unmanned aerial vehicle (UAV) platforms with satellite data, or fusing multispectral data with UAV, satellite and airborne LiDAR, microwave, and nighttime light data, can substantially enhance prediction accuracy. These multi-source data fusion approaches enable more comprehensive characterization of wildfire environments by combining complementary information across various sensing modalities and spatial-temporal resolutions. 

Several review studies have already examined UAV-based wildfire management (Yuan et al., 2015; Bouguettaya et al., 2022; Moumgiakmas et al., 2021; Boroujeni et al., 2024). Notably, these surveys indicate that UAV-related wildfire research has predominantly focused on detection rather than risk prediction (Boroujeni et al., 2024). The potential of UAV-based wildfire risk prediction lies in its capacity to utilize various onboard sensors, including high-resolution multispectral cameras, LiDAR, radar, and acoustic and meteorological sensors, to provide highly accurate fuel condition assessments and environmental monitoring (Boroujeni et al., 2024; Lelis et al., 2024). While UAV-based data offer advantages in terms of resolution and precision, from a methodological perspective, wildfire risk prediction algorithms utilizing UAV data do not fundamentally differ from those relying on spaceborne multispectral and geospatial datasets. 

Beyond UAV data, microwave, spaceborne LiDAR, and nighttime light data play crucial roles in wildfire risk assessment by offering more accurate fuel condition evaluations and records of wildfire occurrences. Each of these data sources provides unique insights: microwave data (e.g., SAR) can penetrate clouds and smoke, enabling the assessment of wildfire, fuel moisture, and soil moisture dynamics; LiDAR data offer detailed three-dimensional structural information of fuel, facilitating accurate estimations of fuel load, continuity, and classification; nighttime light data are sensitive to thermal anoma- 

34 

lies and human activities, making them valuable for identifying potential wildfire ignition sources and estimating carbon emissions. Despite their immense potential in wildfire risk assessment models, studies leveraging these data sources remain relatively scarce, warranting further exploration in future research. 

## _7.2.1. Microwave Data_ 

SAR satellites offer a significant advantage over optical sensors in wildfire risk assessment due to their ability to penetrate clouds and smoke, which often hinder optical observations. Moreover, SAR data provide valuable information on surface roughness and dielectric properties, which vary significantly with changes in fuel characteristics and soil moisture (Meyer, 2019). In wildfire and vegetation-related studies, the C-band (3.75–7.5 cm) and L-band (15–30 cm) SAR are the most commonly used. The C-band exhibits limited penetration capability, making it more sensitive to the upper canopy layer and finer vegetation structures such as small branches or leaves. In contrast, the L-band can penetrate sparse to moderately dense vegetation canopies, allowing for the analysis of structural attributes such as trunk biomass and larger branches. Furthermore, L-band SAR has been shown to be more sensitive to changes in biomass, sub-canopy vegetation, and soil conditions, particularly in high-biomass environments (Coops, 2002; Millard et al., 2018; Coops et al., 2021). 

Apart from SAR, passive microwave remote sensing also provides large-scale soil and vegetation moisture estimates, which are critical factors in wildfire ignition and spread modeling. Notably, passive microwave products are relatively scarce, and in wildfire risk prediction, soil moisture and drought indices derived from meteorological data are more commonly used as proxies. 

Currently, microwave data are primarily employed in wildfire monitoring, burning map generation, and severity assessment, rather than as direct input for wildfire risk prediction models. For instance, Addison and Oommen (2018) utilized L- band ALOS PALSAR data to assess wildfire burn severity in the western United States, leveraging SAR’s sensitivity to surface roughness. Their results demonstrated that SAR-based assessments outperformed optical indices such as the differenced normalized burn ratio (dNBR). Similarly, Tariq et al. (2021) leveraged SAR’s penetration capability and sensitivity to vegetation structural changes by employing Sentinel-1 C-band SAR data to evaluate post-prescribed burning surface fuel and understory vegetation changes in Croajingolong National Park, southeastern Australia. Furthermore, Hu et al. (2023b) explored the application of GANs to translate SAR images into optical representations and generate corresponding burn severity indices. In another study, Horton et al. (2024) developed a wildfire monitoring algorithm based on SAR-derived vegetation index variations, identifying wildfire occurrence through changes in vegetation structure. 

Regarding real-time wildfire spread monitoring, Zhang et al. (2021b) integrated Sentinel-1 SAR and Sentinel-2 multispectral data to develop an approach for near-real-time wildfire propagation tracking. Similarly, Rashkovetsky et al. (2021) compared the wildfire detection capabilities of Sentinel-1 C-band 

SAR, Sentinel-2 multispectral data, Sentinel-3 sea surface temperature data, and MODIS products. Their findings indicated that SAR data significantly enhanced wildfire detection accuracy under cloudy conditions. 

In addition to wildfire detection and severity mapping, a limited number of studies have investigated the potential of SAR’s penetration capability and all-weather data acquisition for wildfire risk prediction. For example, Nur et al. (2022) utilized Sentinel-1 SAR data to generate damage proxy maps, which were subsequently used as target labels for wildfire risk prediction models. Notably, this study primarily focused on SAR-based wildfire burning map generation rather than direct risk assessment. In contrast, Pelletier et al. (2023) employed Sentinel-1 C-band SAR backscatter data as input features for wildfire risk prediction in Canadian treed peatlands. Their findings demonstrated that incorporating SAR data into a Sentinel2 multispectral model improved the prediction of peatland fire probability. Importantly, they also observed that in dense vegetation areas, C-band SAR backscatter exhibited only a weak correlation with fire probability, leading them to recommend its application primarily in sparse or open peatlands. Likewise, Fernández-García et al. (2022) incorporated Sentinel-1 SAR data into a wildfire severity prediction model for southern Europe, using pre-fire C-band SAR cross-ratio as a complementary proxy for fuel load and moisture. Although their study found a negative correlation between SAR-derived indicators and fuel conditions, Sentinel-1-based features exhibited lower predictive performance compared to Sentinel-2 multispectral indices. As a result, these SAR-derived features were not included in their optimized model. 

Beyond their direct application in wildfire mapping, monitoring, severity assessment, and risk prediction, both active and passive microwave data have been extensively validated for their effectiveness in vegetation condition assessment, including FMC and fuel load estimation, as discussed in Section 4.1. Since these variables are crucial explanatory factors in wildfire risk assessment models, leveraging microwave data to derive indices related to fuel conditions or improving the accuracy of vegetation assessments presents a promising avenue for enhancing wildfire risk prediction. Notably, research in this area remains relatively underexplored. 

## _7.2.2. LiDAR Data_ 

LiDAR data share similarities with active microwave remote sensing in that both actively emit signals and receive backscattered or reflected signals. This capability allows them to operate in an all-weather, all-day setting while providing penetration through fuel layers to retrieve structural information. Comparisons between optical sensors and SAR sensors in fuel load estimation have highlighted the importance of canopy structural information for accurate fuel load retrieval (Aragoneses et al., 2024). Unlike optical or SAR-based fuel load estimation methods, airborne LiDAR provides more detailed threedimensional structural information on fuel distribution (Andersen et al., 2005; Hermosilla et al., 2014). Consequently, airborne and spaceborne LiDAR sensors offer the potential to enhance wildfire risk prediction models, assess wildfire damage 

35 

levels, and evaluate the effectiveness of fuel management strategies by directly and accurately estimating fuel load and fuel continuity at various scales (Hillman et al., 2021). 

For example, Skowronski et al. (2011) utilized LiDAR systems to estimate canopy fuel load in pine-dominated forests in New Jersey, USA, predicting canopy bulk density and canopy fuel weight. Similarly, Chen et al. (2017) combined LiDAR data with historical wildfire occurrences, canopy density, elevation, and fuel type to estimate ground fuel load in the jarrah forests of Western Australia. Bright et al. (2017) compared the effectiveness of airborne LiDAR and Landsat time-series data for estimating canopy and surface fuel load in Grand County, Colorado. Their findings indicated that Landsat-based improvements in fuel load estimation were relatively limited. Expanding upon this, Labenski et al. (2023) integrated Sentinel-2 multispectral data with airborne LiDAR-derived forest structure and composition information from two forest regions in southwestern Germany, employing a random forest model to predict and map surface fuel distribution. Moreover, D’Este et al. (2021) incorporated Sentinel-1 SAR data alongside Sentinel-2 multispectral and airborne LiDAR data to estimate dead fine fuel load in southeastern Italy. Their study revealed that, compared to NDVI and C-band SAR data, LiDAR-derived variables exhibited superior performance in dead fine fuel load estimation. Additionally, their findings supported prior observations that woody components contribute more significantly to fuel load, consistent with Li et al. (2020). Furthermore, Comesaña-Cebral et al. (2024) explored the integration of multispectral point cloud data with deep learning models to refine the Prometheus fuel model, aiming to establish a more comprehensive fuel classification standard that better reflects variations in wildfire behavior, thereby enhancing fuel management practices. 

NASA’s recently developed Global Ecosystem Dynamics Investigation (GEDI) full-waveform LiDAR sensor has already demonstrated broad applicability in large-scale aboveground biomass estimation and canopy structure analysis (Myroniuk et al., 2023; Liang et al., 2023; Aragoneses et al., 2024; GuerraHernández et al., 2024). This advancement holds promise for improving wildfire simulation, assessing wildfire-induced vegetation damage, and understanding burn severity. However, relatively few studies have directly employed GEDI LiDAR data for fuel load estimation. One such study by Leite et al. (2022) utilized UAV simulations and on-orbit GEDI data to assess stratified fuel load across three ecosystem layers—grassland, savanna, and forest—in the Brazilian tropical savanna. Their findings suggested that GEDI’s performance in estimating ground and low-lying vegetation fuel load was suboptimal and significantly affected by terrain conditions. 

Beyond fuel parameter retrieval, a limited number of studies have explored the application of LiDAR-derived information in downstream tasks such as wildfire spread modeling and hazard assessment. For instance, Botequim et al. (2019) integrated crown fuel characteristics derived from low-density airborne small-footprint full-waveform LiDAR with stand structural indices to construct spatial wildfire simulations, demonstrating that LiDAR data significantly improved estimates of key forest 

structural characteristics, including canopy height, tree density, and fuel load. In a laboratory-scale study, Marcozzi et al. (2023) employed terrestrial laser scanning point cloud data to characterize three-dimensional fuel structures and evaluate the relationship between fire behavior simulations and LiDAR-derived fuel data resolution. Meanwhile, Hoe et al. (2018) investigated wildfire severity in the Klamath Mountains ecoregion of southwestern Oregon by combining pre- and post-fire multitemporal LiDAR data with Landsat-derived relative differenced normalized burn ratio (RdNBR). Their results indicated that incorporating LiDAR data significantly improved the accuracy of basal area mortality estimation. Additionally, ground-based LiDAR, due to its high vertical resolution, can precisely capture the spatial distribution of wildfire smoke plumes. By analyzing reflectance intensity and pulse time delays, it is possible to infer aerosol particle size, concentration, and optical properties, offering valuable insights into wildfire smoke dispersion and pollutant transport pathways (Ye et al., 2022; Deng et al., 2022; Huang et al., 2024). 

Despite these advantages, LiDAR-based research in wildfire applications has primarily focused on improving the accuracy of fuel structure retrieval rather than directly integrating these results into wildfire risk prediction models. Several factors may contribute to this gap. First, compared to conventional 2D optical imagery, LiDAR data are inherently more complex and specialized, requiring researchers to possess specific technical expertise and training. Second, the availability of spaceborne LiDAR data is limited, and airborne LiDAR acquisitions are costly, making large-scale, long-term data collection challenging. As a result, the scarcity of LiDAR data has constrained its application in wildfire risk prediction. Future research should aim to incorporate higher-quality fuel structure parameters derived from LiDAR data to enhance prediction accuracy while reducing model uncertainty. 

## _7.2.3. Nighttime Light Data_ 

In addition to microwave and LiDAR data, nighttime light data also hold potential for improving wildfire risk prediction due to their sensitivity to thermal anomalies, human activities, and lightning events. These data can be leveraged for wildfire detection and mapping, as well as for modeling the relationships between human activities, lightning, and wildfire occurrences. Furthermore, nighttime light data can serve as indicators of combustion efficiency, aiding in the estimation of wildfire-induced carbon emissions and aerosol composition, as well as in identifying sources of air pollution (Zhou et al., 2023). 

The most commonly used nighttime remote sensing data sources include the Visible Infrared Imaging Radiometer Suite (VIIRS) onboard S-NPP, NOAA-20, and NOAA-21. VIIRS is a 22-band scanning radiometer covering wavelengths from 412 nm to 12 µ _m_ m and is regarded as the successor to MODIS for Earth science data product generation (Barmpoutis et al., 2020). VIIRS is considered an optimal balance between spatial and temporal resolution (Chuvieco et al., 2020), offering a spatial resolution of 375 m in its five imagery bands (I-bands) and 750 m in its 16 moderate resolution bands (M-bands) and the 

36 

day/night band (DNB). Compared to MODIS, VIIRS provides improvements in nighttime detection capabilities and higher spatial resolution. Specifically, VIIRS features seven shortwave radiation bands (M07–M13 and I4) dedicated to nighttime wildfire detection, addressing MODIS’s limitation of having only a single 3.96 µ _m_ MWIR detection band, which is insufficient for characterizing biomass burning emissions (Polivka et al., 2016; Zhou et al., 2023). Additionally, VIIRS’s enhanced spatial resolution enables better detection of smaller wildfires (Schroeder et al., 2014). 

Extensive research has been conducted on wildfire detection using VIIRS data. Since the initial implementation of VIIRSbased wildfire detection algorithms utilizing I-bands and contextual techniques, significant advancements have been made, yielding high spatial resolution (375 m) and strong consistency with MODIS products (Schroeder et al., 2014). For example, to address limitations in detecting small and low-intensity fires, the Fire Identification, Mapping, and Monitoring Algorithm (FILDA) series introduced advanced methodologies. FILDA1 mitigated the "bundling" effect by incorporating additional spectral bands to enhance fire detection sensitivity (Polivka et al., 2016), while FILDA-2 integrated the DNB and M-bands to improve the detection of low-intensity fires and enhance the retrieval accuracy of fire radiative power (FRP) (Wang et al., 2020; Zhou et al., 2023). These advancements have significantly improved VIIRS-based fire monitoring, providing more reliable tools for wildfire detection and emissions analysis. Additionally, Zhang et al. (2023a) employed VIIRS’s VNP14IMG product to construct training labels for a random forest-based wildfire detection model using Himawari-8 data. Similarly, Yu et al. (2024) utilized VIIRS VNP46A2 data in combination with a random forest model for forest fire detection in southwestern China. Their study demonstrated that VIIRS outperformed MODIS and other products in detecting lowertemperature wildfires, making it a valuable complementary data source for wildfire detection. 

Beyond wildfire detection, nighttime light data can serve as a proxy for human activity, making them suitable as input features in data-driven models for analyzing human-induced wildfire risk. Compared to conventional socioeconomic indicators such as GDP, population distribution, energy consumption, land use, and accessibility, nighttime light data offer advantages including higher spatiotemporal resolution, frequent updates, extensive coverage, and spatial continuity, making them more effective in capturing human activity patterns (Chen et al., 2023; Zhang et al., 2023b). Specifically, Chen and Jin (2022) employed annual composite nighttime light images as indicators of human settlement and electricity infrastructure density. By integrating these data with fuel, topographic, and meteorological variables, they analyzed the influence of anthropogenic and lightning ignition on wildfire probability in California. Similarly, Zhang et al. (2023b) utilized nighttime light data as a proxy for socioeconomic factors, compensating for the limitations of statistical data in capturing the spatiotemporal heterogeneity of human activity. By combining nighttime light data with other drivers, they investigated the relationship between wildfire probability and various influencing factors in 

Anhui Province, China. Their study revealed that socioeconomic variables exhibited the highest correlation with wildfire occurrence, while vegetation, topographic, and meteorological factors played a secondary role. Furthermore, Chen et al. (2023) developed a human activity factor based on nighttime light intensity within forest buffer zones. By integrating this factor with other wildfire drivers, they assessed its contribution to wildfire risk across China. Their analysis demonstrated that nighttime light data had greater importance than topographic, meteorological, and fuel-related factors, and incorporating nighttime light data improved model accuracy by 6%. 

While numerous studies have explored the application of nighttime light data in wildfire detection and risk prediction, their broader potential in wildfire-related research remains underexplored. Beyond directly or indirectly incorporating nighttime light data as a socioeconomic driver in wildfire risk models, a limited number of studies have investigated the use of nighttime light data for wildfire hazard assessment, particularly in terms of wildfire impact on human settlements. For instance, Yue et al. (2023) employed nighttime light indices to represent urban development levels (vulnerability) rather than as a direct socioeconomic driver in a wildfire risk prediction model. This approach enabled them to identify high-risk areas where wildfires posed potential threats to economic assets and human populations in Guilin, China. Notably, overall, research on wildfire hazard prediction based on VIIRS and other nighttime light products remains limited. Future studies could leverage nighttime light data to assess wildfire hazards, particularly in the WUI. Additionally, long-term analysis of population density, WUI expansion, and urban dynamics could provide valuable insights into their relationships with wildfire risk and wildfireinduced damages. 

## **8. Conclusion** 

Wildfire risk prediction has evolved through the integration of diverse data sources and the development of various modeling approaches. However, a comprehensive and systematic review of these data and methodologies remains insufficient, particularly in the domain of deep learning, which has seen rapid advancements and increasing applications in wildfire risk assessment. This paper provides a thorough review of wildfire driving factor datasets, feature collinearity analysis, model interpretability, and deep learning-based wildfire prediction models, with a particular emphasis on the role of remote sensing in wildfire risk assessment. 

The development of wildfire risk prediction models necessitates the integration of multiple input data sources, along with reliable ground truth data for model training and validation. These input data typically include fuel characteristics, meteorological and climatic conditions, topography, hydrology, and socioeconomic factors. Our review indicates that most studies prioritize meteorological and climatic variables, followed by fuel and topographical conditions, while socioeconomic and hydrological factors remain underexplored despite their potential impact. To facilitate deep learning-based wildfire risk as- 

37 

sessment, this study also introduced publicly available wildfire burn prediction datasets, including FireCube, Next Day Wildfire Spread, Wildfire DB, WildfireSpreadTS, CFSDS, and the SeasFire Datacube. Furthermore, to enhance model reliability and interpretability, we discussed feature collinearity assessment techniques such as Variance Inflation Factor (VIF), tolerance, and Pearson correlation coefficients, alongside interpretability methods for deep learning models, including Permutation Feature Importance, Explainable Feature Engineering, and SHapley Additive exPlanations (SHAP). 

In terms of modeling approaches, wildfire risk prediction has historically relied on traditional machine learning methods and wildfire danger rating systems. While these conventional approaches have been extensively reviewed, deep learning-based models, despite their increasing adoption, have lacked a structured and systematic analysis. This paper categorizes deep learning models into three primary types: time-series forecasting, image segmentation and classification, and spatiotemporal prediction. Our review highlights an emerging trend towards the utilization of longer time-series data and the development of higher spatiotemporal resolution models to improve wildfire risk assessments. 

Looking forward, we identify several key directions for future research. First, the integration of novel and underutilized remote sensing data sources, such as microwave, LiDAR, and nighttime light data, holds significant potential for improving the accuracy and robustness of wildfire risk prediction models. Second, multimodal learning approaches, which leverage heterogeneous data types such as geospatial imagery, meteorological records, and textual descriptions, may offer enhanced predictive performance by capturing complex interactions among wildfire-driving factors. Additionally, the development of computationally efficient deep learning architectures, such as Mamba, presents an opportunity to model long-term spatiotemporal dependencies more effectively while reducing computational costs. Lastly, cross-disciplinary approaches, particularly the adaptation of techniques from numerical weather prediction models, may provide insights into uncertainty quantification, physical constraints, and data assimilation strategies that could improve wildfire risk assessment models. By addressing these challenges and opportunities, future research can contribute to more reliable, interpretable, and scalable deep learning models for wildfire risk prediction. 

## **Appendix A. Fuel Conditions Estimation** 

Through the above review, we identify that one of the key limitations in wildfire risk prediction is the inaccurate characterization of fuel conditions. Given data scarcity, most studies rely on readily available multispectral and meteorological data, along with indices derived from these sources, to describe fuel conditions. Therefore, we have examined the latest advancements in fuel condition retrieval, with a particular focus on fuel moisture content and fuel load, aiming to provide support for the development of more accurate wildfire risk prediction models. 

## _Appendix A.1. Fuel Moisture Content_ 

## _Appendix A.1.1. Dead Fuel Moisture Content_ 

DFMC is a crucial input in nearly all wildfire risk assessment models (Matthews, 2013). For example, estimates of DFMC are integral to current operational fire prediction systems, including the FWI and the National Fire Danger Rating System in the United States (Vitolo et al., 2020). Estimating DFMC involves calculating EMC based on factors like temperature, relative humidity, and fuel response time, combined with precipitation data and drying algorithms (Nieto et al., 2010). DFMC estimation methods can generally be divided into four categories: measurements at meteorological stations, field sampling, estimates based on meteorological data, and indirect retrieval using multi-source remote sensing data. 

DFMC can be measured using standard wooden dowels installed 10–12 inches above the ground at meteorological stations (Rakhmatulina et al., 2021). However, the sparse distribution of DFMC measurement stations and the limited accuracy of these measurements make it difficult to achieve large-area coverage, even with interpolation of atmospheric parameters. Field sampling of DFMC, on the other hand, provides highly accurate measurements and serves as a valuable data source for both physical process models and empirical modeling. Despite its accuracy, field measurements require careful consideration of various environmental factors, including terrain, vegetation type, ecosystem structure, climate, and soil characteristics. This complexity makes field sampling time-consuming, costly, and spatially constrained (Duff et al., 2017). 

Given these limitations, many studies have focused on integrating field measurements with meteorological station data, numerical weather prediction models, or meteorological reanalysis data to develop empirical and mechanistic models for estimating FMC (Matthews, 2013). Among these, physical process models primarily rely on energy and water balance equations. The most widely used model for DFMC estimation is the Nelson Dead Fuel Moisture Model, proposed by Nelson Jr (2000), which predicts DFMC by simulating heat conduction and moisture transfer between a wooden cylinder, the surrounding atmosphere, and external conditions. This model requires hourly input data on temperature, humidity, radiation, and precipitation to provide DFMC estimates. Additionally, McNorton and Di Giuseppe (2024) designed a new method for estimating DFMC by grouping fuels and simplifying the Nelson model. Other models used for DFMC estimation include bulk litter layer models, Byram’s diffusion equation-based models, and complete process-based models (Matthews, 2013). 

Empirical methods for estimating DFMC rely on observed relationships between measured DFMC and factors such as air temperature, relative humidity, wind speed, soil moisture content, and vapor pressure deficit. These data-driven methods include statistical techniques (Ferguson et al., 2002; Ray et al., 2010; Cawson et al., 2020; Rakhmatulina et al., 2021), but their primary limitation is that they are entirely data-driven, making it difficult to explain the relationship between driving factors like temperature, heat and water vapor fluxes, radiation, and precipitation, and DFMC. Consequently, some studies have 

38 

started to combine data-driven approaches with physical process models (Fan and He, 2021; Fan et al., 2024). 

Apart from the meteorological data-based FMC estimation methods mentioned above, indices such as the Cellulose Absorption Index (CAI), the Lignocellulose Absorption Index (LCAI), the Normalized Difference Tillage Index (NDTI), the Normalized Difference Vegetation Index (NDVI), and the Shortwave Infrared Normalized Difference Residue Index (SINDRI) have been shown to correlate with DFMC (ZORMPAS et al., 2017; Zacharakis and Tsihrintzis, 2023). This forms the theoretical basis for DFMC estimation using remote sensing. However, research on DFMC estimation using multi-source remote sensing data is still limited (McCandless et al., 2020). 

## _Appendix A.1.2. Live Fuel Moisture Content_ 

In early studies, the LFMC was measured similarly to the DFMC through field sampling and weighing methods, with interpolation or inversion used to estimate the entire study area (Bianchi and Defossé, 2015). While this method is highly accurate locally, it is time-consuming, labor-intensive, and not scalable to landscape, regional, or global levels (Yebra et al., 2013a). As such, many studies favor multi-source geospatial data for large-scale and near real-time LFMC estimation, utilizing the growing capabilities of Earth observation technologies for high-resolution data (Rao et al., 2020a; Capps et al., 2021). These contemporary approaches utilize environmental variables such as precipitation and soil moisture, along with spectral, thermal infrared, and microwave data, often in combination with machine learning algorithms, to enhance prediction accuracy (Bowyer and Danson, 2004; Yebra et al., 2013a). 

First, similar to DFMC, LFMC can be estimated on a large scale in near real-time using meteorological parameters. This is because plant water regulation is influenced by environmental factors such as precipitation, soil moisture, and evapotranspiration (Bowyer and Danson, 2004). For example, the NFDRS used by the US Forest Service calculates LFMC using empirical formulas based on precipitation, temperature, and relative humidity (Bradshaw et al., 1984). Moreover, Castro et al. (2003) modeled the live fine fuel moisture content (LFFMC) of Cistus spp. in the Catalonia region of Spain using factors such as temperature, soil water availability, and atmospheric water content. Similarly, Ruffault et al. (2018) compared six drought indices’ ability to estimate LFMC across six different Mediterranean shrubs in southern France, finding that drought indices were effective only at stand scale, with indices simulating longterm drought dynamics (DC, RWC, and KBDI) providing better LFMC predictions. Viegas et al. (2001) used DC, BUI, and DMC from the FWI to estimate LFFMC in various plant species in central Portugal and Catalonia. Furthermore, Vinodkumar et al. (2021b) successfully predicted LFMC across Australia using the lag relationship between soil moisture changes and vegetation moisture responses combined with regression analysis and physical models. 

Meteorological data can also be combined with other datasets to estimate LFMC. For instance, Miller et al. (2023) proposed a 

method using a multimodal Multi-tempCNN model that incorporates multitemporal meteorological data, MODIS MCD43A4 BRDF-Adjusted Reflectance data, and climate zone, topography, and location information. This method enables large-scale LFMC estimation at medium resolution (500 m) over periods longer than two weeks. Similarly, McNorton and Di Giuseppe (2024) integrated soil moisture data and LAI to estimate LFMC, validating the estimates using MODIS data. In the western United States, Wang and Quan (2023) used meteorological indicators, soil moisture data, and vegetation indices to estimate LFMC, finding that inversion accuracy varied with vegetation cover type. 

The advantage of meteorological parameter-based LFMC estimation methods is the ability to generate near real-time LFMC estimates or predictions using data from weather stations, meteorological satellites, or numerical weather forecasting (Capps et al., 2021). However, LFMC is more challenging to estimate using meteorological parameters compared to DFMC. This is because plants actively regulate their water content through absorption and transpiration, with significant differences in physiological characteristics between plant species and a greater influence from phenological conditions and medium-term meteorological conditions (Pellizzaro et al., 2007; Ruffault et al., 2018; Jolly and Johnson, 2018). 

Therefore, compared to LFMC estimation methods based on meteorological data or drought indices, most studies prefer using multi-source remote sensing data to estimate LFMC (Rao et al., 2020a; Capps et al., 2021; Quan et al., 2021a; RodriguezJimenez et al., 2023). Remote sensing technology, as a lowcost means of large-scale, long-term dynamic Earth observation, also enables near real-time, high-resolution LFMC estimation in highly heterogeneous real-world scenarios (Quan et al., 2021b; Zhu et al., 2021; Verbesselt et al., 2002). Additionally, the exponential growth of Earth observation missions (Ustin and Middleton, 2021) has provided new opportunities for LFMC estimation (Leite et al., 2024). Studies on LFMC estimation using multi-source satellite remote sensing primarily utilize multispectral reflectance data, thermal infrared data, and active and passive microwave data, combined with data-driven empirical or machine learning models, radiative transfer-based physical models, or hybrid models that integrate physical constraints with data-driven approaches (Yebra et al., 2013a; McNorton and Di Giuseppe, 2024). 

The theoretical basis for LFMC inversion methods using multispectral reflectance data lies in the presence of water absorption bands in the near-infrared ( 750-1100 nm) and shortwave infrared ( 1100-2500 nm) spectral regions. Plant stress due to drought leads to changes in chlorophyll concentration and leaf internal structure, allowing the relationship between vegetation spectral reflectance (i.e., spectral characteristics) and LFMC to be established (Knipling, 1970; Kriedemann and Barrs, 1983; Bowyer and Danson, 2004; Yebra et al., 2013a; Sow et al., 2013; Zacharakis and Tsihrintzis, 2023; Leite et al., 2024). Thus, LFMC can be inverted by simulating the relationship between spectral characteristics under different water content levels and observed spectral characteristics (Hao and Qu, 2007; Yebra et al., 2008, 2013a; Marino et al., 2020; Quan 

39 

et al., 2021a). While this physical method is generally more robust, it is also more complex in terms of parameterization (Yebra et al., 2013a). Alternatively, empirical methods based on spectral reflectance or spectral indices, including the NDVI, enhanced vegetation index (EVI), soil-adjusted vegetation index (SAVI), normalized difference infrared index (NDII), water index (WI), normalized difference water index (NDWI), visible atmospheric resistance index (VARI), Leaf Water Content Index (LWCI) (Hunt Jr et al., 1987), Global Vegetation Moisture Index (GVMI), and Shortwave Infrared Water Stress Index (SIWSI) (Fensholt and Sandholt, 2003), are simpler and only require fitting the relationship between in situ LFMC measurements and spectral reflectance characteristics. These methods can perform as well as or better than physical models at local scales and across specific vegetation types (Cunill Camprubi et al., 2022). 

For example, Chuvieco et al. (2002) compared the ability of shortwave infrared bands, NDVI, NDII, LWCI, the wetness and greenness components of the Tasseled Cap transformation, and spectral derivatives to model LFMC in Mediterranean grasslands and shrubs. They found that shortwave infrared bands and indices using these bands performed better due to the high correlation between shortwave infrared and LFMC, attributed to water absorption in leaves. Near-infrared and red bands also showed good correlation with LFMC, particularly for herbaceous plants, where drought stress led to changes in chlorophyll content and structure. The study recommended further use of thermal bands and meteorological data to improve modeling accuracy. Additionally, Myoung et al. (2018) used Pearson correlation analysis to compare the correlations between 16-day NDVI and EVI products (MOD13Q1 and MYD13Q1) and NDWI, NDII, and VIARI calculated from MOD09A1 reflectance data and in situ LFMC measurements from the National Fuel Moisture Database. The study ultimately selected EVI and introduced daily minimum temperature data to establish an empirical model for estimating LFMC in southern California. This choice was because EVI effectively captured changes in chlorophyll concentration related to water content, showing better response than other vegetation indices and shortwave infrared bands under water stress, particularly for Mediterranean vegetation. Introducing temperature data improved the model’s ability to capture excessive water loss during extreme heat, correcting overestimates of minimum LFMC. Similarly, García et al. (2020) found that EVI performed better than other ratio vegetation indices, such as NDII, NDVI, and VARI, for LFMC modeling in Eastern California and Oregon. 

Marino et al. (2020) used NDVI, NDII, GVMI, NDWI, EVI, SAVI, VARI, and _VIgreen_ from MCD43A4 and MOD09GA products, as well as the same indices calculated from Sentinel2 data, to estimate the LFMC of Mediterranean shrubs. The main difference between MOD09GA and MCD43A4 and the MOD13Q1 and MYD13Q1 products used by Myoung et al. (2018) is that the former are daily data, which do not smooth out short-term LFMC changes. This feature is more conducive to capturing abnormal LFMC values under extreme conditions and to estimating LFMC for shrubs and grasslands that are more sensitive to short-term environmental changes. Similar to My- 

oung et al. (2018), Marino et al. (2020) also found that using vegetation indices to estimate LFMC tends to overestimate lower LFMC values. However, Marino et al. (2020) found that VARI had the highest accuracy in LFMC modeling compared to other vegetation indices. Combining VARI with NDVI can further improve the accuracy of the model. This is because VARI and NDVI are based on visible (blue, green, red) and near-infrared reflectance data, which are suitable for measuring changes in greenness and LAI related to leaf drying and can indirectly reflect leaf water content. Similarly, Stow et al. (2006); Peterson et al. (2008); Caccamo et al. (2011) found that VARI performed better than other vegetation indices or reflectance bands in estimating LFMC for shrubs in Southern California, Mediterranean climate regions, and southeastern Australia. Although these studies did not show that any particular vegetation index is the best choice in all scenarios, they emphasized the importance of chlorophyll (or greenness) response to water stress. 

Water availability is a key parameter for plant transpiration. Therefore, changes in LFMC affect not only reflectance spectral bands but also canopy temperature (ST). When plants dry out, transpiration and latent heat transfer decrease, which in turn increases sensible heat (Kozlowski et al., 1990; Yebra et al., 2013a). As a result, introducing thermal infrared bands (250014000 nm) into LFMC estimation can improve model performance under certain conditions. It is worth noting that in most studies, land surface temperature (LST) is used as a proxy for ST. Chuvieco et al. (2004) used NDVI and ST data from the AVHRR sensor to estimate LFMC for grasslands and shrubs in Cabañeros National Park, central Spain, based on a linear regression model. The study found that NDVI and ST were positively and negatively correlated with LFMC, respectively, and that the introduction of ST significantly improved the model’s performance. Cunill Camprubi et al. (2022) combined MODIS spectral bands, vegetation indices, land surface temperature, and day of the year as predictors, using a random forest algorithm to estimate LFMC in the Mediterranean basin wildlands. They found that the combination of LST and day of the year had the highest importance, and that when the temperature exceeded 20°C, LST was negatively correlated with LFMC. However, in LFMC estimation experiments based on MODIS LST products, LST did not show a significant advantage over other factors. For example, Sow et al. (2013) compared the performance of the NDVI-to-LST ratio and GVMI, WI, NDWI, NDII, and MSI in estimating LFMC and equivalent water thickness (EWT) in three study areas in Senegal, finding that the NDVIto-LST ratio had no significant advantage in correlating with LFMC and EWT compared to other vegetation indices. It is worth noting that this study did not compare the performance of using NDVI alone to model LFMC or EWT. (McCandless et al., 2020) used machine learning methods to model LFMC across the continental United States using MODIS reflectance data, meteorological data, and terrain data. The random forest method was used to evaluate the importance of various predictors, finding that the importance of LST was only 6%, lower than the importance of altitude (22%), soil saturation (17%), accumulated evapotranspiration (11%), and slope (7%). More- 

40 

over, some other studies also indicate that canopy temperature is an indicator of plant water stress (Gonzalez-Dugo et al., 2012; Rahimzadeh-Bajgiran et al., 2012; Yebra et al., 2013a). 

Although spectral features can model canopy LFMC, they are more sensitive to dry matter such as canopy structure, resulting in lower robustness (Rao et al., 2020b). Additionally, these spectral features couple dry matter and water content information, so when both change due to water stress, there can be issues with estimating LFMC using vegetation indices and other spectral features (Danson and Bowyer, 2004; Yebra et al., 2013b). Moreover, spectral features are affected by lighting conditions and clouds or rain, making it difficult to provide fulltime or near-real-time large-scale, long-term series LFMC mapping (Rao et al., 2020b). Compared to spectral reflectance, microwave remote sensing is more capable of penetrating clouds and is more sensitive to water content (Rao et al., 2020b). For example, active microwave sensors are sensitive to vegetation structure or dielectric properties (including vegetation moisture) through backscatter signals, and their penetration capability can be used to model soil moisture, thus monitoring vegetation water stress (Dorigo et al., 2017). Passive microwave sensors can also be used to estimate LFMC through soil moisture time lags or vegetation optical depth (VOD) (Lu and Wei, 2021a; Forkel et al., 2023). Commonly used microwave sensors primarily operate in the P-band (≈ 70 cm), L-band (≈ 23 cm), C-band and X-band (≈ 3 cm), and Ku-band (≈ 1.6-2.5 cm). Among them, the backscatter signal of P and L bands is primarily coupled with backscatter from the soil and lower canopy, while the backscatter signal of C, X, and Ku bands mainly comes from the interaction between microwave radiation and the upper canopy. 

Tanase et al. (2015) used vertical-vertical (VV), verticalhorizontal (VH), horizontal-vertical (HV), and horizontalhorizontal (HH) polarization L-band radar backscatter signals to model the relationship between backscatter intensity, polarization decomposition signals, radar vegetation index (RVI) (Kim et al., 2012), and canopy height with LFMC and EWT. Experiments in Australian forests demonstrated that the modeling capability of L-band radar data was superior to spectral reflectance data. The penetration of L-band data enables modeling of the lower canopy and surface fine fuel moisture content. However, when the forest is high and dense, and both lower canopy and soil moisture are low, there will be a large error in estimating LFMC for the lower canopy. Wang et al. (2019) explored the performance of C-band Sentinel-1A (5.4 GHz) VV and VH polarization data in estimating LFMC in Texas forests. The model coupled an empirical bare soil backscatter model with the Water Cloud Model (WCM) (De Roo et al., 2001) to establish an LFMC lookup table, directly estimating LFMC, and compared this LFMC with results obtained from Landsat 8 OLI spectral reflectance data using the empirical partial least squares (PLSR) method and measured LFMC data. The experiment showed that the accuracy of LFMC inversion based on Sentinel-1A data was higher than that based on Landsat 8 OLI data and that it could reproduce the temporal variation trend of LFMC. Lu and Wei (2021b) used multi-source microwave soil moisture products ECV_SM and SMAP L-band Level 4 surface 

and root zone soil moisture data, using a robust linear regression model with a time lag to assess LFMC across the continental United States. The study showed that LFMC was most correlated with soil moisture conditions 60 days before LFMC sampling in most regions. 

Considering the influence of soil moisture content and canopy dry matter on radar backscatter, reflectance, or emission signal intensity, some studies have integrated SAR and multispectral reflectance data, along with vegetation cover, canopy height, and soil moisture data, to estimate LFMC. For instance, Jia et al. (2019) employed soil moisture data obtained from the SMAP L-band radiometer, combined with VARI calculated from MODIS MCD43A4 reflectance data, growing degree days (GDD), and precipitation, to estimate LFMC in Southern California using a regression model. This study found that using cumulative soil moisture data combined with cumulative growing degree days yielded better performance in LFMC estimation compared to using MODIS VARI combined with cumulative growing degree days. The superior performance is attributed to a more accurate representation of the water cycle processes between vegetation and soil. 

Rao et al. (2020b) designed a knowledge-assisted neural network to estimate LFMC in the western United States, utilizing Sentinel-1 VV and VH polarized SAR backscatter data, Landsat-8 red, green, blue, near-infrared (NIR), and shortwave infrared (SWIR) optical reflectance data, along with NDVI, NDWI, and near-infrared spectral indices derived from the reflectance data. To separate the contributions of vegetation and soil moisture to the backscatter signal, the study proposed a knowledge-based method and a data-driven approach. The former method leverages the differential sensitivity of VV and VH polarizations to soil and vegetation moisture, using the difference between VV and VH polarizations to separate the contributions of soil and vegetation to backscatter intensity. The latter approach involves training the deep learning model to learn the separation of vegetation moisture and soil moisture contributions by incorporating soil type as an input. The study also established a ratio of backscatter signals to spectral reflectance, utilizing the high water sensitivity of backscatter signals and the high spectral reflectance of dry matter, alongside the aforementioned vegetation indices to separate the contributions of dry matter and water content to LFMC estimation. 

Similarly, Xie et al. (2022a) employed Sentinel-1 data along with MODIS MCD43A4 nadir BRDF-adjusted reflectance (NBAR) data, original band reflectance data from Landsat-8 OLI (red, green, blue, NIR, and SWIR channels), and vegetation indices such as NDVI, NIRV, and NDWI. The study used canopy height and land cover type as auxiliary data to estimate LFMC in the western United States. These data were interpolated to unify spatial and temporal resolutions before being input into an integrated model, where LFMC was predicted through end-to-end training. 

Furthermore, Forkel et al. (2023) achieved global LFMC estimation by combining Ku-band, X-band, and C-band VOD data derived from passive microwave technology with MODIS LAI, AVHRR vegetation cover data, LULC, and meteorological and topographical data. This study demonstrated that the combina- 

41 

tion of Ku-VOD and LAI as predictors significantly improved LFMC estimation performance. Conversely, Chaparro et al. (2024) conducted LFMC inversion experiments in the western United States, showing that when a model effectively separates vegetation structure and dry matter information, the accuracy of LFMC estimation based on VOD is independent of canopy height, land cover type, and radar backscatter signals. 

While the aforementioned LFMC estimates based on multispectral and microwave remote sensing data have achieved satisfactory accuracy, it is noteworthy that some studies suggest that the inclusion of microwave data does not necessarily enhance LFMC inversion accuracy. For example, Tanase et al. (2022) explored the estimation of LFMC in Mediterranean vegetation using C-band Sentinel-1 and Sentinel-2 multispectral data combined with canopy height, vegetation cover, and topographical data. The study found that incorporating radar data did not improve model performance and thus only recommended its use in areas with significant cloud cover. 

Research has also been conducted on the effectiveness of different data sources for LFMC estimation. For instance, Fan et al. (2018) compared the performance of LFMC estimation in southern France using ECV_SM, root zone soil moisture from ECV_SM, microwave polarization difference index (MPDI) calculated from C, X, Ku, K, and Ka band passive microwave data at 6.9, 10.7, 18.7, 23.8, and 36.5 GHz, VOD derived from AMSR-E C and X band data, and vegetation indices such as NDVI, SAVI, VARI, NDWI, NDII, and GVMI calculated from MODIS data. The MPDI and VOD were averaged over 15 days prior to in-situ measurements. The study found that the optical vegetation indices VARI and SAVI outperformed the microwave-derived indices and other optical indices. Among the microwave indices, X-band VOD showed the highest consistency with in-situ measured LFMC. 

## _Appendix A.2. Fuel Load_ 

The methods for estimating fuel load are similar to those for estimating FMC, including direct sampling and the use of physical models or multispectral and microwave remote sensing data. Direct measurement involves collecting field samples, weighing, drying them, and then estimating biomass in the area, which is considered the most accurate assessment method and can provide a data foundation for physical or empirical model evaluations. First, fuel load estimation methods based on ground-measured data combined with vegetation or forest growth models can predict or estimate fuel load by forecasting future vegetation growth, forest structure, and more. For example, Lee et al. (2022) used a Weibull function and mortality model based on forest inventory data to predict the fuel load of Korean red pine (Pinus densiflora) for the next 20 years in Korea. Meanwhile, Nolan et al. (2022) modeled above-ground biomass in the shrub layer of eucalyptus forests in southeastern Australia using allometric equations, considering it as fuel load. 

While ground sampling offers high accuracy, it is inefficient and costly. In contrast, remote sensing technology provides an efficient and comprehensive method for assessing fuel load. For example, Saatchi et al. (2007) used airborne SAR data and a semi-empirical algorithm to estimate the distribution of 

forest biomass and canopy fuel load in Yellowstone National Park. Additionally, Duff et al. (2012) developed a biophysical model to explore the feasibility of using satellite-based NDVI to estimate forest fuel load in southeastern Australia. Li et al. (2020) estimated changes in live fuel load in shrubs and grasslands in the Owyhee Basin, southern Idaho, using MODIS NPP products combined with the Biome-BGC model, and calculated changes in dead fuel load based on the estimates. The study found that even with the same productivity, the fuel load of shrubs was higher than that of grasslands. 

In addition to fuel load estimation using physical or semiempirical models based on remote sensing data, empirical model-based methods are simpler and more commonly used. For instance, Arellano-Pérez et al. (2018) used the random forest method and Sentinel-2 multispectral and vegetation index data to estimate the canopy fuel load of Pinus radiata and Pinus pinaster stands in northwestern Spain. However, due to the low penetration capability of optical sensors, the accuracy of canopy fuel load estimation in this study was limited. Furthermore, Li et al. (2021b) compared the effectiveness of L-band SAR (ALOS-PALSAR) and Landsat 7 ETM+ in estimating fuel load in coniferous mixed forests and found that L-band SAR outperformed optical data in all three fuel load types, with estimation accuracy further improved when both were integrated. Li et al. (2022b) used a data-driven random forest model to correlate long-term spatiotemporal characteristics derived from Landsat 8 OLI and Sentinel-1 data with field-measured fuel load, estimating the fine fuel load (FFL) of pine forests in some areas of Sichuan Province, China. The study found that combining SAR and multispectral data improved FFL estimation accuracy, and temporal features were more important than spatial features. 

The comparison between optical and SAR sensor-based fuel load estimation accuracy highlights the importance of canopy structure information in remote sensing-based fuel load estimation. Compared to the fuel load assessment methods based on optical or SAR imagery mentioned earlier, airborne LiDAR provides more detailed information about vegetation’s threedimensional structure (Aragoneses et al., 2024). Therefore, airborne and satellite-based LiDAR sensors can more directly and accurately estimate fuel load at different scales. For instance, Skowronski et al. (2011) used a LiDAR system to estimate canopy fuel load in pine-dominated forests in New Jersey, USA, predicting crown bulk density and canopy fuel weight. Chen et al. (2017) effectively estimated ground fuel load in Western Australia’s Jarrah forests by combining LiDAR data with previous year fire data, canopy density, elevation, and fuel types. Bright et al. (2017) compared the performance of airborne LiDAR and Landsat time-series data in estimating forest canopy and surface fuel load in a study area in Grand County, Colorado, USA, finding that Landsat provided limited improvement in fuel load estimation. Labenski et al. (2023) further combined Sentinel-2 multispectral data with airborne LiDAR data to extract forest structure and composition information for two forest areas in southwestern Germany, using a random forest model to predict and map surface fuel load. In another study, D’Este et al. (2021) incorporated Sentinel-1 SAR data into a fuel load estimation model based on Sentinel-2 multispectral 

42 

data and airborne LiDAR data for southeastern Italy, estimating dead fine fuel load. The study found that compared to NDVI and C-band SAR data, LiDAR variables had a stronger capacity to estimate dead fine fuel load. The study also found that woody vegetation contributed more to fuel load, consistent with the findings of Li et al. (2020). 

In addition, the more recent NASA GEDI full-waveform LiDAR sensor has been widely used for large-scale above-ground biomass estimation and vegetation canopy structure analysis (Myroniuk et al., 2023; Liang et al., 2023; Aragoneses et al., 2024; Guerra-Hernández et al., 2024), aiding wildfire simulation, assessment of wildfire impacts on vegetation, and understanding wildfire severity. However, only a few studies have directly used GEDI LiDAR data to estimate fuel load. For example, Leite et al. (2022) used unmanned aerial vehicle (UAV) simulations and GEDI data to study the ability to stratify fuel load in grasslands, savannas, and forests within tropical savannas in Brazil. The study found that GEDI performed poorly in estimating fuel load for ground and low-lying vegetation, and was significantly affected by terrain. 

It is important to note that the aforementioned studies do not explicitly distinguish between live and dead fuel. Notably, dead fuel load is a critical component of forest ecosystems and a key determinant of wildfire behavior (Rothermel, 1972; Woodall et al., 2013), warranting special attention. In particular, fine dead fuel is emphasized because it dries rapidly and is highly flammable, making it the primary carrier of fire ignition and spread (Cruz et al., 2003; Elia et al., 2020; D’Este et al., 2021). Additionally, dead and down woody debris (DWD) is another significant contributor to wildfires, particularly influencing surface fire intensity and the transition from surface to crown fire (Alexander, 1982; Hanes et al., 2021). Once surface fires reach the canopy, wildfire intensity and suppression difficulty increase substantially under high wind speeds (Schroeder and Buck, 1977; Hanes et al., 2021). However, estimating dead fuel load remains challenging. Apart from fine fuels such as annual grasses in open grasslands, forest components like litter, duff, and DWD are often invisible in optical remote sensing data, particularly in dense forest regions. 

D’Este et al. (2021) noted that dead fuel load estimation is typically conducted using standard fuel parameter models (Rothermel, 1972; Ottmar et al., 2007) or field sampling. However, our investigation reveals that alternative approaches, including estimation based on net primary productivity (NPP) or above-ground biomass (AGB), field sampling with extrapolation, and remote sensing-based retrieval, are also widely employed. 

The theoretical basis for estimating fuel load using NPP lies in the fact that NPP represents the rate of vegetation growth and is equivalent to litter production (Matthews, 1997). Based on this principle, Clarke et al. (2016) used the BIOS2 modeling environment to simulate fuel load (fine litter) and NPP in Australia. To establish the relationship between these variables, Australia was divided into six climatic regions, and the Pearson correlation coefficient was used to determine the statistical relationship between annual NPP and annual fine litter in each region. Subsequently, the Community Atmosphere-Biosphere 

Land Exchange (CABLE) land surface model was used to simulate NPP under various climate scenarios. Using the previously derived NPP–fuel load relationship, fuel load was estimated from NPP across the study regions. Finally, the estimated fuel load values were expressed in g C m<sup>−2</sup> and converted to t ha<sup>−1</sup> , assuming a carbon fraction of 47%. 

Furthermore, McNorton and Di Giuseppe (2024) developed a long-term global-scale fuel load dataset by integrating the Net Ecosystem Exchange (NEE) model with satellite observations. The study first used the ESA Biomass Climate Change Initiative (ESA-CCI) v3 dataset as the initial global above-ground biomass (AGB) estimate for 2010. Subsequently, AGB was dynamically updated using the ECLand land surface model, ERA5 meteorological data, and ESA-CCI AGB changes from 2010 to 2018. The model further partitions AGB into foliage and wood and classifies each component into live and dead fractions. A static live-to-dead biomass ratio is assigned to each of the 20 vegetation types in the ECLand model based on literature estimates. Finally, the dead foliage and dead wood fuel loads are estimated using the following equations: 



<!-- Start of picture text -->
TFdead = DFP 100 × ( AGB  − ( TWlive  +  TFlive  +  S Wlive )) (A.1)<br><!-- End of picture text -->



<!-- Start of picture text -->
TWdead = 1 − DFP × ( AGB  − ( TWlive  +  TFlive  +  S Wlive ))<br>� 100 �<br>(A.2)<br><!-- End of picture text -->

where _TFdead_ and _TWdead_ represent the dead foliage and dead wood fuel loads (kg m<sup>−2</sup> ), respectively. _AGB_ denotes the aboveground biomass (kg m<sup>−2</sup> ), obtained from satellite observations and land surface models. _TWlive_ and _TFlive_ correspond to the live wood and live foliage fuel loads, respectively, with _TWlive_ representing short-lived seasonal wood mass (e.g., twigs) and _TFlive_ determined using leaf mass per unit area (LMA) and LAI. _S Wlive_ refers to live structural wood, including long-lived biomass such as tree trunks. The parameter _DFP_ represents the dead foliage percentage, which is vegetation-type dependent and remains constant over time. 

These approaches establish relationships between NPP or AGB and fuel load; however, they often rely on idealized assumptions. For instance, Clarke et al. (2016) assumed a linear relationship between NPP and fine litter while neglecting mechanistic changes in litterfall and decomposition. Similarly, McNorton and Di Giuseppe (2024) adopted static live-to-dead biomass ratios and simplified fuel decomposition processes. In contrast, although field sampling methods are expensive and time-consuming, they provide more accurate estimates of dead fuel load. 

To improve estimation accuracy, some studies have integrated field sampling with allometric equations to quantify dead fuel load for specific species. For example, Deltell et al. (2024) conducted an investigation in Ayora, eastern Valencia Province on the Iberian Peninsula, focusing on nine Mediterranean species at different developmental stages. They measured basal stem diameter, height, maximum crown diameter, the perpendicular diameter to the maximum crown diameter, 

43 

and biomass for both live and dead fuels. Using plant structural variables as predictors, species- and development-stagespecific allometric equations were constructed to estimate live fuel, dead fuel, and total fuel load. 

In recent years, some countries have conducted large-scale national inventories of dead fuel load. Woodall et al. (2013) presented results from a nationwide forest downed and dead woody materials (DWM) inventory in the United States, using FIA plots and systematic sampling. Their study summarized total carbon storage and biomass density by state and common tree species while assessing relationships between DWM and factors such as climate, aboveground live biomass, and relative density of live trees. Similarly, Hanes et al. (2021) conducted field measurements of DWD fuel load across 766 National Forest Inventory plots and additional sites across Canada. Their study recorded key variables, including latitude, tree age, species, diameter at breast height (DBH), stand density, and soil drainage class. Using field sampling data combined with these explanatory variables and bioclimatic factors, they developed a multiple linear regression model to generate a nationwide distribution map of DWD fuel load across different forest types and ecological zones in Canada. 

Large-scale field inventories of dead fuel load provide reliable data for understanding fuel characteristics but are not suitable for real-time wildfire risk prediction. Additionally, extrapolation models often rely on idealized assumptions, leading to inaccuracies in dead fuel load estimation (Hanes et al., 2021). Consequently, recent studies have explored the use of remote sensing data to provide real-time and repeatable dead fuel load estimates for regional scale. Fundamentally, these studies aim to establish relationships between ground inventory data and one or more remote sensing datasets or derived indices. 

Passive optical remote sensing images cannot retrieve fuel loads beneath the canopy due to vegetation occlusion and are unable to provide estimates for horizontal and vertical fuel layers within forest stands. Therefore, LiDAR, which captures vegetation’s three-dimensional (3D) structure, is widely used for fuel load estimation. For instance, Lopes Queiroz et al. (2020) proposed a method for estimating coarse woody debris (CWD) volume by integrating high-resolution optical imagery (5 cm GSD) with multispectral LiDAR (including SWIR, NIR, and green channels). Their approach involved first segmenting optical imagery using a random forest classifier to extract visible CWD layers (vCWD) and then estimating canopy-covered CWD distribution using LiDAR-derived active vegetation indices (aNDVI, aNBR). A two-stage zero-adjusted gamma (ZAGA) model was constructed, where a binomial submodel (input variables: vCWD, wetland probability) predicted the probability of CWD occurrence, and a continuous submodel (input variables: vCWD², canopy closure) estimated CWD volume, optimized using the AICc criterion. Experimental results demonstrated that incorporating LiDAR significantly improved model performance compared to optical imagery alone, achieving _R_<sup>2</sup> = 0.72 (RMSE = 0.198 m³/100m²) in independent validation. However, limitations remained, including noise in aNDVI due to the low point density (1.51 pts/m²) of the LiDAR green channel and missing ground points in areas with high canopy 

closure. Additionally, the model’s reliance on wetland probability and maximum tree height variables requires further validation in heterogeneous forests. 

Lin et al. (2024) further investigated the capability of airborne LiDAR alone for estimating four types of dead fuel loads (1-hour, 10-hour, 100-hour, and litter) in southern Italy’s Apulia region. Their study developed multiple linear regression models relating airborne LiDAR-derived height and canopy cover indices to field-sampled dead fuel loads. Regression analysis results showed a predictive _R_<sup>2</sup> between 0.521 and 0.569, with nRMSE values ranging from 0.110 to 0.169. These findings suggest that airborne LiDAR may not accurately estimate dead fuel load, particularly given the study’s LiDAR resolution of 3 pts/m² and the influence of fine fuel size, terrain complexity, environmental factors, and the simplicity of the multiple linear regression model. However, the study identified canopy structural parameters as critical predictors of dead fuel load, consistent with the findings of Lopes Queiroz et al. (2020); Hanes et al. (2021), reinforcing the importance of vegetation 3D structure in fuel load estimation. 

Building on airborne LiDAR data, D’Este et al. (2021) incorporated Sentinel-2 multispectral and Sentinel-1 SAR data to estimate 1-hour dead fine fuel load in southeastern Italy’s Apulia region. Sentinel-1 SAR’s VH and VV polarization data were used for surface reflectance analysis, Sentinel-2 multispectral data for vegetation index calculations, and airborne LiDAR for generating canopy height models (CHM), canopy cover, and vegetation density. RF, support vector machine (SVM), and multiple linear regression (MLR) models were developed to estimate 1-hour dead fine fuel load using these explanatory variables. The study found that, compared to NDVI and C-band SAR data, LiDAR-derived variables (canopy height and cover) contributed more to fine fuel load estimation. Among the models, RF performed best, achieving RMSE = 0.09 t/ha, _R_<sup>2</sup> = 0.50, and a Pearson correlation coefficient _r_ = 0.71. 

Both Lin et al. (2024) and D’Este et al. (2021) highlight that even with airborne LiDAR, model performance may not meet the high accuracy requirements for fine dead fuel load estimation. However, compared to Lopes Queiroz et al. (2020), which focused on larger dead fuels (CWD), LiDAR demonstrated higher accuracy in retrieving CWD volume ( _R_<sup>2</sup> = 0.72, RMSE = 0.198 m³/100m²). These findings suggest that while LiDAR effectively estimates coarse woody debris, its performance in fine dead fuel load retrieval remains limited, necessitating further improvements in data integration and modeling approaches. 

Compared to dead fuel load estimation methods that rely solely on or integrate LiDAR, Li et al. (2021a) highlighted that LiDAR is cost-prohibitive, making it difficult to analyze fuel dynamics across spatial and temporal scales. To address this limitation, their study in southwestern Sichuan, China, explored the use of Sentinel-1 VH and VV polarization data, Sentinel-2 reflectance data, and topographic variables (elevation, slope, and aspect) to estimate five types of forest dead fuel load (FDFL)—1-hour, 10-hour, 100-hour, litter, and the total dead fuel load—using a random forest regression approach. The results indicated that 1-hour and 10-hour FDFL exhib- 

44 

ited the highest correlation with SAR data, while 100-hour FDFL showed similar correlations with both SAR and optical data. Litter was more strongly associated with Sentinel-2 data, whereas the total FDFL was highly negatively correlated with Sentinel-1 VH polarization and visible bands. In terms of predictive performance, 1-hour fuel exhibited the highest accuracy with _R_<sup>2</sup> = 0.57 and MSE = 0.18 tons/ha, while 10-hour and 100-hour fuel achieved _R_<sup>2</sup> values of 0.40 and 0.29, respectively. Overall, C-band SAR combined with multispectral data was still insufficient for accurate dead fuel load estimation. 

From the above review, it is evident that whether using AGB, NPP-, or allometric equation-based retrieval methods, field sampling extrapolation, or LiDAR-based inversion, all these approaches fundamentally estimate dead fuel load indirectly through vegetation biomass or three-dimensional structural information (e.g., canopy cover, canopy height, leaf area index (LAI), gap fraction, and understory density), rather than directly capturing the three-dimensional or spectral characteristics of dead fuel load for quantitative estimation. This limitation likely stems from the inability of passive optical imagery to penetrate the canopy, restricting its capacity to retrieve sub-canopy fuel distribution. Meanwhile, although LiDAR and SAR offer all-weather capabilities, they exhibit low sensitivity to fine dead fuels, with SAR further constrained by environmental factors such as soil moisture. Consequently, direct estimation of dead fuel load is expected to remain a significant challenge in the future. A more feasible solution under data-limited conditions may be to develop a comprehensive understanding of the relationships between climate, topography, vegetation type, structure, and developmental stages with dead fuel load. 

## **References** 

- Abatzoglou, J.T., Kolden, C.A., 2011. Relative importance of weather and climate on wildfire growth in interior alaska. International Journal of Wildland Fire 20, 479–486. 

- Abatzoglou, J.T., Kolden, C.A., 2013. Relationships between climate and macroscale area burned in the western united states. International Journal of Wildland Fire 22, 1003–1020. 

- Abatzoglou, J.T., Kolden, C.A., Balch, J.K., Bradley, B.A., 2016. Controls on interannual variability in lightning-caused fire activity in the western us. Environmental Research Letters 11, 045005. 

- Abdollahi, A., Pradhan, B., 2023. Explainable artificial intelligence (XAI) for interpreting the contributing factors feed into the wildfire susceptibility prediction model. SCIENCE OF THE TOTAL ENVIRONMENT 879, 163004. URL: `https://www.webofscience.com/api/gateway? GWVersion=2&SrcAuth=DynamicDOIArticle&SrcApp=WOS&KeyAID= 10.1016%2Fj.scitotenv.2023.163004&DestApp=DOI&SrcAppSID= USW2EC0D7EfQ4jdthTkoDVukmMmGx&SrcJTitle=SCIENCE+OF+ THE+TOTAL+ENVIRONMENT&DestDOIRegistrantName=Elsevier` , doi: `10.1016/j.scitotenv.2023.163004` . num Pages: 14 Place: Amsterdam Publisher: Elsevier Web of Science ID: WOS:000973651700001. 

- Achu, A.L., Thomas, J., Aju, C.D., Gopinath, G., Kumar, S., Reghunath, R., 2021. Machine-learning modelling of fire susceptibility in a forest-agriculture mosaic landscape of southern India. Ecological Informatics 64, 101348. URL: `https://www. sciencedirect.com/science/article/pii/S1574954121001394` , doi: `10.1016/j.ecoinf.2021.101348` . 

- Addison, P., Oommen, T., 2018. Utilizing satellite radar remote sensing for burn severity estimation. International journal of applied earth observation and geoinformation 73, 292–299. 

- Adhikari, B., Xu, C., Hodza, P., Minckley, T., 2021. Developing a geospatial data-driven solution for rapid natural wildfire risk assessment. Applied Geography 126, 102382. URL: `https://www. sciencedirect.com/science/article/pii/S0143622820314818` , doi: `10.1016/j.apgeog.2020.102382` . 

- Agee, J.K., Skinner, C.N., 2005. Basic principles of forest fuel reduction treatments. Forest ecology and management 211, 83–96. 

- Ager, A.A., Day, M.A., McHugh, C.W., Short, K., Gilbertson-Day, J., Finney, M.A., Calkin, D.E., 2014a. Wildfire exposure and fuel management on western US national forests. Journal of Environmental Management 145, 54–70. URL: `https://linkinghub.elsevier.com/retrieve/pii/ S0301479714002916` , doi: `10.1016/j.jenvman.2014.05.035` . 

- Ager, A.A., Preisler, H.K., Arca, B., Spano, D., Salis, M., 2014b. Wildfire risk estimation in the mediterranean area. Environmetrics 25, 384–396. 

- Ager, A.A., Vaillant, N.M., Finney, M.A., 2010. A comparison of landscape fuel treatment strategies to mitigate wildland fire risk in the urban interface and preserve old forest structure. Forest Ecology and Management 259, 1556–1570. URL: `https://www. sciencedirect.com/science/article/pii/S0378112710000514` , doi: `10.1016/j.foreco.2010.01.032` . 

- Albini, F.A., 1976. Estimating wildfire behavior and effects. volume 30. Department of Agriculture, Forest Service, Intermountain Forest and Range . . . . 

- Aldersley, A., Murray, S.J., Cornell, S.E., 2011. Global and regional analysis of climate and human drivers of wildfire. Science of The Total Environment 409, 3472–3481. URL: `https://www. sciencedirect.com/science/article/pii/S0048969711005353` , doi: `10.1016/j.scitotenv.2011.05.032` . 

- Alexander, M.E., 1982. Calculating and interpreting forest fire intensities. Canadian Journal of Botany 60, 349–357. 

- Ali, S., Abuhmed, T., El-Sappagh, S., Muhammad, K., Alonso-Moral, J.M., Confalonieri, R., Guidotti, R., Del Ser, J., Díaz-Rodríguez, N., Herrera, F., 2023. Explainable artificial intelligence (xai): What we know and what is left to attain trustworthy artificial intelligence. Information fusion 99, 101805. 

- Allaire, F., Mallet, V., Filippi, J.B., 2021. Emulation of wildland fire spread simulation using deep learning. Neural networks 141, 184–198. 

- Alonso, L., Gans, F., Karasante, I., Ahuja, A., Prapas, I., Kondylatos, S., Papoutsis, I., Panagiotou, E., Mihail, D., Cremer, F., Weber, U., Carvalhais, N., 2023. SeasFire Cube: A Global Dataset for Seasonal Fire Modeling in the Earth System. URL: `https://doi.org/10.5281/zenodo.8055879` , doi: `10.5281/zenodo.8055879` . 

- Andela, N., Morton, D.C., Giglio, L., Paugam, R., Chen, Y., Hantson, S., Van Der Werf, G.R., Randerson, J.T., 2019. The global fire atlas of individual fire size, duration, speed and direction. Earth System Science Data 11, 529–552. 

- Andersen, H.E., McGaughey, R.J., Reutebuch, S.E., 2005. Estimating forest canopy fuel parameters using lidar data. Remote sensing of Environment 94, 441–449. 

- Aragoneses, E., García, M., Ruiz-Benito, P., Chuvieco, E., 2024. Mapping forest canopy fuel parameters at european scale using spaceborne lidar and satellite data. Remote Sensing of Environment 303, 114005. 

- Arellano-Pérez, S., Castedo-Dorado, F., López-Sánchez, C.A., GonzálezFerreiro, E., Yang, Z., Díaz-Varela, R.A., Álvarez-González, J.G., Vega, J.A., Ruiz-González, A.D., 2018. Potential of sentinel-2a data to model surface and canopy fuel characteristics in relation to crown fire hazard. Remote Sensing 10, 1645. 

- Arroyo, L.A., Pascual, C., Manzanera, J.A., 2008. Fire models and methods to map fuel types: The role of remote sensing. Forest ecology and management 256, 1239–1252. 

- Artés, T., Oom, D., De Rigo, D., Durrant, T.H., Maianti, P., Libertà, G., SanMiguel-Ayanz, J., 2019. A global wildfire dataset for the analysis of fire regimes and fire behaviour. Scientific data 6, 296. 

- Asif, N.A., Sarker, Y., Chakrabortty, R.K., Ryan, M.J., Ahamed, M.H., Saha, D.K., Badal, F.R., Das, S.K., Ali, M.F., Moyeen, S.I., Islam, M.R., Tasneem, Z., 2021. Graph neural network: A comprehensive review on noneuclidean space. IEEE Access 9, 60588–60606. doi: `10.1109/ACCESS. 2021.3071274` . 

- Badia-Perpinyà, A., Pallares-Barbera, M., 2006. Spatial distribution of ignitions in mediterranean periurban and rural areas: the case of catalonia. International journal of Wildland fire 15, 187–196. 

- Bakke, S.J., Wanders, N., Van Der Wiel, K., Tallaksen, L.M., 2023. A data- 

45 

driven model for Fennoscandian wildfire danger. Natural Hazards and Earth System Sciences 23, 65–89. URL: `https://www.duo.uio.no/handle/ 10852/108719` , doi: `10.5194/nhess-23-65-2023` . accepted: 2024-0227T18:29:41Z. 

- Balaguer-Romano, R., Díaz-Sierra, R., De Cáceres, M., Cunill-Camprubí, À., Nolan, R.H., Boer, M.M., Voltas, J., de Dios, V.R., 2022. A semimechanistic model for predicting daily variations in species-level live fuel moisture content. Agricultural and Forest Meteorology 323, 109022. 

- Balch, J.K., Bradley, B.A., Abatzoglou, J.T., Nagy, R.C., Fusco, E.J., Mahood, A.L., 2017. Human-started wildfires expand the fire niche across the united states. Proceedings of the National Academy of Sciences 114, 2946–2951. 

- Baltrušaitis, T., Ahuja, C., Morency, L.P., 2018. Multimodal machine learning: A survey and taxonomy. IEEE transactions on pattern analysis and machine intelligence 41, 423–443. 

- Bar Massada, A., Syphard, A.D., Hawbaker, T.J., Stewart, S.I., Radeloff, V.C., 2011. Effects of ignition location models on the burn patterns of simulated wildfires. Environmental Modelling & Software 26, 583– 592. URL: `https://www.sciencedirect.com/science/article/ pii/S1364815210003233` , doi: `10.1016/j.envsoft.2010.11.016` . 

- Barber, Q.E., Jain, P., Whitman, E., Thompson, D.K., Guindon, L., Parks, S.A., Wang, X., Hethcoat, M.G., Parisien, M.A., 2024. The canadian fire spread dataset. Scientific data 11, 764. 

- Barmpoutis, P., Papaioannou, P., Dimitropoulos, K., Grammalidis, N., 2020. A review on early forest fire detection systems using optical remote sensing. Sensors 20. URL: `https://www.mdpi.com/1424-8220/20/22/6442` , doi: `10.3390/s20226442` . 

- Benali, A., Russo, A., Sá, A.C., Pinto, R.M., Price, O., Koutsias, N., Pereira, J.M., 2016. Determining fire dates and locating ignition points with satellite data. Remote Sensing 8, 326. 

- Bergado, J.R., Persello, C., Reinke, K., Stein, A., 2021. Predicting wildfire burns from big geodata using deep learning. Safety Science 140, 105276. URL: `https://www.sciencedirect.com/ science/article/pii/S0925753521001211` , doi: `10.1016/j.ssci. 2021.105276` . 

- Bergonse, R., Oliveira, S., Gonçalves, A., Nunes, S., DaCamara, C., Zêzere, J.L., 2021. Predicting burnt areas during the summer season in Portugal by combining wildfire susceptibility and spring meteorological conditions. Geomatics, Natural Hazards and Risk 12, 1039–1057. URL: `https://doi.org/10.1080/19475705.2021.1909664` , doi: `10. 1080/19475705.2021.1909664` . publisher: Taylor & Francis _eprint: https://doi.org/10.1080/19475705.2021.1909664. 

- Bessie, W., Johnson, E., 1995. The relative importance of fuels and weather on fire behavior in subalpine forests. Ecology 76, 747–762. 

- Bhowmik, R.T., Jung, Y.S., Aguilera, J.A., Prunicki, M., Nadeau, K., 2023. A multi-modal wildfire prediction and early-warning system based on a novel machine learning framework. Journal of Environmental Management 341, 117908. URL: `https://www.sciencedirect.com/science/ article/pii/S0301479723006965` , doi: `10.1016/j.jenvman.2023. 117908` . 

- Bi, K., Xie, L., Zhang, H., Chen, X., Gu, X., Tian, Q., 2023. Accurate mediumrange global weather forecasting with 3d neural networks. Nature 619, 533– 538. 

- Bianchi, L.O., Defossé, G.E., 2015. Live fuel moisture content and leaf ignition of forest species in Andean Patagonia, Argentina. International Journal of Wildland Fire 24, 340–348. URL: `https://www.publish.csiro.au/ wf/WF13099` , doi: `10.1071/WF13099` . publisher: CSIRO PUBLISHING. 

- Bjånes, A., De La Fuente, R., Mena, P., 2021. A deep learning ensemble model for wildfire susceptibility mapping. Ecological Informatics 65, 101397. 

- Bommer, P.L., Kretschmer, M., Hedström, A., Bareeva, D., Höhne, M.M.C., 2024. Finding the right xai method—a guide for the evaluation and ranking of explainable ai methods in climate science. Artificial Intelligence for the Earth Systems 3, e230074. 

- Bond, W.J., Woodward, F.I., Midgley, G.F., 2005. The global distribution of ecosystems in a world without fire. New phytologist 165, 525–538. 

- Boroujeni, S.P.H., Razi, A., Khoshdel, S., Afghah, F., Coen, J.L., O’Neill, L., Fule, P., Watts, A., Kokolakis, N.M.T., Vamvoudakis, K.G., 2024. A comprehensive survey of research towards ai-enabled unmanned aerial systems in pre-, active-, and post-wildfire management. Information Fusion , 102369. 

- Botequim, B., Fernandes, P.M., Borges, J.G., González-Ferreiro, E., GuerraHernández, J., 2019. Improving silvicultural practices for mediterranean 

forests through fire behaviour modelling using lidar-derived canopy fuel characteristics. International Journal of Wildland Fire 28, 823–839. 

- Bouguettaya, A., Zarzour, H., Taberkit, A.M., Kechida, A., 2022. A review on early wildfire detection from unmanned aerial vehicles using deep learningbased computer vision algorithms. Signal Processing 190, 108309. 

- Bowd, E.J., Blair, D.P., Lindenmayer, D.B., 2021. Prior disturbance legacy effects on plant recovery post-high-severity wildfire. Ecosphere 12, e03480. 

- Bowyer, P., Danson, F., 2004. Sensitivity of spectral reflectance to variation in live fuel moisture content at leaf and canopy level. Remote Sensing of Environment 92, 297–308. 

- Bradshaw, L.S., Deeming, J.E., Burgan, R.E., Cohen, J.D., 1984. The 1978 National Fire-Danger Rating System: technical documentation. Technical Report. U.S. Department of Agriculture, Forest Service, Intermountain Forest and Range Experiment Station. URL: `http://dx.doi.org/10.2737/ INT-GTR-169` , doi: `10.2737/int-gtr-169` . 

- Braun, W.J., Jones, B.L., Lee, J.S., Woolford, D.G., Wotton, B.M., 2010. Forest fire risk assessment: an illustrative example from ontario, canada. Journal of Probability and Statistics 2010, 823018. 

- Bright, B.C., Hudak, A.T., Meddens, A.J., Hawbaker, T.J., Briggs, J.S., Kennedy, R.E., 2017. Prediction of forest canopy and surface fuels from lidar and satellite time series data in a bark beetle-affected forest. Forests 8, 322. 

- Burge, J., Bonanni, M., Ihme, M., Hu, L., 2021. Convolutional lstm neural networks for modeling wildland fire dynamics. URL: `https://arxiv. org/abs/2012.06679` , `arXiv:2012.06679` . 

- Burge, J., Bonanni, M.R., Hu, R.L., Ihme, M., 2023. Recurrent convolutional deep neural networks for modeling time-resolved wildfire spread behavior. Fire Technology 59, 3327–3354. 

- Byrne, B., Liu, J., Bowman, K.W., Pascolini-Campbell, M., Chatterjee, A., Pandey, S., Miyazaki, K., van der Werf, G.R., Wunch, D., Wennberg, P.O., et al., 2024. Carbon emissions from the 2023 canadian wildfires. Nature , 1–5. 

- Caccamo, G., Chisholm, L., Bradstock, R., Puotinen, M.L., Pippen, B., 2011. Monitoring live fuel moisture content of heathland, shrubland and sclerophyll forest in south-eastern australia using modis data. International Journal of Wildland Fire 21, 257–269. 

- Cahuantzi, R., Chen, X., Güttel, S., 2023. A comparison of lstm and gru networks for learning symbolic sequences, in: Science and Information Conference, Springer. pp. 771–785. 

- Calviño-Cancela, M., Chas-Amil, M.L., García-Martínez, E.D., Touza, J., 2016. Wildfire risk associated with different vegetation types within and outside wildland-urban interfaces. Forest Ecology and Management 372, 1–9. 

- Calviño-Cancela, M., Chas-Amil, M.L., García-Martínez, E.D., Touza, J., 2017. Interacting effects of topography, vegetation, human activities and wildland-urban interfaces on wildfire ignition risk. Forest Ecology and Management 397, 10–17. 

- Canisius, F., Chen, J.M., 2007. Retrieving forest background reflectance in a boreal region from Multi-angle Imaging SpectroRadiometer (MISR) data. Remote Sensing of Environment 107, 312– 321. URL: `https://www.sciencedirect.com/science/article/ pii/S0034425706004184` , doi: `10.1016/j.rse.2006.07.023` . 

- Cao, Y., Zhou, X., Yu, Y., Rao, S., Wu, Y., Li, C., Zhu, Z., 2024. Forest fire prediction based on time series networks and remote sensing images. Forests 15, 1221. 

- Capps, S.B., Zhuang, W., Liu, R., Rolinski, T., Qu, X., 2021. Modelling chamise fuel moisture content across california: A machine learning approach. International Journal of Wildland Fire 31, 136–148. 

- Caron, N., Guyeux, C., Aynes, B., 2024. Predicting wildfire events with calibrated probabilities, in: Proceedings of the 2024 16th International Conference on Machine Learning and Computing, Association for Computing Machinery, New York, NY, USA. p. 168–175. URL: `https://doi.org/ 10.1145/3651671.3651708` , doi: `10.1145/3651671.3651708` . 

- Castelvecchi, D., 2016. Can we open the black box of ai? Nature News 538, 20. 

- Castro, F.X., Tudela, A., Sebastià, M.T., 2003. Modeling moisture content in shrubs to predict fire risk in Catalonia (Spain). Agricultural and Forest Meteorology 116, 49–59. URL: `https://www. sciencedirect.com/science/article/pii/S0168192302002484` , doi: `10.1016/S0168-1923(02)00248-4` . 

- Catchpole, E., Catchpole, W., Viney, N., McCaw, W., Marsden-Smedley, J., 

46 

2001. Estimating fuel response time and predicting fuel moisture content from field data. International Journal of Wildland Fire 10, 215–222. 

- Catry, F.X., Rego, F.C., Bação, F.L., Moreira, F., 2009. Modeling and mapping wildfire ignition risk in portugal. International Journal of Wildland Fire 18, 921–931. 

- Cawson, J.G., Nyman, P., Schunk, C., Sheridan, G.J., Duff, T.J., Gibos, K., Bovill, W.D., Conedera, M., Pezzatti, G.B., Menzel, A., 2020. Estimation of surface dead fine fuel moisture using automated fuel moisture sticks across a range of forests worldwide. International Journal of Wildland Fire 29, 548–559. 

- Chan, J.Y.L., Leow, S.M.H., Bea, K.T., Cheng, W.K., Phoong, S.W., Hong, Z.W., Chen, Y.L., 2022. Mitigating the multicollinearity problem and its machine learning approach: A review. Mathematics 10. URL: `https:// www.mdpi.com/2227-7390/10/8/1283` , doi: `10.3390/math10081283` . 

- Chaparro, D., Jagdhuber, T., Piles, M., Jonard, F., Fluhrer, A., Vall-llossera, M., Camps, A., López-Martínez, C., Fernández-Morán, R., Baur, M., et al., 2024. Vegetation moisture estimation in the western united states using radiometer-radar-lidar synergy. Remote Sensing of Environment 303, 113993. 

- Chavalithumrong, A., Yoon, H.J., Voulgaris, P., 2021. Learning Wildfire Model from Incomplete State Observations. URL: `http://arxiv.org/abs/ 2111.14038` . arXiv:2111.14038 [cs]. 

- Chen, B., Jin, Y., 2022. Spatial patterns and drivers for wildfire ignitions in california. Environmental Research Letters 17, 055004. URL: `https://dx.doi.org/10.1088/1748-9326/ac60da` , doi: `10. 1088/1748-9326/ac60da` . 

- Chen, D., Cheng, S., Hu, J., Kasoar, M., Arcucci, R., 2024a. Explainable global wildfire prediction models using graph neural networks. arXiv preprint arXiv:2402.07152 . 

- Chen, J., Yang, Y., Peng, L., Chen, L., Ge, X., 2022. Knowledge graph representation learning-based forest fire prediction. Remote Sensing 14, 4391. 

- Chen, M., Wang, Y., Zheng, Z., You, X., Zeng, Y., 2023. Modeling the forest fire risk by incorporating a new human activity factor from nighttime light data. Geocarto International 38, 2289454. 

- Chen, R., He, B., Li, Y., Fan, C., Yin, J., Zhang, H., Zhang, Y., 2024b. Estimation of potential wildfire behavior characteristics to assess wildfire danger in southwest China using deep learning schemes. Journal of Environmental Management 351, 120005. URL: `https://linkinghub. elsevier.com/retrieve/pii/S0301479723027937` , doi: `10.1016/j. jenvman.2023.120005` . 

- Chen, R., He, B., Li, Y., Zhang, Y., Liao, Z., Fan, C., Yin, J., Zhang, H., 2024c. Incorporating fire spread simulation and machine learning algorithms to estimate crown fire potential for pine forests in sichuan, china. International Journal of Applied Earth Observation and Geoinformation 132, 104080. 

- Chen, W., Panahi, M., Khosravi, K., Pourghasemi, H.R., Rezaie, F., Parvinnezhad, D., 2019. Spatial prediction of groundwater potentiality using ANFIS ensembled with teaching-learning-based and biogeography-based optimization. Journal of Hydrology 572, 435– 448. URL: `https://www.sciencedirect.com/science/article/ pii/S0022169419302604` , doi: `10.1016/j.jhydrol.2019.03.013` . 

- Chen, Y., Morton, D.C., Andela, N., Giglio, L., Randerson, J.T., 2016. How much global burned area can be forecast on seasonal time scales using sea surface temperatures? Environmental Research Letters 11, 045001. URL: `https://dx.doi.org/10.1088/1748-9326/11/4/ 045001` , doi: `10.1088/1748-9326/11/4/045001` . publisher: IOP Publishing. 

- Chen, Y., Zhu, X., Yebra, M., Harris, S., Tapper, N., 2017. Development of a predictive model for estimating forest surface fuel load in Australian eucalypt forests with LiDAR data. Environmental Modelling & Software 97, 61–71. URL: `https://www.sciencedirect.com/science/article/ pii/S1364815216304418` , doi: `10.1016/j.envsoft.2017.07.007` . 

- Cheng, S., Chassagnon, H., Kasoar, M., Guo, Y., Arcucci, R., 2024. Deep learning surrogate models of jules-inferno for wildfire prediction on a global scale. IEEE Transactions on Emerging Topics in Computational Intelligence , 1–11doi: `10.1109/TETCI.2024.3445450` . 

- Cheng, S., Prentice, I.C., Huang, Y., Jin, Y., Guo, Y.K., Arcucci, R., 2022. Data-driven surrogate model with latent data assimilation: Application to wildfire forecasting. Journal of Computational Physics 464, 111302. 

- Cheng, T., Wang, J., 2008. Integrated spatio-temporal data mining for forest fire prediction. Transactions in GIS 12, 591–611. 

- Chicas, S.D., Østergaard Nielsen, J., Valdez, M.C., Chen, C.F., 2022. Mod- 

elling wildfire susceptibility in belize’s ecosystems and protected areas using machine learning and knowledge-based methods. Geocarto International 37, 15823–15846. 

- Chino, D.Y., Avalhais, L.P., Rodrigues, J.F., Traina, A.J., 2015. Bowfire: detection of fire in still images by integrating pixel color and texture analysis, in: 2015 28th SIBGRAPI conference on graphics, patterns and images, IEEE. pp. 95–102. 

- Chng, Y.X., Zheng, H., Han, Y., Qiu, X., Huang, G., 2024. Mask grounding for referring image segmentation, in: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pp. 26573–26583. 

- Chung, J., Gulcehre, C., Cho, K., Bengio, Y., 2014. Empirical evaluation of gated recurrent neural networks on sequence modeling. arXiv preprint arXiv:1412.3555 . 

- Chuvieco, E., Aguado, I., Jurdao, S., Pettinari, M.L., Yebra, M., Salas, J., Hantson, S., de la Riva, J., Ibarra, P., Rodrigues, M., et al., 2012. Integrating geospatial information into fire risk assessment. International journal of wildland fire 23, 606–619. 

- Chuvieco, E., Aguado, I., Salas, J., García, M., Yebra, M., Oliva, P., 2020. Satellite remote sensing contributions to wildland fire science and management. Current Forestry Reports 6, 81–96. 

- Chuvieco, E., Cocero, D., Riano, D., Martin, P., Martınez-Vega, J., De La Riva, J., Pérez, F., 2004. Combining ndvi and surface temperature for the estimation of live fuel moisture content in forest fire danger rating. Remote Sensing of Environment 92, 322–331. 

- Chuvieco, E., Congalton, R.G., 1989. Application of remote sensing and geographic information systems to forest fire hazard mapping. Remote sensing of Environment 29, 147–159. 

- Chuvieco, E., Deshayes, M., Stach, N., Cocero, D., Riaño, D., 1999. Short-term fire risk: foliage moisture content estimation from satellite data, in: Chuvieco, E. (Ed.), Remote Sensing of Large Wildfires: in the European Mediterranean Basin. Springer, Berlin, Heidelberg, pp. 17–38. URL: `https://doi.org/10.1007/978-3-642-60164-4_3` , doi: `10.1007/978-3-642-60164-4_3` . 

- Chuvieco, E., Riaño, D., Aguado, I., Cocero, D., 2002. Estimation of fuel moisture content from multitemporal analysis of landsat thematic mapper reflectance data: applications in fire danger assessment. International journal of remote sensing 23, 2145–2162. 

- Clark, K.L., Skowronski, N., Hom, J., Duveneck, M., Pan, Y., Van Tuyl, S., Cole, J., Patterson, M., Maurer, S., 2009. Decision support tools to improve the effectiveness of hazardous fuel reduction treatments in the new jersey pine barrens. International journal of wildland fire 18, 268–277. 

- Clarke, H., Pitman, A.J., Kala, J., Carouge, C., Haverd, V., Evans, J.P., 2016. An investigation of future fuel load and fire weather in australia. Climatic Change 139, 591–605. 

- Coen, J.L., Cameron, M., Michalakes, J., Patton, E.G., Riggan, P.J., Yedinak, K.M., 2013. WRF-Fire: Coupled Weather–Wildland Fire Modeling with the Weather Research and Forecasting Model. Journal of Applied Meteorology and Climatology 52, 16–38. URL: `https://journals. ametsoc.org/view/journals/apme/52/1/jamc-d-12-023.1.xml` , doi: `10.1175/JAMC-D-12-023.1` . publisher: American Meteorological Society Section: Journal of Applied Meteorology and Climatology. 

- Cohen, J.D., 1985. The national fire-danger rating system: basic equations. volume 82. US Department of Agriculture, Forest Service, Pacific Southwest Forest and . . . . 

- Comesaña-Cebral, L., Martínez-Sánchez, J., Suárez-Fernández, G., Arias, P., 2024. Wildfire response of forest species from multispectral lidar data. a deep learning approach with synthetic data. Ecological Informatics 81, 102612. 

- Coops, N.C., 2002. Eucalypt forest structure and synthetic aperture radar backscatter: a theoretical analysis. Trees 16, 28–46. 

- Coops, N.C., Tompalski, P., Goodbody, T.R., Queinnec, M., Luther, J.E., Bolton, D.K., White, J.C., Wulder, M.A., van Lier, O.R., Hermosilla, T., 2021. Modelling lidar-derived estimates of forest attributes over space and time: A review of approaches and future trends. Remote Sensing of Environment 260, 112477. 

- Coskuner, K.A., 2022. Assessing the performance of modis and viirs active fire products in the monitoring of wildfires: a case study in turkey. iForestBiogeosciences and Forestry 15, 85. 

- Cruz, M.G., Alexander, M.E., Wakimoto, R.H., 2003. Assessing canopy fuel stratum characteristics in crown fire prone fuel types of western north america. International Journal of Wildland Fire 12, 39–50. 

47 

- Cruz, M.G., Alexander, M.E., Wakimoto, R.H., 2004. Modeling the likelihood of crown fire occurrence in conifer forest stands. Forest Science 50, 640– 658. 

- Cruz, M.G., Alexander, M.E., Wakimoto, R.H., 2005. Development and testing of models for predicting crown fire rate of spread in conifer forest stands. Canadian Journal of Forest Research 35, 1626–1639. 

- Cunill Camprubi, A., González-Moreno, P., Resco de Dios, V., 2022. Live fuel moisture content mapping in the mediterranean basin using random forests and combining modis spectral and thermal data. Remote Sensing 14, 3162. 

- Cunningham, C.X., Williamson, G.J., Bowman, D.M., 2024. Increasing frequency and intensity of the most extreme wildfires on earth. Nature ecology & evolution 8, 1420–1425. 

- Dal Pozzolo, A., Caelen, O., Johnson, R.A., Bontempi, G., 2015. Calibrating probability with undersampling for unbalanced classification, in: 2015 IEEE symposium series on computational intelligence, IEEE. pp. 159–166. 

- Danson, F.M., Bowyer, P., 2004. Estimating live fuel moisture content from remotely sensed reflectance. Remote Sensing of Environment 92, 309–321. 

- Dasgupta, S., Qu, J.J., Hao, X., Bhoi, S., 2007. Evaluating remotely sensed live fuel moisture estimations for fire behavior predictions in georgia, usa. Remote Sensing of Environment 108, 138–150. 

- De Roo, R.D., Du, Y., Ulaby, F.T., Dobson, M.C., 2001. A semi-empirical backscattering model at l-band and c-band for a soybean canopy with soil moisture inversion. IEEE Transactions on Geoscience and Remote Sensing 39, 864–872. 

- Deeming, J.E., 1972. National fire-danger rating system. volume 84. Rocky Mountain Forest and Range Experiment Station, Forest Service, US . . . . 

- Deltell, L., Santana, V.M., Jaime Baeza, M., 2024. Allometric equations to calculate living and dead fuel loads in mediterranean species. European Journal of Forest Research 143, 739–749. 

- Deng, J., Wang, W., Gu, G., Chen, Z., Liu, J., Xie, G., Weng, S., Ding, L., Li, C., 2023. Wildfire susceptibility prediction using a multisource and spatiotemporal cooperative approach. Earth Science Informatics 16, 3511– 3529. 

- Deng, M., Volkamer, R.M., Wang, Z., Snider, J.R., Kille, N., Romero-Alvarez, L.J., 2022. Wildfire smoke observations in the western united states from the airborne wyoming cloud lidar during the bb-flux project. part ii: Vertical structure and plume injection height. Journal of Atmospheric and Oceanic Technology 39, 559–572. 

- Department of Agriculture Forestry and Fisheries South Africa, 2013. Notice 1099 of 2013: Publication of the fire danger rating system for general information in terms of section(9)1 on the National Veld and Forest Fire Act 1998 (Act No. 101, 1998). Department of Agriculture Forestry and Fisheries, South Africa. 

- Depicker, A., De Baets, B., Baetens, J.M., 2020. Wildfire ignition probability in belgium. Natural hazards and earth system sciences 20, 363–376. 

- Devlin, J., Chang, M.W., Lee, K., Toutanova, K., 2019. BERT: Pre-training of deep bidirectional transformers for language understanding, in: Burstein, J., Doran, C., Solorio, T. (Eds.), Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), Association for Computational Linguistics, Minneapolis, Minnesota. pp. 4171– 4186. URL: `https://aclanthology.org/N19-1423` , doi: `10.18653/ v1/N19-1423` . 

- Dong, Z., Zhao, F., Wang, G., Tian, Y., Li, H., 2024. A deep learning framework: Predicting fire radiative power from the combination of polar-orbiting and geostationary satellite data during wildfire spread. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing . 

- Donovan, V.M., Wonkka, C.L., Wedin, D.A., Twidwell, D., 2020. Land-use type as a driver of large wildfire occurrence in the us great plains. Remote Sensing 12, 1869. 

- Dorigo, W., Wagner, W., Albergel, C., Albrecht, F., Balsamo, G., Brocca, L., Chung, D., Ertl, M., Forkel, M., Gruber, A., et al., 2017. Esa cci soil moisture for improved earth system understanding: State-of-the art and future directions. Remote Sensing of Environment 203, 185–215. 

- Duff, T.J., Bell, T.L., York, A., 2012. Predicting continuous variation in forest fuel load using biophysical models: a case study in south-eastern Australia. International Journal of Wildland Fire 22, 318–332. URL: `https: //www.publish.csiro.au/wf/WF11087` , doi: `10.1071/WF11087` . publisher: CSIRO PUBLISHING. 

- Duff, T.J., Keane, R.E., Penman, T.D., Tolhurst, K.G., 2017. Revisiting wildland fire fuel quantification methods: the challenge of understanding a dy- 

namic, biotic entity. Forests 8, 351. 

- Dutta, R., Aryal, J., Das, A., Kirkpatrick, J.B., 2013. Deep cognitive imaging systems enable estimation of continental-scale fire incidence from climate data. Scientific reports 3, 3188. 

- Dzulhijjah, D.A., Majid, M.N., Alwanda, A.Y., Kusuma, D.C., Zakaria, F., Kusrini, K., Kusnawi, K., 2023. Comparative analysis of hybrid long shortterm memory models for fire danger index forecasting with weather data, in: 2023 6th International Conference on Information and Communications Technology (ICOIACT), pp. 165–170. doi: `10.1109/ICOIACT59844. 2023.10455879` . 

- D’Este, M., Elia, M., Giannico, V., Spano, G., Lafortezza, R., Sanesi, G., 2021. Machine learning techniques for fine dead fuel load estimation using multisource remote sensing data. Remote Sensing 13, 1658. 

- Eames, T., Russell-Smith, J., Yates, C., Edwards, A., Vernooij, R., Ribeiro, N., Steinbruch, F., van der Werf, G.R., 2021. Instantaneous pre-fire biomass and fuel load measurements from multi-spectral uas mapping in southern african savannas. Fire 4, 2. 

- Eddin, M.H.S., Roscher, R., Gall, J., 2023. Location-aware adaptive normalization: a deep learning approach for wildfire danger forecasting. IEEE Transactions on Geoscience and Remote Sensing 61, 1–18. 

- El-Madafri, I., Peña, M., Olmedo-Torre, N., 2023. The wildfire dataset: Enhancing deep learning-based forest fire detection with a diverse evolving open-source dataset focused on data representativeness and a novel multitask learning approach. Forests 14, 1697. 

- Elia, M., Giannico, V., Spano, G., Lafortezza, R., Sanesi, G., 2020. Likelihood and frequency of recurrent fire ignitions in highly urbanised mediterranean landscapes. International journal of wildland fire 29, 120–131. 

- Elkan, C., 2001. The foundations of cost-sensitive learning, in: International joint conference on artificial intelligence, Lawrence Erlbaum Associates Ltd. pp. 973–978. 

- Erhan, D., Bengio, Y., Courville, A., Vincent, P., 2009. Visualizing higher-layer features of a deep network. Ph.D. thesis. University of Montreal. 

- Erni, S., Wang, X., Swystun, T., Taylor, S.W., Parisien, M.A., Robinne, F.N., Eddy, B., Oliver, J., Armitage, B., Flannigan, M.D., 2024. Mapping wildfire hazard, vulnerability, and risk to canadian communities. International Journal of Disaster Risk Reduction 101, 104221. 

- Espeholt, L., Agrawal, S., Sønderby, C., Kumar, M., Heek, J., Bromberg, C., Gazen, C., Carver, R., Andrychowicz, M., Hickey, J., et al., 2022. Deep learning for twelve hour precipitation forecasts. Nature communications 13, 1–10. 

- Fan, C., He, B., 2021. A physics-guided deep learning model for 10-h dead fuel moisture content estimation. Forests 12, 933. 

- Fan, C., He, B., Yin, J., Chen, R., Zhang, H., 2024. Process-based and geostationary meteorological satellite-enhanced dead fuel moisture content estimation. GIScience & Remote Sensing 61, 2324556. 

- Fan, L., Wigneron, J.P., Xiao, Q., Al-Yaari, A., Wen, J., Martin-StPaul, N., Dupuy, J.L., Pimont, F., Al Bitar, A., Fernandez-Moran, R., et al., 2018. Evaluation of microwave remote sensing for monitoring live fuel moisture content in the mediterranean region. Remote Sensing of Environment 205, 210–223. 

- FAO, 2006. Fire management-Global assessment 2006. Technical Report. Food and Agriculture Organization of the United Nations. 

- Feng, G., Hu, Z., Zhang, L., Lu, H., 2021. Encoder fusion network with coattention embedding for referring image segmentation, in: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pp. 15506–15515. 

- Fensholt, R., Sandholt, I., 2003. Derivation of a shortwave infrared water stress index from MODIS near- and shortwave infrared data in a semiarid environment. Remote Sensing of Environment 87, 111– 121. URL: `https://www.sciencedirect.com/science/article/ pii/S0034425703001895` , doi: `10.1016/j.rse.2003.07.002` . 

- Ferguson, S.A., Ruthford, J.E., McKay, S.J., Wright, D., Wright, C., Ottmar, R., 2002. Measuring moisture dynamics to predict fire severity in longleaf pine forests. International Journal of Wildland Fire 11, 267–279. 

- Fernandes, P.M., Botelho, H.S., 2003. A review of prescribed burning effectiveness in fire hazard reduction. International Journal of wildland fire 12, 117–128. 

- Fernández-García, V., Beltrán-Marcos, D., Fernández-Guisuraga, J.M., Marcos, E., Calvo, L., 2022. Predicting potential wildfire severity across southern europe with global data sources. Science of the total environment 829, 154729. 

48 

- Fillmore, S.D., McCaffrey, S., Bean, R., Evans, A.M., Iniguez, J., Thode, A., Smith, A.M., Thompson, M.P., 2024. Factors influencing wildfire management decisions after the 2009 us federal policy update. International journal of wildland fire 33. 

- Finney, M.A., 1998. FARSITE, Fire Area Simulator–model development and evaluation. 4, US Department of Agriculture, Forest Service, Rocky Mountain Research Station. 

- Finney, M.A., 2002. Fire growth using minimum travel time methods. Canadian Journal of Forest Research 32, 1420–1424. 

- Flannigan, M., Cantin, A.S., De Groot, W.J., Wotton, M., Newbery, A., Gowman, L.M., 2013. Global wildland fire season severity in the 21st century. Forest Ecology and Management 294, 54–61. 

- Food and Agriculture Organization of the United Nations (FAO), 2011. State of the World’s Forests 2011. Food and Agriculture Organization of the United Nations, Rome. 

- Forkel, M., Schmidt, L., Zotta, R.M., Dorigo, W., Yebra, M., 2023. Estimating leaf moisture content at global scale from passive microwave satellite observations of vegetation optical depth. Hydrology and Earth System Sciences 27, 39–68. URL: `https://hess.copernicus.org/articles/27/39/ 2023/` , doi: `10.5194/hess-27-39-2023` . publisher: Copernicus GmbH. 

- Frandsen, W.H., Andrews, P.L., Forest, I., Range Experiment Station (Ogden, U., 1979. Fire behavior in nonuniform fuels. volume no.232. Ogden, Utah, Intermountain Forest and Range Experiment Station, Forest Service, U.S. Dept. of Agriculture, 1979. URL: `https://www.biodiversitylibrary.org/item/136922` . https://www.biodiversitylibrary.org/bibliography/68702. 

- Fuller, M., 1991. Forest fires: an introduction to wildland fire behavior, management, firefighting, and prevention. John Wiley & Sons, Inc. 

- Fusco, E.J., Finn, J.T., Abatzoglou, J.T., Balch, J.K., Dadashi, S., Bradley, B.A., 2019. Detection rates and biases of fire observations from modis and agency reports in the conterminous united states. Remote Sensing of Environment 220, 30–40. 

- Gao, S., Huang, Y., Zhang, S., Han, J., Wang, G., Zhang, M., Lin, Q., 2020. Short-term runoff prediction with gru and lstm networks without requiring time step optimization during sample generation. Journal of Hydrology 589, 125188. 

- Gao, Y., Wang, R., Zhou, E., 2021. Stock prediction based on optimized lstm and gru models. Scientific Programming 2021, 4055281. 

- García, M., Riaño, D., Yebra, M., Salas, J., Cardil, A., Monedero, S., Ramirez, J., Martín, M.P., Vilar, L., Gajardo, J., et al., 2020. A live fuel moisture content product from landsat tm satellite time series for implementation in fire behavior models. Remote Sensing 12, 1714. 

- Ge, X., Yang, Y., Peng, L., Chen, L., Li, W., Zhang, W., Chen, J., 2022. Spatiotemporal knowledge graph based forest fire prediction with multi source heterogeneous data. Remote Sensing 14, 3496. 

- Gentilucci, M., Barbieri, M., Younes, H., Rihab, H., Pambianchi, G., 2024. Analysis of Wildfire Susceptibility by Weight of Evidence, Using Geomorphological and Environmental Factors in the Marche Region, Central Italy. Geosciences 14, 112. URL: `https://www.mdpi.com/2076-3263/14/ 5/112` , doi: `10.3390/geosciences14050112` . number: 5 Publisher: Multidisciplinary Digital Publishing Institute. 

- Gerard, S., Zhao, Y., Sullivan, J., 2023. Wildfirespreadts: A dataset of multimodal time series for wildfire spread prediction. Advances in Neural Information Processing Systems 36, 74515–74529. 

- Gers, F.A., Schmidhuber, J., Cummins, F., 2000. Learning to forget: Continual prediction with lstm. Neural computation 12, 2451–2471. 

- Ghorbanzadeh, O., Blaschke, T., 2018. Wildfire Susceptibility Evaluation By Integrating an Analytical Network Process Approach Into GIS-Based Analyses, in: Wildfire Susceptibility Evaluation By Integrating an Analytical Network Process Approach Into GIS-Based Analyses. URL: `https://uni-salzburg.elsevierpure.com/en/publications/ wildfire-susceptibility-evaluation-by-integrating-ananalytical-n` . 

- Ghorbanzadeh, O., Blaschke, T., Gholamnia, K., Aryal, J., 2019. Forest Fire Susceptibility and Risk Mapping Using Social/Infrastructural Vulnerability and Environmental Variables. Fire 2, 50. URL: `https://www.mdpi.com/ 2571-6255/2/3/50` , doi: `10.3390/fire2030050` . number: 3 Publisher: Multidisciplinary Digital Publishing Institute. 

- Giglio, L., Boschetti, L., Roy, D.P., Humber, M.L., Justice, C.O., 2018. The collection 6 modis burned area mapping algorithm and product. Remote sensing of environment 217, 72–85. 

- Giglio, L., Descloitres, J., Justice, C.O., Kaufman, Y.J., 2003. An enhanced contextual fire detection algorithm for modis. Remote Sensing of Environment 87, 273–282. URL: `https://www.sciencedirect.com/ science/article/pii/S0034425703001846` , doi: `https://doi.org/ 10.1016/S0034-4257(03)00184-6` . 

- Giglio, L., Randerson, J.T., Van Der Werf, G.R., 2013. Analysis of daily, monthly, and annual burned area using the fourth-generation global fire emissions database (gfed4). Journal of Geophysical Research: Biogeosciences 118, 317–328. 

- Giglio, L., Schroeder, W., Justice, C.O., 2016. The collection 6 modis active fire detection algorithm and fire products. Remote Sensing of Environment 178, 31–41. URL: `https://www.sciencedirect.com/science/ article/pii/S0034425716300827` , doi: `https://doi.org/10.1016/ j.rse.2016.02.054` . 

- Gilreath, J., 2006. Validation of Variables for the Creation of a Descriptive Fire Potential Model for the Southeastern Fire District of Mississippi. Theses and Dissertations URL: `https://scholarsjunction.msstate. edu/td/4942` . 

- Gincheva, A., Pausas, J.G., Edwards, A., Provenzale, A., Cerdà, A., Hanes, C., Royé, D., Chuvieco, E., Mouillot, F., Vissio, G., et al., 2024. A monthly gridded burned area database of national wildland fire data. Scientific data 11, 352. 

- Glossary of Wildland Fire Terminology, 2006. Glossary of Wildland Fire Terminology. Technical Report. National Wildfire Coordinating Group. 

- Gonzalez-Dugo, V., Zarco-Tejada, P., Berni, J.A., Suarez, L., Goldhamer, D., Fereres, E., 2012. Almond tree canopy temperature reveals intra-crown variability that is water stress-dependent. Agricultural and Forest Meteorology 154, 156–165. 

- Good, P.I., Hardin, J.W., 2012. Common errors in statistics (and how to avoid them). John Wiley & Sons. 

- Gopu, A., Ramakrishnan, A., Balasubramanian, G., Srinidhi, K., 2023. A comparative study on forest fire prediction using arima, sarima, lstm, and gru methods, in: 2023 IEEE International Conference on Contemporary Computing and Communications (InC4), IEEE. pp. 1–5. 

- Gould, J.S., McCaw, W.L., Cheney, N.P., 2011. Quantifying fine fuel dynamics and structure in dry eucalypt forest (eucalyptus marginata) in western australia for fire management. Forest ecology and management 262, 531–546. 

- Greenwell, B.M., et al., 2017. pdp: An r package for constructing partial dependence plots. R J. 9, 421. 

- de Groot, W.J., Cantin, A.S., Flannigan, M.D., Soja, A.J., Gowman, L.M., Newbery, A., 2013. A comparison of canadian and russian boreal forest fire regimes. Forest Ecology and Management 294, 23–34. 

- Group, C.F.C.F.D., Science, C.F.C., Directorate, S.D., 1992. Development and structure of the Canadian forest fire behavior prediction system. volume 3. Forestry Canada, Science and Sustainable Development Directorate. 

- Gu, A., Dao, T., 2023. Mamba: Linear-Time Sequence Modeling with Selective State Spaces. URL: `http://arxiv.org/abs/2312.00752` , doi: `10.48550/arXiv.2312.00752` . arXiv:2312.00752 [cs]. 

- Gu, A., Goel, K., Ré, C., 2021. Efficiently modeling long sequences with structured state spaces. arXiv preprint arXiv:2111.00396 . 

- Guerra-Hernández, J., Pereira, J.M., Stovall, A., Pascual, A., 2024. Impact of fire severity on forest structure and biomass stocks using nasa gedi data. insights from the 2020 and 2021 wildfire season in spain and portugal. Science of Remote Sensing 9, 100134. 

- Guk, E., Bar-Massada, A., Yebra, M., Scortechini, G., Levin, N., 2024. Examining the transferability of remote-sensing-based models of live fuel moisture content for predicting wildfire characteristics. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing 17, 14762– 14776. doi: `10.1109/JSTARS.2024.3445138` . 

- Guo, F., Wang, G., Su, Z., Liang, H., Wang, W., Lin, F., Liu, A., 2016. What drives forest fire in Fujian, China? Evidence from logistic regression and Random Forests. International Journal of Wildland Fire 25, 505– 519. URL: `https://www.publish.csiro.au/wf/WF15121` , doi: `10. 1071/WF15121` . publisher: CSIRO PUBLISHING. 

- Hair Jr, J.F., Anderson, R.E., Tatham, R.L., 1986. Multivariate data analysis with readings. Macmillan Publishing Co., Inc. 

- Hall, J.V., Argueta, F., Zubkova, M., Chen, Y., Randerson, J.T., Giglio, L., 2024. Glocab: global cropland burned area from mid-2002 to 2020. Earth System Science Data 16, 867–885. 

- Hall, S.A., Burke, I.C., 2006. Considerations for characterizing fuels as inputs for fire behavior models. Forest Ecology and Management 227, 102–114. 

49 

- Hanes, C.C., Wang, X., de Groot, W.J., 2021. Dead and down woody debris fuel loads in canadian forests. International journal of wildland fire 30, 871–885. 

- Hanes, C.C., Wang, X., Jain, P., Parisien, M.A., Little, J.M., Flannigan, M.D., 2019. Fire-regime changes in canada over the last half century. Canadian Journal of Forest Research 49, 256–269. 

- Hantson, S., Padilla, M., Corti, D., Chuvieco, E., 2013. Strengths and weaknesses of MODIS hotspots to characterize global fire occurrence. Remote Sensing of Environment 131, 152–159. URL: `https://www. sciencedirect.com/science/article/pii/S0034425712004610` , doi: `10.1016/j.rse.2012.12.004` . 

- Hao, X., Qu, J.J., 2007. Retrieval of real-time live fuel moisture content using modis measurements. Remote Sensing of Environment 108, 130–137. 

- Haque, M.K., Azad, M.A.K., Hossain, M.Y., Ahmed, T., Uddin, M., Hossain, M.M., 2021. Wildfire in australia during 2019-2020, its impact on health, biodiversity and environment with some proposals for risk management: a review. Journal of Environmental Protection 12, 391–414. 

- Hardy, C.C., 2005. Wildland fire hazard and risk: Problems, definitions, and context. Forest ecology and management 211, 73–82. 

- Hargrove, W.W., Kumar, J., Norman, S.P., Hoffman, F.M., 2022. Statistically determined global fire regimes (gfrs) empirically characterized using historical modis hotspots. URL: `https://doi.org/10.5281/zenodo. 6522071` , doi: `10.5281/zenodo.6522071` . 

- Harris, L.B., Taylor, A.H., Kassa, H., Leta, S., Powell, B., 2023. Humans and climate modulate fire activity across ethiopia. Fire Ecology 19, 15. 

- Harrison, S.P., Prentice, I.C., Bloomfield, K.J., Dong, N., Forkel, M., Forrest, M., Ningthoujam, R.K., Pellegrini, A., Shen, Y., Baudena, M., et al., 2021. Understanding and modelling wildfire regimes: an ecological perspective. Environmental Research Letters 16, 125008. 

- He, Z., Fan, G., Li, Z., Li, S., Gao, L., Li, X., Zeng, Z.C., 2024. Deep learning modeling of human activity affected wildfire risk by incorporating structural features: A case study in eastern china. Ecological Indicators 160, 111946. 

- Helman, D., Lensky, I.M., Tessler, N., Osem, Y., 2015. A Phenology-Based Method for Monitoring Woody and Herbaceous Vegetation in Mediterranean Forests from NDVI Time Series. Remote Sensing 7, 12314–12335. URL: `https://www.mdpi.com/2072-4292/7/9/12314` , doi: `10.3390/ rs70912314` . number: 9 Publisher: Multidisciplinary Digital Publishing Institute. 

- Hermosilla, T., Ruiz, L.A., Kazakova, A.N., Coops, N.C., Moskal, L.M., 2014. Estimation of forest structure and canopy fuel parameters from smallfootprint full-waveform lidar data. International Journal of Wildland Fire 23, 224–233. 

- Hertelendy, A.J., Howard, C., Sorensen, C., Ranse, J., Eboreime, E., Henderson, S., Tochkin, J., Ciottone, G., 2024. Seasons of smoke and fire: preparing health systems for improved performance before, during, and after wildfires. The Lancet Planetary Health 8, e588–e602. 

- Hillman, S., Wallace, L., Reinke, K., Jones, S., 2021. A comparison between tls and uas lidar to represent eucalypt crown fuel characteristics. ISPRS Journal of Photogrammetry and Remote Sensing 181, 295–307. 

- Hochreiter, S., 1997. Long short-term memory. Neural Computation MIT-Press 

- . 

- Hodges, J.L., Lattimer, B.Y., 2019. Wildland fire spread modeling using convolutional neural networks. Fire technology 55, 2115–2142. 

- Hoe, M.S., Dunn, C.J., Temesgen, H., 2018. Multitemporal lidar improves estimates of fire severity in forested landscapes. International Journal of Wildland Fire 27, 581–594. 

- Holder, A.L., Ahmed, A., Vukovich, J.M., Rao, V., 2023. Hazardous air pollutant emissions estimates from wildfires in the wildland urban interface. PNAS nexus 2, pgad186. 

- Holdrege, M.C., Schlaepfer, D.R., Palmquist, K.A., Crist, M., Doherty, K.E., Lauenroth, W.K., Remington, T.E., Riley, K., Short, K.C., Tull, J.C., Wiechman, L.A., Bradford, J.B., 2024. Wildfire probability estimated from recent climate and fine fuels across the big sagebrush region. Fire Ecology 20, 22. URL: `https://doi.org/10.1186/s42408-024-00252-4` , doi: `10.1186/s42408-024-00252-4` . 

- Hollis, J.J., Matthews, S., Fox-Hughes, P., Grootemaat, S., Heemstra, S., Kenny, B.J., Sauvage, S., 2024. Introduction to the australian fire danger rating system. International Journal of Wildland Fire 33. 

- Hong, H., Jaafari, A., Zenner, E.K., 2019. Predicting spatial patterns of wildfire susceptibility in the Huichang County, China: An integrated model to analysis of landscape indicators. Ecological Indicators 101, 878– 891. URL: `https://www.sciencedirect.com/science/article/` 

`pii/S1470160X19300792` , doi: `10.1016/j.ecolind.2019.01.056` . 

- Horton, D., Johnson, J.T., Baris, I., Jagdhuber, T., Bindlish, R., Park, J., AlKhaldi, M.M., 2024. Wildfire threshold detection and progression monitoring using an improved radar vegetation index in california. Remote Sensing 16, 3050. 

- Hu, P., Tanchak, R., Wang, Q., 2023a. Developing Risk Assessment Framework for Wildfire in the United States – A Deep Learning Approach to Safety and Sustainability. Journal of Safety and Sustainability URL: `https://www.sciencedirect.com/science/article/ pii/S2949926723000033` , doi: `10.1016/j.jsasus.2023.09.002` . 

- Hu, W.S., Li, H.C., Pan, L., Li, W., Tao, R., Du, Q., 2020. Spatial–spectral feature extraction via deep convlstm neural networks for hyperspectral image classification. IEEE Transactions on Geoscience and Remote Sensing 58, 4237–4250. doi: `10.1109/TGRS.2019.2961947` . 

- Hu, X., Wen, H., Zhang, P., Yuen, K.V., Zhong, P., 2024. Near realtime burned area progression mapping with multispectral data using ensemble learning. IEEE Geoscience and Remote Sensing Letters 21, 1–5. doi: `10.1109/LGRS.2024.3412173` . 

- Hu, X., Zhang, P., Ban, Y., Rahnemoonfar, M., 2023b. Gan-based sar and optical image translation for wildfire impact assessment using multi-source remote sensing data. Remote Sensing of Environment 289, 113522. 

- Huang, J., Loría-Salazar, S.M., Deng, M., Lee, J., Holmes, H.A., 2024. Assessment of smoke plume height products derived from multisource satellite observations using lidar-derived height metrics for wildfires in the western us. Atmospheric Chemistry and Physics 24, 3673–3698. 

- Huidobro, G., Giessen, L., Burns, S.L., 2024. And it burns, burns, burns, the ring-of-fire: Reviewing and harmonizing terminology on wildfire management and policy. Environmental Science & Policy 157, 103776. 

- Hunt Jr, E.R., Rock, B.N., Nobel, P.S., 1987. Measurement of leaf relative water content by infrared reflectance. Remote sensing of environment 22, 429–435. 

- Huot, F., Hu, R.L., Goyal, N., Sankar, T., Ihme, M., Chen, Y.F., 2022. Next day wildfire spread: A machine learning dataset to predict wildfire spreading from remote-sensing data. IEEE Transactions on Geoscience and Remote Sensing 60, 1–13. 

- Huot, F., Hu, R.L., Ihme, M., Wang, Q., Burge, J., Lu, T., Hickey, J., Chen, Y.F., Anderson, J., 2021. Deep Learning Models for Predicting Wildfires from Historical Remote-Sensing Data. URL: `http://arxiv.org/abs/ 2010.07445` . arXiv:2010.07445 [cs]. 

- Iban, M.C., Aksu, O., 2024. Shap-driven explainable artificial intelligence framework for wildfire susceptibility mapping using modis active fire pixels: An in-depth interpretation of contributing factors in izmir, türkiye. Remote Sensing 16, 2842. 

- Iban, M.C., Sekertekin, A., 2022. Machine learning based wildfire susceptibility mapping using remotely sensed fire data and gis: A case study of adana and mersin provinces, turkey. Ecological Informatics 69, 101647. 

- Jaafari, A., Gholami, D.M., Zenner, E.K., 2017. A Bayesian modeling of wildfire probability in the Zagros Mountains, Iran. Ecological Informatics 39, 32–44. URL: `https://linkinghub.elsevier.com/retrieve/pii/ S1574954117300912` , doi: `10.1016/j.ecoinf.2017.03.003` . 

- Jaafari, A., Mafi-Gholami, D., Thai Pham, B., Tien Bui, D., 2019. Wildfire Probability Mapping: Bivariate vs. Multivariate Statistics. Remote Sensing 11, 618. URL: `https://www.mdpi.com/2072-4292/11/6/618` , doi: `10.3390/rs11060618` . number: 6 Publisher: Multidisciplinary Digital Publishing Institute. 

- Jain, K., Gandhi, V., 2022. Comprehensive multi-modal interactions for referring image segmentation, in: Muresan, S., Nakov, P., Villavicencio, A. (Eds.), Findings of the Association for Computational Linguistics: ACL 2022, Association for Computational Linguistics, Dublin, Ireland. pp. 3427– 3435. URL: `https://aclanthology.org/2022.findings-acl.270` , doi: `10.18653/v1/2022.findings-acl.270` . 

- Jain, P., Barber, Q.E., Taylor, S.W., Whitman, E., Castellanos Acuna, D., Boulanger, Y., Chavardès, R.D., Chen, J., Englefield, P., Flannigan, M., et al., 2024. Drivers and impacts of the record-breaking 2023 wildfire season in canada. Nature Communications 15, 6764. 

- Jain, P., Coogan, S.C., Subramanian, S.G., Crowley, M., Taylor, S., Flannigan, M.D., 2020. A review of machine learning applications in wildfire science and management. Environmental Reviews 28, 478–505. URL: `https: //cdnsciencepub.com/doi/10.1139/er-2020-0019` , doi: `10.1139/ er-2020-0019` . publisher: NRC Research Press. 

- Jalilian, S., Jouibary, S.S., 2023. Forest wildfire risk mapping, performance 

50 

comparison of machine learning algorithms. Research Square . 

Jenks, G.F., Caspall, F.C., 1971. Error on choroplethic maps: definition, measurement, reduction. Annals of the Association of American Geographers 61, 217–244. 

- Ji, L., Du, Y., Dang, Y., Gao, W., Zhang, H., 2024a. A survey of methods for addressing the challenges of referring image segmentation. Neurocomputing 583, 127599. 

- Ji, Y., Wang, D., Li, Q., Liu, T., Bai, Y., 2024b. Global wildfire danger predictions based on deep learning taking into account static and dynamic variables. Forests 15, 216. 

- Jia, S., Kim, S.H., Nghiem, S.V., Kafatos, M., 2019. Estimating live fuel moisture using smap l-band radiometer soil moisture for southern california, usa. Remote Sensing 11, 1575. 

- Jiang, S., Sweet, L.b., Blougouras, G., Brenning, A., Li, W., Reichstein, M., Denzler, J., Shangguan, W., Yu, G., Huang, F., et al., 2024a. How interpretable machine learning can benefit process understanding in the geosciences. Earth’s Future 12, e2024EF004540. 

- Jiang, W., Qiao, Y., Su, G., Li, X., Meng, Q., Wu, H., Quan, W., Wang, J., Wang, F., 2023. Wfnet: A hierarchical convolutional neural network for wildfire spread prediction. Environmental Modelling & Software 170, 105841. 

- Jiang, W., Qiao, Y., Zheng, X., Zhou, J., Jiang, J., Meng, Q., Su, G., Zhong, S., Wang, F., 2024b. Wildfire risk assessment using deep learning in Guangdong Province, China. International Journal of Applied Earth Observation and Geoinformation 128, 103750. URL: `https://www. sciencedirect.com/science/article/pii/S1569843224001043` , doi: `10.1016/j.jag.2024.103750` . 

- Jiang, W., Wang, F., Su, G., Li, X., Wang, G., Zheng, X., Wang, T., Meng, Q., 2022. Modeling wildfire spread with an irregular graph network. Fire 5, 185. 

- Jin, G., Wang, Q., Zhu, C., Feng, Y., Huang, J., Hu, X., 2020a. Urban fire situation forecasting: Deep sequence learning with spatio-temporal dynamics. Applied Soft Computing 97, 106730. 

- Jin, G., Zhu, C., Chen, X., Sha, H., Hu, X., Huang, J., 2020b. Ufsp-net: a neural network with spatio-temporal information fusion for urban fire situation prediction, in: IOP Conference Series: Materials Science and Engineering, IOP Publishing. p. 012050. 

- Jolly, W.M., Cochrane, M.A., Freeborn, P.H., Holden, Z.A., Brown, T.J., Williamson, G.J., Bowman, D.M., 2015. Climate-induced variations in global wildfire danger from 1979 to 2013. Nature communications 6, 7537. 

- Jolly, W.M., Johnson, D.M., 2018. Pyro-ecophysiology: shifting the paradigm of live wildland fuel research. Fire 1, 8. 

- Jones, M.W., Brambleby, E., Andela, N., van der Werf, G.R., Parrington, M., Giglio, L., 2024a. State of wildfires 2023-24: Anomalies in burned area, fire emissions, and individual fire characteristics by continent, biome, country, and administrative region. doi: `10.5281/zenodo.11400539` . [data set]. 

- Jones, M.W., Kelley, D.I., Burton, C.A., Di Giuseppe, F., Barbosa, M.L.F., Brambleby, E., Hartley, A.J., Lombardi, A., Mataveli, G., McNorton, J.R., et al., 2024b. State of wildfires 2023–2024. Earth System Science Data 16, 3601–3685. 

- Josephson, J.R., Josephson, S.G., 1996. Abductive inference: Computation, philosophy, technology. Cambridge University Press. 

- Kadir, E.A., Kung, H.T., AlMansour, A.A., Irie, H., Rosa, S.L., Fauzi, S.S.M., 2023. Wildfire hotspots forecasting and mapping for environmental monitoring based on the long short-term memory networks deep learning algorithm. Environments 10, 124. 

- Kalamkar, S., et al., 2023. Multimodal image fusion: A systematic review. Decision Analytics Journal , 100327. 

- Kalantar, B., Ueda, N., Idrees, M.O., Janizadeh, S., Ahmadi, K., Shabani, F., 2020. Forest Fire Susceptibility Prediction Based on Machine Learning Models with Resampling Algorithms on Remote Sensing Data. Remote Sensing 12, 3682. URL: `https://www.mdpi.com/2072-4292/12/22/ 3682` , doi: `10.3390/rs12223682` . number: 22 Publisher: Multidisciplinary Digital Publishing Institute. 

- Kanwal, R., Rafaqat, W., Iqbal, M., Weiguo, S., 2023. Data-Driven Approaches for Wildfire Mapping and Prediction Assessment Using a Convolutional Neural Network (CNN). Remote Sensing 15, NA–NA. URL: `https:// go.gale.com/ps/i.do?p=AONE&sw=w&issn=20724292&v=2.1&it= r&id=GALE%7CA772535779&sid=googleScholar&linkaccess=abs` , doi: `10.3390/rs15215099` . publisher: MDPI AG. 

Karniadakis, G.E., Kevrekidis, I.G., Lu, L., Perdikaris, P., Wang, S., Yang, L., 

2021. Physics-informed machine learning. Nature Reviews Physics 3, 422– 440. 

- Katrutsa, A., Strijov, V., 2017. Comprehensive study of feature selection methods to solve multicollinearity problem according to evaluation criteria. Expert Systems with Applications 76, 1–11. 

- Keane, R.E., Burgan, R., Wagtendonk, J.v., 2001. Mapping wildland fuels for fire management across multiple scales: Integrating remote sensing, GIS, and biophysical modeling. International Journal of Wildland Fire 10, 301–319. URL: `https://www.publish.csiro.au/wf/wf01028` , doi: `10.1071/wf01028` . publisher: CSIRO PUBLISHING. 

- Keenan, R.J., Reams, G.A., Achard, F., de Freitas, J.V., Grainger, A., Lindquist, E., 2015. Dynamics of global forest area: Results from the fao global forest resources assessment 2015. Forest ecology and management 352, 9–20. 

- Khalaf, M.W.A., Jouibary, S.S., Jahdi, R., 2024. Performance analysis of convlstm, flammap, and ca algorithms to predict wildfire spread in golestan national park, ne iran. Environmental Modeling & Assessment , 1–14. 

- Khan, S.U., Khan, M.A., Azhar, M., Khan, F., Lee, Y., Javed, M., 2023. Multimodal medical image fusion towards future research: A review. Journal of King Saud University-Computer and Information Sciences 35, 101733. 

- Kiefer, M.T., Zhong, S., 2015. The role of forest cover and valley geometry in cold-air pool evolution. Journal of Geophysical Research: Atmospheres 120, 8693–8711. URL: `https://onlinelibrary.wiley.com/doi/ abs/10.1002/2014JD022998` , doi: `10.1002/2014JD022998` . _eprint: https://agupubs.onlinelibrary.wiley.com/doi/pdf/10.1002/2014JD022998. 

- Kilgore, B.M., Sando, R.W., 1975. Crown-fire potential in a sequoia forest after prescribed burning. Forest Science 21, 83–87. 

- Kim, D.W., Chung, W., Lee, B., 2016. Exploring tree crown spacing and slope interaction effects on fire behavior with a physics-based fire model. Forest Science and Technology 12, 167–175. 

- Kim, Y., Jackson, T., Bindlish, R., Lee, H., Hong, S., 2012. Radar vegetation index for estimating the vegetation water content of rice and soybean. IEEE Geoscience and Remote Sensing Letters 9, 564–568. doi: `10.1109/LGRS. 2011.2174772` . 

- Knipling, E.B., 1970. Physical and physiological basis for the reflectance of visible and near-infrared radiation from vegetation. Remote sensing of environment 1, 155–159. 

- Kochkov, D., Yuval, J., Langmore, I., Norgaard, P., Smith, J., Mooers, G., Klöwer, M., Lottes, J., Rasp, S., Düben, P., et al., 2024. Neural general circulation models for weather and climate. Nature 632, 1060–1066. 

- Kondylatos, S., Prapas, I., Camps-Valls, G., Papoutsis, I., 2023. Mesogeos: A multi-purpose dataset for data-driven wildfire modeling in the mediterranean, in: Thirty-seventh Conference on Neural Information Processing Systems Datasets and Benchmarks Track. URL: `https://openreview. net/forum?id=VH1vxapUTs` . 

- Kondylatos, S., Prapas, I., Ronco, M., Papoutsis, I., Camps-Valls, G., Piles, M., Fernández-Torres, M.A., Carvalhais, N., 2022. Wildfire Danger Prediction and Understanding With Deep Learning. Geophysical Research Letters 49, e2022GL099368. doi: `10.1029/2022GL099368` . _eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1029/2022GL099368. 

- Kozlowski, T.T., Kramer, P.J., Pallardy, S.G., 1990. The Physiological Ecology of Woody Plants. Academic Press. doi: `10.1093/treephys/8.2.213` . 

- Kramer, H.A., Collins, B.M., Kelly, M., Stephens, S.L., 2014. Quantifying ladder fuels: A new approach using lidar. Forests 5, 1432–1453. 

- Kriedemann, P.E., Barrs, H.D., 1983. Photosynthetic Adaptation to Water Stress and Implications for Drought Resistance, in: Crop Reactions To Water And Temperature Stresses In Humid, Temperate Climates. CRC Press. Num Pages: 30. 

- Krizhevsky, A., Sutskever, I., Hinton, G.E., 2012. Imagenet classification with deep convolutional neural networks. Advances in neural information processing systems 25. 

- Krueger, E.S., Levi, M.R., Achieng, K.O., Bolten, J.D., Carlson, J.D., Coops, N.C., Holden, Z.A., Magi, B.I., Rigden, A.J., Ochsner, T.E., 2022. Using soil moisture information to better understand and predict wildfire danger: a review of recent developments and outstanding questions. International Journal of Wildland Fire 32, 111–132. URL: `https://www.publish. csiro.au/wf/WF22056` , doi: `10.1071/WF22056` . publisher: CSIRO PUBLISHING. 

- Kurth, T., Subramanian, S., Harrington, P., Pathak, J., Mardani, M., Hall, D., Miele, A., Kashinath, K., Anandkumar, A., 2023. Fourcastnet: Accelerating global high-resolution weather forecasting using adaptive fourier neural operators, in: Proceedings of the Platform for Advanced Scien- 

51 

tific Computing Conference, Association for Computing Machinery, New York, NY, USA. URL: `https://doi.org/10.1145/3592979.3593412` , doi: `10.1145/3592979.3593412` . 

- Labenski, P., Ewald, M., Schmidtlein, S., Heinsch, F.A., Fassnacht, F.E., 2023. Quantifying surface fuels for fire modelling in temperate forests using airborne lidar and Sentinel-2: potential and limitations. Remote Sensing of Environment 295, 113711. URL: `https://www. sciencedirect.com/science/article/pii/S0034425723002626` , doi: `10.1016/j.rse.2023.113711` . 

- Lall, S., Mathibela, B., 2016. The application of artificial neural networks for wildfire risk prediction, in: 2016 International Conference on Robotics and Automation for Humanitarian Applications (RAHA), IEEE. pp. 1–6. 

- Lam, R., Sanchez-Gonzalez, A., Willson, M., Wirnsberger, P., Fortunato, M., Alet, F., Ravuri, S., Ewalds, T., Eaton-Rosen, Z., Hu, W., et al., 2023. Learning skillful medium-range global weather forecasting. Science 382, 1416– 1421. 

- Lang, S., Alexe, M., Chantry, M., Dramsch, J., Pinault, F., Raoult, B., Clare, M.C.A., Lessig, C., Maier-Gerber, M., Magnusson, L., Bouallègue, Z.B., Nemesio, A.P., Dueben, P.D., Brown, A., Pappenberger, F., Rabier, F., 2024. Aifs – ecmwf’s data-driven forecasting system. URL: `https://arxiv. org/abs/2406.01465` , `arXiv:2406.01465` . 

- Lecina-Diaz, J., Alvarez, A., Retana, J., 2014. Extreme Fire Severity Patterns in Topographic, Convective and Wind-Driven Historical Wildfires of Mediterranean Pine Forests. PLOS ONE 9, e85127. URL: `https://journals.plos.org/plosone/article? id=10.1371/journal.pone.0085127` , doi: `10.1371/journal.pone. 0085127` . publisher: Public Library of Science. 

- LeCun, Y., Bengio, Y., Hinton, G., 2015. Deep learning. nature 521, 436–444. Lee, S.J., Lee, Y.J., Ryu, J.Y., Kwon, C.G., Seo, K.W., Kim, S.Y., 2022. Prediction of wildfire fuel load for pinus densiflora stands in south korea based on the forest-growth model. Forests 13, 1372. 

- Leite, R.V., Amaral, C., Neigh, C.S., Cosenza, D.N., Klauberg, C., Hudak, A.T., Aragão, L., Morton, D.C., Coffield, S., McCabe, T., et al., 2024. Leveraging the next generation of spaceborne earth observations for fuel monitoring and wildland fire management. Remote Sensing in Ecology and Conservation . 

- Leite, R.V., Silva, C.A., Broadbent, E.N., Do Amaral, C.H., Liesenberg, V., De Almeida, D.R.A., Mohan, M., Godinho, S., Cardil, A., Hamamura, C., et al., 2022. Large scale multi-layer fuel load characterization in tropical savanna using gedi spaceborne lidar data. Remote Sensing of Environment 268, 112764. 

- Lelis, C.A.S., Roncal, J.J., Silveira, L., De Aquino, R.D.G., Marcondes, C.A.C., Marques, J., Loubach, D.S., Verri, F.A.N., Curtis, V.V., De Souza, D.G., 2024. Drone-based ai system for wildfire monitoring and risk prediction. IEEE Access 12, 139865–139882. doi: `10.1109/ACCESS.2024. 3462436` . 

- Leuenberger, M., Parente, J., Tonini, M., Pereira, M.G., Kanevski, M., 2018. Wildfire susceptibility mapping: Deterministic vs. stochastic approaches. Environmental Modelling & Software 101, 194–203. 

- Li, B.S., Rad, R., 2024. Wildfire spread prediction in north america using satellite imagery and vision transformer, in: 2024 IEEE Conference on Artificial Intelligence (CAI), IEEE. pp. 1536–1541. 

- Li, F., Zhang, H., Xu, H., Liu, S., Zhang, L., Ni, L.M., Shum, H.Y., 2023a. Mask dino: Towards a unified transformer-based framework for object detection and segmentation, in: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pp. 3041–3050. 

- Li, F., Zhu, Q., Riley, W.J., Zhao, L., Xu, L., Yuan, K., Chen, M., Wu, H., Gui, Z., Gong, J., et al., 2023b. Attentionfire_v1. 0: interpretable machine learning fire model for burned-area predictions over tropics. Geoscientific Model Development 16, 869–884. 

- Li, W., Xu, Q., Yi, J., Liu, J., 2022a. Predictive model of spatial scale of forest fire driving factors: a case study of Yunnan Province, China. Scientific Reports 12, 19029. doi: `10.1038/s41598-022-23697-6` . publisher: Nature Publishing Group. 

- Li, X., Wang, X., Sun, S., Wang, Y., Li, S., Li, D., 2023c. Predicting the wildland fire spread using a mixed-input cnn model with both channel and spatial attention mechanisms. Fire Technology 59, 2683–2717. 

- Li, Y., Chen, R., He, B., Veraverbeke, S., 2022b. Forest foliage fuel load estimation from multi-sensor spatiotemporal features. International Journal of Applied Earth Observation and Geoinformation 115, 103101. 

- URL: `https://www.sciencedirect.com/science/article/pii/ S1569843222002898` , doi: `10.1016/j.jag.2022.103101` . 

- Li, Y., He, B., Kong, P., Xu, H., Zhang, Q., Quan, X., 2021a. Estimation of forest surface dead fuel loads based on multi-source remote sensing data, in: 2021 IEEE International Geoscience and Remote Sensing Symposium IGARSS, pp. 6893–6896. doi: `10.1109/IGARSS47720.2021.9553105` . 

- Li, Y., Quan, X., Liao, Z., He, B., 2021b. Forest fuel loads estimation from landsat etm+ and alos palsar data. Remote Sensing 13, 1189. 

- Li, Z., Huang, Y., Li, X., Xu, L., 2021c. Wildland Fire Burned Areas Prediction Using Long Short-Term Memory Neural Network with Attention Mechanism. Fire Technology 57, 1–23. URL: `https://doi.org/10. 1007/s10694-020-01028-3` , doi: `10.1007/s10694-020-01028-3` . 

- Li, Z., Shi, H., Vogelmann, J.E., Hawbaker, T.J., Peterson, B., 2020. Assessment of fire fuel load dynamics in shrubland ecosystems in the western united states using modis products. Remote Sensing 12, 1911. 

- Liang, H., Zhang, M., Wang, H., 2019. A Neural Network Model for Wildfire Scale Prediction Using Meteorological Factors. IEEE Access 7, 176746– 176755. URL: `https://ieeexplore.ieee.org/document/8924693` , doi: `10.1109/ACCESS.2019.2957837` . conference Name: IEEE Access. 

- Liang, M., Duncanson, L., Silva, J.A., Sedano, F., 2023. Quantifying aboveground biomass dynamics from charcoal degradation in mozambique using gedi lidar and landsat. Remote sensing of environment 284, 113367. 

- Liao, D., Valliant, R., 2012. Variance inflation factors in the analysis of complex survey data. Survey Methodology 38, 53–62. 

- Lin, D., Giannico, V., Lafortezza, R., Sanesi, G., Elia, M., 2024. Use of airborne lidar to predict fine dead fuel load in mediterranean forest stands of southern europe. Fire Ecology 20, 58. 

- Liu, S., Zeng, Z., Ren, T., Li, F., Zhang, H., Yang, J., Li, C., Yang, J., Su, H., Zhu, J., et al., 2023. Grounding dino: Marrying dino with grounded pre-training for open-set object detection. arXiv preprint arXiv:2303.05499 

- Liu, X., Lin, Z., Feng, Z., 2021a. Short-term offshore wind speed forecast by seasonal arima-a comparison against gru and lstm. Energy 227, 120492. 

- Liu, Y., Stanturf, J., Goodrick, S., 2010. Wildfire potential evaluation during a drought event with a regional climate model and NDVI. Ecological Informatics 5, 418–428. URL: `https://www. sciencedirect.com/science/article/pii/S1574954110000531` , doi: `10.1016/j.ecoinf.2010.04.001` . 

- Liu, Z., Lin, Y., Cao, Y., Hu, H., Wei, Y., Zhang, Z., Lin, S., Guo, B., 2021b. Swin transformer: Hierarchical vision transformer using shifted windows, in: Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), pp. 10012–10022. 

- Lizundia-Loiola, J., Otón, G., Ramo, R., Chuvieco, E., 2020. A spatio-temporal active-fire clustering approach for global burned area mapping at 250 m from modis data. Remote Sensing of Environment 236, 111493. 

- Lopes Queiroz, G., McDermid, G.J., Linke, J., Hopkinson, C., Kariyeva, J., 2020. Estimating coarse woody debris volume using image analysis and multispectral lidar. Forests 11, 141. 

- Lopez, A.M., Avila, C.C.E., VanderRoest, J.P., Roth, H.K., Fendorf, S., Borch, T., 2024. Molecular insights and impacts of wildfire-induced soil chemical changes. Nature Reviews Earth & Environment , 1–16. 

- Lu, Y., Wei, C., 2021a. Evaluation of microwave soil moisture data for monitoring live fuel moisture content (lfmc) over the coterminous united states. Science of The Total Environment 771, 145410. 

- Lu, Y., Wei, C., 2021b. Evaluation of microwave soil moisture data for monitoring live fuel moisture content (LFMC) over the coterminous United States. Science of The Total Environment 771, 145410. URL: `https://www. sciencedirect.com/science/article/pii/S0048969721004782` , doi: `10.1016/j.scitotenv.2021.145410` . 

- Lundberg, S.M., Lee, S.I., 2017. A Unified Approach to Interpreting Model Predictions, in: Advances in Neural Information Processing Systems, Curran Associates, Inc. URL: `https://proceedings.neurips.cc/paper/ 2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html` . 

- Luo, L., Zhai, Q., Su, Y., Ma, Q., Kelly, M., Guo, Q., 2018. Simple method for direct crown base height estimation of individual conifer trees using airborne lidar data. Optics express 26, A562–A578. 

- Malik, A., Rao, M.R., Puppala, N., Koouri, P., Thota, V.A.K., Liu, Q., Chiao, S., Gao, J., 2021. Data-Driven Wildfire Risk Prediction in Northern California. Atmosphere 12, 109. URL: `https://www.mdpi.com/20734433/12/1/109` , doi: `10.3390/atmos12010109` . number: 1 Publisher: Multidisciplinary Digital Publishing Institute. 

- Mansuy, N., Miller, C., Parisien, M.A., Parks, S.A., Batllori, E., Moritz, M.A., 2019. Contrasting human influences and macro-environmental factors on 

52 

fire activity inside and outside protected areas of North America. Environmental Research Letters 14, 064007. URL: `https://dx.doi.org/ 10.1088/1748-9326/ab1bc5` , doi: `10.1088/1748-9326/ab1bc5` . publisher: IOP Publishing. 

- Marcozzi, A.A., Johnson, J.V., Parsons, R.A., Flanary, S.J., Seielstad, C.A., Downs, J.Z., 2023. Application of lidar derived fuel cells to wildfire modeling at laboratory scale. Fire 6, 394. 

- Marino, E., Yebra, M., Guillén-Climent, M., Algeet, N., Tomé, J.L., Madrigal, J., Guijarro, M., Hernando, C., 2020. Investigating live fuel moisture content estimation in fire-prone shrubland from remote sensing using empirical modelling and rtm simulations. Remote Sensing 12, 2251. 

- Marjani, M., Ahmadi, S.A., Mahdianpari, M., 2023. Firepred: A hybrid multitemporal convolutional neural network model for wildfire spread prediction. Ecological Informatics 78, 102282. 

- Marjani, M., Mahdianpari, M., Ahmadi, S.A., Hemmati, E., Mohammadimanesh, F., Mesgari, M.S., 2024a. Application of explainable artificial intelligence in predicting wildfire spread: an aspp-enabled cnn approach. IEEE Geoscience and Remote Sensing Letters . 

- Marjani, M., Mahdianpari, M., Mohammadimanesh, F., 2024b. Cnn-bilstm: A novel deep learning model for near-real-time daily wildfire spread prediction. Remote Sensing 16, 1467. 

- Marris, E., 2023. Hawaii wildfires: did scientists expect maui to burn? Nature 

- Martell, D.L., Bevilacqua, E., Stocks, B.J., 1989. Modelling seasonal variation in daily people-caused forest fire occurrence. Canadian Journal of Forest Research 19, 1555–1563. URL: `https://cdnsciencepub.com/doi/10. 1139/x89-237` , doi: `10.1139/x89-237` . publisher: NRC Research Press. 

- Martínez, J., Vega-Garcia, C., Chuvieco, E., 2009. Human-caused wildfire risk rating for prevention planning in Spain. Journal of Environmental Management 90, 1241–1252. URL: `https://www. sciencedirect.com/science/article/pii/S0301479708001758` , doi: `10.1016/j.jenvman.2008.07.005` . 

- Masrur, A., Yu, M., 2023. Chapter 6 - spatiotemporal attention convlstm networks for predicting and physically interpreting wildfire spread, in: Sun, Z., Cristea, N., Rivas, P. (Eds.), Artificial Intelligence in Earth Science. Elsevier, pp. 119–156. URL: `https://www.sciencedirect.com/ science/article/pii/B9780323917377000098` , doi: `https://doi. org/10.1016/B978-0-323-91737-7.00009-8` . 

- Masrur, A., Yu, M., Taylor, A., 2024. Capturing and interpreting wildfire spread dynamics: attention-based spatiotemporal models using convlstm networks. Ecological Informatics 82, 102760. 

- Matthews, E., 1997. Global litter production, pools, and turnover times: Estimates from measurement data and regression models. Journal of Geophysical Research: Atmospheres 102, 18771–18800. 

- Matthews, S., 2013. Dead fuel moisture research: 1991–2012. International journal of wildland fire 23, 78–92. 

- Mbow, C., Goı<sup>¨</sup> ta, K., Bénié, G.B., 2004. Spectral indices and fire behavior simulation for fire risk assessment in savanna ecosystems. Remote Sensing of Environment 91, 1–13. doi: `10.1016/j.rse.2003.10.019` . 

- McArthur, A.G., 1958. The preparation and use of fire danger tables. Technical Report. Forestry and Timber Bureau: Canberra, Australia. 

- McArthur, A.G., 1966. Weather and grassland fire behaviour. Technical Report. Department of National Development, Forestry and Timber Bureau: Canberra, Australia. 

- McCandless, T.C., Kosovic, B., Petzke, W., 2020. Enhancing wildfire spread modelling by building a gridded fuel moisture content product with machine learning. Machine Learning: Science and Technology 1, 035010. 

- McLauchlan, K.K., Higuera, P.E., Miesel, J., Rogers, B.M., Schweitzer, J., Shuman, J.K., Tepley, A.J., Varner, J.M., Veblen, T.T., Adalsteinsson, S.A., et al., 2020. Fire as a fundamental ecological process: Research advances and frontiers. Journal of Ecology 108, 2047–2069. 

- McNorton, J.R., Di Giuseppe, F., 2024. A global fuel characteristic model and dataset for wildfire prediction. Biogeosciences 21, 279–300. doi: `10.5194/ bg-21-279-2024` . publisher: Copernicus GmbH. 

- Meikle, S., Heine, J., 1987. A fire danger index system for the transvaal lowveld and adjoining escarpment areas. South African Forestry Journal 143, 55–56. 

- Mell, W., Jenkins, M.A., Gould, J., Cheney, P., 2007. A physics-based approach to modelling grassland fires. International Journal of Wildland Fire 16, 1–22. URL: `https://www.publish.csiro.au/wf/WF06002` , doi: `10.1071/WF06002` . publisher: CSIRO PUBLISHING. 

- Menning, K.M., Stephens, S.L., 2007. Fire climbing in the forest: a semiqual- 

itative, semiquantitative approach to assessing ladder fuel hazards. Western Journal of Applied Forestry 22, 88–93. 

- Meyer, F.J., 2019. Chapter 2 spaceborne synthetic aperture radar : Principles , data access , and basic processing techniques. URL: `https: //api.semanticscholar.org/CorpusID:201649124` . 

- Miao, X., Li, J., Mu, Y., He, C., Ma, Y., Chen, J., Wei, W., Gao, D., 2023. Time Series Forest Fire Prediction Based on Improved Transformer. Forests 14, 1596. URL: `https://www.mdpi.com/1999-4907/14/8/1596` , doi: `10. 3390/f14081596` . number: 8 Publisher: Multidisciplinary Digital Publishing Institute. 

- Michail, D., Panagiotou, L.I., Davalas, C., Prapas, I., Kondylatos, S., Bountos, N.I., Papoutsis, I., 2024. Seasonal Fire Prediction using Spatio-Temporal Deep Neural Networks. URL: `http://arxiv.org/abs/2404.06437` . arXiv:2404.06437 [cs]. 

- Millard, K., Thompson, D.K., Parisien, M.A., Richardson, M., 2018. Soil moisture monitoring in a temperate peatland using multi-sensor remote sensing and linear mixed effects. Remote Sensing 10, 903. 

- Miller, C., Ager, A.A., 2012. A review of recent advances in risk analysis for wildfire management. International journal of wildland fire 22, 1–14. 

- Miller, C., Parisien, M.A., Ager, A., Finney, M., 2008. Evaluating spatiallyexplicit burn probabilities for strategic fire management planning. WIT Transactions on Ecology and the Environment 119, 245–252. 

- Miller, L., Zhu, L., Yebra, M., Rüdiger, C., Webb, G.I., 2023. Projecting live fuel moisture content via deep learning. International Journal of Wildland Fire 32, 709–727. URL: `https://www.publish.csiro.au/wf/ WF22188` , doi: `10.1071/WF22188` . publisher: CSIRO PUBLISHING. 

- Moayedi, H., Khasmakhi, M.A.S.A., 2023. Wildfire susceptibility mapping using two empowered machine learning algorithms. Stochastic Environmental Research and Risk Assessment 37, 49–72. 

- Molnar, C., König, G., Herbinger, J., Freiesleben, T., Dandl, S., Scholbeck, C.A., Casalicchio, G., Grosse-Wentrup, M., Bischl, B., 2020. General pitfalls of model-agnostic interpretation methods for machine learning models, in: International Workshop on Extending Explainable AI Beyond Deep Models and Classifiers, Springer. pp. 39–68. 

- Moritz, M.A., Batllori, E., Bradstock, R.A., Gill, A.M., Handmer, J., Hessburg, P.F., Leonard, J., McCaffrey, S., Odion, D.C., Schoennagel, T., et al., 2014. Learning to coexist with wildfire. Nature 515, 58–66. 

- Mou, L., Hua, Y., Jin, P., Zhu, X.X., 2020. Era: A data set and deep learning benchmark for event recognition in aerial videos [software and data sets]. IEEE Geoscience and Remote Sensing Magazine 8, 125–133. 

- Moumgiakmas, S.S., Samatas, G.G., Papakostas, G.A., 2021. Computer vision for fire detection on uavs—from software to hardware. Future Internet 13, 200. 

- Mulverhill, C., Coops, N.C., Boulanger, Y., Hoffman, K.M., Cardinal Christianson, A., Daniels, L.D., Flamand-Hubert, M., Wotherspoon, A.R., Achim, A., 2024. Wildfires are spreading fast in canada—we must strengthen forests for the future. Nature 633, 282–285. 

- Myoung, B., Kim, S.H., Nghiem, S.V., Jia, S., Whitney, K., Kafatos, M.C., 2018. Estimating live fuel moisture from modis satellite data for wildfire danger assessment in southern california usa. Remote Sensing 10, 87. 

- Myroniuk, V., Zibtsev, S., Bogomolov, V., Goldammer, J.G., Soshenskyi, O., Levchenko, V., Matsala, M., 2023. Combining landsat time series and gedi data for improved characterization of fuel types and canopy metrics in wildfire simulation. Journal of Environmental Management 345, 118736. 

- Naderpour, M., Rizeei, H.M., Ramezani, F., 2020. Wildfire Prediction: Handling Uncertainties Using Integrated Bayesian Networks and Fuzzy Logic, in: 2020 IEEE International Conference on Fuzzy Systems (FUZZ-IEEE), pp. 1–7. URL: `https://ieeexplore.ieee.org/document/9177700` , doi: `10.1109/FUZZ48607.2020.9177700` . iSSN: 1558-4739. 

- Nami, M.H., Jaafari, A., Fallah, M., Nabiuni, S., 2018. Spatial prediction of wildfire probability in the Hyrcanian ecoregion using evidential belief function model and GIS. International Journal of Environmental Science and Technology 15, 373–384. URL: `https://doi.org/10.1007/s13762017-1371-6` , doi: `10.1007/s13762-017-1371-6` . 

- Nasir, N., Kansal, A., Barneih, F., Al-Shaltone, O., Bonny, T., Al-Shabi, M., Al Shammaa, A., 2023. Multi-modal image classification of covid-19 cases using computed tomography and x-rays scans. Intelligent Systems with Applications 17, 200160. 

- Natekar, S., Patil, S., Nair, A., Roychowdhury, S., 2021. Forest fire prediction using lstm, in: 2021 2nd International Conference for Emerging Technology (INCET), pp. 1–5. doi: `10.1109/INCET51464.2021.9456113` . 

53 

Nelson Jr, R.M., 2000. Prediction of diurnal change in 10-h fuel stick moisture content. Canadian Journal of Forest Research 30, 1071– 1087. URL: `https://cdnsciencepub.com/doi/abs/10.1139/x00032` , doi: `10.1139/x00-032` . publisher: NRC Research Press. 

- Nieto, H., Aguado, I., Chuvieco, E., Sandholt, I., 2010. Dead fuel moisture estimation with msg–seviri data. retrieval of meteorological data for the calculation of the equilibrium moisture content. Agricultural and Forest Meteorology 150, 861–870. 

- Nolan, R.H., de Dios, V.R., Boer, M.M., Caccamo, G., Goulden, M.L., Bradstock, R.A., 2016. Predicting dead fine fuel moisture at regional scales using vapour pressure deficit from modis and gridded weather data. Remote Sensing of Environment 174, 100–108. 

- Nolan, R.H., Price, O.F., Samson, S.A., Jenkins, M.E., Rahmani, S., Boer, M.M., 2022. Framework for assessing live fine fuel loads and biomass consumption during fire. Forest Ecology and Management 504, 119830. 

- Nur, A.S., Kim, Y.J., Lee, C.W., 2022. Creation of wildfire susceptibility maps in plumas national forest using insar coherence, deep learning, and metaheuristic optimization approaches. Remote Sensing 14, 4416. 

- Nur, A.S., Kim, Y.J., Lee, J.H., Lee, C.W., 2023. Spatial Prediction of Wildfire Susceptibility Using Hybrid Machine Learning Models Based on Support Vector Regression in Sydney, Australia. Remote Sensing 15, 760. URL: `https://www.mdpi.com/2072-4292/15/3/760` , doi: `10. 3390/rs15030760` . number: 3 Publisher: Multidisciplinary Digital Publishing Institute. 

- Oak, O., Nazre, R., Naigaonkar, S., Sawant, S., Joshi, A., 2024. A novel transfer learning based cnn model for wildfire susceptibility prediction, in: 2024 5th International Conference for Emerging Technology (INCET), IEEE. pp. 1– 6. 

- Oliveira, S., Gonçalves, A., Zêzere, J.L., 2021a. Reassessing wildfire susceptibility and hazard for mainland portugal. Science of the total environment 762, 143121. 

- Oliveira, S., Rocha, J., Sá, A., 2021b. Wildfire risk modeling. Current Opinion in Environmental Science & Health 23, 100274. URL: `https://www. sciencedirect.com/science/article/pii/S2468584421000465` , doi: `10.1016/j.coesh.2021.100274` . 

- de Oliveira-Júnior, J.F., Mendes, D., Szabo, S., Singh, S.K., Jamjareegulgarn, P., Cardoso, K.R.A., Bertalan, L., da Silva, M.V., da Rosa Ferraz Jardim, A.M., da Silva, J.L.B., et al., 2024. Impact of the el niño on fire dynamics on the african continent. Earth Systems and Environment 8, 45–61. 

- Oquab, M., Darcet, T., Moutakanni, T., Vo, H., Szafraniec, M., Khalidov, V., Fernandez, P., Haziza, D., Massa, F., El-Nouby, A., Assran, M., Ballas, N., Galuba, W., Howes, R., Huang, P.Y., Li, S.W., Misra, I., Rabbat, M., Sharma, V., Synnaeve, G., Xu, H., Jegou, H., Mairal, J., Labatut, P., Joulin, A., Bojanowski, P., 2024. Dinov2: Learning robust visual features without supervision. URL: `https://arxiv.org/abs/2304.07193` , `arXiv:2304.07193` . 

- Ottmar, R.D., Sandberg, D.V., Riccardi, C.L., Prichard, S.J., 2007. An overview of the fuel characteristic classification system—quantifying, classifying, and creating fuelbeds for resource planning. Canadian Journal of Forest Research 37, 2383–2393. 

- Parks, S.A., Abatzoglou, J.T., 2020. Warmer and Drier Fire Seasons Contribute to Increases in Area Burned at High Severity in Western US Forests From 1985 to 2017. Geophysical Research Letters 47, e2020GL089858. URL: `https://onlinelibrary.wiley. com/doi/abs/10.1029/2020GL089858` , doi: `10.1029/2020GL089858` . _eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1029/2020GL089858. 

- Pausas, J.G., Keeley, J.E., 2019. Wildfires as an ecosystem service. Frontiers in Ecology and the Environment 17, 289–295. 

- Pelletier, N., Millard, K., Darling, S., 2023. Wildfire likelihood in Canadian treed peatlands based on remote-sensing time-series of surface conditions. Remote Sensing of Environment 296, 113747. URL: `https://www. sciencedirect.com/science/article/pii/S0034425723002985` , doi: `10.1016/j.rse.2023.113747` . 

- Pellizzaro, G., Duce, P., Ventura, A., Zara, P., 2007. Seasonal variations of live moisture content and ignitability in shrubs of the mediterranean basin. International Journal of Wildland Fire 16, 633–641. 

- Peterson, S.H., Roberts, D.A., Dennison, P.E., 2008. Mapping live fuel moisture with modis data: A multiple regression approach. Remote Sensing of Environment 112, 4272–4284. 

- Phelps, N., Woolford, D.G., 2021a. Comparing calibrated statistical and machine learning methods for wildland fire occurrence prediction: a case study 

of human-caused fires in Lac La Biche, Alberta, Canada. International Journal of Wildland Fire 30, 850–870. URL: `https://www.publish.csiro. au/wf/WF20139` , doi: `10.1071/WF20139` . publisher: CSIRO PUBLISHING. 

- Phelps, N., Woolford, D.G., 2021b. Guidelines for effective evaluation and comparison of wildland fire occurrence prediction models. International journal of wildland fire 30, 225–240. 

- Pisek, J., Rautiainen, M., Nikopensius, M., Raabe, K., 2015. Estimation of seasonal dynamics of understory NDVI in northern forests using MODIS BRDF data: Semi-empirical versus physically-based approach. Remote Sensing of Environment 163, 42–47. URL: `https://www. sciencedirect.com/science/article/pii/S0034425715000991` , doi: `10.1016/j.rse.2015.03.003` . 

- Ploton, P., Mortier, F., Réjou-Méchain, M., Barbier, N., Picard, N., Rossi, V., Dormann, C., Cornu, G., Viennois, G., Bayol, N., et al., 2020. Spatial validation reveals poor predictive performance of large-scale ecological mapping models. Nature communications 11, 4540. 

- Polivka, T.N., Wang, J., Ellison, L.T., Hyer, E.J., Ichoku, C.M., 2016. Improving nocturnal fire detection with the viirs day–night band. IEEE Transactions on Geoscience and Remote Sensing 54, 5503–5519. doi: `10.1109/TGRS. 2016.2566665` . 

- Pollina, J.B., Colle, B.A., Charney, J.J., 2013. Climatology and Meteorological Evolution of Major Wildfire Events over the Northeast United States. Weather and Forecasting 28, 175–193. URL: `https://journals. ametsoc.org/view/journals/wefo/28/1/waf-d-12-00009_1.xml` , doi: `10.1175/WAF-D-12-00009.1` . publisher: American Meteorological Society Section: Weather and Forecasting. 

- Ponomarev, E.I., Zabrodin, A.N., Shvetsov, E.G., Ponomareva, T.V., 2023. Wildfire intensity and fire emissions in siberia. Fire 6, 246. 

- Prapas, I., Bountos, N.I., Kondylatos, S., Michail, D., Camps-Valls, G., Papoutsis, I., 2023. TeleViT: Teleconnection-Driven Transformers Improve Subseasonal to Seasonal Wildfire Forecasting, pp. 3754–3759. URL: `https://openaccess.thecvf.com/content/ ICCV2023W/AIHADR/html/Prapas_TeleViT_TeleconnectionDriven_Transformers_Improve_Subseasonal_to_Seasonal_ Wildfire_Forecasting_ICCVW_2023_paper.html` . 

- Prapas, I., Kondylatos, S., Papoutsis, I., 2022. FireCube: A Daily Datacube for the Modeling and Analysis of Wildfires in Greece. URL: `https://doi. org/10.5281/zenodo.6475592` , doi: `10.5281/zenodo.6475592` . 

- Prapas, I., Kondylatos, S., Papoutsis, I., Camps-Valls, G., Ronco, M., Ángel Fernández-Torres, M., Guillem, M.P., Carvalhais, N., 2021. Deep learning methods for daily wildfire danger forecasting. URL: `https://arxiv. org/abs/2111.02736` , `arXiv:2111.02736` . 

- Preisler, H.K., Brillinger, D.R., Burgan, R.E., Benoit, J., 2004. Probability based models for estimation of wildfire risk. International Journal of wildland fire 13, 133–142. 

- Price, I., Sanchez-Gonzalez, A., Alet, F., Andersson, T.R., El-Kadi, A., Masters, D., Ewalds, T., Stott, J., Mohamed, S., Battaglia, P., et al., 2025. Probabilistic weather forecasting with machine learning. Nature 637, 84–90. 

- Prior, T., Eriksen, C., 2013. Wildfire preparedness, community cohesion and social–ecological systems. Global Environmental Change 23, 1575– 1586. URL: `https://www.sciencedirect.com/science/article/ pii/S0959378013001684` , doi: `10.1016/j.gloenvcha.2013.09.016` . 

- Pye, J.M., Prestemon, J.P., Butry, D.T., Abt, K.L., 2003. Prescribed burning and wildfire risk in the 1998 fire season in florida, in: In: Omi, Philip N.; Joyce, Linda A., technical editors. Fire, fuel treatments, and ecological restoration: Conference proceedings; 2002 16-18 April; Fort Collins, CO. Proceedings RMRS-P-29. Fort Collins, CO: US Department of Agriculture, Forest Service, Rocky Mountain Research Station. p. 15-26, pp. 15–26. 

- Qadir, A., Talukdar, N.R., Uddin, M.M., Ahmad, F., Goparaju, L., 2021. Predicting forest fire using multispectral satellite measurements in Nepal. Remote Sensing Applications: Society and Environment 23, 100539. URL: `https://www.sciencedirect.com/ science/article/pii/S2352938521000756` , doi: `10.1016/j.rsase. 2021.100539` . 

- Quan, X., Wang, W., Xie, Q., He, B., Resco De Dios, V., Yebra, M., Jiao, M., Chen, R., 2023. Improving wildfire occurrence modelling by integrating time-series features of weather and fuel moisture content. Environmental Modelling & Software 170, 105840. doi: `10.1016/j.envsoft.2023. 105840` . 

- Quan, X., Yebra, M., Riaño, D., He, B., Lai, G., Liu, X., 2021a. Global fuel 

54 

moisture content mapping from modis. International Journal of Applied Earth Observation and Geoinformation 101, 102354. 

- Quan, X., Yebra, M., Riaño, D., He, B., Lai, G., Liu, X., 2021b. Global fuel moisture content mapping from MODIS. International Journal of Applied Earth Observation and Geoinformation 101, 102354. URL: `https://www. sciencedirect.com/science/article/pii/S0303243421000611` , doi: `10.1016/j.jag.2021.102354` . 

- Rabier, F., 2005. Overview of global data assimilation developments in numerical weather-prediction centres. Quarterly Journal of the Royal Meteorological Society: A journal of the atmospheric sciences, applied meteorology and physical oceanography 131, 3215–3233. 

- Rahimzadeh-Bajgiran, P., Omasa, K., Shimizu, Y., 2012. Comparative evaluation of the vegetation dryness index (vdi), the temperature vegetation dryness index (tvdi) and the improved tvdi (itvdi) for water stress detection in semi-arid regions of iran. ISPRS Journal of Photogrammetry and Remote Sensing 68, 1–12. 

- Rakhmatulina, E., Stephens, S., Thompson, S., 2021. Soil moisture influences on sierra nevada dead fuel moisture content and fire risks. Forest Ecology and Management 496, 119379. 

- Rao, K., Williams, A.P., Flefil, J.F., Konings, A.G., 2020a. Sar-enhanced mapping of live fuel moisture content. Remote Sensing of Environment 245, 111797. 

- Rao, K., Williams, A.P., Flefil, J.F., Konings, A.G., 2020b. SARenhanced mapping of live fuel moisture content. Remote Sensing of Environment 245, 111797. URL: `https://www. sciencedirect.com/science/article/pii/S003442572030167X` , doi: `10.1016/j.rse.2020.111797` . 

- Rashkovetsky, D., Mauracher, F., Langer, M., Schmitt, M., 2021. Wildfire detection from multisensor satellite imagery using deep semantic segmentation. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing 14, 7001–7016. doi: `10.1109/JSTARS.2021.3093625` . 

- Ray, D., Nepstad, D., Brando, P., 2010. Predicting moisture dynamics of fine understory fuels in a moist tropical rainforest system: results of a pilot study undertaken to identify proxy variables useful for rating fire danger. New Phytologist 187, 720–732. 

- Razavi Termeh, S.V., Kornejady, A., Pourghasemi, H.R., Keesstra, S., 2018. Flood susceptibility mapping using novel ensembles of adaptive neuro fuzzy inference system and metaheuristic algorithms. Science of The Total Environment 615, 438–451. URL: `https://www. sciencedirect.com/science/article/pii/S0048969717326141` , doi: `10.1016/j.scitotenv.2017.09.262` . 

- Rezaie, F., Panahi, M., Bateni, S.M., Lee, S., Jun, C., Trauernicht, C., Neale, C.M.U., 2023. Development of novel optimized deep learning algorithms for wildfire modeling: A case study of Maui, Hawai‘i. Engineering Applications of Artificial Intelligence 125, 106699. URL: `https://www.sciencedirect.com/science/ article/pii/S0952197623008837` , doi: `10.1016/j.engappai.2023. 106699` . 

- Ritter, S.M., Hoffman, C.M., Battaglia, M.A., Linn, R., Mell, W.E., 2023. Vertical and horizontal crown fuel continuity influences group-scale ignition and fuel consumption. Fire 6, 321. 

- Rodriguez-Jimenez, F., Lorenzo, H., Novo, A., Acuña-Alonso, C., Alvarez, X., 2023. Modelling of live fuel moisture content in different vegetation scenarios during dry periods using meteorological data and spectral indices. Forest Ecology and Management 546, 121378. 

- Rogger, M., Agnoletti, M., Alaoui, A., Bathurst, J., Bodner, G., Borga, M., Chaplot, V., Gallart, F., Glatzel, G., Hall, J., et al., 2017. Land use change impacts on floods at the catchment scale: Challenges and opportunities for future research. Water resources research 53, 5209–5219. 

- Romero-Calcerrada, R., Novillo, C., Millington, J.D., Gomez-Jimenez, I., 2008. Gis analysis of spatial patterns of human-caused wildfire ignition risk in the sw of madrid (central spain). Landscape ecology 23, 341–354. 

- Rösch, M., Nolde, M., Ullmann, T., Riedlinger, T., 2024. Data-driven wildfire spread modeling of european wildfires using a spatiotemporal graph neural network. Fire 7, 207. 

- Rothermel, R.C., 1972. A Mathematical Model for Predicting Fire Spread in Wildland Fuels. Research Paper. Intermountain Forest & Range Experiment Station, Forest Service, US Department of Agriculture. Ogden, UT, USA. 

- Rothermel, R.C., Wilson, R., Morris, G.A., Sackett, S.S., 1986. Modeling Moisture Content of Fine Dead Wildland Fuels:. United States Department of Agriculture, Forest Service, Intermountain .... 

- Roy, S.K., Deria, A., Hong, D., Rasti, B., Plaza, A., Chanussot, J., 2023. Multimodal fusion transformer for remote sensing image classification. IEEE Transactions on Geoscience and Remote Sensing 61, 1–20. doi: `10.1109/ TGRS.2023.3286826` . 

- Rubí, J.N.S., Gondim, P.R.L., 2023. A performance comparison of machine learning models for wildfire occurrence risk prediction in the Brazilian Federal District region. Environment Systems and Decisions URL: `https://doi.org/10.1007/s10669-023-09921-2` , doi: `10.1007/s10669-023-09921-2` . 

- Ruffault, J., Martin-StPaul, N., Pimont, F., Dupuy, J.L., 2018. How well do meteorological drought indices predict live fuel moisture content (lfmc)? an assessment for wildfire research and operations in mediterranean ecosystems. Agricultural and Forest Meteorology 262, 391–401. 

- Saatchi, S., Halligan, K., Despain, D.G., Crabtree, R.L., 2007. Estimation of Forest Fuel Load From Radar Remote Sensing. IEEE Transactions on Geoscience and Remote Sensing 45, 1726–1740. URL: `https:// ieeexplore.ieee.org/abstract/document/4215087` , doi: `10.1109/ TGRS.2006.887002` . conference Name: IEEE Transactions on Geoscience and Remote Sensing. 

- Sadasivuni, R., Cooke, W.H., Bhushan, S., 2013. Wildfire risk prediction in Southeastern Mississippi using population interaction. Ecological Modelling 251, 297–306. URL: `https://www. sciencedirect.com/science/article/pii/S0304380013000070` , doi: `10.1016/j.ecolmodel.2012.12.024` . 

- Salih, A.M., Raisi-Estabragh, Z., Galazzo, I.B., Radeva, P., Petersen, S.E., Lekadir, K., Menegaz, G., 2024. A perspective on explainable artificial intelligence methods: Shap and lime. Advanced Intelligent Systems , 2400304. 

- Salis, M., Arca, B., Del Giudice, L., Palaiologou, P., Alcasena-Urdiroz, F., Ager, A., Fiori, M., Pellizzaro, G., Scarpa, C., Schirru, M., Ventura, A., Casula, M., Duce, P., 2021. Application of simulation modeling for wildfire exposure and transmission assessment in Sardinia, Italy. International Journal of Disaster Risk Reduction 58, 102189. URL: `https://linkinghub. elsevier.com/retrieve/pii/S2212420921001552` , doi: `10.1016/j. ijdrr.2021.102189` . 

- Santopaolo, A., Saif, S.S., Pietrabissa, A., Giuseppi, A., 2021. Forest fire risk prediction from satellite data with convolutional neural networks, in: 2021 29th Mediterranean Conference on Control and Automation (MED), IEEE. pp. 360–367. 

- Sayad, Y.O., Mousannif, H., Al Moatassime, H., 2019. Predictive modeling of wildfires: A new dataset and machine learning approach. Fire safety journal 104, 130–146. 

- Scheller, R.M., Domingo, J.B., Sturtevant, B.R., Williams, J.S., Rudy, A., Gustafson, E.J., Mladenoff, D.J., 2007. Design, development, and application of landis-ii, a spatial landscape simulation model with flexible temporal and spatial resolution. ecological modelling 201, 409–419. 

- Schroeder, M.J., Buck, C.C., 1977. Fire weather: A guide for application of meteorological information to forest fire control operations. US Forest Service. 

- Schroeder, W., Oliva, P., Giglio, L., Csiszar, I.A., 2014. The new viirs 375 m active fire detection data product: Algorithm description and initial assessment. Remote Sensing of Environment 143, 85–96. 

- Scott, J.H., 2001. Assessing crown fire potential by linking models of surface and crown fire behavior. 29, US Department of Agriculture, Forest Service, Rocky Mountain Research Station. 

- Senawi, A., Wei, H.L., Billings, S.A., 2017. A new maximum relevanceminimum multicollinearity (mrmmc) method for feature selection and ranking. Pattern Recognition 67, 47–61. 

- Shadrin, D., Illarionova, S., Gubanov, F., Evteeva, K., Mironenko, M., Levchunets, I., Belousov, R., Burnaev, E., 2024. Wildfire spreading prediction using multimodal data and deep neural network approach. Scientific Reports 14, 2606. URL: `https://www.ncbi.nlm.nih.gov/pmc/ articles/PMC10831103/` , doi: `10.1038/s41598-024-52821-x` . 

- Shah, N.A., VS, V., Patel, V.M., 2024. Lqmformer: Language-aware query mask transformer for referring image segmentation, in: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pp. 12903–12913. 

- Shamsoshoara, A., Afghah, F., Razi, A., Zheng, L., Fulé, P., Blasch, E., 2020. The flame dataset: Aerial imagery pile burn detection using drones (uavs). URL: `https://dx.doi.org/10.21227/qad6-r683` , doi: `10. 21227/qad6-r683` . 

Shapley, L.S., 1953. Stochastic games. Proceedings of the national academy of 

55 

sciences 39, 1095–1100. 

- Shi, J., Shirali, A., Jin, B., Zhou, S., Hu, W., Rangaraj, R., Wang, S., Han, J., Wang, Z., Lall, U., Wu, Y., Bobadilla, L., Narasimhan, G., 2025. Deep learning and foundation models for weather prediction: A survey. URL: `https://arxiv.org/abs/2501.06907` , `arXiv:2501.06907` . 

- Short, K.C., 2014. A spatial database of wildfires in the united states, 19922011. Earth System Science Data 6, 1–27. 

- Shvidenko, A., Shchepashchenko, D., Vaganov, E., Sukhinin, A., Maksyutov, S.S., McCallum, I., Lakyda, I., 2011. Impact of wildfire in russia between 1998–2010 on ecosystems and the global carbon budget, in: Doklady Earth Sciences, Springer. pp. 1678–1682. 

- Singla, S., Diao, T., Mukhopadhyay, A., Eldawy, A., Shachter, R., Kochenderfer, M., 2020. Wildfiredb: A spatio-temporal dataset combining wildfire occurrence with relevant covariates, in: 34th Conference on Neural Information Processing Systems (NeurIPS 2020). 

- Skowronski, N.S., Clark, K.L., Duveneck, M., Hom, J., 2011. Threedimensional canopy fuel loading predicted using upward and downward sensing LiDAR systems. Remote Sensing of Environment 115, 703– 714. URL: `https://www.sciencedirect.com/science/article/ pii/S0034425710003172` , doi: `10.1016/j.rse.2010.10.012` . 

- Song, Y., Wang, Y., 2020. Global Wildfire Outlook Forecast with Neural Networks. Remote Sensing 12, 2246. URL: `https://www.mdpi.com/20724292/12/14/2246` , doi: `10.3390/rs12142246` . number: 14 Publisher: Multidisciplinary Digital Publishing Institute. 

- Sow, M., Mbow, C., Hély, C., Fensholt, R., Sambou, B., 2013. Estimation of herbaceous fuel moisture content using vegetation indices and land surface temperature from modis data. Remote Sensing 5, 2617–2638. 

- Srivastava, S.K., Saran, S., de By, R.A., Dadhwal, V.K., 2014. A geo-information system approach for forest fire likelihood based on causative and anti-causative factors. International Journal of Geographical Information Science 28, 427–454. URL: `https://doi.org/10.1080/13658816.2013.797984` , doi: `10.1080/13658816.2013.797984` . publisher: Taylor & Francis 

- _eprint: https://doi.org/10.1080/13658816.2013.797984. 

- Stojanovic, D., nee Voogdt, J.W., Webb, M., Cook, H., Heinsohn, R., 2016. Loss of habitat for a secondary cavity nesting bird after wildfire. Forest Ecology and Management 360, 235–241. 

- Stow, D., Niphadkar, M., Kaiser, J., 2006. Time series of chaparral live fuel moisture maps derived from modis satellite data. International Journal of Wildland Fire 15, 347–360. 

- Su, Z., Zheng, L., Luo, S., Tigabu, M., Guo, F., 2021. Modeling wildfire drivers in Chinese tropical forest ecosystems using global logistic regression and geographically weighted logistic regression. Natural Hazards 108, 1317–1345. URL: `https://doi.org/10.1007/s11069-021-04733-6` , doi: `10.1007/s11069-021-04733-6` . 

- Sundararajan, M., Taly, A., Yan, Q., 2017. Axiomatic attribution for deep networks, in: International conference on machine learning, PMLR. pp. 3319– 3328. 

- Swetnam, T.W., Betancourt, J.L., 1990. Fire-southern oscillation relations in the southwestern united states. Science 249, 1017–1020. 

- Sønderby, C.K., Espeholt, L., Heek, J., Dehghani, M., Oliver, A., Salimans, T., Agrawal, S., Hickey, J., Kalchbrenner, N., 2020. Metnet: A neural weather model for precipitation forecasting. URL: `https://arxiv.org/ abs/2003.12140` , `arXiv:2003.12140` . 

- Tanase, M., Panciera, R., Lowell, K., Aponte, C., 2015. Monitoring live fuel moisture in semiarid environments using l-band radar data. International Journal of Wildland Fire 24, 560–572. 

- Tanase, M.A., Nova, J.P.G., Marino, E., Aponte, C., Tomé, J.L., Yáñez, L., Madrigal, J., Guijarro, M., Hernando, C., 2022. Characterizing live fuel moisture content from active and passive sensors in a mediterranean environment. Forests 13, 1846. 

- Taneja, R., Hilton, J., Wallace, L., Reinke, K., Jones, S., 2021. Effect of fuel spatial resolution on predictive wildfire models. International Journal of Wildland Fire 30, 776–789. URL: `https://www.publish.csiro.au/ wf/WF20192` , doi: `10.1071/WF20192` . publisher: CSIRO PUBLISHING. 

- Tariq, A., Shu, H., Li, Q., Altan, O., Khan, M.R., Baqa, M.F., Lu, L., 2021. Quantitative analysis of forest fires in southeastern australia using sar data. Remote Sensing 13, 2386. 

- Tavakkoli Piralilou, S., Einali, G., Ghorbanzadeh, O., Nachappa, T.G., Gholamnia, K., Blaschke, T., Ghamisi, P., 2022. A Google Earth Engine Approach for Wildfire Susceptibility Prediction Fusion with Remote Sens- 

ing Data of Different Spatial Resolutions. Remote Sensing 14, 672. URL: `https://www.mdpi.com/2072-4292/14/3/672` , doi: `10.3390/ rs14030672` . number: 3 Publisher: Multidisciplinary Digital Publishing Institute. 

- Tesch, T., Kollet, S., Garcke, J., 2023. Causal deep learning models for studying the earth system. Geoscientific Model Development 16, 2149–2166. 

- Thompson, M.P., Vaillant, N.M., Haas, J.R., Gebert, K.M., Stockmann, K.D., 2013. Quantifying the potential impacts of fuel treatments on wildfire suppression costs. Journal of Forestry 111, 49–58. 

- Tolhurst, K., Shields, B., Chong, D., 2008. Phoenix: development and application of a bushfire risk management tool. Australian Journal of Emergency Management, The 23, 47–54. 

- Toulouse, T., Rossi, L., Campana, A., Celik, T., Akhloufi, M.A., 2017. Computer vision for wildfire research: An evolving image dataset for processing and analysis. Fire Safety Journal 92, 188–194. 

- Tran, T.T.K., Bateni, S.M., Rezaie, F., Panahi, M., Jun, C., Trauernicht, C., Neale, C.M.U., 2023. Enhancing predictive ability of optimized group method of data handling (GMDH) method for wildfire susceptibility mapping. Agricultural and Forest Meteorology 339, 109587. URL: `https://www.sciencedirect.com/science/article/pii/ S0168192323002782` , doi: `10.1016/j.agrformet.2023.109587` . 

- Tran, T.T.K., Janizadeh, S., Bateni, S.M., Jun, C., Kim, D., Trauernicht, C., Rezaie, F., Giambelluca, T.W., Panahi, M., 2024. Improving the prediction of wildfire susceptibility on hawai’i island, hawai’i, using explainable hybrid machine learning models. Journal of environmental management 351, 119724. 

- Trucchia, A., Meschi, G., Fiorucci, P., Gollini, A., Negro, D., 2022. Defining Wildfire Susceptibility Maps in Italy for Understanding Seasonal Wildfire Regimes at the National Level. Fire 5, 30. URL: `https://www.mdpi.com/ 2571-6255/5/1/30` , doi: `10.3390/fire5010030` . number: 1 Publisher: Multidisciplinary Digital Publishing Institute. 

- Tucker, C.J., 1979. Red and photographic infrared linear combinations for monitoring vegetation. Remote Sensing of Environment 8, 127– 150. URL: `https://www.sciencedirect.com/science/article/ pii/0034425779900130` , doi: `10.1016/0034-4257(79)90013-0` . 

- Tymstra, C., Bryce, R., Wotton, B., Taylor, S., Armitage, O., et al., 2010. Development and structure of prometheus: the canadian wildland fire growth simulation model. Natural Resources Canada, Canadian Forest Service, Northern Forestry Centre, Information Report NOR-X-417.(Edmonton, AB) . 

- Ujjwal, K., Hilton, J., Garg, S., Aryal, J., 2022. A probability-based risk metric for operational wildfire risk management. Environmental Modelling & Software 148, 105286. 

- Umunnakwe, A., Parvania, M., Nguyen, H., Horel, J.D., Davis, K.R., 2022. Data-driven spatio-temporal analysis of wildfire risk to power systems operation. IET Generation, Transmission & Distribution 16, 2531–2546. 

- Ustin, S.L., Middleton, E.M., 2021. Current and near-term advances in earth observation for ecological applications. Ecological Processes 10, 1. 

- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, L., Polosukhin, I., 2017. Attention is all you need, in: Advances in Neural Information Processing Systems. 

- Vega, J.A., Arellano-Pérez, S., Álvarez-González, J.G., Fernández, C., Jiménez, E., Fernández-Alonso, J.M., Vega-Nieva, D.J., Briones-Herrera, C., Alonso-Rego, C., Fontúrbel, T., et al., 2022. Modelling aboveground biomass and fuel load components at stand level in shrub communities in nw spain. Forest Ecology and Management 505, 119926. 

- Verbesselt, J., Fleck, S., Coppin, P., Viegas, D., 2002. Estimation of fuel moisture content towards fire risk assessment: a review. URL: `https://www.semanticscholar.org/paper/Estimationof-fuel-moisture-content-towards-fire-a-VerbesseltFleck/5d7c76a2a1ee4ca7f5984be7a66866def092df59` . 

- Viegas, D., Piñol, J., Viegas, M., Ogaya, R., 2001. Estimating live fine fuels moisture content using meteorologically-based indices. International Journal of Wildland Fire 10, 223–240. 

- Vilar, L., Camia, A., San-Miguel-Ayanz, J., Martín, M.P., 2016. Modeling temporal changes in human-caused wildfires in mediterranean europe based on land use-land cover interfaces. Forest Ecology and Management 378, 68–78. 

- Viney, N.R., 1991. A review of fine fuel moisture modelling. International Journal of Wildland Fire 1, 215–234. 

- Vinodkumar, V., Dharssi, I., Yebra, M., Fox-Hughes, P., 2021a. Continentalscale prediction of live fuel moisture content using soil moisture 

56 

information. Agricultural and Forest Meteorology 307, 108503. URL: `https://www.sciencedirect.com/science/article/pii/ S0168192321001866` , doi: `https://doi.org/10.1016/j.agrformet. 2021.108503` . 

Vinodkumar, V., Dharssi, I., Yebra, M., Fox-Hughes, P., 2021b. Continentalscale prediction of live fuel moisture content using soil moisture information. Agricultural and Forest Meteorology 307, 108503. URL: `https://www.sciencedirect.com/science/article/pii/ S0168192321001866` , doi: `10.1016/j.agrformet.2021.108503` . 

- Vissio, G., Turco, M., Provenzale, A., 2023. Testing drought indicators for summer burned area prediction in Italy. Natural Hazards 116, 1125–1137. URL: `https://doi.org/10.1007/s11069-022-05714-z` , doi: `10.1007/s11069-022-05714-z` . 

- Viswanathan, S., Anand Kumar, M., Soman, K., 2019. A sequence-based machine comprehension modeling using lstm and gru, in: Emerging Research in Electronics, Computer Science and Technology: Proceedings of International Conference, ICERECT 2018, Springer. pp. 47–55. 

- Vitolo, C., Di Giuseppe, F., Barnard, C., Coughlan, R., San-Miguel-Ayanz, J., Libertá, G., Krzeminski, B., 2020. ERA5-based global meteorological wildfire danger maps. Scientific Data 7, 216. URL: `https://www. nature.com/articles/s41597-020-0554-z` , doi: `10.1038/s41597020-0554-z` . publisher: Nature Publishing Group. 

- Wagner, C.V., 1993. Prediction of crown fire behavior in two stands of jack pine. Canadian Journal of Forest Research 23, 442–449. 

- Walker, X.J., Rogers, B.M., Veraverbeke, S., Johnstone, J.F., Baltzer, J.L., Barrett, K., Bourgeau-Chavez, L., Day, N., de Groot, W., Dieleman, C., et al., 2020. Fuel availability not fire weather controls boreal wildfire severity and carbon emissions. Nature Climate Change 10, 1130–1136. 

- Wang, J., Ke, L., 2024. Llm-seg: Bridging image segmentation and large language model reasoning, in: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops, pp. 1765– 1774. 

- Wang, J., Roudini, S., Hyer, E.J., Xu, X., Zhou, M., Garcia, L.C., Reid, J.S., Peterson, D.A., da Silva, A.M., 2020. Detecting nighttime fire combustion phase by hybrid application of visible and infrared radiation from suomi npp viirs. Remote Sensing of Environment 237, 111466. URL: `https://www.sciencedirect.com/science/ article/pii/S0034425719304857` , doi: `https://doi.org/10.1016/ j.rse.2019.111466` . 

- Wang, L., Quan, X., He, B., Yebra, M., Xing, M., Liu, X., 2019. Assessment of the dual polarimetric sentinel-1a data for forest fuel moisture content estimation. Remote Sensing 11, 1568. 

- Wang, Q., Ihme, M., Gazen, C., Chen, Y.F., Anderson, J., 2024. Firebench: A high-fidelity ensemble simulation framework for exploring wildfire behavior and data-driven modeling. arXiv preprint arXiv:2406.08589 . 

- Wang, S.S.C., Qian, Y., Leung, L.R., Zhang, Y., 2021. Identifying Key Drivers of Wildfires in the Contiguous US Using Machine Learning and Game Theory Interpretation. Earth’s Future 9, e2020EF001910. URL: `https://onlinelibrary.wiley.com/doi/ abs/10.1029/2020EF001910` , doi: `10.1029/2020EF001910` . _eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1029/2020EF001910. 

- Wang, W., Quan, X., 2023. Estimation of live fuel moisture content from multiple sources of remotely sensed data. IEEE Geoscience and Remote Sensing Letters . 

- Wang, Y., Xi, X., Wang, C., Yang, X., Wang, P., Nie, S., Du, M., 2022a. A novel method based on kernel density for estimating crown base height using uavborne lidar data. IEEE Geoscience and Remote Sensing Letters 19, 1–5. doi: `10.1109/LGRS.2022.3171316` . 

- Wang, Z., Lu, Y., Li, Q., Tao, X., Guo, Y., Gong, M., Liu, T., 2022b. Cris: Clip-driven referring image segmentation, in: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pp. 11676–11685. doi: `10.1109/CVPR52688.2022.01139` . 

- Waqas, M., Humphries, U.W., Chueasa, B., Wangwongchai, A., 2024. Artificial intelligence and numerical weather prediction models: A technical survey. Natural Hazards Research . 

- Wing, B.M., Ritchie, M.W., Boston, K., Cohen, W.B., Gitelman, A., Olsen, M.J., 2012. Prediction of understory vegetation cover with airborne lidar in an interior ponderosa pine forest. Remote Sensing of Environment 124, 730–741. 

- Woodall, C., Walters, B., Oswalt, S., Domke, G., Toney, C., Gray, A., 2013. Biomass and carbon attributes of downed woody materials in forests of the 

united states. Forest Ecology and Management 305, 48–59. 

- Wu, J., Li, X., Li, X., Ding, H., Tong, Y., Tao, D., 2024. Toward robust referring image segmentation. IEEE Transactions on Image Processing 33, 1782– 1794. doi: `10.1109/TIP.2024.3371348` . 

- Xie, J., Qi, T., Hu, W., Huang, H., Chen, B., Zhang, J., 2022a. Retrieval of live fuel moisture content based on multi-source remote sensing data and ensemble deep learning model. Remote Sensing 14, 4378. 

- Xie, L., Zhang, R., Zhan, J., Li, S., Shama, A., Zhan, R., Wang, T., Lv, J., Bao, X., Wu, R., 2022b. Wildfire risk assessment in liangshan prefecture, china based on an integration machine learning algorithm. Remote Sensing 14, 4592. 

- Xu, P., Zhu, X., Clifton, D.A., 2023a. Multimodal learning with transformers: A survey. IEEE Transactions on Pattern Analysis and Machine Intelligence 45, 12113–12132. doi: `10.1109/TPAMI.2023.3275156` . 

- Xu, R., Yang, S., Wang, Y., Cai, Y., Du, B., Chen, H., 2024. Visual mamba: A survey and new outlooks. URL: `https://arxiv.org/abs/2404.18861` , `arXiv:2404.18861` . 

- Xu, W., Wooster, M.J., 2023. Sentinel-3 slstr active fire (af) detection and frp daytime product-algorithm description and global intercomparison to modis, viirs and landsat af data. Science of Remote Sensing 7, 100087. 

- Xu, Z., Chen, Z., Zhang, Y., Song, Y., Wan, X., Li, G., 2023b. Bridging vision and language encoders: Parameter-efficient tuning for referring image segmentation, in: Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), pp. 17503–17512. 

- Yahia, O., Ghabi, M., Karoui, M.S., 2023. The Prediction of Regional Wildfire Risk Using High-Resolution Remotely Sensed Soil Moisture Content Estimation, Case Study: Sidi Douma Forest, Saida, Algeria, in: IGARSS 2023 - 2023 IEEE International Geoscience and Remote Sensing Symposium, pp. 3387–3390. URL: `https://ieeexplore.ieee.org/abstract/document/10281986` , doi: `10.1109/IGARSS52108.2023.10281986` . iSSN: 2153-7003. 

- Yan, Y., He, X., Wan, W., Liu, J., 2023. Mmnet: Multi-mask network for referring image segmentation. URL: `https://arxiv.org/abs/2305.14969` , `arXiv:2305.14969` . 

- Yang, C.E., Fu, J.S., Liu, Y., Dong, X., Liu, Y., 2022a. Projections of future wildfires impacts on air pollutants and air toxics in a changing climate over the western United States. Environmental Pollution 304, 119213. URL: `https://www.sciencedirect.com/science/article/pii/ S0269749122004274` , doi: `10.1016/j.envpol.2022.119213` . 

- Yang, J., He, H.S., Gustafson, E.J., 2004. A hierarchical fire frequency model to simulate temporal patterns of fire regimes in landis. Ecological Modelling 180, 119–133. 

- Yang, Z., Wang, J., Tang, Y., Chen, K., Zhao, H., Torr, P.H., 2022b. Lavt: Language-aware vision transformer for referring image segmentation, in: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pp. 18155–18165. 

- Yao, J., Zhang, B., Li, C., Hong, D., Chanussot, J., 2023. Extended vision transformer (exvit) for land use and land cover classification: A multimodal deep learning framework. IEEE Transactions on Geoscience and Remote Sensing 61, 1–15. doi: `10.1109/TGRS.2023.3284671` . 

- Ye, X., Saide, P.E., Hair, J., Fenn, M., Shingler, T., Soja, A., Gargulinski, E., Wiggins, E., 2022. Assessing vertical allocation of wildfire smoke emissions using observational constraints from airborne lidar in the western us. Journal of Geophysical Research: Atmospheres 127, e2022JD036808. 

- Yebra, M., Chuvieco, E., Riano, D., 2008. Estimation of live fuel moisture content from modis images for fire risk assessment. Agricultural and forest meteorology 148, 523–536. 

- Yebra, M., Dennison, P.E., Chuvieco, E., Riaño, D., Zylstra, P., Hunt Jr, E.R., Danson, F.M., Qi, Y., Jurdao, S., 2013a. A global review of remote sensing of live fuel moisture content for fire danger assessment: Moving towards operational products. Remote Sensing of Environment 136, 455–468. 

- Yebra, M., Dennison, P.E., Chuvieco, E., Riaño, D., Zylstra, P., Hunt, E.R., Danson, F.M., Qi, Y., Jurdao, S., 2013b. A global review of remote sensing of live fuel moisture content for fire danger assessment: Moving towards operational products. Remote Sensing of Environment 136, 455– 468. URL: `https://www.sciencedirect.com/science/article/ pii/S0034425713001831` , doi: `10.1016/j.rse.2013.05.029` . 

- Ying, L., Cheng, H., Shen, Z., Guan, P., Luo, C., Peng, X., 2021. Relative humidity and agricultural activities dominate wildfire ignitions in yunnan, southwest china: Patterns, thresholds, and implications. Agricultural and Forest Meteorology 307, 108540. 

57 

- Ying, L., Shen, Z., Yang, M., Piao, S., 2019. Wildfire detection probability of modis fire products under the constraint of environmental factors: A study based on confirmed ground wildfire records. Remote Sensing 11, 3031. 

- Yoon, H.J., Voulgaris, P., 2022. Multi-time predictions of wildfire grid map using remote sensing local data, in: 2022 IEEE International Conference on Knowledge Graph (ICKG), pp. 365–372. doi: `10.1109/ICKG55886.2022. 00053` . 

- Yu, Y., Liu, L., Chang, Z., Li, Y., Shi, K., 2024. Detecting forest fires in southwest china from remote sensing nighttime lights using the random forest classification model. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing 17, 10759–10769. doi: `10.1109/JSTARS. 2024.3410172` . 

- Yuan, C., Zhang, Y., Liu, Z., 2015. A survey on technologies for automatic forest fire monitoring, detection, and fighting using unmanned aerial vehicles and remote sensing techniques. Canadian journal of forest research 45, 783–792. 

- Yuan, Z., Mou, L., Hua, Y., Zhu, X.X., 2024. Rrsis: Referring remote sensing image segmentation. IEEE Transactions on Geoscience and Remote Sensing 62, 1–12. doi: `10.1109/TGRS.2024.3369720` . 

- Yue, W., Ren, C., Liang, Y., Liang, J., Lin, X., Yin, A., Wei, Z., 2023. Assessment of wildfire susceptibility and wildfire threats to ecological environment and urban development based on gis and multi-source data: A case study of guilin, china. Remote Sensing 15, 2659. 

- Zacharakis, I., Tsihrintzis, V.A., 2023. Integrated wildfire danger models and factors: A review. Science of The Total Environment 899, 165704. URL: `https://linkinghub.elsevier.com/retrieve/pii/ S0048969723043279` , doi: `10.1016/j.scitotenv.2023.165704` . 

- Zarzycki, K., Ławry´nczuk, M., 2022. Advanced predictive control for gru and lstm networks. Information Sciences 616, 229–254. 

- Zerveas, G., Jayaraman, S., Patel, D., Bhamidipaty, A., Eickhoff, C., 2021. A Transformer-based Framework for Multivariate Time Series Representation Learning, in: Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discovery & Data Mining, Association for Computing Machinery, New York, NY, USA. pp. 2114–2124. URL: `https://dl.acm.org/ doi/10.1145/3447548.3467401` , doi: `10.1145/3447548.3467401` . 

2, sentinel-1, and alos-2 palsar-2 data for large-scale wildfire-burned area mapping: insights from the 2017–2019 canada wildfires. Remote Sensing 16, 556. 

   - Zhang, X., Lan, M., Ming, J., Zhu, J., Lo, S., 2023b. Spatiotemporal heterogeneity of forest fire occurrence based on remote sensing data: An analysis in anhui, china. Remote Sensing 15. URL: `https://www.mdpi.com/ 2072-4292/15/3/598` , doi: `10.3390/rs15030598` . 

   - Zhao, F., Liu, Y., 2021. Important meteorological predictors for long-range wildfires in China. Forest Ecology and Management 499, 119638. URL: `https://www.sciencedirect.com/science/article/pii/ S0378112721007283` , doi: `10.1016/j.foreco.2021.119638` . 

   - Zhao, S., Prapas, I., Karasante, I., Xiong, Z., Papoutsis, I., CampsValls, G., Zhu, X.X., 2024. Causal graph neural networks for wildfire danger prediction. URL: `https://arxiv.org/abs/2403.08414` , `arXiv:2403.08414` . 

   - Zhou, M., Wang, J., Garcia, L.C., Chen, X., da Silva, A.M., Wang, Z., Román, M.O., Hyer, E.J., Miller, S.D., 2023. Enhancement of nighttime fire detection and combustion efficiency characterization using suomi-npp and noaa20 viirs instruments. IEEE Transactions on Geoscience and Remote Sensing 61, 1–20. doi: `10.1109/TGRS.2023.3261664` . 

   - Zhu, L., Webb, G.I., Yebra, M., Scortechini, G., Miller, L., Petitjean, F., 2021. Live fuel moisture content estimation from MODIS: A deep learning approach. ISPRS Journal of Photogrammetry and Remote Sensing 179, 81–91. URL: `https://www.sciencedirect.com/science/article/ pii/S0924271621001957` , doi: `10.1016/j.isprsjprs.2021.07.010` . 

   - ZORMPAS, K., VASILAKOS, C., ATHANASIS, N., SOULAKELLIS, N., KALABOKIDIS, K., 2017. Dead fuel moisture content estimation using remote sensing. European Journal of Geography 8. 

   - Zubkova, M., Lötter, M., Bronkhorst, F., Giglio, L., 2024. Assessment of the effectiveness of coarse resolution fire products in monitoring long-term changes in fire regime within protected areas in south africa. International Journal of Applied Earth Observation and Geoinformation 132, 104064. 

- Zhang, C., Pan, X., Li, H., Gardiner, A., Sargent, I., Hare, J., Atkinson, P.M., 2018. A hybrid MLP-CNN classifier for very fine resolution remotely sensed image classification. ISPRS Journal of Photogrammetry and Remote Sensing 140, 133–144. URL: `https://www. sciencedirect.com/science/article/pii/S0924271617300254` , doi: `10.1016/j.isprsjprs.2017.07.014` . 

- Zhang, D., Huang, C., Gu, J., Hou, J., Zhang, Y., Han, W., Dou, P., Feng, Y., 2023a. Real-time wildfire detection algorithm based on viirs fire product and himawari-8 data. Remote Sensing 15. URL: `https://www.mdpi. com/2072-4292/15/6/1541` , doi: `10.3390/rs15061541` . 

- Zhang, G., Wang, M., Liu, K., 2019. Forest Fire Susceptibility Modeling Using a Convolutional Neural Network for Yunnan Province of China. International Journal of Disaster Risk Science 10, 386–403. URL: `https://doi.org/10.1007/s13753-019-00233-1` , doi: `10.1007/s13753-019-00233-1` . 

- Zhang, G., Wang, M., Liu, K., 2021a. Deep neural networks for global wildfire susceptibility modelling. Ecological Indicators 127, 107735. URL: `https://www.sciencedirect.com/science/ article/pii/S1470160X21004003` , doi: `10.1016/j.ecolind.2021. 107735` . 

- Zhang, G., Wang, M., Liu, K., 2022. Dynamic prediction of global monthly burned area with hybrid deep neural networks. Ecological Applications 32, e2610. 

- Zhang, G., Wang, M., Yang, B., Liu, K., 2024a. Current and future patterns of global wildfire based on deep neural networks. Earth’s Future 12, e2023EF004088. 

- Zhang, M., Ángel Fernández-Torres, M., Cohrs, K.H., Camps-Valls, G., 2025. Calibration and uncertainty quantification for deep learning-based drought detection. International Journal of Applied Earth Observation and Geoinformation 140, 104563. URL: `https://www.sciencedirect. com/science/article/pii/S1569843225002109` , doi: `https://doi. org/10.1016/j.jag.2025.104563` . 

- Zhang, P., Ban, Y., Nascetti, A., 2021b. Learning u-net without forgetting for near real-time wildfire monitoring by the fusion of sar and optical time series. Remote Sensing of Environment 261, 112467. 

- Zhang, P., Hu, X., Ban, Y., Nascetti, A., Gong, M., 2024b. Assessing sentinel- 

58 


