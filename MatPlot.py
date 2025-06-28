#MatPlot...


#It is a poweful plotting library commonly used for static animated or interactive visualization 

import matplotlib.pyplot as plt 
import numpy as np
 
# y = [22,33,66,11,77]

# plt.plot(x,y)
# plt.title("Basic Line Plot")
# plt.xlabel("x-axis")
# plt.xlabel("y-axis")
# plt.grid(True)
# plt.plot(x, y, color='red', marker='o', linestyle='-', linewidth=2)

# y1 = [1, 2, 3, 4, 7]
# y2 = [23, 55, 66, 77, 46]

# plt.plot(x, y1, label="Ascending")
# plt.plot(x, y1, label="descending")
# plt.legend()

#Bar Graph

# categories = ['A', 'B', 'C', 'D']
# values = [10,24,33,66]
# plt.barh(categories, values, color="red")
# plt.bar(categories, values, color="red")


#Scatter Plotting

# x = [2,3,4,5,6,7,8,9]
# y = [11,22,33,44,55,66,77,88]
# plt.scatter(x, y, color="purple")
# plt.title("Scatter Plot Example")
# plt.xlabel("X values")
# plt.ylabel("Y values")



#Histogram...
# data = np.random.randn(1000)
# plt.hist(data, bins=30, color="purple", edgecolor='black')
# plt.title("Histogram of Random Data")
# plt.xlabel("Values")
# plt.ylabel("Frequency")
# plt.show()


#Histogram...
# sizes = [30,35,55,20]
# labels = ['Python', 'Java', 'C++', 'JavaScript']
# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
# plt.title("Programming Language Usage")
# plt.axis('equal')
# plt.show()

#SubPlot...
# x= [2,3,4,5,6,7,8,9]
# y = [11,22,33,44,55,66,77,88]

# plt.subplot(1,2,1)
# plt.plot(x, y)
# plt.subplot(1,2,2)
# plt.plot(x, y)
# plt.tight_layout()
# plt.savefig("plot.png", dpi=300)
# plt.show()



#