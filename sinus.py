import numpy as np
import matplotlib.pyplot as plt

import cmath
def compute_dft_complex(input):
	n = len(input)
	output = []
	for k in range(n):  # For each output element
		s = complex(0)
		for t in range(n):  # For each input element
			angle = 2j * cmath.pi * t * k / n
			s += input[t] * cmath.exp(-angle)
		output.append(s)
	return output


def DFT_slow(x):
    """Compute the discrete Fourier Transform of the 1D array x"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape(N,1)
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

pi=np.pi

x=np.linspace(-2*pi, 2*pi, 100)
y=np.sin(x)

fig, axs = plt.subplots(2)
axs[0].plot(x,y, marker='>')

# real = DFT_slow(x)
# print(real.real)
# axs[1].plot(x,DFT_slow(x).real, marker='v')
axs[1].plot(x, compute_dft_complex(x), marker='v')
plt.show()
