# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def dct_iv(ys):
    N = len(ys)  # ys is a column vector
    PI2 = np.pi * 2
    ts = (0.5 + np.arange(N)) / N
    fs = (0.5 + np.arange(N)) / 2
    args = np.outer(ts, fs)  # ts is a column vector and fs is a row vector
    M = np.cos(PI2 * args)
    amps = np.dot(M, ys) / 2
    return amps

def inverse_dct_iv(amps):
    return dct_iv(amps) * 2

def plot_signal(signal, ts, ys):
    plt.figure(figsize=(10, 4))
    plt.plot(ts[:1000], ys[:1000])
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Signal')
    plt.show()

if __name__ == '__main__':
    # Create a sine wave
    Freq1 = 440
    Amp1 = 1.0
    Freq2 = 880
    Amp2 = 0.5
    Freq3 = 1320
    Amp3 = 0.25
    Freq4 = 1760
    Amp4 = 0.125
    Freq5 = 2200
    Amp5 = 0.0625
    Freq6 = 2640
    Amp6 = 0.03125
    Duration = 1.0
    Framerate = 44100
    
    # Create an array of points in time
    t = np.linspace(0, Duration, int(Framerate * Duration), endpoint=False)
    
    # Create the sine waves
    sine_wave1 = Amp1 * np.sin(2 * np.pi * Freq1 * t)
    sine_wave2 = Amp2 * np.sin(2 * np.pi * Freq2 * t)
    sine_wave3 = Amp3 * np.sin(2 * np.pi * Freq3 * t)
    sine_wave4 = Amp4 * np.sin(2 * np.pi * Freq4 * t)
    sine_wave5 = Amp5 * np.sin(2 * np.pi * Freq5 * t)
    sine_wave6 = Amp6 * np.sin(2 * np.pi * Freq6 * t)
    
    # Add the sine waves together
    sine_wave = sine_wave1 + sine_wave2 + sine_wave3 + sine_wave4 + sine_wave5 + sine_wave6
    
    # Compute the DCT of the signal
    amps = dct_iv(sine_wave)
    
    # Compute the frequencies of the DCT
    dct_freqs = np.fft.fftfreq(len(amps), 1/Framerate)
    
    # Apply a low pass filter by zeroing out the high frequencies
    cutoff = 800
    amps[dct_freqs > cutoff] = 0
    
    # Compute the inverse DCT
    filtered_signal = np.dot(amps, np.cos(np.pi * np.outer(np.arange(len(amps)), np.arange(len(sine_wave))) / len(sine_wave)))
    
    # Plot the original and filtered signals
    plot_signal(sine_wave, t, sine_wave)
    plot_signal(filtered_signal, t, filtered_signal)

