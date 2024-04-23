from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

# Read the audio file
sr, data = wavfile.read('D:\\Playlist Musica\\01 - Ember (Noisia Remix).wav')


# Convert the audio data to floating point between -1 and 1
data = data / (2.**15)

# Create graph of the audio data in the time domain
plt.axes(xlabel="Time (seconds)", ylabel="Amplitude")
t = np.linspace(0, len(data)/float(sr), len(data))
plt.plot(t, data)
plt.show()

# Create spectrogram of the audio data
plt.axes(xlabel="Time (seconds)", ylabel="Frequency (Hz)")
plt.specgram(data, NFFT=512, Fs=sr, cmap=plt.cm.gist_gray)
plt.plot()
plt.show()

# Create spectogram of magnitude of the audio data
plt.magnitude_spectrum(data, Fs=sr, scale='dB')
plt.show()

