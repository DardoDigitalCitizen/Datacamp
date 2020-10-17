"""
LIST
"""
pop = [30.55, 2.77, 39.21]
countries = ["afghanistan", "albania", "algeria"]

ind_alb = countries.index("albania")

print(ind_alb)
print(pop[ind_alb])

# Not convenient
# Not intuitive

"""
DICTIONARY
"""
world = {"afghanistan":30.55, "albania":2.77, "algeria":39.21} #key:value
print(world["albania"])