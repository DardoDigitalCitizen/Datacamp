"""Finally, you can also remove elements from your list. You can do this with the del statement:"""
x = ["a", "b", "c", "d"]
del(x[1])

""" PAY ATTENTION HERE: as soon as you remove an element from a list, the indexes of the elements that come after 
the deleted element all change!"""

"""The updated and extended version of areas that you've built in the previous exercises is coded below."""
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# There was a mistake! The amount you won with the lottery is not that big after all and it looks like the poolhouse
# isn't going to happen. You decide to remove the corresponding string and float from the areas list.

del(areas[-4:-2])
#You could use to del(areas[-4]);del(areas[-3]). The ; sign is used to place commands on the same line.

print(areas)