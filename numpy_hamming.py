import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, fftshift

window = np.hamming(51)
plt.plot(window, label='hamming')

window = np.hanning(51)
plt.plot(window, label='hanning')

window = np.bartlett(51)
plt.plot(window, label='bartlett')

window = np.blackman(51)
plt.plot(window, label='blackman')

beta = 500
window = np.kaiser(51, beta)
plt.plot(window, label=f'kaiser({beta})')

plt.title("Windows")
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.legend()
plt.show()
