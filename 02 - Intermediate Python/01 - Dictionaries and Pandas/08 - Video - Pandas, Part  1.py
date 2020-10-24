"""
TABULAR DATASET EXAMPLES
"like spreadsheets!"

row =  observations
column = variable
"""
from PIL import Image
tabularDS = Image.open("tabularDS_examples.JPG")
# tabularDS.show()
# Unlock if you want to display examples of Tabular Datasets

"""
DATASETS IN PYTHON

 - 2D Numpy array?
    -> One data type
    
"""
Datasets_inPy = Image.open(("DS_inPy.JPG"))
# Datasets_inPy.show()
# Unlock if you want to display examples of Tabular Datasets with different types of data

"""
 - PANDAS!
    -> Different types
    -> High level data manipulation tool
    -> Created by Wes McKinney
    -> Built on Numpy
    -> DataFrame
    
"""
dict = {
    "country":["Brazil", "Russia", "India", "China", "South Africa"],
    "capital":["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area":[8.516, 17.10, 3.286, 9.597, 1.221],
    "population":[200.4, 143.5, 1252, 1357, 52.98] }
# KEYS (column labels)
# VALUES (data, column by columns)

import pandas as pd
brics = pd.DataFrame(dict)
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

"""
DATAFRAME FROM CSV file

    -> CSV = comma-separated values
"""

brics_csv = pd.read_csv(r'brics.csv', index_col=0) # Tell the function that the first columns contains the row indexes.
print(brics_csv)

