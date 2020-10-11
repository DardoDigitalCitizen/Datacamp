"""
LISTS RECAP

- Powerful
- Collection of values
- Hold different types
- Change, add, remove
- Need for Data Science
    - Mathematical operations over collections
    - Speed
"""
"""
ILUSTRATION
"""

height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

# BMI = weight / height ** 2 # TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'

"""
Solution: Numpy

- Numeric Python
- Alternative to Python List: Numpy Array
    - Calcations over entire arrays
    - Easy and Fast
    - Installation
        - in the terminal: pip3 install numpy
"""

"""
NUMPY
"""

import numpy as np

np_height = np.array(height)
print(np_height)

np_weight = np.array(weight)
print(np_weight)

bmi = np_weight / np_height ** 2 # Now it WORKS!
print(bmi)

"""
Numpy: remarks
"""
np.array([1.0, "is", True])
"""
1) Numpy arrays: contain only one type.
If you try to create and array with different types, the resulting Numpy array will contain a single type.
String in this case

2)Numpy arrays: new kind of python type
A Numpy Arrawy is simply a new kind of python type, like float, list or strings. This means it comes with its 
own methods, which can behave differently than you'd expect
"""
python_list = [ 1, 2, 3]
numpy_array = np.array([1, 2, 3])

sum_list = python_list + python_list
print(sum_list)

sum_numpy_array = numpy_array + numpy_array
print(sum_numpy_array)
# DIFFERENT TYPES: DIFFERENT BEHAVIOR!

"""
NUMPY SUBSETTING
"""
print(bmi)

print(bmi[1])

print(bmi > 23) # False: Below 23, True: Above 23

print(bmi[bmi > 23]) # All the elements above 23