#
# drawing in Python
#

# Drawing is used to add visualization to reports.
# Used extensively in universities and B2B communication.

# Drawing relies on three modules:
# matplotlib that has drawing algorithms
# numpy that handles setting data to arrays
# pandas that has more advanced math algorithms

# This module teaches matplotlib.

# We need following two modules
import matplotlib.pyplot as plt
import numpy as np

# When drawing data, everything must have two axis.
# X ja Y -axis are essentially datapoints (X,Y).
# numpy handles well arrays of datapoints.

# Here we have two arrays of 3 points.
xpoints = np.array([11, 20, 30])
ypoints = np.array([0, 25, 100])

# you can also make any list into numpy array.
# Here we have 9 points long list.
muuttujajonoX = [14,16,22,28,31,39,44,46,58]
x2points = np.array(muuttujajonoX)
y2points = np.array([55,52,57,54,58,55,58,52,54])

"""
# Next step is plotting.
# you must think how may plots you need in a picture.
# subplots are used to set separate plot in picture
# while plot is used to draw one picture.

# this example sets one picture
plt.title("Yksinkertainen kuva")
plt.xlabel("X-tason kuvaus")
plt.ylabel("Y-tason kuvaus")

# usually you need arrays to x and y axis
# And info on how picture is shown
# this depends on type of picture,
# this is a plot, aka line
plt.plot(xpoints, ypoints, 
         color='blue', 
         marker='*', 
         linestyle='dashed',
        linewidth=2, markersize=12)

# If we draw another plot, the one picture will
# have two plots
plt.plot(x2points, y2points, 
         color='green', 
         marker='.', 
         linestyle='solid',
        linewidth=1, markersize=6)


# Finally you need to draw actual plot
plt.show()
"""

# Second way of drawing is to have picture that holds
# multiple plots. Then picture will have to set subplot.
# subplot has 
# subplot(<number of rows>,<number of columns,<index of current plot>)
# Here we have two rows and two columns or 4 possible indexes
# Remember: index starts at 1 and goes left to right, row by row

# this subpolot is upper left
plt.subplot(2,2,1)

# within each subplot the plot is drawn as usual
plt.title("Duo Otsanappi")
plt.xlabel("X-akselin label")
plt.ylabel("Y-akselin label")

plt.plot(x2points, y2points, color='red', marker='+', linestyle='solid',
     linewidth=2, markersize=12)

# this subplot is upper right
plt.subplot(2,2,2)


Xdata = [1,2,3,4,5]
Xarvo = np.array(Xdata)
Ydata = [3,6,4,7,9]
Yarvo = np.array(Ydata)

#plt.title("Piirakka",loc='left')
#plt.pie(Yarvo,[0,0,1,0,1],labels=['','','talo','','auto'])

plt.title("jakauma")
plt.boxplot([Xarvo,Yarvo])

# this subplot is lower left
plt.subplot(2,2,3)

plt.scatter(x2points, y2points)

# this subplot is lower right
plt.subplot(2,2,4)

# bar chart has titles for bars
x = np.array(["A", "B", "C", "D"])
# y-axis shows values of bars
y = np.array([3, 8, 1, 10])
# colowing allows differing chart colors
varitys = np.array(["red","green","red","red"])

# bar shows bars rising vertically while 
# barh shows them going horizontally
#plt.bar(x,y,color=varitys)
plt.barh(x,y,color=varitys)


# finally we need to show actual window with 4 plots
plt.show()

# Note: the plot is automagically scaled.
# you can also set plot logarithmic. See:
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html
# https://stackoverflow.com/questions/773814/plot-logarithmic-axes
