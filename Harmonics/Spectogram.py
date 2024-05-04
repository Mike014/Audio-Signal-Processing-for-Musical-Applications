import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

# Generate a linear chirp signal 
t = np.linspace(0, 1, 11025) # 0 Starting value of the interval, 1 ending of the interval, 11025 number of samples
chirp_signal = signal.chirp(t, f0=10, f1=1000, t1=1, method='linear')

# Calculate the STFT
frequencies, times, Sxx = signal.spectrogram(chirp_signal, fs=11025, nperseg=512) # fs is the sampling frequency, nperseg is the number of samples per segment

# Visualize the Spectogram
plt.pcolormesh(times, frequencies, 10 * np.log10(Sxx), shading='gouraud')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.colorbar(label='Magnitude [dB]')
plt.title('Spectrogram of a Linear Chirp Signal')
plt.ylim(0, 700) # Limit the frequency range to 700 Hz
plt.show()


