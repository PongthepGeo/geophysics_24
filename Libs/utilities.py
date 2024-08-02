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

def simple_harmonic_plot(distance, cosine_values, sine_values):
    plt.plot(distance, cosine_values)
    plt.plot(distance, sine_values)
    plt.xlabel('Distance (m)')
    plt.ylabel('Amplitude')
    plt.legend(['Cosine', 'Sine'], loc='upper right')
    plt.title('Cosine and Sine Waves')
    plt.savefig('figure_out/' + 'simple_har.png', format='png', bbox_inches='tight', transparent=True, pad_inches=0)
    plt.show()

#-----------------------------------------------------------------------------------------#