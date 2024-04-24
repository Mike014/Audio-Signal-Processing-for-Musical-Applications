import numpy as np
import matplotlib.pyplot as plt

# Create a sine wave
Freq1 = 440
Amp1 = 1.0
Freq2 = 880
Amp2 = 0.5
Freq3 = 1320
Amp3 = 0.25
Duration = 1.0
Framerate = 44100

# Create an array of points in time
t = np.linspace(0, Duration, int(Framerate * Duration), endpoint=False)

# Create the sine waves
sine_wave1 = Amp1 * np.sin(2 * np.pi * Freq1 * t)
sine_wave2 = Amp2 * np.sin(2 * np.pi * Freq2 * t)
sine_wave3 = Amp3 * np.sin(2 * np.pi * Freq3 * t)

# Add the sine waves together
sine_wave = sine_wave1 + sine_wave2 + sine_wave3

# Plot the sine wave
plt.magnitude_spectrum(sine_wave, Fs=Framerate, scale="dB")
plt.show()
