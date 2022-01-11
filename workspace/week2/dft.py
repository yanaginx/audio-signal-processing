import matplotlib.pyplot as plt
import numpy as np

N = 64
k0 = 7
# x = np.exp(1j * 2 * np.pi * k0 / N * np.arange(N))  # complex time signal
x = np.cos(2 * np.pi * k0 / N * np.arange(N))  # real time signal

# DFT sequences
X = np.array([])

nv = np.arange(-N/2, N/2)  # time index
kv = np.arange(-N/2, N/2)  # frequency index


for k in kv:
    s = np.exp(1j*2*np.pi * k / N * nv)
    X = np.append(X, sum(x*np.conjugate(s)))

y = np.array([])
for n in nv:
    s = np.exp(1j*2*np.pi * n / N * kv)
    y = np.append(y, 1.0/N*sum(X*s))


# DFT
plt.plot(kv, abs(X))
plt.axis([-N/2, N/2-1, 0, N])
plt.show()

# Inverse DFT
plt.plot(nv, y)
plt.axis([-N/2, N/2-1, -1, 1])
plt.show()
