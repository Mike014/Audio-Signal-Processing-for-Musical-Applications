import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import probplot
from scipy.fftpack import fft

def generate_uncorrelated_gaussian_noise(N, amp=1.0):
    return np.random.normal(0, amp, N)

def normal_probability_plot(data):
    probplot(data, dist="norm", plot=plt)
    plt.show()

N = 44100 
amp = 1.0 

# Generate UG noise
ug_noise = generate_uncorrelated_gaussian_noise(N, amp)

# Calculate the spectrum
ug_noise_fft = fft(ug_noise)
ug_noise_spectrum_real = np.real(ug_noise_fft)
ug_noise_spectrum_imag = np.imag(ug_noise_fft)

# View the normal probability plot
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
normal_probability_plot(ug_noise_spectrum_real)
plt.title('Real Part')

plt.subplot(1, 2, 2)
normal_probability_plot(ug_noise_spectrum_imag)
plt.title('Imaginary Part')
    
