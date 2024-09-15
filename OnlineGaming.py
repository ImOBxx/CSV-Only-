import numpy as np
import pandas as pd
import re

df = pd.read_csv('online_gaming_behavior_dataset.csv')
#print(df.head())

"""
asdm = np.array(df["AvgSessionDurationMinutes"])

print(asdm)

print("Mean Gaming Hours: ", np.mean(asdm))
print("Maximum Gaming Duration: ", np.max(asdm))
print("Minimum Gaming Duration: ", np.min(asdm))
print("Standard Deiviation: ", np.std(asdm))
print("Variance: ", np.var(asdm))
print("36th Percentile: ", np.percentile(asdm, 36))
print("1st Quantile: ", np.quantile(asdm, 1))
print("Median: ", np.median(asdm))
print("Histogram: ", np.histogram(asdm))
print("Average: ", round(np.average(asdm), 2))
print("CoVariance: ", (np.cov(asdm)))
print("Correlation Coefficient: ", np.corrcoef(asdm))
"""


"""
gg = np.array(df["GameGenre"])

print(gg)

x = gg.tolist()

d = {}

for i in x:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)

"""


"""
loc = np.array(df["Location"])

#print(loc)

s = loc.tolist()

d = {}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)
"""



"""
gen = np.array(df["Gender"])
print(gen)

p = gen.tolist()

d = {}

for i in p:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

print(d)
"""

"""
age = np.array(df["Age"])

#print(age)

x = age.tolist()

d = {}
for i in x:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)

r = d.values()
s = d.keys()

print(r)
print(s)
"""

"""
gd = np.array(df["GameDifficulty"])

#print(gd)

s = gd.tolist()

#print(s)

d = {}

for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)
"""


"""
#Single Row
import pandas as pd

# Read CSV into DataFrame
df = pd.read_csv('online_gaming_behavior_dataset.csv')

# Select a single row by index (e.g., first row)
single_row = df.iloc[10]

# Access data in specific columns
#value_in_column = single_row[10]

print(single_row)  # Print the entire selected row
#print(value_in_column)  # Print specific value from the row
"""


ses = np.array(df["SessionsPerWeek"])

print(ses)

print("Median: ", np.median(ses))
print("Mean Value: ", np.mean(ses))
print("Histogram: ", np.histogram(ses))
print("95th Percentile: ", np.percentile(ses, 95))
print("Average: ", np.average(ses))
print("Quantile: ", np.quantile(ses, 1))
print("Standard Deviation: ", np.std(ses))
print("Variance: ", np.var(ses))
print("Covariance: ", np.cov(ses))
print("Correlation Coefficient: ", np.corrcoef(ses))













