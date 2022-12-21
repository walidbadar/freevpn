from PIL import Image, ImageDraw
import numpy as np

# Create a blank image with a white background
width, height = 640, 480
image = Image.new("RGB", (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image)
# Generate evenly spaced values from 0 to 2*pi
theta = np.linspace(0, 2*np.pi, 100)

# Calculate the intensity at each angle
intensity = np.sin(theta)
# Calculate the x and y coordinates for each point
x = intensity * np.cos(theta)
y = intensity * np.sin(theta)
# Convert the coordinates to pixel values
x_pixels = (x + 1) * width / 2
y_pixels = (1 - y) * height / 2

# Draw the line
draw.line(list(zip(x_pixels, y_pixels)), fill=(255, 0, 0))
image.save("polar_plot.png")
