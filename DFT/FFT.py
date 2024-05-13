import numpy as np
import matplotlib.pyplot as plt

# FFT 
fs = 8000 # Sampling frequency
t = np.arange(0,1,1/fs) # Time vector
f1, f2 = 1000, 2500 # Frequencies of the signals
signal = 0.5*np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t) # Signal

# FFT with numpy
X = np.fft.fft(signal)

# Plot
frequencies = np.fft.fftfreq(len(X), 1/fs)
plt.figure(figsize=(14, 5))
plt.stem(frequencies, np.abs(X), 'b', markerfmt='bo', basefmt='r-')
plt.title('FFT - Magnitude')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.xlim(0, fs/2)
plt.grid()
plt.show()
