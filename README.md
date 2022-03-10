# CWG Audition Project

*Analyzing the Eastern Pacific Oscillation 
The EPO is a key teleconnection for U.S. weather patterns, especially in the winter. This two-part project  develops a quick climatology tool to help the CWG forecasters with EPO baseline expectations and starts  the planning process for ideas for subseasonal forecasting support.* 

# Part One: EPO Climatology 
*We are sending you the historical daily .csv file for the EPO index back to 1950. We would like to develop a climatology baseline for this to determine historical-based probabilities for different times of the year for extreme events like one and two standard deviations +EPO and -EPO occurrences. Please write a program that does this, that would be designed to update daily with new EPO information, and  make the code and output available to the CWG team.*

For this problem, the code I have written assumes that new data will be uploaded daily (and the code run again), but using the [NOAA website](https://psl.noaa.gov/data/timeseries/daily/EPO/) would allow for the program to automatically grab new data as it is uploaded, as well as run for new results.

![alt text](https://github.com/austin-snyder/cwg_audition/blob/main/epoindexmean.png?raw=true)

The above graph is representative of the deviation in the expected EPO index on an annual basis. Over the course of any given year, the expected (mean) EPO index for each day is represented by the darker blue line, while the approximate 95% confidence interval for this expected value is represented by the lighter blue fill. Through this first graph, it can be seen that there is greater deviation from the overall mean (~0) during the winter months, while the summer months have values more consistently near zero.

![alt text](https://github.com/austin-snyder/cwg_audition/blob/main/epoprobability.png?raw=true)

This second graph is representative of the historical probability of extreme EPO index values ('events'). Over the course of any given year, the probability of an EPO index being at least 1 standard deviation greater or less than the overall mean is represented by the salmon-colored line, while the red-colored line represents the probability for 2 standard deviations. Similar to the results of the first graph, it can be seen that there is greater likelihood for 'deviant events' in the winter months, while the summer months have a near-zero likelihood for index values 2 standard deviations greater or less than the overall mean.

# Part Two: Developing an EPO Long-Lead Indicator 
*In 500 words or less, please describe potential strategies we could employ to develop probabilistic  expectations for EPO in the subseasonal 16-30 day outlook (weeks 3-4) space. Include thoughts (1)  unknowns/assumptions, (2) possible challenges, and (3) on required resources such as  time/compute/storage. Include potential ML algorithms that could be best suited to solve this problem  with any potential drawbacks too.*

I’ve written the following under the assumption that subseasonal EPO predictions have similar properties to other meteorological forecasting, like temperature and precipitation:

There are 2 types of potential models that could be used for subseasonal Eastern Pacific Oscillation (EPO) predictions: physics-based and data-based.

A physics-based model would rely on principles of thermodynamics, projecting changes to EPO through examining how a simulated ocean-atmosphere state is likely to change over time. Though this can lead to high-accuracy results, a physical model in this scenario would likely run into issues with computational time storage due to the complex nature of the ocean-atmosphere system being considered. Additionally, chaotic behavior and system noise make it difficult to ensure result validity. In contrast, a traditional data-based model would rely on tools like regression analysis rather than physics-based equations. Generally, this means certain assumptions must be met by the data to ensure model outcomes are viable. Between this and the possibility of outputs falling outside the range of real-world possibilities without a physics-based tether, it is difficult to achieve comprehensive, high-accuracy models through traditional data-based methods. <sup>[1](https://doi.org/10.1029/2021MS002502)</sup>

The most promising strategy for addressing these difficulties is employing modern data-based models that incorporate machine learning (ML) techniques. As a general rule, ML techniques often excel where statistical methods struggle, with high uncertainty tolerance, little-to-no assumption requirements, and the ability to analyze incredibly large datasets. Similarly, by including physical relationships as constraints rather than as primary algorithmic pieces, an ML model would be able to emulate or improve upon the accuracy of a physics-based model without the high computational time and space needs.

Machine learning learning techniques can generally be categorized into three groups: supervised, unsupervised, and reinforcement. Because the dataset dealt with here is one in which the inputs & their relationships are not fully understood, but the dataset being dealt with includes known outcomes (EPO indices), supervised learning would be most applicable. Specifically, artificial neural networks (NNs) would likely excel in both classification (determine if EPO index will be negative/positive) and regression (determine actual EPO index) in this scenario. Convolutional NNs would also excel if available data included geospatial images, and recurrent NNs would be useful for analysis of time-dependent features. However, deep learning models like these have had issues handling quasi-periodic or continuous changes in meteorological data, making overfitting a concern even if the data is properly split into training, development, and evaluation sets. <sup>[2](https://doi.org/10.3389/fphy.2019.00153)</sup>

In particular cases where more is understood about the data or there is a larger feature-data ratio, non-deep learning techniques may also excel on a case-by-case basis. For simply using past EPO values to predict future ones, Naive Bayes or Extra Trees/Random Forest would be more than enough and perform their function with fewer computational and space resources. However, all machine learning techniques in this scenario face the issue of low accuracy in highly-specific cases like extreme EPO values due to the relatively small amount of data even available to be analyzed. This could potentially be addressed in neural networks through the isolation of extreme events by emulating the human mind’s significance classification, but this is an area of ongoing research. <sup>[3](https://doi.org/10.48550/arXiv.2110.09304)</sup>

[1] Weyn, J., Durran, D., Caruana, R., & Cresswell-Clay, N. (2021). Sub-Seasonal Forecasting With a Large Ensemble of Deep-Learning Weather Prediction Models. Journal of Advances in Modeling Earth Systems. 13(7). https://doi.org/10.1029/2021MS002502.

[2] Dijkstra, H., Petersik, P., Hernández-García, E., & López, C. (2019). The Application of Machine Learning Techniques to Improve El Niño Prediction Skill. Frontiers in Physics. https://doi.org/10.3389/fphy.2019.00153.

[3] Meiyazhagan, J., Sudharsan, S., Venkatasen, A., & Senthilvelan, M. (2021). Prediction of Occurrence of Extreme Events using Machine Learning. The European Physical Journal Plus. https://doi.org/10.48550/arXiv.2110.09304. 
