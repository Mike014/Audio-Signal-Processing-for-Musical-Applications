from ClassSinusoid import Sinusoid
import numpy as np
import matplotlib.pyplot as plt

def apply_distortion(signal, threshold=0.5):
    # Soft clipping function
    distorted_signal = np.where(np.abs(signal) > threshold, signal, np.sign(signal) * threshold)
    return distorted_signal

def apply_saturation(signal, level=1.0):
    # Hard clipping function
    saturated_signal = np.tanh(level * signal)
    return saturated_signal

# Create a sinusoid signal
sinusoid = Sinusoid(freq=440, amp=1.0, offset=0, func=np.sin)
duration = 1.0
framerate = 44100
ts, signal = sinusoid.make_wave(duration=duration, start=0, framerate=framerate)# ts is the time array, signal is the signal array

# Apply distortion and saturation to the signal
distorted_signal = apply_distortion(signal, threshold=0.5)
saturated_signal = apply_saturation(signal, level=5.0)

# Visualize the original, distorted, and saturated signals
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(ts, signal)
plt.title('Original Signal')
plt.ylim([-1.5, 1.5])

plt.subplot(3, 1, 2)
plt.plot(ts, distorted_signal)
plt.title('Distorted Signal')
plt.ylim([-1.5, 1.5])

plt.subplot(3, 1, 3)
plt.plot(ts, saturated_signal) 
plt.title('Saturated Signal')
plt.ylim([-1.5, 1.5])

plt.tight_layout()
plt.show()


    
    

