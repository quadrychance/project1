# Plots a radar chart.
from pylab import genfromtxt
from math import pi
import matplotlib.pyplot as plt

arr = genfromtxt('fracoutput.txt')
# Set data
cat = ['Water', 'CO2', 'NH3']
values = [arr[0,0], arr[1,0], arr[2,0]]
values2 = [arr[0,1], arr[1,1], arr[2,1]]
values3 = [arr[0,2], arr[1,2], arr[2,2]]
values4 = [arr[0,3], arr[1,3], arr[2,3]]
values5 = [arr[0,4], arr[1,4], arr[2,4]]
N = len(cat)

x_as = [n / float(N) * 2 * pi for n in range(N)]

# Because our chart will be circular we need to append a copy of the first
# value of each list at the end of each list with data
values += values[:1]
values2 += values2[:1]
values3 += values3[:1]
values4 += values4[:1]
values5 += values5[:1]
x_as += x_as[:1]


# Set color of axes
plt.rc('axes', linewidth=0.5, edgecolor="#888888")


# Create polar plot
ax = plt.subplot(111, polar=True)


# Set clockwise rotation. That is:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)


# Set position of y-labels
ax.set_rlabel_position(0)


# Set color and linestyle of grid
ax.xaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)
ax.yaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)


# Set number of radial axes and remove labels
plt.xticks(x_as[:-1], [])

# Set yticks
#plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"])


# Plot data
ax.plot(x_as, values, linewidth=1, linestyle='solid', zorder=3)
# Fill area
#ax.fill(x_as, values,  alpha=0.4)

ax.plot(x_as, values2, linewidth=1, linestyle='solid', zorder=3)
# Fill area
#ax.fill(x_as, values2, alpha=0.4)

ax.plot(x_as, values3, linewidth=1, linestyle='solid', zorder=3)
# Fill area
#ax.fill(x_as, values3,  alpha=0.4)

ax.plot(x_as, values4, linewidth=1, linestyle='solid', zorder=3)
# Fill area
#ax.fill(x_as, values4,  alpha=0.4)

ax.plot(x_as, values5, linewidth=1, linestyle='solid', zorder=3)
# Fill area
#ax.fill(x_as, values5,  alpha=0.4)

# Set axes limits
plt.ylim(0, .06)
#ax.set_rlim(0, .05)
#ax.set_rscale('log')

ax.set_xticklabels(cat)


# Draw ytick labels to make sure they fit properly
for i in range(N):
    angle_rad = i / float(N) * 2 * pi

    if angle_rad == 0:
        ha, distance_ax = "center", 10
    elif 0 < angle_rad < pi:
        ha, distance_ax = "left", 1
    elif angle_rad == pi:
        ha, distance_ax = "center", 1
    else:
        ha, distance_ax = "right", 1

    ax.text(angle_rad, 100 + distance_ax, cat[i], size=10, horizontalalignment=ha, verticalalignment="center")


# Show polar plot
plt.show()
