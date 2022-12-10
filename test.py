import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# test numpy.fft.fft

# generate synthesis
t = np.linspace(0, 1, 1001)
print(t)

f1 = 10
f2 = 2 * f1
f3 = 3 * f1
a1 = 1
a2 = 1
a3 = 1
om1 = 2 * np.pi * f1
om2 = 2 * np.pi * f2
om3 = 2 * np.pi * f3

s = 5 + a1 * np.sin(om1 * t) + a2 * np.sin(om2 * t) + a3 * np.sin(om3 * t)

plt.plot(t, s)
plt.show()
