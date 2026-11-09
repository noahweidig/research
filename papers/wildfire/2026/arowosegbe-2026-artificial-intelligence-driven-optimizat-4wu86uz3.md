---
title: Artificial Intelligence-Driven Optimization of Food Transportation Systems for Enhancing Food Security, Supply Chain Resilience, and Operational Efficiency in the United States
authors:
- Arowosegbe, Oluwakemi
year: '2026'
journal: International Journal of Computer Applications Technology and Research
doi: 10.7753/ijcatr1412.1017
tags:
- decision support
- machine learning
- united states
- wildfire
zotero_key: 4WU86UZ3
item_type: journalArticle
url: https://openalex.org/W7171230907
source_url: 'unpaywall: https://doi.org/10.7753/ijcatr1412.1017'
fulltext_status: fulltext
synced: '2026-11-09'
---

# Artificial Intelligence-Driven Optimization of Food Transportation Systems for Enhancing Food Security, Supply Chain Resilience, and Operational Efficiency in the United States

## Abstract

Food transportation is a critical yet under-optimized component of United States food security, linking farms, processors, distribution centres, retailers, food banks, and consumers across geographically dispersed and disruption-prone networks.Existing systems are constrained by fragmented data, empty backhauls, cold-chain failures, port and highway congestion, driver shortages, severe weather, fuel-price volatility, and unequal access in rural, low-income, and disaster-affected communities.This study develops an artificial intelligence-driven optimization framework tailored to US food logistics.The framework integrates machine-learning demand forecasts, real-time traffic and weather data, vehicle-routing algorithms, predictive maintenance, dynamic fleet allocation, and IoT-based temperature monitoring to coordinate refrigerated and non-refrigerated food movements.It prioritizes perishability, nutritional importance, delivery urgency, infrastructure capacity, and regional vulnerability when generating transport decisions.The proposed system also models disruption scenarios, including hurricanes, wildfires, floods, cyber incidents, and distribution-centre outages, enabling rapid rerouting and inventory rebalancing across states.Expected outcomes include lower spoilage, fewer stockouts, reduced vehicle miles, improved cold-chain compliance, faster emergency food delivery, and more reliable service to underserved areas.By embedding resilience, equity, and sustainability into transport optimization, the framework provides a practical pathway for strengthening national food availability, reducing logistics costs, and improving the overall responsiveness of the US food supply chain.

## Full text

International Journal of Computer Applications Technology and Research Volume 14–Issue 12, 174 – 187, 2025, ISSN:-2319–8656 DOI:10.7753/IJCATR1412.1017 

# **Artificial Intelligence-Driven Optimization of Food Transportation Systems for Enhancing Food Security, Supply Chain Resilience, and Operational Efficiency in the United States** 

|Oluwakemi Betty Arowosegbe<br>Independent Researcher|Blessing Ameh<br>Independent Researcher|
|---|---|
|Supply Chain and Operations Management<br>Chicago, USA|Supply Chain Analytics and Digital Transformation<br>Atlanta, Georgia<br>USA|



**Abstract** : Food transportation is a critical yet under-optimized component of United States food security, linking farms, processors, distribution centres, retailers, food banks, and consumers across geographically dispersed and disruption-prone networks. Existing systems are constrained by fragmented data, empty backhauls, cold-chain failures, port and highway congestion, driver shortages, severe weather, fuel-price volatility, and unequal access in rural, low-income, and disaster-affected communities. This study develops an artificial intelligence-driven optimization framework tailored to US food logistics. The framework integrates machine-learning demand forecasts, real-time traffic and weather data, vehicle-routing algorithms, predictive maintenance, dynamic fleet allocation, and IoT-based temperature monitoring to coordinate refrigerated and non-refrigerated food movements. It prioritizes perishability, nutritional importance, delivery urgency, infrastructure capacity, and regional vulnerability when generating transport decisions. The proposed system also models disruption scenarios, including hurricanes, wildfires, floods, cyber incidents, and distribution-centre outages, enabling rapid rerouting and inventory rebalancing across states. Expected outcomes include lower spoilage, fewer stockouts, reduced vehicle miles, improved cold-chain compliance, faster emergency food delivery, and more reliable service to underserved areas. By embedding resilience, equity, and sustainability into transport optimization, the framework provides a practical pathway for strengthening national food availability, reducing logistics costs, and improving the overall responsiveness of the US food supply chain. **Keywords:** Artificial intelligence; food transportation optimization; food security; cold-chain logistics; supply chain resilience; United States. 

## **1. INTRODUCTION** 

### **1.1 Strategic Importance of Food Transportation to United States Food Security** 

Food transportation constitutes the operational backbone of the United States food supply system by connecting agricultural production with processing facilities, storage warehouses, distribution centres, wholesalers, retailers, restaurants, food banks, and final consumers through an extensive logistics network [1]. The continuous movement of agricultural commodities and processed food products ensures that food produced across diverse regions reaches consumers in sufficient quantities, with appropriate quality and within acceptable delivery timeframes [2]. Consequently, transportation is no longer viewed solely as a logistics activity but as a strategic determinant of national food security because it directly influences food availability, accessibility, affordability, utilisation, and long-term supply stability [3]. Efficient transportation networks also reduce distribution costs, minimise post-harvest losses, preserve product freshness, and improve the reliability of food delivery across urban, suburban, and rural communities [4]. 

The United States depends on a highly integrated multimodal transportation system comprising highways, railways, inland waterways, maritime shipping routes, and air freight services 

to sustain domestic and international food distribution [5]. Road transportation serves as the primary mode for moving fresh produce, dairy products, meat, poultry, and processed foods because of its flexibility, extensive road infrastructure, and ability to support last-mile delivery [6]. Rail transportation provides an economical means of transporting bulk agricultural commodities such as grains, oilseeds, animal feed, and fertilisers over long distances while supporting large-scale commercial agriculture [7]. Inland waterways and maritime transport facilitate high-volume domestic distribution and international agricultural trade, whereas air transportation supports the rapid movement of highly perishable and premium food products that require minimal transit times [8]. The coordinated interaction of these transportation modes strengthens supply continuity despite regional production disparities, seasonal harvesting cycles, fluctuating consumer demand, and unexpected market disruptions [9]. As population growth, urbanisation, digital commerce, and changing consumption patterns continue to increase freight demand, improving transportation performance has become indispensable for enhancing national food security and sustaining the competitiveness of the United States agri-food sector [2]. 

<u>www.ijcat.com</u> 

174 

International Journal of Computer Applications Technology and Research Volume 14–Issue 12, 174 – 187, 2025, ISSN:-2319–8656 DOI:10.7753/IJCATR1412.1017 

### **1.2 Structural and Operational Challenges in United States Food Transportation** 

Despite its strategic significance, the United States food transportation system continues to experience numerous structural and operational constraints that reduce efficiency and increase vulnerability to supply disruptions [5]. Fragmented logistics information systems frequently limit real-time communication among producers, warehouse operators, transport providers, retailers, and regulatory agencies, thereby reducing coordination and delaying operational decision-making [4]. Aging highways, bridges, rail infrastructure, ports, and intermodal terminals contribute to recurring congestion, longer travel times, increased vehicle operating costs, and declining transportation reliability [1]. Escalating fuel prices, persistent commercial driver shortages, and increasing freight demand have further intensified transportation costs throughout national food supply chains [8]. 

