
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import binascii, struct, socket, datetime

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a local address and port
sock.bind(('localhost', 5000))

# Set the figure size and title
fig = plt.figure()
ax = plt.subplot(polar=True)

plt.title("Radar Video")
xs = []
ys = []

def animate(i, xs, ys):
    # Receive data from the socket
    data, addr = sock.recvfrom(1026)
    print (addr)
    print(datetime.datetime.now())
    # angle = int(binascii.hexlify(data)[0:2], 16)
    angle = data[0]+data[1]
    print(angle)
    distance = data[2]
    print(distance)

    # # Plot the data
    xs.append(angle)
    ys.append(distance)

    ax.clear()
    ax.set_theta_zero_location("N")
    ax.plot((np.pi/180)*angle, distance, 'bo')

ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=0.6)
plt.show()
