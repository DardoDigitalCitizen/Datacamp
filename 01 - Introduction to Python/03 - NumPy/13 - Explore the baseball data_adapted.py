"""
It's again available as a 2D Numpy array np_baseball, with three columns.

The Python script in the editor already includes code to print out informative messages with the different summary
statistics. Can you finish the job?

"""

import numpy as np

height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)
age = np.round(np.random.normal(20, 5, 5000), 0)

np_baseball = np.column_stack((height, weight, age))

# The code to print out the mean height is already included. Complete the code for the median height.
# Replace None with the correct code.
avg = np.mean(np_baseball[:, 0])
print("Average: " + str(avg))
med = np.median(np_baseball[:, 0])
print(" Median: " + str(med))

# Use np.std() on the first column of np_baseball to calculate stddev. Replace None with the correct code.
std = np.std(np_baseball[:, 0])
print(" Standard Deviation: " + str(std))

# Do big players tend to be heavier? Use np.corrcoef() to store the correlation between the first and second column
# of np_baseball in corr. Replace None with the correct code.
corr = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])
print("Correlation: " + str(corr))