Maintaining uninterrupted cold-chain conditions remains particularly challenging for fresh fruits, vegetables, dairy products, seafood, pharmaceuticals, and other temperaturesensitive commodities that require strict environmental control during transportation [6]. Equipment failures, inadequate temperature monitoring, inefficient scheduling, and traffic delays frequently contribute to food spoilage, quality deterioration, and substantial economic losses before products reach consumers [3]. Climate-induced hazards, including hurricanes, floods, wildfires, winter storms, droughts, and extreme heat events, increasingly disrupt transportation infrastructure and delay food deliveries across multiple regions of the country [9]. The growing digitalisation of transportation management has simultaneously increased exposure to cybersecurity threats capable of compromising fleet management systems, routing algorithms, logistics databases, and communication networks [7]. Furthermore, transportation inequalities continue to restrict reliable food access within rural, remote, tribal, and economically disadvantaged communities where freight services and logistics infrastructure remain comparatively underdeveloped [2]. 

### **1.3 Research Aim, Objectives, Scope, and Contributions** 

This study aims to develop an artificial intelligence-driven optimization framework for food transportation systems that enhances food security, strengthens supply chain resilience, and improves operational efficiency throughout the United States. The proposed framework integrates machine learning, predictive analytics, intelligent routing algorithms, Internet of Things (IoT)-enabled sensing, real-time traffic intelligence, and adaptive decision-support mechanisms to optimise transportation planning, fleet allocation, cold-chain operations, inventory coordination, and disruption management. 

The objectives of this study are to examine the evolution of artificial intelligence applications in food transportation, develop  a  comprehensive  optimization  architecture  for 

intelligent logistics management, establish mathematical models for evaluating transportation efficiency, supply chain resilience, and AI-enabled transportation performance, and demonstrate how intelligent decision support can improve national food distribution under both normal and disruptive operating conditions [8]. The research adopts a United States perspective by considering multimodal transportation infrastructure, regional agricultural production systems, food distribution networks, and emerging logistics challenges affecting national food security [4]. Conceptually, the study integrates transportation optimization, resilience engineering, and food logistics intelligence into a unified analytical framework capable of supporting strategic transportation planning. Methodologically, the study introduces three original performance metrics the Food Transportation Efficiency Index (FTEI), Food Supply Chain Resilience Index (FSCRI), and Artificial Intelligence Transportation Performance Index (AITPI) for quantitatively evaluating intelligent food transportation systems. From a practical standpoint, the proposed framework provides policymakers, transportation agencies, logistics providers, food manufacturers, and emergency response organisations with a systematic decision-support tool for reducing food losses, improving delivery reliability, strengthening transportation resilience, and promoting sustainable food logistics across the United States. 

## **2. ARTIFICIAL INTELLIGENCE AND THE TRANSFORMATION OF FOOD TRANSPORTATION SYSTEMS** 

### **2.1 Evolution from Conventional Food Logistics to Intelligent Transportation Systems** 

Food transportation has undergone significant transformation over the past several decades as logistics operations have evolved from labour-intensive processes to digitally connected transportation systems [7]. Traditionally, food distribution relied heavily on manual scheduling, paper-based documentation, fixed delivery schedules, telephone communication, and dispatcher experience for route planning and fleet coordination [11]. Warehouse operations functioned largely as isolated facilities with limited information exchange among producers, transport operators, distributors, and retailers, resulting in delayed decision-making, poor shipment visibility, and inefficient resource utilisation [9]. These conventional practices were generally adequate for relatively stable markets but became increasingly ineffective as food supply chains expanded in scale, complexity, and geographical coverage [13]. 

The rapid development of digital technologies introduced substantial improvements in transportation management through Global Positioning System (GPS)-enabled fleet tracking, Geographic Information Systems (GIS), Radio Frequency Identification (RFID), barcode technologies, cloud-based logistics platforms, Electronic Data Interchange (EDI), Internet of Things (IoT) sensors, and integrated Transportation Management Systems (TMS) [8]. These 

175 

<u>www.ijcat.com</u> 

International Journal of Computer Applications Technology and Research Volume 14–Issue 12, 174 – 187, 2025, ISSN:-2319–8656 DOI:10.7753/IJCATR1412.1017 

technologies enabled continuous vehicle monitoring, automated shipment tracking, electronic documentation, enhanced inventory visibility, and improved communication among supply chain participants [10]. Cold-chain monitoring technologies further enhanced the transportation of temperature-sensitive food products by providing real-time information on storage conditions, product integrity, and environmental compliance during transit [14]. 

Despite these technological advances, conventional digital logistics systems remain predominantly data-reporting tools rather than intelligent decision-support systems [12]. Most existing platforms depend on predefined operational rules, historical schedules, and human intervention, making them less capable of responding to rapidly changing traffic conditions, weather events, demand fluctuations, infrastructure failures, and supply chain disruptions [7]. Consequently, the growing uncertainty surrounding modern food transportation has created the need for artificial intelligence-driven systems capable of continuously learning from operational data, predicting future events, and autonomously recommending optimal transportation decisions [11]. 

### **2.2 Artificial Intelligence Technologies for Food Transportation Optimization** 

Artificial intelligence has emerged as a transformative technology that extends beyond conventional logistics automation by enabling predictive, adaptive, and data-driven transportation management across complex food supply chains [10]. Unlike traditional optimization approaches that rely primarily on predefined rules and historical reports, artificial intelligence continuously analyses large volumes of structured and unstructured data to support dynamic operational decision-making under uncertain conditions [13]. 

Machine learning algorithms have become increasingly valuable for forecasting food demand by analysing historical sales, seasonal consumption patterns, demographic characteristics, promotional activities, weather conditions, and regional consumption behaviour [8]. More accurate demand forecasting enables transportation planners to allocate vehicles, personnel, and distribution capacity more efficiently while reducing inventory shortages, unnecessary transportation costs, and food waste throughout the supply chain [14]. 

Deep learning techniques further enhance transportation intelligence by processing large-scale traffic datasets, satellite imagery, weather information, road network conditions, and sensor data to predict traffic congestion, delivery times, travel delays, and infrastructure bottlenecks with greater accuracy than conventional forecasting models [9]. These predictive capabilities improve delivery scheduling, fleet deployment, and customer service while reducing transportation uncertainty [12]. 

Reinforcement learning provides an adaptive approach to vehicle  routing  by  enabling  transportation  systems  to 

continuously learn optimal routing strategies through interactions with changing operational environments [11]. Instead of relying on static route optimization, reinforcement learning dynamically adjusts transportation routes according to real-time traffic congestion, road closures, vehicle availability, customer priorities, weather conditions, and emergency disruptions, thereby improving delivery efficiency and transportation resilience [7]. 

Computer vision technologies contribute to transportation optimization through automated cargo inspection, pallet identification, package verification, vehicle loading assessment, and warehouse surveillance using cameras and image-recognition algorithms [13]. These technologies reduce manual inspection requirements while improving loading accuracy, food quality verification, and operational safety throughout transportation activities [10]. 

Natural language processing facilitates the intelligent management of logistics documentation by automatically extracting relevant information from delivery records, transportation contracts, customs documents, inspection reports, supplier communications, regulatory guidelines, and customer feedback [8]. Automated document interpretation reduces administrative workload, accelerates regulatory compliance, and improves information accessibility across transportation operations [14]. 

