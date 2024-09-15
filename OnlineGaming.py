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








