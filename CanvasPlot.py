import time, threading
import datetime as dt
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.figure import Figure


# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


def overlay(i):
    global color, angle, distances

    if angle == 360:
        ax.clear()
        angle = 0
        color = [0, 0, 0]
    else:
        angle = angle + 1
        # color[0] = color[0] - 0.005

    # for distance in distances:
    preTime = time.time()
    for distance in range(0, 25):
        ax.plot((np.pi / 180) * angle, distance, color=color, marker='.', linestyle='dashed', linewidth=0.1)

fig = plt.figure()
ax = plt.subplot(polar="True")
plt.title('Radar Video')
ax.set_yticklabels([])
ax.set_theta_zero_location("N")

distances = np.linspace(0, 1, 63)
angles = np.arange(0, (2 * np.pi), 0.1)
angle = 0
color = [0, 0, 0]

anim = animation.FuncAnimation(fig, overlay, interval=0.001, blit=False, frames=60)
plt.show()
