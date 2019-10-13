import scipy.misc
import matplotlib.pyplot
import os
from utils import DATA_DIR

# Loads the miss_sa image into an array
miss_sa = matplotlib.pyplot.imread(os.path.join(DATA_DIR, 'miss_south_africa.jpg'))
# Plot the miss_sa array
matplotlib.pyplot.subplot(221)
matplotlib.pyplot.imshow(miss_sa)
#Plot the flipped array
matplotlib.pyplot.subplot(222)
matplotlib.pyplot.imshow(miss_sa[:,::-1])
#Plot a slice array
matplotlib.pyplot.subplot(223)
matplotlib.pyplot.imshow(miss_sa[:int(miss_sa.shape[0]/2),:int(miss_sa.shape[1]/2)])
# Apply a mask
mask = miss_sa % 2 == 0
masked_miss_sa = miss_sa.copy()
masked_miss_sa[mask] = 0
matplotlib.pyplot.subplot(224)
matplotlib.pyplot.imshow(masked_miss_sa)
matplotlib.pyplot.show()