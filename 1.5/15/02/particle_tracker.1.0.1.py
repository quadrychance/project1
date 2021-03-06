# tree is going to be a dictionary, with the key being the merged particle
# and the value being a list containing all previous contributors
#
# so when done, tree[n] is the list of all particles which got absorbed into particle n
#
from pylab import genfromtxt
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
#tree_input = ("HM_term.out")
#sy_in = ("HM_follow_all.out")
#pl_left = ("HM_pl.out")

def flatten(a):
    result = []

    for item in a:
        if type(item)==int:
            result += [item]
        else:
            result += flatten(item)

    return result

# assumes that all input is either an int or a flattened list
def head(a):
    if type(a)==int:
        return a

    else:
        return a[0]

# tree is {int: list}
tree = {}
disappeared = []

filename = 'tree2.txt'
with open(filename,'r') as infile:
    iii=0
    for event in infile:
        words = event.split()

        first = int(words[0])
        second = int(words[4])
        dest = int(words[0])

        # make it so first particle is always the destination; the other is the one whose
        # mass is assigned to another
        if first == dest:
            pass
        elif second == dest:
            tmp = first
            first = second
            second = tmp
        else:                          # dest must be either first or second!
            print("dest must either be first or second")
            exit(1)



        disappeared += [ second ]      # this particle's mass was assigned to another
       # print(disappeared)

        if first in disappeared:
            print("this particle should not exist(first)")    # appear again
            print(first)
            exit(1)
        if first in tree:
            if (words[4]) in (words[0]):
                print(second,iii)
                iii+=1
                print("this particle should not exist(second)")


            if second in tree:
                  tree[first] = tree[first] + tree[ second ]



            else:
                tree[first] = tree[first] + [second]



        else:          # first never been seen
            if second not in tree:                     # if neither first or second has been seen
                tree[first] = [ first, second ]
            else:
                tree[first] =  [first] + tree[second] # if second is composite
#print(tree)
elements = genfromtxt("element.out")
#print(elements[1,0])

treeout= open('treeoutput.txt', 'w')# as file_handler:
for k in np.arange(0,len(elements.T)):
    #for v in range(0,29):
     #   if v ==25:
      #      continue

        if tree[v][0] == elements[k,0]:
                treeout.write("{}\n".format(tree[elements[k,0]]))



            #for item in tree:
               # treeout.write("{}\n".format(tree[elements[k,0]]))"""
treeout.close()




"""from matplotlib.ticker import FuncFormatter
from pylab import genfromtxt
from numpy import flipud
import numpy as np
import matplotlib.pyplot as plt
hist1 = genfromtxt("params.txt")
hist = flipud(hist1)
pl_index = genfromtxt("element.out",dtype=int)
#print(hist.shape)
#print(hist1.shape)
#t = hist[:,0]
sma = hist[:,0]
sma_0 = sma
l = list(pl_index[:,0])
k = tuple(l)
p = ' '.join([str(i) for i in l])
print(p)
#print(l)
#print(tree.keys())
#print(sma_0.shape)
#[tree[i] for i in l]
#a = tree[i]
print(sma_0)
#embryo_distance1 = [sma_0[i-1] for i in tree[49]] FIX THIS!!!!!
embryo_distance2 = [sma_0[i-1] for i in tree[40]]
embryo_distance3 = [sma_0[i-1] for i in tree[44]]
embryo_distance4 = [sma_0[i-1] for i in tree[37]]
embryo_distance5 = [sma_0[i-1] for i in tree[21]]
#embryo_distance6 = [sma_0[i-1] for i in tree[35]]
#embryo_distance = sma_0[:,tree[50]]
print(sma_0)

fig = plt.figure()

ax = fig.add_subplot(111)

p1= .4906
p2= .2626
p3= 1.7810
p4= .0576

planet1 = ax.plot(p1,1,'yo')
planet2 = ax.plot(p2,1,'ro')
planet3 = ax.plot(p3,1,'bo')
planet4 = ax.plot(p4,1,'ko')
#planet5 = ax.plot(1,1,'co')
#planet6 = ax.plot(.2169,1,'mo')


#x1 = embryo_distance1
x2 = np.array(embryo_distance2)/p1
x3 = np.array(embryo_distance3)/p2
x4 = np.array(embryo_distance4)/p3
x5 = np.array(embryo_distance5)/p4
#x6 = embryo_distance6
bins =[10]


#ax.hist(x1,10,color='y', histtype='step', cumulative='True', alpha=0.5)
ax.hist(x2,10,color='r', histtype='step', cumulative='False', alpha=0.5)
hist2y, hist2x, _ = ax.hist(x2,10,color='r', histtype='step', cumulative='True', alpha=0.5)
fz2 = (hist2x[9] - hist2x[0])

ax.hist(x3,10,color='b', histtype='step', cumulative='False', alpha=0.5)
hist3y, hist3x, _ = ax.hist(x3,10,color='b', histtype='step', cumulative='True', alpha=0.5)
fz3 = (hist3x[9] - hist3x[0])

ax.hist(x4,10,color='k', histtype='step', cumulative='False', alpha=0.5)
hist4y, hist4x, _ = ax.hist(x4,10,color='k', histtype='step', cumulative='True', alpha=0.5)
fz4 = (hist4x[9] - hist4x[0])

ax.hist(x5,10,color='m', histtype='step', cumulative='False', alpha=0.5)
hist5y, hist5x, _ = ax.hist(x5,10,color='c', histtype='step', cumulative='True', alpha=0.5)
fz5 = (hist5x[9] - hist5x[0])

avg_fz = (fz2+fz3+fz4+fz5)/4

print(avg_fz)
#ax.hist(x6,10,color='m', histtype='step', cumulative='True', alpha=0.5)


#def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
 #   s = str(100 * y)


  #  return s + '%'

#formatter = FuncFormatter(to_percent)

# Set the formatter
#plt.gca().yaxis.set_major_formatter(formatter)



#ax.set_xscale('log')
ax.set_xlim([0,1])
ax.set_ylim([0,20])
plt.ylabel('Total Number of Embryos')
plt.xlabel('Semi-major axis')





plt.show()"""
