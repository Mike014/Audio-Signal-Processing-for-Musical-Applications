import numpy as np
from scipy.signal import lfilter
import matplotlib.pyplot as plt

def serial_corr(signal, lag=1):
    n = len(signal)
    y1 = signal[lag:]
    y2 = signal[:n-lag]
    corr = np.corrcoef(y1, y2)[0, 1]
    return corr

def autocorr(signal):
    lags = range(len(signal)//2)
    corrs = [serial_corr(signal, lag) for lag in lags]
    return list(lags), corrs

def generate_pink_noise(N, beta=1):
    white_noise = np.random.normal(0, 1, N)
    b = [0.02] * 5
    pink_noise = lfilter([1], b, white_noise)
    return pink_noise

N = 512
betas = [0.3, 1.0, 1.7]

plt.figure(figsize=(10, 6))

for beta in betas:
    pink_noise = generate_pink_noise(N, beta)
    lags, corrs = autocorr(pink_noise)
    plt.plot(lags, corrs, label=f'Beta = {beta}')
    
plt.xlabel('Lag')
plt.ylabel('Correlation')
plt.title('Autocorrelation of Pink Noise')
plt.legend()
plt.show()



  