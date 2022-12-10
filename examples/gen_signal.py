import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# sampling rate
sr = 50       # [hz]
# sampling interval
ts = 1.0 / sr   # [s]
t = np.arange(0, 1, ts) # [s]

f1 = 10 # [hz]
f2 = 15 # [hz]
f3 = 20 # [hz]
amp1 = 10
amp2 = 20
amp3 = 30

s_0 = 90000
s_1 = amp1 * np.sin(2 * np.pi * t * f1)
s_2 = amp2 * np.sin(2 * np.pi * t * f2)
s_3 = amp3 * np.sin(2 * np.pi * t * f3)

signal = s_0 + s_1 + s_2 + s_3

### FFT
# N: number of entries in signal - here equal to sampling rate
# T: ratio of number of entries and sampling rate - here 1
N = len(signal)
T = N / sr
n = np.arange(N)
freq = n / T

spec = np.fft.fft(signal)
amplitude = np.abs(spec) * 2. / N
DC = amplitude[0] / 2.
amplitude[0] = 0

### Plotting
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(t, signal, 'r', label='original')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Amplitude')
ax1.plot(t, np.fft.ifft(spec), '--', label='ifft')

ax2.stem(freq, amplitude, 'b', markerfmt=" ", basefmt="-b", label='fft')
ax2.set_xlabel('Freq (Hz)')
ax2.set_ylabel('FFT Amplitude |X(freq)|')
ax2.text(0, max(amplitude)*0.9, f'DC={DC}', fontsize=11)
ax2.set_xlim(0, max(freq)/2.)
plt.tight_layout()
plt.show()
