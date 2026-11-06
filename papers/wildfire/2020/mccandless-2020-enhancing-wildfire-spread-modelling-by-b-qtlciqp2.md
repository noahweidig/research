---
title: Enhancing wildfire spread modelling by building a gridded fuel moisture content product with machine learning
authors:
- McCandless, Tyler C
- Kosovic, Branko
- Petzke, William
year: '2020'
journal: 'Machine Learning: Science and Technology'
doi: 10.1088/2632-2153/aba480
tags: []
zotero_key: QTLCIQP2
item_type: journalArticle
url: https://iopscience.iop.org/article/10.1088/2632-2153/aba480
source_url: null
fulltext_status: metadata-only
synced: '2026-11-06'
---

# Enhancing wildfire spread modelling by building a gridded fuel moisture content product with machine learning

## Abstract

Abstract
            Wildland fire decision support systems require accurate predictions of wildland fire spread. Fuel moisture content (FMC) is one of the important parameters controlling the rate of spread of wildland fire. However, dead FMC measurements are provided by a relatively sparse network of remote automatic weather stations (RAWS), while live FMC is relatively infrequently measured manually. We developed a high resolution, gridded, real-time FMC data sets that did not previously exist for assimilation into operational wildland fire prediction systems based on ML. We used surface observations of live and dead FMC to train machine learning models to estimate FMC based on satellite observations. Moderate Resolution Imaging Spectrometer Terra and Aqua reflectances are used to predict the live and dead FMC measured by the Wildland Fire Assessment System and RAWS). We evaluate multiple machine learning methods including multiple linear regression, random forests (RFs), gradient boosted regression and artificial neural networks. The models are trained to learn the relationships between the satellite reflectances, surface weather and soil moisture observations and FMC. After training on data corresponding to the temporally and spatially nearest grid points to the irregularly spaced surface FMC observations, the machine learning models could be applied to all grid cells for a gridded product over the Conterminous United States (CONUS). The results show generally that the rule-based approaches have the lowest errors likely due to the sharp decision boundaries among the predictors, and the RF approach that utilizes bagging to avoid over-fitting has the lowest error on the test dataset. The errors are typically between 25%−33% the typical variability of the FMC data, which indicate the skill of the RF in estimating the FMC based on satellite data and surface characteristics. The FMC gridded product based on the RF runs operationally daily over CONUS and can be assimilated into WRF-Fire for more accurate wildland fire spread predictions.

