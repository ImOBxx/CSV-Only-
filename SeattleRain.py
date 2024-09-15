import pandas as pd
import numpy as np

df = pd.read_csv('Seattle2014.csv')['PRCP'].values
inches = df / 254

print()
print("Number days without rain: ", np.sum(inches == 0)) 
print("Number days with rain: ", np.sum(inches != 0)) 
print("Days with more than 0.5 inches:", np.sum(inches > 0.5)) 
print("Rainy days with < 0.1 inches :", np.sum((inches > 0) & (inches < 0.2)))
print()

rainy = (inches > 0)

print()
summer = (np.arange(365) - 172 < 90) & (np.arange(365) - 172 > 0)
print("Median precip on rainy days in 2014 (inches): ", np.median(inches[rainy]))
print("Median precip on summer days in 2014 (inches): ", np.median(inches[summer]))
print("Maximum precip on summer days in 2014 (inches): ", np.max(inches[summer]))
print("Median precip on non-summer rainy days (inches):", np.median(inches[rainy & ~summer]))
print()