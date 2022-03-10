# Import needed libraries.
import pandas as pd
import numpy as np
import scipy.stats as scist
import matplotlib.pyplot as plt

# Import data as Pandas DataFrame and
# calculate statistical measurements for all EPO indices.
epodf = pd.read_csv('epo.csv')
epoavg = epodf.mean()
epostd = epodf.std()

# Convert strings in 'Date' column to DateTime and
# create new date string column with just month-day.
epodf['Date'] = pd.to_datetime(epodf['Date'])
epodf['Month-Day'] = epodf['Date'].dt.strftime('%m-%d')

# Create NumPy Array of unique month-day combinations.
keys = epodf['Month-Day'].unique()

# Calculate statistical measurements for EPO indices within each unique month-day.
epodatalst = []
for key in keys:
    daydata = epodf[epodf['Month-Day'] == key]['Value']
    epodatalst.append([key, daydata.mean(), daydata.std()])

# Create new Pandas DataFrame consisting of:
#   each unique month-day,
#   the associated mean, and
#   the associated standard deviation.
epodays = pd.DataFrame(data=epodatalst, columns=['Day', 'Mean', 'StD']).sort_values(by='Day').reset_index(drop=True)

# Create blank lists for later population.
extremelst1 = []
extremelst2 = []
cilst = []

# Loop through each unique month-day.
for i, day in epodays.iterrows():

    # Create SciPy Normal Distribution for month-day data.
    nDist = scist.norm(day['Mean'], day['StD'])

    # Calculate probability of extreme highs and lows for each month-day.
    extremeHigh1 = 1 - nDist.cdf(epoavg + epostd)[0]
    extremeHigh2 = 1 - nDist.cdf(epoavg + 2*epostd)[0]
    extremeLow1 = nDist.cdf(epoavg - epostd)[0]
    extremeLow2 = nDist.cdf(epoavg - 2*epostd)[0]
    extreme1 = extremeHigh1 + extremeLow1
    extreme2 = extremeHigh2 + extremeLow2

    # Calculate variable for later use in confidence interval creation for month-day means. 
    ci = 1.96 * day['StD']/np.sqrt(50)

    # Iteratively populate lists with information to be plotted.
    extremelst1.append(extreme1)
    extremelst2.append(extreme2)
    cilst.append(ci)

# Plot line data for both 1σ and 2σ probabilities.
fig, ax = plt.subplots(figsize=(12,6), dpi=100)
plt.plot_date(epodays['Day'].tolist(), extremelst1, color='salmon', alpha=0.5, linestyle='solid', label='+/- 1σ')
plt.plot_date(epodays['Day'].tolist(), extremelst2, color='red', alpha=0.5, linestyle='solid', label='+/- 2σ')

# Format plot for readability.
plt.ylabel('Probability of Extreme Events')
plt.xlabel('Time of Year')
plt.xticks(np.array([0, 31, 60, 91, 121, 152, 182, 213, 243, 274, 305, 335]),
           labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend()
plt.title('Eastern Pacific Oscillation')
ax.fill_between(epodays['Day'].tolist(), extremelst2, extremelst1, color='salmon', alpha=0.1)
ax.fill_between(epodays['Day'].tolist(), [0] * 366, extremelst2, color='red', alpha=0.1)

# Save and close plot.
plt.savefig('epoprobability.png')
plt.clf()
plt.close()

# Plot line data for mean EPO index values, as well as associate confidence intervals.
fig, ax = plt.subplots(figsize=(12, 6), dpi=100)
plt.plot_date(epodays['Day'].tolist(), epodays['Mean'].tolist(), color='blue', alpha=1, linestyle='solid', label='EPO Index')
ax.fill_between(epodays['Day'].tolist(), epodays['Mean'].subtract(cilst), epodays['Mean'].add(cilst), color='b', alpha=.1)

# Format plot for readability.
plt.ylabel('EPO Index Mean')
plt.xlabel('Time of Year')
plt.xticks(np.array([0, 31, 60, 91, 121, 152, 182, 213, 243, 274, 305, 335]),
           labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend()
plt.title('Eastern Pacific Oscillation')

# Save and close plot.
plt.savefig('epoindexmean.png')
plt.clf()
plt.close()
