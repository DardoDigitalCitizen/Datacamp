"""
RECAP
"""

world = {"afghanistan":30.55, "albania":2.77, "algeria":39.21}
print(world["albania"])

world = {"afghanistan":30.55, "albania":2.77,
"algeria":39.21, "albania":2.81} # The last pair that you specified was kept in the resulting dictionary
print(world)

"""
KEYS HAVE TO BE "IMMUTABLE" OBJECTS
"""
mixed = {0:"hello", True:"dear", "two":"world"} # Has all immutable objects as keys, is valid
print(mixed)
#test = {["just", "to", "test"]: "value"}  #ERROR: Uses a list as a key, is not valid.
#print(test)

"""
DICTIONARY
"""
world["sealand"] = 0.000027
print(world)

print("sealand" in world)

world["sealand"] = 0.000028
print(world)

del(world["sealand"])
print(world)

"""
LIST VS DICTIONARY

LIST = Select, update and remove: [], Indexed by range of numbers, 
When to choose? When collection of values order matters and you want to select entire subsets.

DICTIONARY = Select, update and remove: [], Indexed by unique keys, 
When to choose? When you need a  lookup table, where looking for data should be fast and 
you can specify with unique keys.
"""