Predictive analytics strengthens fleet management by identifying early indicators of vehicle deterioration through the continuous analysis of engine performance, maintenance records, vibration patterns, fuel consumption, brake conditions, and sensor-generated operational data [9]. Maintenance activities can therefore be scheduled before equipment failures occur, thereby reducing transportation interruptions and improving fleet reliability [12]. Digital twin technology further extends artificial intelligence capabilities by constructing virtual representations of transportation networks, vehicles, warehouses, distribution centres, and cold-chain infrastructure [11]. These virtual environments enable planners to simulate disruption scenarios, evaluate alternative routing strategies, assess emergency response measures, and optimise transportation policies before implementation, thereby supporting proactive rather than reactive transportation management [13]. 

### **2.3 AI-Enabled Transportation Intelligence Across the Food Supply Chain** 

Artificial intelligence enables transportation intelligence by integrating operational information and decision-making across every stage of the United States food supply chain rather than optimising individual logistics activities in isolation [10]. Producers, food processors, transportation providers, warehouse operators, retailers, wholesalers, food banks, regulatory agencies, emergency management organisations, and consumers become connected through intelligent data-sharing platforms capable of continuously exchanging operational information [8]. This integration 

176 

<u>www.ijcat.com</u> 

International Journal of Computer Applications Technology and Research Volume 14–Issue 12, 174 – 187, 2025, ISSN:-2319–8656 DOI:10.7753/IJCATR1412.1017 

improves coordination by eliminating fragmented information flows and enabling transportation decisions to reflect conditions across the entire supply network rather than isolated organisational objectives [14]. 

Real-time visibility generated through IoT devices, GPS tracking systems, cloud platforms, and artificial intelligence analytics enables continuous monitoring of vehicle locations, shipment conditions, delivery progress, inventory status, coldchain performance, and infrastructure availability [9]. Demand-responsive distribution systems subsequently adjust transportation schedules, fleet allocation, warehouse replenishment, and delivery priorities according to changing consumption patterns, emergency requirements, and regional supply imbalances [12]. 

Artificial intelligence also strengthens cross-network coordination by identifying emerging transportation risks before they escalate into widespread supply disruptions [11]. Automated alert systems continuously detect abnormal traffic conditions, equipment failures, route interruptions, temperature deviations, cybersecurity incidents, and severe weather events, allowing logistics managers to implement corrective actions before food quality or delivery performance is compromised [7]. Continuous machine learning further improves transportation performance by incorporating operational feedback from previous deliveries, customer behaviour, environmental conditions, and infrastructure performance into future decision-making models [13]. Through continuous learning, predictive intelligence, and integrated coordination, artificial intelligence transforms food transportation from a reactive logistics function into an adaptive, resilient, and intelligent national decision-support system capable of strengthening food security and operational 

efficiency across the United States [10]. 

## **3. PROPOSED AI-DRIVEN FRAMEWORK FOR FOOD TRANSPORTATION OPTIMIZATION** 

**3.1 Architecture of the AI-Driven Food Transportation Optimization Framework** 

The proposed Artificial Intelligence (AI)-driven Food Transportation Optimization Framework is designed as an integrated decision intelligence architecture that continuously acquires, analyses, predicts, optimises, executes, and evaluates transportation activities across the United States food supply chain. Unlike conventional transportation management systems that primarily record operational data after transportation activities have occurred, the proposed framework transforms diverse real-time information into predictive and adaptive transportation decisions capable of improving food security, operational efficiency, and supply chain resilience. 

The first component of the framework comprises a multisource data acquisition layer, which continuously gathers information from heterogeneous internal and external sources to provide comprehensive situational awareness of transportation operations. Internal data include food demand forecasts, warehouse inventory levels, supplier production schedules, vehicle locations, fleet availability, driver schedules, delivery priorities, transportation costs, product perishability characteristics, refrigeration status, and historical logistics records [15]. External information is simultaneously collected from traffic management systems, weather forecasting services, fuel price databases, road condition 



<u>www.ijcat.com</u> 

177 

International Journal of Computer Applications Technology and Research Volume 14–Issue 12, 174 – 187, 2025, ISSN:-2319–8656 DOI:10.7753/IJCATR1412.1017 

monitoring platforms, infrastructure capacity reports, public safety agencies, regulatory information systems, satellite observations, and Internet of Things (IoT) sensors installed on vehicles and cold-chain equipment [21]. Integrating these diverse data sources enables the framework to maintain a continuously updated representation of transportation conditions across the national food distribution network. Following data acquisition, the framework performs data preprocessing and intelligent data integration to improve information quality before analytical processing begins. Data originating from multiple organisations frequently contain inconsistencies, duplicate records, missing values, incompatible formats, and communication delays that may reduce analytical accuracy [16]. Consequently, preprocessing procedures perform data validation, cleaning, normalisation, feature extraction, anomaly detection, temporal synchronisation, and database integration to produce reliable datasets suitable for artificial intelligence modelling [22]. This stage also transforms structured logistics records and unstructured information, including weather bulletins, traffic reports, inspection documents, and operational communications, into standardised analytical inputs [18]. 

The processed information is subsequently transferred to the predictive intelligence layer, where machine learning, deep learning, and predictive analytics models generate forecasts for food demand, transportation requirements, travel time, congestion, infrastructure availability, equipment failures, cold-chain risks, and disruption probabilities. Rather than reacting to operational problems after they occur, predictive 

models estimate future transportation conditions, allowing planners to prepare proactive response strategies before disruptions significantly affect food distribution [13]. 

Predictions generated by the predictive intelligence layer are subsequently supplied to the optimization engine, which applies artificial intelligence algorithms to determine optimal shipment consolidation, fleet allocation, warehouse coordination, vehicle routing, delivery scheduling, resource utilisation, and emergency response strategies. Multiple operational objectives including transportation cost, delivery time, fuel consumption, food freshness, carbon emissions, customer service, and infrastructure constraints are evaluated simultaneously to generate balanced transportation decisions that maximise overall system performance. 

The optimised decisions are communicated through an interactive decision-support interface that enables logistics managers, transportation agencies, warehouse operators, retailers, food manufacturers, emergency response organisations, and policymakers to monitor system performance and implement recommended operational actions. Transportation execution is continuously monitored through GPS tracking, IoT sensing, and cloud-based communication systems, while operational outcomes are returned to the framework through a continuous feedback mechanism that retrains prediction models, refines optimisation parameters, and continuously improves transportation intelligence over time. 



<u>www.ijcat.com</u> 

178 

International Journal of Computer Applications Technology and Research Volume 14–Issue 12, 174 – 187, 2025, ISSN:-2319–8656 DOI:10.7753/IJCATR1412.1017 

### **3.2 Intelligent Transportation Optimization and Decision Workflow** 

The effectiveness of the proposed framework depends on a structured workflow that transforms continuously generated operational data into adaptive transportation decisions capable of responding to changing supply chain conditions. Rather than treating transportation planning as a sequence of isolated activities, the proposed workflow establishes an integrated decision-making process in which every operational stage contributes information for subsequent optimization and continuous learning. 

