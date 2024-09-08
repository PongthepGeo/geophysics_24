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

density_map = np.load('data_out/density_map.npy')

#-----------------------------------------------------------------------------------------#

G = 6.67430e-11  # m^3 kg^-1 s^-2
n_y, n_x = density_map.shape  # Get the shape of the density map (height, width)
x_obs_points = np.arange(0, n_x, 5)  # Observation points along the x-axis, skipping every 5 pixels
y_obs = 0  # Observation is along the x-axis (cross-section)
# Create arrays for pixel coordinates assuming (0, 0) is the top-left corner
x_pixels = np.arange(n_x)  # x coordinates of the pixels
y_pixels = np.arange(n_y)  # y coordinates of the pixels
X, Y = np.meshgrid(x_pixels, y_pixels)  # Grid of pixel coordinates
# Flatten the density map to create the density vector m_rho
m_rho = density_map.flatten()
# Initialize an array to store the gravitational effects for all observation points
gravity_profile = np.zeros_like(x_obs_points, dtype=float)

#-----------------------------------------------------------------------------------------#

# Compute the gravitational effect at each observation point along the x-axis
for obs_idx, x_obs in enumerate(x_obs_points):
    # Initialize the gravity kernel matrix A for this observation point
    A = np.zeros((1, n_x * n_y))
    # Populate the gravity kernel matrix A for the current observation point
    # NOTE the code processes rows first and then columns, it is row-major. 
    for i in range(n_y):
        for j in range(n_x):
            # Position of the pixel (x_j, y_i) and its distance to the observation point
            x_pixel = X[i, j]  # x-coordinate of the pixel
            y_pixel = Y[i, j]  # y-coordinate of the pixel
            # Distance between the pixel and the observation point (on the x-axis, y_obs = 0)
            r = np.sqrt((x_obs - x_pixel)**2 + (y_obs - y_pixel)**2)
            # Avoid division by zero at the observation point
            if r == 0:
                A[0, i * n_x + j] = 0  
            else:
                # Gravitational prism kernel for the pixel (x_j, y_i)
                A[0, i * n_x + j] = -G * (y_pixel * np.log(x_pixel + r) - x_pixel * np.log(y_pixel + r)) / r**2
    # Compute the gravitational effect g_z = A * m_rho for the current observation point
    g_z = np.dot(A, m_rho)
    # Store the result in the gravity profile array
    gravity_profile[obs_idx] = g_z[0]

#-----------------------------------------------------------------------------------------#

# U.plot_model_kernel(density_map, x_obs_points, gravity_profile, output_dir='figure_out')
U.plot_density_model(density_map, output_dir='figure_out')
U.plot_gravitational_profile(x_obs_points, gravity_profile, output_dir='figure_out')

#-----------------------------------------------------------------------------------------#