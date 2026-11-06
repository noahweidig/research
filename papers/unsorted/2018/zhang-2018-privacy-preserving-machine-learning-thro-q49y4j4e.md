---
title: Privacy-preserving Machine Learning through Data Obfuscation
authors:
- Zhang, Tianwei
- He, Zecheng
- Lee, Ruby B.
year: '2018'
journal: arXiv
doi: 10.48550/arXiv.1807.01860
tags:
- machine learning
zotero_key: Q49Y4J4E
item_type: preprint
url: http://arxiv.org/abs/1807.01860
source_url: 'arxiv: https://arxiv.org/pdf/1807.01860'
fulltext_status: fulltext
synced: '2026-11-06'
---

# Privacy-preserving Machine Learning through Data Obfuscation

## Abstract

As machine learning becomes a practice and commodity, numerous cloud-based services and frameworks are provided to help customers develop and deploy machine learning applications. While it is prevalent to outsource model training and serving tasks in the cloud, it is important to protect the privacy of sensitive samples in the training dataset and prevent information leakage to untrusted third parties. Past work have shown that a malicious machine learning service provider or end user can easily extract critical information about the training samples, from the model parameters or even just model outputs. In this paper, we propose a novel and generic methodology to preserve the privacy of training data in machine learning applications. Specifically we introduce an obfuscate function and apply it to the training data before feeding them to the model training task. This function adds random noise to existing samples, or augments the dataset with new samples. By doing so sensitive information about the properties of individual samples, or statistical properties of a group of samples, is hidden. Meanwhile the model trained from the obfuscated dataset can still achieve high accuracy. With this approach, the customers can safely disclose the data or models to third-party providers or end users without the need to worry about data privacy. Our experiments show that this approach can effective defeat four existing types of machine learning privacy attacks at negligible accuracy cost.

## Full text

# **Privacy-preserving Machine Learning through Data Obfuscation** 

Tianwei Zhang Princeton University tianweiz@alumni.princeton.edu 

Zecheng He Ruby B. Lee Princeton University Princeton University zechengh@princeton.edu rblee@princeton.edu 

## **ABSTRACT** 

As machine learning becomes a practice and commodity, numerous cloud-based services and frameworks are provided to help customers develop and deploy machine learning applications. While it is prevalent to outsource model training and serving tasks in the cloud, it is important to protect the privacy of sensitive samples in the training dataset and prevent information leakage to untrusted third parties. Past work have shown that a malicious machine learning service provider or end user can easily extract critical information about the training samples, from the model parameters or even just model outputs. 

In this paper, we propose a novel and generic methodology to preserve the privacy of training data in machine learning applications. Specifically we introduce a obfuscate function and apply it to the training data before feeding them to the model training task. This function adds random noise to existing samples, or augments the dataset with new samples. By doing so sensitive information about the properties of individual samples, or statistical properties of a group of samples, is hidden. Meanwhile the model trained from the obfuscated dataset can still achieve high accuracy. With this approach, the customers can safely disclose the data or models to third-party providers or end users without the need to worry about data privacy. Our experiments show that this approach can effective defeat four existing types of machine learning privacy attacks at negligible accuracy cost. 

## **1. INTRODUCTION** 

Nowadays machine learning has become a core component of many popular applications, such as image classification, speech recognition, natural language translation. To support the increased demand of machine learning-based development, many cloud providers push Machine Learning as a Service (MLaaS), providing computing platforms and learning frameworks for machine learning model training and serving. Typical MLaaS platforms include Amazon Sagemaker [1], Google Cloud ML Engine [2], Microsoft Azure ML Studio [3]. To use the MLaaS, customers provide training dataset and (or) machine learning algorithms to the cloud provider. The cloud provider sets up the machine learning environment, allocates certain amount of computation resources, and runs the model training task automatically. The cloud provider can also offer the model serving services, in which a model trained in the cloud side or the customer side is stored in the cloud platform. The cloud provider releases query APIs to end users, enabling them to use the model for prediction or classification. 

A training dataset is necessary to train and generate a machine learning model. A dataset can contain sensitive samples, _e.g._ , personal medical records, employee information, financial data, _etc._ How to protect the privacy of such samples has become a new security concern in machine learning. This privacy threat is especially serious in Machine Learning as a Service. First, in a model training service, customers need to upload the training data to the cloud provider, and the provider has full access to the data. Past work have shown that a malicious provider can easily steal the sensitive data, embed them into the model for leakage [34]. Second, in a model serving service, customers need to upload the pre-trained models to the cloud provider and set up end points for remote users to use the models. A successful machine learning model incorporates essential information about the training set. So even if the malicious provider does not have direct access to the dataset, he can extract sensitive information about the training data from the model parameters [5, 16, 24]. Third, even if the cloud provider is trusted, a malicious remote user who has only black-box access to the model output results is still able to retrieve information about the training data by querying the model with carefully-crafted inputs [9,10,14,21,22,30,33,38]. 

Protecting the privacy of training data in machine learning is challenging. First, when customers outsource machine learning tasks to the MLaaS provider, they have to grant the service provider full accesses to the data or models. This inevitably causes a big attack surface. Second, a correct machine learning model _must_ reveal information about the data on which it was trained. This creates opportunities for an adversary to learn information from the models. Third, given a fact that the adversary can steal different properties of the sensitive samples from different sources in different scenarios, it is very hard to have a generic method to eliminate all these information leakage. 

Some solutions were proposed to achieve privacy-preserving machine learning. These solutions can be classified into two categories. The first category is to design privacy-aware machine learning algorithms [4, 32] and platforms [17, 26] to prevent information leakage from models. However, this assumes that these security schemes can be correctly deployed in MLaaS. A malicious cloud provider with full control of machine learning tasks and platforms can easily subvert such privacy protection by disabling these solutions. Besides, in a model training service, customers are required to disclose the dataset to the cloud provider. These security-aware algorithms or platforms cannot prevent training data leakage in this scenario. The second category is to process the training 

data before releasing them to untrusted third parties. For instance, homomorphic encryption is introduced to process the training samples and then models are trained over the encrypted data [6] . While this can prevent data leakage, homomorphic encryption is not generic for arbitrary machine learning algorithms and the performance is not efficient. 

In this paper, we propose a novel and generic methodology to protect the privacy of training data in MLaaS. Our method follows the second defense category described above: training data processing. Specifically, we introduce a new function `Obfuscate` to help hide the sensitive information by adding random noise to the training dataset. We consider two cases: for the attacks that attempt to steal the properties of individual samples, we add random noise to these sensitive samples; for the attacks that attempt to learn the statistical properties of groups of samples, we augment the dataset with faked noisy samples. These noise are injected to obfuscate the adversary’s observations, while maintaining the prediction accuracy of trained models. Customers who are concerned with their sensitive data can apply this function to the training dataset and then disclose them to the MLaaS provider. So even the untrusted service provider or remote end users have access to the training data, model parameters or model outputs, they cannot discover the sensitive information hidden by the `Obfuscate` operation. Our evaluation indicates that this methodology can eliminate the leakage of four different types of privacy attacks [5,9,33,34]. This function introduces negligible performance overhead and accuracy reduction ( _<_ 5%). 

The key contributions of this paper are: 

- a comprehensive analysis of privacy attacks in machine learning services. 

- a generic method of obfuscating training dataset to eliminate data leakage. 

- evaluation of data obfuscation to defeat different types of machine learning privacy attacks. 

The rest of the paper is organized as follows: Sec. 2 gives the background of machine learning and model privacy attacks. Sec. 3 describes the methodology of obfuscating individual or group of samples to hide information. Sec. 4 shows the application of this methodology in different case studies. We discuss related work in Sec. 5 and conclude in Sec. 6. 

## **2. BACKGROUND** 

## **2.1 Machine Learning** 

A supervised machine learning model is a parameterized function _fθ_ : _X �→Y_ that maps input data _x ∈X_ (feature) to output data _y ∈Y_ (label). For a classification problem, _X_ is a _d_ -dimensional vector space and _Y_ is a discrete set of classes. This function is able to accurately predict the label of new data that have not seen before. 

