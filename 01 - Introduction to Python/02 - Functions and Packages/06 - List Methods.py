"""
Strings are not the only Python types that have methods associated with them. Lists, floats, integers and booleans
are also types that come packaged with a bunch of useful methods. In this exercise, you'll be experimenting with:

- index(), to get the index of the first element of a list that matches its input
- count(), to get the number of times an element appears in a list.

You'll be working on the list with the area of different parts of a house: areas.
"""

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use the index() method to get the index of the element in areas that is equal to 20.0. Print out this index.
print(areas.index(20.0))

# Call count() on areas to find out how many times 9.50 appears in the list. Again, simply print out this number.
print(areas.count(9.50))