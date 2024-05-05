import numpy as np
import sounddevice as sd

# duration and sampling frequency
duration = 15.0
framerate = 44100

# Generate white noise
white_noise = np.random.normal(0, 1, int(framerate * duration))

# Play the white noise
sd.play(white_noise, framerate)

sd.wait()
