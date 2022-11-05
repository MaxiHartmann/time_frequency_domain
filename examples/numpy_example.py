import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-poster')
# sampling rate
sr = 2000
# sampling interval
ts = 1.0/sr
t = np.arange(0,1,ts)

# DC-Value
x = 15

freq = 1.
x += 3*np.sin(2*np.pi*freq*t)

freq = 4
x += np.sin(2*np.pi*freq*t)

freq = 7
x += 0.5* np.sin(2*np.pi*freq*t)

from numpy.fft import fft, ifft

X = fft(x)
N = len(X)
n = np.arange(N)
T = N/sr
freq = n/T

plt.figure(figsize = (12, 6))
plt.subplot(121)

### scale amplitude: everything except DC-part (amp[0]) with 2/N
amplitude = np.abs(X) * 2. / N
amplitude[0] = amplitude[0] / 2.
DC=amplitude[0]
plt.stem(freq, amplitude, 'b', \
         markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
plt.text(0, DC, f'DC={DC}', fontsize=11)
plt.xlim(0, 10)

plt.subplot(122)
plt.plot(t, ifft(X), 'r')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()
