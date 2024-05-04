import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.signal.windows import hamming  # Aggiornato per evitare l'avviso di deprecazione
from ClassSinusoid import Sinusoid

# Genera un'onda sinusoidale
sinusoid = Sinusoid(freq=440, amp=1.0, offset=0, func=np.sin)
duration = 1.0
ts, signal = sinusoid.make_wave(duration=duration, start=0, framerate=44100)

# Applica una finestra di Hamming al segnale
window = hamming(len(signal))
windowed_signal = signal * window

# Calcola la DFT del segnale
fft_signal = fft(signal)
fft_windowed_signal = fft(windowed_signal)

# Visualizza la DFT del segnale
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(np.abs(fft_signal)[:len(signal)//2])
plt.title('Spettro senza finestra')

plt.subplot(1, 2, 2)
plt.plot(np.abs(fft_windowed_signal)[:len(signal)//2])
plt.title('Spettro con finestra di Hamming')

plt.show()



