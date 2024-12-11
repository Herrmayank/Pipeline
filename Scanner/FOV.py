import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def draw_3d_pyramid(height_mm, deflection_angle=22.5):
    # Convert angle to radians for math functions
    angle_radians = math.radians(deflection_angle)

    # Calculate base of the triangle in millimeters
    base_mm = math.tan(angle_radians) * height_mm

    # Calculate the side of the square (FOV base) and area
    side_of_square_mm = 2 * base_mm
    area_of_square_mm2 = side_of_square_mm ** 2

    # Define the vertices of the pyramid
    vertices = [
        [base_mm, base_mm, 0],
        [base_mm, -base_mm, 0],
        [-base_mm, -base_mm, 0],
        [-base_mm, base_mm, 0],
        [0, 0, height_mm]
    ]

    # Define the sides of the pyramid (5 faces)
    faces = [
        [vertices[0], vertices[1], vertices[4]],
        [vertices[1], vertices[2], vertices[4]],
        [vertices[2], vertices[3], vertices[4]],
        [vertices[3], vertices[0], vertices[4]],
        [vertices[0], vertices[1], vertices[2], vertices[3]]  # Base
    ]

    # Create 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the faces
    pyramid = Poly3DCollection(faces, edgecolors='r', linewidths=1, alpha=0.5)
    pyramid.set_facecolor('cyan')
    ax.add_collection3d(pyramid)

    # Set plot limits
    ax.set_xlim([-base_mm, base_mm])
    ax.set_ylim([-base_mm, base_mm])
    ax.set_zlim([0, height_mm])

    # Label the axes
    ax.set_xlabel('X axis (mm)')
    ax.set_ylabel('Y axis (mm)')
    ax.set_zlabel('Height (mm)')

    # Annotate calculated values
    ax.text2D(0.05, 0.95, f"Deflection Angle: {deflection_angle}°", transform=ax.transAxes)
    ax.text2D(0.05, 0.90, f"Height: {height_mm} mm", transform=ax.transAxes)
    ax.text2D(0.05, 0.85, f"Base Side: {side_of_square_mm:.2f} mm", transform=ax.transAxes)
    ax.text2D(0.05, 0.80, f"Base Area: {area_of_square_mm2:.2f} mm²", transform=ax.transAxes)

    # Set plot title
    plt.title('FOV Calculation')

    plt.show()

# Example: Draw 3D upside-down pyramid for 1000 mm height
draw_3d_pyramid(448)