The workflow begins with data acquisition, where operational information is continuously collected from producers, warehouses, transportation fleets, retailers, IoT sensors, traffic monitoring systems, weather forecasting agencies, infrastructure databases, fuel markets, regulatory authorities, and emergency management organisations. The availability of multiple information sources provides comprehensive situational awareness across the transportation network while reducing dependence on isolated organisational databases. 

The second stage performs data cleaning and preprocessing by correcting inconsistent records, eliminating duplicate observations, replacing missing values, synchronising temporal information, identifying abnormal measurements, and integrating heterogeneous datasets into standardised analytical formats. Data quality has a direct influence on the accuracy and reliability of artificial intelligence models, making preprocessing an essential prerequisite for intelligent transportation decision-making [21]. 

Following preprocessing, artificial intelligence models perform food demand prediction using historical consumption patterns, seasonal variations, population characteristics, market behaviour, promotional activities, weather conditions, and socioeconomic indicators [19]. Accurate demand estimation enables transportation planners to anticipate future distribution requirements while reducing stock shortages, excessive inventory accumulation, and unnecessary transportation activities [22]. 

Demand forecasts are subsequently combined with risk assessment models that evaluate congestion probability, adverse weather conditions, infrastructure limitations, vehicle reliability, cold-chain vulnerabilities, cybersecurity threats, labour availability, and emergency disruptions capable of affecting transportation performance [16]. Early identification of operational risks supports proactive mitigation strategies before disruptions significantly influence food distribution [14]. 

The optimization engine subsequently performs route and fleet optimization by selecting appropriate vehicles, consolidating shipments, assigning drivers, determining warehouse allocations, scheduling deliveries, and identifying optimal transportation routes based on multiple operational objectives. Reinforcement learning continuously adapts routing decisions according to real-time traffic conditions, 

road closures, weather events, delivery urgency, vehicle availability, and infrastructure constraints [20]. 

Optimised transportation plans are then implemented during the transportation execution stage, where fleets distribute food products according to dynamically generated schedules while maintaining compliance with cold-chain requirements and regulatory standards. Throughout transportation, GPS tracking systems, IoT sensors, vehicle diagnostics, and communication platforms provide continuous monitoring of vehicle location, cargo conditions, delivery progress, refrigeration performance, fuel consumption, and equipment health [15]. 

Whenever unexpected events occur, including traffic congestion, accidents, infrastructure failures, refrigeration malfunctions, severe weather, or emergency food requirements, the framework automatically recalculates transportation routes, reallocates vehicles, adjusts delivery priorities, coordinates warehouse operations, and initiates predictive maintenance interventions where necessary. Finally, performance evaluation compares planned and actual transportation outcomes using predefined efficiency, resilience, sustainability, and service-quality indicators. The resulting operational feedback continuously retrains artificial intelligence models, enabling transportation decisions to become increasingly accurate, adaptive, and resilient over time. 

### **3.3 Expected Effects on Food Security, Resilience, and Operational Performance** 

The proposed artificial intelligence-driven transportation optimization framework has the potential to substantially improve operational performance throughout the United States food distribution system by replacing reactive transportation management with predictive and adaptive decision-making. More accurate demand forecasting and intelligent shipment planning enable transportation providers to allocate fleet resources according to anticipated distribution requirements rather than historical assumptions, thereby reducing unnecessary vehicle movements, transportation delays, and resource underutilisation. 

Dynamic vehicle routing further minimises travel distance, congestion exposure, idle time, and empty mileage by continuously identifying the most efficient transportation paths according to prevailing operational conditions. Improved routing efficiency reduces fuel consumption, greenhouse gas emissions, transportation expenses, and delivery times while simultaneously increasing fleet productivity and service reliability. Predictive maintenance further decreases vehicle breakdowns by identifying mechanical deterioration before equipment failures occur, thereby reducing unexpected transportation interruptions and maintenance costs. 

The framework also strengthens food quality preservation through continuous cold-chain monitoring supported by IoT sensors and artificial intelligence analytics. Real-time detection  of  abnormal  temperature  conditions  enables 

<u>www.ijcat.com</u> 

179 

International Journal of Computer Applications Technology and Research Volume 14–Issue 12, 174 – 187, 2025, ISSN:-2319–8656 DOI:10.7753/IJCATR1412.1017 

immediate corrective action before product quality deteriorates, thereby reducing food spoilage, post-harvest losses, product recalls, and associated financial losses. Improved coordination among warehouses, transportation providers, retailers, and distribution centres further reduces inventory shortages, delivery uncertainty, and stockout occurrences that frequently affect highly perishable food products. 

Supply chain resilience is expected to improve considerably because artificial intelligence continuously evaluates disruption risks and generates alternative transportation strategies before operational failures propagate throughout the national distribution network. During hurricanes, floods, wildfires, winter storms, port closures, cybersecurity incidents, labour disputes, infrastructure failures, and distribution-centre disruptions, predictive intelligence enables the rapid rerouting of transportation assets, redistribution of inventory, and dynamic adjustment of delivery priorities to maintain food availability. These adaptive capabilities reduce recovery time, minimise disruption-related economic losses, and improve the continuity of essential food distribution services. 

The framework also provides important social benefits by strengthening emergency food delivery capabilities during natural disasters, public health emergencies, and humanitarian crises. Artificial intelligence can identify vulnerable populations, estimate emergency food demand, prioritise relief shipments, coordinate multiple transportation providers, and optimise resource allocation for food banks, emergency agencies, humanitarian organisations, and local governments. Underserved rural, remote, tribal, and economically disadvantaged communities may particularly benefit from demand-responsive transportation planning that allocates distribution resources according to actual community needs rather than fixed delivery schedules. Collectively, these improvements position the proposed framework as an intelligent transportation ecosystem capable of enhancing national food security, strengthening supply chain resilience, improving operational efficiency, reducing environmental impacts, and supporting equitable food accessibility throughout the United States. 

## **4. MATHEMATICAL MODELS AND PERFORMANCE EVALUATION METRICS** 

### **4.1 Food Transportation Efficiency Index** 

The successful implementation of artificial intelligence within food transportation requires objective performance measures capable of evaluating how effectively transportation resources are converted into reliable food delivery services [21]. Existing logistics performance indicators often assess isolated operational variables, such as transportation cost, delivery time, or vehicle utilisation, independently, making it difficult to obtain a comprehensive assessment of transportation efficiency across an integrated food supply chain [24]. Consequently, this study proposes the Food Transportation 

Efficiency Index (FTEI) as a composite performance measure that evaluates overall transportation efficiency by integrating multiple operational indicators into a single standardised metric. The index provides decision-makers with a quantitative basis for comparing transportation performance across different commodities, geographical regions, logistics providers, and distribution strategies. 

The proposed index is expressed as: 



Where: 

- FTEI = Food Transportation Efficiency Index 

- Ei = normalized score of transportation efficiency indicator _i_ 

- Wi = weight assigned to transportation efficiency indicator _i_ 

- n = total number of transportation efficiency indicators 

The index incorporates eight major efficiency dimensions: delivery-time performance, transportation cost per unit of food delivered, vehicle-capacity utilisation, fuel efficiency, empty-mile reduction, on-time delivery rate, food-loss reduction, and cold-chain compliance. Each indicator is first normalised onto a common numerical scale, such as 0–1 or 0– 100, to eliminate differences in measurement units before aggregation. Indicator weights may subsequently be determined using expert judgement, stakeholder consultation, entropy weighting, or multi-criteria decision-making techniques depending on operational priorities. 

