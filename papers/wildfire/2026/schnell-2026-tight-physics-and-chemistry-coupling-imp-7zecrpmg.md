---
title: 'Tight physics and chemistry coupling improves air quality forecasts: a case study of the 2020 North American wildfires with the Rapid Refresh model coupled to Chemistry (RAP-Chem v1.0)'
authors:
- Schnell, Jordan
- Ahmadov, Ravan
- Grell, Georg A.
- Olson, Joseph B.
- James, Eric
- Hu, Ming
- Wong, Ka Yee
- McDonald, Brian
- Schwantes, Rebecca H.
- He, Jian
- Harkins, Colin
- Angevine, W. M.
- Jamison, Brian
- Pierce, R. Bradley
- Coggon, Matthew M.
- Baker, Barry
- Freitas, Saulo R.
- Pereira, Gabriel
- Tsidulko, M.
year: '2026'
journal: null
doi: 10.5194/egusphere-2026-4786
tags:
- large wildfires
- prescribed burning
- western united states
- wildfire
zotero_key: 7ZECRPMG
item_type: journalArticle
url: https://openalex.org/W7202382949
source_url: 'unpaywall: https://egusphere.copernicus.org/preprints/2026/egusphere-2026-4786/egusphere-2026-4786.pdf'
fulltext_status: fulltext
synced: '2026-11-09'
---

# Tight physics and chemistry coupling improves air quality forecasts: a case study of the 2020 North American wildfires with the Rapid Refresh model coupled to Chemistry (RAP-Chem v1.0)

## Abstract

Abstract. The Rapid Refresh model coupled to Chemistry (RAP-Chem) is an experimental forecast model built and operated by the NOAA Global Systems Laboratory (GSL). The RAP-Chem is a full chemistry extension to the operational smoke forecasting model, RAP-Smoke. RAP-Chem’s chemistry includes a reduced complexity, carbon-bond, gas-phase mechanism and an aerosol scheme that are coupled together to produce secondary aerosols and perform heterogeneous chemistry. The model includes chemical lateral boundary conditions, hourly anthropogenic emissions and online emissions from biomass burning, dust, sea salt, and biogenic sources. RAP-Chem also includes the direct aerosol effect on radiation and photolysis and a simplified indirect aerosol effect that couples prognostic aerosols to representative aerosols in the aerosol-aware microphysics scheme. The default ‘offline’ vertical mixing implemented in WRF-Chem is updated to instead mix chemical species alongside other scalars in the model’s planetary boundary layer (PBL) scheme, which tends to improve predictions across species – increasing surface ozone (O3) and decreasing less reactive tracers (e.g., CO). Sub-grid boundary layer clouds in the PBL scheme are also coupled to a WRF-Chem photolysis scheme for the first time, overall reducing O3 biases in the eastern US. Here we present the ability of the RAP-Chem model to simulate the extreme North American wildfires in 2020. We demonstrate that the relatively simple gas-phase chemical mechanism alongside our model physics developments and coupling with chemistry can predict maximum daily 8-h average O3 with exceptional skill (Normalized Mean Bias (NMB) = 6.6 %) averaged over CONUS, improving on simulations that neglect the direct aerosol effect (NMB = 9.5 %). Ozone biases are large in regions with extreme aerosol loading, but the NMB improves more significantly. The model produces the observed extreme aerosol loading with less skill; tending to underpredict extreme wildfire induced concentrations while overpredicting urban particle pollution. As with O3, daily average PM2.5 is predicted with better skill when the direct aerosol feedback is included (-15.8 % vs. -16.8 %). Overall we find that improving the coupling between chemistry and physics processes in the air quality model improves its predictions of both weather and atmospheric composition.

## Full text

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





1 **Tight  physics  and  chemistry  coupling  improves  air  quality  forecasts:** 

- 2 **a  case  study  of  the  2020  North  American  wildfires  with  the  Rapid** 

- 3 **Refresh model coupled to Chemistry (RAP-Chem v1.0)** 

- 4 Jordan  Schnell<sup>1,2</sup> ,  Ravan  Ahmadov<sup>2</sup> ,  Georg  A.  Grell<sup>2</sup> ,  Joseph  B.  Olson<sup>2</sup> ,  Eric  James<sup>2</sup> ,  Ming  Hu<sup>2</sup> ,  Ka  Yee 5 Wong<sup>2,4</sup> ,  Brian  McDonald<sup>3</sup> ,  Rebecca  H.  Schwantes<sup>3</sup> ,  Jian  He<sup>1,3</sup> ,  Colin  Harkins<sup>1,3</sup> ,  Wayne  M.  Angevine<sup>1,3</sup> , 6 Brian  Jamison<sup>2,4</sup> ,  R.  Bradley  Pierce<sup>5</sup> ,  Matthew  Coggon<sup>3</sup> ,  Barry  Baker<sup>6</sup> ,  Saulo  Freitas<sup>7</sup> ,  Gabriel  Pereira<sup>8</sup> , 7 Marina Tsidulko<sup>9</sup> 

- 8 1  Cooperative  Institute  for  Research  in  Environmental  Sciences  (CIRES),  University  of  Colorado 9 Boulder, USA 

- 2  NOAA Global Systems Laboratory, 325 Broadway, Boulder, CO, USA 

- 10 

- 3  NOAA Chemical Sciences Laboratory, 325 Broadway, Boulder, CO, USA 

- 11 

- 12 4  Cooperative  Institute  for  Research  in  the  Atmosphere  (CIRA),  Colorado  State  University,  3925A  West 13 Laporte Ave, Fort Collins, CO 80521, USA 

- 14 5  Space  Science  and  Engineering  Center,  University  of  Wisconsin-Madison,  1225  W.  Dayton  St., 15 Madison, WI 53706, USA 

- 16 6  NOAA Air Resources Laboratory, 5830 University Research Court, College Park, MD 20740, USA 

- 17 7  National  Institute  for  Space  Research  (INPE),  Avenida  dos  Astronautas,  1.758,  Jardim  Granja  -  CEP 18 12227-010, São José dos Campos, SP - Brazil 

- 19 8  Federal  University  of  São  João  del-Rei  (UFSJ),  Praça  Frei  Orlando,  170  -  Centro,  São  João  del-Rei  - 20 MG, 36307-352, Brazil 

- 21 9  NOAA  National  Environmental  Satellite.  Data,  and  Information  Service  (NESDIS),  1335  East-West 22 Highway, SSMC1, 8th Floor, Suite 8300, Silver Spring, MD 20910, USA 

- 23 

- 24 _Correspondence to_ : Jordan Schnell (jordan.schnell@colorado.edu) 

- 25 

26 

27 

1 

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





# 28 **Abstract** 

29 The  Rapid  Refresh  model  coupled  to  Chemistry  (RAP-Chem)  is  an  experimental  forecast  model  built  and  operated  by  the 30 NOAA  Global  Systems  Laboratory  (GSL).  The  RAP-Chem  is  a  full  chemistry  extension  to  the  operational  smoke 31 forecasting  model,  RAP-Smoke.  RAP-Chem’s  chemistry  includes  a  reduced  complexity,  carbon-bond,  gas-phase  mechanism 32 and  an  aerosol  scheme  that  are  coupled  together  to  produce  secondary  aerosols  and  perform  heterogeneous  chemistry.  The 33 model  includes  chemical  lateral  boundary  conditions,  hourly  anthropogenic  emissions  and  online  emissions  from  biomass 34 burning,  dust,  sea  salt,  and  biogenic  sources.  RAP-Chem  also  includes  the  direct  aerosol  effect  on  radiation  and  photolysis 35 and  a  simplified  indirect  aerosol  effect  that  couples  prognostic  aerosols  to  representative  aerosols  in  the  aerosol-aware 36 microphysics  scheme.  The  default  ‘offline’  vertical  mixing  implemented  in  WRF-Chem  is  updated  to  instead  mix  chemical 37 species  alongside  other  scalars  in  the  model’s  planetary  boundary  layer  (PBL)  scheme,  which  tends  to  improve  predictions 38 across  species  -  increasing  surface  ozone  (O  3  )  and  decreasing  less  reactive  tracers  (e.g.,  CO).  Sub-grid  boundary  layer  clouds 39 in  the  PBL  scheme  are  also  coupled  to  a  WRF-Chem  photolysis  scheme  for  the  first  time,  overall  reducing  O  3  biases  in  the 40 eastern  US.  Here  we  present  the  ability  of  the  RAP-Chem  model  to  simulate  the  extreme  North  American  wildfires  in  2020. 41 We  demonstrate  that  the  relatively  simple  gas-phase  chemical  mechanism  alongside  our  model  physics  developments  and 42 coupling  with  chemistry  can  predict  maximum  daily  8-h  average  O  3  with  exceptional  skill  (Normalized  Mean  Bias  (NMB)  = 43 6.6%)  averaged  over  CONUS,  improving  on  simulations  that  neglect  the  direct  aerosol  effect  (NMB  =  9.5%).  Ozone  biases 44 are  large  in  regions  with  extreme  aerosol  loading,  but  the  NMB  improves  more  significantly.  The  model  produces  the 45 observed  extreme  aerosol  loading  with  less  skill;  tending  to  underpredict  extreme  wildfire  induced  concentrations  while 46 overpredicting  urban  particle  pollution.  As  with  O  3  ,  daily  average  PM  2.5  is  predicted  with  better  skill  when  the  direct  aerosol 47 feedback  is  included  (-15.8%  vs.  -16.8%).  Overall  we  find  that  improving  the  coupling  between  chemistry  and  physics 48 processes in the air quality model improves its predictions of both weather and atmospheric composition. 

# 49 **1 Introduction** 

