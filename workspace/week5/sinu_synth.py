import utilFunctions as UF
import numpy as np
# np.seterr(divide='ignore', invalid='ignore')

bins = np.array([-4, -3, -2, -1, 0, 1, 2, 3])
X = UF.genBhLobe(bins)

print(X)
