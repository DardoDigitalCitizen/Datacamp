"""SUBSETTING LISTS"""

fam = ["Liz", 1.73, "Emma", 1.68, "mom", 1.71, "dad", 1.89]

print(fam)

print(fam[3])
print(fam[6])
print(fam[-1]) # <-
print(fam[7]) # <-

"""LIST SLICING"""
print(fam)

print(fam[3:5])
print(fam[1:4])

"""[ START(inclusive) : END(exclusive) ]"""

print(fam[:4])
print(fam[5:])
