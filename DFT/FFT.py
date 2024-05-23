import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

# Create a signal
fs = 44100
duration = 5
f1 = 40
f2 = 100
f3 = 200
t = np.linspace(0, duration, int(fs*duration))# Create a time vector
complex_signal = np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t) + 0.2*np.sin(2*np.pi*f3*t)# Create a complex signal



# Supponiamo che 'signal' sia il tuo segnale audio e 'fs' la frequenza di campionamento
fft_result = fft(complex_signal)
frequencies = np.linspace(0, fs, len(complex_signal))

plt.plot(frequencies, np.abs(fft_result))
plt.xlabel('Frequenza (Hz)')
plt.ylabel('Ampiezza')
plt.show()
