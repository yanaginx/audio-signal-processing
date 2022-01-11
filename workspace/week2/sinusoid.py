import matplotlib.pyplot as plt
import numpy as np

# Complex sine wave
N = 500
k = 3
n = np.arange(-N/2, N/2)
s = np.exp(1j * 2 * np.pi * k * n / N)

# plt.plot(n, np.real(s))  # real part of the complex sine
plt.plot(n, np.imag(s))  # imaginary part of the complex sine
plt.axis([-N/2, N/2-1, -1, 1])
plt.xlabel('n')
plt.ylabel('Amplitude')

plt.show()

# A = .8
# f0 = 1000
# phi = np.pi/2
# fs = 44100
# t = np.arange(-0.002, 0.002, 1.0/fs)  # 1/fs = sampling period
# x = A*np.cos(2*np.pi * f0 * t + phi)

# plt.plot(t, x)
# plt.axis([-.002, .002, -.8, .8])
# plt.xlabel('time')
# plt.ylabel('Amplitude')

# plt.show()
