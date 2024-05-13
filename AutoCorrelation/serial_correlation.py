import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('C:\\Users\\PC\\source\\repos\\Python For Audio Signal Processing\\Python For Audio Signal Processing\\Noise')
from PinkNoise import PinkNoise

def serial_corr(signal, lag=1):
    n = len(signal)
    y1 = signal[lag:]
    y2 = signal[:n-lag]
    corr = np.corrcoef(y1, y2)[0, 1]
    return corr

def test_serial_corr():
    duration = 0.5
    fs = 44100
    num_samples = int(duration * fs)
    
    # Make uncorrelated uniform noise
    uncorrelated_uniform_noise = np.random.uniform(-1, 1, num_samples)
    corr_uniform = serial_corr(uncorrelated_uniform_noise)
    
    # Make uncorrelated Gaussian noise
    uncorrelated_gaussian_noise = np.random.normal(0, 1, num_samples)
    corr_gaussian = serial_corr(uncorrelated_gaussian_noise)
    
    # Make Brownian noise
    steps = np.random.normal(loc=0, scale=1, size=num_samples)
    brownian_noise = np.cumsum(steps)
    corr_brownian = serial_corr(brownian_noise)
    
    # Make pink noise
    pink_noise_generator = PinkNoise(N=num_samples, amp=1.0, beta=1.0)
    pink_noise = pink_noise_generator.apply_pink_filter(pink_noise_generator.generate_white_noise())
    pink_noise = pink_noise_generator.normalize_signal(pink_noise)
    corr_pink = serial_corr(pink_noise)
    
    # View results with matplotlib
    noises = ['Uniform', 'Gaussian', 'Brownian', 'Pink']
    correlations = [corr_uniform, corr_gaussian, corr_brownian, corr_pink]
    
    for n_type, corr_value in zip(noises, correlations):
        print(f"Serial correlation for {n_type} noise: {corr_value:.2f}")
    
    plt.figure(figsize=(10, 6))
    plt.bar(noises, correlations, color=['blue', 'green', 'red', 'pink'])
    plt.ylabel('Correlazione Seriale')
    plt.title('Correlazione Seriale per Diversi Tipi di Rumore')
    plt.ylim(0, 1.1)  
    plt.show()

if __name__ == "__main__":
    test_serial_corr()
    



    














