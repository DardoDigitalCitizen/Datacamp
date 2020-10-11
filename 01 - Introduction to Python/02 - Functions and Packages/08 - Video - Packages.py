"""
MOTIVATION

- Funcstions and methods are powerful
- All code in Python distribution?
    - Huge code base: messy
    - Lots of code you won't use
    - Maintenance problem
"""
"""
PACKAGES

- Directiory of Python Scripts
- Each script = module
- Specify functions, methods, types
- Thousands of packages available
    - Numpy: to efficiently work with arrays
    - Matplotlib: for data visualization
    - Scikit-learn: for machine learning
"""
"""
Install package

- http://pip.readthedocs.org/en/stable/installiing/
- Download get-pip.py
- Terminal: 
    - python3 get-pip.py
    - pip3 install numpy
"""
"""
IMPORT PACKAGE
"""
import numpy
#array([1, 2, 3]) = will result in a error

print(numpy.array([1, 2, 3]))

import numpy as np # You can import the package and refer to it with a different name
np.array([1, 2, 3])

from numpy import array # There are cases when you only need a function from a package. You have to explicit it.
array(([1, 2, 3]))

"""
from numpy import array

- my_script.py
"""
np_fam = array(fam_ext) # Using Numpy, but not very clear
np_fam = np.array(fam_ext) # Clearly using Numpy
