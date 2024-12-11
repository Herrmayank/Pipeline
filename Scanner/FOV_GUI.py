import math
import tkinter as tk
from tkinter import simpledialog

def calculate_fov(height_mm, deflection_angle=22.5):
    height_m = height_mm / 1000.0  # Convert mm to meters
    angle_radians = math.radians(deflection_angle)  # Convert degrees to radians
    base_m = math.tan(angle_radians) * height_m
    side_of_square_m = 2 * base_m
    fov_m2 = side_of_square_m ** 2
    return fov_m2

def calculate_height(fov_m2, deflection_angle=22.5):
    side_of_square_m = math.sqrt(fov_m2)
    base_m = side_of_square_m / 2
    angle_radians = math.radians(deflection_angle)
    height_m = base_m / math.tan(angle_radians)
    return height_m * 1000  # Convert back to mm

def on_submit_fov():
    height = float(height_entry.get())
    fov = calculate_fov(height)
    result_label.config(text=f"Calculated FOV: {fov:.2f} square meters")

def on_submit_height():
    fov = float(fov_entry.get())
    height = calculate_height(fov)
    result_label.config(text=f"Estimated Height: {height:.2f} mm")

root = tk.Tk()
root.title("FOV and Height Calculator")

# Height input
tk.Label(root, text="Enter Height (mm):").pack()
height_entry = tk.Entry(root)
height_entry.pack()
submit_button_fov = tk.Button(root, text="Calculate FOV", command=on_submit_fov)
submit_button_fov.pack()

# FOV input
tk.Label(root, text="Enter FOV (m²):").pack()
fov_entry = tk.Entry(root)
fov_entry.pack()
submit_button_height = tk.Button(root, text="Estimate Height", command=on_submit_height)
submit_button_height.pack()

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.pack()

root.mainloop()
