---
title: Spatiotemporal prediction of wildfire size extremes with Bayesian finite sample maxima
authors:
- Joseph, Maxwell B.
- Rossi, Matthew W.
- Mietkiewicz, Nathan P.
- Mahood, Adam L.
- Cattau, Megan E.
- St. Denis, Lise Ann
- Nagy, R. Chelsea
- Iglesias, Virginia
- Abatzoglou, John T.
- Balch, Jennifer K.
year: '2019'
journal: Ecological Applications
doi: 10.1002/eap.1898
tags:
- climate
- climate change
- extremes
- fire
- modeling
- spatiotemporal
- wildfire
zotero_key: EAPHMP5T
item_type: journalArticle
url: https://onlinelibrary.wiley.com/doi/abs/10.1002/eap.1898
source_url: 'unpaywall: https://www.biorxiv.org/content/biorxiv/early/2019/02/16/384115.full.pdf'
fulltext_status: fulltext
synced: '2026-11-06'
---

# Spatiotemporal prediction of wildfire size extremes with Bayesian finite sample maxima

## Abstract

Wildfires are becoming more frequent in parts of the globe, but predicting where and when wildfires occur remains difficult. To predict wildfire extremes across the contiguous United States, we integrate a 30-yr wildfire record with meteorological and housing data in spatiotemporal Bayesian statistical models with spatially varying nonlinear effects. We compared different distributions for the number and sizes of large fires to generate a posterior predictive distribution based on finite sample maxima for extreme events (the largest fires over bounded spatiotemporal domains). A zero-inflated negative binomial model for fire counts and a lognormal model for burned areas provided the best performance. This model attains 99% interval coverage for the number of fires and 93% coverage for fire sizes over a six year withheld data set. Dryness and air temperature strongly predict extreme wildfire probabilities. Housing density has a hump-shaped relationship with fire occurrence, with more fires occurring at intermediate housing densities. Statistically, these drivers affect the chance of an extreme wildfire in two ways: by altering fire size distributions, and by altering fire frequency, which influences sampling from the tails of fire size distributions. We conclude that recent extremes should not be surprising, and that the contiguous United States may be on the verge of even larger wildfire extremes.

## Full text

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

# Spatiotemporal prediction of wildfire extremes with Bayesian finite sample maxima 

Maxwell B. Joseph<sup>∗1</sup> , Matthew W. Rossi<sup>1</sup> , Nathan P. Mietkiewicz<sup>1</sup> , Adam L. Mahood<sup>1</sup> , Megan E. Cattau<sup>1</sup> , Lise Ann St. Denis<sup>1</sup> , R. Chelsea Nagy<sup>1</sup> , Virginia Iglesias<sup>1</sup> , John T. Abatzoglou<sup>2</sup> , and Jennifer K. Balch<sup>1</sup> 

> 1Earth Lab, University of Colorado Boulder 

> 2Department of Geography, University of Idaho 

##### **Abstract** 

Wildfires are becoming more frequent in parts of the globe, but predicting where and when wildfires occur remains difficult. To predict wildfire extremes across the contiguous United States, we integrate a 30 year wildfire record with meteorological and housing data in spatiotemporal Bayesian statistical models with spatially varying nonlinear effects. We compared different distributions for the number and sizes of large fires to generate a posterior predictive distribution based on finite sample maxima for extreme events (the largest fires over bounded spatiotemporal domains). A zero-inflated negative binomial model for fire counts and a lognormal model for burned areas provided the best performance. This model attains 99% interval coverage for the number of fires and 93% coverage for fire sizes over a six year withheld data set. Dryness and air temperature strongly predict extreme wildfire probabilities. Housing density has a hump-shaped relationship with fire occurrence, with more fires occurring at intermediate housing densities. Statistically, these drivers affect the chance of an extreme wildfire in two ways: by altering fire size distributions, and by altering fire frequency, which influences sampling from the tails of fire size distributions. We conclude that recent extremes should not be surprising, and that the contiguous United States may be on the verge of even larger wildfire extremes. 

> ∗maxwell.b.joseph@colorado.edu 

1 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

**Key words** : fire; wildfire; Bayesian; spatiotemporal; extremes; climate. 

- 1 

## **Introduction** 

- 2 Wildfire frequency and burned area has increased over the past couple decades in the 

- 3 United States (Dennison et al. 2014; Westerling 2016), and elsewhere (Krawchuk et al. 

- 4 2009; Pechony and Shindell 2010). In addition to the ecological and smoke impacts associ- 

- 5 ated with increased burned area, there has been an increasing interest in extreme wildfires 

- 6 (Williams 2013) given their impact on human lives and infrastructure (Kochi et al. 2010; 

- 7 Diaz 2012). While case studies of particular extremes provide insight into what caused 

- 8 past events (Peterson et al. 2015; Nauslar, Abatzoglou, and Marsh 2018), predictions of 

- 9 future extremes at a national level could inform disaster related resource allocation. The 

- 10 term “extreme” has multiple meanings with respect to wildfires (Tedim et al. 2018), and 

- 11 in this paper we take consider an extreme wildfire to be a fire with the largest burned area 

- 12 over a bounded spatiotemporal domain, i.e., the block maximum within a spatial region 

- 13 and a temporal interval (Coles et al. 2001). For example, the block maxima for widlfires 

- 14 across the contiguous U.S. can be defined on a yearly basis (Figure 1). 

- 15 Factors driving wildfire extremes vary in space and time (Barbero et al. 2014), but it is 

- 16 unclear how best to account for this in a predictive model. Previous efforts have used year 

- 17 or region-specific models, aggregating over space or time (Bermudez et al. 2009), tempo- 

- 18 rally or spatially explicit models (Mendes et al. 2010), and spatial models with year as a 

- 19 covariate (Díaz-Avalos, Juan, and Serra-Saurina 2016). Recently, rich spatiotemporal mod- 

- 20 els have been described with linear, spatially constant covariate effects (Serra, Saez, Juan, 

- 21 et al. 2014; Serra, Saez, Mateu, et al. 2014). However, linear, spatially constant effects 

- 22 are suboptimal over large spatial domains with nonlinear drivers (Fosberg 1978, Goodrick 

- 23 (2002), Preisler et al. (2004); Preisler and Westerling 2007; Balshi et al. 2009; Krawchuk et 

- 24 al. 2009; Pechony and Shindell 2009; Vilar et al. 2010; Woolford et al. 2011; Woolford et 25 al. 2014). For example, global wildfire probability shows a hump-shaped relationship with 26 temperature and moisture (Moritz et al. 2012). Interactions among drivers also impose 

2/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

- 27 nonlinearity, e.g., in hot and dry climates fires are fuel limited (McLaughlin and Bowers 

- 28 1982), but in cold and wet climates fires are energy limited (Krawchuk and Moritz 2011). 

- 29 Prediction is also complicated by uncertainty in which distribution(s) to use to assign 

- 30 probabilities to extreme events. The generalized Pareto distribution (GPD) has frequently 

- 31 been used (Bermudez et al. 2009; Jiang and Zhuang 2011), but the GPD requires a thresh- 

- 32 old to delineate extreme events (Davison and Smith 1990, Coles (2014)). The utility and 

- 33 validity of a threshold for extremes in a heterogeneous region is debatable (Tedim et al. 

- 34 2018). Recently proposed metastatistical extreme value (MEV) approaches do not require 

- 35 such a threshold, and are based on the statistical distribution of finite sample maxima, i.e., 

- 36 the probability distribution of the maximum value for a finite number of events (Marani 

- 37 and Ignaccolo 2015; Zorzetto, Botter, and Marani 2016). In the MEV framework, the oc38 currence and size of future events, and the parameters of their distributions are treated 39 as random variables which together imply a distribution for extremes. This approach has 

- 40 roots in compound distributions (Dubey 1970; Wiitala 1999), doubly stochastic processes 

- 41 (Cox and Isham 1980), superstatistics (Beck and Cohen 2003), and the Bayesian posterior 

- 42 predictive distribution (Gelman et al. 2013). The link to Bayesian inference is particularly 

- 43 useful, as it provides an easy way to propagate uncertainty forward to to predictions of 44 extremes (Coles, Pericchi, and Sisson 2003). 

- 45 Here, we extend the finite sample maximum approach to account for non-linear, spatially 

- 46 varying covariate effects with the goal of predicting extreme wildfire events from a sta- 

- 47 tistical perspective across the contiguous United States. Specifically, we aim to predict 48 occurrence (where and when), and magnitude (burned area) of large wildfires at a monthly 

- 49 time scale and regional spatial scale across the contiguous United States. 

3/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

## 50 **Methods** 

###### 51 

### **Data description** 

- 52 We acquired wildfire event data for the contiguous United States from the Monitoring 

- 53 Trends in Burn Severity (MTBS, www.mtbs.gov) program (Eidenshink et al. 2007), which 

- 54 includes spatiotemporal information on the occurrence of wildfires in the United States 55 from 1984 to 2016. The MTBS data contain fires greater than 1000 acres ( _≈_ 405 hectares) 56 in the western U.S. and greater than 500 acres ( _≈_ 202 hectares) in the eastern U.S. For 57 consistency across the U.S., we discarded all records in the MTBS data less than 1000 

- 58 acres, retaining 10,736 fire events (Figure 2A). Each event in the MTBS data has a discov59 ery date, spatial point location, and final size. 

- 60 To explain fire size and occurrence, we used a combination of meteorological variables in61 cluding humidity, air temperature, precipitation, and wind speed. These variables were 62 selected on the basis of previous work, and also with an aim to drive a predictive model 

- 63 with interpretable meteorological quantities. Meteorological layers were acquired from the 

- 64 gridMET data (Abatzoglou 2013) that blends monthly high-spatial resolution (~4-km) 65 climate data from the Parameter-elevation Relationships on Independent Slopes Model 

- 66 (Daly et al. 2008) with high-temporal resolution (hourly) data from the National Land 

- 67 Data Assimilation System (NLDAS2) using climatologically aided interpolation. The resul68 tant products are a suite of surface meteorological variables summarized at the daily time 69 step and at a 4-km pixel resolution. Daily total precipitation, minimum relative humidity, 70 mean wind speed, and maximum air temperature were averaged at a monthly time step for 71 each of 84 Environmental Protection Agency level 3 (L3) ecoregions for each month from 

- 72 1984 to 2016 (Omernik 1987; Omernik and Griffith 2014). We also computed cumulative 

- 73 monthly precipitation over the previous 12 months for each ecoregion-month combina- 

- 74 tion. We chose to segment the U.S. with level 3 ecoregions as a compromise between the 75 more numerous (computationally demanding) level 4 ecoregions, and the coarser level 2 76 ecoregions. 

4/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

- 77 We used publicly available housing density estimates that were generated based on the 

- 78 U.S. 2000 decennial census as explanatory variables that may relate to human ignition 79 pressure (Radeloff et al. 2010). These are provided at decadal time steps, and spatially 

- 80 at the level of census partial block groups. To generate approximate measures of hous- 

- 81 ing density at monthly time intervals, we used a simple linear interpolation over time for 82 each block group, then aggregated spatially across block groups to compute mean housing 83 density for each ecoregion in each month. 

###### 84 

### **Model development** 

- 85 We built two types of models: one describing the occurrence of fires within each L3 ecore86 gion over time (i.e., the total number of fires occurring in each ecoregion for each month 87 from 1984 - 2016), and another describing the size of each wildfire in each ecoregion and 88 month. For occurrence models, the response variable was a count (number of fires), and 89 for burned area models, the response was a continuous positive quantity (size of each fire 90 event). We used the period from 1984 to 2009 for training, witholding the period from 91 2010 to 2016 to evaluate predictive performance. 

###### 92 

#### **Fire occurrence** 

- 93 We constructed four models for fire occurrence and compared their predictive performance 94 based on test-set log likelihood and posterior predictive checks for the proportion of zeros, 95 maximum count, and total count. The models differed in the distributions used in the like- 

- 96 lihood, representing counts as a Poisson, negative binomial, zero-inflated Poisson, or zero- 

- 97 inflated negative binomial random variable. The Poisson distribution is a common choice 

- 98 for counts, and the negative binomial distribution provides an alternative that can account 

- 99 for overdispersion. The zero-inflated versions of these distributions include a component 

- 100 to represent extra zeros, which might be expected to work well if there are independent 

- 101 processes that determine whether nonzero counts are possible (Lambert 1992). 

- 102 For spatial units (ecoregions) _s_ = 1 _, ..., S_ and time steps (months) _t_ = 1 _, ..., T_ , each 

5/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

103 model defines a probability mass function for _ns,t_ : the number of fires over 405 hectares in 104 ecoregion _s_ and time step _t_ . For each of the four count distributions under consideration, 105 location parameters _µs,t_ and (for zero-inflated models) structural zero inflation parameters 106 _πs,t_ were allowed to vary in space and time. We used a log link function to ensure that 107 _µs,t >_ 0, and a logit link function to ensure that _πs,t ∈_ (0 _,_ 1). Concatenating over spatial 108 and temporal units, so that **_µ_** = ( _µs_ =1 _,t_ =1 _, µs_ =2 _,t_ =1 _, ..., µs_ = _S,t_ =1 _, µs_ = _S,t_ =2 _, ..., µs_ = _S,t_ = _T_ ), and 109 similarly for **_π_** , we modeled location and (when applicable) zero inflation parameters as: 



<!-- Start of picture text -->
log( µ ) =  α ( µ ) +  X β ( µ ) +  φ ( µ ) + log( a ) ,<br><!-- End of picture text -->



<!-- Start of picture text -->
logit( π ) =  α ( π ) +  X β ( π ) +  φ ( π ) ,<br><!-- End of picture text -->

