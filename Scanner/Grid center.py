import numpy as np
import matplotlib.pyplot as plt

# Given values
r = 1.0  # Radius, replace with your actual value
z0 = 2.0  # Distance, replace with your actual value

# Create a figure and axis
fig, ax = plt.subplots()

# Generate a range of angles α and β
alpha_values = np.deg2rad(np.linspace(-22.5, 22.5, 21))  # 21 points from -22.5 to 22.5 degrees
beta_values = np.deg2rad(np.linspace(-22.5, 22.5, 21))  # 21 points from -22.5 to 22.5 degrees

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

        # Plot the distorted point
        ax.scatter(x, y, c='r', marker='o')

# Set plot limits to ensure a symmetric grid
max_range = max(max(X) - min(X), max(Y) - min(Y)) / 2
mid_x = (max(X) + min(X)) / 2
mid_y = (max(Y) + min(Y)) / 2
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)

# Setting up the 1x1mm grid background
ax.set_xticks(np.arange(mid_x - max_range, mid_x + max_range + 1, 1), minor=True)
ax.set_yticks(np.arange(mid_y - max_range, mid_y + max_range + 1, 1), minor=True)
ax.grid(which='minor', color='gray', linestyle='-', linewidth=0.5)
ax.grid(which='major', color='black', linewidth=1)
ax.set_aspect('equal', adjustable='box')  # Ensures equal scaling

# Set labels for the axes
ax.set_xlabel('X-axis (mm)')
ax.set_ylabel('Y-axis (mm)')

# Set the plot title
plt.title('GLS System Distortion with 1x1mm Grid Background')

# Show the plot
plt.show()
