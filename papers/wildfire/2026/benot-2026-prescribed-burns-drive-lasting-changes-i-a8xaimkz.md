---
title: Prescribed burns drive lasting changes in soil nitrogen cycling and microbial function
authors:
- Benot, Alaina O.
- Waldschmidt, Gray
- Gilvarg, Samuel C.
- Legge, Eva O. L.
- Okyere, Isaac J.
- Tiyapun, Chanistha
- Lucas, Sarah K.
- Yacht, Andrew L. Vander
- Goff, Jennifer Louise
year: '2026'
journal: mSystems
doi: 10.1128/msystems.00852-26
tags:
- prescribed burning
- united states
zotero_key: A8XAIMKZ
item_type: journalArticle
url: https://openalex.org/W7125372033
source_url: 'unpaywall: https://www.biorxiv.org/content/biorxiv/early/2026/01/21/2026.01.21.700861.full.pdf'
fulltext_status: fulltext
synced: '2026-11-06'
---

# Prescribed burns drive lasting changes in soil nitrogen cycling and microbial function

## Abstract

ABSTRACT Fire is a major pulse disturbance to soil microbial communities, with broad implications for nutrient cycling; however, regular burning is also a natural and often-essential process maintaining biodiversity in unique and imperiled fire-dependent ecosystems. Prescribed fire is widely used to promote this biodiversity and simultaneously reduce wildfire risk. Although such repeated burning is known to alter surface biodiversity, belowground soil geochemistry, and soil microbial community structure, the functional consequences (i.e . , the metabolic capabilities that underlie the ecosystem services soil microorganisms provide) remain underexplored. Here, we examined the effects of 30 years of repeated prescribed fire at the Albany Pine Bush—a fire-dependent, inland pitch pine barren ecosystem of the northeastern United States. Compared with the control stands, we observed that this long-term fire management has led to substantial depletion of inorganic soil nitrogen, specifically nitrate. We found no meaningful differences in the higher-level taxonomic composition of soil prokaryotic or fungal communities; however, analysis of metagenome-assembled genomes assembled from these soils revealed several differentially abundant populations. Furthermore, our metagenomic analysis revealed significant changes in the nitrogen-cycling functional potential, specifically decreased dissimilatory nitrate reduction and denitrification potential in repeatedly burned soils. These functional shifts have important implications for both nutrient cycling and emissions of trace nitrogen gases from these soils. Our results suggest that functionally meaningful changes in the soil microbiome can persist between burn events, even when higher-order community membership appears stable. This may imply that repeated fire can deplete reactive nitrogen emissions from soils by lowering the functional capacity of nitrogen-reducing microbes. IMPORTANCE Prescribed fire is widely used by land managers to reduce wildfire risk and promote biodiversity. While the effects of fire on aboveground processes are well understood, much less is known about how repeated burning influences soil biological properties—including the functional role that soil microorganisms play in nutrient cycling and greenhouse gas production. We addressed this gap by studying soils from the Albany Pine Bush, a rare and endangered ecosystem that has experienced regular prescribed fires for 30 years. Long-term fire management significantly altered soil chemistry, specifically lowering the amount of nitrogen in the soil. In addition, we found that fire management decreased the genetic potential of the soil microbial community to produce nitrogen oxides—potent contributors to climate change. Thus, prescribed fire’s contribution to greenhouse gas emissions may involve a complex relationship between direct fire-driven emissions, increased fire resilience of promoted vegetation, and—as suggested by our results—the reduced ability of soil microbes to produce greenhouse gases.

## Full text

bioRxiv preprint doi: https://doi.org/10.64898/2026.01.21.700861; this version posted January 21, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC 4.0 International license. 

- 1 **Prescribed Burns Drive Lasting Changes in Soil Nitrogen Cycling and Microbial Function** 

2 

- 3 1Alaina O. Benot, 2Gray Waldschmidt, 3Isaac J. Okyere, 4Eva O.L. Legge, 2Andrew L. Vander Yacht, 4 2Samuel C. Gilvarg, 3Chanistha Tiyapun, 3Jennifer L. Goff 

