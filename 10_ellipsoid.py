import numpy as np
import matplotlib.pyplot as plt

a = 6378137.0; b = 6356752.314245
degree = np.linspace(0, 360, 90)
radian = np.deg2rad(degree)
x = a*np.cos(radian)
y = b*np.sin(radian)

G = 6.674*pow(10, -11)
m = 5.972*pow(10, 24)
r = np.sqrt(pow(x, 2) + pow(y, 2))
g = (G*m)/pow(r, 2)

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(20, 10))
ax.ticklabel_format(useOffset=False, style='plain')
plt.scatter(x, y, s=100, c=g, cmap='rainbow', marker='o', edgecolor='black')
plt.title('Gravity variation in ellipse model', size=24, fontweight='bold')
plt.xlabel('radius (m)', size=18)
plt.ylabel('radius (m)', size=18)
plt.grid(color='green', linestyle='--', linewidth=2.0)
clb = plt.colorbar()
clb.ax.tick_params(labelsize=18) 
clb.ax.set_ylabel(r'$gravity\ (m\cdotp s^{-2})$', rotation=270, labelpad=50, fontsize=18)
plt.show()