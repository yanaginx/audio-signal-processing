import numpy as np
import matplotlib.pyplot as plt
import os
import sys
from scipy.fftpack.basic import fft
from scipy.signal import get_window
import utilFunctions as UF
import stft as STFT

inputFile = '../../sounds/flute-A4.wav'
window = 'hamming'
M = 801
N = 1024
H = 400

(fs, x) = UF.wavread(inputFile)

w = get_window(window, M, fftbins=False)

mX, pX = STFT.stftAnal(x, w, N, H)
