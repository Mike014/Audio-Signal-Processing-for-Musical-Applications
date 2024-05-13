import numpy as np
import matplotlib.pyplot as plt

def make_sine(freq, offset, duration, framerate):
    t = np.linspace(0, duration, int(framerate*duration), endpoint=False)
    return np.sin(2*np.pi*freq*t) + offset

def plot_waves(wave1, wave2):
    plt.figure(figsize=(10, 4))
    plt.plot(wave1[:500], label='Wave 1')
    plt.plot(wave2[:500], label='Wave 2', linestyle='--')
    plt.legend()
    plt.show()
    
def calculate_correlation(wave1, wave2):
    corr_matrix = np.corrcoef(wave1, wave2)
    print('Matrix shape:\n', corr_matrix)
    return corr_matrix[0, 1]

if __name__ == "__main__":
    freq = 440
    duration = 1.0
    framerate = 44100
    
wave1 = make_sine(freq, 0, duration, framerate)
wave2 = make_sine(freq, 1, duration, framerate)

plot_waves(wave1, wave2)

correlation = calculate_correlation(wave1, wave2)
print(f"Correlation between the two waves: {correlation:.2f}")

