
import numpy as np
import matplotlib.pyplot as plt

class Chirp:
    def __init__(self, start=440, end=880, amp=1.0):
        self.start = start
        self.end = end
        self.amp = amp
        
    def evaluate(self, ts):
        freqs = np.linspace(self.start, self.end, len(ts))
        dts = np.diff(ts, prepend=0)
        dphis = 2 * np.pi * freqs * dts
        phases = np.cumsum(dphis)
        ys = self.amp * np.sin(phases)
        return ys
    
# Test the Chirp class
chirp = Chirp(start=220, end=880) 
ts = np.linspace(0, 1, 1000, endpoint=False)
ys = chirp.evaluate(ts)

# Plot the chirp signal
plt.figure(figsize=(12, 6))
plt.plot(ts, ys)    
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Linear Chirp')
plt.grid(True)
plt.show()
