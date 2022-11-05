import numpy as np
from scipy.signal import get_window
import matplotlib.pyplot as plt

freq = 100.1
t = np.arange(0, 2, step=1/1000)
m = t.size
s = np.sin(2 * np.pi * freq * t)



fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.plot(t, s)
ax1.set_title("sinusoid {}hz, {} samples, sampling rate {} Hz".format(freq, m, 1/(t[1] - t[0])))


for window in ['boxcar', 'hamming', 'blackman', 'hanning']:
    n = 4096
    w = np.fft.rfft(s * get_window(window, m), n=n)
    freqs = np.fft.rfftfreq(n, d=t[1] - t[0])
    ax2.plot(freqs, 20*np.log10(np.abs(w)), label=window)
    max_amp=np.array(20*np.log10(np.abs(w)))
    max_amp_index=max_amp.argmax(axis=0)
    print(f"Freq with highest amplitude: {freqs[max_amp_index]}")
# ax2.set_ylim(-60, 60)
# ax2.set_xlim(5, 15)
plt.legend()
plt.tight_layout()
plt.show()
