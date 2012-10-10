

# http://docs.scipy.org/doc/scipy/reference/tutorial/ndimage.html#ndimage-ccallbacks
import numpy as np

#from example import shift_function
import example
from scipy.ndimage import geometric_transform

array = np.reshape(np.arange(12).astype(float64),(4,3))
fnc = example.shift_function(0.5)

geometric_transform(array, fnc)


