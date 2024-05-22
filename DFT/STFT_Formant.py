import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import stft, iirfilter, lfilter, freqz
from scipy.io.wavfile import write
from scipy.fft import fft, ifft
from pydub import AudioSegment
from pydub.playback import play

def brown_noise(n_samples):
    return np.cumsum(np.random.normal(0, 1, n_samples))

# Set parameters
fs = 44100 # Sample rate
bw = 50.0 # Bandwidth
duration = float(input("Insert duration in second: ")) # seconds

# Formant frequencies for each vowel
formants = {
    'a': [730, 1090, 2440], 
    'e': [660, 1700, 2400],
    'i': [440, 1220, 2650],
    'o': [450, 800, 2830],
    'u': [325, 700, 2530]
}

# Get user input
vowel = input("Enter a vowel (a, e, i, o, u): ")

# Create a bandpass filter for each formant
filters = [iirfilter(2, [f-bw/2, f+bw/2], rs=60, btype='band', analog=False, ftype='butter', fs=fs) for f in formants[vowel]]
# Generate brown noise
x = brown_noise(int(fs * duration))

# Normalize to 16-bit range
x *= 32767 / np.max(np.abs(x))
# Convert to 16-bit data
x = x.astype(np.int16)

# Save and play the brown noise
write('brown_noise.wav', fs, x)
brown_noise = AudioSegment.from_wav('brown_noise.wav')
print("Playing the brown noise...")
play(brown_noise)

# Apply the second filter to the signal
b, a = filters[1]
x_filtered = lfilter(b, a, x)

# Normalize to 16-bit range
x_filtered *= 32767 / np.max(np.abs(x_filtered))
# Convert to 16-bit data
x_filtered = x_filtered.astype(np.int16)

write('filtered.wav', fs, x_filtered)
filtered_sound = AudioSegment.from_wav('filtered.wav')
print("Playing the sound after the filter...")
play(filtered_sound)

# Normalize to 16-bit range
x_filtered = x_filtered.astype(np.float64)  # Convert to float64
x_filtered *= 32767 / np.max(np.abs(x_filtered))
x_filtered = x_filtered.astype(np.int16)  # Convert back to int16

# Compute the DFT of the filtered signal
X_filtered = fft(x_filtered)

# Compute the IDFT
x_reconstructed = ifft(X_filtered)

# Compute the STFT
window_size = 512
fft_size = 1024
hop_size = 256
frequencies, times, Zxx = stft(x_filtered, fs, window='blackman', nperseg=window_size, noverlap=hop_size, nfft=fft_size)

# Plot the filtered signal (time domain)
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.plot(x_filtered)
plt.title('Filtered Signal in Time Domain')

# Plot the DFT (frequency domain)
plt.subplot(2, 2, 2)
plt.plot(np.abs(X_filtered))
plt.title('Magnitude of DFT of Filtered Signal')

# Plot the reconstructed signal (time domain)
plt.subplot(2, 2, 3)
plt.plot(x_reconstructed.real)  # Use real part to remove numerical errors
plt.title('Reconstructed Signal from IDFT')

# Plot the STFT (time-frequency domain)
plt.subplot(2, 2, 4)
plt.pcolormesh(times, frequencies, 20*np.log10(np.abs(Zxx)), shading='gouraud')
plt.title('STFT Magnitude of Filtered Signal')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.colorbar()  # Show the color bar

plt.tight_layout()
plt.show()

# Save the sound to a file
write('output.wav', fs, x_filtered)

# Load the sound file
print("Playing the final sound...")
sound = AudioSegment.from_wav('output.wav')

# Play the sound
play(sound)






