import numpy as np
import matplotlib.pyplot as plt

# DFT 
fs = 8000 # Sampling frequency
t = np.arange(0,1,1/fs) # Time vector
f1, f2 = 1000, 2500 # Frequencies of the signals
signal = 0.5*np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t) # Signal

# DFT function
def DFT(signal):
    N = len(signal) 
    n = np.arange(N) 
    k = n.reshape((N,1))
    e = np.exp(-2j*np.pi*k*n/N)
    X = np.dot(e, signal)
    return X

# instance of DFT
X = DFT(signal)

# Plot
frequencies = np.arange(len(X))
plt.figure(figsize=(14, 5))
plt.stem(frequencies, np.abs(X), 'b', markerfmt='bo', basefmt='r-')
plt.title('DFT - Magnitude')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.xlim(0, fs/2)
plt.grid()
plt.show()






