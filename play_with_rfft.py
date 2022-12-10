import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#### INPUTS ####
time_1 = 0
time_2 = 2
N = 1024
f = 30
a = 8
################

fs = N / (time_2 - time_1)
t = np.linspace(time_1, time_2, N)
omega = 2 * np.pi * f
s = a * np.sin(omega*t)
# s = s - np.mean(s)

fig, (ax1, ax2)  = plt.subplots(2)

ax1.plot(t, s)
ax1.set_xlabel('time [s]')
ax1.set_ylabel('pressure [Pa]')

S = np.fft.rfft(s)
amp = np.abs(S) * 2 / N
n = np.arange(0, int(N/2+1))
f_nyq = fs / 2
freq = n * fs / N
ax2.stem(freq, amp, markerfmt=" ")
ax2.set_xlim(0, N/2 + 1)
ax2.set_yscale('linear')
ax2.set_ylim(0, a)
ax2.set_xlabel('Frequency [Hz]')
ax2.set_ylabel('Intensity [Pa]')

print("--------------------------------------")
print(f" Orig. Signal: s = {a}sin(2pi * {f}hz * t)")
print("--------------------------------------")
print(f" Period         = {time_2 - time_1} s")
print(f" Sampling rate  = {fs} Hz")
print(f" Sampling point = {N} ")
print(f" Nyquist-Freq   = {f_nyq} Hz")

threshold = 0.1 * a
amps_iloc = np.argwhere(amp > threshold )
print(f"Frequencies with relevant amplitude > {threshold}:")
for i in amps_iloc[0]:
    print(f"freq={freq[i]:0.4e}, amp={amp[i]:0.4e}, freq_err={f - freq[i]:0.4e}, amp_err={a - amp[i]:0.4e}")

fig.tight_layout()
# plt.savefig("bild_2.png")

plt.show()
