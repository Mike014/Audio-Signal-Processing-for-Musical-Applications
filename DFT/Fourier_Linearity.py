import numpy as np
import matplotlib.pyplot as plt

# Define two signals
x1 = np.sin(2*np.pi*40*np.linspace(0,1,1000)) # 40 Hz
x2 = np.sin(2*np.pi*80*np.linspace(0,1,1000)) # 80 Hz

# Compute the DFT of the two signals
x = x1 + x2

# Compute the DFT of the sum of the two signals
X1 = np.fft.fft(x1) # DFT of x1, x1 is a sine wave
X2 = np.fft.fft(x2) # DFT of x2, x2 is a sine wave
X = np.fft.fft(x) # DFT of x, x is the sum of x1 and x2, x is a complex wave

# Plot the magnitude of the DFT of the two signals
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(x1)
plt.title('Signal 1')

plt.subplot(2, 2, 1)
plt.plot(x2)
plt.title('Signal 2')

plt.subplot(2, 2, 2)
plt.plot(np.abs(X1))
plt.title('DFT of x1')

plt.subplot(2, 2, 2)
plt.plot(np.abs(X2))
plt.title('DFT of x2')

plt.figure()
plt.plot(x)
plt.title('Sum of the two signals')

plt.figure()
plt.plot(np.abs(X))
plt.title('DFT of sum of the two signals')

plt.show()


