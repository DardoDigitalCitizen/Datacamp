"""
BIULT-IN FUNCTIONS

- Maximum of list: max()
- Length of list or string: len()
- Get index in list: ?
- Reversing a list: ?
"""
"""
BACK 2 BASICS
"""

sister = "liz" # Object, type: str, examples of methods: capitalize() replace()

height = 1.73 # Object, type: float, examples of methods: bit_length() conjugate()

fam = ["liz", 1.73, "emma", 1.68,
       "mom", 1.71, "dad", 1.89] # Object, type: list, examples of methods: index() count()

"""
METHODS: Functions that belongs to objects.
"""

"""
list METHODS
"""
fam_index = fam.index("mom") # The index() method returns the index of the specified element in the list.
print(fam_index)

fam_count = fam.count(1.73) # The count() method returns the number of elements with the specified value.
print(fam_count)

"""
str METHODS
"""
print(sister)

sister_cap = sister.capitalize() # The capitalize() method returns a string where the first character is upper case.
print(sister_cap)

sister_replace = sister.replace("z", "sa") # The replace() method replaces a specified phrase with another specified phrase.
print(sister_replace)

"""
METHODS

- Everything = object
- Object have methods associated, depending on type
"""

#fam_replace = fam.replace("mom", "mommy")
# ERROR: 'list' object has no attribute 'replace'

sister_index = sister.index("z")
print(sister_index)

fam_index = fam.index("mom")
print(fam_index)

"""
METHODS (2)
"""

fam.append("me")
print(fam)

fam.append(1.79)
print(fam)


"""
SUMMARY

Functions
- type(fam) -> list

Methods: call functions on objects
- fam.index("dad")
"""