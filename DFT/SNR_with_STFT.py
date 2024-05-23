import numpy as np
from scipy.signal import stft, istft

def calculate_snr(original_signal, reconstructed_signal):
    # Compute the SNR in dB
    noise = original_signal - reconstructed_signal[:len(original_signal)]
    signal_power = np.sum(original_signal ** 2) 
    noise_power = np.sum(noise ** 2)
    snr = 10 * np.log10(signal_power / noise_power)
    
    return snr

def stft_reconstruction(signal, window, nperseg, noverlap): 
    # Compute the STFT of the signal
    f, t, Zxx = stft(signal, fs=1.0, window=window, nperseg=nperseg, noverlap=noverlap)
    
    # Reconstruct the signal from the STFT
    _, reconstructed_signal = istft(Zxx, fs=1.0, window=window, nperseg=nperseg, noverlap=noverlap)
    
    return reconstructed_signal

if __name__ == '__main__':
    # Generate a random signal
    original_signal = np.random.normal(0, 1 , 1000)
    
    # Window Parameters for STFT
    window = 'blackman'
    nperseg = 256
    noverlap = nperseg // 2
    
    # Reconstruct the signal from the STFT
    reconstructed_signal = stft_reconstruction(original_signal, window, nperseg, noverlap)
    
    # Compute the SNR
    snr = calculate_snr(original_signal, reconstructed_signal)
    print(str(snr))
