---
title: 'HazardWeaver: Scientific Route Selection for Hazard Analysis Agents'
authors:
- Zhu, Wangshu
- Cheng, Xueqi
- Wu, Liang
- Dong, Yushun
year: '2026'
journal: arXiv (Cornell University)
doi: 10.48550/arxiv.2610.03591
tags:
- large wildfires
zotero_key: E285AU47
item_type: journalArticle
url: https://openalex.org/W7220359965
source_url: null
fulltext_status: metadata-only
synced: '2026-11-06'
---

# HazardWeaver: Scientific Route Selection for Hazard Analysis Agents

## Abstract

Understanding and assessing natural hazards is essential for disaster preparedness and risk reduction. Recent advances in large language models have spurred growing interest in AI agents for hazard analysis, particularly their ability to integrate scientific data, models, and tools into automated workflows. However, effective automation requires agents to determine which scientific methods are appropriate for a given event and executable with the available data and tools. As new evidence and execution results become available, these conditions can change, requiring agents to reconsider their choices. We formulate this problem as state-dependent scientific route selection and introduce HazardWeaver. Specifically, HazardWeaver first leverages the Hazard Knowledge Compiler to extract evidence-linked conditions governing scientific applicability, then its Hazard Capability Graph represents executable scientific capabilities and checks compatibility between their inputs and outputs. Using these complementary representations, the Hazard Weaver Agent component selects applicable and executable routes, carries out their workflows, and revises its decisions as the analysis state changes. To evaluate both the scientific outputs and the decisions that produce them, we introduce the Hazard Weaver Benchmark, comprising 141 instances across seven single-hazard domains and four multi-hazard interaction classes. The benchmark accommodates multiple valid scientific routes and evaluates output correctness, route validity, and justified abstention. Extensive experiments on this benchmark show that HazardWeaver outperforms existing agent systems, with the largest gains on tasks with multiple eligible scientific routes. Our code is publicly available at https://github.com/LabRAI/HazardWeaver.

