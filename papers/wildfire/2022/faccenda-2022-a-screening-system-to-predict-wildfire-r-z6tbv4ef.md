---
title: A screening system to predict wildfire risk of invasive plants
authors:
- Faccenda, Kevin
- Daehler, Curtis C.
year: '2022'
journal: Biological Invasions
doi: 10.1007/s10530-021-02661-x
tags:
- invasive species
- random forest
- wildfire
zotero_key: Z6TBV4EF
item_type: journalArticle
url: https://doi.org/10.1007/s10530-021-02661-x
source_url: 'unpaywall: https://link.springer.com/content/pdf/10.1007/s10530-021-02661-x.pdf'
fulltext_status: fulltext
synced: '2026-11-06'
---

# A screening system to predict wildfire risk of invasive plants

## Abstract

Globally, invasive plant-fueled wildfires have tremendous environmental, economical, and societal impacts, and the frequencies of wildfires and plant invasions are on an upward trend globally. Identifying which plant species tend to increase the frequency or severity of wildfire is important to help manage their impacts. We developed a screening system to identify introduced plant species that are likely to increase wildfire risk, using the Hawaiian Islands to test the system and illustrate how the system can be applied to inform management decisions. Expert-based fire risk scores derived from field experiences with 49 invasive species in Hawai′i were used to train a machine learning model that predicts expert fire risk scores from among 21 plant traits obtained from literature and databases. The model revealed that just four variables can identify species categorized as higher fire risk by experts with 90% accuracy, while low risk species were identified with 79% accuracy. We then used the predictive model to screen > 140 recently naturalized plants in Hawai′i to illustrate how the screening tool can be applied. The screening tool identified a managebly small set of species (6% of naturalizations in the last ~ 10 years) that are likely to pose a high fire risk and can be targeted for eradication or containment to reduce future wildfire risks. Because the screening system uses general plant traits that are likely relevant to fire risk in drylands around the world, it can likely be applied with minimal modification to other regions where invasive plants pose potential fire risks.

## Full text

Biol Invasions (2022) 24:575–589 https://doi.org/10.1007/s10530-021-02661-x (0123456789().,-volV)( 

ORIGINAL PAPER 



# A screening system to predict wildfire risk of invasive plants 

Kevin Faccenda . Curtis C. Daehler 

Received: 20 April 2021 / Accepted: 6 October 2021 / Published online: 12 November 2021 � The Author(s) 2021 

