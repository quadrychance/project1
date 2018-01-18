from matplotlib import pyplot;
from pylab import genfromtxt;
import numpy as np
from math import pi
#array1 = np.asarray("1_4.out")
mat0 = genfromtxt("population.txt");

fig1, ax = pyplot.subplots()

mat0 = ax.scatter(mat0[:,4]/0.000003003, mat0[:,6] ,c= 'k', s = 50*(mat0[:,4]/0.000003003))

ax.set_xlabel("m")
ax.set_ylabel("o")
ax.set_xlim([.05,20])
ax.set_ylim([0,180])
ax.set_title("Planet Population")
colors = ['k']
ax.set_xscale('log')



axes = pyplot.gca()

pyplot.legend();
pyplot.show();
