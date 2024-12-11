import numpy as np
import matplotlib.pyplot as plt

# Given values
r = 1.0  # Radius, replace with your actual value
z0 = 2.0  # Distance, replace with your actual value

# Create a figure and axis
fig, ax = plt.subplots()

# Generate a range of angles α and β
alpha_values = np.deg2rad(np.linspace(-22.5, 22.5, 21))  # 21 points from -22.5 to 22.5 degrees
beta_values = np.deg2rad(np.linspace(-22.5, 22.5, 21))   # 21 points from -22.5 to 22.5 degrees

# Initialize lists to store all X and Y values
all_x_values = []
all_y_values = []

# Loop through α and β values for columns
for alpha in alpha_values:
    x_values = []
    y_values = []
    for beta in beta_values:
        # Equations from the simple model
        x = -r * np.tan(alpha) * (((z0 - r) / (r * np.cos(beta))) + 1)
        y = (((z0 - r) / np.cos(beta)) + (r * (1 + np.sin(beta))))

        x_values.append(x)
        y_values.append(y)
        all_x_values.append(x)
        all_y_values.append(y)

    # Plot lines to join points in each column
    ax.plot(x_values, y_values, c='r', linewidth=0.5)

# Loop through β and α values for rows
for beta in beta_values:
    x_values = []
    y_values = []
    for alpha in alpha_values:
        # Equations from the simple model
        x = -r * np.tan(alpha) * (((z0 - r) / (r * np.cos(beta))) + 1)
        y = (((z0 - r) / np.cos(beta)) + (r * (1 + np.sin(beta))))

        x_values.append(x)
        y_values.append(y)

    # Plot lines to join points in each row
    ax.plot(x_values, y_values, c='r', linewidth=0.5)

# Determine symmetric grid range
max_range = max(max(all_x_values) - min(all_x_values), max(all_y_values) - min(all_y_values)) / 2
mid_x = (max(all_x_values) + min(all_x_values)) / 2
mid_y = (max(all_y_values) + min(all_y_values)) / 2

# Marking the center of the plot
ax.scatter(mid_x, mid_y, c='blue', marker='o', zorder=5)  # Blue dot at the center
ax.text(mid_x + 0.05, mid_y, f'({mid_x:.2f}, {mid_y:.2f})', color='blue', zorder=5)  # Label the center

# Setting plot limits for symmetric grid
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)

# Setting up the 10x10mm grid background
ax.set_xticks(np.arange(mid_x - max_range, mid_x + max_range + 10, 10), minor=True)
ax.set_yticks(np.arange(mid_y - max_range, mid_y + max_range + 10, 10), minor=True)
ax.grid(which='minor', color='gray', linestyle='-', linewidth=0.5)
ax.grid(which='major', color='black', linewidth=1)
ax.set_aspect('equal', adjustable='box')  # Ensures equal scaling

# Set labels for the axes
ax.set_xlabel('X-axis (mm)')
ax.set_ylabel('Y-axis (mm)')

# Set the plot title
plt.title('GLS System Distortion - Grid Pattern with 10x10mm Background')

# Show the plot
plt.show()
