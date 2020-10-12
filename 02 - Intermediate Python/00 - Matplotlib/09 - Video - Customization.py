"""
DATA VISUALIZATION

- Many options
    - Different plot types
    - Many customizations: change colors, shapes, labels, axe, and so on.

- Choice depends on
    - Data
    - Story you want to tell with this data
"""

"""
BASIC PLOT
example
"""
import matplotlib.pyplot as plt

# BEFORE
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

# AFTER -> Added more data
year = [1800, 1850, 1900] + year # Fifth = Adding more data points.
pop = [1.0, 1.262, 1.650] + pop

plt.plot(year, pop)

plt.xlabel('Year') # First = Labels
plt.ylabel('Population')
plt.title('World Population Projections') # Second = Title
plt.yticks([0, 2, 4, 6, 8, 10],# Third = Started from Zero to Ten, with intervals of Two
           ['0', '2B', '4B', '6B', '8B', '10B'])# Fourth =  Giving names to the sticks. B = Billions

plt.show()