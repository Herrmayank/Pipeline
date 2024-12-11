import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the side of the square based on the height of GLS
def calculate_square_side(height):
    deflection_angle = 22.5  # degrees
    base = np.tan(np.deg2rad(deflection_angle)) * height
    side = 2 * base
    return side

# GLS height - Replace this with the user input value in a GUI scenario
gls_height = 0.25  # Example height, 1 meter

# Calculate the side of the square for the given height
side_length = calculate_square_side(gls_height)

# Convert side length to cm for plotting
side_length_cm = side_length * 100

# Create a figure and axis
fig, ax = plt.subplots()

# Adjust the range of angles based on the calculated side length
alpha_values = np.deg2rad(np.linspace(-22.5, 22.5, int(side_length_cm)))  # Adjusted range
beta_values = np.deg2rad(np.linspace(-22.5, 22.5, int(side_length_cm)))   # Adjusted range

# Loop through α and β values
for alpha in alpha_values:
    x_values = []
    y_values = []
    for beta in beta_values:
        # Equations from the simple model
        x = -np.tan(alpha) * side_length / 2
        y = side_length / 2 - (side_length / 2 * np.sin(beta))

        x_values.append(x)
        y_values.append(y)

    # Plot lines to join points in each column
    ax.plot(x_values, y_values, c='r', linewidth=0.5)

# Loop through β and α values to plot lines in each row
for beta in beta_values:
    x_values = []
    y_values = []
    for alpha in alpha_values:
        # Equations from the simple model
        x = -np.tan(alpha) * side_length / 2
        y = side_length / 2 - (side_length / 2 * np.sin(beta))

        x_values.append(x)
        y_values.append(y)

    # Plot lines to join points in each row
    ax.plot(x_values, y_values, c='r', linewidth=0.5)

# Set labels for the axes
ax.set_xlabel('X-axis (cm)')
ax.set_ylabel('Y-axis (cm)')

# Set the plot title
plt.title(f'GLS System Distortion - Grid Pattern at Height: {gls_height}m')

# Show the plot
plt.show()
