import numpy as np
from scipy.signal import triang
from scipy.fftpack import fft

x = triang(15)  # 15 samples
X = fft(x)
mX = abs(X)
pX = np.angle(X)