Higher FTEI values indicate greater transportation efficiency because they reflect improved resource utilisation, lower logistics costs, reduced spoilage, higher delivery reliability, and more effective preservation of food quality during transportation. The index can be benchmarked across different transportation modes, food commodity categories, logistics providers, states, or regional distribution systems to identify operational strengths and areas requiring improvement. Transportation agencies and logistics managers may also employ the FTEI to evaluate investment outcomes, compare alternative routing strategies, monitor continuous operational improvement, and support evidence-based transportation planning for national food distribution systems. 

### **4.2 Food Supply Chain Resilience Index** 

Transportation efficiency alone does not guarantee uninterrupted food availability because transportation systems must also maintain operational continuity during unexpected disruptions [26]. Increasing climate uncertainty, infrastructure failures, labour shortages, cybersecurity incidents, and geopolitical disturbances have highlighted the importance of 

<u>www.ijcat.com</u> 

180 

International Journal of Computer Applications Technology and Research Volume 14–Issue 12, 174 – 187, 2025, ISSN:-2319–8656 DOI:10.7753/IJCATR1412.1017 

resilience as a fundamental characteristic of modern food transportation systems [23]. To evaluate this capability, this study proposes the Food Supply Chain Resilience Index (FSCRI) as a quantitative measure of a transportation network's ability to withstand, adapt to, and recover from operational disruptions while maintaining continuous food distribution. 

Recovery capability evaluates the speed with which transportation operations return to acceptable performance following disruptions. Adaptive routing capacity measures the ability of artificial intelligence to generate alternative transportation routes when existing routes become unavailable because of congestion, infrastructure damage, or adverse weather conditions. Distribution redundancy evaluates the availability of backup warehouses, alternative carriers, substitute transportation modes, and secondary distribution centres capable of sustaining logistics operations during emergencies. 

Continuity of food delivery measures the ability to maintain uninterrupted food movement despite operational disturbances, while transportation network visibility evaluates real-time information sharing among transportation operators, warehouses, producers, retailers, regulators, and emergency agencies. Together, these dimensions provide a comprehensive assessment of transportation resilience rather than simply measuring operational recovery following a disruption. 

The FSCRI is particularly valuable for evaluating transportation preparedness for hurricanes, floods, wildfires, port disruptions, cyberattacks, bridge failures, rail interruptions, severe winter storms, and distribution-centre closures. Decision-makers may also employ the index to compare resilience investments, prioritise infrastructure improvements, evaluate emergency response strategies, and identify vulnerabilities requiring additional contingency planning across regional and national food transportation networks. 

The proposed resilience index is expressed as: 



### **4.3 Artificial Intelligence Transportation Performance Index** 

Although transportation efficiency and resilience measure operational outcomes, they do not directly evaluate the effectiveness of artificial intelligence technologies responsible for supporting transportation decisions [26]. Consequently, this study proposes the Artificial Intelligence Transportation Performance Index (AITPI) as a complementary performance metric that measures the contribution of artificial intelligence to transportation planning, operational monitoring, predictive intelligence, and adaptive decision-making. The index enables an objective assessment of artificial intelligence capabilities while supporting comparisons among conventional logistics systems, digitally enabled transportation systems, and fully integrated AI-driven transportation networks. 

The proposed index is expressed as: 



Where: 

- AITPI = Artificial Intelligence Transportation Performance Index 

- P = prediction accuracy 

- O = route optimization performance 

- S = decision-response speed 

- M = monitoring effectiveness 

L = continuous-learning capability Prediction accuracy measures the reliability of artificial intelligence models in forecasting food demand, transportation requirements, delivery times, equipment failures, congestion, and disruption risks. Route optimization performance evaluates improvements in transportation efficiency generated through intelligent vehicle routing, shipment consolidation, fleet allocation, and warehouse coordination. Decision-response speed assesses the time required for artificial intelligence systems to analyse operational information and generate transportation recommendations following changing operating conditions. 

Where: 

- FSCRI = Food Supply Chain Resilience Index 

- R = recovery capability 

- A = adaptive routing capacity 

- D = distribution redundancy 

- C = continuity of food delivery 

- V = transportation network visibility 

Monitoring effectiveness evaluates anomaly detection, coldchain monitoring performance, fleet visibility, equipment diagnostics, and automated alert generation throughout transportation operations. Continuous-learning capability measures the ability of machine-learning algorithms to improve prediction accuracy and decision quality by incorporating operational feedback obtained from previous transportation activities. 

Higher AITPI values indicate increasingly intelligent transportation systems capable of generating more accurate forecasts, faster operational responses, improved anomaly 

<u>www.ijcat.com</u> 

181 

International Journal of Computer Applications Technology and Research Volume 14–Issue 12, 174 – 187, 2025, ISSN:-2319–8656 DOI:10.7753/IJCATR1412.1017 

detection, enhanced system reliability, and continuous adaptation to changing logistics environments. The index therefore provides transportation agencies, policymakers, logistics providers, and researchers with an objective framework for evaluating artificial intelligence maturity while supporting technology investment decisions and benchmarking transportation intelligence across conventional, digitally enabled, and fully autonomous food transportation systems. 

**Table 1. Variables, Indicators, Measurement Units, and Interpretation of the Proposed Food Transportation Performance Indices** 

|**Inde**<br>**x**|**Variable/Ind**<br>**icator**|**Primary**<br>**Data**<br>**Source**|<br>**Measurem**<br>**ent Scale**|**Expected**<br>**Perform**<br>**ance**<br>**Direction**|<br> <br>**Operati**<br>**onal**<br>**Relevan**<br>**ce**|
|---|---|---|---|---|---|
|**FTE**<br>**I**|<br>Delivery-time<br>performance|GPS,<br>TMS|%|Higher is<br>better|<br>Delivery<br>reliabilit<br>y|
||Transportatio<br>n cost per unit|<br>Financia<br>l records|<sup>£/$ per unit</sup>|<sup>Lower is</sup><br>better|<br>Cost<br>efficienc<br>y|
||Vehicle-<br>capacity<br>utilization|Fleet<br>manage<br>ment|%|Higher is<br>better|<br>Asset<br>utilizatio<br>n|
||Fuel<br>efficiency|Vehicle<br>telematic<br>s|<br>km/L<br>or<br>mpg|<br>Higher is<br>better|<br>Energy<br>efficienc<br>y|
||Empty-mile<br>reduction|GPS<br>records|<sup>%</sup>|Higher<br>reduction|Fleet<br>producti<br>vity|
||On-time<br>delivery rate|Delivery<br>systems|<sup>%</sup>|Higher is<br>better|<br>Service<br>quality|
||Food-loss<br>reduction|Cold-<br>chain<br>reports|%|Higher<br>reduction|Food<br>preservat<br>ion|
||Cold-chain<br>compliance|IoT<br>sensors|<sup>%</sup>|Higher is<br>better|<br>Product<br>safety|
|**FSC**<br>**RI**|Recovery<br>capability|Emergen<br>cy<br>response<br>data|<br>Index|Higher is<br>better|<br>Recover<br>y speed|
||Adaptive<br>routing<br>capacity|Routing<br>systems|<sup>Index</sup>|Higher is<br>better|<br>Operatio<br>nal<br>flexibilit<br>y|



