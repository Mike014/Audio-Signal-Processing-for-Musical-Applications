import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 96000
T = 5
hz = 440

t = np.linspace(0, T, int(sampling_rate * T))

signal = np.sin(2 * np.pi * hz * t)

plt.figure(figsize=(10, 4))
plt.stem(t[:1000], signal[:1000], 'b', markerfmt='bo', basefmt="r")
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Periodic Signal')
plt.grid(True)
plt.show()
