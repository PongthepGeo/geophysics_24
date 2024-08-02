import numpy as np
import matplotlib.pyplot as plt
# Define the frequency of the cosine wave
frequency = 5
# Generate a time array from 0 to 1 second, with 500 points
time = np.linspace(0, 1, 500)
# Calculate the angle for the cosine function
x = 2 * np.pi * frequency * time
# Compute the cosine values
cosine_values = np.cos(x)

plt.plot(time, cosine_values)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Cosine Wave with Frequency = 5 Hz')
plt.show()