import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
from scipy.fftpack import fft, ifft

class PinkNoise:
    def __init__(self, N=44100, amp=1.0, beta=1.0):
        self.N = N
        self.amp = amp
        self.beta = beta

    def generate_white_noise(self):
        """Generate white noise"""
        return np.random.normal(scale=self.amp, size=self.N)

    def apply_pink_filter(self, signal):
        """Apply a pink filter to the signal"""
        N = len(signal)
        fft_signal = fft(signal)
        frequencies = np.fft.fftfreq(N, d=1)
        # Avoid division by zero and negative values issues
        frequencies[0] = np.inf  # Set the first value to infinity to avoid division by zero
        filter_curve = 1 / (np.abs(frequencies) ** (self.beta / 2.0))
        filter_curve[0] = 0  # Set the first value to 0 after computing the filter to avoid NaN
        filtered_fft_signal = fft_signal * filter_curve
        filtered_signal = ifft(filtered_fft_signal).real
        return filtered_signal

    def normalize_signal(self, signal):
        """Normalize the signal"""
        signal_max = np.max(np.abs(signal))
        return (signal / signal_max) * self.amp

    def generate_and_plot(self):
        # Generate white noise
        white_noise = self.generate_white_noise()

        # Apply the pink filter
        pink_noise = self.apply_pink_filter(white_noise)

        # Normalize the signal
        pink_noise = self.normalize_signal(pink_noise)

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
        

if __name__ == "__main__":
    pink_noise = PinkNoise()
    pink_noise.generate_and_plot()

   
    
    
