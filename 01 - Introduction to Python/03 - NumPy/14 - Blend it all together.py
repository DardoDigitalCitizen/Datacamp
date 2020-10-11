"""
In the last few exercises you've learned everything there is to know about heights and weights of baseball players.
Now it's time to dive into another sport: soccer.

You've contacted FIFA for some data and they handed you two lists. The lists are the following:

positions = ['GK', 'M', 'A', 'D', ...]
heights = [191, 184, 185, 180, ...]

Each element in the lists corresponds to a player. The first list, positions, contains strings representing each
player's position. The possible positions are: 'GK' (goalkeeper), 'M' (midfield), 'A' (attack) and 'D' (defense).
The second list, heights, contains integers representing the height of the player in cm. The first player in the
lists is a goalkeeper and is pretty tall (191 cm).

You're fairly confident that the median height of goalkeepers is higher than that of other players on the soccer field.
 Some of your friends don't believe you, so you are determined to show them using the data you received from FIFA and
 your newly acquired Python skills.
"""
import numpy as np
import random2

positions = random2.sample((['GK', 'M', 'A', 'D'] * 1250), 5000) # Generates a random list
height = np.round(np.random.normal(1.65, 0.20, 5000), 2)

# Convert heights and positions, which are regular lists, to numpy arrays. Call them np_heights and np_positions.
np_positions = np.array(positions)
np_heights = np.array(height)

# Extract all the heights of the goalkeepers. You can use a little trick here: use np_positions == 'GK' as an index
# for np_heights. Assign the result to gk_heights
gk_heights = np_heights[np_positions == 'GK']
print(gk_heights)

# Extract all the heights of all the other players. This time use np_positions != 'GK' as an index for np_heights.
# Assign the result to other_heights.
other_heights = np_heights[np_positions != 'GK']
print(other_heights)

# Print out the median height of the goalkeepers using np.median(). Replace None with the correct code.
print(np.median(gk_heights))

# Do the same for the other players. Print out their median height. Replace None with the correct code.
print(np.median(other_heights))