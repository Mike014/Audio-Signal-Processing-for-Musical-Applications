# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def synthesize(amps, freqs, ts):    
    signal = np.zeros_like(ts)
    for amp, freq in zip(amps, freqs):
        signal += amp * np.sin(2 * np.pi * freq * ts)
    return signal

def analyze(signal, freqs, ts):
    PI2 = np.pi * 2
    args = np.outer(ts, freqs)
    M = np.cos(PI2 * args)
    amps = np.linalg.solve(M, signal)
    return amps

def test_orthogonality(N):
    time_unit = 0.001
    ts = np.arange(N) / N * time_unit
    max_freq = N / time_unit / 2
    fs = np.arange(N) / N * max_freq
    PI2 = np.pi * 2
    args = np.outer(ts, fs)
    M = np.cos(PI2 * args)
    
    MTM = np.dot(M.T, M)
    
    I = np.eye(N)
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.imshow(MTM, cmap='hot', interpolation='nearest')
    plt.title("$M^T M$")
    plt.colorbar()
    
    plt.subplot(1, 2, 2)
    plt.imshow(I, cmap='hot', interpolation='nearest')
    plt.title("$I$")
    plt.colorbar()
    
    plt.show()
    
    is_orthogonal = np.allclose(MTM, I, atol=1e-7)
    print("\nIs orthogonal: ", is_orthogonal)
    
def plot_signal(signal, ts, ys):
    plt.figure(figsize=(10, 4))
    plt.plot(ts[:1000], ys[:1000])
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Synthesized signal')
    plt.show()
    
amps = np.array([0.6, 0.25, 0.1, 0.05])
freqs = np.array([100, 200, 300, 400])
framerate = 44100
ts = np.linspace(0, 1, framerate)

signal = synthesize(amps, freqs, ts)
plot_signal(signal, ts, signal)

test_orthogonality(10)





