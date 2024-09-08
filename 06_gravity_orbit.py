#-----------------------------------------------------------------------------------------#
import sys
sys.path.append('./Libs')
import utilities as U
#-----------------------------------------------------------------------------------------#
import numpy as np
import matplotlib.pyplot as plt
#-----------------------------------------------------------------------------------------#

# Constants
G = 6.67430e-11  # gravitational constant in m^3 kg^-1 s^-2
M = 5.972e24     # mass of the Earth in kg

# Positions (x, y) in meters
positions = {
    "Earth's Surface": (4.504e6, 4.504e6),
    "Mountain Average": (-4.506e6, 4.506e6),
    "Mean Satellite Orbit": (3.286e6, 5.686e6),
    "Moon Orbit": (3.326e8, -1.922e8)
}

#-----------------------------------------------------------------------------------------#

radii = []
magnitudes = []
colors = ['blue', 'green', 'red', 'purple']
for name, (x, y) in positions.items():
    radius, magnitude = U.gravitational_field_magnitude(x, y, G, M)
    radii.append(radius)
    magnitudes.append(magnitude)

#-----------------------------------------------------------------------------------------#

labels = list(positions.keys())
U.plot_gravitational_field(radii, magnitudes, colors, labels)

#-----------------------------------------------------------------------------------------#