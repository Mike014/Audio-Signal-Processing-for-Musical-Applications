import numpy as np
from scipy.signal import stft
from scipy.io.wavfile import read
import matplotlib.pyplot as plt

def computeEngEnv(x, fs, window, M, N, H):
    # Compute the STFT 
    f, t, Zxx = stft(x, fs, window=window, nperseg=M, noverlap=H, nfft=N)
    
    # Compute the energy envelope for each band
    low_freq_bins = np.where((f > 0) & (f < 500))
    high_freq_bins = np.where((f > 500) & (f < 5000))
    
    # Compute the energy envelope for each band
    low_band_energy = 10 * np.log10(np.sum(np.abs(Zxx[low_freq_bins])**2, axis=0))
    high_band_energy = 10 * np.log10(np.sum(np.abs(Zxx[high_freq_bins])**2, axis=0))
    
    return low_band_energy, high_band_energy, t

if __name__ == '__main__':
    # Generata pink noise 
    N = 44100
    fs = 44100  # Add a sampling rate for your pink noise
    amp = 1.0
    beta = 1.0
    pink_noise = np.random.normal(scale=amp, size=N) # Generate white noise
    
    # Apply the pink filter
    N = len(pink_noise)
    fft_signal = np.fft.fft(pink_noise)
    frequencies = np.fft.fftfreq(N, d=1)
    # Avoid division by zero and negative values issues
    frequencies[0] = np.inf  # Set the first value to infinity to avoid division by zero
    filter_curve = 1 / (np.abs(frequencies) ** (beta / 2.0))
    filter_curve[0] = 0  # Set the first value to 0 after computing the filter to avoid NaN
    filtered_fft_signal = fft_signal * filter_curve
    filtered_signal = np.fft.ifft(filtered_fft_signal).real
    pink_noise = filtered_signal
    
    # Normalize the signal
    signal_max = np.max(np.abs(pink_noise))
    pink_noise = (pink_noise / signal_max) * amp
    
    compute_Eng_Env_Signal = computeEngEnv(pink_noise, fs, 'hann', 1024, 1024, 512)
    print(compute_Eng_Env_Signal)
    
    plt.figure()
    plt.plot(compute_Eng_Env_Signal[2], compute_Eng_Env_Signal[0], label='Low band energy')
    plt.plot(compute_Eng_Env_Signal[2], compute_Eng_Env_Signal[1], label='High band energy')
    plt.xlabel('Time (s)')
    plt.ylabel('Energy (dB)')
    plt.title('Energy envelope')
    plt.legend()
    plt.show()

    
    
    


     

