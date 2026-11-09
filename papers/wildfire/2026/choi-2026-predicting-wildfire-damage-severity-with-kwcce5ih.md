---
title: 'Predicting Wildfire Damage Severity with Composite Indexing and Fire Weather Features: A Case Study in Gangwon Province, South Korea'
authors:
- Choi, Jaeun
- Yang, Wonseok
- Kim, Seokju
- Jeong, Ahyeon
- Baek, Jiwoo
- Ko, Nanggyun
- Jeon, Chumni
- Jung, Eun Sang
year: '2026'
journal: Fire
doi: 10.3390/fire9070310
tags:
- fire severity
- ignition
- wildfire
- wildfire occurrence
zotero_key: KWCCE5IH
item_type: journalArticle
url: https://openalex.org/W7169755086
source_url: null
fulltext_status: metadata-only
synced: '2026-11-09'
---

# Predicting Wildfire Damage Severity with Composite Indexing and Fire Weather Features: A Case Study in Gangwon Province, South Korea

## Abstract

Accurate wildfire prediction increasingly determines whether emergency resources arrive before a disaster becomes uncontrollable, yet the dominant paradigm reduces the problem to binary occurrence, offering no estimate of the severity that drives suppression planning. This study develops a machine-learning framework for four-class wildfire severity prediction, conditional on ignition, from weather-station observations and calendar terms alone. We construct a composite severity index (CSI) by applying principal component analysis to five damage dimensions (burned area, suppression equipment, personnel, duration, and property loss) recorded for 868 wildfires in Gangwon Province, South Korea (2011–2022) and pair standard observations with effective humidity and six indices of the Canadian Forest Fire Weather Index (FWI) System. Under a leakage-safe protocol, the strongest tree ensembles reach a macro F1 of 0.46 to 0.50 (recommended configuration: 0.41 ± 0.03 across 20 repeated splits) against a four-class chance level of 0.25, and the recommended Random Forest attains an extreme-class recall of 0.474; the CSI target outperforms burned area by 5.5 macro-F1 points under identical inputs. A weather-only screen separates extreme from non-extreme events with an ROC AUC of 0.758, capturing 47% of extreme events at a 20% alert budget. We also quantify how oversampling misplaced before the train-test split inflates the macro F1 to 0.65–0.83, a cause for caution for the severity-prediction literature.

