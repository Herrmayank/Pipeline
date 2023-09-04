import numpy as np
import matplotlib.pyplot as plt
#Definitions:

#x: The first mirror hit by the incoming laser ray, used for horizontal axis scanning.

#y: The second mirror in the system, employed for vertical axis scanning.

#z: The position of the laser coordinate system's origin (O) on the rotation axis at the center of the X-mirror.

#z0: The distance from the origin to a screen parallel to the XOY plane.

#α: The angle that defines the position of the first mirror (X-mirror).

#β: The angle that describes the position of the second mirror (Y-mirror).

#Equations:

#Equation (1):

#CA = P + tQ

#Where:

#CA = (0, r·sinβ, r - r·cosβ)

#P = (0, 0, 0; r·sinβ, 0, r - r·cosβ)

#t = t

#Q = (r·tanα, -r·sinβ, r·cosβ)

#Equation (2):

#P = P₀ + tP₁

#Where:

#P = (0, r·sinβ, r - r·cosβ)

#P₀ = (0, 0, 0; r·sinβ, 0, r - r·cosβ)

#t = ((z0 - r) / (r·cosβ)) + 1

#P₁ = (r·tanα, -r·sinβ, r·cosβ)

#Equations (3):

#x = -r * tan(α) * [{(z0 - r) / (r * cos(β))} + 1]

#y = [{(z0 - r) / cos(β)} + {r * (1 + sin(β))}]

#z = z0
#point spread function
# Given values
r = 1.0  # Replace with your actual value
z0 = 2.0  # Replace with your actual value

# Create a figure and axis
fig, ax = plt.subplots()

# Generate a range of angles α and β
alpha_values = np.deg2rad(np.linspace(-22.5, 22.5, 21))  # 21 points from -22.5 to 22.5 degrees
beta_values = np.deg2rad(np.linspace(-22.5, 22.5, 21))   # 21 points from -22.5 to 22.5 degrees

# Loop through α and β values
for alpha in alpha_values:
    for beta in beta_values:
        # Equations from the simple model
        x = -r * np.tan(alpha) * (((z0 - r) / (r * np.cos(beta))) + 1)
        y = (((z0 - r) / np.cos(beta)) + (r * (1 + np.sin(beta))))

        # Plot the distorted point
        ax.scatter(x, y, c='r', marker='o')

# Set labels for the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Set the plot title
plt.title('GLS System Distortion')

# Show the plot
plt.show()
