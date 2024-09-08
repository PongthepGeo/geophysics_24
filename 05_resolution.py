#-----------------------------------------------------------------------------------------#
import sys
sys.path.append('./Libs')
import utilities as U
#-----------------------------------------------------------------------------------------#
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.ndimage import gaussian_filter
#-----------------------------------------------------------------------------------------#

image = Image.open('/home/pongthep/Downloads/pin_02.png')
image = np.asarray(image)
image = image[:, :, 0] # show only the first channel
print(image.shape)
blur = gaussian_filter(image, sigma=50)

#-----------------------------------------------------------------------------------------#

U.plot_resolution(image, blur)

#-----------------------------------------------------------------------------------------#