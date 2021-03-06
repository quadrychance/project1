from pylab import genfromtxt
from numpy import flipud
import re
import numpy as np
import matplotlib.pyplot as pyplot
import matplotlib.lines as mlines
import matplotlib.cm as cm
import matplotlib.pylab as pylab
params = {'legend.fontsize': 'x-large',
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

from math import pi
import matplotlib.lines as mlines
big_line = 28
big_CO2 = 32
big_NH3 = 28
treeoutput = open("treeoutput.txt", "r")
big = genfromtxt("waterbig2.txt")

exit

big_mass = big[:,4]
big_frac = (big_mass[:]*.1)
CO2_frac_big = (big_mass[:]*.029)
NH3_frac_big = (big_mass[:]*.05)
CO2_frac_big[0:big_CO2] = 0
NH3_frac_big[0:big_NH3] = 0
big_frac[0:big_line] = 0

small_line = 280
small_CO2 = 312
small_NH3 = 284
small = genfromtxt("watersmall2.txt")
small_mass = small[:,4]
small_frac = (small_mass[:]*.1)
CO2_frac_small = (small_mass[:]*.029)
NH3_frac_small = (small_mass[:]*.05)

small_frac[0:small_line] = 0
CO2_frac_small[0:small_CO2] = 0
NH3_frac_small[0:small_NH3] = 0
#print(treeoutput)
#print(small_frac)
print(np.shape(big_mass))
print(np.shape(big_CO2))
stack = np.vstack((big_mass,big_frac, CO2_frac_big, NH3_frac_big))
stack2 = np.vstack((small_mass, small_frac, CO2_frac_small, NH3_frac_small))
stacked = np.hstack((stack, stack2))
#print(stacked.T)

#print(mat3[21])
with open('treeoutput.txt', 'r') as data:
    output_data = []
    for dd in data.readlines():
        #print()
        dd = dd.strip()
       # print(dd)
        dd = dd.strip('[]')
        #print("'{}'".format(dd))
        numbers = dd.split(',')
       # print(numbers)
        numbers = [int(nn.strip()) for nn in numbers]
       # print(numbers, type(numbers), type(numbers[0]))
        output_data.append(numbers)
#print(output_data)
mass_tot = []
water_mass = []
CO2_mass = []
NH3_mass = []
CO2_frac = []
NH3_frac = []
mass_frac = []
for i in range (len(output_data)):
    this_planet = output_data[i]
    temp_mass = 0
    temp_water = 0
    temp_CO2 = 0
    temp_NH3 = 0
    for n in range(len(this_planet)):
        temp_mass = stacked[0,n] + temp_mass
        temp_water = stacked[1,n]+ temp_water
        temp_CO2 = stacked[2,n]+ temp_CO2
        temp_NH3 = stacked[3,n]+ temp_NH3
    mass_tot.append(temp_mass)
    mass_frac.append(temp_water/temp_mass)
    CO2_frac.append(temp_CO2/temp_mass)
    NH3_frac.append(temp_NH3/temp_mass)
    print(this_planet)
    print(temp_mass)
    print(temp_water)
    print(temp_water/temp_mass)
    print()

    water_mass.append(temp_water)
    CO2_mass.append(temp_CO2)
    NH3_mass.append(temp_NH3)
print(mass_tot)
print(water_mass)
print(CO2_mass)
print(NH3_mass)
water=[]
CO2=[]
NH3=[]
for u in range(len(CO2_mass)):
    CO2_m= CO2_mass[u]
    m_t = mass_tot[u]
    CO2.append(CO2_m/m_t)
print(CO2)
for l in range(len(water_mass)):
    w_m= water_mass[l]
    m_t = mass_tot[l]
    water.append(w_m/m_t)
print(water)
for t in range(len(NH3_mass)):
    NH3_m= NH3_mass[t]
    m_t = mass_tot[t]
    NH3.append(NH3_m/m_t)
print(NH3)

fracout= open('fracoutput.txt', 'w')# as file_handler:
fracout.write("{}\n".format(water))
fracout.write("{}\n".format(CO2))
fracout.write("{}\n".format(NH3))
fracout.close()




allparams = genfromtxt('allparams.txt')

allparams1 = allparams.T

#small_params = genfromtxt('smallparams.txt')
#print(np.shape(stacked))
#print(np.shape(allparams1))
mat = np.vstack((allparams1, stacked))


#print(mat.shape)
#print(mat)







#print(mat0)


pyplot.scatter(mat[0,:], mat[9,:]/0.000003003, c= 'cyan', s=(mat[10,:]/0.000003003)*6000, edgecolor = 'k')
pyplot.scatter(mat[0,:], mat[9,:]/0.000003003, c= 'k', s=(mat[9,:]/0.000003003)*200, edgecolor='none' )

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
pyplot.xlim([.01,1.5])
#pyplot.xscale('log')
pyplot.yscale('log')
pyplot.legend();
pyplot.show();

elements = genfromtxt("element.out")
arr2=np.asarray(water)
print(len(arr2))
print(len(elements[0:4,4]))
print((len(arr2)))
arr5 = np.linspace(0,1,15)

arr3=np.zeros(4)
#arr4=np.vstack((arr2,arr3))
#colors, rescale = matplotlib.cm.get_cmap('Spectral'), matplotlib.colors.Normalize(vmin=0, vmax=.2)

pyplot.axvline(x=0.45, ymin=0, ymax = 15, linewidth=2, color='g')
pyplot.axvline(x=0.20, ymin=0, ymax = 15, linewidth=2, color='g')
pyplot.scatter(elements[0:len(arr2),1], elements[0:len(water),2], s=elements[0:len(arr2),4]/0.000003003*100, c=arr2[:]*100, cmap='YlGnBu', vmin=0, vmax=10)

pyplot.xlabel("Semi-Major Axis", fontsize = 16)
pyplot.ylabel("e", fontsize = 16)
pyplot.ylim([0,.5])
pyplot.colorbar().set_label('Fractional Water Mass (%)')
pyplot.xlim([.01,5])
pyplot.xscale('log')
#pyplot.yscale('log')
pyplot.legend();
pyplot.show();