Abstract Globally, invasive plant-fueled wildfires have tremendous environmental, economical, and societal impacts, and the frequencies of wildfires and plant invasions are on an upward trend globally. Identifying which plant species tend to increase the frequency or severity of wildfire is important to help manage their impacts. We developed a screening system to identify introduced plant species that are likely to increase wildfire risk, using the Hawaiian Islands to test the system and illustrate how the system can be applied to inform management decisions. Expert-based fire risk scores derived from field experiences with 49 invasive species in Hawai<sup>0</sup> i were used to train a machine learning model that predicts expert fire risk scores from among 21 plant traits obtained from literature and databases. The model revealed that just four variables can identify species categorized as higher fire risk by experts with 90% accuracy, while low risk species were identified with 79% accuracy. We then used the predictive model to screen [ 140 recently naturalized plants in Hawai<sup>0</sup> i to illustrate how the screening tool can be applied. The screening tool identified a managebly small set of 

Supplementary Information The online version contains supplementary material available at https://doi.org/10.1007/ s10530-021-02661-x. 

K. Faccenda (&) � C. C. Daehler School of Life Sciences, University of Hawai<sup>0</sup> i at Ma¯noa, 3190 Maile Way, Honolulu, HI 96822, USA e-mail: faccenda@hawaii.edu 

species (6% of naturalizations in the last * 10 years) that are likely to pose a high fire risk and can be targeted for eradication or containment to reduce future wildfire risks. Because the screening system uses general plant traits that are likely relevant to fire risk in drylands around the world, it can likely be applied with minimal modification to other regions where invasive plants pose potential fire risks. 

Keywords Screening system � Wildfire � Invasive plant � Random forest � Hawai<sup>0</sup> i 

## Background 

Globally, uncontrolled wildland fires have major impacts on human health (Reid et al. 2016), soil stability (Shakesby 2011), and rare plant and ecosystem conservation (DLNR 2003) among many other impacts. The size and intensity of wildfires has been on an upward trend globally and is projected to increase as temperature, rainfall, and other climatic patterns are altered by climate change (Settele et al. 2014; Williams et al. 2019). In many areas, especially throughout the tropics and subtropics, biomass from invasive plants comprises a major component of the fuel that drives wildfires (Smith and Tunison 1992; D’Antonio and Vitousek 1992; Fusco et al. 2019). New plant introductions are continuing around the 

123 

576 

K. Faccenda, C. C. Daehler 

world, and similar or increased rates of introduction and plant naturalization are likely to continue in the future (Seebens et al. 2017; Seebens et al. 2021). Characterizing the fire risk of alien plants is a pressing need in order to help resource managers anticipate how novel alien plant invasions may alter wildfire risk and threaten natural resource conservation and other human interests. We define plants with high fire risk as those which can modify fuels across a landscape in a manner that increases the risk of wildfires with undesirable impacts. 

Plant flammability (including ignitability, sustainability, combustibility, and consumability) has previously been assessed via a variety of experimental methods such as chemical assays of plant tissue (Broido and Nelson 1964), calorimetry (Madrigal et al. 2013; Simpson et al. 2016), plant functional trait analysis (Santacruz-Garcı´a et al. 2019), and small scale (Dimitrakopoulos and Papaioannou 2001; Ganteaume et al. 2013) or twig scale burn tests (Jaureguiberry et al. 2011; Wyse et al. 2016, 2018; Alam et al. 2020). These methods require large amounts of plant material and specialized equipment, especially for the most accurate methods (Alam et al. 2020). If wildfire risk of plants can be assessed via information available from existing literature and data, such an approach would allow easier identification of high risk species before new alien plant species arrive or when they are discovered in a region or site, allowing managers or policy makers to make informed decisions about prohibiting introductions, eradicating, or controlling these high risk species. 

Identifying plant species of concern via weed risk assessments (WRA) has been shown to be a valuable tool for predicting which introduced plant species may become invasive pests (Daehler and Carino 2000; Dawson et al. 2009; Gasso´ et al. 2010; McClay et al. 2010; Morais et al. 2017; He et al. 2018). Current WRA frameworks such as the widely adopted Australian WRA (Pheloung et al. 1999) assess a species by examining characteristics relating to the plant’s biology and behavior elsewhere in order to predict whether a plant is likely to be a weed. Previous work has used geographic modeling to identify regions which are more or less vulnerable to invasion by species known to promote fire (Link et al. 2006; Chambers et al. 2019). However, geographically independent risk assessment systems have not been 

developed to specifically predict an introduced plant’s risk of promoting wildfires. 

Hawai<sup>0</sup> i has the largest percentage area burned by wildfire among all US states due to a combination of historical land use practices and the spread of invasive plants (Ellsworth et al. 2014; Trauernicht et al. 2015). Hawai<sup>0</sup> i also is continuing to experience new plant naturalizations at an average rate of about 10 new species per year over the last decade (Evenhuis 2020); it is likely that some of these newly naturalized species may go on to further modify fire regimes and pose additional wildfire threats. This combination of factors makes Hawai<sup>0</sup> i an ideal and practical case study for developing and testing a generalizable, literaturebased screening system for alien plants which can increase wildfire risk. 

Expert rankings of plant flammability (generally defined as the ability of plant material to ignite and sustain a fire) have previously been shown to be highly correlated with experimentally measured plant flammability (Wyse et al. 2016). In particular, local experts who have first-hand knowledge of particular species’ behavior in the field can provide a reliable assessment of species’ behavior, and thus expert ratings could be used to assess fire risk of established invaders in a region. However, obtaining an expertbased assessment requires identifying one or more appropriate individuals who are willing to provide the assessment. Furthermore, local experts are unlikely to have first-hand fire-related experience with new plant introductions and naturalizations. Therefore, a literature-based screening system that has been calibrated based on expert ratings can be more broadly implemented for screening, relative to a strict reliance on expert ratings. 

Our objective was to develop a literature-based screening system that can be used to assess the wildfire risk posed by introduced plants. Previous work has shown that machine learning techniques can be used to develop efficient and accurate screening systems by identifying information that is most useful for prediction. For example, the Australian WRA (Pheloung et al. 1999) uses 49 questions, but machine learning methods have found that it could be reduced to as few as 4 questions while yielding similar predictive ability to the full assessment (Caley and Kuhnert 2006; Weber et al. 2009). We employed a similar approach using conditional random forests (Strobl et al. 2008), a type of random forest algorithm (Breiman 2001), to 

123 

577 

A screening system to predict wildfire risk of invasive plants 

identify the most important plant traits among 21 literature-derived variables in order to construct a screening system to identify introduced plants that pose high wildfire risk, as indicated by expert ratings. We then demonstrate application of this approach to predict wildfire risk by screening recently arriving or naturalizing plants in Hawai<sup>0</sup> i, for which no first-hand experience is available from local experts. 

## Methods 

## Expert survey of invasive plant fire risk 

In order to obtain expert-based ratings for Hawai<sup>0</sup> i, natural resource managers were asked to rate the wildfire risk of 49 naturalized plants in Hawai<sup>0</sup> i based on their personal experience and observations of the species specifically in Hawai<sup>0</sup> i. An invitation to complete an online survey was circulated among several email listservers targeting resource managers, wildfire managers, and invasive plant managers in Hawai<sup>0</sup> i. Email invitations were also sent directly to 32 individuals known to have experience with invasive plants and wildfires across Hawai<sup>0</sup> i. The survey ran for 1 month starting October 19, 2020. The survey asked each respondent to rate wildfire risk in Hawai<sup>0</sup> i posed by each of 49 naturalized plant species using one of the following 5 categories: unknown, no concern, low risk, medium risk, and high risk. To document the backgrounds of each expert, the survey also asked which island(s) the respondent is most familiar with as well as what type of resources they manage and how they obtained their experience. 

The 49 species chosen for the survey were selected by C. Daehler from the list of naturalized plants in Hawai<sup>0</sup> i (Imada 2019) and included mostly recognized weeds of natural areas (Motooka et al. 2003), focusing on those found in dry or seasonally dry environments, with many life forms of plants included. The taxonomy used here follows Imada (2019). In two cases, genus names were used on the expert survey as Hawai<sup>0</sup> i has two naturalized species in those genera that are morphologically and ecologically similar (Cortaderia spp. = C. jubata ? C. selloana and Cryptostegia spp. = C. madagascariensis ? C. grandiflora). 

## Expert-based fire risk score 

In order to establish initial coarse fire risk categories of potential use for informing management decisions, two risk categories were defined, low risk and high/ medium risk. A plant was categorized as low risk if more than half of its ratings were ‘‘low risk’’ or ‘‘no concern’’ (not counting blank or ‘‘unknown’’ responses). Otherwise, the plant was categorized as high/medium risk. A quantitative risk score was also calculated for each species by expressing the survey responses as a proportion as recommended by Harpe (2015) with slight modification by weighing a medium risk rating by 50% relative to a high risk rating. The following formula was used: (number of high responses ? the number of medium responses * 0.5) / the total number of responses. Survey responses which were left blank or answered as ‘‘unknown’’ for a given species were not counted in the denominator. 

## Assembling literature-based species information 

Previous work has identified various functional, chemical, or ecological traits that may be associated with increased plant flammability (mostly ignitability), such as small leaf size, stem branching pattern (Alam 2019), thin leaves or high specific leaf area (Grootemaat 2015; Alam et al. 2020), high horizontal continuity of fuels across a landscape (Brooks et al. 2004), dead leaf retention (Bowman et al. 2014), tissues which contain high quantities of oils or resins (Brooks et al. 2004), and growth habit (Cui et al. 2020) to name a few. White and Zipperer (2010) along with Bowman et al. (2014) also provided more general plant traits associated with fire promotion. Although these previous findings were not specific to invasive plants, we nevertheless expect that invasive or weedy plants possessing these traits may pose high wildfire risks. We used this prior research on plant flammability and trait trends in fire-prone vegetation to identify a list of 21 traits to be collected from literature and databases (Table 1). 

Species information was assembled from literature and database searches as well as photos (full protocol detailed in Online Resource 1). All information was collected without access to the plant itself, under the assumption that a screener wanting to apply the screening system may not have convenient access to live material. Any information derived from field 

123 

578 

K. Faccenda, C. C. Daehler 

Table 1 Full set of literature-derived plant traits tested for potential inclusion in a screening system used to predict wildfire risk: For the details of how these traits were evaluated, see Online Resource 1 

|Trait|Description|Reason|Values|
|---|---|---|---|
|Vine|Is the plant a vine?|The growth form of a plant is broadly correlated with|Yes, no|
|Woody|Is the plant woody?|its fuel characteristics (Cui et al. 2020)|Yes, no|
|Herbaceous|Is the plant herbaceous (not forming significant woody<br>tissue)?||Yes, no|
|Graminoid|Is the plant in one of the following families: Poaceae,<br>Cyperaceae, Typhaceae, or Juncaceae?||Yes, no|
|Average<br>height|Height of plant, median value between reported min<br>and max height|Heights of grasses have been correlated with<br>flammability (Jardine 2017)|Continuous|
|Leaf<br>thickness|Thickness of the photosynthetic organs of the plant,<br>even if they are not true leaves|Thinner leaves burn more quickly and take less<br>energy to ignite (Grootemaat 2015; Alam 2019)|Thin/chartaceous,<br>thick/leathery,<br>succulent/water<br>filled|
|SLA|Specific leaf area of dry leaves||Continuous|
|Leaf or<br>Leaflet<br>Area|Approximate area of the smallest leaf division|Greater leaf surface area has been implicated to high<br>flammability (Alam 2019)|Continuous|
|Fine standing<br>debris|Does the plant retain large quantities of fine dead<br>material elevated off the ground?|Fine standing dead material is typically dry and easy<br>to ignite (Bowman et al. 2014)|Yes, no, no data|
|Monocultures|Is the plant capable of forming monocultures across<br>the landscape?|Plants which occur at high density can modify fuel<br>characteristics more than those which occur at low<br>|Yes, no|
|Stand density|How dense is the plant capable of getting?|density (White and Zipperer 2010)|Sparse, dense, no<br>data|
|Vegetatitive<br>horizontal<br>continuity|Does a plant spread vegetatively by rooting, stolons, or<br>runners in such a way that individual genets form a<br>single clone is capable of spreading fire across a<br>landscape?|Plants which sprawl across the landscape can spread<br>fire quickly (Brooks et al. 2004)|High, low, no data|
|Leaf litter|How much litter is produced by the plant?|A buildup of leaf litter can spread fuel across a<br>landscape (Burton et al. 2020)|High/medium, low,<br>no data|
|Native<br>habitat fire<br>proneness|In any part of the plant’s native range is its habitat<br>described as fire prone due to natural or human<br>caused fires?|There is a positive correlation between habitat fire<br>proneness and plant flammability (Cui et al. 2020)|Yes, no, no data|
|Fire<br>promoting<br>native|Does the species act as a major fuel source, increase<br>fire severity, frequency, or modify fuel bed<br>characteristics within its native range?|Plants which have a history of flammability in one<br>area may be flammable in other areas|Yes, no|
|Fire<br>promoting<br>invader<br>elsewhere|Same as fire promoting native but within the species<br>introduced range||Yes, no|
|Reported<br>flammable|Is the species described as being flammable, being a<br>major wildfire fuel, or high fire risk? This mainly<br>refers to fuels with high ignitability||High, low, no data|
|Regenerates<br>after fire|Does the plant regrow after fire by any means? This<br>includes resprouters, reseeders, and recruiters which<br>dispersed into the area within approximately one<br>year post fire|Many plants which have evolved flammability have<br>also evolved the ability to regenerate after fire<br>(Mutch 1970)|Yes, no, no data|
|Promoted By<br>fire|Does the plant increase in abundance after a fire?||Yes, no, no data|
|Flammable<br>compounds|Does the plant contain high quantities of flammable<br>oils or resins which make the tissues more flammable<br>or lower the ignition temperature?|These increase tissue flammability (Brooks et al.<br>2004)|Yes, no|
|Congeneric<br>relative is<br>flammable|Does a plant in the same genus meet the reported<br>flammable criteria?|Flammability is a phylogenetically conserved trait<br>(Cui et al. 2020). This has also been useful as a<br>predictor in WRA (e.g. Weber et al. 2009)|Yes, no|



123 

579 

A screening system to predict wildfire risk of invasive plants 

studies in Hawai<sup>0</sup> i was not used for the literature-based species assessments. Trait data were assembled for all species ranked by experts, as well as for the set of 142 species reported as newly naturalized or potentially naturalizing in Hawai<sup>0</sup> i between 2010 and 2019 (Kelsey Brock pers. comm.). 

To designate trait data for Cortaderia spp. and Cryptostegia spp. each species was evaluated separately, and then literature-based data from both species in each genus were combined to create a composite species, using the most extreme (most likely to promote fire) trait value from the two species. 

## Random forest modeling 

A random forest based model was chosen to predict wildfire risk from the literature survey data for several reasons; it handles both categorical and quantitative data, it handles interactions between predictors well, it is very robust to overfitting, and can provide importance values for predictor variables (Breiman 2001). Specifically, conditional random forest (cforest; Strobl et al. 2008) was chosen, which is a variant of the traditional random forest that uses a forest of conditional inference trees (Strobl et al. 2008). Cforest provides unbiased variable splitting during tree growth which gives an advantage when using both categorical and continuous variables in the same model as well as providing more accurate variable importance metrics (Strobl et al. 2009). 

All code and statistics were run in R (R Core Team 2021), and the party package (Strobl et al. 2008) was used for the cforest models. To compare models and run cross-validation caret (Kuhn 2020) was used, ggplot2 (Wickham 2016) was used to create figues, sqldf (Grothendieck 2017) was used for manipulating data. 

For categorical plant trait variables, missing values were treated as their own attributes (Twala et al. 2008; Josse et al. 2019) as being unable to find data during the literature search was not truly random. For the missing quantitative values in the training data (only SLA), the missing values were imputed using the na.roughfix function from the randomForest package (Liaw and Wiener 2002). 

All models were trained as regression models using the quantitative expert-based risk score as the response variable and the literature-based traits as predictor variables. The mtry hyperparameter was optimized for 

each model by selecting the model with the lowest root-mean-square error (RMSE). Each model was run using leave one out cross-validation (LOOCV), and the RMSE and the area under the receiver operator characteristic (AUC) were calculated. To assess variable importance, a conditional variable importance metric was used as it is able to identify important predictors among correlated variables more accurately than random forest (Strobl et al. 2009). The varImp function in the party package was used for this after a cforest model was trained on the data. 

The model complexity was reduced by eliminating predictor variables to assess whether predictive success can be maintained with fewer literature-based variables. Predictor variables were eliminated one at a time, starting with those with the lowest importance and ascending the list until the model performance began to decline as determined by the RMSE value reported from the cross-validation. After the RMSE value began to drop, the final model was trained using only the remaining, most important, predictors. The AUC score for the final model was generated by leavepair-out cross-validation as recommended by Airola et al. (2009) using the nlpred package (Benkeser 2020). 

The sensitivity and specificity of the final model were approximated using the predicted scores from each of the 49 LOOCV runs and whether the species was ranked by experts as low or high/medium risk. These sensitivity and specificity values based on LOOCV are approximate, as the small size of our training dataset (49 species) did not allow partitioning of the data into separate training and evaluation datasets. 

The final model was then used to predict fire risk scores for the 142 recently naturalized and potentially naturalized species in Hawai<sup>0</sup> i. As the final cforest model is a regression model and outputs a numeric score, a threshold value can be chosen to separate species into categories, such as low and high fire risk. We define a species with a score below this threshold as ‘‘low risk’’ and species above it as ‘‘higher risk’’ for potential management action. 

## Results 

Fifty experts responded to the wildfire risk survey resulting in an average of 35 ratings for each species 

123 

580 

K. Faccenda, C. C. Daehler 

with a standard deviation of ± 7.7. The minimum number of responses received for a species was 17. One respondent ranked all species as either high or medium fire risk and was a clear outlier, this response was removed resulting in a total of 49 expert responses used in this analysis. Respondents self-reported that their experiences with wildfire and invasive plants in Hawai<sup>0</sup> i derived from their expertise as land managers (59%), researchers (16%), field technicians or contractors (15%), naturalists (6%), and educators or community liaisons (4%). 63% of respondents designated themselves as natural resource managers, 25% as natural and cultural resource managers, and 12% did not list themselves as directly managing any resources. Respondents obtained their experiences from across all of the seven main Hawaiian islands with the exception of Ni‘ihau, which is a smaller, privately owned island. 

Fire risk scores for the 49 species surveyed ranged from 0 to 0.98 with an approximately continuous variation between the highest and lowest scores (Fig. 1). The cforest model revealed that the most important predictor variables of expert rankings of wildfire risk are Reported Flammable, Graminoid, Congeneric Relative is Flammable, and Fire Promoting Invader Elsewhere (Fig. 2). Only the four variables previously listed were used to train the final cforest model used for prediction, as removing the other 17 variables did not substantially decrease the model’s performance. Using the full dataset of 21 variables, the model had an RMSE of 0.184 and an AUC of 0.903. In contrast, the model using only the four most important predictor variables had an RMSE of 0.178 and AUC of 0.881. From hereon, we refer to the final trained cforest model as the screening system. 

Using a threshold value of 0.34 to separate low risk and higher risk species, the screening system had a 90% sensitivity (true positive rate) and 79% specificity (true negative rate). As the cforest model is deterministic and has only 4 input variables and 24 unique combinations of inputs, these were tabulated in Table 2 to allow the screening system to be used without having to run the cforest model or any other code. 

After assessing all recently naturalized and potentially naturalized species in Hawai<sup>0</sup> i, 94% were categorized as low fire risk, while 8 of 142 (6%) were categorized as higher risk, to be considered for management action (Table 3). Species which were ranked as low fire risk are included in Online Resource 

Fig. 1 Expert-based fire risk scores of each species assessed in c the land manager survey. The score is the proportion of the respondents who ranked the plant as high fire risk plus � of the respondents who ranked it medium risk out of the total number of respondents for each species. Species that had ratings of High or Medium by the majority of experts, were categorized as High/ Medium risk (black bars); other species were categorized as low risk (gray bars) 

2. We also present the species’ fire risk scores along with corresponding literature-based information and whether they regenerate after fire, or are promoted by fire, as these data could be used in combination with the fire risk score to inform management decisions. Assessing each species for only the four literaturebased variables required for the simplified screening system took an average of 35 min with a standard deviation of ± 15 min and a maximum time of 83 min. 

## Discussion 

We developed a literature-based screening system for predicting wildfire risk of alien plants. The literaturebased assessment scores had a high predictive ability, correctly identifying 90% of plants considered to be a high fire risk. The screening system is easy to complete, requiring only literature-based answers to four questions, and can typically be completed for a plant species in an hour or less. The assessment questions are not location-specific and we expect the screening system can be applied with little or no modification in other fire-prone regions of the world. 

Threshold values for low/higher risk 

To inform management decisions, the screening system separates plants into two categories: low risk and higher risk. The low risk category was calibrated such that most experts agreed these plants were of low or no concern as contributors to wildfires. The threshold of 0.34 used to separate the low risk and higher risk species in Table 2 was chosen as it was desired that the screening system should have a higher sensitivity (true positive rate for higher risk species) than specificity in accordance with the precautionary principle. Thus, the 0.34 threshold is conservative in placing species in the low risk category. However, 

123 

581 

A screening system to predict wildfire risk of invasive plants 



123 

582 

K. Faccenda, C. C. Daehler 



Fig. 2 Importance values of various wildfire risk predictor variables as determined by a conditional random forest model when trained on the expert fire risk scores. The increase in model accuracy is in units of Mean Standard Error (MSE) 

depending on goals, different threshold values could be chosen to get an even higher sensitivity (true positive rate) at the cost of a lower specificity (a higher false positive rate). The relationship between sensitivity and specificity is given in Online Resource 3. 

Analysis of plant traits 

Somewhat unsurprisingly, our model determined that the most important variable for predicting whether a species will pose a high wildfire risk in Hawai<sup>0</sup> i is whether it has been reported as flammable somewhere else (Fig. 2). Previous work in the field of invasion ecology has also found that the best way to predict whether a plant will display a complex and emergent trait such as invasiveness (or in our case fire risk) in a new area is simply to ask whether it or a closely related relative displays that trait somewhere else (Daehler and Strong 1993; Scott and Panetta 1993; Mack 1996; Lockwood et al. 2001). When similar tree-based machine learning techniques have been used to reduce 

the number of variables in a weed risk assessment, plant behavior elsewhere (i.e. ‘‘weed elsewhere’’ and ‘‘congeneric weed‘‘) also appeared in the reduced models (Reichard and Hamilton 1997; Caley and Kuhnert 2006; Weber et al. 2009). 

Various fundamental biological traits thought to underlie fire risk were not identified as the most important traits in our model with emergent traits such as Reported Flammable showing the most importance (Fig. 2). However, when the model was run using the full suite of predictor variables except Reported Flammable, Congeneric Relative is Flammable, Graminoid, and Fire Promoting Invader Elsewhere, this modified model still has substantial predictive skill with a RMSE of 0.224 an AUC of 0.83. This indicates that a predictive model for fire risk can be developed from the other more fundamental traits, albeit less effectively than from the emergent traits. The relative importance rankings of variables left in this model were generally similar to those variables’ importance in the full model (Fig. 2), with the two most important 

123 

583 

A screening system to predict wildfire risk of invasive plants 

Table 2 All possible combinations of inputs to the reduced random forests model used as a screening system, and their corresponding scores. A species scoring [ 0.34 (italic scores) 

is considered a higher fire risk, while scores \ 0.34 are categorized as posing low wildfire risk 

|Reported flammable|Congeneric relative is flammable|Fire promoting invader elsewhere|Graminoid|Score|
|---|---|---|---|---|
|High|No|No|No|0.50|
|High|No|No|Yes|0.70|
|High|No|Yes|No|0.50|
|High|No|Yes|Yes|0.70|
|High|Yes|No|No|0.52|
|High|Yes|No|Yes|0.72|
|High|Yes|Yes|No|0.53|
|High|Yes|Yes|Yes|0.72|
|Low|No|No|No|0.25|
|Low|No|No|Yes|0.32|
|Low|No|Yes|No|0.25|
|Low|No|Yes|Yes|0.33|
|Low|Yes|No|No|0.30|
|Low|Yes|No|Yes|0.38|
|Low|Yes|Yes|No|0.31|
|Low|Yes|Yes|Yes|0.38|
|No data|No|No|No|0.16|
|No Data|No|No|Yes|0.25|
|No data|No|Yes|No|0.17|
|No data|No|Yes|Yes|0.25|
|No data|Yes|No|No|0.22|
|No data|Yes|No|Yes|0.31|
|No data|Yes|Yes|No|0.23|
|No data|Yes|Yes|Yes|0.31|



Table 3 Species identified as higher risk (scoring [ 0.34) from among 142 recently naturalized plants in Hawai<sup>0</sup> i, as well as their trait values used to obtain the score. Whether the plant regenerates after fire and is promoted by fire (increase in 

population post fire) is also included in the table, as this information may be useful in determining whether a species may develop or integrate into a fire feedback loop 

|Species|Risk<br>Score|Graminoid|Fire promoting<br>invader elsewhere|Reported<br>flammable|Congeneric relative<br>is flammable|Regenerates<br>after fire|Promoted<br>by fire|
|---|---|---|---|---|---|---|---|
|Disakisperma dubia<br>(Leptochloa dubia)|0.70|Yes|No|High|No|No data|No data|
|Eucalyptus cinerea|0.52|No|No|High|Yes|Yes|No data|
|Eucalyptus goniocalyx|0.52|No|No|High|Yes|Yes|No data|
|Banksia marginata|0.52|No|No|High|Yes|Yes|No|
|Gutierrezia sarothrae|0.52|No|No|High|Yes|Yes|Yes|
|Chromolaena odorata|0.50|No|Yes|High|No|Yes|No|
|Cirsium arvense|0.50|No|Yes|High|No|Yes|Yes|
|Pachira aquatica|0.50|No|No|High|No|No data|No data|



123 

584 

K. Faccenda, C. C. Daehler 

predictors being Leaf Litter and Promoted by Fire, both of which are correlated with increasing fire risk. 

Amount of litter produced was identified by the full model as the fifth most important variable, and the most important variable in the modified model above despite the leaf or leaflet size and leaf thickness variables both having very low importance (Fig. 2). Other work has shown that leaf size and leaf thickness directly affect the flammability (ignitability and sustainability) of litter (Engber and Varner 2012; Cornwell et al. 2015; Grootemaat 2015; Burton et al. 2020). However, these variables do not predict the quantity of litter produced which may ultimately be more important than leaf size and thickness. The leaf litter variable may also be acting as a proxy for habitat moisture, as dry habitats where leaf litter can accumulate tend to be more flammable than moist habitats where leaf litter quickly decays (Riutta et al. 2012). The Promoted by Fire trait has the sixth highest importance in the full model and the second in the modified model. Although we see no obvious inherent link between fire risk and a plant being promoted by fire, these traits are generally correlated for grasses that are part of a grass-fire cycle, and this signal may appear in the model due to the grasses that were included in the training data. 

All of the grasses in the training dataset were ranked as high/medium risk by the majority of experts (Fig. 1). This result is not surprising given the wellrecognized historical relationship between grasses and fire in many parts of the world and the fact that all grassses surveyed were relatively large and competitive species that grow in dry or seasonally dry environments. Of all the growth form traits examined, graminoid was the only one which was retained in the final model indicating its major importance. However, the fact that no grasses in the training dataset were rated by experts as a low fire risk is also a limitation as it means that the cforest model may not have learned to distinguish between high and potentially low fire risk grasses as well as possible. Nevertheless, the screening system will rate a grass as low risk, depending on information from the remaining three model variables, so we expect that the model can identify low risk grasses when they are screened. 

The experts surveyed ranked all five vines in the training set (Cardiospermum grandiflorum, Coccinia grandis, Cryptostegia spp., Dolichandra unguis-cati, and Passiflora tarminiana) as a low fire risk in 

Hawai<sup>0</sup> i. This is interesting as vines often act as ladder fuels which can move flames from a ground or grass fuel layer into the canopy and cause an escalation from a surface fire into a canopy fire (Brooks et al. 2004). It is uncertain whether these vines were ranked as low fire risk because they do not act as ladder fuels, or whether managers felt that they did not add substantial fuels to a fire. 

## Extending the model 

The screening system, as it was developed here, likely has lower value for predicting wildfire risk of native species since the Fire Promoting Invader Elsewhere question used is not applicable for most native plants which have not had a history of introduction outside the native range. The screening tool presented here is expected to be most useful when local expertise about a species fire risk is not available in an area, whereas for many native species, local expertise and evidence from historical fire records may be more readily available. 

In the course of carrying out literature searches, it was noticed that fire-related data seemed sparse for some species originating from predominantly nonEnglish speaking regions including, but not limited to Eastern and Southeast Asia, and Central America, especially when the species is not naturalized in other areas. Although we utilized online translations services when non-English sources were found online, additional data may exist in languages other than English that were not discovered using our English keywords and scientific names as search terms. This had little impact on the 49 species in the training dataset, but assessment of future species could include local keywords for fire from the species native/ introduced range when searching the literature. 

## Testing for biases 

We also tested whether expert survey participants who identified as researchers may have added circularity to the data by using their knowledge of literature rather than personal experience to rate fire risk (contradicting our survey instructions). We ran the reduced (4 variable) model again, but excluded researchers from the expert survey data. We found that the model RMSE increased slightly after removing the researchers (from 0.178 to 0.185) and the AUC also slightly 

123 

585 

A screening system to predict wildfire risk of invasive plants 

increased (from 0.881 to 0.885). These only minor changes in model predictive skill suggest that researchers, who were expected to have deep knowledge of scientific literature, did not strongly bias our survey results or introduce circularity. 

## Application of the model in Hawai<sup>0</sup> i 

To illustrate an application of the system, we screened 142 recently naturalized and potentially naturalizing plant species in Hawai<sup>0</sup> i in order to determine whether they may be expected to pose wildfire risks. Because these species have not yet spread widely in Hawai<sup>0</sup> i, direct field experiences in Hawai<sup>0</sup> i are not informative of fire risk for these species. The screening system indicates that the vast majority of newly naturalized species pose a low fire risk, and this allows managers to focus on a small number of species categorized as higher risk. Species distribution models could be considered to identify which areas the species are likely to spread into, so management and containment work can be focused in those areas (Chambers et al 2019). Additional local information should also be considered in prioritization. 

Among the eight species categorized as higher risk (Table 3), all scored well above the 0.34 cut-off, ranging from 0.50 to 0.70. Only one of these species is a grass, which is known only from a limited area of one island (Moloka‘i), and it might be considered as a target for eradication. A herbaceous second species, Cirsium arvense, is a spiny thistle that was reported as naturalized on Maui in 2018 (Oppenheimer 2019). This species is an aggressive weed in various parts of the world, spreads clonally by rhizomes as well as wind dispersed seeds (Keil 2006) and has been demonstrated to be a fire risk on the mainland United States. It also regenerates well after fire and it is promoted by fire (Zouhar 2001). Controlling populations as they enter fire sensitive areas should be of high priority. 

The remaining six species categorized as higher risk are woody. Chromolaena odorata is a sprawling shrub that has already been recognized as a major weed and is the focus of an eradication campaign by the O‘ahu Invasive Species Council (www.oahuisc. org/devil-weed/), but it has also been detected on Hawai<sup>0</sup> i island as of 2021 (https://www.biisc.org/ chromo/). These informational websites discuss various impacts of this invader but do not mention fire risk, 

suggesting a possible information gap. C. odorata has been described as having such extreme flammability (ignitability) as to be able to burn while still green (Macdonald 1983) and can act as a ladder fuel which can elevate understory or grass fires to become canopy fires (Te Beest et al. 2012). It also quickly regenerates after fire but fortunately, its population does not seem to increase after fire (Te Beest et al. 2012). 

Two species of Eucalyptus (E. cinerea and E. goniocalyx) have begun to show signs of naturalization and spread from the forestry plantations where they were initially planted (Wagner et al. 1999). Formation of new satellite populations should be monitored as Eucalyptus is generally a high fire risk. These species could be considered lower priority for immediate control, since plantations were planted [ 50 years ago and their recruitment rates have been relatively low. Wildfire risk is likely to be lower for these species unless dense stands develop. 

Two additional woody plants, Banksia marginata and Gutierrezia sarothrae are upright shrubby plants cultivated for their attractive flowers, but they could pose serious wildfire risk if they form dense populations. Both of these species require careful monitoring, particularly because they both produce abundant wind-dispersed seeds and will be difficult to control if they begin to spread more widely. 

The last species in the higher risk category seems to be of less concern. Pachira aquatica was first identified as naturalizing on O‘ahu in 2011 (Evenhuis and Eldredge 2013). This species is recognized as producing a flammable litter which can promote fires during the dry season in mangrove forests in Mexico (Caldero´n et al. 2020). In Hawai<sup>0</sup> i it has been naturalized in lowland rainforest, where its litter is unlikely to burn, and the plant has low dispersal ability, producing few, very large seeds. Control of this plant is a low priority in terms of wildfire concern. 

## Conclusion 

Invasive plants are often an important component of the biomass that promotes wildfires. Because the frequency and intensity of wildfires has been on an upward trend globally, and because climate change has the potential to increase wildfire risk in new areas, proactive management to prevent the spread of new fire-promoting invaders is an important approach to 

123 

586 

K. Faccenda, C. C. Daehler 

reduce wildfire risks in many dry or seasonally dry regions of the world. We developed and tested a screening system capable of identifying plant species that pose higher fire risk. The screening system has high accuracy based on testing in Hawai<sup>0</sup> i and uses data readily available from literature and databases. This screening system may be useful to land managers and decision makers for identifying plant management and exclusion priorities in any area where wildfire is a concern. 

Acknowledgements This research was funded by the Department of the Interior Pacific Islands Climate Adaptation Science Center. The project described in this publication was supported by Grant or Cooperative Agreement No.G20AC00073 to C. Daehler from the United States Geological Survey. The views and conclusions contained in this document are those of the authors and should not be interpreted as representing the opinions or policies of the U.S. Geological Survey. Mention of trade names or commercial products does not constitute their endorsement by the Pacific Islands Climate Adaptation Science Center or the National Climate Adaptation Science Center or the US Geological Survey. This manuscript is submitted for publication with the understanding that the United States Government is authorized to reproduce and distribute reprints for Governmental purposes. Thank you to two anonymous reviews whose comments helped improve this manuscript. We thank Kelsey Brock for providing feedback on the species list used for our expert survey and Kelsey Brock, Lucas Fortini and Clay Trauernicht for reviewing drafts of the wording used for our expert survey. Thank you to Ronja Steinbach for helping with species assessments. We greatly appreciate the time and expertise shared by all the resource managers who completed the survey. This is publication #151 from the School of Life Sciences, University of Hawai<sup>0</sup> i at Ma¯noa. 

Author contributions All authors contributed to the study conception and design. Material preparation, data collection and analysis were performed by Kevin Faccenda. The first draft of the manuscript was written by Kevin Faccenda and all authors commented on previous versions of the manuscript. All authors read and approved the final manuscript. 

Funding This work was funded by the USGS. 

Data availability The datasets generated and analysed during the current study are available from the corresponding author on reasonable request. 

Code Availability Code is available upon request. 

### Declarations 

Conflict of interest The authors have no conflicts of interest to declare. 

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/. 

## References 

- Airola A, Pahikkala T, Waegeman W, De Baets B, Salakoski T (2009) A comparison of AUC estimators in small-sample studies. In: Machine learning in systems biology PMLR, pp 3–13 

- Alam MA (2019) Plant functional traits associated with shoot flammability. Doctoral dissertation, Lincoln University 

- Alam MA, Wyse SV, Buckley HL, Perry GL, Sullivan JJ, Mason NW, Buxton R, Richardson SJ, Curran TJ (2020) Shoot flammability is decoupled from leaf flammability, but controlled by leaf functional traits. J Ecol 108:641–653. https://doi.org/10.1111/1365-2745.13289 

- Benkeser D (2020) nlpred: estimators of non-linear cross-validated risks optimized for small samples. R package version 1.0.1 https://CRAN.R-project.org/package=nlpred 

- Bowman DM, French BJ, Prior LD (2014) Have plants evolved to self-immolate? Front in Plant Sci 5:1–9. https://doi.org/ 10.3389/fpls.2014.00590 

- Breiman L (2001) Random forests. Mach Learn 45:5–32. https://doi.org/10.1023/A:1010933404324 

- Broido A, Nelson MA (1964) Ash content: its effect on combustion of corn plants. Science 146:652–653. https://doi. org/10.1126/science.146.3644.652 

- Brooks ML, D’Antonio CM, Richardson DM, Grace JB, Keeley JE, DiTomaso JM, Hobbs RJ, Pellant M, Pyke D (2004) Effects of invasive alien plants on fire regimes. Bioscience 54:677–688. https://doi.org/10.1641/00063568(2004)054[0677:EOIAPO]2.0.CO;2 

- Burton JE, Cawson JG, Filkov AI, Penman TD (2020) Leaf traits predict global patterns in the structure and flammability of forest litter beds. J of Ecol 109:1344–1355. https://doi.org/ 10.1111/1365-2745.13561 

- Caldero´n RJ, Mata DI, Garnica JGF, Vela´zquez JRT, Sa´nchezMejı´a ZM, Me´ndez SM, Alvarado CM (2020) Fuel beds variation of coastal tropical freshwater forested wetlands in three disturbance regimes at La Encrucijada, Biosphere Reserve, Mexico. https://doi.org/10.21203/rs.3.rs-42037/ v1. Accessed 3 Feb 2021 

- Caley P, Kuhnert PM (2006) Application and evaluation of classification trees for screening unwanted plants. Austral 

123 

587 

A screening system to predict wildfire risk of invasive plants 

Ecol 31:647–655. https://doi.org/10.1111/j.1442-9993. 2006.01617.x 

- Chambers JC, Allen CR, Cushman SA (2019) Operationalizing ecological resilience concepts for managing species and ecosystems at risk. Front Ecol Evol 7:241. https://doi.org/ 10.3389/fevo.2019.00185 

- Clayton WD, Vorontsova MS, Harman KT, Williamson H (2021) GrassBase—The Online World Grass Flora. http:// www.kew.org/data/grasses-db.html. Accessed Oct 2020 

- Cornwell WK, Elvira A, van Kempen L, van Logtestijn RS, Aptroot A, Cornelissen JHC (2015) Flammability across the gymnosperm phylogeny: the importance of litter particle size. New Phytol 206:672–681. https://doi.org/10. 1111/nph.13317 

- Cui X, Paterson AM, Wyse SV, Alam MA, Maurin KJ, Pieper R, Cubino JP, O’Connell DM, Donkers D, Bre´da J, Buckley HL (2020) Shoot flammability of vascular plants is phylogenetically conserved and related to habitat fire-proneness and growth form. Nat Plants 6:355–359. https://doi. org/10.1038/s41477-020-0635-1 

- Daehler CC, Carino DA (2000) Predicting invasive plants: prospects for a general screening system based on current regional models. Biol Invasions 2:93–102. https://doi.org/ 10.1023/A:1010002005024 

- Daehler CC, Strong DR (1993) Prediction and biological invasions. Trends Ecol Evol 8:380. https://doi.org/10.1016/ 0169-5347(93)90227-g 

- D’Antonio CM, Vitousek PM (1992) Biological invasions by exotic grasses, the grass/fire cycle, and global change. Annu Rev Eco Syst 23:63–87. https://doi.org/10.1146/ annurev.es.23.110192.000431 

- Dawson W, Burslem DF, Hulme PE (2009) The suitability of weed risk assessment as a conservation tool to identify invasive plant threats in East African rainforests. Biol Conserv 142:1018–1024. https://doi.org/10.1016/j.biocon. 2009.01.013 

- Dimitrakopoulos AP, Papaioannou KK (2001) Flammability assessment of Mediterranean forest fuels. Fire Technol 37:143–152. https://doi.org/10.1023/A:1011641601076 

- DLNR (2003) Management plan for the ahupua‘a of Pu‘u Wa‘awa‘a and the makai lands of Pu‘u Anahulu. Department of Land and Natural Resources, State of Hawai’i, Honolulu. https://dlnr.hawaii.gov/forestry/files/2014/06/ PuuWaaWaaplanv6.pdf Accessed 15 Feb 2021 

- Ellsworth LM, Litton CM, Dale AP, Miura T (2014) Invasive grasses change landscape structure and fire behaviour in Hawaii. Appl Veg Sci 17:680–689. https://doi.org/10. 1111/avsc.12110 

- Engber EA, Varner JM III (2012) Patterns of flammability of the California oaks: the role of leaf traits. Can J Forest Res 42:1965–1975. https://doi.org/10.1139/x2012-138 

- Evenhuis NL (2020) Twenty-five years of the records of the Hawaii Biological Survey. Bishop Museum Occas Pap 129:1–2 

- Evenhuis NL, Eldredge LG (2013) New plant records for the Hawaiian Islands 2011–2012. Bishop Museum Occas Pap 114:5–16 

- Flora of North America Editorial Committee (eds) (1993?) Flora of North America North of Mexico. 21? vols. New York and Oxford 

- Fusco EJ, Finn JT, Balch JK, Nagy RC, Bradley BA (2019) Invasive grasses increase fire occurrence and frequency across US ecoregions. Proc Natl Acad Sci 116:23594–23599. https://doi.org/10.1073/pnas. 1908253116 

- Ganteaume A, Jappiot M, Lampin C, Guijarro M, Hernando C (2013) Flammability of some ornamental species in wildland–urban interfaces in southeastern France: laboratory assessment at particle level. Environ Manag 52:467–480. https://doi.org/10.1007/s00267-013-0067-z 

- Gasso´ N, Basnou C, Vila M (2010) Predicting plant invaders in the Mediterranean through a weed risk assessment system. Biol Invasions 12:463–476. https://doi.org/10.1007/ s10530-009-9451-2 

- Grootemaat S (2015) Plant traits and their effect on fire and decomposition. Dissertation, Macquarie University North Ryde, Sydney 

- Grothendieck G (2017) sqldf: Manipulate R Data Frames Using SQL. R package version 0.4-11. https://CRAN.R-project. org/package=sqldf 

- Gucker CL, Zouhar K, Smith JK, Stone KR (2012) Characteristics of information available on fire and invasive plants in the eastern United States. Fire Ecol 8:57–81. https://doi. org/10.4996/fireecology.0802057 

- Harpe SE (2015) How to analyze Likert and other rating scale data. Curr Pharm Teach Learn 7:836–850. https://doi.org/ 10.1016/j.cptl.2015.08.001 

- He S, Yin L, Wen J, Liang Y (2018) A test of the Australian weed risk assessment system in China. Biol Invasions 20:2061–2076. https://doi.org/10.1007/s10530-018-16809 

- Imada CT (2019) Hawaiian naturalized vascular plant checklist. Bishop Museum Tech Rep 69 

- Jardine E (2017) Global relationships between plant functional traits and environment in grasslands. Doctoral dissertation, University of Sheffield. 

- Jaureguiberry P, Bertone G, Diaz S (2011) Device for the standard measurement of shoot flammability in the field. Austral Ecol 36:821–829. https://doi.org/10.1111/j.14429993.2010.02222.x 

- Jepson Flora Project (eds.) (2021) Jepson eFlora. https://ucjeps. berkeley.edu/eflora/ 

- Josse J, Prost N, Scornet E, Varoquaux G (2019) On the consistency of supervised learning with missing values. arXiv: 1902.06931 

- Kattge J, Bo¨nisch G, Dı´az S, Lavorel S, Prentice IC, Leadley P, Tautenhahn S, Werner G et al (2020) TRY plant trait database - enhanced coverage and open access. Global Change Biol 26:119–188. https://doi.org/10.1111/gcb. 14904 

- Keil DJ (2006) Cirsium. In: Flora of North America Editorial Committee (eds) Flora of North America. Volume 19 Magnoliophyta Asteraceae, Part 1. Oxford University Press, New York 

- Kuhn M (2020) caret: Classification and Regression Training. R package version 6.0–86. https://CRAN.R-project.org/ package=caret 

- Liaw A, Wiener M (2002) Classification and Regression by randomForest. R News 2:18–22 

123 

588 

K. Faccenda, C. C. Daehler 

- Link SO, Keeler CW, Hill RW, Hagen E (2006) Bromus tectorum cover mapping and fire risk. Int J Wildland Fire 15:113–119. https://doi.org/10.1071/WF05001 

- Lockwood JL, Simberloff D, McKinney ML, Von Holle B (2001) How many, and which, plants will invade natural areas? Biol Invasions 3:1–8. https://doi.org/10.1023/A: 1011412820174 

- Macdonald IAW (1983) Alien trees, shrubs and creepers invading indigenous vegetation in the Hluhluwe-Umfolozi Game Reserve Complex in Natal. Bothalia 14:949–959. https://doi.org/10.4102/abc.v14i3/4.1268 

- Mack RN (1996) Predicting the identity and fate of plant invaders: Emergent and emerging approaches. Biol Conserv 78(1–2):107–121. https://doi.org/10.1016/0006-3207(96) 00021-3 

- Madrigal J, Hernando C, Guijarro M (2013) A new bench-scale methodology for evaluating the flammability of live forest fuels. J Fire Sci 31:131–142. https://doi.org/10.1177/ 0734904112458244 

- McClay A, Sissons A, Wilson C, Davis S (2010) Evaluation of the Australian weed risk assessment system for the prediction of plant invasiveness in Canada. Biol Invasions 12:4085–4098. https://doi.org/10.1007/s10530-010-98193 

- Morais M, Marchante E, Marchante H (2017) Big troubles are already here: risk assessment protocol shows high risk of many alien plants present in Portugal. J Nat Conserv 35:1–12. https://doi.org/10.1016/j.jnc.2016.11.001 

- Motooka P, Castro L, Nelson D, Nagai G, Ching L (2003) Weeds of Hawaii’s pastures and natural areas: an identification and management guide College of Tropical Agriculture and Human Resources. University of Hawai<sup>0</sup> i at Manoa, Honolulu 

- Mutch RW (1970) Wildland fires and ecosystems–a hypothesis. Ecology 51:1046–1051. https://doi.org/10.2307/1933631 

- Oppenheimer H (2019) New Hawaiian plant records for 2018. Bishop Museum Occas Pap 126:3–9 

- Pheloung PC, Williams PA, Halloy SR (1999) A weed risk assessment model for use as a biosecurity tool evaluating plant introductions. J Environ Manag 57:239–251. https:// doi.org/10.1006/jema.1999.0297 

- POWO (2021) Plants of the World Online. Facilitated by the Royal Botanic Gardens, Kew. http://www. plantsoftheworldonline.org/ 

- R Core Team (2021) R: A language and environment for statistical computing. R Foundation for Statistical Computing. https://www.R-project.org 

- Reichard SH, Hamilton CW (1997) Predicting invasions of woody plants introduced into North America. Conserv Biol 11:193–203. https://doi.org/10.1046/j.1523-1739.1997. 95473.x 

- Reid CE, Brauer M, Johnston FH, Jerrett M, Balmes JR, Elliott CT (2016) Critical review of health impacts of wildfire smoke exposure. Environ Health Perspect 124:1334–1343. https://doi.org/10.1289/ehp.1409277 

- Riutta T, Slade EM, Bebber DP, Taylor ME, Malhi Y, Riordan P, Macdonald DW, Morecroft MD (2012) Experimental evidence for the interacting effects of forest edge, moisture and soil macrofauna on leaf litter decomposition. Soil Biol Biochem 49:124–131. https://doi.org/10.1016/j.soilbio. 2012.02.028 

- Santacruz-Garcı´a AC, Bravo S, del Corro F, Ojeda F (2019) A comparative assessment of plant flammability through a functional approach: the case of woody species from Argentine Chaco region. Austral Ecol 44:1416–1429. https://doi.org/10.1111/aec.12815 

- Schwilk DW (2015) Dimensions of plant flammability. New Phytol 206:486–488. https://doi.org/10.1111/nph.13372 

- Scott JK, Panetta FD (1993) Predicting the Australian weed status of southern African plants. J Biogeogr 20:87–93. https://doi.org/10.2307/2845742 

- Seebens H et al (2017) No saturation in the accumulation of alien species worldwide. Nat Commun 8:1–9. https://doi. org/10.1038/ncomms14435 

- Seebens H, Bacher S, Blackburn TM, Capinha C, Dawson W, Dullinger S, Genovesi P, Hulme PE, van Kleunen M, Ku¨hn I, Jeschke JM, Lenzner B, Liebhold AM, Pattison Z, Pergl J, Pysek P, Winter M, Essl F (2021) Projecting the continental accumulation of alien species through to 2050. Global Change Biol 27:970–982. https://doi.org/10.1111/ gcb.15333 

- Settele JR, Scholes R, Betts RA, Bunn S, Leadley P, Nepstad D, Overpeck JT, Taboada MA et al (2014) Terrestrial and inland water systems. In: Field CB, Barros VR, Dokken DJ, Mach KJ, Mastrandrea MD, Bilir TE, Chatterjee M, Ebi KL, Estrada YO, Genova RC, Girma B, Kissel ES, Levy AN, MacCracken S, Mastrandrea PR, White LL (eds) Climate change 2014: impacts, adaptation, and vulnerability. Part A: Global and sectoral aspects. Contribution of working group II to the fifth assessment report of the intergovernmental panel on climate change. Cambridge University Press, Cambridge, United Kingdom and New York, NY, USA, pp 271–359. https://doi.org/10.1017/ CBO9781107415379 

- Shakesby RA (2011) Post-wildfire soil erosion in the Mediterranean: review and future research directions. Earth-Sci Rev 105:71–100. https://doi.org/10.1016/j.earscirev.2011. 01.001 

- Simpson KJ, Ripley BS, Christin PA, Belcher CM, Lehmann CE, Thomas GH, Osborne CP (2016) Determinants of flammability in savanna grass species. J Ecol 104:138–148. https://doi.org/10.1111/1365-2745.12503 

- Smith CW, Tunison JT (1992) Fire and alien plants in Hawaii: research and management implications for native ecosystems. In: Alien plant invasions in native ecosystems of Hawaii: management and research. Cooperative National Park Resources Studies Unit, Honolulu, pp 394–408 

- Strobl C, Boulesteix A, Kneib T, Augustin T, Zeileis A (2008) Conditional variable importance for random forests. BMC Bioinform 9:307. https://doi.org/10.1186/1471-2105-9307 

- Strobl C, Hothorn T, Zeileis A (2009) Party on! The R Journal 1:14–17 

- Te Beest M, Cromsigt JP, Ngobese J, Olff H (2012) Managing invasions at the cost of native habitat? An experimental test of the impact of fire on the invasion of Chromolaena odorata in a South African savanna. Biol Invasions 14:607–618. https://doi.org/10.1007/s10530-011-0102-z 

- Trauernicht C, Pickett E, Giardina CP, Litton CM, Cordell S, Beavers A (2015) The contemporary scale and context of wildfire in Hawai<sup>0</sup> i. Pacific Sci 69:427–444. https://doi.org/ 10.2984/69.4.1 

123 

589 

A screening system to predict wildfire risk of invasive plants 

- Twala BETH, Jones MC, Hand DJ (2008) Good methods for coping with missing data in decision trees. Pattern Recognit Lett 29:950–956. https://doi.org/10.1016/j. patrec.2008.01.010 

- Wagner WL, Herbst DR, Sohmer SH (1999) Manual of the flowering plants of Hawai<sup>0</sup> i. University of Hawai<sup>0</sup> i Press, Honolulu, Hawaii 

- Weber J, Panetta FD, Virtue J, Pheloung P (2009) An analysis of assessment outcomes from eight years’ operation of the Australian border weed risk assessment system. J Environ Manag 90:798–807. https://doi.org/10.1016/j.jenvman. 2008.01.012 

- WFO (2021) World Flora Online. http://www.worldfloraonline. org 

- White RH, Zipperer WC (2010) Testing and classification of individual plants for fire behaviour: plant selection for the wildland–urban interface. Int J Wildland Fire 19:213–227. https://doi.org/10.1071/WF07128 

- Wickham H (2016) ggplot2: elegant graphics for data analysis. Springer-Verlag, New York 

- Williams AP, Abatzoglou JT, Gershunov A, Guzman-Morales J, Bishop DA, Balch JK, Lettenmaier DP (2019) Observed impacts of anthropogenic climate change on wildfire in California. Earth’s Future 7:892–910. https://doi.org/10. 1029/2019EF001210 

- Wu ZY, Raven PH, (eds.) (1994?). Flora of China. Science Press, Beijing; Missouri Botanical Garden Press, St. Louis 

- Wyse SV, Perry GL, O’Connell DM, Holland PS, Wright MJ, Hosted CL, Whitelock SL, Geary IJ, Maurin KJ, Curran TJ (2016) A quantitative assessment of shoot flammability for 60 tree and shrub species supports rankings based on expert opinion. Int J Wildland Fire 25:466–477. https://doi.org/ 10.1071/WF15047 

- Wyse SV, Perry GL, Curran TJ (2018) Shoot-level flammability of species mixtures is driven by the most flammable species: implications for vegetation-fire feedback favouring invasive species. Ecosystems 2:886–900. https://doi.org/ 10.1007/s10021-017-0195-z 

- Zouhar K (2001) Cirsium arvense. In: Fire Effects Information System, [Online]. U.S. Department of Agriculture, Forest Service, Rocky Mountain Research Station, Fire Sciences Laboratory (Producer). https://www.fs.fed.us/database/ feis/plants/forb/cirarv/all.html. Accessed 15 Mar 2021 

Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

123 


