import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

# Generate white noise
duration = 50.0
framerate = 44100
sample = int(framerate * duration)
white_noise = np.random.normal(0, 1, sample)

# Approximante the pink noise whit a filter 1/f
freqs = np.fft.rfftfreq(sample, 1/framerate)
pink_noise = np.fft.irfft(np.fft.rfft(white_noise) / np.sqrt(freqs + 1e-6)) 

# Calculate the power of the spectrum 
power_spectrum = np.abs(np.fft.rfft(pink_noise))**2

# Calculate the cumulative power
cumulative_power = np.cumsum(power_spectrum)

# Play the pink noise
sd.play(pink_noise, framerate)

# Create the Graph
plt.figure(figsize=(12, 6))
plt.plot(freqs[1:], cumulative_power[1:])
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Cumulative Power')
plt.title('Cumulative Power of Pink Noise')
plt.grid(True, which="both", ls="--")
plt.show()


