import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import struct, binascii, socket, time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 5000))

def overlay(i):
    global angle

    data, addr = sock.recvfrom(1026)
    # angle = int(binascii.hexlify(data)[0:2], 16)
    angle = data[0] + data[1]
    print(angle)
    distance = data[2]

    preTime = time.time()
    if angle == 360:
        ax.clear()
        angle = 0
    else:
        angle = angle + 1

    # for distance in distances:
    ax.scatter((np.pi/180) * angle, 1, color=color, marker='.', linestyle='dashed', linewidth=0.1)
    print(angle)
    curTime = time.time()
    print((curTime - preTime)*1000)
    # ax.plot(angle, distance, c='white', marker='*', linestyle='dashed', linewidth=1, markersize=2)
    plt.title('Radar Video')
    ax.set_yticklabels([])
    ax.set_theta_zero_location("N")

fig = plt.figure()
ax = plt.subplot(polar="True")
ax.set_yticklabels([])
ax.set_theta_zero_location("N")
# canvas = FigureCanvas(fig)
plt.title('Radar Video')

distances = np.linspace(0, 1, 100)
angles = np.arange(0, (2 * np.pi), 0.1)

angle = 0
color = (0, 0, 0)

anim = animation.FuncAnimation(fig, overlay, interval=1, blit=False, frames=100)
# anim.save('overlay.mp4', writer=writer)
plt.show()

