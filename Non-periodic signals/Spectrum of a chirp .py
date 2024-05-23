from ExpoChirp import ExpoChirp
import numpy as np
import matplotlib.pyplot as plt

# Create an Exponential Chirp signal
ExChirp = ExpoChirp(50, 600)
wave = ExChirp.make_wave()

# Calculate the spectrum of the Exponential Chirp signal
fft_result = np.fft.fft(wave)
frequencies = np.fft.fftfreq(len(wave), 1/ExChirp.framerate)

# Test the Exponential Chirp signal and its spectrum
plt.figure(figsize=(12, 6))
plt.plot(frequencies, np.abs(fft_result))   
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Spectrum of an Exponential Chirp')
plt.grid(True)
plt.show()


