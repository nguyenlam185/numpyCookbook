# There is a minor modification from the book
# due to the depreciation of luna() function
# in the scipy library

import scipy.misc
import sys
import matplotlib.pyplot as mp
import numpy.testing
import numpy as np
import os
from utils import DATA_DIR

# This script resizes the miss_sa image from Scipy.
if(len(sys.argv) != 3):
    print ('Usage python %s yfactor xfactor' % (sys.argv[0]))
    sys.exit()

# Loads the miss_sa image into an array
miss_sa = mp.imread(os.path.join(DATA_DIR, 'miss_south_africa.jpg'))
print("Miss SA shape: " + str(miss_sa.shape))
#miss_sa's dimensions
MISS_Y = 1200
MISS_X = 799
#Check the shape of the miss_sa array
numpy.testing.assert_equal((MISS_Y, MISS_X, 3), miss_sa.shape)
# Get the resize factors
yfactor = float(sys.argv[1])
xfactor = float(sys.argv[2])
# Resize the miss_sa array
resized = miss_sa.repeat(yfactor, axis=0).repeat(xfactor, axis=1)
#Check the shape of the resized array
numpy.testing.assert_equal((yfactor * MISS_Y, xfactor * MISS_X, 3), resized.shape)
# Plot the miss_sa array
mp.subplot(211)
mp.imshow(miss_sa)
#Plot the resized array
mp.subplot(212)
mp.imshow(resized)
mp.show()