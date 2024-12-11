import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

# New dimensions for the sketched and computed GLS paths
sketched_length = 335
sketched_breadth = 318
computed_length = 323
computed_breadth = 312

# New area for the expected square and its side length calculation
new_area_expected_square = 0.08  # in square meters
new_area_expected_square_mm = new_area_expected_square * 1000000  # convert to square mm
new_expected_square_side = math.sqrt(new_area_expected_square_mm)

# Create figure and axes
fig, ax = plt.subplots()

# Add the new rectangles and the expected square to the axes
sketched_rect = patches.Rectangle((0, 0), sketched_length, sketched_breadth, linewidth=1, edgecolor='b', facecolor='none', label='Sketched GLS Path (335x318 mm)')
computed_rect = patches.Rectangle((0, 0), computed_length, computed_breadth, linewidth=1, edgecolor='r', facecolor='none', label='Computed GLS Path (323x312 mm)')
expected_square = patches.Rectangle((0, 0), new_expected_square_side, new_expected_square_side, linewidth=1, edgecolor='g', facecolor='none', label='Expected Path for FOV (Approx. 282.84x282.84 mm)')

ax.add_patch(sketched_rect)
ax.add_patch(computed_rect)
ax.add_patch(expected_square)

# Labeling inside the plot
ax.text(sketched_length/2, sketched_breadth/2, '335x318 mm', horizontalalignment='center', verticalalignment='center', color='b')
ax.text(computed_length/2, computed_breadth/2, '323x312 mm', horizontalalignment='center', verticalalignment='center', color='r')
ax.text(new_expected_square_side/2, new_expected_square_side/2, f'{new_expected_square_side:.2f} mm²', horizontalalignment='center', verticalalignment='center', color='g')

# Set limits, labels, and title
ax.set_xlim(0, max(sketched_length, computed_length, new_expected_square_side) + 50)
ax.set_ylim(0, max(sketched_breadth, computed_breadth, new_expected_square_side) + 50)
ax.set_xlabel('Length (mm)')
ax.set_ylabel('Breadth (mm)')
ax.set_title('Comparative Visualization of Sketched and Computed GLS Paths with Expected Path for a FOV of 0.08 m²')

# Add a legend outside the plot
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1))

# Show the plot
plt.show()
