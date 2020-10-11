"""
There are several ways to import packages and modules into Python. Depending on the import call, you'll have to use
different Python code.

Suppose you want to use the function inv(), which is in the linalg subpackage of the scipy package. You want to be able
to use this function as follows:

my_inv([[1,2], [3,4]])
"""
# Which import statement will you need in order to run the above code without an error?
# ANSWER: from scipy.linalg import inv

"""
My Test
"""
import numpy as np
import scipy


my_inv = np.array([[1,2], [3,4]])
my_inverse_inv = scipy.linalg.inv(my_inv) #function to calculate the inverse of a matrix.
# The inverse of a matrix is such that if it is multiplied by the original matrix, it results in identity matrix.

print(my_inv)
print(my_inverse_inv)
# SciPy has optimized and added functions that are frequently used in NumPy and Data Science.
