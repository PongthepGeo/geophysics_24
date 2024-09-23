#-----------------------------------------------------------------------------------------#
import sys
sys.path.append('./Libs')
import utilities as U
#-----------------------------------------------------------------------------------------#
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
#-----------------------------------------------------------------------------------------#

# img = Image.open('dataset/model.png')
img = Image.open('dataset/test.png')
output_dir = 'data_out' # save as npy

#-----------------------------------------------------------------------------------------#

img_array = np.array(img)
unique_colors = np.unique(img_array[:, :, :3].reshape(-1, 3), axis=0)  # Only use RGB
# Assign random densities between 3000 and 4000 for each unique color
np.random.seed(42)  # For reproducibility
color_to_density = {tuple(color): np.random.uniform(3000, 4000) for color in unique_colors}
density_map = np.zeros(img_array.shape[:2])

#-----------------------------------------------------------------------------------------#

# Map the colors in the image to the random densities
for i in range(img_array.shape[0]):
    for j in range(img_array.shape[1]):
        pixel_color = tuple(img_array[i, j, :3])  # Get the RGB color of the pixel
        if pixel_color in color_to_density:
            density_map[i, j] = color_to_density[pixel_color]

#-----------------------------------------------------------------------------------------#

U.plot_density(img_array, density_map, output_dir='figure_out')
os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists
np.save(f'{output_dir}/density_map.npy', density_map)  # Save the density map
print(f'Density map saved in {output_dir}/density_map.npy')

#-----------------------------------------------------------------------------------------#