110 where _α_<sup>(</sup><sup>_µ_)</sup> and _α_<sup>(</sup><sup>_π_)</sup> are scalar intercept parameters, **X** is a known ( _S × T_ ) _× p_ design matrix, 111 where _p_ is the number of input features, **_β_**<sup>(</sup><sup>_µ_)</sup> and **_β_**<sup>(</sup><sup>_π_)</sup> are column vector parameters of 112 length _p_ , **_φ_**<sup>(</sup><sup>_µ_)</sup> and **_φ_**<sup>(</sup><sup>_π_)</sup> are column vector parameters of length _S × T_ containing spatiotem113 poral adjustments, and **_a_** is a known offset vector of areas for spatial unit _s_ = 1 _,_ 2 _, ..., S_ , 114 repeated _T_ times. 

115 

#### **Burned area** 

- 116 We developed five candidate models for fire size, each of which specified a different distri117 bution for the size (burned area) of individual fire events (Reed and McKelvey 2002; Her118 nandez et al. 2015), including the generalized Pareto (Hosking and Wallis 1987), tapered 119 Pareto (Schoenberg, Peng, and Woods 2003), lognormal, gamma, and Weibull distribu- 

- 120 tions. We evaluated each model in terms of test set log likelihood, and posterior predictive 121 checks for fire size extremes. We defined the response _yi_ as the number of hectares burned 122 over 405 for the _i_<sup>_th_</sup> fire event, which occurred in spatial unit _si_ and time step _ti_ . 

- 123 Because each burned area distribution has a different parameterization, we included 

- 124 covariate effects in a distribution-specific way. For the generalized Pareto distribution 

6/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

125 (GPD), we assumed a positive shape parameter, leading to a Lomax distribution for ex126 ceedances (Bermudez et al. 2009). The GPD and Lomax shape parameters are related by 127 _κ_<sup>(</sup><sup>_GPD_)</sup> = 1 _/κ_<sup>(</sup><sup>_L_)</sup> , and the GPD scale parameter is related to the Lomax scale and shape 128 parameters by _σ_<sup>(</sup><sup>_GPD_)</sup> = _σ_<sup>(</sup><sup>_L_)</sup> _/κ_<sup>(</sup><sup>_L_)</sup> . We introduced covariate dependence via the Lomax 129 scale parameter using a log link. For event _i_ , log( _σi_<sup>(</sup><sup>_L_)</sup> ) = _α_ + **_X_** ( _si,ti_ ) **_β_** + _φsi,ti_ , where _α_ is 130 an intercept parameter, **_β_** is a length _p_ vector of coefficients, **_X_** ( _si,ti_ ) is a row vector from 131 **X** , and _φsi,ti_ is a spatiotemporal adjustment for _si_ and _ti_ . For the tapered Pareto model, 132 we modeled the shape parameter as log( _κi_ ) = _α_ + **_X_** ( _si,ti_ ) **_β_** + _φsi,ti_ . The lognormal model 133 included covariate dependence via the location parameter: _µi_ = _α_ + **_X_** ( _si,ti_ ) **_β_** + _φsi,ti_ . The 134 gamma model used a log link for the expected value: log( _E_ ( _yi_ )) = _α_ + **_X_** ( _si,ti_ ) **_β_** + _φsi,ti_ . Last, 135 we modeled the Weibull scale parameter as log( _σi_ ) = _α_ + **_X_** ( _si,ti_ ) **_β_** + _φsi,ti_ . More detail on 136 the parameterization of each burned area distribution is provided in the Appendices. 

137 

#### **Accounting for nonlinear forcing** 

138 The design matrix **X** was constructed to allow for spatially varying nonlinear effects of 139 housing density and meteorological drivers. We used B-splines to account for nonlinearity 140 (Figure 3) and allowed the coefficients for each basis vector to vary spatially (Wood 2017). 141 First, we constructed univariate B-splines for log housing density, wind speed, same month 142 precipitation, previous 12 month precipitation, air temperature, and humidity, with five 143 degrees of freedom (including an intercept) for each variable. This step generated 30 basis 144 vectors (five for each of six variables). 

145 To allow for spatial variation in these nonlinear effects, we added interaction effects be146 tween each of the basis vectors and ecoregions (Brezger and Lang 2006; Kneib, Hothorn, 147 and Tutz 2009). The hierarchical nesting of ecoregion designations (Figure 2B-D) lends 148 itself to such interactions. Conceptually, coefficients in a level 3 ecoregion may be related 149 to coefficients in the level 2 ecoregion containing the level 3 region, the level 1 ecoregion 150 containing the level 2 region, and a global effect. The coefficient associated with a basis 151 vector for any level 3 ecoregion is treated as a sum of a global effect, a level 1 ecoregion 152 adjustment, a level 2 ecoregion adjustment, and a level 3 ecogregion adjustment. Thus, 

7/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

153 for every univariate basis vector, we included interaction effects with ecoregion at each of 154 the three ecoregion levels. This allows borrowing of information across space (level 3 ecore155 gions in a level 2 ecoregion are often adjacent), and for regions that are ecologically similar. 156 We also included adjustments on the global intercept for each level 1, 2, and 3 ecoregion to 157 account for spatial variation that is unrelated to climate or housing density. This specifica158 tion induces sparsity in **X** that we exploit to increase the efficiency of computing **_µ_** and **_π_** . 159 In total, **X** has _p_ = 3,472 columns, with 97% zero entries. 

###### 160 

### **Prior specification** 

161 To avoid overfitting, we used a regularized horseshoe prior on the coefficients associated 162 with the spatially varying nonlinear effects described above (Piironen, Vehtari, and others 163 2017). This prior places high probability close to zero, while retaining heavy enough tails 164 that nonzero coefficients are not shrunk too strongly toward zero. This is consistent with 165 our prior expectation that most of the coefficients associated with the columns in **X** were 166 close to zero. For the zero inflated count models, we used a multivariate horseshoe to allow 167 information sharing between the zero inflated and distribution specific location parameters 168 (Peltola et al. 2014). For the remaining count models and all burned area models, this 169 was a univariate horseshoe prior. Spatiotemporal random effects were constructed using 170 a temporally autoregressive, spatially intrinsically autoregressive formulation (Besag and 171 Kooperberg 1995; Banerjee, Carlin, and Gelfand 2014). Details of these priors and the 172 resulting joint distributions are provided in the Appendices. 

###### 173 

### **Posterior predictive inference for finite sample maxima** 

174 We used the posterior predictive distribution to check each model and make inference on 175 extremes. The posterior predictive distribution provides a distribution for replications 176 of observed data ( _y_<sup>rep</sup> ), and predictions of future data (Gelman et al. 2013). Concep177 tually, for a good model, _y_<sup>rep</sup> should be similar to observed training data _y_ , and future 178 predictions should be similar to future data. Distributions over both quantities can be 

8/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

- 179 obtained by conditioning on _y_ and marginalizing over model parameters _θ_ , e.g., [ _y_<sup>rep</sup> _|y_ ] = 

180 � [ _y_ rep _|θ_ ][ _θ|y_ ] _dθ_ . 

181 Posterior predictive distributions facilitate model checks that compare predicted and ob182 served test statistics (Gelman, Meng, and Stern 1996). To evaluate whether models cap183 tured tail behavior, we compared empirical maxima ( _T_ ( _y_ ) = max( _y_ )) to the predicted 184 distribution of maxima _T_ ( _y_<sup>rep</sup> ). We also include predictive checks for the proportion of 185 zero counts, and totals for count and burned area models. Posterior predictive inference 186 for finite sample maxima is similar in spirit to the MEV approach. Both obtain a distri187 bution over maxima by marginalizing over unknowns including the number of events, size 188 of each event, and parameters of their distributions (Marani and Ignaccolo 2015). How189 ever, a Bayesian approach explicitly conditions on the observed data to obtain a posterior 190 distribution of parameters. 

191 Seeing this connection is useful in the context of including priors and propagating uncer192 tainty to derived parameters. For any ecoregion _s_ and timestep _t_ , if we define a particular 193 maximum fire size conditional on a fire having occurred as _zs,t_ , and let _Zs,t_ represent the 194 random variable of maximum fire size, then the cumulative distribution function (CDF) 195 for _zs,t_ is given by Pr( _Zs,t ≤ zs,t_ ) = F( _y_ ( _s,t_ ))<sup>_ns,t_</sup> , where F( _y_ ( _s,t_ )) is the CDF of fire size, and 196 _ns,t_ is the number of wildfire events. Thus, Pr( _Zs,t ≤ zs,t_ ) is the distribution function for 197 the finite sample maximum. The CDF for _zs,t_ can be inverted to produce a quantile func198 tion that permits computation of prediction intervals for maximum fire sizes, conditional 199 on fires having occurred. Given a collection of posterior draws from a burned area model 200 that parameterize F( _y_ ( _s,t_ )), and a collection of posterior draws of _n_<sup>rep</sup> _s,t_<sup>fromtheposterior</sup> 201 predictive distribution of a wildfire count model, a posterior distribution for the CDF or 202 quantile function of maximum fire size can be generated which combines the two models 203 to facilitate inference on the distribution of extremes. 

9/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

###### 204 

### **Parameter estimation** 

205 We used a combination of variational approximations and Hamiltonian Monte Carlo meth206 ods to sample from the posterior distributions of count and burned area models. A varia207 tional approximation (Kucukelbir et al. 2015) was used for count models to quickly iden208 tify a preferred model. The best performing count model and all burned area models were 209 fit using the No-U-Turn Sampler (Hoffman and Gelman 2014). Models were fit in the Stan 210 probabilistic programming language using the `rstan` package (Carpenter et al. 2016; Stan 211 Development Team 2018). We ran four chains for 1000 iterations each, discarding the first 212 500 iterations as warmup. Convergence was assessed using visual inspection of trace plots, 213 with potential scale reduction statistic values _R_<sup>ˆ</sup> _≥_ 1 _._ 1 as an indicator convergence failure 214 (Brooks and Gelman 1998). 

###### 215 

### **Implementation** 

216 All data processing, model fitting, and visualization were implemented with open source 217 software, primarily in the R programming language (R Core Team 2017), and wrapped in 218 a reproducible workflow via GNU Make and Docker (Stallman, McGrath, and Smith 2004; 219 Boettiger 2015). Data cleaning and transformation required the R packages assertthat 220 (Wickham 2017a), lubridate (Grolemund and Wickham 2011), Matrix (Bates and Maech221 ler 2018), pbapply (Solymos and Zawadzki 2018), splines (R Core Team 2018), tidyverse 222 (Wickham 2017b), and zoo (Zeileis and Grothendieck 2005). Spatial data were processed 223 with raster (Hijmans 2017), rgdal (Bivand, Keitt, and Rowlingson 2018), sf (Pebesma 224 2018), and spdep (Bivand and Piras 2015). Finally, we used cowplot (Wilke 2017), ggre225 pel (Slowikowski 2018), ggthemes (Arnold 2018), patchwork (Pedersen 2017), and RCol226 orBrewer (Neuwirth 2014) for visualization. The manuscript was written in R Mark227 down (Allaire et al. 2018). Analyses were run on an Amazon Web Services m5.2xlarge 228 EC2 instance with four physical cores and 32 GB of RAM, and the whole workflow re229 quires _≈_ 72 hours. All code to reproduce the analysis is available on GitHub at https: 230 //github.com/mbjoseph/wildfire-extremes (Joseph 2018). 

10/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

###### 231 

## **Results** 

###### 232 

### **Wildfire occurrence** 

- 233 The zero-inflated negative binomial distribution performed best on the held-out test set 234 (Table 1), and was able to recover the proportion of zeros, count maxima, and count to- 

- 235 tals in posterior predictive checks for both the training and test data (Figure 4). All of 236 the other count models that we considered exhibited lack of fit to at least one of these 237 statistics in posterior predictive checks. Hereafter, we report results from the zero-inflated 238 negative binomial model. 

239 Minimum relative humidity and maximum air temperature had the strongest effects on 240 both the zero-inflation component and the expected value of the negative binomial com241 ponent (Figure 5, posterior median for _ρ_ : 0.665, 95% credible interval (CI): 0.319 - 0.861). 242 The model uncovered unique effects of meteorological variables at level 1, 2, and 3 ecore243 gions (Figure 6). For example, a positive interaction effect between the second air temper244 ature basis vector and the L1 Great Plains ecoregions indicates that the expected number 245 of wildfires in plains ecoregions with cold conditions is high relative to other ecoregions. 246 The Ozark/Ouachita-Appalachian forest and Ozark Highlands were also identified as 247 having region-specific temperature effects (Figure 6). Twelve month total precipitation 248 also had region specific effects in the Mississippi Alluvial and Southeast Coastal Plains 249 ecoregion, where it was associated with lower expected fire counts (Figure 6). In contrast, 250 increasing cumulative twelve month precipitation was associated with higher counts in 251 desert ecoregions (Figure 5). Housing density showed a unimodal relationship to expected 252 count (Figure 5), with lower expected counts in sparsely populated ecoregions, and higher 253 expected counts with moderately populated ecoregions. 

254 Posterior 95% credible interval coverage for the number of fires over 405 hectares in the 255 test set was 98.8%. The lowest test set interval coverage was 89.3%, in the Cross Timbers 256 L3 ecoregion. When observed counts fell outside the 95% prediction interval, counts were 257 larger than predicted 100% of the time. The largest difference between observed numbers 

11/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

258 and predicted 97.5% posterior quantiles (the upper limit for the 95% credible interval) oc259 curred for the Columbia Mountains/Northern Rockies L3 ecoregion in August 2015, when 260 36 fires over 405 hectares occurred and at most 22 were predicted. For nearly half of the 261 level 3 ecoregions (43 of 85), accounting for 39.7% of the land area of the contiguous U.S., 262 the zero-inflated negative binomial model had 100% test set prediction interval coverage. 

