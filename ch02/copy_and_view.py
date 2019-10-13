# This sample cannot work as decribed in the book
# it might be due to some update of the libraries

import scipy.misc
import sys
import matplotlib.pyplot as mp

import os
from utils import DATA_DIR

# Loads the miss_sa image into an array
miss_sa = mp.imread(os.path.join(DATA_DIR, 'miss_south_africa.jpg'))
acopy = miss_sa.copy()
aview = miss_sa.view()
# Plot the Lena array
mp.subplot(221)
mp.imshow(miss_sa)
#Plot the copy
mp.subplot(222)
mp.imshow(acopy)
#Plot the view
mp.subplot(223)
mp.imshow(aview)
# Plot the view after changes
aview.flat = 0
mp.subplot(224)
mp.imshow(aview)
mp.show()