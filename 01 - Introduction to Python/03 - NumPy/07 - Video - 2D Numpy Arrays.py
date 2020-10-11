"""
TYPE OF NUMPY ARRAYS
"""
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

print(type(np_height))
print(type(np_weight))

"""
2D NUMPY ARRAYS
"""
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]]) # if you change one float to str, all the elements become str
print(np_2d)

print(np_2d.shape) # (2, 5) # 2 rows, 5 columns

"""
SUBSETTING
"""
print(np_2d[0]) # select the first row

print(np_2d[0][2]) # select the row then the columm
print(np_2d[0, 2]) # does the same

print(np_2d[:, 1:3]) # select the height and weight of the second and thir family member.
# you want both rows so you put the sign :
# you want the second and third collum, so you put 1:3

print(np_2d[1,:]) # select only the weights.
# you want only the second row, so you put 1
# you want all the columms soo you put :