###### 263 

### **Wildfire burned areas** 

264 The lognormal distribution performed best on the test set (Table 2), and captured tail265 behavior better than other burned area distributions (Figure 7). The GPD model was too 266 heavy-tailed to adequately capture the pattern in the empirical data, predicting fires far 267 larger than those observed in the training and test sets (Figure 7). The tapered Pareto 268 distribution was too light-tailed (Figure 7). The gamma and Weibull models performed 269 very poorly overall on the test set (Table 2), apparently due to a lack of congruence be270 tween the shapes of these distributions and the actual burned area distribution. Despite 271 a poor fit to the bulk of the wildfire burned area distribution, both performed adequately 272 in the upper tails (Figure 7). Hereafter we present results for the lognormal model, which 273 had the highest test set log likelihood and captured tail behavior of the empirical fire size 274 distribution. 

275 Relative humidity was the primary driver of expected burned area for a fire event (Figure 276 8A). The first basis vector for mean daily minimum relative humidity was the only coeffi277 cient with a 95% credible interval that did not include zero (posterior median: 1.68, 95% 278 CI: (0.8 - 2.29)). This nonlinear effect can be observed in Figure 8B as an increase in the 279 expected burned area below 20% mean daily minimum humidity. This leads to a season280 ality gradient among ecoregions of expected fire sizes, with little or no seasonal signal in 281 typically humid ecoregions such as Marine West Coast Forests of the Pacific Northwest, 282 and seasonal oscillations in ecoregions that have periodic fluctuations between dry and hu283 mid conditions such as the Temperate Sierras (Figure 8C). There was not strong evidence 284 that meteorological variables had spatially variable effects on expected wildfire burned 285 area. 

12/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

286 Overall, 95% posterior predictive interval coverage in the test set for burned areas was 287 93%. The lowest test set coverage was 0%, for the Eastern Great Lakes Lowlands L3 ecore288 gion, followed by 50%, for the Central California Valley L3 ecoregion, though these ecore289 gions had just 1 and 2 wildfire events in the test set. When observed fire sizes fell outside 290 the 95% prediction interval, 24.9% of wildfires were smaller than predicted, and 75.1% of 291 wildfires were larger than predicted. The largest discrepancy between the actual size of a 292 wildfire and the predicted 97.5% posterior quantile was observed with the Wallow Fire in 293 2011 which burned 228,107 hectares, but the predicted upper limit for size was 20,756. We 294 investigate this discrepancy further in the case study below. The lognormal burned area 295 model achieved 100% interval coverage in 24 of 67 ecoregions that had wildfire events in 296 the test set, accounting for 26% of the land area of the contiguous U.S. 

###### 297 

### **Inference on extremes** 

