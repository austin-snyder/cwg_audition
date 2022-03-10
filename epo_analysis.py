# import needed libraries
import pandas as pd
import numpy as np
import scipy.stats as scist
import matplotlib.pyplot as plt

# import data as pandas dataframe
epodf = pd.read_csv('epo.csv')

# calculate statistical measurements for all EPO indices
epoavg = epodf.mean()
epostd = epodf.std()

# string to datetime
epodf['Date'] = pd.to_datetime(epodf['Date'])

# add column with year dropped to analyze individual days
epodf['Month-Day'] = epodf['Date'].dt.strftime('%m-%d')

# grab numpy array of unique days
keys = epodf['Month-Day'].unique()

# calculate mean and standard deviation for each unique day
epodatalst = []
for key in keys:
    daydata = epodf[epodf['Month-Day'] == key]['Value']
    epodatalst.append([key, daydata.mean(), daydata.std()])

# create dataframe of statistical measurements for unique days
epodays = pd.DataFrame(data=epodatalst, columns=['Day', 'Mean', 'StD']).sort_values(by='Day').reset_index(drop=True)

# assuming normal distribution, calculate daily likelihood of extreme highs/lows
extremelst1 = []
extremelst2 = []
cilst = []
for i, day in epodays.iterrows():
    nDist = scist.norm(day['Mean'], day['StD'])

    extremeHigh1 = 1 - nDist.cdf(epoavg + epostd)[0]
    extremeHigh2 = 1 - nDist.cdf(epoavg + 2*epostd)[0]
    extremeLow1 = nDist.cdf(epoavg - epostd)[0]
    extremeLow2 = nDist.cdf(epoavg - 2*epostd)[0]
    extreme1 = extremeHigh1 + extremeLow1
    extreme2 = extremeHigh2 + extremeLow2

    # calculate confidence 
    ci = 1.96 * day['StD']/np.sqrt(50)

    extremelst1.append(extreme1)
    extremelst2.append(extreme2)
    cilst.append(ci)

# plot separate line data for both 1σ and 2σ
fig, ax = plt.subplots(figsize=(12,6), dpi=100)
plt.plot_date(epodays['Day'].tolist(), extremelst1, color='salmon', alpha=0.5, linestyle='solid', marker='None', label='+/- 1σ')
plt.plot_date(epodays['Day'].tolist(), extremelst2, color='red', alpha=0.5, linestyle='solid', marker='None', label='+/- 2σ')

# format plot
plt.ylabel('Probability of Extreme Events')
plt.xlabel('Time of Year')
plt.xticks(np.array([0, 31, 60, 91, 121, 152, 182, 213, 243, 274, 305, 335]),
           labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend()
plt.title('Eastern Pacific Oscillation')
ax.fill_between(epodays['Day'].tolist(), extremelst2, extremelst1, color='salmon', alpha=0.1)
ax.fill_between(epodays['Day'].tolist(), [0] * 366, extremelst2, color='red', alpha=0.1)
plt.savefig('epoprobability.png')
plt.clf()
plt.close()

fig, ax = plt.subplots(figsize=(12, 6), dpi=100)
plt.plot_date(epodays['Day'].tolist(), epodays['Mean'].tolist(), color='blue', alpha=1, linestyle='solid', marker='None', label='EPO Index')

# format plot
plt.ylabel('EPO Index Mean')
plt.xlabel('Time of Year')
plt.xticks(np.array([0, 31, 60, 91, 121, 152, 182, 213, 243, 274, 305, 335]),
           labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend()
plt.title('Eastern Pacific Oscillation')
ax.fill_between(epodays['Day'].tolist(), epodays['Mean'].subtract(cilst), epodays['Mean'].add(cilst), color='b', alpha=.1)
plt.savefig('epoindexmean.png')
plt.clf()
plt.close()

print()