- 5 1Department of Environmental Biology, SUNY College of Environmental Science and Forestry, 6 Syracuse, NY 13210 

- 7 2Department of Sustainable Resources Management, SUNY College of Environmental Science and 8 Forestry, Syracuse, NY 13210 

- 9 3Department of Chemistry, SUNY College of Environmental Science and Forestry, Syracuse, NY 

- 10 13210 

- 11 4Department of Biology, Syracuse University, Syracuse, NY, 13210 

- 12 

13 

## **Key Words** 

14 Albany Pine Bush Preserve; Nitrogen; Denitrification; Nutrient Cycling; Fire Ecology; Metagenomes; 15 Soil; Forest; Pine Barrens 

16 

17 

18 

19 

20 

- 21 

- 22 

- 23 

- 24 

- 25 

- 26 

- 27 

- 28 

- 29 

- 30 

31 

bioRxiv preprint doi: https://doi.org/10.64898/2026.01.21.700861; this version posted January 21, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC 4.0 International license. 

51 52 53 54 55 56 57 58 59 

# 32 **Abstract** 

33 Fire can be a major pulse disturbance to soil microbial communities. Yet regular burning is a natural 34 and essential process that maintains biodiversity and the unique attributes of rare and imperiled fire35 dependent ecosystems. Most studies of fire effects on soil microbial communities typically focus on 36 short-term (<1 year) responses following a single fire event. Here we examined the longer-term 37 effects of repeated prescribed fire at the Albany Pine Bush—a fire-dependent, inland pitch pine 38 ( _Pinus rigida_ ) barren ecosystem of the northeastern US. We observed that this long-term fire 39 management ( _i.e._ , a fire interval of approximately every 5 to 13 years over the past 30 years) has led 40 to substantial depletion of soil nitrogen, specifically nitrate. However, we found no lasting shifts in the 41 higher-level taxonomic composition of soil prokaryotic communities. Instead, metagenomic analysis 42 revealed significant changes in the nitrogen-cycling functional potential, specifically, decreased 43 dissimilatory nitrate reduction and denitrification potential in repeatedly burned soils. Collectively, 44 these data suggest fire-induced geochemical changes persist under repeated burning, potentially 45 driving substantial shifts in soil microbial functional diversity. Our study reveals strain-level changes 46 that would be missed when examining only higher-level taxonomic patterns. Where fire is repeatedly 47 applied, fire-induced shifts in soil microbial communities can persist well beyond a few weeks after 48 burning—challenging prevailing views of short-lived belowground effects of prescribed burns. 

# 49 

# 50 

## **Brief Communication** 

51 Ecological disturbances, such as fire, alter microbial communities and their activities within Earth’s 52 biogeochemical cycles [1–3]. Yet, research on fire-microbe feedbacks has overwhelmingly focused 53 on short-term responses to single, high-intensity wildfires, typically within the first year post-burn 54 [4,5]. Despite the increasing use of prescribed fire ( _i.e_ ., an intentionally burned area) to mitigate 55 wildfires and foster biodiversity, the long-term impact of repeated prescribed fires on soil microbial 56 communities remains poorly understood. Available evidence suggests that taxonomic shifts following 57 a single prescribed fire are modest and transient, often dissipating within weeks to months [3,6–8]. 58 Whether repeated burning produces persistent structural and functional changes remains unclear. 59 Given prescribed fire’s impact on aboveground biodiversity, we hypothesized that multi-decadal fire 60 management imprints a lasting geochemical signature in soil that fundamentally reshapes 61 microbiome functional potential, with far-reaching implications for nutrient cycling and trace gas 62 fluxes [9]. 

