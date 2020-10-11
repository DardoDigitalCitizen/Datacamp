"""You saw before that a Python list can contain practically anything; even other lists!
To subset lists of lists, you can use the same technique as before: square brackets.
Try out the commands in the following code sample in the IPython Shell:"""

x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
print(x[2][0])
print(x[2][:2])
# x[2] results in a list, that you can subset again by adding additional square brackets.

#What will house[-1][1] return?

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

print(house[-1][1])