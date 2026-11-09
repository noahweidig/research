---
title: A Spatiotemporal Graph Neural Network Framework for Retrospective Bias Correction of CMAQ Air Quality Simulations over the Continental United States
authors:
- Stergiou, Ioannis
- Traka, Nektaria
- Melas, Dimitrios
- Tagaris, Efthimios
- Sotiropoulou, Rafaella‐Eleni P.
year: '2026'
journal: Atmospheric Pollution Research
doi: 10.1016/j.apr.2026.103191
tags:
- drivers
- machine learning
- modeling
- united states
zotero_key: MXJVWRMS
item_type: journalArticle
url: https://openalex.org/W7204909574
source_url: null
fulltext_status: metadata-only
synced: '2026-11-09'
---

# A Spatiotemporal Graph Neural Network Framework for Retrospective Bias Correction of CMAQ Air Quality Simulations over the Continental United States

## Abstract

A spatiotemporal graph neural network (STGNN) framework combining CNN–LSTM temporal encoding with Graph Attention Networks v2 (GATv2) spatial message passing was evaluated for retrospective bias correction of Community Multiscale Air Quality (CMAQ) simulations under day-ahead observational information constraints. Using five years of hourly EPA observations from 235 monitoring stations across the continental United States, t improved model performance under retrospective, reanalysis-driven conditions, while restricting all observation-derived inputs to information available at least 24 h before the target prediction hour. The reported skill should therefore be interpreted as an upper bound on operational forecast performance, as the WRF–CMAQ inputs were derived from retrospective reanalysis rather than forecast-mode simulations. The STGNN achieves a root–mean–square error (RMSE) of 4.53 ppb for NO 2 and 7.32 ppb for O 3 , representing relative error reductions of 52.4% and 65.0%, respectively, over raw CMAQ fields. The framework increases the coefficient of determination, R 2 , from –0.15 to 0.74 for NO 2 and from –0.72 to 0.79 for O 3 , while substantially minimizing systematic model bias and improving diurnal variability representations. Comprehensive ablation experiments show that the CNN–LSTM temporal encoder provides most of the predictive skill, while graph message passing yields modest additional RMSE reductions of 2.2% for NO 2 and 3.0% for O 3 , with station-cluster bootstrap confidence intervals excluding zero. Wind–modulated edge weight variants provide negligible predictive benefit over static distance-based connectivity. Across four regional holdout experiments, the complete framework produced lower point-estimate RMSE than raw CMAQ at stations excluded from training, with reductions of 17.4–32.5% for NO 2 and 40.4–60.0% for O 3 . Paired station-cluster bootstrap intervals excluded zero in seven of the eight region–pollutant comparisons. Permutation feature importance analysis isolates raw model predictions and hybrid 24–hour lagged temperature errors as the dominant drivers of predictive utility, highlighting the strong predictive association between lagged meteorological-error information and CMAQ bias within the evaluated framework.

