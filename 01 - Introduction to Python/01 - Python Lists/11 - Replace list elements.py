"""Replacing list elements is pretty easy. Simply subset the list and assign new values to the subset.
You can select single elements or you can change entire list slices at once.
Example: """

x = ["a", "b", "c", "d"]
x[1] = "r"
print(x)
# ['a', 'r', 'c', 'd']
x[2:] = ["s", "t"]
print(x)
# ['a', 'r', 's', 't']

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Update the area of the bathroom area to be 10.50 square meters instead of 9.50.
areas[-1] = 10.50

# Make the areas list more trendy! Change "living room" to "chill zone".
areas[4] = "chill zone"

print(areas)