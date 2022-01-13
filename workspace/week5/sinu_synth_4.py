import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import get_window
import dftModel as DFT
import utilFunctions as UF
from scipy.signal import blackmanharris, triang
from scipy.fftpack import ifft


(fs, x) = UF.wavread('../../sounds/oboe-A4.wav')
Ns = 512
hNs = int(Ns/2)
H = int(Ns/4)
M = 511
t = -70
w = get_window('hamming', M, fftbins=False) if M % 2 else get_window(
    'hamming', M)
x1 = x[int(.8*fs):int(.8*fs+M)]
mX, pX = DFT.dftAnal(x1, w, Ns)
ploc = UF.peakDetection(mX, t)
iploc, ipmag, ipphase = UF.peakInterp(mX, pX, ploc)
ipfreq = fs*iploc/float(Ns)
Y = UF.genSpecSines_p(ipfreq, ipmag, ipphase, Ns, fs)
y = np.real(ifft(Y))

sw = np.zeros(Ns)
ow = triang(Ns/2)
sw[hNs-H:hNs+H] = ow
bh = blackmanharris(Ns)
bh = bh / sum(bh)
sw[hNs-H:hNs+H] = sw[hNs-H:hNs+H] / bh[hNs-H:hNs+H]

yw = np.zeros(Ns)
yw[:hNs-1] = y[hNs+1:]
yw[hNs-1:] = y[:hNs+1]
yw *= sw

freqaxis = fs*np.arange(Ns/2+1)/float(Ns)
plt.plot(freqaxis, mX)
plt.plot(fs*iploc / Ns, ipmag, marker='x', linestyle='')
plt.show()
