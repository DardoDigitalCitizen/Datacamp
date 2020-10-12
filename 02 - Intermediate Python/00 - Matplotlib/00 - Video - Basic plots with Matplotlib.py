"""
BASIC PLOTS WITH MATPLOTLIB

- Visualization
- Data Structure
- Control Structures #Customize the flow of your scripts and algorithms.
- Case Study

DATA VISUALIZATION

- Very important in Data Analysis
    - Explore data
    - Report insights

* GapMinder, Wealth and Health of nations
"""

"""
MATPLOTLIB
"""
import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

plt.plot(year, pop) # Tells Python what to plot and how to plot it
plt.show() # Actually displays the plot. You might want to add titles and lables

"""
SCATTER PLOT
"""
import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

plt.scatter(year, pop) # Plots all the individual data points. Python doesn't draw a line through them.
plt.show()