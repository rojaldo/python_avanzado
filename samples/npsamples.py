import numpy as np

data = np.genfromtxt('data/titanic.csv', delimiter=',', skip_header=1)

# print column 5
ages = data[:, 6]

# remove NaN values
ages = ages[~np.isnan(ages)]

# get mean and median
mean_age = np.mean(ages)
median_age = np.median(ages)

print(f'Mean age: {mean_age}')
print(f'Median age: {median_age}')