|**Inde**<br>**x**|**Variable/Ind**<br>**icator**|**Primary**<br>**Data**<br>**Source**|**Measurem**<br>**ent Scale**|**Expected**<br>**Perform**<br>**ance**<br>**Direction**|<br> <br>**Operati**<br>**onal**<br>**Relevan**<br>**ce**|
|---|---|---|---|---|---|
||Distribution<br>redundancy|Logistics<br>network|<br><sup>Index</sup>|Higher is<br>better|<br>Supply<br>continuit<br>y|
||Continuity of<br>delivery|Delivery<br>records|<sup>%</sup>|Higher is<br>better|<br>Service<br>resilienc<br>e|
||Network<br>visibility|Integrate<br>d<br>platform<br>s|Index|Higher is<br>better|<br>Informat<br>ion<br>sharing|
|**AIT**<br>**PI**|Prediction<br>accuracy|AI<br>models|<sup>%</sup>|Higher is<br>better|<br>Forecast<br>quality|
||Route<br>optimization<br>performance|Routing<br>engine|%<br>improveme<br>nt|Higher is<br>better|<br>Operatio<br>nal<br>optimiza<br>tion|
||Decision-<br>response<br>speed|AI<br>platform|Seconds/mi<br>nutes|Lower is<br>better|<br>Rapid<br>decision-<br>making|
||Monitoring<br>effectiveness|IoT<br>platform|Detection<br>rate (%)|Higher is<br>better|<br>Operatio<br>nal<br>visibility|
||Continuous-<br>learning<br>capability|AI<br>system<br>logs|Improveme<br>nt rate|Higher is<br>better|<br>Model<br>adaptabil<br>ity|



## **5. APPLICATIONS, IMPLEMENTATION CHALLENGES, FUTURE DIRECTIONS, AND CONCLUSION 5.1 Applications Across United States Food Transportation Networks** 

Artificial intelligence offers significant opportunities to optimise transportation activities across the diverse logistics environments that constitute the United States food distribution system [29]. Because food commodities differ substantially in perishability, transportation distance, storage requirements, delivery urgency, and market characteristics, optimization strategies must be tailored to the operational requirements of individual supply chains rather than applying a uniform transportation model [33]. 

Within refrigerated transportation, artificial intelligence continuously  analyses  temperature  data,  refrigeration 

<u>www.ijcat.com</u> 

182 

International Journal of Computer Applications Technology and Research Volume 14–Issue 12, 174 – 187, 2025, ISSN:-2319–8656 DOI:10.7753/IJCATR1412.1017 

performance, traffic conditions, vehicle location, and estimated arrival times to preserve cold-chain integrity throughout distribution [31]. Predictive monitoring enables the early detection of refrigeration failures, allowing corrective actions before product quality deteriorates or regulatory compliance is compromised [35]. Fresh produce distribution particularly benefits from intelligent routing algorithms that minimise transit time, reduce post-harvest deterioration, and prioritise deliveries according to product shelf life and regional market demand [30]. 

The transportation of meat, poultry, seafood, and dairy products requires even stricter environmental control because small deviations in temperature may significantly reduce food safety and commercial value [34]. Artificial intelligence therefore combines real-time sensor information with predictive analytics to optimise refrigeration performance, delivery sequencing, and vehicle scheduling while ensuring compliance with food safety regulations [32]. Grain transportation presents different optimization priorities, emphasising large-scale shipment consolidation, rail scheduling, intermodal coordination, storage availability, and export logistics rather than rapid delivery [29]. 

Artificial intelligence also strengthens food bank operations 

needs, infrastructure availability, and emergency conditions [31]. 

Urban food transportation benefits from dynamic last-mile routing that considers traffic congestion, delivery density, customer availability, parking constraints, and time-sensitive deliveries [33]. Conversely, improving rural food access requires optimisation strategies that minimise transportation costs while maintaining reliable services across geographically dispersed communities where freight demand is comparatively low [30]. Artificial intelligence further improves port-to-inland transportation and interstate food distribution by integrating maritime schedules, rail services, highway networks, warehouse capacity, and regional demand forecasts into coordinated transportation decisions that enhance national food availability and logistics efficiency [34]. 

### **5.2 Technical, Institutional, Ethical, and Policy Challenges** 

Despite its considerable potential, implementing artificial intelligence across food transportation networks presents numerous technical, institutional, ethical, financial, and regulatory challenges that must be addressed before widespread adoption can be achieved [32]. One of the most 



and emergency food distribution by forecasting demand, identifying vulnerable populations, prioritising relief deliveries, and coordinating transportation resources among government agencies, humanitarian organisations, and private logistics providers [35]. During disaster response, intelligent transportation systems dynamically allocate vehicles and adjust delivery priorities according to changing community 

significant technical barriers concerns fragmented data ownership, whereby producers, transportation companies, warehouses, retailers, government agencies, and logistics service providers maintain separate information systems that frequently lack interoperability [30]. Limited integration among these independent databases reduces data availability, 

<u>www.ijcat.com</u> 

183 

International Journal of Computer Applications Technology and Research Volume 14–Issue 12, 174 – 187, 2025, ISSN:-2319–8656 DOI:10.7753/IJCATR1412.1017 

restricts real-time decision-making, and weakens the predictive capabilities of artificial intelligence models [35]. 

Digital infrastructure disparities also remain evident across transportation networks, particularly among small carriers, rural producers, and community-based food distributors that often lack advanced communication systems, cloud platforms, IoT infrastructure, or intelligent fleet management technologies [31]. These technological inequalities may widen operational disparities unless targeted investment programmes support inclusive digital transformation throughout the food transportation sector [34]. 

Ethical concerns also arise regarding algorithmic bias, where artificial intelligence models trained on incomplete or geographically unrepresentative datasets may unintentionally favour particular regions, transportation providers, or commercial interests while reducing service quality in underserved communities [33]. Cybersecurity threats present another major concern because increasingly connected transportation systems become more vulnerable to ransomware attacks, data manipulation, communication failures, and unauthorised access capable of disrupting national food distribution operations [29]. Privacy protection, particularly with respect to commercial transportation data and consumer information, requires robust governance mechanisms that balance operational intelligence with responsible data management [35]. 

Implementation costs associated with artificial intelligence infrastructure, advanced sensors, cloud computing, workforce training, and system integration may exceed the financial capacity of smaller transportation providers and agricultural producers [30]. Regulatory inconsistencies among federal agencies, state authorities, transportation regulators, food safety organisations, and emergency management institutions may also create uncertainty regarding liability, operational standards, and legal responsibility for autonomous transportation decisions [34]. Consequently, successful implementation requires coordinated governance frameworks that promote algorithmic transparency, stakeholder accountability, common interoperability standards, workforce reskilling, and collaborative decision-making among government institutions, food companies, transportation providers, technology developers, and emergency management agencies [32]. 

### **Table 2. Major Barriers to AI-Driven Food Transportation Optimization and Corresponding Mitigation Strategies** 

|**Challenge**<br>**Category**|**Major Barrier**|<sup>**Mitigation**</sup><br>**Strategy**|**Responsible**<br>**Stakeholders**|
|---|---|---|---|
|Technical|Fragmented<br>data systems|National<br>interoperability<br>standards<br>and<br>integrated data<br>platforms|<br>Federal<br>agencies,<br>technology<br>providers,<br>logistics|



