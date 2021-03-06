# Two way mismatch algorithm
import numpy as np
import utilFunctions as UF
import dftModel as DFT
import matplotlib.pyplot as plt
from scipy.signal import get_window


def TWM_Errors(pfreq, pmag, f0c):
    """
    Two-way mismatch algorithm for f0 detection (by Beauchamp&Maher)
    [better to use the C version of this function: UF_C.twm]
    pfreq, pmag: peak frequencies in Hz and magnitudes,
    f0c: frequencies of f0 candidates
    returns f0, f0Error: fundamental frequency detected and its error
    """

    p = 0.5                                          # weighting by frequency value
    # weighting related to magnitude of peaks
    q = 1.4
    # scaling related to magnitude of peaks
    r = 0.5
    rho = 0.33                                       # weighting of MP error
    Amax = max(pmag)                                 # maximum peak magnitude
    maxnpeaks = 10                                   # maximum number of peaks used
    harmonic = np.matrix(f0c)
    ErrorPM = np.zeros(harmonic.size)                # initialize PM errors
    MaxNPM = min(maxnpeaks, pfreq.size)
    for i in range(0, MaxNPM):                      # predicted to measured mismatch error
        difmatrixPM = harmonic.T * np.ones(pfreq.size)
        difmatrixPM = abs(difmatrixPM - np.ones((harmonic.size, 1))*pfreq)
        FreqDistance = np.amin(difmatrixPM, axis=1)    # minimum along rows
        peakloc = np.argmin(difmatrixPM, axis=1)
        Ponddif = np.array(FreqDistance) * (np.array(harmonic.T)**(-p))
        PeakMag = pmag[peakloc]
        MagFactor = 10**((PeakMag-Amax)/20)
        ErrorPM = ErrorPM + (Ponddif + MagFactor*(q*Ponddif-r)).T
        harmonic = harmonic+f0c

    ErrorMP = np.zeros(harmonic.size)                # initialize MP errors
    MaxNMP = min(maxnpeaks, pfreq.size)
    for i in range(0, f0c.size):                    # measured to predicted mismatch error
        nharm = np.round(pfreq[:MaxNMP]/f0c[i])
        nharm = (nharm >= 1)*nharm + (nharm < 1)
        FreqDistance = abs(pfreq[:MaxNMP] - nharm*f0c[i])
        Ponddif = FreqDistance * (pfreq[:MaxNMP]**(-p))
        PeakMag = pmag[:MaxNMP]
        MagFactor = 10**((PeakMag-Amax)/20)
        ErrorMP[i] = sum(MagFactor * (Ponddif + MagFactor*(q*Ponddif-r)))

    Error = (ErrorPM[0]/MaxNPM) + (rho*ErrorMP/MaxNMP)  # total error

    return Error


(fs, x) = UF.wavread('../../sounds/sawtooth-440.wav')
N = 1024
M = 601
t = -60
minf0 = 50
maxf0 = 2000

hN = int(N/2)
hM = int((M+1)/2)

w = get_window('hamming', M, False) if M % 2 else get_window(
    'hamming', M)
start = int(.8*fs)

x1 = x[start:start+M]
mX, pX = DFT.dftAnal(x1, w, N)
ploc = UF.peakDetection(mX, t)
iploc, ipmag, ipphase = UF.peakInterp(mX, pX, ploc)
ipfreq = fs * iploc/N
f0c = np.argwhere((ipfreq > minf0) & (ipfreq < maxf0))[:, 0]
f0cf = ipfreq[f0c]
f0Errors = TWM_Errors(ipfreq, ipmag, f0cf)

freqaxis = fs*np.arange(N/2+1)/float(N)
plt.plot(freqaxis, mX)
plt.plot(ipfreq, ipmag, marker='x', linestyle='')
plt.show()
