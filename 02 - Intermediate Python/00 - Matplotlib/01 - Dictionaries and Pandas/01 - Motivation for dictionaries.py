"""
To see why dictionaries are useful, have a look at the two lists defined below*. countries contains the names
of some European countries. capitals lists the corresponding names of their capital.
"""
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Use the index() method on countries to find the index of 'germany'. Store this index as ind_ger.
ind_ger = countries.index('germany')

# Use ind_ger to access the capital of Germany from the capitals list. Print it out.
print(capitals[ind_ger])