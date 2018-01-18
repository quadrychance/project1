from matplotlib import pyplot
import matplotlib.lines as mlines
from pylab import genfromtxt
from math import pi
import numpy as np
import matplotlib.lines as mlines
#mat0 = genfromtxt("mod.out");


treeoutput = open("treeoutput", "r")
mat0 = genfromtxt("water2.txt")
mat1 = mat0[:,4]
mat2 = (mat1[:]*.1)
mat2[0:40] = 0
mat3 = genfromtxt('params.txt')
print(treeoutput)
print(mat2)
print(np.shape(mat1))
print(np.shape(mat2))
mat4 = np.column_stack((mat1,mat2,mat3))
print(mat4)




#print(mat0)


pyplot.scatter(mat4[:,2], mat4[:,0]/0.000003003 ,c= 'cyan',s=(mat4[:,1]/0.000003003)*3500, edgecolor = 'k' )

pyplot.scatter(mat4[:,2], mat4[:,0]/0.000003003 ,c= 'k',s=(mat4[:,0]/0.000003003)*200, edgecolor='none' )


blue_dot = mlines.Line2D([],[], color='cyan', marker='o',
                          markersize=15, label='Water')

black_dot = mlines.Line2D([],[], color='black', marker='o',
                          markersize=15, label='Rock')
pyplot.legend(handles=[blue_dot, black_dot])
pyplot.xlabel("semi-major axis (AU)", fontsize = 16)
pyplot.ylabel("mass ($M_{\oplus}$)", fontsize = 16)
pyplot.title("Initial Embryo Distribution and Water Mass Fractions")
axes = pyplot.gca()
pyplot.ylim([.001,5])
pyplot.xlim([.01,1])
#pyplot.xscale('log')
#pyplot.yscale('log')
pyplot.legend();
pyplot.show();
