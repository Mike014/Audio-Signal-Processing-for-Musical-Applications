# -*- coding: utf-8 -*-
import numpy as np
from scipy.signal import get_window
from scipy.fftpack import fft, fftshift

def extractMainLobe(window, M):
    # """
    # Input:
    # window (string): Window type to be used (Either rectangular (‘boxcar’), ‘hamming’ or ‘blackmanharris’)
    # M (integer): length of the window to be used
    # Output:
    # The function should return a numpy array containing the main lobe of the magnitude spectrum of the window in decibels (dB).
    # """
    
    w = get_window(window, M) # Get the window
    
    # Compute the magnitude spectrum of the window
    N = 8 * M 
    w_fft = fft(w, N)
    
    # Compute the magnitude spectrum in dB
    w_fft_mag = 20 * np.log10(abs(w_fft) + np.finfo(float).eps) # Add epsilon to avoid log(0)
    
    # Shift zero frequency component to the center
    w_fft_mag_shifted = fftshift(w_fft_mag) # Shift zero frequency component to the center
    
    # Find the indices of the main lobe
    half_size = N // 2
    main_lobe_start = np.argmin(w_fft_mag_shifted[:half_size])
    main_lobe_end = half_size + np.argmin(w_fft_mag_shifted[half_size:])
    
    # Extract the main lobe
    main_lobe = w_fft_mag_shifted[main_lobe_start:main_lobe_end]
    
    return main_lobe

if __name__ == '__main__':
    window = 'hamming'
    M = 51
    main_lobe = extractMainLobe(window, M)
    print(main_lobe)
    print(main_lobe.shape) # Expected output: '(25,)'