50 Timely  and  accurate  air  quality  forecasts  are  essential  tools  to  protect  public  health,  particularly  in  areas  heavily  influenced 51 by  urban  and/or  wildfire  emissions.  The  Rapid  Refresh  assimilation  and  forecasting  model  (RAP-Smoke;  Benjamin  et  al., 52 2016 )  is  an  hourly-updating  system  that  has  been  providing  operational  predictions  of  meteorology  and  wildfire  smoke  at 53 NOAA  since  December,  2020.  The  RAP-Smoke  is  built  off  of  the  Weather  Research  and  Forecasting  model  (WRF; 54 (Skamarock  et  al.,  2008;  Powers  et  al.,  2017)  with  the  Advanced  Research  WRF  (ARW)  dynamical  core,  with  smoke 55 emissions  and  plume  rise  parameterizations  built  off  of  the  WRF  coupled  to  chemistry  (i.e.,  WRF-Chem;  Grell  et  al.,  2005 ). 56 WRF-Chem  is  the  air  quality  component  of  WRF  and  contains  a  range  of  emission  source  schemes,  chemical  mechanisms, 57 and  feedbacks  to  physics.  Experimental  forecasts  were  produced  with  RAP-Smoke  at  the  NOAA  Global  Systems  Laboratory 58 (GSL)  during  its  development,  and,  as  an  experimental  follow-on  to  this  project,  we  have  coupled  additional  WRF-Chem 59 chemistry packages to the RAP in an effort to build a more comprehensive air quality modeling system described herein. 

2 

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





60 

61 WRF-Chem  is  considered  a  “fully  coupled”  air  quality  model  in  that  air  composition  is  allowed  to  provide  a  forcing  on 62 forecasted  meteorology  (Grell  et  al.,  2005) .  Additionally,  the  chemical  and  meteorological  tracers  of  WRF-Chem  share  the 63 same  grid  and  advection  schemes,  and  optionally  the  same  time  step.  This  differs  from  an  “offline”  model  where  the 64 meteorological  forcing  is  obtained  through  a  meteorology-only  simulation  prior  to  the  chemical  simulation.  Moreover,  the 65 meteorology  only  simulation  need  not  be  on  the  same  grid  as  the  subsequent  chemistry  simulation  (i.e.,  the  meteorological 66 fields  are  interpolated  in  both  time  and  space).  Indeed,  the  RAP/HRRR-Smoke  system  includes  the  direct  aerosol  effect  by 67 including  extinction  due  to  smoke  in  its  radiation  module  (Benjamin  et  al.,  2016) .  However,  RAP/HRRR-Smoke  only 68 simulates  a  single  smoke  aerosol  tracer,  and  so  the  aerosol  feedback  is  routinely  underestimated  due  to  other  missing  aerosol 69 sources  (e.g.,  anthropogenic  activities,  dust,  etc.),  which  likely  contributes  to  the  bias  in  HRRR  (James  et  al.,  2022) . 70 Moreover,  the  impact  of  aerosols  on  radiation  is  calculated  via  a  look-up-table  approach  as  opposed  to  a  physically-based 71 calculation of extinction (e.g., Mie theory) that can take into account aerosol size and mixing state. 

## 72 

73 While  WRF-Chem  is  considered  “fully-coupled”,  there  are  still  inconsistencies  between  physics  and  chemistry.  For  example, 74 with  the  exception  of  the  ACM2  planetary  boundary  layer  (PBL)  scheme  (Pleim,  2007) ,  the  vertical  mixing  of 75 meteorological  tracers  in  WRF-Chem  is  handled  separately  from  the  vertical  mixing  of  chemical  tracers.  Instead,  an 76 exchange  coefficient  is  diagnosed  in  the  PBL  scheme  and  passed  to  a  separate  dedicated  vertical  mixing  routine  in  the 77 chemistry  code,  which  only  performs _local_ mixing  (i.e.,  only  mixing  between  adjacent  layers).  Thus  if  a  user  selects  a 78 non-local  PBL  scheme,  the  vertical  mixing  of  meteorological  and  chemical  tracers  will  be  inconsistent.  The 79 RAP/HRRR-Smoke  system  uses  the  Mellor–Yamada–Nakanishi–Niino  with  eddy-diffusivity  /  mass-flux  (MYNN-EDMF) 80 adapted  from  Nakanishi  &  Niino  (2004,  2009) ,  which  like  ACM2  can  now  also  mix  all  chemical  species  both  locally  and 81 nonlocally.  The  MYNN-EDMF  scheme  produces  its  own  subgrid  cloud  macrophysics,  separate  from  the  microphysics  and 82 cumulus  parameterizations.  These  clouds  were  initially  coupled  to  the  RRTMG  radiation  schemes  (Benjamin  et  al.  2016, 83 Olson  et  al.  2026),  but  they  were  not  added  to  the  photolysis  schemes  in  WRF-Chem  (i.e.,  those  schemes  that  calculate  the 84 disassociation  of  molecules  due  to  sunlight).  Thus,  the  meteorological  parameterizations  would  receive  different  actinic 85 fluxes  than  those  in  chemistry.  A  similar  situation  exists  for  the  cumulus  parameterization:  until  WRF-Chem  v4.3  (released 86 May  2021),  convective  transport  of  chemical  tracers  could  only  be  performed  by  a  version  of  the  Grell-Devyani  cumulus 87 scheme  (Grell  &  Dévényi,  2002)  embedded  into  the  chemistry  code.  Accordingly,  unless  the  user  also  chose  to  use  the 88 Grell-Devyani  scheme  for  the  meteorological  cumulus  parameterizations,  meteorological  and  chemical  tracers  would  be 89 mixed  inconsistently.  Now  (Li  et  al.,  2019) ,  one  can  choose  the  Grell-Freitas  cumulus  scheme  (Grell  and  Freitas,  2014;  Li  et 90 al.,  2018) ;  used  only  in  RAP-Smoke  and  RAP-Chem,  not  HRRR  to  simultaneously  advect  meteorological  and  chemical 91 tracers,  as  well  as  represent  aerosol  wet  scavenging.  Finally,  there  is  the  chemistry  connection  to  microphysics.  WRF-Chem 92 v4.6  has  two  microphysics  schemes  ( Morrison  et  al.  (2005)  and  Lin  et  al.  (1983) )  that  are  coupled  to  chemistry  such  that 93 aerosols  are  allowed  to  act  as  cloud  condensation  and  ice  nuclei  (CCN  and  IN).  However,  these  schemes  require  a  chemical 

3 

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





94 mechanism  that  distinguishes  cloud-borne  vs.  interstitial  aerosols,  essentially  doubling  the  number  of  aerosol  tracers,  which 95 significantly  increases  the  computational  cost  of  a  simulation.  The  Thompson-Eidhammer  microphysics  scheme  used  in 96 RAP/HRRR-Smoke  (Thompson  and  Eidhammer,  2014)  takes  a  more  simplified  approach,  and  is  “aware”  of  two  aerosol 97 types,  water-friendly  aerosols  (WFA)  and  ice-friendly  aerosols  (IFA),  which  are  completely  separate  from  the  chemical 98 parameterizations  and  based  on  climatology.  Though,  recent  efforts  have  been  made  to  couple  prognostic  aerosols  with  the 99 Thompson-Eidhammer  MP  scheme,  which  improved  cloud  cover  predictions  of  HRRR  during  the  September  2020  North 100 American wildfires  (Conrick et al., 2021) 

101 

102 In  this  work,  we  further  couple  the  WRF-Chem  chemistry  packages  to  the  RAP  weather  forecast  model,  addressing  the 103 aforementioned  chemistry-physics  coupling  inconsistencies.  We  produce  a  24  h  forecast  for  each  day  of  the  1  August  – 30 104 September,  2020  extreme  wildfire  season  in  an  effort  to  demonstrate  the  model  improvements  as  a  result  of  including  tighter 105 coupling  between  chemistry  and  physics.  The  manuscript  is  structured  as  follows:  In  Section  2,  we  describe  the  RAP-Chem 106 model  and  code  developments,  our  experimental  configurations,  and  the  observational  datasets  we  use  to  verify  our  model. 107 Section  3  presents  our  results,  starting  with  a  large-scale  overview  of  model  performance  and  a  focus  on  wildfire-influenced 108 regions.  We  then  highlight  the  impacts  that  several  chemistry-physics  couplings  have  on  forecast  skill.  Our  conclusions  are 109 presented in Section 4. 

# 110 **2 Data and Methods** 

# 111 **2.1 RAP-Chem** 

112 We  use  an  experimental  version  of  the  Rapid  Refresh  (RAP),  which  is  based  on  the  WRF  version  3.9  with  significant 113 modifications  to  the  physics  and  dynamics  packages  (e.g.,  see  (Benjamin  et  al.,  2016) .  The  experimental  RAP-Chem  forecast 114 (https://rapidrefresh.noaa.gov/RAPchem/)  has  been  running  at  NOAA  GSL  since  August  2020.  The  experiments  herein  use 115 the source code and static fields as of the 17 August 2024 06Z forecast. 

116 

117 RAP-Chem  is  run  with  51  vertical  levels  from  the  surface  to  10  hPa  at  a  13.5  km  horizontal  resolution  over  a  domain  that 118 includes  North  and  Central  America,  as  well  as  parts  of  South  America,  Europe,  and  Asia  (Fig.  S1a).  The  lowest  model  layer 119 is  ~8m  thick,  with  the  first  ~8  layers  in  the  lowest  1  km  of  the  atmosphere;  Fig.  S1b  shows  the  eta  levels  provided  to  the 120 WRF  Preprocessing  System  (WPS).  RAP-Smoke  uses  a  meteorological  and  chemical  timestep  of  60  s,  however  here  we  use 121 72  s  to  reduce  computation  (within  the  WRF  recommended  timestep  =  6*∆x);  no  model  instability  issues  occurred  using  this 122 reduced  timestep.  Initial  and  time-varying  boundary  conditions  are  provided  by  the  Global  Forecast  System  v16  (GFS, 123 https://www.nco.ncep.noaa.gov/pmb/products/gfs/).  Chemical  boundary  conditions  come  from  the  RAQMS  forecast  model 124 from  the  University  of  Wisconsin  (Bruckner  et  al.,  2024) .  An  important  consideration  is  that  the  operational  RAP-Smoke 125 undergoes  extensive  meteorological  data  assimilation  (Benjamin  et  al.,  2016)  and  the  real-time  RAP-Chem  utilizes  the 

4 

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





126 assimilated  input  and  boundary  conditions.  Here,  however,  we  do  not  perform  any  data  assimilation  and  so  meteorological 127 performance  is  almost  surely  degraded  from  that  of  a  simulation  with  full  data  assimilation.  The  model  physics  options 128 include  the  Thompson-Eidhammer  microphysics  scheme  (Thompson  and  Eidhammer,  2014) ,  the  Grell-Freitas  cumulus 129 scheme  (GF;  Freitas  et  al.,  2021)  with  convective  removal  and  parameterized  aqueous  chemistry  turned  off.  We  use  the 130 Mellor–Yamada–Nakanishi–Niino  eddy-diffusivity  mass-flux  (MYNN-EDMF)  boundary  layer  (Olson  et  al.  2026)  and 131 surface  layer  scheme  (Olson  et  al.  2021)  with  modifications  (see  Sect.  2.1.1)  and  the  Rapid  Update  Cycle  (RUC)  land  model 132 (Smirnova  et  al.,  2016) .  For  radiation,  we  use  the  Rapid  Radiative  Transfer  Model  for  GCMS  (RRMTG;  (Clough  et  al., 133 2005) )  for  both  shortwave  and  longwave  radiation  schemes  and  improve  physics  coupling  by  supplying  RRTMG  with 134 prognostic  O  3 profiles.  For  photolysis  we  use  the  updated  TUV  scheme  (Madronich  and  Flocke,  1997)  with  several 135 modifications.  We  supply  the  TUV  with  GFS  total  O  3  columns  to  improve  photolysis  rate  calculations.  We  also  supply  TUV 136 with  the  subgrid  clouds  simulated  by  the  MYNN-EDMF  (see  Sect.  2.1.1  and  Sect.  3.4.2).  Also  included  in  the  model  is  wet 137 removal  from  resolved  precipitation  (offline,  see  below),  updated  convective  wet  scavenging  (Li  et  al.,  2019,  2018) ,  dry 138 deposition, and gravitational settling. 139 

140 For  gas-phase  chemistry,  we  use  a  reduced  carbon-bond  mechanism  based  on  Houweling  et  al.  (1998)  with  several 141 modifications.  The  choice  of  the  mechanism’s  starting  point  and  subsequent  modifications  were  generally  performed  with 142 the  goal  of  reducing  the  computational  burden  of  the  mechanism  while  increasing  complexity.  First,  we  do  not  include  the 143 transport  of  radical  species  or  simulate  the  elemental  odd-oxygen  species  O<sup>3</sup> (P)  or  O<sup>1</sup> (D),  instead  parameterizing  them  within 144 the  photolysis  of  NO  2 and  O  3 like  in  the  Carbon  Bond  Mechanism  v4  (Gery  et  al.,  1989) .  We  also  do  not  simulate  methane, 145 instead  parameterizing  the  terminal  oxidation  products  using  a  globally  uniform  concentration  of  1.8  ppm.  A  similar 146 approach  is  used  for  H  2 with  a  fixed  concentration  of  531  ppb.  We  also  added  monoterpenes,  sesquiterpenes, 147 2-methyl-3-buten-2-ol  (MBO),  and  IVOC  (an  intermediate  volatility  VOC)  and  their  oxidation  reactions  with  OH,  O  3  ,  and 148 NO  3  to  improve  the  secondary  organic  aerosols  (SOA)  simulations.  We  additionally  updated  reaction  rates  and  included  the 149 necessary  oxidation  of  organic  condensable  vapors  to  simulate  SOA.  We  also  include  heterogeneous  loss  of  N  2  O  5  using  a 150 modified  parameterizations  from  the  T1_MOZCART  chemical  mechanism  (Schwantes  et  al.,  2020) .  For  SOA,  we  use  a 151 simplified  version  of  the  MADE  VBS-SOA  mechanism  described  in  Ahmadov  et  al.  (2012)  similar  to  WRF-Chem’s 152 _chem_opt_ =  108.  We  have  also  extended  our  mechanism  using _chem_opt_ =  109  as  a  template  for  including  cloud-borne 153 aerosols  species  to  explicitly  simulate  the  indirect  aerosol  effect,  though  the  results  are  beyond  the  scope  of  this  paper.  The 154 gas-phase  mechanism  contains  97  reactions  among  48  species,  of  which  41  are  transported.  The  aerosol  mechanism  consists 155 of  42  species,  three  of  which  are  the  number  concentrations  of  the  three  aerosol  modes  (Aitken,  accumulation,  and  coarse). 156 The  real-time  RAP-Chem  includes  two  additional  aerosol  species  representing  coarse  and  fine  pollen,  whose  emissions  are 157 based  on  the  Pollen  Emission  for  Climate  Models  (PECM;  (Wozniak  and  Steiner,  2017) );  the  emissions  of  these  species  are 158 not  included  in  the  experiments  herein,  and  will  instead  be  described  in  a  follow-up  manuscript.  Together,  the  complete 159 chemical  mechanism  (gases,  primary  and  secondary  aerosols)  consists  of  only  90  species,  significantly  fewer  than 

5 

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





160 operational  air  quality  models  (e.g.,  the  US  AQM/NAQFC  during  our  simulation  period  simulated  155  species 161 (https://www.emc.ncep.noaa.gov/mmb/aq/AQChangelog.html)). 

162 

163 Anthropogenic  emissions  are  designed  to  reflect  July  2020,  COVID-19  conditions,  those  used  in  the  real-time  forecasts  for 164 the  2020  period  as  described  in  (He  et  al.,  2023) .  Over  CONUS,  the  onroad  and  nonroad  portion  of  our  emission  datasets  are 165 based  on  the  methodology  of  the  gridded  Fuel-Based  Inventory  of  Vehicle  Emissions  (FIVE;  see  (McDonald  et  al.,  2018) ), 166 which  is  extremely  well-suited  to  capture  rapid  adjustments  to  the  transportation  sector  as  occurred  during  COVID-19. 167 Reductions  in  fuel  sales  also  led  to  decreases  in  oil  and  gas  refining  as  well  as  refueling  emissions  (i.e.,  fugitive  VOCs)  and 168 so  use  another  fuel  use  based  emission  inventory  (FOG;  (Francoeur  et  al.,  2021) )  for  oil  and  gas  NOx  and  VOC  emissions. 169 Increased  emissions  from  volatile  chemical  products  (VCPs),  key  components  of  urban  ozone  and  SOA  formation,  was  also 170 likely  from  more  frequent  and  widespread  cleaning  and  disinfecting  (McDonald  et  al.,  2018) .  Area  VCP  emissions 171 (dominant  sector)  are  modified  based  on  the  VCP  emission  inventory  for  2018  (see  (Coggon  et  al.,  2021;  Stockwell  et  al., 172 2021)  ).  Other  anthropogenic  sectors  (e.g.,  power  generation,  agriculture)  were  largely  unaffected  by  the  COVID-19 173 disruptions.  In  any  case,  where  possible  for  point  sources,  we  use  the  Continuous  Emission  Monitoring  System  (CEMS)  and 174 rely  on  the  NEI-2017  v1  baseline  for  those  sources  not  reported  by  CEMS.  Outside  of  CONUS  we  use  the  CEDS-2017 175 inventory  (McDuffie  et  al.,  2020) .  The  emissions  have  a  diurnal  profile  and  are  delineated  by  weekday,  Saturday,  or  Sunday. 176 Daily  wildfire  emissions  are  generated  using  the  fire  radiative  power  (FRP)  method  of  the  RAP/HRRR-Smoke  (Ahmadov  et 177 al.,  2017;  Chow  et  al.,  2022;  Dowell  et  al.,  2022)  and  expanded  to  include  emissions  of  gases  and  aerosols  relevant  to  our 178 chemical  mechanism  using  (Andreae,  2019) .  Sea  salt  emissions  are  calculated  online  based  on  the  routines  developed  for  the 179 MADE  aerosol  module  in  WRF-Chem.  Dust  emissions  are  calculated  online  with  the  FENGSHA  dust  scheme  (Campbell  et 180 al., 2022) . 

# 181 **2.1.1 Improvements to PBL mixing of chemical tracers** 

182 As  described  in  the  introduction,  the  default  WRF-Chem  is  configured  to  perform  vertical  mixing  of  chemical  tracers 183 alongside  dry  deposition  in  the  chemical  driver  using  exchange  coefficients  passed  from  the  PBL  driver.  Only  local  mixing 184 occurs,  even  if  using  a  non-local  PBL  scheme.  Here  we  update  the  MYNN-EDMF  PBL  scheme  to  enable  it  to  mix  chemical 185 tracers  alongside  the  meteorological  transported  scalars  (Olson  et  al.,  2026) .  The  effect  of  this  update  is  to,  by  default, 186 perform  non-local  vertical  mixing  inside  the  MYNN-EDMF  PBL  driver  as  opposed  to  dry_dep_driver  when  using  the 187 MYNN-EDMF  PBL  scheme.  During  shallow,  typically  nighttime,  boundary  layers,  surface  emissions  in  a  chemical  transport 188 model  can  be  unrealistically  trapped  near  the  surface  due  to  misrepresentations  of  mechanical  turbulence,  which  can  lead  to 189 artificially  elevated  levels  of  primary  pollutants  or  artificially  low  O  3 due  to  excessive  NO  x  titration  [Huszar  et  al.,  2018a,b; 190 2020;  and  references  therein].  WRF-Chem  attempts  to  remedy  this  by  modifying  the  exchange  coefficients  received  from  the 191 PBL  driver  over  large  emissions  sources  to  simulate  unresolved  mixing  (e.g.,  traffic  turbulence,  heat  flux  from  urban  areas 192 and  fires).  The  updated  exchange  coefficient  is  not  passed  back  to  the  meteorological  model.  The  modification  in  the 

6 

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





193 unmodified  WRF-Chem  sets  a  minimum  exchange  coefficient  in  the  first  11  model  layers  to  1.0  m<sup>2</sup> s<sup>-1</sup> if  there  is  any  CO 194 emitted  by  anthropogenic  sources.  This  minimum  increases  to  2.0  m<sup>2</sup> s<sup>-1</sup> throughout  one-half  the  model’s  vertical  levels  if 195 there  are  any  wildfire  CO  emissions  or  when  the  anthropogenic  emissions  of  CO  (or  unspeciated  PM  2.5  )  are  greater  than  200 196 mol  km<sup>-2</sup> h<sup>-1</sup> (0.168  µg  m<sup>-2</sup> s<sup>-1</sup> ).  We  also  include  an  artificial  enhancement  in  the  updated  MYNN-EDMF,  however,  here  we 197 do  so  as  a  function  of  emissions  of  nitrogen  oxide  (NO)  and/or  FRP,  and  only  when  the  PBL  height  is  less  than  100  m. 198 Equations  (S1–S3)  describe  the  formulation  of  the  enhancements,  where _khdz(k)_ is  the  MYNN-EDMF  PBL  scheme 199 exchange  coefficient  at  model  layer _k_ normalized  by  the  height  ( _dz)_ and  density  ( _rho_ )  of  the  layer, _emis_ant_no_ are  the 200 anthropogenic  emissions  of  NO  and _no_threshold_ is  set  to  10  mol  km<sup>-2</sup> h<sup>-1</sup> Finally,  as  described  above,  we  also  couple  the 201 MYNN-EDMF-simulated  subgrid  water  and  ice  clouds  to  the  TUV  photolysis  scheme  following  the  same  logic  as  the 202 already implemented subgrid Grell-Freitas cumulus scheme clouds (also included here). 

# 203 **2.1.2 Aerosol feedbacks** 

204 RAP-Chem  utilizes  the  WRF-Chem  optical  driver  with  volume  averaging  in  the  Mie  (Fast  et  al.,  2006)  calculations 205 ( _aer_op_opt_ =  1)  to  calculate  aerosol  extinction  over  four  predefined  wavelengths.  Aerosols  are  removed  via  wet  scavenging 206 from  resolved  ( _wetscav_onoff_ =  -1)  and  convective  ( _conv_tr_wetscav_ =  1)  precipitation.  The  resolved  removal  is  considered 207 to  be  an  “offline”  approach  since  the  routine  is  called  from  the  chemistry  driver  as  opposed  to  the  microphysics;  the 208 convective  removal  is,  however,  another  example  of  tight  chemistry-physics  coupling  since  it  occurs  inside  the  Grell-Freitas 209 cumulus  scheme  (Li  et  al.,  2019,  2018) .  We  have  also  included  a  simplified  indirect  effect  in  all  of  the  RAP-Chem 210 experiments  by  coupling  the  prognostic  aerosols  to  the  water-friendly  and  ice-friendly  aerosols  (WFA  and  IFA,  respectively) 211 simulated  by  the  Thompson-Eidhammer  microphysics  scheme.  Equations  1-2  in  H.  Li  et  al.  (2024)  describe  the  conversion 212 of  prognostic  aerosol  mass  mixing  ratio  (µg  kg<sup>-1</sup> )  to  number  concentrations  (kg<sup>1-</sup> ).  In  RAP-Chem,  IFA  is  fine  mode  dust  and 213 WFA  consists  of  the  aitken  mode  fractions  of  ammonium  (NH  4  ),  sulfate  (SO  4  ),  POA,  SOA  as  well  as  sodium  and  chloride 214 (i.e.,  sea  salt).  Simulating  the  indirect  effect  in  WRF-Chem  typically  requires  a  doubling  of  the  number  of  aerosols  (i.e., 215 interstitial  and  cloud-borne  equivalents)  whereas  in  this  approach,  we  utilize  tracers  already  included  in  the  model,  thus 216 having  only  a  negligible  impact  on  forecast  wallclock  time.  Evaluating  the  sensitivity  of  this  parameterization  is  beyond  this 217 work, however, it is another important chemistry-physics connection included in our model. 

# 218 **2.2 Experiments** 

219 We  perform  six  simulations  of  varying  length  and  complexity  in  an  effort  to  demonstrate  the  model’s  fidelity  at  producing 220 accurate  air  quality  forecasts  and  to  quantify  and  demonstrate  the  improvements  in  the  model  due  to  improved 221 physics-chemistry coupling (Table 1). 

222 

223 

7 

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





**Table 1.** RAP-Chem experiments and configurable options. 

|**Experiment**<br>**Name**|**Chemistry**<br>**Mixing**|**Enhanced**<br>**Mixing**|**Wildfire**<br>**Plumerise**|**Direct**<br>**Feedback**|**PBL-Photolysis**<br>**Feedback**|**Simulation**<br>**Period (2020)**|
|---|---|---|---|---|---|---|
|**_control_**|MYNN-EDMF|yes|yes|yes|yes|1 Aug – 30 Sep|
|**_no_dirfdb_**|MYNN-EDMF|yes|yes|no|yes|1 Aug – 30 Sep|
|**_newmix_**|MYNN-EDMF|no|no|no|yes|1-7 Aug|
|**_oldmix_**|WRF-Chem|no|no|no|yes|1-7 Aug|
|**_enhmix_**|MYNN-EDMF|yes|no|no|yes|1-7 Aug|
|**_phtmix_**|MYNN-EDMF|yes|no|no|no|1-7 Aug|



224 

225 Our  primary  experiment  ( _control_ )  covers  a  two  month  period  (1  August  –  30  September,  2020)  during  which  the  US 226 experienced  sustained  poor  air  quality  due  to  massive  wildfires  burning  in  the  West  (e.g.,  Zhou  et  al,  2021,  Higuera  et  al., 227 2021).  Figure  S2  shows  the  integrated  FRP  over  the  time  period  highlighting  two  distinct  burning  periods,  though  the 228 integrated  FRP  during  September  was  more  than  double  that  in  August.  The _control_ experiment  includes  all  of  the  improved 229 physics-chemistry  coupling  described  above,  and  we  consider  it  to  be  our  reference  experiment.  The  experiment _no_dirfdb_ 230 turns  off  the  direct  aerosol  effect  ( _aer_ra_feedback  =_ 0),  and  is  also  simulated  over  the  full  two-month  period.  Four 231 simulations  are  used  to  quantify  changes  due  to  the  updates  to  MYNN-EDMF  (Sect.  2.1.1).  The _oldmix_ simulation  performs 232 mixing  following  the  default  mixing  method  of  WRF-Chem  v3.9  (Powers  et  al.,  2017;  Skamarock  et  al.,  2008)  with  one 233 modification  to  the  source  code:  In  the  original  WRF-Chem  subroutine _dry_dep_driver_ ,  the  exchange  coefficients  obtained 234 from  the  PBL  scheme  are  artificially  enhanced  in  half  of  the  vertical  levels  for  grid  cells  with  fire  emissions  or  large 235 anthropogenic  emissions  (so  long  as  urban  physics  is  not  in  use  (i.e., _sf_urban_physics_ =  0)  and  CO  is  an  emitted  species). 236 For _oldmix_ ,  we  turn  off  this  default  enhanced  mixing.  The  experiment _newmix_ utilizes  the  updated  mixing  code,  also  not 237 including  the  enhancement  routines  described  above.  An  additional  sensitivity  experiment  ( _enhmix_ )  is  conducted  to 238 demonstrate  the  utility  of  enhanced  mixing  inside  the  MYNN-EDMF  scheme  over  urban  and  wildfire  grid  cells.  In  a  final 239 experiment,  ( _phtmix_ ),  we  do  not  include  the  effect  of  subgrid  clouds  simulated  by  MYNN-EDMF  in  the  photolysis  scheme. 240 In  all  * _mix_ experiments,  we  do  not  invoke  the  wildfire  plume  rise  parameterization  such  that  no  other  routines  impact  the 241 vertical  redistribution  of  emissions  and  a  fair  comparison  between  the  old  and  new  mixing  routines  can  be  made.  Moreover, 242 we  also  do  not  simulate  aerosol  feedback  to  meteorology  (i.e.,  like _no_dirfdb_ ).  As  such,  we  focus  on  the  1-7  August  2020 243 time  period  for  the  * _mix_ experiments  to  avoid  simulating  a  period  with  an  excessive  number  of  fires  in  the  domain  (see  Fig. 244 S2).  We  initialize  the  forecasts  at  00Z  each  day  with  GFSv16  meteorological  fields;  chemical  fields  are  cycled  between 245 successive  simulations  (i.e.,  no  chemistry  initializations  beyond  the  first  day  initialized  with  RAQMS).  We  consider  the  first 246 3  days  (29-31  July,  2020)  of _control_ a  spin-up  period  and  discard  from  the  analysis.  The _no_dirfdb,_ and  * _mix_ experiments  are 247 initialized  on  1  August  2020  and  branch  from _control_ .  All  of  our  experiments  cover  the  entire  RAP  domain,  though  we 248 frequently display results over CONUS or one of the 10 US EPA regions (EPA, 2025). 

8 

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





# 249 **2.3 Observations** 

250 To  evaluate  the  RAP-Chem  experiments,  we  use  a  variety  of  surface  and  remotely-sensed  observational  datasets.  For 251 meteorological  evaluation,  we  use  the  NOAA  Integrated  Surface  Database  (ISD,  also  referred  to  as  ISH/ISH-lite; 252 https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database),  using  observations  of  2-m  temperature 253 (T  2m  ),  2-m  dew  point  temperature  (Td  2m  ),  10-m  wind  speed  (U  10m  ),  visibility  (VIS),  and  precipitation.  We  also  utilize 254 measurements  of  total,  direct,  and  diffuse  downwelling  shortwave  radiation  from  seven  SURFRAD  and  five  SOLRAD  sites 255 across  CONUS  (Augustine  et  al.,  2005,  2000)  operated  by  NOAA  Global  Monitoring  Laboratory  (GML).  For  air 256 composition,  we  primarily  use  the  USA  EPA  AirNOW  network  (https://www.airnow.gov/about-the-data/),  which  includes 257 stations  in  the  US,  Canada,  and  Mexico.  This  data  is  provided  in  near  real-time  and  is  best  suited  for  real-time  evaluation  of 258 forecast  models.  Composition  variables  considered  include  surface  O  3  ,  PM  2.5  ,  nitrogen  dioxide  (NO  2  ),  and  carbon  monoxide 259 (CO).  We  also  utilize  NASA’s  AErosol  RObotic  NETwork  (AERONET;  Holben  et  al.,  1998,  2001)  stations  to  perform 260 verification  of  aerosol  optical  depth  at  550  nm  (AOD  550)  ).  We  also  utilize  NASA’s  AQUA  AIRS  retrievals  of  CO  vertical 261 profiles ( https://airs.jpl.nasa.gov/mission/overview/ ). 

# 262 **3 Results** 

# 263 **3.1 Meteorological performance** 

264 We  evaluate  the  meteorological  performance  of _control_ against  surface  measurements  from  the  NOAA  ISD  using  the  newly 265 developed  MELODIES  MONET,  a  modular  framework  that  integrates  diverse  atmospheric  chemistry  observational  datasets 266 with chemistry model results for the evaluation of air quality and atmospheric composition 267 <u>( https://melodies-monet.readthedocs.io/en/stable/ ).  Fig.  S3  shows  the  spatial  bias  plots  for  T  2m  ,  Td  2m  ,  U  10m  ,  VIS,  and  the  time</u> 268 series  of  total  daily  precipitation  over  the  RAP-Chem  domain.  In  general,  the  model  performs  very  well  for  each  of  the 269 meteorological  parameters,  which  is  somewhat  expected  given  that  the  foundation  of  the  RAP-Chem  is  the  operational 270 numerical  weather  prediction  (NWP)  forecast  system,  RAP-Smoke  (though  here  we  do  not  include  the  data  assimilation  or 271 hourly  cycling  that  is  performed  in  RAP-Smoke).  T  2m is  generally  biased  low  (about  -1°C)  in  much  of  Canada,  Mexico,  and 272 the  eastern  US,  while  biased  high  (~1–3°C)  over  the  western  regions  heavily  impacted  by  smoke,  initially  indicating  a  low 273 bias  in  simulated  aerosols  and/or  their  radiative  extinction.  Averaged  over  CONUS,  the  mean  bias  (MB)  is  very  small 274 (-0.1°C).  Td  2m is  generally  well  simulated  (CONUS  MB  =  -0.4°C)  except  for  the  smoke  influenced  regions  where  it  is  biased 275 low  by  2–5°C.  Wind  Speed  is  generally  biased  high  (~0–2  m  s<sup>-1</sup> )  though  there  are  some  small  negative  biases  in  the  US  West. 276 Visibility  diagnostics  are  often  utilized  by  those  in  aviation,  and  accurate  forecasts  are  critical  to  maintaining  smooth  flight 277 operations.  RAP-Chem  uses  the  same  visibility  diagnostics  as  the  operational  RAP/HRRR-Smoke  system,  though  in 278 RAP-Chem,  aerosols  beyond  smoke  are  accounted  for  in  the  extinction  calculation.  Outside  of  the  central  US  where 279 RAP-Chem  is  biased  low  in  visibility  (0–2  km),  visibility  is  generally  overpredicted,  up  to  5  km  greater  than  observations  in 

9 

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





280 the  most  heavily  smoke-influenced  regions  (CONUS  MB  =  2067  m).  Paired  with  the  temperature  biases,  these  biases 281 indicate  large  underestimations  in  near  surface  smoke  concentrations.  Precipitation  is  biased  slightly  high  averaged  over 282 CONUS  (~0.1  mm),  though  much  larger  underestimations  (>2  mm)  are  found  in  the  central  United  States  through  the  path  of 283 Hurricane Laura where daily rainfall totals exceeded 25 mm (not shown). 

# 284 **3.2 Surface air quality and AOD performance** 

285 Figure  1a-b  shows  the  1  August  –  30  September,  2020  time  series  of  RAP-Chem  simulated  maximum  daily  8-h  average 286 (MDA8)  surface  O  3 and  24-h  averaged  PM  2.5 compared  with  EPA  AirNOW  monitors  in  the  CONUS.  Figures  S4-S5  show 287 the  same  time  series  over  each  of  the  10  EPA  regions  as  well  as  the  average  observed  values  over  the  time  period  for  each 288 station  overlain  on  the  average  field  of  each  model  simulation.  The  normalized  mean  bias  (NMB)  for  each  simulation 289 compared to each EPA region over each of the experiment’s respective simulation periods is in Table 2. 

290 

**Table 2.** Normalized Mean Bias (NMB, %) for MDA8 O  3 (ppb) and 24-h average PM  2.5 (µg m<sup>-3</sup> ) over 1 August - 30 September, 2020 for _control_ and _no_dirfdb_ and 1-7 August, 2020 for _*mix_ . 

|**O 3**|**_US_**|**_R1_**|**_R2_**|**_R3_**|**_R4_**|**_R5_**|**_R6_**|**_R7_**|**_R8_**|**_R9_**|**_R10_**|
|---|---|---|---|---|---|---|---|---|---|---|---|
|_control_|6.6|13.3|10.8|6.1|14.1|-1.5|1.7|-0.7|-1.1|11.2|22.4|
|_no_dirfdb_|9.5|15.2|13.3|8.2|14.7|1.4|-3.5|2.3|2.2|15.9|33.7|
|_oldmix_|4.3|14.1|10.3|1.9|2.5|1.7|-4.8|-6.4|-3.0|17.5|14.5|
|_newmix_|4.6|13.7|8.6|2.1|2.3|3.7|-13.6|-4.7|-2.2|17.5|16.0|
|_enhmix_|4.6|13.7|8.5|2.1|2.3|3.8|-4.8|-4.5|-2.2|17.4|16.0|
|_phtmix_|8.2|15.8|12.8|8.1|9.7|10.0|-1.4|-1.5|-2.0|16.3|16.3|
|**PM2.5**|**_US_**|**_R1_**|**_R2_**|**_R3_**|**_R4_**|**_R5_**|**_R6_**|**_R7_**|**_R8_**|**_R9_**|**_R10_**|
|_control_|-15.8|3.0|89.5|53.9|39.6|25.6|22.6|33.9|-17.5|-34.0|-44.1|
|_no_dirfdb_|-16.8|3.7|88.1|53.7|39.4|25.8|23.3|34.3|-13.6|-34.0|-48.7|
|_oldmix_|10.9|-17.9|67.8|54.6|4.2|27.2|21.2|45.3|-10.6|2.5|-15.9|
|_newmix_|9.6|-17.9|66.9|49.0|0.3|26.9|18.8|46.9|-11.4|1.0|-16.3|
|_enhmix_|7.2|-19.1|54.2|47.0|-1.8|23.6|16.7|39.6|-13.3|0.0|-17.0|
|_phtmix_|10.9|-17.4|64.9|55.3|4.0|28.1|20.4|42.2|-12.5|-0.2|-16.7|



291 

292 

10 

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





293 



294 **Figure 1.** Time series (1 August – 30 September, 2020) of ( **a** ) MDA8 O  3  , ( **b)** daily average PM  2.5 observed by EPA AirNOW and ( **c** ) daily 295 average AOD  550 as observed by AERONET compared to those simulated by the _control_ and _no_dirfdb_ experiments. EPA AirNow data 296 courtesy of the U.S. Environmental Protection Agency. AERONET data courtesy of NASA. 297 

298 For  O  3  ,  RAP-Chem _control_ performs  well  over  CONUS  until  a  period  of  observed  sharp  decreases  in  O  3  during  the  first  half 299 of  September.  This  period  is  better  captured  by _control_ compared  to _no_dirfdb_ and  is  explored  in  Sect  3.3  and  3.5. 300 RAP-Chem _control_ matches  the  observational  variability  with  minimal  normalized  mean  bias  (NMB)  and  RMSE  in  all  EPA 301 regions  (NMB  =  -1.5%  to  22.4%;  RMSE  =  6.3  to 15.2  ppb).  Air  quality  models  frequently  demonstrate  high  O  3 biases  in 

11 

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





302 EPA  Region  4  (US  Southeast),  often  attributed  to  large  and  variable  sources  of  biogenic  (e.g.,  (Guo  et  al.,  2018)  and 303 agricultural  burning  emissions  (Tang  et  al.,  2022) .  In  EPA  Region  4,  RAP-Chem _control_ does  a  remarkable  job  during  the 304 first  half  of  the  month  of  August,  but  exhibits  a  ~2-3  ppb  systematic  bias  during  the  second  half  of  August  and  then  again 305 during  the  beginning  and  end  of  September  (Fig.  S4).  It’s  unclear  why  the  model  performs  poorly  here,  but  it  may  be  related 306 to  precipitation  events  not  properly  scavenging  precursor  species.  In  EPA  Region  5  (upper  Midwest),  RAP-Chem _control_ 307 performs  exceptionally  well  in  August,  with  the  only  notable  deficiency  being  slightly  underestimated  minima.  It  generally 308 captures  the  daytime  peaks  during  the  first  half  of  the  month,  but  is  biased  low  by  ~5  ppb  during  the  latter  half.  The  average 309 diurnal  profile  of  O  3  averaged  over  CONUS  and  each  of  the  EPA  regions  (Fig.  S6)  reveals  biases  are  often  positive  during 310 the  day  (8AM–8PM)  and  negative  at  night  (8PM–8AM),  resulting  in  a  more  pronounced  diurnal  cycle  as  compared  to  the 311 observations. Overall, the shape of the diurnal cycle of O  3  is captured well. 

312 

313 RAP-Chem  simulates  PM  2.5 with  less  skill  than  O  3  ,  largely  due  to  the  extreme  influence  from  the  wildfires  during  the 314 experimental  period,  but  also  partially  due  to  overestimated  emissions  in  urban  areas.  (i.e.,  many  EPA  AirNOW  monitors  are 315 located  in  urban  locations  with  significant  traffic  influence  and  therefore  can  overstate  the  influence  of  those  regions). 316 Indeed,  the  emissions  of  unspeciated  PM  2.5 were  logarithmically  transformed  to  limit  this  bias.  In  all  non-wildfire  source 317 regions  (R1-R7),  RAP-Chem  tends  to  largely  overestimate  both  the  variability  and  magnitude  of  PM  2.5  .  It  is  likely  that  the 318 diurnal  cycle  of  urban  (e.g.,  traffic)  emissions  needs  further  modification  given  the  location  of  the  biases  (cities)  and  the 319 species responsible. 

320 

321 Figure  1c  compares  observed  and  modeled  AOD  550 at  20  AERONET  sites  within  the  RAP-Chem  domain  for  the  simulation 322 period.  Overall,  RAP-Chem _control_ is  biased  low  in  AOD  550  at  most  locations  and  CONUS  (NMB  =  -17.5%),  resulting  from 323 a  combination  of  low  bias  in  simulated  PM  2.5 (Fig  1b),  incorrect  vertical  distributions  of  aerosols,  and/or  inaccurate 324 representations  of  the  aerosols’  refractive  indices.  Indeed,  if  AOD  550 is  instead  calculated  with  a  look-up-table  (LUT) 325 approach  based  on  the  EPA  IMPROVE  algorithm  (Malm  et  al.,  1994)  AOD  550 improves  at  some  sites  (e.g.,  Fig.  S7)  during 326 peak  extinction  periods,  but  the  LUT  approach  tends  to  significantly  overestimate  background  AOD  550  .  While  a 327 physically-based  approach  to  calculating  aerosol  extinction  is  often  desired,  some  forecast  systems  may  prefer  a  LUT 328 approach  that  can  be  easily  tuned  and  requires  minimal  computational  requirements  over  the  more  expensive  Mie-calculated 329 extinction used here and associated uncertainties in mixing state assumptions (e.g., volume averaging vs. internally mixed). 

# 330 **3.3 Wildfire region performance** 

331 The  August-September  2020  period  was  one  of  the  most  active  and  destructive  wildfire  seasons  in  the  Western  US  to  date. 332 EPA  Regions  8,  9,  and  10  were  significantly  inundated  by  heavy  smoke  as  well  as  an  influx  of  O  3 precursors  species  (i.e., 333 NO  x and  VOCs)  leading  to  sustained  poor  air  quality  in  all  three  regions  (e.g.,  Fig  S4-5,  (Higuera  and  Abatzoglou,  2021; 334 Zhou et al., 2021) . 

12 

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





335 

336 For  EPA  region  R8,  RAP-Chem  shows  generally  good  agreement  overall  for  both  O  3 and  PM  2.5 during  both  months.  In 337 August,  both _control_ and _no_dirfdb_ underestimate  peak  PM  2.5 abundances  (e.g.,  August  19-20,  24-26),  but  they  are  much 338 better  simulated  by _control_ .  For  O  3  ,  both  RAP-Chem  simulations  are  biased  low  through  August  and  biased  slightly  high  in 339 September,  though _control_ has  significantly  smaller  biases  compared  to _no_dirfdb_ ,  nearly  10  ppb  on  some  days.  In 340 September,  both  simulations  again  produced  excellent  PM  2.5 predictions  in  R8  outside  of  the  false  alarm  on  September  14th 341 seen  in  both  experiments  (though  to  a  lesser  extent  in _control_ ).  For  O  3  ,  both _control_ and _no_dirfdb_ struggle  to  capture 342 nighttime lows. 

343 

344 In  EPA  region  R9,  RAP-Chem  shows  relatively  good  agreement  overall  for  both  O  3 and  PM  2.5  ,  but  less  so  compared  to  R8. 345 As  in  R8,  RAP-Chem  struggles  to  capture  the  nighttime  O  3 low  during  both  months,  likely  resulting  from  too  little  titration 346 in  the  nocturnal  PBL.  The  nighttime  bias  also  likely  contributes  to  the  systematic  ~10  ppb  bias  in  the  day  during  the  end  of 347 August  and  middle  of  September.  Peak  O  3 is  generally  overestimated  in  RAP-Chem  in  EPA  R9.  Some  improvements  are 348 seen  in  the _control_ compared  to _no_dirfdb_ ,  though  the  impact  is  relatively  small.  For  PM  2.5  ,  RAP-Chem  mostly  captures  the 349 peak abundances in August in both experiments, but both simulations fail to capture the mid-month peak in September. 

350 

351 In  EPA  region  R10,  surface  O  3 is  mostly  simulated  extremely  well,  especially  by _control_ ,  which  accurately  captures  large 352 decreases  in  O  3 from  9-14  September  due  to  reductions  in  temperature  and  photolysis  rates  from  overhead  smoke. 353 RAP-Chem _no_dirfdb_ overestimates  O  3 by  almost  70  ppb  demonstrating  the  importance  of  capturing  aerosol  impacts  on 354 radiation  and  photolysis.  During  September,  RAP-Chem _control_ captures  the  PM  2.5  increases  through  around  12  September, 355 but  then  misses  the  buildup  that  continues  to  occur  through  15  September.  However,  RAP-Chem _control_ simulates  ~50  µg 356 m<sup>-3</sup> more than _no_dirfdb_ , dramatically improving predictions for several days. 

357 

358 Figure  S8  shows  the  correlation  between  the  bias  in  hourly  O  3 with  the  bias  in  hourly  PM  2.5  for  both _control_ and _no_dirfdb_ , 359 illustrating  the  complex  interplay  between  urban  chemistry,  wildfire  smoke  –  both  near  the  source  and  transported,  and  the 360 impact of the aerosol feedback on radiation. 

361 

362 In _no_dirfdb,_ strong  negative  correlations  are  seen  along  the  northern  half  of  the  west  coast,  and  positive  correlations  in 363 regions  directly  downwind  of  the  wildfire  locations  in  the  upper  Intermountain  West.  The  strong  negative  correlations  along 364 the  West  Coast  are  due  to  the  model  over  predicting  the  amount  of  surface  insolation  and  thus  the  photochemistry  of 365 combined  anthropogenic  and  wildfire  emissions.  This  is  despite  the  low  biases  in  PM  2.5  because  there  was  still  large  amounts 366 of  smoke  and  precursors  that  reached  these  areas.  In _control_ ,  this  correlation  is  significantly  reduced  because  the  model 367 simulated  much  less  ozone  with  roughly  the  same  amount  of  precursor.  Downwind  of  the  wildfires  (e.g.,  Montana),,  the 368 correlations  are  positive,  and  much  stronger  in _no_dirfdb._ When _no_dirfdb_ underpredicts  the  smoke  and  precursor  input  it 

13 

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





369 also  leads  to  an  underprediction  of  ozone.  Conversely,  because  the  models  generally  overpredict  the  amount  of  smoke 370 downwind  (e.g.,  Fig.  S4),,  the  correlations  in _no_dirfdb_ are  large  and  positive  because  there  is  no  reduction  in  solar 371 insolation.  In _control_ ,  these  correlations  are  much  smaller  due  to  the  aerosol  feedback  reducing  the  amount  of  active 372 photochemistry. 

# 373 **3.4 Improved chemistry-physics coupling in the PBL scheme** 

# 374 **3.4.1 Vertical mixing** 

375 Here  we  compare  the  * _mix_ simulations  to  quantify  the  improvements  of  the  chemistry  coupling  to  MYNN-EDMF.  Figure 376 2a-c  displays  domain-wide  average  surface  differences  ( _newmix_ minus _oldmix_ )  of  key  chemical  species  (O  3  ,  CO,  and  PM  2.5  ) 377 over  the  1-7  August  2020  test  period.  Overall,  all  four  * mix_ simulations  are  similar  to _control_ in  that  they  show  good  O  3 378 prediction  skill  and  in  general  are  biased  low  compared  to  observations  (Table  2),  though _control_ remains  the  best 379 simulation.  Small  but  systematic  differences  in  O  3  are  found  between _oldmix_ and _newmix_ (±2  ppb).  Much  larger  changes  are 380 seen  when  incorporating  the  enhanced  mixing  ( _enhmix_ minus _newmix_ ,  Fig  2d-f).  Enhanced  mixing  generally  has  the  effect  of 381 increasing  surface  O  3 at  night,  as  the  added  enhancement  reduces  NO  titration  and  can  bring  elevated  O  3 from  the  residual 382 layer  to  the  surface  (Hu  et  al.,  2012) .  Enhancement  also  increases  the  surface  O  3  daily  maximum,  likely  due  to  increased  O  3 383 and  precursor  availability  from  the  previous  night  since  the  enhancement  switch  is  only  very  rarely  activated  during  the 384 daytime  due  to  the  condition  for  low  PBL  heights.  For  PM  2.5  ,  differences  between _newmix_ and _oldmix_ are  very  minimal  when 385 averaged  over  the  EPA  regions,  though _enhmix_ consistently  predicts  lower  PM  2.5 concentrations  during  the  daily  peak, 386 improving  the  model  performance  in  7  of  10  EPA  Regions  (Table  3).  Over  urban  areas  and  directly  over  wildfires, _newmix_ 387 has  higher  PM  2.5 concentrations.  Downwind  of  the  large  fire  in  California,  however, _newmix_ shows  large  reductions 388 indicating  more  smoke  is  lofted  above  the  surface  compared  to _oldmix_ (recall  plume  rise  parameterizations  are  disabled  in  all 389 _*mix_ simulations).  Compared  to _newmix_ , _enhmix_ simulates  a  relatively  uniform  increase  of  PM  2.5 (~1-3  ug  m<sup>-3</sup> ),  of  which 390 most  of  the  difference  occurs  in  the  first  three  days  of  the  simulations.  Similar  to  PM  2.5  , _newmix_ CO  is  in  general  lower 391 compared  to _oldmix_ but  elevated  over  urban  locations  and  wildfires.  Additionally  like  PM  2.5  ,  lower  concentrations  are  also 392 observed  downwind  of  wildfires.  Compared  to _newmix_ , _enhmix_ simulates  lower  CO  concentrations  over  urban  areas, 393 however increases are seen over most of the domain. 

14 

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





394 395 **Figure 2** . Average surface differences for ( **a-c** ) _newmix_ minus _oldmix_ for surface ( **a** ) O  3  , ( **b** ) CO, and ( **c** ) PM  2.5 and ( **d-f)** _enhmix_ minus 396 _newmix_ for  surface ( **d** ) O  3  , ( **e** ) CO, and ( **f** ) PM  2.5 

397 

398 The  nonlocal  mixing  component  of  the  MYNN-EDMF  allows  mass  and  momentum  exchanges  between  non-adjacent  model 399 layers,  which  is  particularly  important  during  periods  with  deep  boundary  layers.  Figure  3  provides  an  example  of  the 400 changes  in  CO  abundances  as  a  result  of  the  MYNN-EDMF  changes  over  a  grid  cell  near  Phoenix,  AZ.  Compared  to  an  EPA 401 AirNOW  surface  measurement  (Fig.  3a),  each  of  the  simulations  reproduce  the  CO  time  series  modestly  well,  particularly 402 during  the  first  four  days.  During  the  final  three  days,  the  model  tends  to  overestimate  the  daily  midday  peaks,  potentially 403 related  to  overestimated  urban  emissions.  Only  very  small  differences  in  CO  are  seen  between  the  simulations,  with  the 404 largest  differences  seen  in  the  simulations  that  include  the  modified  enhancement  equation.  Fig  3b-d  shows  the  CO  time 405 series  over  the  same  grid  cell  as  a  function  of  height  for  the _oldmix_ , _newmix_ ,  and _enhmix_ simulations  overlain  by  CO 406 observations  from  AQUA  AIRS.  These  plots  reveal  enhanced  CO  throughout  the  PBL  for  all  three  simulations,  and  in 407 general  underestimate  compared  to  AQUA  AIRS.  Comparing  the  differences  (Fig.  3e  and  3f)  reveals  a  consistent  pattern  of 408 _newmix_ simulating  increased  CO  at  the  surface  (~5  ppb)  and  towards  the  top  of  the  PBL  (up  to  25  ppb)  and  reduced  CO  in 409 between  (around  -20  ppb).  Another  interesting  feature  is  elevated  CO  in _newmix_ throughout  the  column  as  the  PBL  grows, 410 particularly in the final days of the simulation period. 

15 

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





411 



412 **Figure 3.** ( **a** ) Time series of surface CO for each of the _*mix_ experiments and compared to observations from AirNOW monitoring site 413 South Phoenix. **(b-d)** Time series of the vertical profile of CO mixing ratio in ( **b)** _oldmix_ ( **c** ) _newmix_ and ( **d** ) _enhmix_ . Colored circles show 414 observations by the AIRS instrument aboard the AQUA satellite. Black lines denote the model-diagnosed PBL height ( **e)** Water vapor 415 mixing ratio in _newmix_ . ( **f)** Difference ( _newmix_ minus _oldmix_ )  in CO mixing ratios. ( **g)** Difference ( _enhmix_ minus _oldmix_ )  in CO mixing 416 ratios. EPA AirNow data courtesy of the U.S. Environmental Protection Agency. AIRS data courtesy of NASA. 417 

418 Figure  5  provides  a  similar  layout  as  Figure  4,  but  here  for  a  shallow  convection  case  near  northern  Georgia  (including  the 419 grid  cell  over  the  EPA  Monitor  South  Dekalb  located  at  33.69  N,  84.27  W).  Clouds  extend  from  ~1  km/900  mb  through  ~5 420 km/600  mb  throughout  the  region  and  below  the  clouds  (not  shown),  and _newmix_ CO  concentrations  are  lower  compared  to 421 _oldmix_ ,  while  they  are  higher  above  the  boundary  layer  clouds.  Compared  to  an  EPA  AirNOW  surface  measurement  at  South 422 DeKalb  (Fig.  4a),  each  of  the  simulations  reproduce  the  shape  of  the  CO  time  series  modestly  well,  though  tending  to 423 underestimate  observed  CO,  especially  at  night  when  the  observations  are  at  their  highest.  Only  very  small  differences  in  CO 424 are  seen  between  the  simulations  at  the  surface,  again  primarily  from  the  simulations  that  include  the  modified  enhancement 

16 

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





425 equation.  Larger  differences  are  seen  aloft.  For  example,  Fig  4b-d  shows  the  CO  time  series  over  the  same  grid  cell  as  a 426 function  of  height  for  the _oldmix_ , _newmix_ ,  and _enhmix_ simulations  overlain  by  PBL  height  and  observations  from  AQUA 427 AIRS.  The  difference  between _newmix_ and _oldmix_ reveals  a  consistent  pattern  of _newmix_ simulating  increased  CO  (~10  ppb) 428 above  the  PBL,  and  decreases  (10-20  ppb)  below  it,  similar  to  that  found  in  Phoenix.  The  decreased  CO  through  ~2km 429 improves  the  bias  since _oldmix_ tends  to  overestimate  CO  in  the  lower  layers  above  the  surface.  For  the  second  half  of  the 430 simulation,  we  can  see  significant  increases  aloft  in  the _enhmix_ case,  though  this  tends  to  disagree  with  the  observations. 431 Overall,  the  correlation  with  AIRS  CO  improves  in _newmix_ and _oldmix_ for  both  the  daytime  ascending  (Fig.  S9)  and 432 nighttime  descending  (Fig.  S10)  modes.  The  correlations  do  not  improve  as  substantially  in _enhmix_ compared  to _newmix_ , 433 though  the  largest  improvements  are  seen  over  urban  locations  for  the  nighttime  descending  mode  (i.e.,  where  and  when  the 434 enhancement would be active). 

435 



436 **Figure 4.** As Fig. 3, but for a location near Atlanta, GA (South Dekalb, 33.69 N, 84.27 W). EPA AirNow data courtesy of the U.S. 437 Environmental Protection Agency. AIRS data courtesy of NASA. 

17 

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





438 **3.4.2 Photolysis coupling to subgrid clouds in MYNN-EDMF** 

439 



440 **Figure 5** . ( **a** ) Average daytime (12-23Z) total cloud (water + ice) column from MYNN-EDMF in _newmix_ , ( **b** ) average daytime differences 441 ( _phtmix_ minus _enhmix_ ) in surface photolysis rates of NO  2  and ( **c** ) surface O  3 from 1-7 August. ( **d** ) Time series of _*_mix_ simulated and 442 observed surface O  3 at the EPA AirNOW site United Ave over the same period. The location of the United Ave AirNow site is shown in 443 (a). EPA AirNow data courtesy of the U.S. Environmental Protection Agency. 444 

445 In  the  WRF-Chem  TUV  scheme,  several  options  exist  to  include  the  impacts  of  clouds,  both  those  that  are  resolved  in  the 446 microphysics  scheme  and  those  parameterized  in  the  Grell-Freitas,  Grell-Devyani,  or  G3  cumulus  scheme.  The _phtmix_ 447 experiment  removes  this  impact  included  in _oldmix_ , _newmix_ ,  and _enhmix_ ,  allowing  a  quantification  of  the  impact  of  the 448 subgrid  boundary  layer  water  and  ice  clouds  simulated  by  the  MYNN-EDMF  scheme  on  photolysis  and  resulting 449 photochemistry.  Figure  5a  shows  the  total  column  boundary  layer  cloud  concentrations  averaged  over  daytime  hours  (12Z  – 450 23Z)  of  the  simulation  period  in _phtmix_ .  Boundary  layer  clouds  are  simulated  at  a  maximum  in  the  Southeast  and 

18 

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





451 Appalachia,  with  almost  no  BL  clouds  simulated  in  western  states.  Fig  5b  shows  the  average  difference  ( _phtmix_ minus 452 _enhmix_ )  in  surface  daytime  photolysis  rates  of  NO  2  (jNO  2  ),  which  closely  follows  the  pattern  of  BL  clouds.  Expectedly,  Fig. 453 5c  shows  daytime  O  3  reductions  throughout  most  of  the  eastern  US  ranging  from  ~1  to  8  ppb.  Small  increases  (~1  ppb)  are 454 found  throughout  the  Mojave  desert.  Here  the  increased  O  3 is  likely  related  to  the  Apple  wildfire  in  southern  California. 455 Finally,  Fig.  5d  shows  the  impact  at  a  single  site  (United  Ave,  33.72°N,  84.36°W).  During  most  of  the  period,  only  small 456 differences  can  be  seen  between  the  simulations.  On  August  3,  however,  the _phtmix_ simulation  overpredicts  daytime  ozone 457 to  a  similar  degree  as _oldmix_ .  On  August  5, _phtmix_ overpredicts  daytime  O  3 by  over  30  ppb,  but  the  other  simulations 458 ( _oldmix_ , _newmix_ , and _enhmix_ ) that include boundary layer cloud impacts on photolysis accurately capture observed O  3  . 

# 459 **3.5 Aerosol feedback: direct effect** 

460 The  RAP-Chem  includes  the  direct  aerosol  feedback  by  calculating  the  extinction  of  aerosols  using  Mie  theory  and  providing 461 that  extinction  to  the  model’s  radiation  and  photolysis  schemes.  The  direct  aerosol  effect  acts  to  reduce  available  radiation, 462 which  can  lead  to,  among  other  things,  stabilization  of  the  boundary  layer  and  reduction  in  photolysis  rates.  A  shallower 463 stable  boundary  layer  allows  pollutants  to  accumulate  near  the  surface,  however,  for  some  secondary  pollutants  like  O  3  ,  this 464 can  lead  to  decreases  in  their  abundance  due  to  nonlinear  chemistry.  Reductions  in  photolysis  rates  will  also  contribute  to 465 decreases  in  surface  O  3  .  Overall,  averaged  over  CONUS,  surface  O  3  is  ~1  ppb  higher  in _no_dirfdb_ compared  to _control,_ with 466 both  MB  and  RMSE  improvements  (2.4  to  1.4  and  13.2  to  12.2,  respectively).  The _control_ experiment  has  a  lower  RMSE 467 compared  to _no_dirfdb_ in  7  out  of  10  EPA  regions,  most  notably  in  the  wildfire  regions  (see  Sect.  3.3).  To  further 468 demonstrate  the  improvements  in  the  model  due  to  the  direct  aerosol  effect,  we  focus  on  Washington  state  in  EPA  Region  10 469 during  September  2020  when  aerosol  concentrations  were  extremely  high  and  thus  the  aerosol  feedback  is  also  strong. 470 Figure  6a  shows  the  time  series  of  observed  hourly  PM  2.5 compared  to  the _control_ and _no_dirfdb_ simulations  averaged  over 471 all  AirNow  sites  in  Washington.  Overall, _control_ accurately  predicts  the  surface  aerosol  enhancement  from  7-13  September 472 with _no_fdb_ simulating  PM  2.5 concentrations  that  are  ~50  ug  m-3  lower  than _control_ (and  more  biased  compared  to 473 observations).  This  forecast  deficiency  was  widely  noted  in  the  then-experimental  RAP/HRRR-Smoke  forecast  model  as 474 well  as  other  operational  models  (e.g.,  the  NAQFC)  and  is  still  an  area  of  active  investigation  (e.g.,  Conrick  et  al.,  2021) . 475 Figure  6b  shows  the  T  2m  time  series  over  the  same  period.  The _control_ simulation  demonstrates  excellent  skill  at  reproducing 476 the  observed  time  series,  accurately  capturing  the  decreases  in  temperature  due  to  high  aerosol  loadings  that _no_dirfdb_ 477 misses.  This  impact  is  also  seen  in  the  surface  O  3 time  series  (Fig  6c)  where  the  aerosol  direct  effect  in _control_ reduces 478 surface  O  3 over  EPA  Region  10  by  ~40  ppb  compared  to _no_dirfdb_ ,  allowing _control_ to  accurately  capture  the  reduced  O  3 479 production seen in the observations. 

19 

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





480 



481 **Figure 6.** Time series (1 Aug - 30 Sep, 2020) of hourly (a) surface PM  2.5  , (b) 2-m temperature, and (c) surface O  3 averaged over 482 Washington state for _control_ , _no_dirfdb_ , as compared to EPA AirNOW (a,c) and NOAA ISD (b) monitors. EPA AirNow data courtesy of 483 the U.S. Environmental Protection Agency. NOAA ISD data courtesy of the National Oceanic and Atmospheric Administration. 484 

20 

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





485 It  is  important  for  the  model  to  not  only  simulate  the  total  amount  of  radiation  reaching  a  model  layer,  but  also  the  type  of 486 that  radiation  (i.e.,  direct  vs.  diffuse).  Figure  7  shows  the  diurnal  cycle  of  total,  direct,  and  diffuse  radiation  averaged  over  all 487 the  SURFRAD  and  SOLRAD  sites  as  compared  to _control_ ,  and _no_dirfdb_ .  RAP-Chem _control_ matches  the  observations  of 488 total  irradiance  well  (MB=  6.0  W  m<sup>-2</sup> averaged  across  all  sites)  while _no_dirfdb_ is  expectedly  biased  high  (18.4  W  m<sup>-2</sup> )  .  For 489 direct  irradiance  only,  both  RAP-Chem  experiments  are  biased  high,  but  including  the  aerosol  effect  drastically  reduces  the 490 bias  (from  127.1  to  61.3  W  m<sup>-2</sup> ).  Conversely,  diffuse  radiation  is  increased  by  including  the  direct  effect,  and  as  such  the  bias 491 in  RAP-Chem _no_dirfdb_ for  diffuse  irradiance  is  drastically  reduced  in  RAP-Chem _control_ (-16.9  vs.  2.3  W  m<sup>-2</sup> ).  We  find  the 492 biases in irradiance increase as the overhead aerosol column amount increases (not shown). 

493 



494 

495 **Figure 7.** Diurnal cycle (UTC) of ( **a** ) total, ( **b** ) direct, and ( **c** ) diffuse radiation averaged over all available SURFRAD and SOLRAD sites 496 (black) as compared to the _control_ (blue) and _no_dirfdb_ (red) simulations. SOLRAD and SURFRAD data courtesy of the National Oceanic 497 and Atmospheric Administration. 

21 

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





# 498 **4 Conclusions** 

499 Here  we  present  retrospective  experiments  with  the  experimental  Rapid  Refresh  model  coupled  to  Chemistry  (RAP-Chem),  a 500 coupled  meteorology-chemistry  model  operating  in  real-time  at  NOAA  GSL  since  the  fall  of  2020.  Our  primary  simulation 501 includes  our  real-time  configuration  and  was  performed  during  a  period  of  intense  wildfire  activity  in  North  America  (1  Aug 502 – 30  Sep,  2020)  to  evaluate  the  fidelity  of  the  model  to  reproduce  observed  air  composition  and  accompanying  meteorology. 503 This primary experiment includes multiple existing and new developments in chemistry-physics coupling, including: 

504 

- 505 1. Coupling of updated aerosol scheme to the radiation (RRTMG) and photolysis (TUV) schemes 

- 506 2. Online, convective transport and wet scavenging within the Grell-Freitas cumulus scheme 

- 507 3. Online, non-local mixing of chemical scalars in the MYNN-EDMF PBL scheme 

- 508 4. Coupling of the MYNN-EDMF PBL clouds in the TUV photolysis scheme 

- 509 5. Coupling of prognostic aerosols to WFA and IFA in the Thompson-Eidhammer MP scheme. 

510 

511 Overall,  we  find  that  the  RAP-Chem,  despite  using  a  relatively  simple  gas-phase  mechanism,  is  able  to  simulate  the  salient 512 features  of  observed  surface  O  3 and  PM  2.5 as  well  as  demonstrate  skill  in  predicting  enhancements  (or  reductions)  of  O  3  and 513 PM  2.5 due  to  wildfires.  A  separate  experiment _no_dirfdb_ evaluates  the  impact  of  (1)  by  turning  off  the  aerosol  direct  effect.  In 514 most  cases,  including  the  direct  aerosol  effect  improves  model  predictions  for  surface  ozone,  particulate  matter,  and  the 515 accompanying  meteorology.  Surface  PM  2.5 is  generally  underestimated  in  wildfire  source  regions  as  well  as  the  extinction  of 516 those  aerosols  (e.g.,  underestimated  AOD  550  ).  However,  during  periods  of  peak  underestimation,  a  simpler  look-up-table 517 approach  captures  this  extinction,  providing  insight  into  potential  modifications  to  the  wildfire  emission  factors  and/or  the 518 aerosol refractive indices and hygroscopicity used in the Mie calculations. 

519 

520 Further,  we  have  performed  four  sensitivity  simulations  (i.e., _*mix_ )  to  evaluate  the  improvements  in  the  model  due  to  the  (3) 521 inclusion  of  online  (i.e.,  coupled,  within  the  physics),  non-local  mixing  inside  the  MYNN-EDMF  PBL  scheme,  artificially 522 enhancing  near-surface  exchange  coefficients  and  (4)  inclusion  of  parameterized  PBL  clouds  in  the  TUV  photolysis  scheme. 523 In  general,  the  impact  of  new  mixing  is  best  seen  in  the  distribution  of  CO  abundances,  where  the  updated  mixing  is  able  to 524 loft  and  thus  increase  primary  pollutant  abundances  higher  in  the  atmosphere,  thereby  reducing  abundances  closer  to  the 525 surface.  Average  ozone  at  the  surface,  however,  increases  due  to  more  efficient  photochemistry  paired  with  increased 526 nighttime  minima.  Large  differences  are  seen  when  including  the  modified  exchange  coefficients  ( _enhmix)_ ,  particularly  over 527 urban  areas  at  night  where  turbulent  mixing  from  anthropogenic  processes  (e.g.  traffic)  are  unaccounted  for.  Generally,  the 528 largest  impact  is  to  reduce  nighttime  ozone  titration  (i.e.,  increasing  abundances)  since  the  enhancement  is  only  activated 529 under  shallow  stable  boundary  layers  (<  100  m).  Measurements  of  vertical  profiles  of  various  tracer  gases  are  required  to 530 conduct  more  rigorous  verification  of  the  new  inline  PBL  mixing  in  the  future.  Future  work  will  also  investigate  adding  a 

22 

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





531 heat  flux  to  the  surface  layer  as  an  alternate  parameterization  for  both  wildfires  and  anthropogenic  activities.  Leveraging  the 532 urban  parametrizations  in  land  surface  schemes  will  also  be  investigated.  The  inclusion  of  the  PBL  simulated  clouds  in  the 533 TUV  scheme  reduces  photolysis  rates  leading  to  1-5  ppb  reductions  in  surface  O  3 across  the  eastern  US  (very  few  PBL 534 clouds  are  simulated  in  the  west).  This  coupling  is  crucial  to  reduce  high  ozone  bias  in  air  quality  models,  in  particular  the 535 regions  where  shallow  convection  is  prevalent.  Overall,  we  find  that  improving  the  coupling  between  chemistry  and  physics 536 processes in the experimental RAP-Chem improves its predictions of both weather and atmospheric chemistry. 

# 537 **Code and data availability** 

538 The  RAP-Chem  v1.0  model  code,  anthropogenic,  wildfire,  and  biogenic  emission  files,  as  well  as  the  namelist.wps  and 539 Vtable  used  to  generate  the  initial  and  lateral  boundary  conditions  are  available  at  10.5281/zenodo.21793915  (Schnell,  2026) 540 Example  namelist.input  files  for  each  experiment,  all  figure  plotting  scripts  or  YAML  files  for  MELODIES-MONET,  and  all 541 model  output  necessary  to  reproduce  the  figures  are  also  included  at  10.5281/zenodo.21793915  (Schnell,  2026) .  The  WRF 542 Preprocessing  System  (WPS)  code  to  generate  the  initial  and  lateral  boundary  conditions  is  available  at 543 <u>https://www2.mmm.ucar.edu/wrf/users/download/get_source.html .</u> The GFS data is available at 

544 <u>https://www.nco.ncep.noaa.gov/pmb/products/gfs</u> and  RAQMS  data  is  from <u>http://raqms-ops.ssec.wisc.edu/ .  The</u> 545 MELODIES-MONET  platform  can  be  installed  via  the  instructions  at <u>https://melodies-monet.readthedocs.io/en/stable/ ,</u> 546 which  also  enables  efficient  download  and  preprocessing  of  the  NOAA  ISD,  EPA  AirNow,  and  AERONET  observation  data 547 used  herein.  MODIS  AQUA  AIRS  data  can  be  retrieved  from  https://search.earthdata.nasa.gov/ .  NOAA  GML  SURFRAD 

547 used  herein.  MODIS  AQUA  AIRS  data  can  be  retrieved  from  https://search.earthdata.nasa.gov/ .  NOAA  GML  SURFRAD 548 and SOLRAD data can be retrieved from <u>https://gml.noaa.gov/aftp/data/radiation/ .</u> 

# 549 **Author contributions** 

550 JS  and  RA  designed  the  experiments.  JS  carried  out  the  experiments,  performed  the  data  analysis,  and  led  the  writing  of  the 551 paper.  JS,  RA,  GAG,  JBO,  EJ,  MH,  BB,  SF  contributed  to  the  model  code.  BM,  RHS,  JH,  CH,  RBP,  MC,  GP,,  and  MT 552 helped generate ancillary input data. All other authors contributed to the writing and review of the manuscript. 

# 553 **Competing interests** 

554 The authors declare that they have no conflict of interest. 

# 555 **Disclaimer** 

556 The  statements,  findings,  conclusions,  and  recommendations  are  those  of  the  author(s)  and  do  not  necessarily  reflect  the 557 views of NOAA or the U.S. Department of Commerce. 

23 

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





# 558 **Acknowledgments** 

559 The  authors  wish  to  thank  the  administrators  of  the  Jet  supercomputer  in  Boulder,  CO  for  their  tireless  efforts  maintaining 560 the  computing  environment  and  system.  We  also  acknowledge  the  usage  of  Google  Gemini  in  the  assistance  of  the  creation 561 of some of the plotting routines. 

# 562 **Financial Support** 

563 This  research  was  supported  in  part  by  the  NOAA  cooperative  agreement  NA22OAR4320151,  for  the  Cooperative  Institute 564 for Earth System Research and Data Science (CIESRDS), and the Earth Radiation Budget (ERB) initiative. 

# 565 **References** 

- 566 Ahmadov, R., Grell, G., James, E., Csiszar, I., Tsidulko, M., Pierce, B., McKeen, S., Benjamin, S., Alexander, C., Pereira, 567 G., Freitas, S., Goldberg, M., 2017. Using VIIRS fire radiative power data to simulate biomass burning emissions, 568 plume rise and smoke transport in a real-time air quality modeling system, in: 2017 IEEE International Geoscience 569 and Remote Sensing Symposium (IGARSS). Presented at the 2017 IEEE International Geoscience and Remote 570 Sensing Symposium (IGARSS), IEEE, Fort Worth, TX, pp. 2806–2808. 571 https://doi.org/10.1109/IGARSS.2017.8127581 

- 572 Ahmadov, R., McKeen, S.A., Robinson, A.L., Bahreini, R., Middlebrook, A.M., De Gouw, J.A., Meagher, J., Hsie, E. -Y., 573 Edgerton, E., Shaw, S., Trainer, M., 2012. A volatility basis set model for summertime secondary organic aerosols 574 over the eastern United States in 2006. J. Geophys. Res. Atmospheres 117, 2011JD016831. 

- 575 https://doi.org/10.1029/2011JD016831 

- 576 Andreae, M.O., 2019. Emission of trace gases and aerosols from biomass burning – an updated assessment. Atmospheric 577 Chem. Phys. 19, 8523–8546. https://doi.org/10.5194/acp-19-8523-2019 

- 578 Augustine, J.A., DeLuisi, J.J., Long, C.N., 2000. SURFRAD—A National Surface Radiation Budget Network for 579 Atmospheric Research. Bull. Am. Meteorol. Soc. 81, 2341–2357. 

- 580 https://doi.org/10.1175/1520-0477(2000)081%3C2341:SANSRB%3E2.3.CO;2 

- 581 Augustine, J.A., Hodges, G.B., Cornwall, C.R., Michalsky, J.J., Medina, C.I., 2005. An Update on SURFRAD—The GCOS 582 Surface Radiation Budget Network for the Continental United States. J. Atmospheric Ocean. Technol. 22, 583 1460–1472. https://doi.org/10.1175/JTECH1806.1 

- 584 Benjamin, S.G., Weygandt, S.S., Brown, J.M., Hu, M., Alexander, C.R., Smirnova, T.G., Olson, J.B., James, E.P., Dowell, 585 D.C., Grell, G.A., Lin, H., Peckham, S.E., Smith, T.L., Moninger, W.R., Kenyon, J.S., Manikin, G.S., 2016. A 586 North American Hourly Assimilation and Model Forecast Cycle: The Rapid Refresh. Mon. Weather Rev. 144, 587 1669–1694. https://doi.org/10.1175/MWR-D-15-0242.1 

- 588 Bruckner, M., Pierce, R.B., Lenzen, A., Diskin, G., DiGangi, J., De Maziere, M., Jones, N., Makarova, M., 2024. 589 UFS-RAQMS Global Atmospheric Composition Model: TROPOMI CO Column Assimilation. 590 https://doi.org/10.5194/egusphere-2024-2501 

- 591 Campbell, P.C., Tang, Y., Lee, P., Baker, B., Tong, D., Saylor, R., Stein, A., Huang, J., Huang, H.-C., Strobach, E., McQueen, 592 J., Pan, L., Stajner, I., Sims, J., Tirado-Delgado, J., Jung, Y., Yang, F., Spero, T.L., Gilliam, R.C., 2022. 

- 593 Development and evaluation of an advanced National Air Quality Forecasting Capability using the NOAA Global 594 Forecast System version 16. Geosci. Model Dev. 15, 3281–3313. https://doi.org/10.5194/gmd-15-3281-2022 

24 

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 595 Chow, F.K., Yu, K.A., Young, A., James, E., Grell, G.A., Csiszar, I., Tsidulko, M., Freitas, S., Pereira, G., Giglio, L., Friberg, 596 M.D., Ahmadov, R., 2022. High-Resolution Smoke Forecasting for the 2018 Camp Fire in California. Bull. Am. 597 Meteorol. Soc. 103, E1531–E1552. https://doi.org/10.1175/BAMS-D-20-0329.1 

- 598 Clough, S.A., Shephard, M.W., Mlawer, E.J., Delamere, J.S., Iacono, M.J., Cady-Pereira, K., Boukabara, S., Brown, P.D., 599 2005. Atmospheric radiative transfer modeling: a summary of the AER codes. J. Quant. Spectrosc. Radiat. Transf. 600 91, 233–244. https://doi.org/10.1016/j.jqsrt.2004.05.058 

- 601 Coggon, M.M., Gkatzelis, G.I., McDonald, B.C., Gilman, J.B., Schwantes, R.H., Abuhassan, N., Aikin, K.C., Arend, M.F., 602 Berkoff, T.A., Brown, S.S., Campos, T.L., Dickerson, R.R., Gronoff, G., Hurley, J.F., Isaacman-VanWertz, G., Koss, 603 A.R., Li, M., McKeen, S.A., Moshary, F., Peischl, J., Pospisilova, V., Ren, X., Wilson, A., Wu, Y., Trainer, M., 604 Warneke, C., 2021. Volatile chemical product emissions enhance ozone and modulate urban chemistry. Proc. Natl. 605 Acad. Sci. 118, e2026653118. https://doi.org/10.1073/pnas.2026653118 

- 606 Conrick, R., Mass, C.F., Boomgard-Zagrodnik, J.P., Ovens, D., 2021. The Influence of Wildfire Smoke on Cloud 607 Microphysics during the September 2020 Pacific Northwest Wildfires. Weather Forecast. 

- 608 https://doi.org/10.1175/WAF-D-21-0044.1 

- 609 Dowell, D.C., Alexander, C.R., James, E.P., Weygandt, S.S., Benjamin, S.G., Manikin, G.S., Blake, B.T., Brown, J.M., 610 Olson, J.B., Hu, M., Smirnova, T.G., Ladwig, T., Kenyon, J.S., Ahmadov, R., Turner, D.D., Duda, J.D., Alcott, T.I., 611 2022. The High-Resolution Rapid Refresh (HRRR): An Hourly Updating Convection-Allowing Forecast Model. 612 Part I: Motivation and System Description. Weather Forecast. 37, 1371–1395. 

- 613 https://doi.org/10.1175/WAF-D-21-0151.1 

- 614 Fast, J.D., Gustafson, W.I., Easter, R.C., Zaveri, R.A., Barnard, J.C., Chapman, E.G., Grell, G.A., Peckham, S.E., 2006. 615 Evolution of ozone, particulates, and aerosol direct radiative forcing in the vicinity of Houston using a fully coupled 616 meteorology-chemistry-aerosol model. J. Geophys. Res.-Atmospheres 111, 29. 617 https://doi.org/10.1029/2005jd006721 

- 618 Francoeur, C.B., McDonald, B.C., Gilman, J.B., Zarzana, K.J., Dix, B., Brown, S.S., De Gouw, J.A., Frost, G.J., Li, M., 619 McKeen, S.A., Peischl, J., Pollack, I.B., Ryerson, T.B., Thompson, C., Warneke, C., Trainer, M., 2021. Quantifying 620 Methane and Ozone Precursor Emissions from Oil and Gas Production Regions across the Contiguous US. Environ. 621 Sci. Technol. 55, 9129–9139. https://doi.org/10.1021/acs.est.0c07352 

- 622 Freitas, S.R., Grell, G.A., Li, H., 2021. The Grell–Freitas (GF) convection parameterization: recent developments, 623 extensions, and applications. Geosci. Model Dev. 14, 5393–5411. https://doi.org/10.5194/gmd-14-5393-2021 

- 624 Gery, M.W., Whitten, G.Z., Killus, J.P., Dodge, M.C., 1989. A photochemical kinetics mechanism for urban and regional 625 scale computer modeling. J. Geophys. Res. Atmospheres 94, 12925–12956. 

- 626 https://doi.org/10.1029/JD094iD10p12925 

- 627 Grell, G.A., Dévényi, D., 2002. A generalized approach to parameterizing convection combining ensemble and data 628 assimilation techniques. Geophys. Res. Lett. 29. https://doi.org/10.1029/2002GL015311 

- 629 Grell, G.A., Freitas, S.R., 2014. A scale and aerosol aware stochastic convective parameterization for weather and air quality 630 modeling. Atmospheric Chem. Phys. 14, 5233–5250. https://doi.org/10.5194/acp-14-5233-2014 631 Grell, G.A., Peckham, S.E., Schmitz, R., McKeen, S.A., Frost, G., Skamarock, W.C., Eder, B., 2005. Fully coupled “online” 632 chemistry within the WRF model. Atmos. Environ. 39, 6957–6975. https://doi.org/10.1016/j.atmosenv.2005.04.027 633 Guo, J.J., Fiore, A.M., Murray, L.T., Jaffe, D.A., Schnell, J.L., Moore, C.T., Milly, G.P., 2018. Average versus high surface 634 ozone levels over the continental USA: model bias, background influences, and interannual variability. Atmospheric 635 Chem. Phys. 18, 12123–12140. https://doi.org/10.5194/acp-18-12123-2018 

- 636 He, J., Harkins, C., O’Dell, K., Li, M., Francoeur, C., Aikin, K.C., Anenberg, S., Baker, B., Brown, S.S., Coggon, M.M., 637 Frost, G.J., Gilman, J.B., Kondragunta, S., Lamplugh, A., Lyu, C., Moon, Z., Pierce, B.R., Schwantes, R.H., 638 Stockwell, C.E., Warneke, C., Yang, K., Nowlan, C.R., González Abad, G., McDonald, B.C., 2023. COVID-19 639 perturbation on US air quality and human health impact assessment. PNAS Nexus 3, pgad483. 640 https://doi.org/10.1093/pnasnexus/pgad483 

- 641 Higuera, P.E., Abatzoglou, J.T., 2021. Record-setting climate enabled the extraordinary 2020 fire season in the western 642 United States. Glob. Change Biol. 27, 1–2. https://doi.org/10.1111/gcb.15388 

25 

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





643 Holben, B.N., Eck, T.F., Slutsker, I., Tanré, D., Buis, J.P., Setzer, A., Vermote, E., Reagan, J.A., Kaufman, Y.J., Nakajima, T., 644 Lavenu, F., Jankowiak, I., Smirnov, A., 1998. AERONET—A Federated Instrument Network and Data Archive for 645 Aerosol Characterization. Remote Sens. Environ. 66, 1–16. https://doi.org/10.1016/S0034-4257(98)00031-5 

- 646 Holben, B.N., Tanré, D., Smirnov, A., Eck, T.F., Slutsker, I., Abuhassan, N., Newcomb, W.W., Schafer, J.S., Chatenet, B., 647 Lavenu, F., Kaufman, Y.J., Castle, J.V., Setzer, A., Markham, B., Clark, D., Frouin, R., Halthore, R., Karneli, A., 648 O’Neill, N.T., Pietras, C., Pinker, R.T., Voss, K., Zibordi, G., 2001. An emerging ground-based aerosol climatology: 649 Aerosol optical depth from AERONET. J. Geophys. Res. Atmospheres 106, 12067–12097. 

- 650 https://doi.org/10.1029/2001JD900014 

- 651 Houweling, S., Dentener, F., Lelieveld, J., 1998. The impact of nonmethane hydrocarbon compounds on tropospheric 652 photochemistry. J. Geophys. Res. Atmospheres 103, 10673–10696. https://doi.org/10.1029/97JD03582 

- 653 Hu, X.-M., Doughty, D.C., Sanchez, K.J., Joseph, E., Fuentes, J.D., 2012. Ozone variability in the atmospheric boundary 654 layer in Maryland and its implications for vertical transport model. Atmos. Environ. 46, 354–364. 655 https://doi.org/10.1016/j.atmosenv.2011.09.054 

- 656 James, E.P., Alexander, C.R., Dowell, D.C., Weygandt, S.S., Benjamin, S.G., Manikin, G.S., Brown, J.M., Olson, J.B., Hu, 657 M., Smirnova, T.G., Ladwig, T., Kenyon, J.S., Turner, D.D., 2022. The High-Resolution Rapid Refresh (HRRR): 658 An Hourly Updating Convection-Allowing Forecast Model. Part II: Forecast Performance. Weather Forecast. 37, 659 1397–1417. https://doi.org/10.1175/WAF-D-21-0130.1 

- 660 Li, H., Grell, G.A., Ahmadov, R., Zhang, L., Sun, S., Schnell, J., Wang, N., 2024. A simple and realistic aerosol emission 661 approach for use in the Thompson–Eidhammer microphysics scheme in the NOAA UFS Weather Model (version 662 GSL global-24Feb2022). Geosci. Model Dev. 17, 607–619. https://doi.org/10.5194/gmd-17-607-2024 

- 663 Li, Y., Pickering, K.E., Barth, M.C., Bela, M.M., Cummings, K.A., Allen, D.J., 2019. Wet Scavenging in WRF-Chem 664 Simulations of Parameterized Convection for a Severe Storm During the DC3 Field Campaign. J. Geophys. Res. 665 Atmospheres 124, 7413–7428. https://doi.org/10.1029/2019JD030484 

- 666 Li, Y., Pickering, K.E., Barth, M.C., Bela, M.M., Cummings, K.A., Allen, D.J., 2018. Evaluation of Parameterized 667 Convective Transport of Trace Gases in Simulation of Storms Observed During the DC3 Field Campaign. J. 668 Geophys. Res. Atmospheres 123. https://doi.org/10.1029/2018JD028779 

- 669 Lin, Y.-L., Farley, R.D., Orville, H.D., 1983. Bulk Parameterization of the Snow Field in a Cloud Model. J. Clim. Appl. 670 Meteorol. 22, 1065–1092. https://doi.org/10.1175/1520-0450(1983)022%3C1065:BPOTSF%3E2.0.CO;2 

- 671 Madronich, S., Flocke, S., 1997. Theoretical Estimation of Biologically Effective UV Radiation at the Earth’s Surface, in: 672 Zerefos, C.S., Bais, A.F. (Eds.), Solar Ultraviolet Radiation. Springer Berlin Heidelberg, Berlin, Heidelberg, pp. 673 23–48. https://doi.org/10.1007/978-3-662-03375-3_3 

- 674 Malm, W.C., Sisler, J.F., Huffman, D., Eldred, R.A., Cahill, T.A., 1994. Spatial and seasonal trends in particle concentration 675 and optical extinction in the United States. J. Geophys. Res. Atmospheres 99, 1347–1370. 

- 676 

   - https://doi.org/10.1029/93JD02916 

- 677 McDonald, B.C., De Gouw, J.A., Gilman, J.B., Jathar, S.H., Akherati, A., Cappa, C.D., Jimenez, J.L., Lee-Taylor, J., Hayes, 678 P.L., McKeen, S.A., Cui, Y.Y., Kim, S.-W., Gentner, D.R., Isaacman-VanWertz, G., Goldstein, A.H., Harley, R.A., 679 Frost, G.J., Roberts, J.M., Ryerson, T.B., Trainer, M., 2018. Volatile chemical products emerging as largest 

- 680 

   - petrochemical source of urban organic emissions. Science 359, 760–764. https://doi.org/10.1126/science.aaq0524 

- 681 McDuffie, E.E., Smith, S.J., O’Rourke, P., Tibrewal, K., Venkataraman, C., Marais, E.A., Zheng, B., Crippa, M., Brauer, M., 682 Martin, R.V., 2020. A global anthropogenic emission inventory of atmospheric pollutants from sector- and 683 fuel-specific sources (1970–2017): an application of the Community Emissions Data System (CEDS). Earth Syst. 684 Sci. Data 12, 3413–3442. https://doi.org/10.5194/essd-12-3413-2020 

- 685 Morrison, H., Curry, J.A., Khvorostyanov, V.I., 2005. A New Double-Moment Microphysics Parameterization for 

- 686 Application in Cloud and Climate Models. Part I: Description. J. Atmospheric Sci. 62, 1665–1677. 

- 687 

   - https://doi.org/10.1175/JAS3446.1 

- 688 Nakanishi, M., Niino, H., 2009. Development of an Improved Turbulence Closure Model for the Atmospheric Boundary 689 Layer. J. Meteorol. Soc. Jpn. Ser II 87, 895–912. https://doi.org/10.2151/jmsj.87.895 

- 690 Nakanishi, M., Niino, H., 2004. An Improved Mellor–Yamada Level-3 Model with Condensation Physics: Its Design and 691 Verification. Bound.-Layer Meteorol. 112, 1–31. https://doi.org/10.1023/B:BOUN.0000020164.04146.98 

26 

https://doi.org/10.5194/egusphere-2026-4786 Preprint. Discussion started: 13 August 2026 _⃝_ c Author(s) 2026. CC BY 4.0 License. 





- 692 Olson, J., Angevine, W.M., Turner, D.D., Sun, X., Simonson, J.M., Evans, C., Kenyon, J.S., Li, H., Schnell, J., Puhales, F.S., 693 Cherubini, T., Li, W., Zhang, M., 2026. A Description of the MYNN-EDMF Turbulence Scheme. NOAA Tech. 694 Memo. OAR GSL 77. https://doi.org/10.25923/RAHR-SJ70 

- 695 Pleim, J.E., 2007. A Combined Local and Nonlocal Closure Model for the Atmospheric Boundary Layer. Part I: Model 696 Description and Testing. J. Appl. Meteorol. Climatol. 46, 1383–1395. https://doi.org/10.1175/JAM2539.1 

- 697 Powers, J.G., Klemp, J.B., Skamarock, W.C., Davis, C.A., Dudhia, J., Gill, D.O., Coen, J.L., Gochis, D.J., Ahmadov, R., 698 Peckham, S.E., Grell, G.A., Michalakes, J., Trahan, S., Benjamin, S.G., Alexander, C.R., Dimego, G.J., Wang, W., 699 Schwartz, C.S., Romine, G.S., Liu, Z.Q., Snyder, C., Chen, F., Barlage, M.J., Yu, W., Duda, M.G., 2017. THE 

- 700 WEATHER RESEARCH AND FORECASTING MODEL Overview, System Efforts, and Future Directions. Bull. 701 Am. Meteorol. Soc. 98, 1717–1737. https://doi.org/10.1175/bams-d-15-00308.1 

- 702 Schnell, J., 2026. Supporting data for Schnell et al., “Tight physics and chemistry coupling improves air quality forecasts: a 703 case study of the 2020 North American wildfires with the Rapid Refresh model coupled to Chemistry (RAP-Chem 704 v1.0).” https://doi.org/10.5281/ZENODO.20667784 

- 705 Schwantes, R.H., Emmons, L.K., Orlando, J.J., Barth, M.C., Tyndall, G.S., Hall, S.R., Ullmann, K., St. Clair, J.M., Blake, 706 D.R., Wisthaler, A., Bui, T.P.V., 2020. Comprehensive isoprene and terpene gas-phase chemistry improves 

- 707 simulated surface ozone in the southeastern US. Atmospheric Chem. Phys. 20, 3739–3776. 

- 708 https://doi.org/10.5194/acp-20-3739-2020 

- 709 Skamarock, W., Klemp, J., Dudhia, J., Gill, D., Barker, D., Wang, W., Huang, X.-Y., Duda, M., 2008. A Description of the 710 Advanced Research WRF Version 3. UCAR/NCAR. https://doi.org/10.5065/D68S4MVH 

- 711 Smirnova, T.G., Brown, J.M., Benjamin, S.G., Kenyon, J.S., 2016. Modifications to the Rapid Update Cycle Land Surface 712 Model (RUC LSM) Available in the Weather Research and Forecasting (WRF) Model. Mon. Weather Rev. 144, 713 1851–1865. https://doi.org/10.1175/MWR-D-15-0198.1 

- 714 Stockwell, C.E., Coggon, M.M., Gkatzelis, G.I., Ortega, J., McDonald, B.C., Peischl, J., Aikin, K., Gilman, J.B., Trainer, M., 715 Warneke, C., 2021. Volatile organic compound emissions from solvent- and water-borne coatings – compositional 716 differences and tracer compound identifications. Atmospheric Chem. Phys. 21, 6005–6022. 

- 717 

   - https://doi.org/10.5194/acp-21-6005-2021 

- 718 Tang, W., Emmons, L.K., Buchholz, R.R., Wiedinmyer, C., Schwantes, R.H., He, C., Kumar, R., Pfister, G.G., Worden, 719 H.M., Hornbrook, R.S., Apel, E.C., Tilmes, S., Gaubert, B., Martinez-Alonso, S., Lacey, F., Holmes, C.D., Diskin, 720 G.S., Bourgeois, I., Peischl, J., Ryerson, T.B., Hair, J.W., Weinheimer, A.J., Montzka, D.D., Tyndall, G.S., Campos, 721 T.L., 2022. Effects of Fire Diurnal Variation and Plume Rise on U.S. Air Quality During FIREX-AQ and WE-CAN 722 Based on the Multi-Scale Infrastructure for Chemistry and Aerosols (MUSICAv0). J. Geophys. Res. Atmospheres 723 127, e2022JD036650. https://doi.org/10.1029/2022JD036650 

- 724 Thompson, G., Eidhammer, T., 2014. A Study of Aerosol Impacts on Clouds and Precipitation Development in a Large 725 Winter Cyclone. J. Atmospheric Sci. 71, 3636–3658. https://doi.org/10.1175/jas-d-13-0305.1 

- 726 Wozniak, M.C., Steiner, A.L., 2017. A prognostic pollen emissions model for climate models (PECM1.0). Geosci. Model 727 Dev. 10, 4105–4127. https://doi.org/10.5194/gmd-10-4105-2017 

- 728 Zhou, X., Josey, K., Kamareddine, L., Caine, M.C., Liu, T., Mickley, L.J., Cooper, M., Dominici, F., 2021. Excess of 729 COVID-19 cases and deaths due to fine particulate matter exposure during the 2020 wildfires in the United States. 730 Sci. Adv. 7, eabi8789. https://doi.org/10.1126/sciadv.abi8789 

27 
