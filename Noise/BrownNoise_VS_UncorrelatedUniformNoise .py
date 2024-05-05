import numpy as np
import matplotlib.pyplot as plt

# Settings
np.random.seed(0)
num_points = 1000

# Generate UU noise
uu_noise = np.random.uniform(-1, 1, num_points)

# Generate Brown noise
brownian_step = np.random.uniform(-1, 1, num_points)
brown_noise = np.cumsum(brownian_step)

# Normalize the Signals
uu_noise = (uu_noise - np.mean(uu_noise)) / np.std(uu_noise)
brown_noise = (brown_noise - np.mean(brown_noise)) / np.std(brown_noise)

# Create the Graph
plt.figure(figsize=(12, 6))

# Graph of the Uncorrelated Uniform Noise
plt.subplot(1, 2, 1)
plt.plot(uu_noise, label='UU Noise')
plt.title('Uncorrelated Uniform Noise')
plt.xlabel('Time')
plt.ylabel('Amplitude')  # Corretto da 'ylabe' a 'ylabel'
plt.grid(True)
plt.legend()

# Graph of the Brown Noise
plt.subplot(1, 2, 2)
plt.plot(brown_noise, label='Brown Noise')
plt.title('Brown Noise')
plt.xlabel('Time')
plt.ylabel('Amplitude')  # Corretto da 'ylabe' a 'ylabel'
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()




