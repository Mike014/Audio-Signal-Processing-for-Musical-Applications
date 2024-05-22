import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import stft, istft, windows

# Generate a test signal
duration = float(input('Enter the duration of the signal in seconds: '))
f1 = float(input('Enter the frequency of the first sinusoid: '))
window_size = int(input('Enter the window size: '))
while window_size != 2**np.ceil(np.log2(window_size)):
    print('Window size must be a power of 2, try 512 or 1024')
    window_size = int(input('Enter the window size: '))
fft_size = int(input('Enter the FFT size: '))
while fft_size != 2**np.ceil(np.log2(fft_size)) or fft_size < window_size:
    print('FFT size must be a power of 2 and greater than or equal to the window size')
    fft_size = int(input('Enter the FFT size: '))
hop_size = int(input('Enter the hop size: '))
while hop_size > window_size:
    print('Hop size must be less than or equal to the window size')
    hop_size = int(input('Enter the hop size: '))
fs = 44100
t = np.linspace(0, duration, int(fs*duration))

x = np.sin(2*np.pi*f1*t)

# Compute the STFT
frequencies, times, Zxx = stft(x, fs, window='hann', nperseg=window_size, noverlap=hop_size, nfft=fft_size)

# Compute the inverse STFT
t, x_reconstructed = istft(Zxx, fs, window='hann', nperseg=window_size, noverlap=hop_size, nfft=fft_size)

# Show the stft module output
plt.pcolormesh(times, frequencies, 20*np.log10(np.abs(Zxx)), shading='gouraud')
plt.title('STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.colorbar() # Show the color bar
plt.show()

# Plot the reconstructed signal
plt.figure()
plt.plot(t, x_reconstructed)
plt.title('Reconstructed Signal')
plt.xlabel('Time [sec]')
plt.ylabel('Amplitude')
plt.show()

# Get a list of all window functions in the windows module
window_functions = [getattr(windows, name) for name in dir(windows) if callable(getattr(windows, name)) and not name.startswith('_')]

# Show the different windows
for window in window_functions:
    try:
        print(window.__name__)# Print the name of the window function
        plt.plot(window(1024))
        plt.title(window.__name__ + ' Window') 
        plt.show()
    except TypeError:
        # Some window functions require additional parameters, so we skip them
        pass

