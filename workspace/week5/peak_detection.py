import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import get_window
import sys
import os
import dftModel as DFT
import utilFunctions as UF


(fs, x) = UF.wavread('../../sounds/sine-440.wav')
M = 501
N = 2048
t = -20
w = get_window('hamming', M, fftbins=False) if M % 2 else get_window(
    'hamming', M)
x1 = x[int(.8*fs): int(.8*fs+M)]
mX, pX = DFT.dftAnal(x1, w, N)
ploc = UF.peakDetection(mX, t)
pmag = mX[ploc]
# parabola interpolation
iploc, ipmag, ipphase = UF.peakInterp(mX, pX, ploc)

freqaxis = fs * np.arange(N/2+1)/float(N)
plt.plot(freqaxis, mX)
# plt.plot(fs * ploc / float(N), pmag, marker='x', linestyle='')
plt.plot(fs * iploc / float(N), ipmag, marker='x', linestyle='')

plt.show()
