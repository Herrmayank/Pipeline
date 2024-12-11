import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

# Given values
r = 40.0  # Radius
z0 = 50.0  # Distance
length = 335  # Length for the label
breadth = 318  # Breadth for the label
fov = 0.08  # Field of View in m2

# Generate a range of angles α and β with half the number of points in each direction
alpha_values = np.deg2rad(np.linspace(-22.5, 22.5, 15))  # 11 points from -22.5 to 22.5 degrees
beta_values = np.deg2rad(np.linspace(-22.5, 22.5, 15))  # 11 points from -22.5 to 22.5 degrees

# Initialize arrays for X and Y coordinates
X = []
Y = []

# Loop through α and β values
for alpha in alpha_values:
    for beta in beta_values:
        # Equations from the simple model
        x = -r * np.tan(alpha) * (((z0 - r) / (r * np.cos(beta))) + 1)
        y = (((z0 - r) / np.cos(beta)) + (r * (1 + np.sin(beta))))

        # Append to arrays
        X.append(x)
        Y.append(y)

# Creating a figure and axis
fig, ax = plt.subplots()

# Plot the points
ax.scatter(X, Y, c='r', marker='o')

# Determine the corner points of the plot
min_x, max_x = min(X), max(X)
min_y, max_y = min(Y), max(Y)

# Draw a rectangle around the plot passing through the corner points
rectangle = plt.Rectangle((min_x, min_y), max_x - min_x, max_y - min_y, fill=False, edgecolor='blue', linewidth=2)
ax.add_patch(rectangle)

# Add label on the top right corner in blue
label_text = f"FOV={fov}m², Length = {length}, Breadth = {breadth}"
ax.text(max_x, max_y, label_text, horizontalalignment='right', verticalalignment='top', color='blue')

# Mark the center point with a cross 'x'
center_x = (max_x + min_x) / 2
center_y = (max_y + min_y) / 2
ax.plot(center_x, center_y, 'x', color='black', markersize=10, markeredgewidth=2)  # Mark the center with 'x'

# Set labels for the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Set the plot title
ax.set_title('GLS Distortion Plot')

# Create a 1x1mm grid
ax.set_xticks(np.arange(min(X), max(X), 1))
ax.set_yticks(np.arange(min(Y), max(Y), 1))
ax.grid(which='both')

# Show the plot with grid overlay
plt.show()
