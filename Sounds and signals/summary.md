## Signal

# ClassSinusoid.py 
- This file defines a Sinusoid class that represents a sinusoidal signal. The class has methods to evaluate the signal at an array of points in time (evaluate) and to generate a wave by sampling the signal at a certain framerate (make_wave). The file also includes an example of how to create a Sinusoid object, generate a wave from it, and plot the magnitude spectrum of the wave.

# Periodic signals.py 
- This file shows how to create sinusoidal signals with different frequencies and amplitudes using numpy and matplotlib. It creates three sinusoidal signals, adds them together to form a composite signal, and then plots the magnitude spectrum of the composite signal.

# Spectrums.py 
- This file extends the example in Periodic signals.py by creating six sinusoidal signals, adding them together, and then applying a Fourier transform to the composite signal to obtain its spectrum. It then applies a low-pass filter to the spectrum by zeroing out frequencies above a certain cutoff value, and finally plots the magnitude spectrum of the original and filtered signals.

# Wave.py 
- This file shows how to read an audio file using scipy.io.wavfile.read, extract the audio data from the file, and then plot the first 1024 samples of the audio signal.