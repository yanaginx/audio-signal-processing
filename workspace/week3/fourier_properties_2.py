import numpy as np
from scipy.fftpack import fft
import sys
import os
import math
import utilFunctions as UF

M = 501
hM1 = int(math.floor(M+1)/2)
hM2 = int(math.floor(M/2))

(fs, x) = UF.wavread('../../sounds/soprano-E4.wav')
# hamming is the smoothing window, will be discussed next week
x1 = x[5000:5000+M] * np.hamming(M)

N = 1024
hN = int(N/2)
fftbuffer = np.zeros(N)
fftbuffer[:hM1] = x1[hM2:]
fftbuffer[N-hM2:] = x1[:hM2]

X = fft(fftbuffer)
mX = (20*np.log10(abs(X)))[0:hN]
pX = (np.unwrap(np.angle(X)))[0:hN]