|**Challenge**<br>**Category**|**Major Barrier**|<sup>**Mitigation**</sup><br>**Strategy**|**Responsible**<br>**Stakeholders**|
|---|---|---|---|
||||companies|
|Technical|Limited digital<br>infrastructure|<br>Investment<br>in<br>IoT,<br>cloud<br>platforms, and<br>communication<br>networks|<br> <br>Federal<br>and<br>state<br>governments,<br>private sector|
|Operational|Poor<br>system<br>integration|<br>Unified<br>transportation<br>management<br>architecture|Logistics<br>providers,<br>warehouse<br>operators|
|Financial|High<br>implementation<br>cost|Grants,<br>tax<br>incentives,<br>public-private<br>partnerships|<br>Government,<br>investors,<br>food<br>companies|
|Institutional|Weak<br>interagency<br>coordination|National<br>governance<br>framework and<br>shared<br>operational<br>protocols|<br>USDA, DOT,<br>FEMA, state<br>authorities|
|Ethical|AI model bias|Representative<br>datasets,<br>algorithm<br>auditing,<br>explainable AI|Researchers,<br>developers,<br>regulators|
|Cybersecurity|<br>Cyberattacks<br>and<br>ransomware|Zero-trust<br>architecture,<br>encryption,<br>continuous<br>monitoring|Cybersecurity<br>agencies,<br>transport<br>operators|
|Privacy|Commercial<br>and operational<br>data protection|<br>Data<br>governance<br>policies<br>and<br>controlled<br>information<br>sharing|<br>Regulators,<br>food<br>companies|
|Workforce|Skills shortages<br>and<br>displacement|<br>Workforce<br>reskilling<br>and<br>AI<br>training<br>programmes|<br> <br>Universities,<br>employers,<br>government|
|Regulatory|Inconsistent<br>standards<br>and<br>liability|<br>Harmonised AI<br>regulations and<br>accountability<br>frameworks|<br> <br>Federal<br>and<br>state<br>policymakers|



<u>www.ijcat.com</u> 

184 

International Journal of Computer Applications Technology and Research Volume 14–Issue 12, 174 – 187, 2025, ISSN:-2319–8656 DOI:10.7753/IJCATR1412.1017 

### **5.3 Future Research Directions and Conclusion** 

Future research should focus on advancing intelligent transportation technologies capable of supporting increasingly adaptive, sustainable, and resilient food distribution systems throughout the United States. One important research direction involves autonomous refrigerated freight vehicles that combine artificial intelligence, autonomous navigation, advanced refrigeration systems, and connected vehicle technologies to improve delivery reliability while reducing operational costs and human error. The development of connected vehicle infrastructure capable of exchanging realtime information among transportation assets, roadside systems, warehouses, and traffic management centres will further enhance collaborative transportation decision-making and network-wide operational visibility. 

Federated learning represents another promising research area because it enables artificial intelligence models to learn from distributed datasets without requiring organisations to exchange sensitive commercial information directly. This capability may significantly improve collaboration among producers, transportation providers, retailers, food manufacturers, and public agencies while preserving commercial confidentiality and data privacy. Digital twin technologies also require further investigation to improve simulation accuracy for transportation networks, enabling policymakers and logistics managers to evaluate disruption scenarios, infrastructure investments, emergency response strategies, and operational policies before implementation. 

Emerging technologies such as drone-assisted emergency food deliveries offer additional opportunities for improving food accessibility in remote communities and disaster-affected regions where conventional transportation infrastructure has been compromised. Blockchain-supported traceability systems may strengthen transparency by improving product authentication, shipment visibility, regulatory compliance, and food safety throughout transportation operations. Future transportation optimization should also integrate low-carbon routing strategies, electric freight vehicles, renewable energy infrastructure, and carbon-aware logistics planning to reduce greenhouse gas emissions while maintaining transportation efficiency. Furthermore, the development of national food logistics intelligence platforms capable of integrating transportation, agriculture, meteorology, infrastructure, emergency management, and public health information could substantially strengthen coordinated decision-making during both routine operations and national emergencies. 

Additional research is required to validate artificial intelligence models across different geographical regions, transportation modes, commodity categories, and seasonal operating conditions. Greater attention should also be directed towards improving real-time data sharing, ensuring equitable technology access for rural communities and smaller logistics providers, strengthening cyber resilience against evolving digital threats, and evaluating the environmental impacts 

associated with large-scale artificial intelligence infrastructure and computational resource consumption. 

Artificial intelligence has the potential to fundamentally transform food transportation from a reactive logistics function into an intelligent, predictive, and adaptive national decision-support system. The framework proposed in this study demonstrates how multi-source data integration, predictive analytics, optimization algorithms, intelligent routing, cold-chain monitoring, and continuous operational learning can be coordinated to improve transportation performance across the United States food supply chain. The proposed Food Transportation Efficiency Index, Food Supply Chain Resilience Index, and Artificial Intelligence Transportation Performance Index provide structured mechanisms for evaluating transportation effectiveness, resilience, and intelligent operational capability. The practical applications discussed illustrate how artificial intelligence can improve transportation planning across diverse food logistics environments while supporting emergency response and equitable food distribution. Successful implementation, however, depends upon secure digital infrastructure, interoperable information systems, transparent governance, collaborative institutional arrangements, inclusive technology adoption, and continuous operational improvement. Through these coordinated efforts, AI-driven food transportation optimization can strengthen food availability, reduce logistics losses, improve disruption response, increase resource utilisation, and expand reliable food access for underserved communities across the United States. 

## **6. REFERENCE** 

1. Luoga AW. The role of artificial intelligence in enhancing supply chain performance: Insights from Tanzania brewery companies. International Journal of Research in Business & Social Science. 2025 Dec 15;14(10). 

2. Singh D, Sharma A, Singh RK, Rana PS. Artificial intelligence enabled supply chain resilience: insights from FMCG industry. Journal of Global Operations and Strategic Sourcing. 2025 May 2;18(2):414-41. 

3. Sumi SS. Implementation of explainable AI-driven framework for supply chain optimization: A practical case study in industrial engineering. International Journal of Scientific Interdisciplinary Research. 2025 Dec 16;6(2):143-72. 

4. Moridiyat Kehinde Adebiyi. (2025). GOVERNANCE FRAGMENTATION AND ITS IMPACT ON CONSTRUCTION PRODUCTIVITY DECLINE ACROSS UNITED STATES INFRASTRUCTURE DEVELOPMENT PROJECTS SINCE 1968. International Journal Of Engineering Technology Research & Management (IJETRM), 09(12), 1080– 1095. <u>https://doi.org/10.5281/zenodo.21304920</u> 

5. Zhang L, Qin Z, Xu B, Li W, Wu Y, Li G. Machine learning-driven intelligent transformation of food safety: from multi-source risk identification to whole-chain preventive control. Critical Reviews in Food Science and Nutrition. 2025 Dec 15:1-8. 

185 

<u>www.ijcat.com</u> 

International Journal of Computer Applications Technology and Research Volume 14–Issue 12, 174 – 187, 2025, ISSN:-2319–8656 DOI:10.7753/IJCATR1412.1017 

6. Zhang L, Qin Z, Xu B, Li W, Wu Y, Li G. Machine learning-driven intelligent transformation of food safety: from multi-source risk identification to whole-chain preventive control. Critical Reviews in Food Science and Nutrition. 2025 Dec 15:1-8. 