298 By combining the output of the event count and burned area models, we derived pos299 terior prediction intervals for the size of the largest fire in a month for each region (the 300 “burned area maximum”), integrating over uncertainty in the number of fires, as well as 301 the lognormal mean and standard deviation for burned area. We evaluated the posterior 302 distribution for the quantile function of the finite sample maximum of a lognormal distri303 bution (exp( _µ_ + _σ_ _~~√~~_ 2erf<sup>_−_1</sup> (2 _P_<sup>1</sup><sup>_/n_</sup> _−_ 1)), where _n_ is the number of wildfire events, erf<sup>_−_1</sup> is 304 the inverse error function, and _P_ is a probability) to generate prediction intervals for maxi305 mum fire sizes by month and ecoregion, conditional on one or more fires having occurred. 306 In the holdout period from 2010 to 2016, a 99% prediction interval achieved 77.4% interval 307 coverage, with 14.8% of the burned area maxima (140 fire events) being larger than pre308 dicted (Figure 9). As an additional check, we used the posterior distribution of the model 309 to predict the total area burned by wildfires in the test set. The model predicted the total 310 area burned over the entire contiguous United States in test period from 2010 to 2016 to 311 be 30,339,123 (95% CI: (20,496,551 - 50,446,932) and the actual value was 30,440,173. 

312 While fires over a million acres ( _≈_ 404,686 hectares) in size have happened historically in 313 the contiguous U.S. (Pernin 1971), no such fires were represented in in the training or test 

13/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

314 sets. If we extrapolate, the probability of at least one fire this large in the period from 315 2010 to 2016 was estimated to be between 0.191 and 0.651 (95% CI), with a posterior 316 median of 0.348. The highest probability for such an event was 0.014 (posterior median), 317 with a 95% CI of (0, 0.237) seen for the Southwestern Tablelands ecoregion in June 2011. 318 The second highest probability was 0.004 (posterior median), with a 95% CI of (0, 0.056) 319 seen for the Arizona/New Mexico Mountains ecoregion in June 2011. Aggregating spa320 tially, we estimated monthly probabilities of a million acre wildfire. These probabilities 321 show seasonal signals corresponding to peak fire seasons, with a shift toward higher and 322 broader peaks beginning in the 21st century (Figure 10). 

###### 323 

### **Error analysis case study: the 2011 Wallow Fire** 

324 To better understand how well the model could or could not anticipate notable extreme 325 events, and why, we used the largest fire in the test set as a case study. The Wallow Fire 326 was accidentally ignited on May 29, 2011 by two campers in the L3 Arizona/New Mex327 ico Mountains ecoregion. It burned through the month of June and into early July. The 328 model underpredicted the total burned area of the Wallow Fire. Integrating over uncer329 tainty in the predicted number of fires and expected fire size, the 99% credible interval for 330 the maximum fire size for May 2011 was (730 - 107,419) hectares, but the Wallow Fire is 331 recorded as 228,103 hectares. 

- 332 We evaluated the contribution of each covariate to the linear predictor functions of the 333 three model components (lognormal mean for burned areas, negative binomial mean for 334 counts, and the logit probability of the zero-inflation component) to understand why these 335 predictions differed. We defined the contribution of a variable as the dot product of the 336 elements in the design matrix **X** corresponding to a particular driver variable (e.g., humid337 ity), and the estimated coefficients in **_β_** corresponding to that variable. This provides a 338 quantitative measure of how each input variable contributes to the linear predictor for an 339 ecoregion, and incorporates the overall, level 1, level 2, and level 3 ecoregion adjustments 340 on these effects. Humidity is the primary driver of variation in the model’s predictions 341 overall, and June 2011 - the month after ignition - favored more large fires, with drier, hot- 

14/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

- 342 ter conditions (Figure 11). The 99% credible interval for June 2011 was (4,258 - 428,765) 343 hectares, which contains the true value. Had the Wallow Fire ignited two days later, the 344 true final size would have been contained in the prediction interval. Evidently, conditions 345 in May that drove (under)predictions of maximum burned area were not representative of 346 the conditions over most of the Wallow Fire’s duration. 

347 Temporal mismatch aside, meteorological conditions local to the Wallow Fire differed 348 from the monthly regional means (Figure 12). In particular, wind speeds in the Wallow 349 Fire vicinity exceeded the regional monthly mean values on the date of ignition and in 350 the weeks following ignition. Over the majority of the duration of the Wallow Fire (May 351 29 to July 8), local daily conditions were drier and hotter on average than regional mean 352 monthly conditions in May, which were used to drive the statistical model. This local vari353 ability is not represented in the regional models developed here. The failure of the model 354 to correctly predict the size of the Wallow fire suggests potential avenues for improvement, 355 discussed below. 

###### 356 

## **Discussion** 

- 357 Extreme wildfires are often devastating, but perhaps they need not be surprising. By 358 allowing the non-linear effects of weather and housing density to vary across space, this 359 model achieves good predictive accuracy for fire extremes at a regional scale over a six 

- 360 year prediction window. This model predicts that extremely large wildfires, perhaps even 361 over one million acres (404,686 hectares), have a non-negligible probability of occurrence in 362 the contiguous United States. Such predictions can support regional wildfire management 363 and probabilistic hazard assessment. 

- 364 Driving a model with meteorological features raises challenges related to predictive un365 certainty and covariate shift - a change in the underlying distribution of forcing variables, 

- 366 potentially outside of the historic range. Ideally, this uncertainty would be propagated for- 

- 367 ward in a predictive model, possibly through stacking of predictive distributions that are 368 generated from multiple models of future climate dynamics (Yao et al. 2017). But, even 

15/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

- 369 if one had a perfect forecast, novel conditions present a challenge for predictive modeling 370 (Quionero-Candela et al. 2009). For example, the High Plains ecoregion had its highest 371 mean monthly precipitation, lowest 12 month running precipitation, driest, hottest, and 372 windiest conditions in the test set period. Extrapolating beyond the range of training in373 puts is generally difficult, but the hierarchical spatial effect specification used here allows 374 partial pooling among climatically similar ecoregions that can inform such predictions, 375 unlike models fit separately to disjoint spatial regions. 

376 Similar issues could arise when making predictions for observed but rare meteorologi377 cal conditions. For example, mean daily minimum humidity values over 60% accounted 378 for just 3.76% of the ecoregion-months in the training data, and 0 fires occurred in such 379 months. As a consequence, there is relatively little data that can be used to inform the 380 model for such conditions, and the prior distribution which shrinks coefficients toward 381 zero may dominate the likelihood in the posterior distribution. In this case, the poste382 rior distribution for the last basis coefficient for the partial effect of humidity is likely to 383 be close to zero. This could explain why the estimated partial effect of humidity on the 384 expected counts was less negative at the upper end of the observed humidity range, al385 though previous work has found similarly nonlinear partial effects (Preisler et al. 2004). 386 The count model performed extremely well in this range, with 100% interval coverage for 387 the 299 ecoregion-months with mean daily minimum humidity values greater than 60% 388 in the withheld test data. The model nearly always predicted zero counts with high confi389 dence when conditions were this humid: 298 of 299 predictions made for such conditions 390 were 95% credible intervals of (0, 0). The remaining prediction had a posterior median of 391 zero, along with a 95% credible interval from 0 to 1. Monotonicity constraints could be 392 incorporated into these models via monotonic spline bases (Ramsay and others 1988), or 393 an ordered prior distribution for basis coefficients (Brezger and Steiner 2008). In this case, 394 the count model performs well under humid conditions without monotonicity constraints, 395 and there seems to be little room for performance improvements that might result from 396 such constraints. 

397 Human-caused climate change is expected to increase fire activity in the western U.S. 

16/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

- 398 (Rogers et al. 2011; Westerling et al. 2011; Moritz et al. 2012; Abatzoglou and Williams 399 2016) and elsewhere (Flannigan et al. 2009), but the nonlinear effect of housing density 400 could provide additional insight into future expectations. While housing density is increas401 ing over time in most U.S. ecoregions, some of these ecoregions are in the range of values 402 in which this increases the expected number of large fires, while others are so populated 403 that further increases would reduce the chance of a large fire. The hump-shaped effect of 404 human density on the expected number of large fires is likely driven by ignition pressure 405 and fire suppression (Balch et al. 2017). As human density increases from zero, ignition 406 pressure increases, but eventually landscapes become so urbanized, fragmented, and/or 407 fire-suppressed that wildfire risk decreases (Syphard et al. 2007; Bowman et al. 2011; 408 Bistinas et al. 2013; Knorr et al. 2013; Mcwethy et al. 2013; Syphard et al. 2017; Nagy et 409 al. 2018). At intermediate density, wildfire regimes respond to human ignition and altered 410 fuel distributions (Guyette, Muzika, and Dey 2002), but these responses depend on envi411 ronmental context and characteristics of the human population (Marlon et al. 2008; Li et 

- 412 al. 2009). This model indicates that the combination of moderate to high human density 

- 413 and dry conditions would nonlinearly increase the chance of an extreme fire event. Both 414 human density and dryness are expected to increase in the future across large swaths of 415 the U.S. (Lloyd, Sorichetta, and Tatem 2017; Stavros et al. 2014, Radeloff et al. (2010)), 416 with potential implications for human mortality, health risks from smoke and particulate 417 emission, and the financial burden of wildfire management (Reid et al. 2016; Radeloff et al. 418 2018). 

419 This work points to promising directions for future predictive efforts. Default choices such 420 as Poisson and GPD distributions should be checked against alternative distributions. 421 Further, the predictive skill of this model seems to suggest that ordinary events provide 422 information on extremes, which would not be the case if the generative distribution of 423 extremes was completely unique. Previous case studies have identified that extremes or 424 anomalies in climatological drivers play a role in the evolution of extreme wildfires (Peter425 son et al. 2015), but for this work, monthly averages of climatological drivers over fairly 426 large spatial regions were used, which may smooth over anomalous or extreme conditions. 427 Enhancing the spatiotemporal resolution of predictive models could better represent cli- 

17/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

- 428 matic and social drivers and provide localized insights to inform decision-making. This 

- 429 raises computational challenges, but recent advances in distributed probabilistic computing 430 (Tran et al. 2017), efficient construction of spatiotemporal point processes (Shirota and 431 Banerjee 2018), and compact representations of nonlinear spatial interactions (Lee and 432 Durbán 2011) may provide solutions. 

- 433 The Wallow Fire case study reveals at least one limitation of increasing the spatiotem434 poral resolution. When the model predictions are driven by covariates that are summa435 rized in space and time (e.g. a mean across an ecoregion in a month), summary values 436 may not represent conditions that are most relevant to an event. With a discrete space437 time segmentation, events can occur at the boundary of a spatiotemporal unit, e.g., if 438 a fire spreads into an adjacent ecoregion or ignites on the last day of the month. Large 439 wildfires can span months, and a model that only uses conditions upon ignition to pre440 dict total burned area can fail to account for conditions that change over the course of 441 the event. Modeling ignitions as a point process in continuous space and time (Brillinger, 

- 442 Preisler, and Benoit 2003), and explicitly modeling subsequent fire duration and spread 

- 443 could better separate conditions that ignite fires from those that affect propagation. Such 444 an approach might be amenable to including information on fuel continuity, which is likely 445 to limit the size of extremely large fires and did not factor into the current predictions 446 (Rollins, Morgan, and Swetnam 2002; Hargrove et al. 2000). 

447 To the extent that a model reflects the generative process for extreme events, the decom448 position of contributions to the model’s predictions may provide insight into attribution 449 for meteorological and anthropogenic drivers of extremes. However, a model trained to 450 represent a region-wide distribution of fire sizes will inevitably fail to capture local factors 451 that are relevant to specific events such as the Wallow Fire. If predicting the dynamics 452 of particular fire events is a goal, process-based models designed to model fire spread are 453 likely to be more appropriate than regional statistical models such as those developed 454 here. 

455 This paper presents and evaluates a statistical approach to explain and predict extreme 456 wildfires that incorporates spatially varying non-linear effects. The model reveals consider- 

18/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

457 able differences among ecoregions spanning the mountain west to the great plains, deserts, 458 and eastern forests, and suggests a non-negligible chance of extreme wildfires larger than 459 those seen in over the past 30 years in the contiguous U.S. Predictive approaches such as 460 this can inform decision-making by placing probabilistic bounds on the number of wildfires 461 and their sizes, while provide deeper insights into wildfire ecology. 

###### 462 

## **Acknowledgments** 

463 We thank Mitzi Morris, Kyle Foreman, Daniel Simpson, Bob Carpenter, and Andrew Gel464 man for contributing to the implementation of an intrinsic autoregressive spatial prior 465 in Stan. We also thank two anonymous reviewers for their thoughtful comments, which 466 greatly improved the paper. 

###### 467 

## **Literature cited** 

- 468 Abatzoglou, John T. 2013. “Development of Gridded Surface Meteorological Data for Eco469 logical Applications and Modelling.” _International Journal of Climatology_ 33 (1). Wiley 470 Online Library: 121–31. 

- 471 Abatzoglou, John T., and A. Park Williams. 2016. “Impact of Anthropogenic Climate 472 Change on Wildfire Across Western Us Forests.” _Proceedings of the National Academy of_ 473 _Sciences_ 113 (42). National Academy of Sciences: 11770–5. doi:10.1073/pnas.1607171113. 

- 474 Allaire, JJ, Yihui Xie, Jonathan McPherson, Javier Luraschi, Kevin Ushey, Aron Atkins, 475 Hadley Wickham, Joe Cheng, and Winston Chang. 2018. _Rmarkdown: Dynamic Docu-_ 476 _ments for R_ . https://CRAN.R-project.org/package=rmarkdown. 

- 477 Arnold, Jeffrey B. 2018. _Ggthemes: Extra Themes, Scales and Geoms for ’Ggplot2’_ . https: 478 //CRAN.R-project.org/package=ggthemes. 

- 479 Balch, Jennifer K, Bethany A Bradley, John T Abatzoglou, R Chelsea Nagy, Emily J 

19/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

- 480 Fusco, and Adam L Mahood. 2017. “Human-Started Wildfires Expand the Fire Niche 

- 481 Across the United States.” _Proceedings of the National Academy of Sciences_ 114 (11). Na482 tional Acad Sciences: 2946–51. 

- 483 Balshi, Michael S, A DAVID McGUIRE, Paul Duffy, Mike Flannigan, John Walsh, and 

- 484 Jerry Melillo. 2009. “Assessing the Response of Area Burned to Changing Climate in 

- 485 Western Boreal North America Using a Multivariate Adaptive Regression Splines (Mars) 486 Approach.” _Global Change Biology_ 15 (3). Wiley Online Library: 578–600. 

- 487 Banerjee, Sudipto, Bradley P Carlin, and Alan E Gelfand. 2014. _Hierarchical Modeling_ 488 _and Analysis for Spatial Data_ . CRC Press. 

- 489 Barbero, R, JT Abatzoglou, EA Steel, and Narasimhan K Larkin. 2014. “Modeling Very 490 Large-Fire Occurrences over the Continental United States from Weather and Climate 491 Forcing.” _Environmental Research Letters_ 9 (12). IOP Publishing: 124009. 

- 492 Bates, Douglas, and Martin Maechler. 2018. _Matrix: Sparse and Dense Matrix Classes_ 493 _and Methods_ . https://CRAN.R-project.org/package=Matrix. 

- 494 Beck, Christian, and EGD Cohen. 2003. “Superstatistics.” _Physica A: Statistical Mechan-_ 495 _ics and Its Applications_ 322. Elsevier: 267–75. 

- 496 Bermudez, P de Zea, J Mendes, JMC Pereira, KF Turkman, and MJP Vasconcelos. 2009. 497 “Spatial and Temporal Extremes of Wildfire Sizes in Portugal (1984–2004).” _International_ 498 _Journal of Wildland Fire_ 18 (8). CSIRO Publishing: 983–91. 

- 499 Besag, Julian, and Charles Kooperberg. 1995. “On Conditional and Intrinsic Autoregres500 sions.” _Biometrika_ 82 (4). Oxford University Press: 733–46. 

- 501 Bistinas, Ioannis, Duarte Oom, Ana C. L. Sá, Sandy P. Harrison, I. Colin Prentice, and 

- 502 José M. C. Pereira. 2013. “Relationships between Human Population Density and Burned 503 Area at Continental and Global Scales.” _PLoS ONE_ . doi:10.1371/journal.pone.0081188. 

- 504 Bivand, Roger, and Gianfranco Piras. 2015. “Comparing Implementations of Estimation 505 Methods for Spatial Econometrics.” In. American Statistical Association. 

506 Bivand, Roger, Tim Keitt, and Barry Rowlingson. 2018. _Rgdal: Bindings for the ’Geospa-_ 

20/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

- 507 

   - _tial’ Data Abstraction Library_ . https://CRAN.R-project.org/package=rgdal. 

- 508 Boettiger, Carl. 2015. “An Introduction to Docker for Reproducible Research.” _ACM_ 509 _SIGOPS Operating Systems Review_ 49 (1). ACM: 71–79. 

- 510 Bowman, David MJS, Jennifer Balch, Paulo Artaxo, William J Bond, Mark A Cochrane, 

- 511 Carla M D’antonio, Ruth DeFries, et al. 2011. “The Human Dimension of Fire Regimes on 512 Earth.” _Journal of Biogeography_ 38 (12). Wiley Online Library: 2223–36. 

- 513 Brezger, Andreas, and Stefan Lang. 2006. “Generalized Structured Additive Regression 514 Based on Bayesian P-Splines.” _Computational Statistics & Data Analysis_ 50 (4). Elsevier: 515 967–91. 

- 516 Brezger, Andreas, and Winfried J Steiner. 2008. “Monotonic Regression Based on 

- 517 Bayesian P–Splines: An Application to Estimating Price Response Functions from 

- 518 Store-Level Scanner Data.” _Journal of Business & Economic Statistics_ 26 (1). Taylor & 519 Francis: 90–104. 

- 520 Brillinger, David R, Haiganoush K Preisler, and John W Benoit. 2003. “Risk Assessment: 521 A Forest Fire Example.” _Lecture Notes-Monograph Series_ . JSTOR, 177–96. 

- 522 Brooks, Stephen P, and Andrew Gelman. 1998. “General Methods for Monitoring Conver523 gence of Iterative Simulations.” _Journal of Computational and Graphical Statistics_ 7 (4). 524 Taylor & Francis: 434–55. 

- 525 Carpenter, Bob, Andrew Gelman, Matt Hoffman, Daniel Lee, Ben Goodrich, Michael 

- 526 Betancourt, Michael A Brubaker, Jiqiang Guo, Peter Li, and Allen Riddell. 2016. “Stan: 527 A Probabilistic Programming Language.” _Journal of Statistical Software_ 20: 1–37. 

- 528 Coles, S. 2014. _An Introduction to Statistical Modeling of Extreme Values_ . Springer. https: 529 //books.google.com/books?id=G-D-sgEACAAJ. 

- 530 Coles, Stuart, Joanna Bawa, Lesley Trenner, and Pat Dorazio. 2001. _An Introduction to_ 531 _Statistical Modeling of Extreme Values_ . Vol. 208. Springer. 

- 532 Coles, Stuart, Luis Raúl Pericchi, and Scott Sisson. 2003. “A Fully Probabilistic Approach 

21/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

- 533 to Extreme Rainfall Modeling.” _Journal of Hydrology_ 273 (1-4). Elsevier: 35–50. 

- 534 Cox, David Roxbee, and Valerie Isham. 1980. _Point Processes_ . Vol. 12. CRC Press. 

- 535 Daly, Christopher, Michael Halbleib, Joseph I Smith, Wayne P Gibson, Matthew K 536 Doggett, George H Taylor, Jan Curtis, and Phillip P Pasteris. 2008. “Physiographically 537 Sensitive Mapping of Climatological Temperature and Precipitation Across the Contermi538 nous United States.” _International Journal of Climatology_ 28 (15). Wiley Online Library: 539 2031–64. 

- 540 Davison, Anthony C, and Richard L Smith. 1990. “Models for Exceedances over High 541 Thresholds.” _Journal of the Royal Statistical Society. Series B (Methodological)_ . JSTOR, 542 393–442. 

- 543 Dennison, Philip E, Simon C Brewer, James D Arnold, and Max A Moritz. 2014. “Large 544 Wildfire Trends in the Western United States, 1984–2011.” _Geophysical Research Letters_ 41 545 (8). Wiley Online Library: 2928–33. 

- 546 

   - Diaz, John M. 2012. “Economic Impacts of Wildfire.” _Southern Fire Exchange_ . 

- 547 Díaz-Avalos, Carlos, Pablo Juan, and Laura Serra-Saurina. 2016. “Modeling Fire Size of 548 Wildfires in Castellon (Spain), Using Spatiotemporal Marked Point Processes.” _Forest_ 549 _Ecology and Management_ 381. Elsevier: 360–69. 

- 550 Dubey, Satya D. 1970. “Compound Gamma, Beta and F Distributions.” _Metrika_ 16 (1). 551 Springer: 27–31. 

- 552 Eidenshink, J, B Schwind, K Brewer, ZL Zhu, B Quayle, and S Howard. 2007. “A Project 553 for Monitoring Trends in Burn Severity.” _Nutrition and Cancer_ 58 (1): 28–34. 

- 554 Flannigan, Mike D., Meg A. Krawchuk, William J. de Groot, B. Mike Wotton, and 

- 555 Lynn M. Gowman. 2009. “Implications of Changing Climate for Global Wildland 556 Fire.” Journal Article. _International Journal of Wildland Fire_ 18 (5): 483–507. 557 doi:http://dx.doi.org/10.1071/WF08187. 

- 558 Fosberg, Michael A. 1978. “Weather in Wildland Fire Management: The Fire Weather 

22/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

- 559 

   - Index.” _US for Serv Reprints of Articles by FS Employees_ . 

- 560 Gelman, A., J.B. Carlin, H.S. Stern, D.B. Dunson, A. Vehtari, and D.B. Rubin. 2013. 

- 561 _Bayesian Data Analysis, Third Edition_ . Chapman & Hall/Crc Texts in Statistical Science. 

- 562 Taylor & Francis. https://books.google.com/books?id=ZXL6AQAAQBAJ. 

- 563 Gelman, Andrew, Xiao-Li Meng, and Hal Stern. 1996. “Posterior Predictive Assessment of 

- 564 Model Fitness via Realized Discrepancies.” _Statistica Sinica_ . JSTOR, 733–60. 

- 565 Goodrick, Scott L. 2002. “Modification of the Fosberg Fire Weather Index to Include 

- 566 Drought.” _International Journal of Wildland Fire_ 11 (4). CSIRO: 205–11. 

- 567 Grolemund, Garrett, and Hadley Wickham. 2011. “Dates and Times Made Easy with 568 lubridate.” _Journal of Statistical Software_ 40 (3): 1–25. http://www.jstatsoft.org/v40/ 569 i03/. 

- 570 Guyette, R. P., R. M Muzika, and D. C. Dey. 2002. “Dynamics of an Anthropogenic Fire 571 Regime.” _Ecosystems_ 5: 472–86. doi:10.1007/s10021-002-0115-7. 

- 572 Hargrove, William W, RH Gardner, MG Turner, WH Romme, and DG Despain. 2000. 

- 573 “Simulating Fire Patterns in Heterogeneous Landscapes.” _Ecological Modelling_ 135 (2-3). 574 Elsevier: 243–63. 

- 575 Hernandez, Charles, C Keribin, P Drobinski, and S Turquety. 2015. “Statistical Modelling 576 of Wildfire Size and Intensity: A Step Toward Meteorological Forecasting of Summer Ex577 treme Fire Risk.” In _Annales Geophysicae_ , 33:1495–1506. 12. 

- 578 Hijmans, Robert J. 2017. _Raster: Geographic Data Analysis and Modeling_ . https://CRAN. 579 R-project.org/package=raster. 

- 580 Hoffman, Matthew D, and Andrew Gelman. 2014. “The No-U-Turn Sampler: Adaptively 581 Setting Path Lengths in Hamiltonian Monte Carlo.” _Journal of Machine Learning Re-_ 582 _search_ 15 (1): 1593–1623. 

- 583 Hosking, Jonathan RM, and James R Wallis. 1987. “Parameter and Quantile Estimation 

23/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

- 584 for the Generalized Pareto Distribution.” _Technometrics_ 29 (3). Taylor & Francis: 339–49. 

- 585 Jiang, Yueyang, and Qianlai Zhuang. 2011. “Extreme Value Analysis of Wildfires in Cana586 dian Boreal Forest Ecosystems.” _Canadian Journal of Forest Research_ 41 (9). NRC Re587 search Press: 1836–51. 

- 588 Joseph, Max. 2018. “Mbjoseph/Wildfire-Extremes: First Release.” doi:10.5281/zenodo.1326858. 

- 589 Kneib, Thomas, Torsten Hothorn, and Gerhard Tutz. 2009. “Variable Selection and Model 590 Choice in Geoadditive Regression Models.” _Biometrics_ 65 (2). Wiley Online Library: 626– 591 34. 

592 Knorr, W, T Kaminski, A Arneth, and U Weber. 2013. “Impact of human population 593 density on fire frequency at the global scale Impact of human population density on fire 594 frequency at the global scale Impact of human population density on fire frequency at the 595 global scale.” _Biogeosciences Discuss_ 10: 15735–78. doi:10.5194/bgd-10-15735-2013. 

- 596 Kochi, Ikuho, Geoffrey H Donovan, Patricia A Champ, and John B Loomis. 2010. “The 

- 597 Economic Cost of Adverse Health Effects from Wildfire-Smoke Exposure: A Review.” _In-_ 598 _ternational Journal of Wildland Fire_ 19 (7). CSIRO: 803–17. 

- 599 Krawchuk, Meg A, Max A Moritz, Marc-André Parisien, Jeff Van Dorn, and Katharine 

- 600 Hayhoe. 2009. “Global Pyrogeography: The Current and Future Distribution of Wildfire.” 601 _PloS One_ 4 (4). Public Library of Science: e5102. 

602 Krawchuk, Meg A., and Max A. Moritz. 2011. “Constraints on global fire activity vary 603 across a resource gradient.” _Ecology_ 92 (1): 121–32. doi:10.1890/09-1843.1. 

- 604 Kucukelbir, Alp, Rajesh Ranganath, Andrew Gelman, and David Blei. 2015. “Automatic 605 Variational Inference in Stan.” In _Advances in Neural Information Processing Systems_ , 606 568–76. 

- 607 Lambert, Diane. 1992. “Zero-Inflated Poisson Regression, with an Application to Defects 608 in Manufacturing.” _Technometrics_ 34 (1). Taylor & Francis: 1–14. 

- 609 Lee, Dae-Jin, and María Durbán. 2011. “P-Spline Anova-Type Interaction Models for 610 Spatio-Temporal Smoothing.” _Statistical Modelling_ 11 (1). SAGE Publications Sage India: 

24/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

611 

New Delhi, India: 49–69. 

612 Li, Li-Ming, Wei-Guo Song, Jian Ma, and Kohyu Satoh. 2009. “Artificial neural network 613 approach for modeling the impact of population density and weather parameters on for614 est fire risk.” _International Journal of Wildland Fire_ 18 (6). CSIRO PUBLISHING: 640. 615 doi:10.1071/WF07136. 

- 616 Lloyd, Christopher T, Alessandro Sorichetta, and Andrew J Tatem. 2017. “High Reso617 lution Global Gridded Data for Use in Population Studies.” _Scientific Data_ 4. Nature 618 Publishing Group: 170001. 

619 Marani, Marco, and Massimiliano Ignaccolo. 2015. “A Metastatistical Approach to Rain620 fall Extremes.” _Advances in Water Resources_ 79. Elsevier: 121–26. 

621 Marlon, J. R., P. J. Bartlein, C. Carcaillet, D. G. Gavin, S. P. Harrison, P. E. Higuera, 622 F. Joos, M. J. Power, and I. C. Prentice. 2008. “Climate and human influences on global 623 biomass burning over the past two millennia.” _Nature Geoscience_ . doi:10.1038/ngeo313. 

- 624 McLaughlin, Steven P, and Janice E Bowers. 1982. “Effects of Wildfire on a Sonoran 625 Desert Plant Community.” _Ecology_ . JSTOR, 246–48. 

626 Mcwethy, D. B., P. E. Higuera, C. Whitlock, T. T. Veblen, D. M J S Bowman, G. J. Cary, 627 S. G. Haberle, et al. 2013. “A conceptual framework for predicting temperate ecosystem 628 sensitivity to human impacts on fire regimes.” _Global Ecology and Biogeography_ 22 (8): 629 900–912. 

- 630 Mendes, Jorge M, Patrícia Cortés de Zea Bermudez, José Pereira, KF Turkman, and MJP 631 Vasconcelos. 2010. “Spatial Extremes of Wildfire Sizes: Bayesian Hierarchical Models for 632 Extremes.” _Environmental and Ecological Statistics_ 17 (1). Springer: 1–28. 

- 633 Moritz, Max A, Marc-André Parisien, Enric Batllori, Meg A Krawchuk, Jeff Van Dorn, 634 David J Ganz, and Katharine Hayhoe. 2012. “Climate Change and Disruptions to Global 635 Fire Activity.” _Ecosphere_ 3 (6). Wiley Online Library: 1–22. 

636 Nagy, R, Emily Fusco, Bethany Bradley, John T Abatzoglou, and Jennifer Balch. 2018. 637 “Human-Related Ignitions Increase the Number of Large Wildfires Across Us Ecoregions.” 

25/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

- 638 

   - _Fire_ 1 (1). Multidisciplinary Digital Publishing Institute: 4. 

- 639 Nauslar, Nicholas, John Abatzoglou, and Patrick Marsh. 2018. “The 2017 North Bay and 

- 640 Southern California Fires: A Case Study.” _Fire_ 1 (1). Multidisciplinary Digital Publishing 641 Institute: 18. 

- 642 Neuwirth, Erich. 2014. _RColorBrewer: ColorBrewer Palettes_ . https://CRAN.R-project. 643 org/package=RColorBrewer. 

- 644 Omernik, James M. 1987. “Ecoregions of the Conterminous United States.” _Annals of the_ 645 _Association of American Geographers_ 77 (1). Taylor & Francis: 118–25. 

- 646 Omernik, James M, and Glenn E Griffith. 2014. “Ecoregions of the Conterminous United 647 States: Evolution of a Hierarchical Spatial Framework.” _Environmental Management_ 54 648 (6). Springer: 1249–66. 

- 649 Pebesma, Edzer. 2018. _Sf: Simple Features for R_ . https://CRAN.R-project.org/package= 650 sf. 

- 651 Pechony, O, and DT Shindell. 2009. “Fire Parameterization on a Global Scale.” _Journal of_ 652 _Geophysical Research: Atmospheres_ 114 (D16). Wiley Online Library. 

- 653 Pechony, Olga, and Drew T Shindell. 2010. “Driving Forces of Global Wildfires over the 

- 654 Past Millennium and the Forthcoming Century.” _Proceedings of the National Academy of_ 655 _Sciences_ 107 (45). National Acad Sciences: 19167–70. 

- 656 Pedersen, Thomas Lin. 2017. _Patchwork: The Composer of Ggplots_ . https://github.com/ 657 thomasp85/patchwork. 

- 658 Peltola, Tomi, Aki S Havulinna, Veikko Salomaa, and Aki Vehtari. 2014. “Hierarchical 659 Bayesian Survival Analysis and Projective Covariate Selection in Cardiovascular Event 660 Risk Prediction.” In _Proceedings of the Eleventh Uai Conference on Bayesian Modeling_ 661 _Applications Workshop-Volume 1218_ , 79–88. CEUR-WS. org. 

- 662 Pernin, Peter. 1971. “The Great Peshtigo Fire: An Eyewitness Account.” _The Wisconsin_ 

26/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

- 663 

   - _Magazine of History_ . JSTOR, 246–72. 

- 664 Peterson, David A, Edward J Hyer, James R Campbell, Michael D Fromm, Johnathan W 

- 665 Hair, Carolyn F Butler, and Marta A Fenn. 2015. “The 2013 Rim Fire: Implications for 

- 666 Predicting Extreme Fire Spread, Pyroconvection, and Smoke Emissions.” _Bulletin of the_ 667 _American Meteorological Society_ 96 (2): 229–47. 

- 668 Piironen, Juho, Aki Vehtari, and others. 2017. “Sparsity Information and Regularization 669 in the Horseshoe and Other Shrinkage Priors.” _Electronic Journal of Statistics_ 11 (2). The 670 Institute of Mathematical Statistics; the Bernoulli Society: 5018–51. 

- 671 Preisler, Haiganoush K, and Anthony L Westerling. 2007. “Statistical Model for Fore672 casting Monthly Large Wildfire Events in Western United States.” _Journal of Applied_ 673 _Meteorology and Climatology_ 46 (7): 1020–30. 

- 674 Preisler, Haiganoush K, David R Brillinger, Robert E Burgan, and JW Benoit. 2004. 675 “Probability Based Models for Estimation of Wildfire Risk.” _International Journal of Wild-_ 676 _land Fire_ 13 (2). CSIRO: 133–42. 

- 677 Quionero-Candela, Joaquin, Masashi Sugiyama, Anton Schwaighofer, and Neil D Lawrence. 678 2009. _Dataset Shift in Machine Learning_ . The MIT Press. 

- 679 R Core Team. 2017. _R: A Language and Environment for Statistical Computing_ . Vienna, 680 Austria: R Foundation for Statistical Computing. https://www.R-project.org/. 

- 681 ———. 2018. _R: A Language and Environment for Statistical Computing_ . Vienna, Austria: 682 R Foundation for Statistical Computing. https://www.R-project.org/. 

- 683 Radeloff, Volker C, David P Helmers, H Anu Kramer, Miranda H Mockrin, Patricia M 684 Alexandre, Avi Bar-Massada, Van Butsic, et al. 2018. “Rapid Growth of the Us Wildland685 Urban Interface Raises Wildfire Risk.” _Proceedings of the National Academy of Sciences_ 686 115 (13). National Acad Sciences: 3314–9. 

- 687 Radeloff, Volker C, Susan I Stewart, Todd J Hawbaker, Urs Gimmi, Anna M Pidgeon, 688 Curtis H Flather, Roger B Hammer, and David P Helmers. 2010. “Housing Growth in and 689 Near United States Protected Areas Limits Their Conservation Value.” _Proceedings of the_ 

27/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

- 690 

   - _National Academy of Sciences_ 107 (2). National Acad Sciences: 940–45. 

- 691 Ramsay, James O, and others. 1988. “Monotone Regression Splines in Action.” _Statistical_ 692 _Science_ 3 (4). Institute of Mathematical Statistics: 425–41. 

- 693 Reed, William J, and Kevin S McKelvey. 2002. “Power-Law Behaviour and Parametric 694 Models for the Size-Distribution of Forest Fires.” _Ecological Modelling_ 150 (3). Elsevier: 695 239–54. 

- 696 Reid, Colleen E, Michael Brauer, Fay H Johnston, Michael Jerrett, John R Balmes, and 697 Catherine T Elliott. 2016. “Critical Review of Health Impacts of Wildfire Smoke Expo698 sure.” _Environmental Health Perspectives_ 124 (9). National Institute of Environmental 699 Health Science: 1334. 

- 700 Rogers, Brendan M., Ronald P. Neilson, Ray Drapek, James M. Lenihan, John R. Wells, 701 Dominique Bachelet, and Beverly E. Law. 2011. “Impacts of Climate Change on Fire 702 Regimes and Carbon Stocks of the U.S. Pacific Northwest.” _Journal of Geophysical Re-_ 703 _search: Biogeosciences_ 116 (G3): n/a–n/a. doi:10.1029/2011JG001695. 

- 704 Rollins, Matthew G, Penelope Morgan, and Thomas Swetnam. 2002. “Landscape-Scale 705 Controls over 20th Century Fire Occurrence in Two Large Rocky Mountain (Usa) Wilder706 ness Areas.” _Landscape Ecology_ 17 (6). Springer: 539–57. 

- 707 Schoenberg, Frederic Paik, Roger Peng, and James Woods. 2003. “On the Distribution of 708 Wildfire Sizes.” _Environmetrics_ 14 (6). Wiley Online Library: 583–92. 

- 709 Serra, Laura, Marc Saez, Pablo Juan, Diego Varga, and Jorge Mateu. 2014. “A Spatio710 Temporal Poisson Hurdle Point Process to Model Wildfires.” _Stochastic Environmental_ 711 _Research and Risk Assessment_ 28 (7). Springer: 1671–84. 

- 712 Serra, Laura, Marc Saez, Jorge Mateu, Diego Varga, Pablo Juan, Carlos Díaz-Ávalos, and 713 Håvard Rue. 2014. “Spatio-Temporal Log-Gaussian Cox Processes for Modelling Wildfire 714 Occurrence: The Case of Catalonia, 1994–2008.” _Environmental and Ecological Statistics_ 715 21 (3). Springer: 531–63. 

- 716 Shirota, Shinichiro, and Sudipto Banerjee. 2018. “Scalable Inference for Space-Time Gaus- 

28/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

- 717 

   - sian Cox Processes.” _arXiv Preprint arXiv:1802.06151_ . 

- 718 Slowikowski, Kamil. 2018. _Ggrepel: Automatically Position Non-Overlapping Text Labels_ 719 _with ’Ggplot2’_ . https://CRAN.R-project.org/package=ggrepel. 

- 720 Solymos, Peter, and Zygmunt Zawadzki. 2018. _Pbapply: Adding Progress Bar to ’*Apply’_ 721 _Functions_ . https://CRAN.R-project.org/package=pbapply. 

- 722 Stallman, Richard M., Roland McGrath, and Paul D. Smith. 2004. _GNU Make: A Pro-_ 723 _gram for Directing Recompilation, for Version 3.81_ . Free Software Foundation. 

- 724 Stan Development Team. 2018. “RStan: The R Interface to Stan.” http://mc-stan.org/. 

- 725 Stavros, E Natasha, John T Abatzoglou, Donald McKenzie, and Narasimhan K Larkin. 

- 726 2014. “Regional Projections of the Likelihood of Very Large Wildland Fires Under a 

- 727 Changing Climate in the Contiguous Western United States.” _Climatic Change_ 126 (3728 4). Springer: 455–68. 

- 729 Syphard, Alexandra D. AD, Volker C. VC Radeloff, Jon E. Keeley, Todd J. Hawbaker, 

- 730 Murray K. Clayton, Susan I. Stewart, and Roger B. Hammer. 2007. “Human influence on 731 California fire regimes.” _Ecological Applications_ 17 (5): 1388–1402. 

- 732 Syphard, Alexandra D., Jon E. Keeley, Anne H. Pfaff, and Ken Ferschweiler. 

- 733 2017. “Human presence diminishes the importance of climate in driving fire ac- 

- 734 tivity across the United States.” _Proceedings of the National Academy of Sciences_ . 735 doi:10.1073/pnas.1713885114. 

- 736 Tedim, Fantina, Vittorio Leone, Malik Amraoui, Christophe Bouillon, Michael R Coughlan, 737 Giuseppe M Delogu, Paulo M Fernandes, et al. 2018. “Defining Extreme Wildfire Events: 738 Difficulties, Challenges, and Impacts.” _Fire_ 1 (1). Multidisciplinary Digital Publishing 739 Institute: 9. 

- 740 Tran, Dustin, Matthew D Hoffman, Rif A Saurous, Eugene Brevdo, Kevin Murphy, and 

- 741 David M Blei. 2017. “Deep Probabilistic Programming.” _arXiv Preprint arXiv:1701.03757_ . 

- 742 Vilar, Lara, Douglas G Woolford, David L Martell, and M Pilar Martín. 2010. “A Model 743 for Predicting Human-Caused Wildfire Occurrence in the Region of Madrid, Spain.” _Inter-_ 

29/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

- 744 

   - _national Journal of Wildland Fire_ 19 (3). CSIRO: 325–37. 

- 745 Westerling, AL, BP Bryant, HK Preisler, TP Holmes, HG Hidalgo, T Das, and SR 

- 746 Shrestha. 2011. “Climate Change and Growth Scenarios for California Wildfire.” _Climatic_ 747 _Change_ 109 (1). Springer: 445–63. 

- 748 Westerling, Anthony LeRoy. 2016. “Increasing Western Us Forest Wildfire Activity: Sensi749 tivity to Changes in the Timing of Spring.” _Phil. Trans. R. Soc. B_ 371 (1696). The Royal 750 Society: 20150178. 

- 751 Wickham, Hadley. 2017a. _Assertthat: Easy Pre and Post Assertions_ . https://CRAN. 752 R-project.org/package=assertthat. 

- 753 ———. 2017b. _Tidyverse: Easily Install and Load the ’Tidyverse’_ . https://CRAN. 754 R-project.org/package=tidyverse. 

- 755 Wiitala, Marc R. 1999. “Assessing the Risk of Cumulative Burned Acreage Using the Pois756 son Probability Model.” _Fire Economics, Planning, and Policy: Bottom Lines_ . Citeseer, 757 51. 

- 758 Wilke, Claus O. 2017. _Cowplot: Streamlined Plot Theme and Plot Annotations for ’Gg-_ 759 _plot2’_ . https://CRAN.R-project.org/package=cowplot. 

- 760 Williams, Jerry. 2013. “Exploring the Onset of High-Impact Mega-Fires Through a Forest 761 Land Management Prism.” _Forest Ecology and Management_ 294. Elsevier: 4–10. 

- 762 Wood, S.N. 2017. _Generalized Additive Models: An Introduction with R_ . 2nd ed. Chapman; 763 Hall/CRC. 

- 764 Woolford, DG, DR Bellhouse, WJ Braun, Ch B Dean, DL Martell, and J Sun. 2011. “A 765 Spatio-Temporal Model for People-Caused Forest Fire Occurrence in the Romeo Malette 766 Forest.” _Journal of Environmental Statistics_ 2: 2–16. 

- 767 Woolford, Douglas G, CB Dean, David L Martell, Jiguo Cao, and BM Wotton. 2014. 768 “Lightning-Caused Forest Fire Risk in Northwestern Ontario, Canada, Is Increasing and 769 Associated with Anomalies in Fire Weather.” _Environmetrics_ 25 (6). Wiley Online Library: 

30/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

- 770 

   - 406–16. 

- 771 Yao, Yuling, Aki Vehtari, Daniel Simpson, Andrew Gelman, and others. 2017. “Using 

- 772 Stacking to Average Bayesian Predictive Distributions.” _Bayesian Analysis_ . International 773 Society for Bayesian Analysis. 

- 774 Zeileis, Achim, and Gabor Grothendieck. 2005. “Zoo: S3 Infrastructure for Reg- 

- 775 ular and Irregular Time Series.” _Journal of Statistical Software_ 14 (6): 1–27. 776 doi:10.18637/jss.v014.i06. 

- 777 Zorzetto, E, G Botter, and M Marani. 2016. “On the Emergence of Rainfall Extremes 

- 778 from Ordinary Events.” _Geophysical Research Letters_ 43 (15). Wiley Online Library: 8076– 779 82. 

31/59 

; this version posted February 16, 2019. The copyright holder for this preprint (which wasthis version posted February 16, 2019. The copyright holder for this preprint (which wasThe copyright holder for this preprint (which was 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which wasthis version posted February 16, 2019. The copyright holder for this preprint (which wasThe copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

###### 780 

## **Tables** 

**Table 1.** Performance of count models on the test set in descending order. Posterior means are provided with standard deviations in parentheses. 

|Model|Holdout log likelihood|
|---|---|
|ZI Negative binomial|-3671 (70)|
|ZI Poisson|-4093 (77)|
|Negative binomial|-4298 (114)|
|Poisson|-4572 (139)|



32/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

**Table 2.** Performance of burned area models on the test set in descending order. Posterior means are provided with standard deviations in parentheses. 

|Model|Holdout log likelihood|
|---|---|
|Lognormal|-26341 (43)|
|Generalized Pareto|-26377 (45)|
|Tapered Pareto|-26386 (49)|
|Weibull|-27592 (236)|
|Gamma|-30675 (993)|



33/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

781 

## **Figures** 



**Figure 1.** Sizes of wildfires over 405 hectares in the contiguous United States, from the Monitoring Trends in Burn Severity multiagency program. Each point represents a fire event, and the largest fires for each year (the block maxima) are shown as solid black points. 

34/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 



**Figure 2.** A. Large wildfire ignition locations are shown as points across the study region. Colors in panels B, C, and D show level 1, 2, and 3 ecoregions respectively. 

35/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 



**Figure 3.** Conceptual figure to illustrate the use of B-splines to construct nonlinear functions. In the left panel, five B-spline vectors are shown, which map values of an input variable (on the x-axis) to a value on the y-axis. The middle panel shows the same B-spline vectors, but weighted (multiplied) by real numbers, with the weights illustrated as annotations. These weighted B-spline vectors are summed to produce the values of a nonlinear function (right panel). 

36/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 



**Figure 4.** Count predictive checks. Row one shows observed count frequencies as black points and predicted frequencies as lines. Rows two, three, and four show predicted proportions of zeros, maxima, and sums (respectively) in the training and test data, with empirical values as dashed lines. Rows two through four facilitate comparison of performance on training and test sets. Ideally, model predictions cluster around the dashed lines for both the training (x-axis direction) and test (y-axis direction) sets, leading to a tight cluster of points at the intersection of the dashed lines. 

37/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 



**Figure 5.** Partial effects on the log-transformed negative binomial mean component of the zero-inflated negative binomial model for each level 3 ecoregion, colored by level 1 ecoregion. Lines are posterior medians. Results are similar for the zero-inflation component. 

38/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 



**Figure 6.** Caterpillar plots of zero inflated negative binomial model coefficients, _β_<sup>(</sup><sup>_µ_)</sup> (left) and _β_<sup>(</sup><sup>_π_)</sup> (right). Horizontal line segments denote 95% credible intervals. Grey segments indicate coefficients with a less than 87% posterior probability of being positive or negative, and colored segments indicate coefficients that are probably positive (red) or negative (blue). B-spline vectors are indicated by colons, e.g., `Humidity:1` indicates the first basis vector corresponding to humidity. Interactions between variables `a` and `b` are represented as `a x b` . Level 1 ecoregions are represented by `L1 ecoregion name` , and `L2` and `L3` indicate level 2 and 3 ecoregions. 

39/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 



**Figure 7.** Predictive checks for burned area models. The top row shows predicted density in color and empirical density for the training set in black, which reveals overall lack of fit for the gamma and Weibull models. Row two shows the complementary cumulative distribution function (CCDF) at the tails, with 95% and 50% prediction intervals shown in color and observed data as black points, which shows that the Generalized Pareto distribution predicts values that are too extreme. The third and fourth rows show checks for maximum and total burned areas in the training and test set, with observed values as dashed lines and posterior draws as colored points. These final two rows facilitate checks for summary statistics on both the training and test set, with the ideal model generating predictions (colored points) clustered close to where the dashed lines intersect. 

40/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 



**Figure 8. A** . Estimated posterior medians and 95% credible intervals for each of the 3,473 coefficients associated with expected burned area. Only one coefficient - the first basis vector for humidity - had a 95% credible interval that excluded zero, shown in red. This effect is visualized in **B** . Partial effects of mean daily minimum humidity for each level 3 ecoregion, with posterior medians drawn as lines, and the 95% credible intervals as ribbons. **C** . Monthly time series of expected fire sizes for every level 3 ecoregion, faceted and colored by level 1 ecoregions sorted by mean humidity. Lines are posterior medians and ribbons are 95% credible intervals. 

41/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 



**Figure 9.** Posterior 99% (light red) and 95% (dark red) prediction intervals for the burned area of the largest fire event by month and level 3 ecoregion in the test set, shown for ecoregions with wildfires in more than 20 months. Empirical maxima are shown as black dots. 

42/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 



**Figure 10.** Estimated monthly posterior probabilities that one or more fire events exceed one million acres (404,686 hectares). The line represents the posterior median, and shaded region represents an 80% credible interval. The training period up to 2010 is shown in black, and the test period for which data were withheld during parameter estimation is shown in red. 

43/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 



**Figure 11.** Posterior median contribution of each input variable to the linear predictor function of model components for the Arizona/New Mexico Mountains level 3 ecoregion from 2010-2016. A dotted vertical line marks May 2011, when the Wallow Fire ignited. Vertical positions of colored lines show contributions to the linear predictor function of each model component. 

44/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 



**Figure 12.** A. Progression of the Wallow Fire based on perimeter data collected from the GeoMAC database, spanning May 30, 2011 to June 27, 2011. The perimeter at the end of may is outlined in white, with brighter colors indicating later dates. B. Daily local meteorological conditions and monthly regional mean conditions for the Wallow Fire, along with the associated burned area over time. The blue line represents monthly averages of meteorological quantities computed over the entire Arizona/New Mexico Mountains ecoregion, and black points represent values extracted for "local" 4 km grid cells contained within the final burned area perimeter of the Wallow Fire. 

45/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

###### 782 

## **Appendices** 

###### 783 

### **Prior specifications** 

784 Prior distributions were chosen to regularize coefficients on the distribution specific means 785 _β_<sup>(</sup><sup>_µ_)</sup> and structural zero parameters _β_<sup>(</sup><sup>_π_)</sup> . We used a regularized horseshoe prior on these 786 coefficients, which shrinks irrelevant coefficients towards zero, while regularizing nonzero 787 coefficients (Piironen, Vehtari, and others 2017). For zero-inflated models, we used a multi788 variate version of the regularized horseshoe (Peltola et al. 2014): 



<!-- Start of picture text -->
 βj ( µ )    τ 1 2 λ ˜2 1 ,j ρτ 1 τ 2 λ ˜ 1 ,jλ ˜ 2 ,j  <br> βj ( π )  ∼ N 0 ,  ρτ 1 τ 2 λ ˜ 1 ,jλ ˜ 2 ,j τ 2 2 λ ˜2 2 ,j   ,<br>λ ˜ 2 m,j = c 2 m λ 2 j ,<br>c 2 m +  τ  2 m λ 2 j<br><!-- End of picture text -->

789 for each response dimension _m_ = 1 _,_ 2 and coefficient _j_ = 1 _, ..., p_ . Here _ρ_ is a correlation 790 parameter, _τ_ 1 and _τ_ 2 are global variance hyperparameters, _c_ 1 and _c_ 2 are hyperparameters 791 that determine the amount of shrinkage on the largest coefficients, and _λj_ is a local scale 792 parameter drawn from a half-Cauchy distribution that control the amount of shrinkage 793 applied to coefficient _j_ (Piironen, Vehtari, and others 2017). With this prior specification, 794 information can be shared across the two response dimensions through the correlation pa795 rameter _ρ_ , and/or through the local scale parameters _λj_ . For count models without struc796 tural zeros (the Poisson and negative binomial models), this multivariate prior simplifies to 797 a univariate regularized horseshoe prior. 

798 Spatiotemporal random effects were constructed using a temporally autoregressive, spa799 tially intrinsically autoregressive formulation (Besag and Kooperberg 1995; Banerjee, Car800 lin, and Gelfand 2014). Temporarily suppressing the superscript that indicates whether 801 the effects are on _µ_ or _π_ , and denoting column _t_ from an _S × T_ **Φ** as **_φ_** _t_ we have: 



<!-- Start of picture text -->
φ t =1 ∼ N( 0 ,  ( τ ( φ ) ( D  − W )) − 1 )<br><!-- End of picture text -->

46/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 



<!-- Start of picture text -->
φ t ∼ N( η φ t− 1 ,  ( τ ( φ ) ( D  − W )) − 1 ) , t  = 2 , ..., T<br><!-- End of picture text -->

- 802 where _η_ is a temporal dependence parameter, _τ_<sup>(</sup><sup>_φ_)</sup> is a precision parameter, **D** is an _S × S_ 

- 803 diagonal matrix with entries corresponding to the number of spatial neighbors for each 

- 804 spatial unit, and **W** is an _S × S_ spatial adjacency matrix with nonzero elements only when 805 spatial unit _i_ is a neighbor of spatial unit _j_ ( _wi,j_ = 1 if _i_ is a neighbor of _j_ , and _wi,j_ = 0 

- 806 otherwise, including _wi,i_ = 0 for all _i_ ). _τ_<sup>(</sup><sup>_φ_)</sup> is a precision parameter. We imposed a soft 

- 807 identifiability constraint that places high prior mass near<sup>�</sup><sup>_S_</sup> _s_ =1<sup>_φ∗_</sup> _t,s_<sup>= 0forall</sup><sup>_t_.</sup> 

- 808 We applied a univariate regularized horseshoe prior to all _β_ coefficients in burned area 809 models (Piironen, Vehtari, and others 2017): 



<!-- Start of picture text -->
c 2 λ 2<br>βj ∼ N�0 , τ 2 λ ˜2 j � , λ ˜ 2 j = j ,<br>c 2 +  τ 2 λ 2<br>j<br><!-- End of picture text -->

- 810 Spatiotemporal random effects were constructed in the same way as for the count models. 

47/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

###### 811 

### **Joint distributions** 

812 Here we provide the unnormalized posterior densities for each model. Square brackets rep- 

813 resent a probability mass or density function. Parameterizations for model likelihoods are 

814 provided first, followed by the factorization of the joint distribution, with explicit priors. 

#### 815 **Poisson wildfire count model** 

816 We used the following parameterization of the Poisson distribution: 



<!-- Start of picture text -->
[ n|µ ] = µne−µ ,<br>n !<br><!-- End of picture text -->

817 where _µ_ is the mean and variance. 

818 The unnormalized posterior density of this model is: 



<!-- Start of picture text -->
[ β ( µ ) , α ( µ ) ,  φ , σ ( φ ) , η,  λ , c, τ |  N ]  ∝<br>S T<br>� �[ ns,t| β ( µ ) , α ( µ ) , φs,t ] ×<br>s =1 t =1<br>T<br>[ φ 1 |σ ( φ ) ] �[ φ t| φ t− 1 , σ ( φ ) , η ] ×<br>t =2<br>p<br>�[ βj ( µ ) |λj, c, τ ][ λj ] ×<br>j =1<br>[ σ ( φ ) ][ η ][ c ][ τ ][ α ( µ ) ]<br><!-- End of picture text -->

48/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 



<!-- Start of picture text -->
S T<br>=<br>� � Poisson( ns,t| exp( α ( µ ) +  X ( s,t ) β ( µ ) +  φs,t )) ×<br>s =1 t =1<br>Normal( φ 1 | 0 ,  (( σ ( φ ) ) − 2 ( D  − W )) − 1 ) ×<br>T<br>� Normal( φ t|η φ t− 1 ,  (( σ ( φ ) ) − 2 ( D  − W )) − 1 ) ×<br>t =2<br>p τ 2 c 2 λ 2<br>� Normal βj ( µ ) | 0 , j ×  Cauchy + ( λj| 0 ,  1) ×<br>j =1 � c 2 +  τ 2 λ 2 j �<br>Normal + ( σ ( φ ) | 0 ,  1 2 )  ×  Beta( η| 1 ,  1)  ×  Inv-Gamma( c 2 | 2 . 5 ,  10) ×<br>Normal + ( τ | 0 ,  5 2 )  ×  Normal( α ( µ ) | 0 ,  5 2 ) .<br><!-- End of picture text -->

49/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

###### 819 

#### **Negative binomial wildfire count model** 

820 We used the following parameterization of the negative binomial distribution: 



<!-- Start of picture text -->
µ δ<br>[ n|µ, δ ] = � n  +  δn − 1�� µ  +  δ � n � µ  +  δ � δ,<br><!-- End of picture text -->

821 where _µ_ is the mean, and _δ_ is a dispersion parameter. 

822 The unnormalized posterior density of this model is: 



<!-- Start of picture text -->
[ β ( µ ) , α ( µ ) ,  φ , σ ( φ ) , η,  λ , c, τ, δ |  N ]  ∝<br>S T<br>� �[ ns,t| β ( µ ) , α ( µ ) , φs,t, δ ] ×<br>s =1 t =1<br>T<br>[ φ 1 |σ ( φ ) ] �[ φ t| φ t− 1 , σ ( φ ) , η ] ×<br>t =2<br>p<br>�[ βj ( µ ) |λj, c, τ ][ λj ] ×<br>j =1<br>[ σ ( φ ) ][ η ][ c ][ τ ][ α ( µ ) ][ δ ]<br><!-- End of picture text -->



<!-- Start of picture text -->
S T<br>=<br>� � Negative Binomial( ns,t| exp( α ( µ ) +  X ( s,t ) β ( µ ) +  φs,t ) , δ ) ×<br>s =1 t =1<br>Normal( φ 1 | 0 ,  (( σ ( φ ) ) − 2 ( D  − W )) − 1 ) ×<br>T<br>� Normal( φ t|η φ t− 1 ,  (( σ ( φ ) ) − 2 ( D  − W )) − 1 ) ×<br>t =2<br>p τ 2 c 2 λ 2<br>� Normal βj ( µ ) | 0 , j ×  Cauchy + ( λj| 0 ,  1) ×<br>j =1 � c 2 +  τ 2 λ 2 j �<br>Normal + ( σ ( φ ) | 0 ,  1 2 )  ×  Beta( η| 1 ,  1)  ×  Inv-Gamma( c 2 | 2 . 5 ,  10) ×<br>Normal + ( τ | 0 ,  5 2 )  ×  Normal( α ( µ ) | 0 ,  5 2 )  ×  Normal + ( δ| 0 ,  5 2 ) .<br><!-- End of picture text -->

50/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

823 **Zero-inflated Poisson wildfire count model** 

824 We used the following parameterization of the zero-inflated Poisson distribution: 



<!-- Start of picture text -->
[ n|µ, π ] =  In =0(1  − π  +  πe −µ ) +  In> 0 π µne−µ ,<br>n !<br><!-- End of picture text -->

825 where _µ_ is the Poisson mean, and 1 _− π_ is the probability of an extra zero. 

826 The unnormalized posterior density of this model is: 



<!-- Start of picture text -->
[ β ( µ ) , α ( µ ) ,  β ( π ) , α ( π ) ,  φ ( µ ) , σ ( φ,µ ) , η ( µ ) ,  φ ( π ) , σ ( φ,π ) , η ( π ) ,  λ , c, τ, ρ |  N ]  ∝<br>S T<br>� �[ ns,t| β ( µ ) , α ( µ ) ,  β ( π ) , α ( π ) , φ ( s,t µ ) , φ ( s,t π )] ×<br>s =1 t =1<br>T<br>[ φ ( 1 µ ) |σ ( φ,µ )] �[ φ ( t µ ) | φ ( t− µ ) 1 , σ ( φ,µ ) , η ( µ )] ×<br>t =2<br>T<br>[ φ ( 1 π ) |σ ( φ,π )] �[ φ ( t π ) | φ ( t− π ) 1 , σ ( φ,π ) , η ( π )] ×<br>t =2<br>p<br>�[ βj ( µ ) , β j ( π ) |λj, c, τ, ρ ][ λj ] ×<br>j =1<br>2<br>[ σ ( φ,µ ) ][ σ ( φ,π ) ][ η ( µ ) ][ η ( π ) ][ α ( µ ) ][ α ( π ) ][ ρ ] � [ cm ][ τm ]<br>m =1<br><!-- End of picture text -->

51/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 



<!-- Start of picture text -->
S T<br>=<br>� � ZIP( ns,t|e α ( µ )+ X ( s,t ) β ( µ )+ φ ( s,t µ )  ,  logit − 1 ( α ( π ) +  X ( s,t ) β ( π ) +  φ ( s,t π ))) ×<br>s =1 t =1<br>Normal( φ ( 1 µ ) | 0 ,  (( σ ( φ,µ )) − 2( D  − W )) − 1) ×<br>T<br>� Normal( φ t ( µ ) |η ( µ ) φ ( t− µ ) 1 ,  (( σ ( φ,µ )) − 2( D  − W )) − 1) ×<br>t =2<br>Normal( φ ( 1 π ) | 0 ,  (( σ ( φ,π )) − 2( D  − W )) − 1) ×<br>T<br>� Normal( φ t ( π ) |η ( π ) φ ( t− π ) 1 ,  (( σ ( φ,π )) − 2( D  − W )) − 1) ×<br>t =2<br>j �=1 p N  ββjj (( πµ ))  ���� 0 ,  ρτ 1 τ 2 � τc 1 2 1 2 c + c 2 1 2 1 τλ c + 1 22 j 2 1 λτλ 2 j 1 22 j λ � 2 j c 2 2 c +2 2 τλ 2 22 j λ 2 j ρτ 1 τ 2 � τc 2 2 1 2 c + c 2 1 2 2 τλ c + 1 22 j 2 2 λτλ 2 j 2 22 j λ � 2 j c 2 2 c +2 2 τλ 2 22 j λ 2 j    ×<br>p<br>� Cauchy + ( λj| 0 ,  1) ×<br>j =1<br><!-- End of picture text -->



<!-- Start of picture text -->
Normal + ( σ ( φ,µ ) | 0 ,  1 2 )  ×  Normal + ( σ ( φ,π ) | 0 ,  1 2 ) ×<br>Beta( η ( µ ) | 1 ,  1)  ×  Beta( η ( π ) | 1 ,  1) ×<br>Normal( α ( µ ) | 0 ,  5 2 )  ×  Normal( α ( π ) | 0 ,  5 2 )  ×  LKJ( ρ| 3) ×<br>2<br>� Inv-Gamma( c 2 m | 2 . 5 ,  10)  ×  Normal+( τm| 0 ,  52) .<br>m =1<br><!-- End of picture text -->

52/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

827 

**Zero-inflated negative binomial wildfire count model** 

828 We used the following parameterization of the zero-inflated negative binomial distribution: 



<!-- Start of picture text -->
δ µ δ<br>[ n|µ, δ, π ] =  In =0(1  − π  +  π � µ  +  δ � δ ) +  In> 0� n  +  δn − 1�� µ  +  δ � n � µ  +  δ � δ,<br><!-- End of picture text -->

829 where _µ_ is the negative binomial mean, _δ_ is the negative binomial dispersion, and , and 830 1 _− π_ is the probability of an extra zero. 

831 The unnormalized posterior density of this model is: 



<!-- Start of picture text -->
[ β ( µ ) , α ( µ ) ,  β ( π ) , α ( π ) ,  φ ( µ ) , σ ( φ,µ ) , η ( µ ) ,  φ ( π ) , σ ( φ,π ) , η ( π ) ,  λ , c, τ, ρ, δ |  N ]  ∝<br>S T<br>� �[ ns,t| β ( µ ) , α ( µ ) ,  β ( π ) , α ( π ) , φ ( s,t µ ) , φ ( s,t π ) , δ ] ×<br>s =1 t =1<br>T<br>[ φ ( 1 µ ) |σ ( φ,µ )] �[ φ ( t µ ) | φ ( t− µ ) 1 , σ ( φ,µ ) , η ( µ )] ×<br>t =2<br>T<br>[ φ ( 1 π ) |σ ( φ,π )] �[ φ ( t π ) | φ ( t− π ) 1 , σ ( φ,π ) , η ( π )] ×<br>t =2<br>p<br>�[ βj ( µ ) , β j ( π ) |λj, c, τ, ρ ][ λj ] ×<br>j =1<br>2<br>[ σ ( φ,µ ) ][ σ ( φ,π ) ][ η ( µ ) ][ η ( π ) ][ α ( µ ) ][ α ( π ) ][ ρ ][ δ ] � [ cm ][ τm ] .<br>m =1<br><!-- End of picture text -->

53/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 



<!-- Start of picture text -->
S T<br>=<br>� � ZINB( ns,t|e α ( µ )+ X ( s,t ) β ( µ )+ φ ( s,t µ )  , δ,  logit − 1 ( α ( π ) +  X ( s,t ) β ( π ) +  φ ( s,t π ))) ×<br>s =1 t =1<br>Normal( φ ( 1 µ ) | 0 ,  (( σ ( φ,µ )) − 2( D  − W )) − 1) ×<br>T<br>� Normal( φ t ( µ ) |η ( µ ) φ ( t− µ ) 1 ,  (( σ ( φ,µ )) − 2( D  − W )) − 1) ×<br>t =2<br>Normal( φ ( 1 π ) | 0 ,  (( σ ( φ,π )) − 2( D  − W )) − 1) ×<br>T<br>� Normal( φ t ( π ) |η ( π ) φ ( t− π ) 1 ,  (( σ ( φ,π )) − 2( D  − W )) − 1) ×<br>t =2<br>j �=1 p N  ββjj (( πµ ))  ���� 0 ,  ρτ 1 τ 2 � τc 1 2 1 2 c + c 2 1 2 1 τλ c + 1 22 j 2 1 λτλ 2 j 1 22 j λ � 2 j c 2 2 c +2 2 τλ 2 22 j λ 2 j ρτ 1 τ 2 � τc 2 2 1 2 c + c 2 1 2 2 τλ c + 1 22 j 2 2 λτλ 2 j 2 22 j λ � 2 j c 2 2 c +2 2 τλ 2 22 j λ 2 j    ×<br>p<br>� Cauchy + ( λj| 0 ,  1) ×<br>j =1<br><!-- End of picture text -->

Normal<sup>+</sup> ( _σ_<sup>(</sup><sup>_φ,µ_)</sup> _|_ 0 _,_ 1<sup>2</sup> ) _×_ Normal<sup>+</sup> ( _σ_<sup>(</sup><sup>_φ,π_)</sup> _|_ 0 _,_ 1<sup>2</sup> ) _×_ Beta( _η_<sup>(</sup><sup>_µ_)</sup> _|_ 1 _,_ 1) _×_ Beta( _η_<sup>(</sup><sup>_π_)</sup> _|_ 1 _,_ 1) _×_ 

Normal( _α_<sup>(</sup><sup>_µ_)</sup> _|_ 0 _,_ 5<sup>2</sup> ) _×_ Normal( _α_<sup>(</sup><sup>_π_)</sup> _|_ 0 _,_ 5<sup>2</sup> ) _×_ LKJ( _ρ|_ 3) _×_ Normal<sup>+</sup> ( _δ|_ 0 _,_ 5<sup>2</sup> ) _×_ 2 � Inv-Gamma( _c_<sup>2</sup> _m_<sup>_|_2</sup><sup>_._5</sup><sup>_,_10)</sup><sup>_×_Normal+(</sup><sup>_τm|_0</sup><sup>_,_52)</sup><sup>_._</sup> _m_ =1 

54/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

832 

**Generalized Pareto/Lomax burned area model** 

833 We used the following parameterization of the GPD/Lomax distribution: 



<!-- Start of picture text -->
[ y|σ, κ ] = 1 ,<br>σ � κσy + 1 � − ( κ +1) κ− 1<br><!-- End of picture text -->

834 

where _κ_ is a shape parameter and _σ_ is a scale parameter. 

835 The unnormalized posterior density of this model is: 



<!-- Start of picture text -->
[ β , α,  φ , σ ( φ ) , η, κ ( L ) ,  λ , c, τ |  y ]  ∝<br>n tot<br>�[ yi| β , α, φsi,ti, κ ( L ) ] ×<br>i =1<br>T<br>[ φ 1 |σ ( φ ) ] �[ φ t| φ t− 1 , σ ( φ ) , η ] ×<br>t =2<br>p<br>�[ βj|λj, c, τ ][ λj ] ×<br>j =1<br>[ α ][ c ][ τ ][ κ ( L ) ][ η ][ σ ( φ ) ]<br><!-- End of picture text -->



<!-- Start of picture text -->
n tot<br>=<br>� Lomax( yi|κ ( L ) , e α + X ( si,ti ) β + φsi,ti ) ×<br>i =1<br>Normal( φ 1 | 0 ,  (( σ ( φ ) ) − 2 ( D  − W )) − 1 ) ×<br>T<br>� Normal( φ t|η φ t− 1 ,  (( σ ( φ ) ) − 2 ( D  − W )) − 1 ) ×<br>t =2<br>p τ 2 c 2 λ 2<br>� Normal βj| 0 , j ×  Cauchy + ( λj| 0 ,  1) ×<br>j =1 � c 2 +  τ 2 λ 2 j �<br><!-- End of picture text -->

Normal( _α|_ 0 _,_ 5<sup>2</sup> ) _×_ Inv-Gamma( _c_<sup>2</sup> _|_ 2 _._ 5 _,_ 10) _×_ Normal<sup>+</sup> ( _τ |_ 0 _,_ 5<sup>2</sup> ) Normal<sup>+</sup> ( _κ_<sup>(</sup><sup>_L_)</sup> _|_ 0 _,_ 5<sup>2</sup> ) _×_ Beta( _η|_ 1 _,_ 1) _×_ Normal<sup>+</sup> ( _σ_<sup>(</sup><sup>_φ_)</sup> _|_ 0 _,_ 1<sup>2</sup> ) _._ 

55/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

836 **Tapered Pareto burned area model** 

837 We used the following parameterization of the tapered Pareto distribution: 



<!-- Start of picture text -->
[ y|κ, ν ] = exp( −x/ν ) ,<br>� κy + ν 1 �<br><!-- End of picture text -->

838 where _κ_ is a shape parameter and _ν_ a taper parameter. 

839 The unnormalized posterior density of this model is: 



<!-- Start of picture text -->
[ β , α,  φ , σ ( φ ) , η, ν,  λ , c, τ |  y ]  ∝<br><!-- End of picture text -->



<!-- Start of picture text -->
n tot<br>�[ yi| β , α, φsi,ti, ν ] ×<br>i =1<br>T<br>[ φ 1 |σ ( φ ) ] �[ φ t| φ t− 1 , σ ( φ ) , η ] ×<br>t =2<br>p<br>�[ βj|λj, c, τ ][ λj ] ×<br>j =1<br>[ α ][ c ][ τ ][ ν ][ η ][ σ ( φ ) ]<br><!-- End of picture text -->



<!-- Start of picture text -->
n tot<br>=<br>� Tapered Pareto( yi|e α + X ( si,ti ) β + φsi,ti , ν ) ×<br>i =1<br>Normal( φ 1 | 0 ,  (( σ ( φ ) ) − 2 ( D  − W )) − 1 ) ×<br>T<br>� Normal( φ t|η φ t− 1 ,  (( σ ( φ ) ) − 2 ( D  − W )) − 1 ) ×<br>t =2<br>p τ 2 c 2 λ 2<br>� Normal βj| 0 , j ×  Cauchy + ( λj| 0 ,  1) ×<br>j =1 � c 2 +  τ 2 λ 2 j �<br><!-- End of picture text -->

Normal( _α|_ 0 _,_ 5<sup>2</sup> ) _×_ Inv-Gamma( _c_<sup>2</sup> _|_ 2 _._ 5 _,_ 10) _×_ Normal<sup>+</sup> ( _τ |_ 0 _,_ 5<sup>2</sup> ) _×_ Cauchy<sup>+</sup> ( _ν|_ 0 _,_ 1) _×_ Beta( _η|_ 1 _,_ 1) _×_ Normal<sup>+</sup> ( _σ_<sup>(</sup><sup>_φ_)</sup> _|_ 0 _,_ 1<sup>2</sup> ) _._ 

56/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

#### 840 **Lognormal burned area model** 

841 We used the following parameterization of the lognormal distribution: 



<!-- Start of picture text -->
1 − (log( y )  − µ )2<br>[ y|µ, σ ] = 1 ,<br>y σ √ 2 π exp � 2 σ 2 �<br><!-- End of picture text -->

842 where _µ_ and _σ_ are location and scale parameters, respectively. 

843 The unnormalized posterior density of this model is: 



<!-- Start of picture text -->
[ β , α,  φ , σ ( φ ) , η, σ,  λ , c, τ |  y ]  ∝<br>n tot<br>�[ yi|β, α, φsi,ti, σ ] ×<br>i =1<br>T<br>[ φ 1 |σ ( φ ) ] �[ φ t| φ t− 1 , σ ( φ ) , η ] ×<br>t =2<br>p<br>�[ βj|λj, c, τ ][ λj ] ×<br>j =1<br>[ α ][ c ][ τ ][ σ ][ η ][ σ ( φ ) ]<br><!-- End of picture text -->



<!-- Start of picture text -->
n tot<br>=<br>� Lognormal( yi|α  +  X ( si,ti ) β  +  φsi,ti, σ ) ×<br>i =1<br>Normal( φ 1 | 0 ,  (( σ ( φ ) ) − 2 ( D  − W )) − 1 ) ×<br>T<br>� Normal( φ t|η φ t− 1 ,  (( σ ( φ ) ) − 2 ( D  − W )) − 1 ) ×<br>t =2<br>p τ 2 c 2 λ 2<br>� Normal βj| 0 , j ×  Cauchy + ( λj| 0 ,  1) ×<br>j =1 � c 2 +  τ 2 λ 2 j �<br><!-- End of picture text -->

Normal( _α|_ 0 _,_ 5<sup>2</sup> ) _×_ Inv-Gamma( _c_<sup>2</sup> _|_ 2 _._ 5 _,_ 10) _×_ Normal<sup>+</sup> ( _τ |_ 0 _,_ 5<sup>2</sup> ) _×_ Normal<sup>+</sup> ( _σ|_ 0 _,_ 5<sup>2</sup> ) _×_ Beta( _η|_ 1 _,_ 1) _×_ Normal<sup>+</sup> ( _σ_<sup>(</sup><sup>_φ_)</sup> _|_ 0 _,_ 1<sup>2</sup> ) _._ 

57/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

844 **Gamma burned area model** 

845 We used the following parameterization of the gamma distribution: 



<!-- Start of picture text -->
1<br>[ y|κ, σ ] = Γ( κ ) σ κ yκ− 1exp( −y/σ ) ,<br><!-- End of picture text -->

846 where _κ_ is a shape parameter and _σ_ a scale parameter. 

847 The unnormalized posterior density of this model is: 



<!-- Start of picture text -->
[ β , α,  φ , σ ( φ ) , η, κ,  λ , c, τ |  y ]  ∝<br>n tot<br>�[ yi|β, α, φsi,ti, κ ] ×<br>i =1<br>T<br>[ φ 1 |σ ( φ ) ] �[ φ t| φ t− 1 , σ ( φ ) , η ] ×<br>t =2<br>p<br>�[ βj|λj, c, τ ][ λj ] ×<br>j =1<br>[ α ][ c ][ τ ][ κ ][ η ][ σ ( φ ) ]<br><!-- End of picture text -->



<!-- Start of picture text -->
n tot<br>=<br>� Gamma( yi|κ, κ/ exp( α  +  X ( si,ti ) β  +  φsi,ti )) ×<br>i =1<br>Normal( φ 1 | 0 ,  (( σ ( φ ) ) − 2 ( D  − W )) − 1 ) ×<br>T<br>� Normal( φ t|η φ t− 1 ,  (( σ ( φ ) ) − 2 ( D  − W )) − 1 ) ×<br>t =2<br>p τ 2 c 2 λ 2<br>� Normal βj| 0 , j ×  Cauchy + ( λj| 0 ,  1) ×<br>j =1 � c 2 +  τ 2 λ 2 j �<br><!-- End of picture text -->

Normal( _α|_ 0 _,_ 5<sup>2</sup> ) _×_ Inv-Gamma( _c_<sup>2</sup> _|_ 2 _._ 5 _,_ 10) _×_ Normal<sup>+</sup> ( _τ |_ 0 _,_ 5<sup>2</sup> ) _×_ Normal<sup>+</sup> ( _κ|_ 0 _,_ 5<sup>2</sup> ) _×_ Beta( _η|_ 1 _,_ 1) _×_ Normal<sup>+</sup> ( _σ_<sup>(</sup><sup>_φ_)</sup> _|_ 0 _,_ 1<sup>2</sup> ) _._ 

58/59 

bioRxiv preprint doi: https://doi.org/10.1101/384115; this version posted February 16, 2019. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY 4.0 International license. 

#### 848 **Weibull burned area model** 

849 We used the following parameterization of the Weibull distribution: 



<!-- Start of picture text -->
[ y|κ, σ ] = κ exp − ,<br>σ � σy � κ− 1 � � σy � α �<br><!-- End of picture text -->

850 where _κ_ is a shape parameter and _σ_ is a scale parameter. 

851 The unnormalized posterior density of this model is: 



<!-- Start of picture text -->
[ β , α,  φ , σ ( φ ) , η, κ, λ, c, τ |  y ]  ∝<br>n tot<br>�[ yi|β, α, φsi,ti, κ ] ×<br>i =1<br>T<br>[ φ 1 |σ ( φ ) ] �[ φ t| φ t− 1 , σ ( φ ) , η ] ×<br>t =2<br>p<br>�[ βj|λj, c, τ ][ λj ] ×<br>j =1<br>[ α ][ c ][ τ ][ κ ][ η ][ σ ( φ ) ]<br><!-- End of picture text -->



<!-- Start of picture text -->
n tot<br>=<br>� Weibull( yi|κ,  exp( α  +  X ( si,ti ) β  +  φsi,ti )) ×<br>i =1<br>Normal( φ 1 | 0 ,  (( σ ( φ ) ) − 2 ( D  − W )) − 1 ) ×<br>T<br>� Normal( φ t|η φ t− 1 ,  (( σ ( φ ) ) − 2 ( D  − W )) − 1 ) ×<br>t =2<br>p τ 2 c 2 λ 2<br>� Normal βj| 0 , j ×  Cauchy + ( λj| 0 ,  1) ×<br>j =1 � c 2 +  τ 2 λ 2 j �<br><!-- End of picture text -->

Normal( _α|_ 0 _,_ 5<sup>2</sup> ) _×_ Inv-Gamma( _c_<sup>2</sup> _|_ 2 _._ 5 _,_ 10) _×_ Normal<sup>+</sup> ( _τ |_ 0 _,_ 5<sup>2</sup> ) _×_ Normal<sup>+</sup> ( _κ|_ 0 _,_ 5<sup>2</sup> ) _×_ Beta( _η|_ 1 _,_ 1) _×_ Normal<sup>+</sup> ( _σ_<sup>(</sup><sup>_φ_)</sup> _|_ 0 _,_ 1<sup>2</sup> ) _._ 

59/59 


