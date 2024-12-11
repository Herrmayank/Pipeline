import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Given values
r = 400.0  # Radius, replace with your actual value
z0 = 500.0  # Distance, replace with your actual value

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

# Determine the center of the plotted coordinates
center_x = (max(X) + min(X)) / 2
center_y = (max(Y) + min(Y)) / 2

# Marking the center of the plotted coordinates
ax.scatter(center_x, center_y, c='blue', marker='o')  # Mark the center
ax.text(center_x + 0.1, center_y, f'({center_x:.2f}, {center_y:.2f})', color='blue')  # Label the center

# Set labels for the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Set the plot title
plt.title('GLS System Distortion')

# Set up the grid
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.grid(which='major', color='gray', linestyle='-', linewidth=0.5)

# Show the plot
plt.show()
