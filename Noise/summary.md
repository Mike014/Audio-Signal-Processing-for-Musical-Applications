## Noise

# Gaussian noise.py
This script generates uncorrelated Gaussian noise (UG noise) using a normal distribution. It calculates the spectrum of the generated noise and then displays normal probability plots for both the real and imaginary parts of the spectrum. This is done to verify that the spectrum of UG noise is also normally distributed, in both its real and imaginary parts.

# PinkNoise.py
The `PinkNoise.py` file deals with generating pink noise. It starts by generating white noise using a normal distribution, then applies a pink filter to convert the white noise into pink noise. The pink filter modifies the spectrum of the white noise following a power law. Finally, the script displays both the white and pink noise and calculates and shows their power spectra, demonstrating the difference between the two types of noise.

# Integrated spectrum.py
This script defines an `IntegratedSpectrum` class that calculates the integrated spectrum of a signal. The integrated spectrum is useful for analyzing the cumulative distribution of the signal's power across different frequencies. The code calculates the integrated spectrum of a randomly generated white noise signal, and then displays the cumulative power as a function of frequency on a log-log plot.

# BrownNoise_VS_UncorrelatedUniformNoise.py
In this script, two types of noise are generated and compared: uncorrelated uniform noise (UU noise) and brown noise. The uncorrelated uniform noise is generated with uniformly distributed random values, while the brown noise is obtained by cumulatively summing uniformly distributed random steps, simulating a Brownian motion process. Both signals are normalized and then displayed to show their temporal characteristics.