**Model training.** The training process of a machine learning model is to find the optimal parameters _θ_ that can accurately reflect the relationship between _X_ and _Y_ . To achieve this, a training dataset _D_ = _{xi, yi}i_<sup>_N_</sup> =1<sup>with</sup><sup>_N_samplesis</sup> needed, where _xi ∈X_ is the feature data and _yi ∈Y_ is the corresponding ground-truth label. Then a loss function _L_ is adopted to measure the distance between the ground-truth output _yi_ and the predicted output _fθ_ ( _xi_ ). Ωis a regularization term that penalizes model complexity and help avoid 

overfitting. The goal of training a model is to minimize this loss function (Equation 1). 



<!-- Start of picture text -->
N<br>θ ∗ = arg min θ ( � L ( yi, fθ ( xi ) + Ω( θ )) (1)<br>i =1<br><!-- End of picture text -->

**Model inference.** After the model training is completed and the optimal parameters _θ_<sup>_∗_</sup> are obtained, given an input _x_ , the corresponding output can be calculated as _y_ = _fθ_<sup>_∗_</sup> ( _x_ ). This prediction process is called inference. We can also calculate the prediction accuracy of the model over a testing dataset _D_<sup>_t_</sup> = _{xi_<sup>_t, y_</sup> _i_<sup>_t}_</sup> _i_<sup>_M_</sup> =1<sup>tomeasurethemodel’sperfor-</sup> mance. For a classification problem where the output is a discrete number of values, the prediction accuracy is defined in Equation 2, where I is the indicator function. 



<!-- Start of picture text -->
M<br>acc ( D t , fθ ∗ ) = M 1 � I( fθ ∗ ( x t i ) =  y i t ) (2)<br>i =1<br><!-- End of picture text -->

**Deep learning.** The past few years have witnessed the fast development in deep learning, a new branch of machine learning. Algorithmic breakthroughs, the feasibility of data collection, and increasing computational power have contributed to the popularity of deep learning techniques. Deep learning have been widely adopted in many artificial intellectual applications, such as image recognition [15], natural language processing [23], speech recognition [13], _etc._ . A deep learning model is usually in the form of a neural network. Various neural network architectures have been proposed for different applications, _e.g._ multilayer perceptrons [28], convolutional neural networks [19] and recurrent neural networks [29]. A neural network consists of an input layer, an output layer and a sequence of hidden layers between the input and output. Each layer is a collection of units called _neurons_ , which are connected to other neurons in the previous layer and the following layer. Each connection between the neurons can transmit a signal to another neuron in the next layer by applying a linear function followed by an element-wise nonlinear activation function (e.g. sigmoid or ReLU). In this way, a neural network transforms the inputs through hidden layers and then the outputs. Backward propagation [11] and stochastic gradient descent [27] are commonly used methods to train a deep learning model and find the optimal parameters. 

## **2.2 Privacy Threats in MLaaS** 

Cloud-based machine learning services are released to provide automated solutions for machine learning data processing, model training, inference and further deployment. They attract machine learning practitioners to deploy applications in the cloud without having to set up their own large-scale infrastructure and computation resources. 

There are two main types of machine learning services in the cloud (Figure 1). The first one is model training: the cloud provider offers the computing resources and the customer selects a machine learning algorithm. Then the ML algorithm runs on the computing resources and generates the model for the customer. The second one is model serving: the customer uploads a model to the cloud platform. The cloud platform releases query APIs to end users. Then the end users can use the ML model for prediction or classification via these query APIs. A cloud platform can offer both 



<!-- Start of picture text -->
Service provider Service provider<br>Training data<br>Training code Model query data<br>query result<br>Customer Customer End user<br>(a) Model training (b) Model serving<br><!-- End of picture text -->

Figure 1: Data leakage in MLaaS. 

the model training and model serving services to customers to achieve end-to-end machine learning deployment. Recent work proposed privacy attacks in MLaaS: a malicious cloud provider or end user can extract sensitive information about the training dataset from machine learning tasks running in the cloud. We summarize these attacks based on the leaked information sources and types. 

### _2.2.1 Leaked information sources._ 

In different service modes, an adversary can steal sensitive information from different sources. **Training set.** Generating a model requires the training data and code. In the model training service (Figure 1a), customers do not necessarily need to upload the training code as they can select default ones from the cloud provider. However, training data is a necessity from customers to generate the models that are applicable to customers’ scenarios. So the cloud provider has full access to the training data _D_ . If the cloud provider is malicious, he can retrieve arbitrary information directly from the training set. Song et al. [34] designed a ML model memorization attack based on this threat model: the adversary can steal the critical training data and encode them into the trained model in different ways. So another adversary is able to retrieve the training data from the model parameters if he has white-box access to the model, or from the model outputs if he only has blackbox access to the model. 

**Model parameters.** In the model serving service (Figure 1b), the cloud provider may not have access to the training set if the model is not trained in the cloud. However he has access to the trained model _fθ_ and is able to identify the model algorithm, neural network topology, model parameters and hyper-parameters. Since the model _fθ_ is generated over the training _D_ (Equation 1), the model parameters _θ_ reveal some information about the training set. A malicious cloud provider is able to steal some information from the model parameters. For instance, Ateniese et al. [5] demonstrated a machine learning attack, that uses model parameters as features to classify and identify some sensitive properties about the training dataset. 

In the model training service, model parameters can also leak information. This case happens in distributed machine learning, where multiple nodes collaborate to train a machine learning model and each node uses its own training dataset. As every node needs to keep synchronizing the model parameters with other nodes. A malicious node can infer the training dataset of other nodes from the shared model parameters. Membership inference attack [24] and model inversion attack [16] have been demonstrated in this setting and threat model. 

**Model output.** In the model serving scenario (Figure 1b), in addition to the cloud provider who has white-box access to the model, an end user with black-box access to the model also has chances to retrieve training set properties only from the model outputs. Basically end users are allowed to use the model for prediction or classification. They send a sample to the cloud provider and receive the corresponding prediction result for this sample. The idea here is that the training data can affect the model parameters, which can then affect the prediction results of specific samples. Then an untrusted end user can send carefully-crafted input to the model and use the output to learn about the training data. For instance, in model inversion attacks [9, 10], the adversary attempts to reconstruct the training sample from the output confidence score. The attack strategy is to find the optimized sample whose confidence score is most close to 1 for one specific class. In membership inference attacks [33], the adversary uses the output confidence score of some samples as the training data to build a classify and predict if one target training sample is a member of the training set used for training this model. 

### _2.2.2 Leaked information types._ 

The adversary can extract different types of properties about the training set _D_ = _{xi, yi}i_<sup>_N_</sup> =1<sup>,asdescribedbelow.</sup> **Individual samples.** An adversary may be interested in some specific training samples ( _xi_<sup>_∗_</sup> _, yi_<sup>_∗_</sup> ) inside the training set, and want to obtain the properties of these samples, denoted as _P_ ( _xi_<sup>_∗_</sup> _, yi_<sup>_∗_</sup> ). 

For instance, the adversary wants to fully recover the sensitive training samples. In this case, the sensitive property is the sample values, _i.e._ , _P_ ( _xi_<sup>_∗_</sup> _, yi_<sup>_∗_</sup> ) = _xi_<sup>_∗_</sup> . Past work have shown that the adversary is able to steal the sensitive medical records in pharmacogenetic models via model inversion attacks [10] or images in image classification models [34]. 

Another example is membership inference attack, where the adversary wants to infer if one sample is used during the model training phase. Then the property is denoted as _P_ ( _xi_<sup>_∗_</sup> _, yi_<sup>_∗_</sup> ) = I( _xi_<sup>_∗_</sup> _, yi_<sup>_∗_</sup> _∈ D_ ). Shokri et al. [33] demonstrated the possibility of membership inference attacks in different machine learning models, _e.g._ , image classification, purchase recommendation, medical procedure prediction. **Groups of samples.** Instead of one individual sample, the adversary may be interested in a group of samples _g_<sup>_∗_</sup> . In this group, each sample ( _xi, yi_ ) _∈ g_<sup>_∗_</sup> has the same feature _F_ . The adversary wants to learn the statistical properties of these samples, denoted as _P_ ( _g_<sup>_∗_</sup> ). 

One typical example is model inversion attack [9]. In a face recognition system, the adversary wants to reconstruct the looking of one person ( _i.e._ , one class). In this case, the adversary considers a group of samples within the same class: _F_ : _yi_ = _y_<sup>_∗_</sup> . The property he wants to obtain is the average value of the samples in this group: _P_ ( _g_<sup>_∗_</sup> ) = _avg_ ( _xi_ ). This attack is effective at the datasets that samples within each class is very similar. 

A similar attack is demonstrated in [5], where the adversary can extract the nationalities of samples in the speech recognition system, and the traffic source website in the traffic analyzer. Here the adversary considers all the samples in the dataset: _F_ : _xi, yi ∈ D_ , _i.e._ , _g_<sup>_∗_</sup> = _D_ . The properties in consideration are some attributes of the samples, _P_ ( _g_<sup>_∗_</sup> ) = _attr_ ( _xi_ ). These properties can be recovered from model parameters. 

## **3. METHODOLOGY** 

**Threat model.** We consider three attack settings in two machine learning service modes, as shown in Figure 1. In the first case, the adversary is the cloud provider in the model training mode (Figure 1a). The customers upload the training data to the adversary. So the adversary has direct access to all the training data. In the second case, the adversary is also the cloud provider in the model serving mode (Figure 1b). The customers upload the model to the adversary. So he has _white-box_ access to the target model: _i.e._ , he is able to access the model parameters (e.g., network weights), hyper-parameters (e.g., regularization parameters, number of training epochs), model architecture. In the third case, the adversary is a remote end user in the model serving mode (Figure 1b). He only has _black-box_ access to the model: _i.e._ , he can only make queries to the target model and get the prediction results, _e.g._ , the confident score of each class for a given input in a classification model. 

**Challenges.** It is very challenging to design a method to protect the privacy of training data in MLaaS. First, the features of ML and MLaaS make it hard to eliminate information leakage to third parties. For model training, the customers _must_ disclose the data to the cloud provider to run the training task. For model serving, the customers _must_ allow the cloud provider to access the model parameters, and the end users to obtain the model outputs. The parameters and outputs of a correct ML model _inevitably_ reflect the training data. 

Second, the adversary in our threat model is very powerful and it is difficult to have a generic method to cover all attack settings. Past work proposed new algorithms or systems to preserve the training data privacy [4, 26, 32]. These work all assume that the desired algorithms and systems are correctly implemented and deployed in MLaaS. For the threat model in which the adversary has full control of the training dataset and model training process, enhancing the training algorithms or environment is not enough to guarantee the privacy of training data. 

Third, there are different types of properties about the training set (Sec. 2.2.2), and considering all theses properties is challenging. For instance, collaborative machine learning with differential privacy was proposed to protect the privacy of training data [32]. However, it has been proven that this method can only protect the properties of individual samples, but not the statistical properties of groups of samples [16,24]. Similarly, Triastcyn and Faltings [36] proposed to use GAN to generate artificial dataset to replace the original dataset for privacy-aware model training. However, the artificial dataset still keeps the statistical properties of original dataset, as the discriminator network in GAN cannot distinguish the artificial dataset from the original one. 

**Overview.** We aim to design a methodology to protect the privacy of training dataset in MLaaS. Our goal is to eliminate the leakage of properties of both individual samples as well as groups of samples, even the adversary (malicious cloud provider or end users) can access the training dataset, model parameters or model outputs. 

Instead of designing new algorithms or systems, we propose to process the training data _D_ and convert it to _D_<sup>_′_</sup> before outsourcing them into the machine learning services. This data processing needs to meet two goals: 

- **R1** : there are no confidential information about critical 



<!-- Start of picture text -->
Customer Service Provider End User<br>D OBFUSCATE D’ Model Model x<br>Apps<br>MODULE Training Serving<br>y<br><!-- End of picture text -->

Figure 2: Methodology Overview 

individual or groups of samples embedded in _D_<sup>_′_</sup> or the model trained from such data. So the adversary with access to _D_<sup>_′_</sup> , the model or the query outputs cannot get useful information. 

- **R2** : The model trained from the new dataset _D_<sup>_′_</sup> should have negligible prediction accuracy decrease compared to the one trained from the original dataset _D_ . 

Figure 2 shows the overview of our methodology. We add a new module, Obfuscate Module at the customer’s side to process the training data. This module obfuscates the training dataset, to hide critical information. With this design we do not need to make any assumptions or requirements for the untrusted third parties. We consider the privacy of individual properties as well as group statistical properties. To hide individual properties, we add random noise to sensitive samples. To hide group statistical properties, we augment the dataset with new faked samples. Below we describe the obfuscation mechanisms to achieve the two goals. 

## **3.1 Obfuscating Individual Samples** 

### _3.1.1 Mechanism_ 

We first consider the protection of individual samples. Given a dataset _D_ = _{xi, yi}i_<sup>_N_</sup> =1<sup>,therearesomesensitive</sup> samples that customers do not want to disclose to third parties. We denote the set of these samples as _d_<sup>_∗_</sup> _⊆ D_ . Note that the samples inside this set do not need to have common features. This is different from the groups of samples discussed in Sec. 3.2. For each sensitive sample ( _x_<sup>_∗_</sup> _, y_<sup>_∗_</sup> ) _∈ d_<sup>_∗_</sup> , the adversary is interested to learn the property _P_ ( _x_<sup>_∗_</sup> _, y_<sup>_∗_</sup> ). 

The Obfuscate Module takes these sensitive samples as input, and converts them to new samples. Algorithm 1 shows the pseudo code of this module. The `ObfuscateIndividualSample` function inside this module is applied to obfuscate each sensitive sample. The basic idea is to add noise to these samples, so the adversary will not learn the property from the converted new samples. Meanwhile, the added noise will not affect the model accuracy. 

There are different ways to add noise. Generically, for the input vector _xi_<sup>_∗_</sup> , we can randomly select part of the feature values (with the ratio of _r_ ) and add Gaussian noise _N_ (0 _, σ_ ) to these values. Requirements **R1** and **R2** can be achieved by adjusting the parameters _r_ and _σ_ . A more sophisticated way is to identify the sensitive features in each input and only add Gaussian noise _N_ (0 _, σ_ ) to these feature values. For instance, in a face recognition model, we can only obscure the faces of sensitive training images. For a medical machine learning model, we can add noise to the critical features, _e.g._ , age or occupation, of the sensitive patients. 

### _3.1.2 Analysis_ 

When adding noise to individual samples, there is a tradeoff between the privacy protection ( **R1** ) and model prediction accuracy ( **R2** ). 

For requirement **R1** , adding random noise to individual 



<!-- Start of picture text -->
Algorithm 1: Obfuscating individual samples<br>Input:<br>D : original dataset<br>d ∗ : the set of sensitive samples<br>Output:<br>D ′ : new artificial dataset<br>begin<br>D ′ = D<br>for each ( x ∗ , y ∗ ) ∈ d ∗ do<br>remove ( x ∗ , y ∗ ) from D ′<br>( x ∗′ , y ∗′ ) = ObfuscateIndividualSample ( x ∗ , y ∗ )<br>add ( x ∗′ , y ∗′ ) to D ′<br>end<br>return D ′<br>end<br>function ObfuscateIndividualSample( x ∗ , y ∗ )<br>x ∗′ = x ∗ + Noise ( x ∗ )<br>y ∗′ = y ∗<br>return ( x ∗′ , y ∗′ )<br>end<br><!-- End of picture text -->

samples can reduce the information leakage about these samples. Consider the case in which the adversary has the maximum capability, _e.g._ , direct access to the training dataset [34]. The adversary can retrieve the maximum and most accurate information about the training data, _i.e._ , the exact values. After obfuscating the sensitive samples, the adversary can at most obtain the samples with random noise. If the strength of added noise ( _σ_ ) is large enough and the ratio of feature values involved ( _r_ ) is large enough to cover sensitive information, the adversary fail to get useful information from his observation. For the threat model where the adversary does not have direct access to the dataset, he has to infer the property of the individual samples indirectly from the model parameters or query outputs [33]. The models trained over the converted samples can only reflect the characteristics of noisy ones, and it is difficult for the adversary to recover the correct information. 

For requirement **R2** , machine learning models are robust against appropriate random noise in the training set [40]. If the added noise is not biased, it can help prevent model overfitting. However, adding too much noise to the training dataset can reduce the accuracy of the target model. There are two factors that affect the model accuracy when obfuscating the samples: the number of samples that need to be obfuscated, and the amount of noise added to each sensitive sample. If only a small number of samples inside the training set need to be protected and obfuscated, then the obfuscating operation does not affect the accuracy, as the other samples can still contribute to generating a correct model. When the number of sensitive samples is large, then the amount of the noise becomes important in maintaining the model accuracy. We need to select the appropriate noise strength ( _σ_ in Gaussian noise), and the portion of involved feature values ( _r_ ) to hide sensitive information with negligible accuracy degradation. Experiments in Sec. 4 demonstrate that appropriate noise addition parameters can help achieve both requirements **R1** and **R2** . 

## **3.2 Obfuscating Groups of Samples** 

### _3.2.1 Mechanism_ 

Next we consider the protection of statistical properties of training samples. The adversary is interested in a group 

of samples _g_<sup>_∗_</sup> that have common feature _F_<sup>_∗_</sup> . He expects to retrieve the statistical information about the samples in this group, _P_ ( _g_<sup>_∗_</sup> ). The adversary may be interested in multiple groups. We denote the group of these groups as _G_<sup>_∗_</sup> . 

Similarly, the Obfuscate Module uses the `ObfuscateGroupSample` function to add random noise to each sensitive group, as shown in Algorithm 2. Different from obfuscating individual samples which directly adds noise to every sensitive sample, we can add some carefully-crafted training samples into each group instead of modifying the original samples. This operation can hide the statistical properties of sensitive groups. 

We introduce a new parameter _r_ , denoting the ratio of new samples added to a group in consideration. Then we calculate the number of new samples required for this group. To generate a new sample, we randomly pick an original one from this group, convert the feature value into its negative, and add small amount of noise. We assign this new feature value with a label so that this new sample satisfies the group’s common feature _F_<sup>_∗_</sup> . For instance, for a face recognition task, the negative of a pixel value _x_ of an image sample is calculated as 255 _− x_ . If the adversary attempts to reconstruct the looking of one person, then the common feature of the target group is that all samples have the same label. So we should assign the new samples with the same label. Then we add this new sample into the group. Since the new samples are the negative of original ones, the statistical values of the new group the adversary can infer will not reveal the properties of original samples. 

**Algorithm 2:** Obfuscating group samples 

|**Input:**<br>_D_: original dataset<br>|
|---|
|_G_<sup>_∗_</sup>: A set of sensitive groups<br>_r_: ratio of added samples compared to original ones<br>**Output:**<br>i|
|_D_<sup>_′_</sup>: new artificial dataset|
|**begin**<br>|
|_D_<sup>_′_ </sup>= _D_<br>**for** each _g_<sup>_∗_</sup>_∈G_<sup>_∗_</sup>**do**<br>remove _g_<sup>_∗_</sup>from _D_<sup>_′_</sup><br>_g_<sup>_∗′_ </sup>= `ObfuscateGroupSample`(_g_<sup>_∗_</sup>_, r_)<br>add _g_<sup>_∗′_ </sup>to _D_<sup>_′_</sup><br>**end**<br>**return** _D_<sup>_′_</sup><br>**end**|
|**function** `ObfuscateGroupSample(`_g_<sup>_∗_</sup>_, r_`)`<br>N = `GetNumberSample`(_g_<sup>_∗_</sup>) _·_ r<br>_g_<sup>_∗′_ </sup>= _g_<sup>_∗_</sup><br>**for** _i = 1 ..._ N **do**<br>get a random sample (_x_<sup>_∗_</sup>_, y_<sup>_∗_</sup>) from _g_<sup>_∗_</sup><br>_x_<sup>_∗′_ </sup>= `Negative`(_x_<sup>_∗_</sup>) + `Noise`(_x_<sup>_∗_</sup>)<br>select _y_<sup>_∗′_</sup>, s.t. (_x_<sup>_∗′_</sup>_, y_<sup>_∗′_</sup>) satisfies _F_<sup>_∗_</sup><br>add (_x_<sup>_∗′_</sup>_, y_<sup>_∗′_</sup>) to _g_<sup>_∗′_</sup><br>**end**<br>**return** _g_<sup>_∗′_</sup><br>**end**|



### _3.2.2 Analysis_ 

Since the adversary does not focus on individual samples, obfuscating individual samples (Sec. 3.1) cannot achieve requirement **R1** : if each sample is injected with random noise, the adversary can still obtain the statistical properties of the samples, as the noise will be filtered when the adversary calculates the statistical characteristics of the samples. Instead, we add new samples whose properties are the op- 

posite of the original ones. Then when the adversary tries to infer the properties from the models, he will get the statistical results combining both the original samples and the new samples. The injection of the new samples will hide the properties of original samples. 

For requirement **R2** , adding noisy synthetic data into the training set does not affect model accuracy. It has been shown that machine learning models, especially deep learning models, have a vast capacity and they can essentially express any function to fit the given data [39]. When adding new synthetic samples, the trained model from augmented dataset is fitted to both the original samples and the new ones [34]. So the model still has high quality on the original data samples. Experiments in Sec. 4 confirm this argument. 

## **4. CASE STUDIES** 

In this section, we evaluate the effects of the data obfuscation in achieving privacy-preserving machine learning. We consider four existing types of model privacy attacks: model memorization attack [34] and membership inference attack [33] target on the properties of individual samples; model inversion attack [9] and model classification attack [5] target on the statistical properties of groups of samples. For each attack, we demonstrate the security evaluation as well as the performance impact of obfuscating individual samples or groups of samples. 

## **4.1 Model Memorization Attack** 

### _4.1.1 Attack_ 

Model memorization attack targets on individual samples: the adversary is interested in some sensitive samples ( _x_<sup>_∗_</sup> _, y_<sup>_∗_</sup> ), and wants to recover the exact feature values of these samples, _i.e._ , _P_ ( _x_<sup>_∗_</sup> _, y_<sup>_∗_</sup> ) = _x_<sup>_∗_</sup> . The adversary can be a malicious cloud provider in a model training service, with full access to the training set and models. He can steal the sensitive samples, and encode the values into the model parameters or outputs. Another malicious party can retrieve these sensitive information from the model during model serving. 

Song et al. [34] proposed several techniques for the adversary to encode sensitive data into the models. (1) LSB encoding: the adversary can encode the training dataset in the least significant (lower) bits of the model parameters. (2) Correlated value encoding: the adversary can gradually encode information while training model parameters. For instance, the adversary can add a malicious term to the loss function which maximizes the correlation between the parameters and the data he wants to encode. (3) Sign encoding: similar to correlated value encoding, the adversary can use the sign of model parameters to interpret as bit strings, _e.g._ , positive parameters represent 1 and negative parameters represent 0. (4) Abusing model capacity: different from the above attacks, the adversary is assumed to have no access to the model parameters. Then he can augment the training dataset with synthetic inputs whose labels encode the critical information. Then information is leaked via the outputs of these added inputs. 

**Implementation** . We use the same code and configuration from [34] to reproduce the sign encoding attack, as it has a relatively good performance in data encoding. The target machine learning model is a 34-layer residual network over CIFAR10 dataset [18]. CIFAR10 dataset contains 50,000 training images from 10 classes, _e.g._ , airplane, automobile, 

bird, etc. We pick one image for each class as the target sample, as shown in Figure 3a. Note that the images in the original CIFAR10 database are colored. Here we show them as gray-scaled as the deep learning application first converts these images to gray-scaled during input pre-proposing. 

The adversary is able to encode around 400 images into one model due to the limited number of model parameters. Figure 3b shows the images recovered from the compromised models. We can see that the adversary can accurately recover most pixels of the images. He can easily identify the objects and details from the recovered images. 

### _4.1.2 Defense_ 

Since the adversary attempts to recover the values of individual images, we obfuscate each sensitive sample by adding random noise to that sample. For each image, we randomly select 1/3 of pixels and add Gaussian noise _N_ (0 _,_ 75) to the selected pixels. 

**Privacy.** We first consider the defense effects in privacypreserving. Figure 3c shows the images the adversary recovers via model memorization technique. Since we add random noise to the images, the adversary only gets the noisy images. From these images, we observe that it is very difficult for the adversary to identify the objects and their labels. It is even harder to recognize the image details. So with data obfuscation, even the adversary has control of the training set, he cannot recover the clean and accurate data. 

**Accuracy.** Next we consider the impact of adding noise to the model prediction accuracy. Figure 4 shows the training and validation accuracy versus training epochs. We consider different ratios of sensitive samples that are obfuscated ( _r_ in Algorithm 1). We can see that the training time is not affected by the noise addition: each case reaches the maximum accuracy at almost the same time. However, there is a tradeoff between validation accuracy and noise ratio. When we add noise to 1/2 of the samples, the validation accuracy decreases 2%. If we add noise to all of the samples, then the validation accuracy drops by 5%, which is still acceptable. Noise addition is more effective when there are not so many sensitive samples to be protected. 

## **4.2 Membership Inference Attack** 

### _4.2.1 Attack_ 

Next we consider membership inference attack [33], which also targets on the property of individual samples. For one specific sample ( _x_<sup>_∗_</sup> _, y_<sup>_∗_</sup> ), the adversary wants to learn the membership property: _P_ ( _x_<sup>_∗_</sup> _, y_<sup>_∗_</sup> ) = I( _x_<sup>_∗_</sup> _, y_<sup>_∗_</sup> _∈ D_ ), _i.e._ , if the sample is used in the model training. The adversary does not have direct access to the training dataset or trained model. But he is able to use the trained model for prediction: he can send any feature data to the model and obtain the confidence score/probability that the input data belong to each class. 

To infer the membership property, the adversary trains a lot of shadow models using the same algorithm of the target model. For each shadow model, the adversary randomly chooses some data samples to form a training set and a validation set. The shadow model is trained over the training set. Then he feeds both the training feature data and validation feature data into the shadow model and obtains the corresponding results, _i.e._ , probabilities of each class. If the model is overfitted (this is an assumption in [33]), the prediction results of training data and validation data are 





<!-- Start of picture text -->
(a) Target images<br><!-- End of picture text -->





<!-- Start of picture text -->
(b) Recovered images<br><!-- End of picture text -->





<!-- Start of picture text -->
(c) Recovered images with data obfuscation<br><!-- End of picture text -->

Figure 3: Model memorization attack and the defense 



<!-- Start of picture text -->
100% 100%<br>80% 80%<br>60% 60%<br>40% 40%<br>r=0 r=0<br>20% r=0.25 20% r=0.25<br>r=0.5 r=0.5<br>r=1 r=1<br>0% 0%<br>0 20 40 60 80 100 0 20 40 60 80 100<br>epochs epochs<br>(a) Training accuracy (b) Validation accuracy<br>y y<br>c c<br>a a<br>r r<br>u u<br>c c<br>c c<br>a a<br><!-- End of picture text -->

Figure 4: Prediction accuracy of machine learning models in model memorization attack. 

different. So the adversary can build a classifier, with the prediction results of feature data as input, and whether the data is from the training set (denoted as 1) or the validation set (denoted as 0) as the label. With this classifier, the adversary sends the feature value of sensitive sample in consideration to the target model and retrieves the prediction result. Then he sends the prediction result to the classifier and gets the conclusion whether the sensitive sample is a member of the target model’s training set. 

**Implementation.** We reproduce one membership inference attack from [33] with the same configuration and parameters: the target model is a convolutional neural network over the CIFAR10 dataset. We select two sizes of the training set for the target and shadow models: 2,500 and 10,000. The validation set has the same size as the training set. The adversary runs 100 shadow models with different subsets of training and validation samples. He uses logistic regression to classify whether the sample is included in the training set based on its prediction result. 

The black lines ( _r_ = 0) in Figure 5 show the adversary’s membership inference accuracy of samples in each class ( _x_ - axis), with 10,000 and 2,500 training samples respectively. We observe that the adversary can achieve high prediction accuracies for different classes (80% _∼_ 90%). Our repro- 

duced results match the ones from [33]. To better illustrate the membership inference attack effects, we show the confusion matrices in Tables 1a (10,000 training samples) and 2a (2,500 training samples). We can see that the adversary has high confidence of identifying the samples that are included in the training set. He has relatively high errors when the samples are not in the training set. In general the _F_ 1 scores are very high (0.86 and 0.89). 

### _4.2.2 Defense_ 

We use the same defense strategy of model memorization attack to prevent the adversary from inferring the membership of specific samples. We obfuscate each sensitive samples by injecting Gaussian noise. Then the target model is trained over noisy samples. When the adversary conducts the membership inference attack, his shadow models and the classifier are generated over the clean samples. If a sensitive sample is included in the target model’s training set, the output of this sample from the target model will indicate that this sample is not in the training set, as the target model is trained with the noisy samples, not the clean ones. **Privacy.** The red lines ( _r_ = 1) in Figure 5 show the adversary’s inference accuracy after the training samples are obfuscated. The base line is 50% (blue dash line), which is the adversary’s random guessing accuracy. With data obfuscation, the adversary’s inference accuracy drops to 50% _∼_ 65%, close to random guessing. This is much lower than the case without data obfuscation. Tables 1b and 2b shows the confusion matrices with the defense: the adversary’s true positives are decreased significantly, as he will mis-classify the training samples as non-members of the training set. **Accuracy.** We also need to consider the prediction accuracy of the target model with obfuscation. Figures 6 and 7 show the training and validation accuracy of the target model with two training set sizes. We consider different ratios ( _r_ = 0 _._ 25 _,_ 0 _._ 5 _,_ 1) of sensitive samples that are obfuscated. First we observe that in membership inference attacks, the validation accuracy is much lower that the training accuracy, indicating that the target models are overfitted. Shokri et al. [33] have the same conclusion and results, as the difference between training and validation accuracy 



<!-- Start of picture text -->
100% rr==01 100% rr==01 100% 100%<br>90% 90% 80% 80%<br>80% 80% 60% 60%<br>70% 70%<br>40% 40%<br>6500%% random guessing accuracy 6500%% random guessing accuracy 200%% rrrr====0001..255 200%% rrrr====0001..255<br>1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 0 5 10 15 20 25 30 0 5 10 15 20 25 30<br>classes classes epochs epochs<br>(a) 10k training samples (b) 2.5k training samples (a) Training accuracy (b) Validation accuracy<br>Figure 5: Accuracy of the membership inference attack. Figure 6: Prediction accuracy of machine learning models<br>in membership inference attack (10k training samples).<br>gives the adversary the opportunity to judge if one sample<br>is from training set or validation set. Second, obfuscating<br>100% 100%<br>smaller ratios of samples will not affect the validation ac-<br>curacy. When all the samples are obfuscated ( r = 1), the 80% 80%<br>validation accuracy degradation is within 5%, which is ac-<br>ceptable. 60% 60%<br>Table 1: Confusion matrix in membership inference attack 40% 40%<br>(10k training samples) 20% rr==00.25 20% rr==00.25<br>r=0.5 r=0.5<br>0% r=1 0% r=1<br>0 5 10 15 20 25 30 0 5 10 15 20 25 30<br>epochs epochs<br>(a) Training accuracy (b) Validation accuracy<br>Figure 7: Prediction accuracy of machine learning models<br>in membership inference attack (2.5k training samples).<br>aracccuy carccayu carccayu carccayu<br>y y<br>c c<br>a a<br>r r<br>u u<br>c c<br>c c<br>a a<br><!-- End of picture text -->

gives the adversary the opportunity to judge if one sample is from training set or validation set. Second, obfuscating smaller ratios of samples will not affect the validation accuracy. When all the samples are obfuscated ( _r_ = 1), the validation accuracy degradation is within 5%, which is acceptable. 

Table 1: Confusion matrix in membership inference attack (10k training samples) 

|(a)|_r_ = 0: _F_1|= 0_._86|(b)|_r_ = 1: _F_1|= 0_._52|
|---|---|---|---|---|---|
||Predicted:<br>**in**|Predicted:<br>**out**||Predicted:<br>**in**|Predicted:<br>**out**|
|Actual:<br>**in**|1|0|Actual:<br>**in**|0.44|0.56|
|Actual:<br>**out**|0.31|0.69|Actual:<br>**out**|0.26|0.74|



Figure 7: Prediction accuracy of machine learning models in membership inference attack (2.5k training samples). 

Table 2: Confusion matrix in membership inference attack (2.5k training samples) 

|(a)|_r_ = 0: _F_1|= 0_._89|(b)|_r_ = 1: _F_1|= 0_._51|
|---|---|---|---|---|---|
||Predicted:<br>**in**|Predicted:<br>**out**||Predicted:<br>**in**|Predicted:<br>**out**|
|Actual:<br>**in**|0.99|0.01|Actual:<br>**in**|0.41|0.59|
|Actual:<br>**out**|0.23|0.77|Actual:<br>**out**|0.2|0.8|



## **4.3 Model Inversion Attack** 

### _4.3.1 Attack_ 

Model inversion attack is a type of model privacy attack that can leak the statistical properties of samples with the same label. For instance, Fredrikson et al. [9] designed a model inversion attack, in which an adversary can recover recognizable images of people’s faces. In this attack, the adversary is interested in a group _g_<sup>_∗_</sup> of samples with the same feature, _i.e._ , same label: _F_ : _yi_ = _y_<sup>_∗_</sup> . He wants to recover the statistical property of these samples, _i.e._ , the average value: _P_ ( _g_<sup>_∗_</sup> ) = _avg_ ( _xi_ ). The adversary retrieves the statistical property from the model parameters and outputs. 

Recovering such statistical property is an optimization problem. For the above face recognition model inversion attack, given a person’s name (label), the adversary’s goal is to 

find the image, whose output from the model has the highest confidence score in that person’s class. The adversary can use gradient descent method to solve this optimization problem and recover the image of that person. 

**Implementation.** We reproduce this attack from [9]. We adopt the AT&T Face Database [31]. This database contains 40 classes with each one has 10 gray-scaled images of one person. We pick five persons from the database and their original faces are shown in Figure 8a. Figure 8b shows the corresponding images recovered by the adversary. We can see the recovered images are very close to the original ones and the adversary can easily identify the looking of one person from the attack results. 

### _4.3.2 Defense_ 

We use Algorithm 2 to hide the statistical property of sensitive samples. For the sensitive class, we add some new samples to the training set. These samples are synthesized as the negative values of the original images. So when the adversary conducts the model inversion attack to obtain the average value of the training samples in that class, the new samples will hide the information of the original ones. **Privacy** . Figures 8c – 8e show the recovered images after we add different numbers of samples into the training set. We use _r_ to denote the ratio of the new samples to the original ones. We can observe that the added noisy samples can obscure the adversary’s observations. This obfuscation operation is more effective when _r_ is larger. When we add 





<!-- Start of picture text -->
(a) Target images<br>(b) Recovered images<br>(c) Recovered images with r = 0 . 25<br>(d) Recovered images with r = 0 . 5<br>(e) Recovered images with r = 1<br>Figure 8: Model inversion attack and the defense<br><!-- End of picture text -->

the same number of new samples ( _r_ = 1) to the training set, the adversary can hardly recognize the persons’ faces. **Accuracy.** Figure 9 shows the training and validation accuracies versus the number of training epochs with different ratios of new added samples. We use _r_ = 0 as the baseline. We can see that with the new synthetic samples, model training takes a little longer time to reach stable results. However, the model accuracy remains the same. This confirms that adding new samples do not affect the model accuracy of the old samples. 

## **4.4 Model Classification Attack** 

### _4.4.1 Attack_ 

Last, we consider model classification attacks that target on the entire training set ( _F_ : _xi, yi ∈ D_ ) [5]. The adversary wants to learn some attributes of the training set, _P_ ( _g_<sup>_∗_</sup> = _D_ ) = _attr_ ( _xi_ ). Ateniese et al. [5] gave two examples about the training set attributes: inferring if the voice training samples contain Indian accents in a speech recognition, and inferring if Google web traffic is used in a network traffic classification task. In this attack setting, the adversary is assumed to have access to the model parameters, and infer the attributes from these parameters. 

Similar to membership inference attack, the adversary can 



<!-- Start of picture text -->
100%<br>100%<br>80%<br>80%<br>60%<br>60%<br>40%<br>40%<br>20% rr==00.25 20% rr==00.25<br>r=0.5 r=0.5<br>0% r=1 0% r=1<br>0 50 100 150 200 250 0 100 200 300 400<br>epochs epochs<br>(a) Training accuracy (b) Validation accuracy<br>y y<br>c c<br>aru aru<br>c c<br>c c<br>a a<br><!-- End of picture text -->

Figure 9: Prediction accuracy of machine learning models in model inversion attack. 

build a classifier to predict the property. Specifically, the adversary can first train a number of shadow models. Some of the shadow models are trained over the training set with the property _P_ . These shadow models are labeled as 1. The rest shadow models are trained over the training set without the property. These shadow models are labeled as 0. Then the adversary retrieves the parameters of each shadow model as the features, and trains a new classifier over these features and model labels. This classifier can map the model parameters to the model labels, _i.e._ , whether the training set used in this model has the property or not. So given the target model, the adversary can retrieve its model parameters, feed them into the classifier and predict if the training set of this model has the property. 

**Implementation.** Since detailed attack code, machine learning algorithms and training dataset are not opensourced in [5], we implement a new attack using the same technique. We consider a handwritten digit classification task, which uses LeNet neural network to classify digits “0” – “9” from handwritten images. The adversary wants to learn the property that _if the training set is MNIST [20] or not_ . In our experiment, the adversary trains 100 shadow models with MNIST and 100 shadow models with another handwritten image dataset, EMNIST [8]. For each shadow model, the adversary retrieves all the trainable parameters in each neural network layer ( `conv1/kernel` , `conv1/bias` , `conv2/kernel` , `conv2/bias` , `fc1/kernel` , `fc1/bias` , `fc2/kernel` , `fc2/bias` ), and calculates the mean and standard deviation of each parameter vector. This generates 16 values, representing the feature of the shadow model. Then the adversary builds a classifier using logistic regression to classify the MNIST or non-MNIST shadow models from the feature values. To measure the adversary’s classification accuracy, we train another 100 models with MNIST and 100 models with EMNIST for validation. Table 3a shows the confusion matrix of the classification. We can observe that the classifier has a very good performance: only 1 model with non-MNIST is mis-classified as EMNIST. The F1-score is 0.995. 

### _4.4.2 Defense_ 

Similar to model inversion attack, we can obfuscate the entire training data by augmenting the dataset with synthetic samples that are negative of original ones (Algorithm 2). With these faked samples, the statistical property of the original dataset is hidden from the adversary’s classifier. 

Table 3: Confusion matrix in model classification attack 



<!-- Start of picture text -->
(a) r = 0: F 1 = 0 . 995 (b) r = 0 . 25: F 1 = 0 . 246<br>Predicted: Predicted: Predicted: Predicted:<br>MNIST non-MNIST MNIST non-MNIST<br>Actual: Actual:<br>0.99 0.01 0.14 0.86<br>MNIST MNIST<br>Actual: Actual:<br>0 1 0 1<br>non-MNIST non-MNIST<br><!-- End of picture text -->

|(c) _r_ =|0_._5: _F_1|= 0_._198|(d) _r_ =|1: _F_1|= 0_._077|
|---|---|---|---|---|---|
||Predicted:<br>**MNIST**|Predicted:<br>**non-MNIST**||Predicted:<br>**MNIST**|Predicted:<br>**non-MNIST**|
|Actual:<br>**MNIST**|0.11|0.89|Actual:<br>**MNIST**|0.04|0.96|
|Actual:<br>**non-MNIST**|0|1|Actual:<br>**non-MNIST**|0|1|





<!-- Start of picture text -->
100% 100%<br>80% 80%<br>60% 60%<br>40% 40%<br>r=0 r=0<br>20% r=0.25 20% r=0.25<br>r=0.5 r=0.5<br>r=1 r=1<br>0% 0%<br>0 20 40 60 80 100 0 20 40 60 80 100<br>epochs epochs<br>(a) Training accuracy (b) Validation accuracy<br>y y<br>c c<br>a a<br>r r<br>u u<br>c c<br>c c<br>a a<br><!-- End of picture text -->

Figure 10: Prediction accuracy of machine learning models in model classification attack. 

**Privacy.** Tables 3b – 3d show the confusion matrices of the adversary’s classifier when we add different ratios of synthetic samples. We can observe that with the augmented dataset, most MNIST models will be classified as non-MNIST, and the defense is more effective when the added sample ratio _r_ increases. One interesting observation is that adding new samples cannot make the adversary mis-classify the non-MNIST model as MNIST model. This is because EMNIST is already an extended version of MNIST and contains different types of handwritten digits. So adding noise to this dataset makes it more extended and less like pure MNIST data. But this is already effective in protecting the statistical properties of training set: when the adversary feeds the target model into his classifier, he will always get the nonMNIST label, and cannot tell if the training dataset of the target model is MNIST or not. 

**Accuracy.** Figure 10 shows the prediction accuracy of the training set that is augmented and the validation set during the training process. We observe that adding new noisy samples to the training set has very small impact to the training performance: when adding the same number of synthetic samples as the original ones, it takes almost the same amount of time to reach the same high accuracy. 

## **5. RELATED WORK** 

## **5.1 Machine Learning Privacy Attacks** 

Different types of attacks were designed to breach the privacy of machine learning models or datasets. 

**Training data privacy.** Training data is a popular target for adversaries to steal during the model training or serving phases. Ateniese et al. [5] proposed the model classification attack: given a target model, an adversary is able to extract some meaningful attributes of the training dataset. The basic attack strategy is to train different shadow models 

over datasets with different attributes. Then the adversary can build a new classifier which can predict the dataset attributes based on a model parameter as the feature. 

Shokri et al. [33] proposed the membership inference attacks to infer if one individual sample is included in the training set of the target model. The attack technique is similar to [5]: the adversary builds a quantity of shadow models with different training datasets. He collects the prediction results of the training samples and validation samples from each shadow model. Using the prediction results as features and whether the sample is from training set or validation set as the labels, the adversary can build a new classifier to predict the membership given a sensitive sample and a target model. Salem et al. [30] simplified the attacks by relaxing some assumptions, _e.g._ , using multiple shadow models, knowledge of the target model structure and dataset from the same distribution. Further studies show that membership inference attacks are possible even when the target models are not overfitted [22,38]. Membership inference attacks are also demonstrated in Generative Adversarial Networks [14,21]. Melis et al. [24] studies the inference attacks in collaborative learning: the adversary can learn the membership of training data used by other participants, based on the shared parameters in a distributed learning system. 

Fredrikson et al. [10] proposed the model inversion attacks: given a machine learning model, part of a sensitive sample’s features and its label, the adversary is able to recover the rest features of this sample. The adversary’s strategy is to reverse the model training process: figuring out the mapping from the output to input and predicting the input feature that best matches the output label. An advanced model inversion attack over deep neural network was proposed in [9] which is able to inverse an image classification model and recover an image given the corresponding label of the image. Hitaj et al. [16] demonstrated the possibility of model inversion attacks in collaborative learning even under privacy-preserving protection. They adopted the Generative Adversary Network to actively recover the private data samples used by other participants. 

Song et al. [34] proposed model memorization attacks, in which the adversary has direct access to the training data. He attempts to encode the sensitive data into the model for a receiver entity to retrieve them. Two cases were considered: if the receiver entity has white-box access to the produced model, then the adversary can directly encode the training data into the model parameters; if the receiver party only has black-box access to the model, then the adversary can encode the training data into the outputs corresponded to some specific inputs. In these ways, the private training samples are leaked from model parameters or outputs. **Model privacy.** In addition to the training set, adversaries may also be interested in the privacy of machine learning models. Tram`er et al. [35] proposed an attack to steal 

machine learning models using prediction APIs. The basic idea is that the adversary can generate a quantity of input samples and feed them into the target model for prediction. With the predicted outputs, the adversary can discover the model that best represents the relationships between inputs and outputs. Oh et al. [25] built metamodels to extract more model details such as neural network architecture, which is assumed public in [35]. Wang et al. [37] designed attacks to steal the hyperparameter of the machine learning model. A hyperparameter is used to balance the loss function and regularization term in the objective function. The adversary can obtain this value from the training set and model. The hyperparameter can further help the adversary recover the model parameters in a more efficient way. 

In this paper we consider the privacy attacks on the training data, so model privacy is out of the scope, as models are usually public and less private than the training dataset. We design a generic methodology that can cover different types of privacy attacks with different adversary’s capabilities, and protect the privacy of different properties of training data. 

## **5.2 Machine Learning Privacy Solutions** 

**Enhancing the algorithms.** One solution is to design secure algorithms to prevent information leakage during model training. Shokri and Shmatikov [32] proposed to use distributed training to protect the privacy of training data: different participants can train the model with their data locally and only upload the parameters with differential privacy noise, so training data will not be leaked to unauthorized parties. Hamm et al. [12] applied the same idea to privacy machine learning in distributed IoT sensing systems. Cao et al. [7] proposed a methodology to modify the training algorithms to remove the effects of sensitive training samples on the models. Ohrimenko et al. [26] proposed to use Intel SGX-processors to protect the training tasks against privileged adversaries in the host environment. They also designed data-oblivious machine learning algorithms that can eliminate the data-dependent accesses. Similarly, Hunt et al. [17] used Intel SGX to restrict the confidential training data from being leaked to adversaries. Abadi et al. [4] applied differential privacy mechanism to design privacypreserving deep learning algorithm: they added noise during the stochastic gradient descent process to eliminate the model parameters’ dependency on the training dataset. 

The above methodologies have some drawbacks. First, the distributed privacy-preserving approach [32] can only protect the privacy of individual samples, but does not prevent property inference attacks that apply to groups of training samples [24]. Second, for the above methods, we must assume that the designed machine learning algorithms and schemes can be correctly deployed in MLaaS. However, if the adversary takes control of the machine learning platform, he may not run the enhanced algorithms or systems for privacy protection. Third, if the adversary has direct access to the training data [34], then enhancing the training process does not work. Fourth, for SGX-assistant solutions, new hardware support is required, which makes it hard and impractical to deploy. Besides, SGX solutions cannot be applied to GPU architecture, which is now widely used in machine learning tasks. 

**Enhancing the dataset.** Enhancing the dataset has advantages over enhancing the training algorithms: even the adversary has direct access to the training data or MLaaS 

platform, he cannot get the sensitive data from the enhanced set. Bost et al. [6] proposed to encrypt the dataset before feeding them into the training algorithm. They designed machine learning operators which can operate on the encrypted data. By doing so the adversary cannot get the data if he does not have the encryption key. Although Homomorphic encryption works but it is hard to be applied to any arbitrary algorithm, and the performance is not efficient. 

Triastcyn and Faltings [36] proposed to use Generative Adversarial Network with differential-privacy to generate artificial data for deep learning. This idea is similar to our data obfuscation methodology. However, their approach is lack of strict differential privacy guarantees. The artificial data generated by their approach is quite close to real samples, with very minor differences in details. This is not enough for privacy preservation. Besides, they cannot defeat inference attacks against statistical properties, as the new samples still keep the characteristics of original ones. In contrast, we exploit the obfuscation operations on the training dataset to hide the sensitive properties while maintaining the model’s prediction accuracy. We empirically show that this solution can defeat different types of data privacy attacks. 

## **6. CONCLUSION** 

The fast development of machine learning techniques have raised the security concern of data privacy. Past work have shown that an adversary can easily steal properties about the sensitive training samples in a MLaaS platform. We propose a generic approach to protect the privacy of training data by obfuscating the training set. We consider the protection of sensitive properties of individual samples, as well as statistical properties of groups of samples. Our empirical evaluations indicate this method can effective defeat a wide range of existing privacy attacks without affecting the training performance and prediction accuracy. Future work include the optimization of adding noise to individual samples by selecting minimal key feature values, and using GAN to generate new dataset to hide statistical properties. 

## **7. REFERENCES** 

- [1] `https://aws.amazon.com/sagemaker/` , 2018. 

- [2] `https://cloud.google.com/mlengine/docs/technical-overview` , 2018. 

- [3] `https://azure.microsoft.com/enus/services/machine-learning-studio/` , 2018. 

- [4] M. Abadi, A. Chu, I. Goodfellow, H. B. McMahan, I. Mironov, K. Talwar, and L. Zhang. Deep learning with differential privacy. In _ACM Conference on Computer and Communications Security_ , 2016. 

- [5] G. Ateniese, L. V. Mancini, A. Spognardi, A. Villani, D. Vitali, and G. Felici. Hacking smart machines with smarter ones: How to extract meaningful data from machine learning classifiers. _International Journal of Security and Networks_ , 2015. 

- [6] R. Bost, R. A. Popa, S. Tu, and S. Goldwasser. Machine learning classification over encrypted data. In _Network and Distributed System Security Symposium_ , 2015. 

- [7] Y. Cao and J. Yang. Towards making systems forget with machine unlearning. In _IEEE Symposium on Security and Privacy_ , 2015. 

- [8] G. Cohen, S. Afshar, J. Tapson, and A. van Schaik. Emnist: an extension of mnist to handwritten letters. _arXiv preprint arXiv:1702.05373_ , 2017. 

- [9] M. Fredrikson, S. Jha, and T. Ristenpart. Model inversion attacks that exploit confidence information and basic countermeasures. In _ACM Conference on Computer and Communications Security_ , 2015. 

- [10] M. Fredrikson, E. Lantz, S. Jha, S. Lin, D. Page, and T. Ristenpart. Privacy in pharmacogenetics: An end-to-end case study of personalized warfarin dosing. In _USENIX Security Symposium_ , 2014. 

- [11] I. Goodfellow, Y. Bengio, A. Courville, and Y. Bengio. _Deep learning_ , volume 1. MIT press Cambridge, 2016. 

- [12] J. Hamm, A. C. Champion, G. Chen, M. Belkin, and D. Xuan. Crowd-ml: A privacy-preserving learning framework for a crowd of smart devices. In _IEEE International Conference on Distributed Computing Systems_ , 2015. 

- [13] A. Y. Hannun, C. Case, J. Casper, B. Catanzaro, G. Diamos, E. Elsen, R. Prenger, S. Satheesh, S. Sengupta, A. Coates, and A. Y. Ng. Deep Speech: Scaling Up End-to-end Speech Recognition. _CoRR_ , abs/1412.5567, 2014. 

- [14] J. Hayes, L. Melis, G. Danezis, and E. De Cristofaro. Logan: evaluating privacy leakage of generative models using generative adversarial networks. _arXiv preprint arXiv:1705.07663_ , 2017. 

- [15] K. He, X. Zhang, S. Ren, and J. Sun. Deep Residual Learning for Image Recognition. _CoRR_ , abs/1512.03385, 2015. 

- [16] B. Hitaj, G. Ateniese, and F. P´erez-Cruz. Deep models under the gan: information leakage from collaborative deep learning. In _ACM Conference on Computer and Communications Security_ , 2017. 

- [17] T. Hunt, C. Song, R. Shokri, V. Shmatikov, and E. Witchel. Chiron: Privacy-preserving machine learning as a service. _arXiv preprint arXiv:1803.05961_ , 2018. 

- [18] A. Krizhevsky and G. Hinton. Learning multiple layers of features from tiny images. Technical report, Citeseer, 2009. 

- [19] Y. Le Cun, L. Jackel, B. Boser, J. Denker, H. Graf, I. Guyon, D. Henderson, R. Howard, and W. Hubbard. Handwritten Digit Recognition: Applications of Neural Network Chips and Automatic Learning. _IEEE Communications Magazine_ , 27(11):41–46, 1989. 

- [20] Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner. Gradient-based learning applied to document recognition. _Proceedings of the IEEE_ , 86(11), 1998. 

- [21] K. S. Liu, B. Li, and J. Gao. Generative model: Membership attack, generalization and diversity. _arXiv preprint arXiv:1805.09898_ , 2018. 

- [22] Y. Long, V. Bindschaedler, L. Wang, D. Bu, X. Wang, H. Tang, C. A. Gunter, and K. Chen. Understanding membership inferences on well-generalized learning models. _arXiv preprint arXiv:1802.04889_ , 2018. 

- [23] M. Luong, H. Pham, and C. D. Manning. Effective Approaches to Attention-based Neural Machine Translation. _CoRR_ , abs/1508.04025, 2015. 

learning. _arXiv preprint arXiv:1805.04049_ , 2018. 

   - [25] S. J. Oh, M. Augustin, M. Fritz, and B. Schiele. Towards reverse-engineering black-box neural networks. In _INternational Conference on Learning Representations_ , 2018. 

   - [26] O. Ohrimenko, F. Schuster, C. Fournet, A. Mehta, S. Nowozin, K. Vaswani, and M. Costa. Oblivious multi-party machine learning on trusted processors. In _USENIX Security Symposium_ , 2016. 

   - [27] H. Robbins and S. Monro. A stochastic approximation method. _The annals of mathematical statistics_ , pages 400–407, 1951. 

   - [28] F. Rosenblatt. The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain. _Psychological review_ , 65(6):386, 1958. 

   - [29] D. E. Rumelhart, G. E. Hinton, and R. J. Williams. Learning Representations by Back-propagating Errors. _nature_ , 323(6088):533, 1986. 

   - [30] A. Salem, Y. Zhang, M. Humbert, M. Fritz, and M. Backes. Ml-leaks: Model and data independent membership inference attacks and defenses on machine learning models. _arXiv preprint arXiv:1806.01246_ , 2018. 

   - [31] F. S. Samaria and A. C. Harter. Parameterisation of a stochastic model for human face identification. In _IEEE Workshop on Applications of Computer Vision_ , 1994. 

   - [32] R. Shokri and V. Shmatikov. Privacy-preserving deep learning. In _ACM Conference on Computer and Communications Security_ , 2015. 

   - [33] R. Shokri, M. Stronati, C. Song, and V. Shmatikov. Membership inference attacks against machine learning models. In _IEEE Symposium on Security and Privacy_ , 2017. 

   - [34] C. Song, T. Ristenpart, and V. Shmatikov. Machine learning models that remember too much. In _ACM Conference on Computer and Communications Security_ , 2017. 

   - [35] F. Tram`er, F. Zhang, A. Juels, M. K. Reiter, and T. Ristenpart. Stealing machine learning models via prediction apis. In _USENIX Security Symposium_ , 2016. 

   - [36] A. Triastcyn and B. Faltings. Generating artificial data for private deep learning. _arXiv preprint arXiv:1803.03148_ , 2018. 

   - [37] B. Wang and N. Z. Gong. Stealing hyperparameters in machine learning. In _IEEE Symposium on Security and Privacy_ , 2018. 

   - [38] S. Yeom, I. Giacomelli, M. Fredrikson, and S. Jha. Privacy risk in machine learning: Analyzing the connection to overfitting. In _IEEE Computer Security Foundations Symposium_ , 2018. 

   - [39] C. Zhang, S. Bengio, M. Hardt, B. Recht, and O. Vinyals. Understanding deep learning requires rethinking generalization. In _International Conference on Learning Representations_ , 2017. 

   - [40] Z. Zhong, L. Zheng, G. Kang, S. Li, and Y. Yang. Random erasing data augmentation. _arXiv preprint arXiv:1708.04896_ , 2017. 

- [24] L. Melis, C. Song, E. De Cristofaro, and V. Shmatikov. Inference attacks against collaborative 


