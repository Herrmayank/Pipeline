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

# Initialize arrays for all X and Y coordinates
all_x_values = []
all_y_values = []

# Loop through α and β values to plot lines in each column
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

    ax.plot(x_values, y_values, c='r', linewidth=0.5)

# Loop through β and α values to plot lines in each row
for beta in beta_values:
    x_values = []
    y_values = []
    for alpha in alpha_values:
        # Equations from the simple model
        x = -r * np.tan(alpha) * (((z0 - r) / (r * np.cos(beta))) + 1)
        y = (((z0 - r) / np.cos(beta)) + (r * (1 + np.sin(beta))))
        x_values.append(x)
        y_values.append(y)
        all_x_values.append(x)
        all_y_values.append(y)

    ax.plot(x_values, y_values, c='r', linewidth=0.5)

# Calculate the true center of the entire grid
center_x = np.mean(all_x_values)
center_y = np.mean(all_y_values)

# Marking the true center of the entire grid with lines
ax.axhline(y=center_y, color='blue', linestyle='--', linewidth=1)  # Horizontal line through center Y
ax.axvline(x=center_x, color='blue', linestyle='--', linewidth=1)  # Vertical line through center X

# Adding tick marks and labels for the center point on the axes
ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
ax.set_xticks(list(ax.get_xticks()) + [center_x])
ax.set_yticks(list(ax.get_yticks()) + [center_y])
ax.set_xticklabels(list(ax.get_xticks()), rotation=45)
ax.set_yticklabels(list(ax.get_yticks()))

# Set labels for the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Set the plot title
plt.title('GLS System Distortion - Grid Pattern with True Center Marked')

# Show the plot
plt.show()
