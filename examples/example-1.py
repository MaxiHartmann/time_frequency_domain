import matplotlib.pyplot as plt
import numpy as np
import math

# Amplitudes
A0 = 1000
A1 = 150
A2 = 100

# frequencies
f1 = 745
f2 = 11920

N = 501

# time
t = np.linspace(0, 0.005, N)
p = A0 + A1 * np.cos(2*np.pi * f1 * t) + A2 * np.cos(2 * np.pi * f2 * t)



fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))
ax1.plot(t, p, color='red')
ax1.set_xlabel('Pressure (Pa)')
ax1.set_ylabel('Time (s)')


# duration
T1 = 1 / f1
T2 = 1 / f2
print("f1 = {:.03f}".format(f1))
print("f2 = {:.03f}".format(f2))
print("Greatest common divisor of f1 and f2:")
print("gcd = {}".format(math.gcd(f1, f2)))
print("T1 = {:.03e} s".format(T1))
print("T2 = {:.03e} s".format(T2))
ax1.vlines(0, A0-500, A0+500)
ax1.vlines(T1, A0-500, A0+500, color='green')
ax1.vlines(T2, A0-500, A0+500, color='blue')


pf = np.fft.fft(p)

##
# m = 2
# N = 2**m
# dt = 2 * T
#
N = int(len(pf)/2+1)

dt = t[1] - t[0]
fa = 1.0/dt # scan frequency
print('dt=%.5fs (Sample Time)' % dt)
print('fa=%.2fHz (Frequency)' % fa)

tf = np.linspace(0, fa/2, N, endpoint=True)

ax2.plot(tf, np.abs(pf[:N]))
plt.show()


