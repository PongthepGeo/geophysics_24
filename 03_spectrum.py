#-----------------------------------------------------------------------------------------#
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
#-----------------------------------------------------------------------------------------#
params = {
	'savefig.dpi': 300,  
	'figure.dpi' : 300,
	'axes.labelsize':12,  
	'axes.titlesize':12,
	'axes.titleweight': 'bold',
	'legend.fontsize': 10,
	'xtick.labelsize':10,
	'ytick.labelsize':10,
	'font.family': 'serif',
	'font.serif': 'Times New Roman'
}
matplotlib.rcParams.update(params)
#-----------------------------------------------------------------------------------------#

A = 1  # Base Amplitude
lambda_ = 2  # Base Wavelength in meters
T = 1  # Base Period in seconds
phi = np.pi / 4  # Base Phase shift in radians
x = np.linspace(0, 10, 500)  # Distance from 0 to 10 meters
t = 0  # Initial time (can be changed to observe wave at different times)
waveform = np.zeros_like(x)
num_spectra = 5

plt.figure()

for i in range(num_spectra):
    freq = i + 1
    amplitude = A / (i + 1)  # Reduce amplitude for higher frequencies
    phase_shift = phi * np.random.rand()  # Random phase shift
    y = amplitude * np.cos(2 * np.pi * freq * x / lambda_ - 2 * np.pi * t / T + phase_shift)
    plt.plot(x, y, linestyle='--', linewidth=0.5, label=f'harmonic {i+1}')
    waveform += y

#-----------------------------------------------------------------------------------------#

plt.plot(x, waveform, 'k', label='combined waves', linewidth=2)
plt.xlabel('Distance (m)')
plt.ylabel('Amplitude')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.savefig('figure_out/' + 'spectrum.png', format='png', bbox_inches='tight', transparent=True, pad_inches=0.05)
plt.show()

#-----------------------------------------------------------------------------------------#