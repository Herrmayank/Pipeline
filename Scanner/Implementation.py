import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

# Define the rectangles and their dimensions
rect1_length = 410
rect1_breadth = 470
rect2_length = 455
rect2_breadth = 400

# Define the area for the new square and calculate its side length
area_expected_square = 0.140  # in square meters
area_expected_square_mm = area_expected_square * 1000000  # convert to square mm
expected_square_side = math.sqrt(area_expected_square_mm)

# Create figure and axes
fig, ax = plt.subplots()

# Add the rectangles and the expected square to the axes
rect1 = patches.Rectangle((0, 0), rect1_length, rect1_breadth, linewidth=1, edgecolor='r', facecolor='none', label='Computed GLS Path (410x470 mm)')
rect2 = patches.Rectangle((0, 0), rect2_length, rect2_breadth, linewidth=1, edgecolor='b', facecolor='none', label='Sketched GLS Path (455x400 mm)')
expected_square = patches.Rectangle((0, 0), expected_square_side, expected_square_side, linewidth=1, edgecolor='g', facecolor='none', label='Expected Path for FOV (Approx. 374.17x374.17 mm)')

ax.add_patch(rect1)
ax.add_patch(rect2)
ax.add_patch(expected_square)

# Labeling inside the plot
ax.text(rect1_length/2, rect1_breadth/2, '410x470 mm', horizontalalignment='center', verticalalignment='center', color='r')
ax.text(rect2_length/2, rect2_breadth/2, '455x400 mm', horizontalalignment='center', verticalalignment='center', color='b')
ax.text(expected_square_side/2, expected_square_side/2, f'{expected_square_side:.2f} mm²', horizontalalignment='center', verticalalignment='center', color='g')

# Set limits, labels, and title with the specified wording
ax.set_xlim(0, max(rect1_length, rect2_length, expected_square_side) + 50)
ax.set_ylim(0, max(rect1_breadth, rect2_breadth, expected_square_side) + 50)
ax.set_xlabel('Length (mm)')
ax.set_ylabel('Breadth (mm)')
ax.set_title('Overlay of the Computed and Sketched GLS Paths with the Expected Path for a FOV of 0.140 m² for h=448mm')

# Add a legend outside the plot
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1))

# Show the plot
plt.show()