7. Mahmud D. Building AI-Driven Economic Resilience Systems to Support Stability During Future Pandemic Lockdowns. Review of Applied Science and Technology. 2025 Jun 5;4(02):01-32. 

8. Mgbajiaka J. Co-designing resilient infrastructure: participatory approaches for sustainable implementation. Curr J Appl Sci Technol. 2025;44(8):11-17. 

9. Luoga AW. The role of artificial intelligence in enhancing supply chain performance: Insights from Tanzania brewery companies. International Journal of Research in Business & Social Science. 2025 Dec 15;14(10). 

10. Alwash R. Artificial Intelligence-Driven Precision Agriculture: A Multi-Scale Framework for ClimateResilient and Sustainable Food Production Systems. CBRTS Journal of Sustainable Development. 2025;1(1):28-40. 

11. Twum-Ampofoah, Juliana, Samuel Olawole Akande, Daniel Kofi Yeboah, and Attah Nnaemeka Melford. 2025. “Analytics of Third-Party Risk in U.S. Supply Chains: AI for Proactive Risk Scoring and Mitigation”. _Journal of Engineering Research and Reports_ 27 (11):178-93. https://doi.org/10.9734/jerr/2025/v27i111693. 

12. Peprah JA, Amoah J, Kwarteng K, Jibril AB, Sharif T. Artificial intelligence and additive manufacturing for resilient supply chain in Africa: A systematic literature review. Future Business Journal. 2025 Apr 1;11(1):54. 

13. Teixeira AR, Ferreira JV, Ramos AL. Intelligent supply chain management: A systematic literature review on artificial intelligence contributions. Information. 2025 May 13;16(5):399. 

14. Alegimenlen HO. A geospatial framework for transportation safety planning using multi-criteria spatial risk modeling. Int J Surv Struct Eng. 2024;5(2):56-72. doi:10.22271/2707840X.2024.v5.i2a.62. 

15. Moridiyat Kehinde Adebiyi. Construction Contract Review Automation Using Artificial Intelligence to Reduce Disputes and Improve Project Delivery Performance Nationwide. Int J Comput Artif Intell 2021;2(2):90-102. 

   - DOI: 10.33545/27076571.2021.v2.i2a.354 

16. Trollman H. Feature extraction for artificial intelligence enabled food supply chain failure mode prediction. Discover food. 2024 Apr 6;4(1):22. 

17. Uzozie OT, Onaghinor O, Esan OJ, Osho GO, Olatunde J. AI-driven supply chain resilience: A framework for predictive analytics and risk mitigation in emerging markets. International Journal of Multidisciplinary Research and Growth Evaluation. 2023 Jan;4(1):114150. 

18. Rane J, Amol Chaudhari R, Rane N. Artificial Intelligence and Machine Learning for Supply Chain Resilience: Risk Assessment and Decision Making in Manufacturing Industry 4.0 and 5.0. Artificial Intelligence and Machine Learning for Supply Chain Resilience: Risk Assessment and Decision Making in Manufacturing Industry. 2025 Jul 24;4. 

19. Effah D, Bai C, Asante WA, Quayson M. The role of artificial intelligence in coping with extreme weatherinduced cocoa supply chain risks. IEEE Transactions on Engineering Management. 2023 Jul 19;71:9854-75. 

20. Dora M, Kumar A, Mangla SK, Pant A, Kamal MM. Critical success factors influencing artificial intelligence adoption in food supply chains. International Journal of Production Research. 2022 Jul 18;60(14):4621-40. 

21. Arinze CA, Agho MO, Eyo-Udo NL, Abbey AB, Onukwulu EC. AI-Driven Transport and Distribution Optimization Model (TDOM) for the downstream petroleum sector: Enhancing sme supply chains and sustainability. Magna Sci. Adv. Res. Rev. 2025 Jan;13:137-53. 

22. Rane J, Chaudhari RA, Rane NL. Enhancing Sustainable Supply Chain Resilience Through Artificial Intelligence and Machine Learning: Industry 4.0 and Industry 5.0 in Manufacturing. Deep Science Publishing; 2025 Jul 26. 

23. Wu H, Liu J, Liang B. AI-driven supply chain transformation in Industry 5.0: Enhancing resilience and sustainability. Journal of the Knowledge Economy. 2025 Mar;16(1):3826-68. 

24. Sah BP, Shaikh S. AI-driven IoT and blockchain integration in Industry 5.0: A systematic review of supply chain transformation. Innovatech Engineering Journal. 2024 Dec 8;1(01):99-116. 

25. Ivanov MI, Ghercă AM, Gafencu LN. Artificial intelligence and sustainable development: Reducing food waste, building resilient organisations, and enhancing public financial administration. BRAIN. Broad Research in Artificial Intelligence and Neuroscience. 2025 Feb 4;16(1):243-60. 

26. Samuels A. Digital transformation in supply chains: improving resilience and sustainability through AI, Blockchain, and IoT. Frontiers in Sustainability. 2025 Dec 5;6:1584580. 

27. Ismaeil MK. The role and impact of artificial intelligence on supply chain management: Efficiency, challenges, and strategic implementation. Journal of Ecohumanism. 2024;3(4):89-106. 

28. Gorain S, Dutta S, Roy S. Supply Chain Optimization in Agribusiness with Artificial Intelligence. InSmart Farming, Smarter Solutions 2025 Oct 21 (pp. 197-221). CRC Press. 

29. Ikram A, Mehmood H, Arshad MT, Rasheed A, Noreen S, Gnedeka KT. Applications of artificial intelligence (AI) in managing food quality and ensuring global food security. CyTA-Journal of Food. 2024 Dec 31;22(1):2393287. 

30. Rahman ST. Strategic Application of Artificial Intelligence In Agribusiness Systems For Market 

186 

<u>www.ijcat.com</u> 

International Journal of Computer Applications Technology and Research Volume 14–Issue 12, 174 – 187, 2025, ISSN:-2319–8656 DOI:10.7753/IJCATR1412.1017 

Efficiency And Zoonotic Risk Mitigation. ASRC Procedia: Global Perspectives in Science and Scholarship. 2025 Apr 29;1(01):862-94. 

31. Chen W, Men Y, Fuster N, Osorio C, Juan AA. Artificial intelligence in logistics optimization with sustainable criteria: A review. Sustainability. 2024 Oct 22;16(21):9145. 

32. Eyo-Udo N. Leveraging artificial intelligence for enhanced supply chain optimization. Open Access Research Journal of Multidisciplinary Studies. 2024 Apr;7(2):001-15. 

   34. Olabiyi TE. Explainable large language model frameworks for healthcare risk prediction, clinical fraud detection, hospital enterprise analytics, and population health forecasting. _Int J Appl Res._ 2025;11(12):388-403. doi:10.22271/allresearch.2025.v11.i12e.13895. 

   35. Dhal SB, Kar D. Transforming agricultural productivity with AI-driven forecasting: Innovations in food security and supply chain optimization. Forecasting. 2024 Oct 19;6(4):92551. 

33. Ferreira AC, Francisco MB, De Pinho AF. The use of artificial intelligence in supply chain management: Systematic literature review and future research directions. IEEE Access. 2025 Aug 28. 

<u>www.ijcat.com</u> 

187 
