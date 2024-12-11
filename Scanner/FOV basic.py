import math

def calculate_fov(height_mm, deflection_angle=22.5):
    height_m = height_mm / 1000.0  # Convert mm to meters
    angle_radians = math.radians(deflection_angle)  # Convert degrees to radians
    base_m = math.tan(angle_radians) * height_m
    side_of_square_m = 2 * base_m
    fov_m2 = side_of_square_m ** 2
    return fov_m2

# Calculate FOV for  788 mm height
fov_at_348mm = calculate_fov(348)
print(f"The FOV at a height of 388 mm is {fov_at_348mm:.2f} square meters.")