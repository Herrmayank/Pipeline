import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

# Function to calculate the deflection angle for a given FOV and height
def calculate_deflection_angle_for_fov(fov_m2, height_mm):
    height_m = height_mm / 1000.0  # Convert mm to meters
    side_of_square_m = math.sqrt(fov_m2)  # Calculate the side of the square
    base_m = side_of_square_m / 2
    angle_radians = math.atan(base_m / height_m)
    deflection_angle = math.degrees(angle_radians)  # Convert radians to degrees
    return deflection_angle

# Calculate the deflection angle for a FOV of 0.140 square meters and height of 448 mm
deflection_angle = calculate_deflection_angle_for_fov(0.140, 448)

# Given values
r = 40.0  # Radius
z0 = 50.0  # Distance

# Adjust alpha_values and beta_values based on the calculated deflection angle
alpha_values = np.deg2rad(np.linspace(-deflection_angle, deflection_angle, 21))
beta_values = np.deg2rad(np.linspace(-deflection_angle, deflection_angle, 21))

# Create a figure and axis
fig, ax = plt.subplots()

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

# Find the outermost points
min_x, max_x = min(X), max(X)
min_y, max_y = min(Y), max(Y)

# Draw a rectangle connecting the outermost points
rectangle = plt.Rectangle((min_x, min_y), max_x - min_x, max_y - min_y, fill=False, edgecolor='blue', linestyle='--')
ax.add_patch(rectangle)

# Calculate the length and breadth of the rectangle
length = max_x - min_x
breadth = max_y - min_y

# Set labels for the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Set the plot title
plt.title('GLS System Distortion')

# Set up the grid
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.grid(which='major', color='gray', linestyle='-', linewidth=0.5)

# Display the length and breadth on the plot
ax.text(0.95, 0.95, f'Length: {length:.2f} mm\nBreadth: {breadth:.2f} mm',
        verticalalignment='top', horizontalalignment='right',
        transform=ax.transAxes, color='green', fontsize=10)

# Show the plot
plt.show()


