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

# Initialize arrays for X and Y coordinates
X = []
Y = []

# Loop through α and β values
for alpha in alpha_values:
    for beta in beta_values:
        # Equations from the simple model
        x = -r * np.tan(alpha) * (((z0 - r) / (r * np.cos(beta))) + 1)
        y = (((z0 - r) / np.cos(beta)) + (r * (1 + np.sin(beta))))

        X.append(x)
        Y.append(y)

        # Plot the distorted point
        ax.scatter(x, y, c='r', marker='o')

# Set the limits for the axes to include negative values
ax.set_xlim(min(X), max(X))
ax.set_ylim(min(Y), max(Y))

# Optionally, set the tick intervals
x_tick_interval = (max(X) - min(X)) / 10  # Example: divide the X range into 10 intervals
y_tick_interval = (max(Y) - min(Y)) / 10  # Example: divide the Y range into 10 intervals

ax.set_xticks(np.arange(min(X), max(X) + x_tick_interval, x_tick_interval))
ax.set_yticks(np.arange(min(Y), max(Y) + y_tick_interval, y_tick_interval))

# Set labels for the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Set the plot title
plt.title('GLS System Distortion')

# Show the plot
plt.show()
