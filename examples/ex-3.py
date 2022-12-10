import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (15,5)

# fig, axs = plt.subplots(2, subplot_kw={'projection': 'polar', 'projection': 'cartesian'})
fig = plt.figure()
ax1 = fig.add_subplot(projection='polar')
ax2 = fig.add_subplot()
plt.show()
