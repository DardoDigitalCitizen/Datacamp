"""
DATA ANALYSIS

- Get to know your data
- Little data -> simply look at it
- Big data ->?
"""

import numpy as np

"""
np_city = np.array([[1.64, 71.78],
                    [1.37, 63.35],
                    [1.6, 55.09],
                    [2.04, 74.85],
                    [2.04, 68.72],
                    [2.01, 73.57]])
"""
height = np.round(np.random.normal(2.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)
# Use the random.normal() method to get a Normal Data Distribution.
# It has three parameters:
#
# loc - (Mean) where the peak of the bell exists.
#
# scale - (Standard Deviation) how flat the graph distribution should be.
#
# size - The shape of the returned array.


np_city = np.column_stack((height, weight))
# numpy.column_stack(tup): Stack 1-D arrays as columns into a 2-D array.

"""
NUMPY
"""
print(np_city.shape)

print(np.mean(np_city[:, 0])) # add up all the numbers and then divide by the number of numbers

print(np.median(np_city[:, 0])) # order the set from lowest to highest and find the exact middle

print(np.corrcoef(np_city[:, 0 ], np_city[:, 1]))

print(np.std(np_city[:, 0]))
"""
- sum(), sort()...
Numpy also features more basics functions, such as sort(), sum(), which also exist in the basic Py distribution.

- Enforce single data type: SPEED!
Because Numpy enforces a single data type in an array, it can drasticall speed up the calculations
"""

"""
GENERATE DATA: Simulate it with Numpy Functions!

- Arguments for np.random.normal()
    - distribution mean
    - distribution standard deviantion
    - number of samples
"""
# I sampled two random distributions 5000 times to create the height and weight arrays, and the used
# collum_stack to paste them together as two columns.
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)

np_city = np.column_stack((height, weight))