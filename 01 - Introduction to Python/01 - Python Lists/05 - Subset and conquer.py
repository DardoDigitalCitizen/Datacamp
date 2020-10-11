"""Subsetting Python lists is a piece of cake. Take the code sample below, which creates a list x and then selects "b"
from it. Remember that this is the second element, so it has index 1. You can also use negative indexing."""

x = ["a", "b", "c", "d"]
print(x[1])
print(x[-3]) # same result!

"""Remember the areas list from before, containing both strings and floats? Its definition is already in the script. 
Can you add the correct code to do some Python subsetting?"""

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out the second element from the areas list (it has the value 11.25).
print(areas[1])

# Subset and print out the last element of areas, being 9.50. Using a negative index makes sense here!
print(areas[-1])

# Select the number representing the area of the living room (20.0) and print it out.
print(areas[-5])