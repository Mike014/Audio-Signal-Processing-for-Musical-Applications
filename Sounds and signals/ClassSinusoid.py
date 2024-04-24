import numpy as np
import matplotlib.pyplot as plt

class Sinusoid:
    def __init__(self, freq=440, amp=1.0, offset=0, func=np.sin):
        self.freq = freq
        self.amp = amp
        self.offset = offset
        self.func = func

    def evaluate(self, ts):
        phases = 2 * np.pi * self.freq * ts + self.offset
        ys = self.amp * self.func(phases)
        return ys

    def make_wave(self, duration=1, start=0, framerate=11025):
        n = round(duration * framerate)
        ts = start + np.arange(n) / framerate
        ys = self.evaluate(ts)
        return ts, ys

# Create a sinusoid signal
sinusoid = Sinusoid(freq=440, amp=1.0, offset=0, func=np.sin)

# Make a wave from the sinusoid signal
ts, ys = sinusoid.make_wave(duration=1.0, start=0, framerate=44100)

# Plot the wave
plt.magnitude_spectrum(ys, Fs=44100, scale="dB")
plt.show()

    


    
    

   