63 Although the use of fire by Indigenous communities in the region dates back millennia [10], the 64 Albany Pine Bush Preserve (APBP, Albany, N.Y., U.S.A. [42.71 °N, 73.86 °W]) has a contemporary 65 prescribed burn history dating back approximately 30 years [11,12]. This fire-dependent landscape 66 has a pitch pine ( _Pinus ridiga_ ) dominated canopy with a scrub oak ( _Quercus ilicifolia_ ), dwarf oak ( _Q._ 67 _prinoides_ ), and herbaceous plant understory [12]. Fire maintains nutrient-poor soils, preventing 68 succession into closed-canopy hardwood forests [12,13]. Thus, the APBP serves as a powerful 69 model system for examining long-term impacts of prescribed fire on soil microbiomes. 

70 We sampled soils from nine stands at the APBP, spanning a gradient of prescribed fire frequency 71 over the past 30 years: “frequent” stands experienced ≥4 fires (average fire return interval = 5.7 72 years) while “infrequent” stands experienced >1 but ≤3 fires (average fire return interval = 13.3 73 years), reflective of the high and low ends, respectively, of historic fire return intervals [14]. “Control” 74 plots had no record of fire over this period **(Fig. 1A, Tables S1-S2)** . Within each stand, soils were 

bioRxiv preprint doi: https://doi.org/10.64898/2026.01.21.700861; this version posted January 21, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC 4.0 International license. 

- 75 collected at four sampling sites from two depths (0-15 cm and 15-30 cm), homogenized by depth 76 and stand, and stored at -80°C before analysis (n = 18 samples) **(Table S3)** . Metagenomic 77 sequencing and assembly methods are described in Benot et al. (2025) [15]. Taxonomic profiles 78 were generated using Kaiju, and nitrogen-cycling genes were quantified using Fama, both 79 implemented on the DOE KnowledgeBase Platform [16]. Soil geochemical analyses **(Table S4)** 80 included: pH, % organic matter, % total nitrogen (TN), % total carbon (TC), exchangeable acidity, 81 effective cation exchange capacity, ammonium chloride-extractable-calcium, potassium, magnesium, 82 phosphorus, aluminum, iron, manganese, sodium, and zinc, nitrate (NO3⁻-N), and ammonium (NH483 N). For additional details, see **SUPPORTING METHODS** . 

84 Fire affects the soil surface [13]. Yet geochemical changes observed at both soil depths suggested 85 both acute and sustained impacts of fire on soil chemistry **(Table S5** ). Principal component analysis 86 (PCA) of the geochemical data **(Table S4)** revealed separation of sites by both fire management 87 history and depth **(Fig. 1B)** that involved significant shifts in soil nitrogen (N) chemistry. At 0-15 cm, 88 %TN decreased ~1.5-fold in both fire treatments compared to controls (one-way ANOVA with Tukey 89 HSD, _p < 0.05_ for both treatments) **(Fig. 1C)** . No differences in NH4-N were observed between 90 treatments (one-way ANOVA, _p > 0.05_ ). However, bioavailable NO3⁻-N declined substantially with 91 burning at both depths, with 9-fold (frequent) and 5-fold (infrequent) reductions in the surface soils 92 and similar declines at the 15-30 cm depth (5-fold and 4-fold, respectively) (one-way ANOVA with 93 Tukey HSD, _p < 0.05_ ) **(Fig. 1D)** . Possible mechanisms for this NO3⁻-N loss includes incorporation 94 into recalcitrant pyrogenic organic matter [4,17] and volatilization [18]. 

95 Subsequently, read-based taxonomic mapping was used to evaluate whether fire-driven soil 96 changes altered microbial community composition. Sample depth had a significant effect on 97 community composition from the phylum to genus levels (PERMANOVA, _p < 0.05_ ), whereas fire 98 treatment and its interaction with depth were not significant influences at these taxonomic levels 99 (PERMANOVA, _p > 0.05_ ). This aligns with prior studies reporting minimal or no detectable change in 100 community composition weeks to months after a prescribed fire [8,19]. Across all soils, the most 101 prevalent phyla were _Proteobacteria_ , followed by _Acidobacteria_ and _Actinobacteria_ ( **Fig. S1, Tables** 102 **S6-S10).** 

