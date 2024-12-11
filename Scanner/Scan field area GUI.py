import tkinter as tk
from math import tan, atan, degrees, radians


def calculate_scan_area():
    deflection_angle = float(deflection_angle_entry.get())
    distance_to_surface = float(distance_to_surface_entry.get())
    scan_area = 2 * distance_to_surface * tan(deflection_angle)
    scan_area_result.set(f"Scan Area: {scan_area:.2f} square meters")


def calculate_deflection_angle():
    scan_area = float(scan_area_entry.get())
    distance_to_surface = float(distance_to_surface_entry.get())
    deflection_angle = atan(scan_area / (2 * distance_to_surface))
    deflection_angle_result.set(f"Deflection Angle: {degrees(deflection_angle):.2f} degrees")


# Create the main window
root = tk.Tk()
root.title("GLS Scan Area Calculator")

# Create and configure the input fields
deflection_angle_label = tk.Label(root, text="Deflection Angle (radians):")
deflection_angle_label.pack()
deflection_angle_entry = tk.Entry(root)
deflection_angle_entry.pack()

scan_area_label = tk.Label(root, text="Scan Area (square meters):")
scan_area_label.pack()
scan_area_entry = tk.Entry(root)
scan_area_entry.pack()

distance_to_surface_label = tk.Label(root, text="Distance to Surface (meters):")
distance_to_surface_label.pack()
distance_to_surface_entry = tk.Entry(root)
distance_to_surface_entry.pack()

# Create variables to store the results
scan_area_result = tk.StringVar()
deflection_angle_result = tk.StringVar()

# Create buttons to perform the calculations
calculate_area_button = tk.Button(root, text="Calculate Scan Area", command=calculate_scan_area)
calculate_area_button.pack()

calculate_angle_button = tk.Button(root, text="Calculate Deflection Angle", command=calculate_deflection_angle)
calculate_angle_button.pack()

# Create labels to display the results
result_label1 = tk.Label(root, textvariable=scan_area_result)
result_label1.pack()

result_label2 = tk.Label(root, textvariable=deflection_angle_result)
result_label2.pack()

# Start the main loop
root.mainloop()