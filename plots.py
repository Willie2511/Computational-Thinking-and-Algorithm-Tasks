# IPython log file
# Willie Byrne
# This program displays a plot of the functions
# f(x)=x, g(x)=x**2 and h(x)=x**3
# On the one set of axes

import numpy as np
import matplotlib.pyplot as plt
# First task was to import matplotlib.pyplot and numpy

x = np.linspace(0, 4, 100)
#Decided to space the range 0-4 out using 100 numbers
# This made it easier when graphing the data 
g = x**2
h = x**3

plt.plot(x, g, 'g', label="squared")
#First i am plotting and labelling g
plt.plot(x, h, 'r', label="cubed")
# Then I plot and label h
# I used different colors so they were distinguishable on a graph
plt.legend()
plt.title("Weekly Task 8")
plt.xlabel('X')
plt.ylabel('Y')
# Finally I added a title, a legend and labels to complete the graph
plt.show()

