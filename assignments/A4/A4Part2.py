from scipy.fftpack.basic import fft
import utilFunctions as UF
import stft
import os
import sys
import numpy as np
import math
from scipy.signal import get_window
import matplotlib.pyplot as plt
from loadTestCases import load
sys.path.append(os.path.join(os.path.dirname(
    os.path.realpath(__file__)), '../../software/models/'))
eps = np.finfo(float).eps


"""
A4-Part-2: Measuring noise in the reconstructed signal using the STFT model 

Write a function that measures the amount of noise introduced during the analysis and synthesis of a 
signal using the STFT model. Use SNR (signal to noise ratio) in dB to quantify the amount of noise. 
Use the stft() function in stft.py to do an analysis followed by a synthesis of the input signal.

A brief description of the SNR computation can be found in the pdf document (A4-STFT.pdf, in Relevant 
Concepts section) in the assignment directory (A4). Use the time domain energy definition to compute
the SNR.

With the input signal and the obtained output, compute two different SNR values for the following cases:

1) SNR1: Over the entire length of the input and the output signals.
2) SNR2: For the segment of the signals left after discarding M samples from both the start and the 
end, where M is the analysis window length. Note that this computation is done after STFT analysis 
and synthesis.

The input arguments to the function are the wav file name including the path (inputFile), window 
type (window), window length (M), FFT size (N), and hop size (H). The function should return a python 
tuple of both the SNR values in decibels: (SNR1, SNR2). Both SNR1 and SNR2 are float values. 

Test case 1: If you run your code using piano.wav file with 'blackman' window, M = 513, N = 2048 and 
H = 128, the output SNR values should be around: (67.57748352378475, 304.68394693221649).

Test case 2: If you run your code using sax-phrase-short.wav file with 'hamming' window, M = 512, 
N = 1024 and H = 64, the output SNR values should be around: (89.510506656299285, 306.18696700251388).

Test case 3: If you run your code using rain.wav file with 'hann' window, M = 1024, N = 2048 and 
H = 128, the output SNR values should be around: (74.631476225366825, 304.26918192997738).

Due to precision differences on different machines/hardware, compared to the expected SNR values, your 
output values can differ by +/-10dB for SNR1 and +/-100dB for SNR2.
"""


def computeSNR(inputFile, window, M, N, H):
    """
    Input:
            inputFile (string): wav file name including the path 
            window (string): analysis window type (choice of rectangular, triangular, hanning, hamming, 
                    blackman, blackmanharris)
            M (integer): analysis window length (odd positive integer)
            N (integer): fft size (power of two, > M)
            H (integer): hop size for the stft computation
    Output:
            The function should return a python tuple of both the SNR values (SNR1, SNR2)
            SNR1 and SNR2 are floats.
    """
    # your code here
    (fs, x) = UF.wavread(inputFile)
    w = get_window(
        window, M, fftbins=False) if M % 2 else get_window(window, M)
    y = stft.stft(x, w, N, H)
    input_size = len(x)

    noise = abs(np.subtract(x, y))
    e_signal = sum(xn*xn for xn in x)
    e_noise = sum(nn*nn for nn in noise)
    SNR1 = 10*np.log10(e_signal/e_noise)

    trimmed_signal = x[M:input_size-M]
    trimmed_output = y[M:input_size-M]
    trimmed_noise = abs(np.subtract(trimmed_signal, trimmed_output))
    e_trimmed_signal = sum(xn*xn for xn in trimmed_signal)
    e_trimmed_noise = sum(nn*nn for nn in trimmed_noise)
    SNR2 = 10*np.log10(e_trimmed_signal/e_trimmed_noise)

    return(SNR1, SNR2)


res = load(2, 2)
output = computeSNR(**res['input'])
print(output)
print(res['output'])
