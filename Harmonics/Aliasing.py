import numpy as np
import matplotlib.pyplot as plt

# Parameters
framerate = 10000
t = np.linspace(0, 5 / 4500, int(5 * framerate / 4500), endpoint=False)

# Generate a 4500 Hz cosine signal
ys1 = np.cos(2 * np.pi * 4500 * t)

# Generate a 5500 Hz cosine signal
ys2 = np.cos(2 * np.pi * 5500 * t)

# Plot the signals
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, ys1, label='4500 Hz cosine')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, ys2, label='5500 Hz cosine')
plt.legend()

plt.show()



