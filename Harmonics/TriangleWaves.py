import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

# Parameters
Freq = 440 
Amp = 1.0
Duration = 0.5
Framerate = 10000

# Create an array of points in time
t = np.linspace(0, Duration, int(Duration *  Framerate), endpoint=False)

# Create the triangle wave
ys = Amp * 2 * (Freq * t % 1 - 0.5)

# Compute the spectrum using FFT
Spectrum = np.abs(fft(ys))

# Create the frequency array for the spectrum
Freqnc = np.linspace(0, Framerate, len(Spectrum))

# Plot the first 1024 samples of the triangle wave
plt.plot(ys[:1024])

# Label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time (samples)")

# Set the title
plt.title("Triangle Wave")

# Display the plot
plt.plot(Freqnc, Spectrum)
plt.show()