103 Given significant shifts in soil N in fire-managed sites, the metagenomic reads were mapped to 104 microbial N-cycling genes **(Table S11)** . Unlike the community analysis, variation in N-cycling gene 105 composition was significantly explained by both fire treatment and depth (PERMANOVA, _p = 0.004_ 106 and _p = 0.005,_ respectively)—with treatment as the strongest predictor (25.5% of variance 107 explained) **(Fig. 2A)** . These are likely species- or strain-level differences not resolved by coarser 108 taxonomic analyses [20]. Depleted bioavailable NO3⁻-N in fire-managed soils may be one driver of 109 these shifts. Indeed, there was a strong positive correlation (Pearson's R > _0.60_ ) between soil nitrate 110 concentrations and the abundances of dissimilatory nitrate reduction and denitrification genes **(Table** 111 **S12)** . 

112 We also observed significant decreases in the abundances of the denitrification and dissimilatory 113 nitrate reduction pathways **(Fig. 2B-E)** at lower soil depths (15-30 cm) at fire-managed relative to 114 control sites (one-way ANOVA with Tukey HSD, _p < 0.05_ ). In contrast, the abundances of nitrogen 115 fixation, ammonium oxidation, nitrite assimilation, ammonification, urea degradation, or assimilatory 116 nitrate reduction pathways **(Figs. S3-7)** were unchanged. As these pathways are linked to 117 ammonium flux, the stable ammonium concentrations across treatments may explain the absence of 

bioRxiv preprint doi: https://doi.org/10.64898/2026.01.21.700861; this version posted January 21, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC 4.0 International license. 

125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 

- 118 detectable shifts. In contrast, within the denitrification/dissimilatory nitrate reduction pathways, _napA_ 119 (encoding periplasmic nitrate reductase), _nirK_ (copper-containing nitrite reductase), _qnor_ (quinol120 dependent nitric oxide reductase), and _nosZ_ (nitrous oxide reductase) all decreased in abundance at 121 the lower depth **(Fig. S9)** . At lower soil depths, most mapped reads for _napA_ , _nirK_ , _nosZ_ , and _qnor_ 122 were associated with _Proteobacteria_ , with smaller contributions from _Bacteroidetes_ ( _napA_ , _nosZ_ ), 123 _Acidobacteria_ ( _qnor_ ), _Actinobacteria_ ( _nirK_ , _qnor_ ), _Chloroflexi_ ( _nirK_ ), _Nitrospirae_ ( _nirK_ ), and 124 _Planctomycetes_ ( _qnor_ ) **(Table S13)** . Relative to control soils, fire management reduced relative 125 abundances of _Proteobacteria_ -associated _napA_ and _nirK_ . In contrast, relative abundances of 126 _Proteobacteria_ -associated _nosZ_ increased, while relative abundances of _nosZ_ reads associated with 127 _Bacteroidetes_ declined. Together, these shifts indicate that long-term fire management also 128 restructures the taxonomic partitioning of dissimilatory nitrate reduction/denitrification potential. 

Despite extensive research on wildfire feedbacks on soil microbiomes, the impacts of long-term prescribed fire regimes on microbial communities remain poorly characterized [3–6]. Prior work suggests that single prescribed burns have limited, short-lived effects on microbial taxonomic composition—relative to more intense and severe wildfire—with detectable changes generally disappearing within weeks to months [6–8,19]. In contrast, our results reveal persistent fire-driven restructuring of microbial functional potential, particularly within N-cycling pathways. Specifically, we observe a sustained reduction of microbial denitrification potential, linking prescribed fire to longterm modulation of soil reactive N gas fluxes—specifically nitrous acid, nitric oxide, and nitrous oxide. Together, these findings demonstrate that repeated prescribed fire restructures soil microbiomes in ways that taxonomic analyses alone cannot detect. 

## **Acknowledgments** 

We gratefully thank The Albany Pine Bush Preserve Commission (specifically Neil Gifford, Steve Campbell, Tyler Briggs, and Alex Soldo) for their expertise and guidance regarding the Albany Pine Bush Preserve. We also thank the University of Delaware Ammon-Pinizzotto Biopharmaceutical Innovation Center DNA Sequencing & Genotyping Center for conducting DNA sequencing and the University of Maine for soil geochemical analysis. Also, we’d like to acknowledge Matthew Lathrop for their GIS technical expertise and Aaron Ninokawa for guidance with statistical analyses in R. Financial support for this project came from SUNY ESF startup funds to JLG. 

## **Data Availability** 

All geochemical data and site metadata are available in the supplemental information files. All <mark>sequencing data used here are associated with BioProject</mark> <u><mark>PRJNA1269515. Raw sequencing data</mark></u> <mark>– are available through NCBI Sequence Read Archive (SRA) via accession numbers SRX28992350</mark> <u><mark>SRX28992355; SRX29211976–SRX29211981; and SRX29333943–SRX29333948. Tables S1, S3-</mark></u> <mark>S4, S6-S11, and S13 can be found on Figshare:</mark> <u>https://doi.org/10.6084/m9.figshare.31083271.</u> 

## **References** 

1. Falkowski PG, Fenchel T, Delong EF. The Microbial Engines That Drive Earth’s Biogeochemical Cycles. _Science_ 2008; **320** :1034–9. 

2. Van Der Heijden MGA, Bardgett RD, Van Straalen NM. The unseen majority: soil microbes as drivers of plant diversity and productivity in terrestrial ecosystems. _Ecol Lett_ 2008; **11** :296–310. 

bioRxiv preprint doi: https://doi.org/10.64898/2026.01.21.700861; this version posted January 21, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC 4.0 International license. 

- 162 3. Uppal S, Woolet J, Venkateshwaran M _et al._ A granular view of the traits controlling soil bacterial 163 community reconstruction following a prescribed burn. 2024:2024.06.20.599938. 

- 164 4. Certini G. Effects of fire on properties of forest soils: a review. _Oecologia_ 2005; **143** :1–10. 

- 165 5. Nelson AR, Narrowe AB, Rhoades CC _et al._ Wildfire-dependent changes in soil microbiome 166 diversity and function. _Nat Microbiol_ 2022; **7** :1419–30. 

- 167 6. Rafie SAA, Blentlinger LR, Putt AD _et al._ Impact of prescribed fire on soil microbial communities in 168 a Southern Appalachian Forest clear-cut. _Front Microbiol_ 2024; **Volume 15-2024** , DOI: 169 10.3389/fmicb.2024.1322151. 

- 170 7. Glassman SI, Randolph JWJ, Saroa SS _et al._ Prescribed versus wildfire impacts on exotic plants 171 and soil microbes in California grasslands. _Appl Soil Ecol_ 2023; **185** :104795. 

- 172 8. Kapoor B, Onufrak A, Klingeman Iii W _et al._ Signatures of prescribed fire in the microbial 173 communities of Cornus florida are largely undetectable five months post-fire. _PeerJ_ 2023; **11** :e15822. 

- 174 9. Legge EOL, Koyama A, Fernandez CW _et al._ Dearth under earth: Understudied plant-soil-fire 175 feedback as drivers of forest mesophication and oak regeneration failures. _For Ecol Manag_ 176 2025; **597** :123147. 

- 177 10. Williams GW. References On The American Indian Use of Fire In Ecosystems. 2003. 

- 178 11. Barnes JK, Institute NYSBR, Museum NYS. _Natural History of the Albany Pine Bush_ � _: Albany_ 179 _and Schenectady Counties, New York, Including a Field Guide and Trail Map_ . Albany, N.Y, New York 180 State Museum, University of the State of New York, State Education Dept, c2003, 2003. 

- 181 12. Gifford NA, Briggs T. _2023 Review and Recommendations for the Fire Management Plan for the_ 182 _Albany Pine Bush Preserve_ . Albany Pine Bush Preserve Commission, 2023:1–9. 

- 183 13. DeBano LF. THE EFFECT OF FIRE ON SOIL PROPERTIES. _SOLO_ 1990. 

- 184 14. Jamison E-AK, D’Amato AW, Dodds KJ. Describing a landscape mosaic: Forest structure and 185 composition across community types and management regimes in inland northeastern pitch pine 186 barrens. _For Ecol Manag_ 2023; **536** :120859. 

- 187 15. Benot Alaina O., Waldschmidt Gray, Tiyapun Chanistha _et al._ Metagenomic characterization of 188 fire-adapted soil microbiomes in the Albany Pine Bush Preserve. _Microbiol Resour Announc_ 189 2025; **0** :e00664-25. 

- 190 16. Arkin AP, Cottingham RW, Henry CS _et al._ KBase: The United States Department of Energy 191 Systems Biology Knowledgebase. _Nat Biotechnol_ 2018; **36** :566–9. 

- 192 17. Neary DG, Ryan KC, DeBano LF. _Wildland Fire in Ecosystems: Effects of Fire on Soils and_ 193 _Water_ . U.S. Department of Agriculture, Forest Service, Rocky Mountain Research Station, 2005. 

- 194 18. Stephens EZ, Homyak PM. Post-fire soil emissions of nitric oxide (NO) and nitrous oxide (N2O) 195 across global ecosystems: a review. _Biogeochemistry_ 2023; **165** :291–309. 

- 196 19. Kranz C, Whitman T. Short communication: Surface charring from prescribed burning has 197 minimal effects on soil bacterial community composition two weeks post-fire in jack pine barrens. 198 _Appl Soil Ecol_ 2019; **144** :134–8. 

bioRxiv preprint doi: https://doi.org/10.64898/2026.01.21.700861; this version posted January 21, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC 4.0 International license. 

199 20. Louca S, Parfrey LW, Doebeli M. Decoupling function and taxonomy in the global ocean 200 microbiome. _Science_ 2016; **353** :1272–7. 

# 201 **Figures** 

202 203 **Fig 1. A** _:_ Location of randomly distributed sub-sampling sites within selected APBP stands. **B** : PCA 204 plot of homogenized sample site geochemistry. **C** and **D** : Bar graph of average NO3--N (mg/kg) and 205 average percentage total nitrogen, respectively. One-way ANOVAs were conducted independently 206 for each soil depth, followed by a post hoc Tukey’s HSD test. Lowercase (a, b) and uppercase (A, B) 207 letters indicate significantly different ( _p < 0.05_ ) treatment means at 0-15 cm and 15-30 cm depths, 208 respectively. Bar graphs were created in <u>https://BioRender.com.</u> 

209 

bioRxiv preprint doi: https://doi.org/10.64898/2026.01.21.700861; this version posted January 21, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC 4.0 International license. 













210 211 **Figure 2. A:** Nonmetric multidimensional scaling using Bray-Curtis dissimilarity of N-cycling genes in 212 individual samples. **B:** Normalized heatmap of individual genes in the denitrification pathway. **C:** 213 Normalized heatmap of individual genes in the dissimilatory nitrate reduction pathway. For **B** and **C** , 214 one-way ANOVAs were conducted, followed by a post hoc Tukey’s HSD test, and lowercase letters 215 (a, b) indicate significantly different ( _p<0.05_ ) treatment means. **D:** Gene abundance of dissimilatory 216 nitrate reduction pathway genes at 15-30 cm grouped by treatment. **E:** Gene abundance of 

bioRxiv preprint doi: https://doi.org/10.64898/2026.01.21.700861; this version posted January 21, 2026. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under a CC-BY-NC 4.0 International license. 

217 denitrification pathway genes at 15-30 cm grouped by treatment. Figure layout was performed in 218 <u>https://BioRender.com.</u> 219 


