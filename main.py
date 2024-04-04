import numpy as np
import pandas as pd
df = pd.read_csv('data tenderncy.csv')

## create new data and remove NaN values
new_data = df.dropna()

print("Generate sample data:")
np.random.seed(0)
data = np.random.randint(0, 100, 100)

print("Percentiles: ")
percentiles = np.percentile(data, [25, 50, 75])
print("25th percentile:", percentiles[0])
print("50th percentile (median):", percentiles[1])
print("75th percentile:", percentiles[2])
# I wrote print for space
print("")

# my out will be 23.0 for 25th percentile
# 47.0 for 50th percentile
# 74.25 for 75th percentile

print("Standard deviation and variance we will look at in output:")
std_dev = np.std(data)
variance = np.var(data)
print("Standard deviation:", std_dev)
print("Variance:", variance)
# I wrote print for space
print("")

#we will be using correlation
data2 = np.random.randint(0, 100, 100)
correlation = np.corrcoef(data, data2)[0, 1]
print("Correlation between two datasets:", correlation)

#In those code we are trying to fix numbers it is all about wrong data
#I used ("at") methot as ("loc")
new_data.at[0, 'Phone 1'] = '+561 23-4567-890'
new_data.at[1, 'Phone 1'] = '+253 11 22 3333'
new_data.at[2, 'Phone 1'] = '+253 11 22 3333'
new_data.at[3, 'Phone 1'] = '+561 23-4567-890'
new_data.at[4, 'Phone 1'] = '+253 11 22 3333'
new_data.at[5, 'Phone 1'] = '+253 11 22 3333'
new_data.at[6, 'Phone 1'] = '+561 23-4567-890'
new_data.at[7, 'Phone 1'] = '+253 11 22 3333'
new_data.at[8, 'Phone 1'] = '+253 11 22 3333'
new_data.at[9, 'Phone 1'] = '+561 23-4567-890'
new_data.at[10, 'Phone 1'] = '+253 11 22 3333'
new_data.at[11, 'Phone 1'] = '+253 11 22 3333'


#in this code ewe
data_matrix = np.random.rand(5, 5)
correlation_matrix = np.corrcoef(data_matrix)
print("Correlation matrix:")
print(correlation_matrix)

data3 = np.random.randint(0, 100, 100)
data4 = np.random.randint(0, 100, 100)
correlation2 = np.corrcoef(data3, data4)[0, 1]
print("Correlation between two unrelated datasets:", correlation2)



print("here we find no true values:")
print(new_data.duplicated())



print(new_data.to_string())