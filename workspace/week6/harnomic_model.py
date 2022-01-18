import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import get_window

import utilFunctions as UF
import sineModel as SM
import harmonicModel as HM

# inputFile = '../../sounds/vignesh.wav'
inputFile = '../../sounds/piano.wav'
# window = 'blackman'
# M = 1201
# N = 2048
# t = -90
# minSineDur = 0.1
# nH = 50
# minf0 = 130
# maxf0 = 300
# f0et = 5
# harmDevSlope = 0.1

# Ns = 512
# H = 128

window = 'hamming',
M = 2047
N = 2048
H = 128
f0et = 5.0
t = -90
minf0 = 230
maxf0 = 290
nH = 5

(fs, x) = UF.wavread(inputFile)
w = get_window(window, M)

# hfreq, hmag, hphase = HM.harmonicModelAnal(
# x, fs, w, N, H, t, nH, minf0, maxf0, f0et, harmDevSlope, minSineDur)
hfreq, hmag, hphase = HM.harmonicModelAnal(
    x, fs, w, N, H, t, nH, minf0, maxf0, f0et, harmDevSlope=0.01, minSineDur=0.0)

numFrames = int(hfreq[:, 0].size)
frmTime = H*np.arange(numFrames)/float(fs)
hfreq[hfreq <= 0] = np.nan

plt.plot(frmTime, hfreq)

plt.show()
