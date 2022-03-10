# CWG Audition Project

Analyzing the Eastern Pacific Oscillation 
The EPO is a key teleconnection for U.S. weather patterns, especially in the winter. This two-part project  develops a quick climatology tool to help the CWG forecasters with EPO baseline expectations and starts  the planning process for ideas for subseasonal forecasting support. 

# Part One: EPO Climatology 
We are sending you the historical daily .csv file for the EPO index back to 1950. We would like to develop a climatology baseline for this to determine historical-based probabilities for different times of the year for extreme events like one and two standard deviations +EPO and -EPO occurrences. Please write a program that does this, that would be designed to update daily with new EPO information, and  make the code and output available to the CWG team.

![alt text](https://github.com/austin-snyder/cwg_audition/blob/main/epoindexmean.png?raw=true)

The above graph is representative of the deviation in the expected EPO index on an annual basis. Over the course of any given year, the expected (mean) EPO index for each day is represented by the darker blue line, while the approximate 95% confidence interval for this expected value is represented by the lighter blue fill. Through this first graph, it can be seen that there is greater deviation from the overall mean (~0) during the winter months, while the summer months have values more consistently near zero.

![alt text](https://github.com/austin-snyder/cwg_audition/blob/main/epoprobability.png?raw=true)

This second graph is representative of the historical probability of extreme EPO index values ('events'). Over the course of any given year, the probability of an EPO index being at least 1 standard deviation greater or less than the overall mean is represented by the salmon-colored line, while the red-colored line represents the probability for 2 standard deviations. Similar to the results of the first graph, it can be seen that there is greater likelihood for 'deviant events' in the winter months, while the summer months have a near-zero likelihood for index values 2 standard deviations greater or less than the overall mean.

# Part Two: Developing an EPO Long-Lead Indicator 
In 500 words or less, please describe potential strategies we could employ to develop probabilistic  expectations for EPO in the subseasonal 16-30 day outlook (weeks 3-4) space. Include thoughts (1)  unknowns/assumptions, (2) possible challenges, and (3) on required resources such as  time/compute/storage. Include potential ML algorithms that could be best suited to solve this problem  with any potential drawbacks too.
