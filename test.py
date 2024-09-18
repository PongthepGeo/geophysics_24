import numpy as np
import matplotlib.pyplot as plt
#-----------------------------------------------------------------------------------------#

def gravitational_field_magnitude_2(rho, R, x_obs, y_obs, x_sphere, y_sphere, G):
    M = rho * (4 / 3) * np.pi * R**3  # Mass of the sphere
    r_squared = (x_obs - x_sphere)**2 + (y_obs - y_sphere)**2  # Distance squared
    g_magnitude = G * M / r_squared
    return g_magnitude

def plot_gravitational_field(observation_points, observed_g, title, label, color, output_filename, output_dir='figure_out'):
    plt.figure()
    x_observed = np.array([pt[0] for pt in observation_points])
    plt.scatter(x_observed, observed_g, color=color, label=label, s=20, edgecolors='black')
    plt.xlabel('Observation Point X (m)')
    plt.ylabel(r'$|\mathbf{g}|$')
    plt.title(title)
    plt.legend()
    plt.grid(True, linestyle='--')
    plt.savefig(f'{output_dir}/{output_filename}.svg', format='svg',
                bbox_inches='tight', transparent=True, pad_inches=0.0)
    plt.show()

def plot_sphere(sphere_name, sphere, observation_points, observed_g, output_dir='figure_out'):
    title = f'Gravitational Field Magnitude due to {sphere_name}'
    label = sphere_name
    color = sphere['color']
    output_filename = f'sphere_{sphere_name}'
    plot_gravitational_field(observation_points, observed_g, title, label, color, output_filename, output_dir)

def plot_total_and_individual_fields(spheres, observation_points, total_g, individual_g, output_dir='figure_out'):
    plt.figure()
    x_observed = np.array([pt[0] for pt in observation_points])
    
    for sphere_name, observed_g in individual_g.items():
        plt.scatter(x_observed, observed_g, color=spheres[sphere_name]['color'], label=sphere_name, s=20, edgecolors='black')
    
    plt.scatter(x_observed, total_g, marker='x', color='cyan', label='Total Gravity', s=20)
    plt.xlabel('Observation Point X (m)')
    plt.ylabel(r'$|\mathbf{g}|$')
    plt.title('Total Gravitational Field Magnitude and Individual Contributions')
    plt.legend()
    plt.grid(True, linestyle='--')
    plt.savefig(f'{output_dir}/total_and_individual_fields.svg', format='svg',
                bbox_inches='tight', transparent=True, pad_inches=0.0)
    plt.show()

G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
spheres = {
	'Sphere a': {'x': 15.22, 'y': 40.47, 'R': 10.1, 'rho': 3441, 'color': 'blue'}
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
        g = gravitational_field_magnitude_2(sphere['rho'], sphere['R'], x_obs, y_obs, sphere['x'], sphere['y'], G)
        observed_g.append(g)
    individual_g[sphere_name] = observed_g
    total_g += np.array(observed_g)
    plot_sphere(sphere_name, sphere, observation_points, observed_g)
plot_total_and_individual_fields(spheres, observation_points, total_g, individual_g)

#-----------------------------------------------------------------------------------------#