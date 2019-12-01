import matplotlib.pyplot as plt
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks
import numpy as np

x = electrocardiogram()[2000:4000]
peaks, _ = find_peaks(x, height=0)
plt.plot(x)
plt.plot(peaks, x[peaks], "x")
plt.plot(np.zeros_like(x), "--", color="gray")
plt.show()

peaks, _ = find_peaks(x, distance=150)
# difference between peaks is >= 150
print(x)
# prints [186 180 177 171 177 169 167 164 158 162 172]

plt.plot(x)
plt.plot(peaks, x[peaks], "x")
plt.show()