import numpy as np
import matplotlib.pyplot as plt

# setting the axes projection as polar
ax = plt.subplot(111, polar=True)
# plt.axes(projection='polar')
ax.set_theta_zero_location("N")

# setting the radius
radius = np.arange(0, 1.0, 0.01)

# radian values
radians = np.arange(0, (2 * np.pi), 0.05)
print (radians)

# plotting the circle
for radian in radians:
    for rad in radius:
        ax.plot(radian, rad, color='black', marker='.', linestyle='dashed', linewidth=1, markersize=2)

# display the Polar plot
# plt.show()