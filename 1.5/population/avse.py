from matplotlib import pyplot;
from pylab import genfromtxt;
import numpy as np
from math import pi
#array1 = np.asarray("1_4.out")
mat0 = genfromtxt("population.txt");

fig1, ax = pyplot.subplots()

mat0 = ax.scatter(mat0[:,1], mat0[:,2] ,c= 'k', s = 50*(mat0[:,4]/0.000003003))

ax.set_xlabel("log semi-major axis (AU)")
ax.set_ylabel("e")
ax.set_xlim([.05,2])
ax.set_ylim([0,1])
ax.set_title("Planet Population")
colors = ['k']
ax.set_xscale('log')



axes = pyplot.gca()

pyplot.legend();
pyplot.show();
