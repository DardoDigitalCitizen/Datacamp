"""LIST MANIPULATION
- Change list elements
- Add list elements
- Remove list elements"""

""" CHANGING LIST ELEMENTS"""

fam = ["Liz", 1.73, "Emma", 1.68, "mom", 1.71, "dad", 1.89]
print(fam)
# ['Liz', 1.73, 'Emma', 1.68, 'mom', 1.71, 'dad', 1.89]

fam[7] = 1.86
print(fam)
# ['Liz', 1.73, 'Emma', 1.68, 'mom', 1.71, 'dad', ---1.86---]

fam[0:2] = ["Lisa", 1.74]
print(fam)
# [---'Lisa', 1.74---, 'Emma', 1.68, 'mom', 1.71, 'dad', 1.86]

"""ADDING AND REMOVING ELEMENTS"""

fam_ext = fam + ["Me", 1,79]
print(fam_ext)
# ['Lisa', 1.74, 'Emma', 1.68, 'mom', 1.71, 'dad', 1.86, ---'Me', 1, 79---]

del(fam[2])
print(fam)
# ['Lisa', 1.74, ------- 1.68, 'mom', 1.71, 'dad', 1.86]

"""BEHIND THE SCENES (1)"""

x = ["a", "b", "c"]

# Select the same value
y = x

y[1] = "z"
print(y)
# ['a', 'z', 'c']
print(x)
# ['a', 'z', 'c']

"""BEHIND THE SCENES (2)"""

x = ["a", "b", "c"]

# Only select the elements
y = list(x)
y = x[:]

y[1] = "z"
print(x)
# ['a', 'b', 'c']

print(y)
# ['a', 'z', 'c']