import numpy as np
import matplotlib.pyplot as plt

class ExpoChirp:
    def __init__(self, start, end, duration=1, framerate=11025):
        self.start = start
        self.end = end
        self.duration = duration
        self.framerate = framerate
        self.ts = np.linspace(0, duration, framerate * duration, endpoint=False)
        
    def evaluate(self):
        start, end = np.log10(self.start), np.log10(self.end)
        freqs = np.logspace(start, end, len(self.ts))
        phase = 2 * np.pi * np.cumsum(freqs) / self.framerate
        return np.cos(phase)
    
    def make_wave(self):
        samples = self.evaluate()
        return samples

# Test the ExpoChirp class    
ExChirp = ExpoChirp(30, 500)
wave = ExChirp.make_wave()

# Conversion of samples to a readable format
samples = np.array(wave, dtype=np.int16)

# Plot the exponential chirp signal
plt.figure(figsize=(12, 6))
plt.plot(ExChirp.ts, wave)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Exponential Chirp')
plt.grid(True)
plt.show()


        

