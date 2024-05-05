import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
from scipy.fftpack import fft, ifft

def generate_white_noise(N, amp=1.0):
    """Generate white noise"""
    return np.random.normal(scale=amp, size=N)

def apply_pink_filter(signal, beta=1.0):
    """Apply a pink filter to the signal"""
    N = len(signal)
    fft_signal = fft(signal)
    frequencies = np.fft.fftfreq(N, d=1)
    # Avoid division by zero and negative values issues
    frequencies[0] = np.inf  # Set the first value to infinity to avoid division by zero
    filter_curve = 1 / (np.abs(frequencies) ** (beta / 2.0))
    filter_curve[0] = 0  # Set the first value to 0 after computing the filter to avoid NaN
    filtered_fft_signal = fft_signal * filter_curve
    filtered_signal = ifft(filtered_fft_signal).real
    return filtered_signal

def normalize_signal(signal, amp=1.0):
    """Normalize the signal"""
    signal_max = np.max(np.abs(signal))
    return (signal / signal_max) * amp

N = 44100  # Number of samples
amp = 1.0  # Amplitude
beta = 1  # Beta value for the pink filter

# Generate white noise
white_noise = generate_white_noise(N, amp)

# Apply the pink filter
pink_noise = apply_pink_filter(white_noise, beta)

# Normalize the signal
pink_noise = normalize_signal(pink_noise, amp)

# View the signal white and pink noise
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(white_noise[:500])
plt.title('White Noise')
plt.subplot(1, 2, 2)
plt.plot(pink_noise[:500])
plt.title('Pink Noise')
plt.tight_layout()
plt.show()

# Calculate the power spectrum of the white and pink noise
frequencies, power_white = welch(white_noise, nperseg=1024)
_, power_pink = welch(pink_noise, nperseg=1024)

plt.figure(figsize=(10, 5))
plt.loglog(frequencies, power_white, label='White Noise')
plt.loglog(frequencies, power_pink, label='Pink Noise', color='pink')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Power')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()


   
    
    
