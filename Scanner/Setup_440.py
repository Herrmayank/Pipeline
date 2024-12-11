import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Given values
r = 300  # Radius
z0 = 500.0  # Distance

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
        # Equations from the simple model, with distortion applied only to x
        x = -r * np.tan(alpha) * (((z0 - r) / (r * np.cos(beta))) + 1)
        y = beta  # Keeping y as the original beta value for no distortion in y-axis

        # Append to arrays
        X.append(x)
        Y.append(y)

        # Plot the distorted point with reduced size
        ax.scatter(x, y, c='r', marker='o', s=5)

# Draw a rectangle connecting the outermost points
min_x, max_x = min(X), max(X)
min_y, max_y = min(Y), max(Y)
rectangle = plt.Rectangle((min_x, min_y), max_x - min_x, max_y - min_y, fill=False, edgecolor='blue', linestyle='--')
ax.add_patch(rectangle)

# Calculate and mark the center of the plot
center_x = (max_x + min_x) / 2
center_y = (max_y + min_y) / 2
ax.scatter(center_x, center_y, c='blue', marker='x', s=100)  # Mark the center with a larger marker
ax.text(center_x, center_y, ' Center', color='blue', fontsize=10, verticalalignment='bottom')

# Set labels for the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Set the plot title
plt.title('GLS System Distortion')

# Set up the grid
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.grid(which='major', color='gray', linestyle='-', linewidth=0.5)

# Display the FOV, length, and breadth values on the plot in blue
label_text = "FOV: 0.140m\u00B2, Length = 335, Breadth = 318"
ax.text(0.95, 0.95, label_text,
        verticalalignment='top', horizontalalignment='right',
        transform=ax.transAxes, color='blue', fontsize=10)

# Show the plot
plt.show()
