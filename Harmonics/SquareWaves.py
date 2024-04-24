import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

# Parameters
Freq = 80
Amp = 1.0
Duration = 0.5
Framerate = 10000

# Create an array of points in time
t = np.linspace(0, Duration, int(Duration * Framerate), endpoint=False)

# Create the Square wave
ys = Amp * np.sign(np.sin(2 * np.pi * Freq * t))

# Compute the spectrum using FFT
Spectrum = np.abs(fft(ys))

# Create the frequency array for the spectrum
Freqnc = np.linspace(0, Framerate, len(Spectrum))

# Plot the first 1024 samples of the Square wave
plt.plot(Freqnc[:len(Freqnc)//2], Spectrum[:len(Spectrum)//2])
plt.show()