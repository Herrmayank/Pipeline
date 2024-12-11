import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def draw_3d_pyramid(height_mm, deflection_angle=22.5, inner_deflection_angle=20):
    # Convert angle to radians for math functions
    angle_radians = math.radians(deflection_angle)
    inner_angle_radians = math.radians(inner_deflection_angle)

    # Calculate base of the outer and inner triangles in millimeters
    base_mm = math.tan(angle_radians) * height_mm
    inner_base_mm = math.tan(inner_angle_radians) * height_mm

    # Calculate the side of the square (FOV base) and area for both pyramids
    side_of_square_mm = 2 * base_mm
    area_of_square_mm2 = side_of_square_mm ** 2
    inner_side_of_square_mm = 2 * inner_base_mm
    inner_area_of_square_mm2 = inner_side_of_square_mm ** 2

    # Create figure and axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Function to create pyramid vertices
    def create_pyramid_vertices(base_size):
        return [
            [base_size, base_size, 0],
            [base_size, -base_size, 0],
            [-base_size, -base_size, 0],
            [-base_size, base_size, 0],
            [0, 0, height_mm]
        ]

    # Define the vertices of the outer and inner pyramids
    outer_vertices = create_pyramid_vertices(base_mm)
    inner_vertices = create_pyramid_vertices(inner_base_mm)

    # Function to create pyramid faces
    def create_pyramid_faces(vertices):
        return [
            [vertices[0], vertices[1], vertices[4]],
            [vertices[1], vertices[2], vertices[4]],
            [vertices[2], vertices[3], vertices[4]],
            [vertices[3], vertices[0], vertices[4]],
            [vertices[0], vertices[1], vertices[2], vertices[3]]  # Base
        ]

    # Define the faces of the outer and inner pyramids
    outer_faces = create_pyramid_faces(outer_vertices)
    inner_faces = create_pyramid_faces(inner_vertices)

    # Plot the outer pyramid (GLS)
    outer_pyramid = Poly3DCollection(outer_faces, edgecolors='r', linewidths=1, alpha=0.3)
    outer_pyramid.set_facecolor('cyan')
    ax.add_collection3d(outer_pyramid)

    # Plot the inner pyramid (Camera)
    inner_pyramid = Poly3DCollection(inner_faces, edgecolors='b', linewidths=1, alpha=0.9)
    inner_pyramid.set_facecolor('yellow')
    ax.add_collection3d(inner_pyramid)

    # Annotate calculated values for GLS
    ax.text2D(0.05, 0.95, f"GLS - Angle: {deflection_angle}°, Height: {height_mm} mm", transform=ax.transAxes)
    ax.text2D(0.05, 0.92, f"GLS Base Side: {side_of_square_mm:.2f} mm, Area: {area_of_square_mm2:.2f} mm²", transform=ax.transAxes)

    # Annotate calculated values for Camera
    ax.text2D(0.05, 0.89, f"Camera - Angle: {inner_deflection_angle}°, Height: {height_mm} mm", transform=ax.transAxes)
    ax.text2D(0.05, 0.86, f"Camera Base Side: {inner_side_of_square_mm:.2f} mm, Area: {inner_area_of_square_mm2:.2f} mm²", transform=ax.transAxes)

    # Set plot limits
    ax.set_xlim([-base_mm, base_mm])
    ax.set_ylim([-base_mm, base_mm])
    ax.set_zlim([0, height_mm])

    # Label the axesjj
    ax.set_xlabel('X axis (mm)')
    ax.set_ylabel('Y axis (mm)')
    ax.set_zlabel('Height (mm)')

    # Set plot title
    plt.title('Field of View (FOV) Calculation')

    plt.show()

# Example: Draw 3D pyramids for 1000 mm height
draw_3d_pyramid(1000)
