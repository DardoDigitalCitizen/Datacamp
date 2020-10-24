"""
CSV TO DATA FRAME (1)
Putting data in a dictionary and then building a DataFrame works, but it's not very efficient. What if you're dealing
with millions of observations? In those cases, the data is typically available as files with a regular structure. One
of those file types is the CSV file, which is short for "comma-separated values".

To import CSV data into Python as a Pandas DataFrame you can use read_csv().

Let's explore this function with the same cars data from the previous exercises. This time, however, the data is
available in a CSV file, named cars.csv.

CSV TO DATA FRAME (2)

Your read_csv() call to import the CSV data didn't generate an error, but the output is not entirely what we wanted.
The row labels were imported as another column without a name.

Remember index_col, an argument of read_csv(), that you can use to specify which column in the CSV file should be used
as a row label? Well, that's exactly what you need here!



"""
# To import CSV files you still need the pandas package: import it as pd.
import pandas as pd

# Use pd.read_csv() to import cars.csv data as a DataFrame. Store this dataframe as cars.
# Specify the index_col argument inside pd.read_csv(): set it to 0, so that the first column is used as row labels.
cars = pd.read_csv(r'cars.csv', index_col=0)
print(cars)