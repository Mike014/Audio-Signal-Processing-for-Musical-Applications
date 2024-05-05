import numpy as np
import matplotlib.pyplot as plt

class IntegratedSpectrum:
    def __init__(self, signal, framerate):
        self.signal = signal
        self.framerate = framerate
        self.fs, self.cs = self.compute_integrated_spectrum()
        
    def compute_integrated_spectrum(self):
        # Correzione: Usa 'self.signal' invece di 'Self.signal'
        fft_result = np.fft.rfft(self.signal)
        power_spectrum = np.abs(fft_result)**2
        cumulative_sum = np.cumsum(power_spectrum)
        cumulative_sum /= cumulative_sum[-1]
        frequencies = np.fft.rfftfreq(len(self.signal), 1/self.framerate)
        return frequencies, cumulative_sum
    
    def plot_power(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.fs[1:], self.cs[1:])
        plt.xscale('log')
        plt.yscale('log')
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Cumulative Power')
        plt.title('Cumulative Power of the Signal')
        plt.grid(True, which="both", ls="--")
        plt.show()
        

# Test the IntegratedSpectrum class
if __name__ == "__main__":
    duration = 1.0
    framerate = 44100
    samples = int(duration * framerate) 
    white_noise = np.random.normal(0, 1, samples)
    
    integrated_spectrum = IntegratedSpectrum(white_noise, framerate)
    
    integrated_spectrum.plot_power()