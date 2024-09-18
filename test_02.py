#-----------------------------------------------------------------------------------------#
import sys
sys.path.append('./Libs')
import utilities as U
#-----------------------------------------------------------------------------------------#
import numpy as np
import matplotlib.pyplot as plt
#-----------------------------------------------------------------------------------------#

G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
spheres = {
    'Sphere a y=40.47 ': {'x': 15.22, 'y': 40.47, 'R': 10.1, 'rho': 3441, 'color': 'blue'},
	'Sphere a y=20': {'x': 15.22, 'y': 20, 'R': 10.1, 'rho': 3441, 'color': 'red'},
	
}

#-----------------------------------------------------------------------------------------#

observed_y = 10
observation_points = [(observed_x, observed_y) for observed_x in range(-70, 120, 5)]
# Initialize a list to store the total gravitational field
total_g = np.zeros(len(observation_points))
individual_g = {sphere_name: [] for sphere_name in spheres.keys()}

#-----------------------------------------------------------------------------------------#

for sphere_name, sphere in spheres.items():
    observed_g = []
    for x_obs, y_obs in observation_points:
        g = U.gravitational_field_magnitude_2(sphere['rho'], sphere['R'], x_obs, y_obs, sphere['x'], sphere['y'], G)
        observed_g.append(g)
    individual_g[sphere_name] = observed_g
    total_g += np.array(observed_g)
    U.plot_sphere(sphere_name, sphere, observation_points, observed_g)
U.plot_total_and_individual_fields(spheres, observation_points, total_g, individual_g)

#-----------------------------------------------------------------------------------------#