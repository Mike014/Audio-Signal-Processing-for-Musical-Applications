import numpy as np
import matplotlib.pyplot as plt

# Create a sine wave
Freq1 = 440
Amp1 = 1.0
Freq2 = 880
Amp2 = 0.5
Freq3 = 1320
Amp3 = 0.25
Freq4 = 1760
Amp4 = 0.125
Freq5 = 2200
Amp5 = 0.0625
Freq6 = 2640
Amp6 = 0.03125
Duration = 1.0
Framerate = 44100

# Create an array of points in time
t = np.linspace(0, Duration, int(Framerate * Duration), endpoint=False)

# Create the sine waves
sine_wave1 = Amp1 * np.sin(2 * np.pi * Freq1 * t)
sine_wave2 = Amp2 * np.sin(2 * np.pi * Freq2 * t)
sine_wave3 = Amp3 * np.sin(2 * np.pi * Freq3 * t)
sine_wave4 = Amp4 * np.sin(2 * np.pi * Freq4 * t)
sine_wave5 = Amp5 * np.sin(2 * np.pi * Freq5 * t)
sine_wave6 = Amp6 * np.sin(2 * np.pi * Freq6 * t)

# Add the sine waves together
sine_wave = sine_wave1 + sine_wave2 + sine_wave3 + sine_wave4 + sine_wave5 + sine_wave6

# Compute the FFT of the signal
spectrum = np.fft.fft(sine_wave)

# Compute the frequencies of the FFT
fft_freqs = np.fft.fftfreq(len(spectrum), 1/Framerate)

# Apply a low pass filter by zeroing out the high frequencies
cutoff = 800
spectrum[fft_freqs > cutoff] = 0

# Compute the inverse FFT
filtered_signal = np.fft.ifft(spectrum)

# Plot the original and filtered signals
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.magnitude_spectrum(sine_wave, Fs=Framerate, scale='dB', color='b')
plt.title('Original Signal')

plt.subplot(1, 2, 2)
plt.magnitude_spectrum(filtered_signal, Fs=Framerate, scale='dB', color='r')
plt.title('Filtered Signal')

plt.show()
