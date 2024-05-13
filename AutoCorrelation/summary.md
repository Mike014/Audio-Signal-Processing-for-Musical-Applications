## Summary

# Correlation.py

This script generates two sine waves with the same frequency but different offsets and calculates the correlation between them. The main functions are:

- make_sine(freq, offset, duration, framerate): Generates a sine wave given a frequency, an offset, a duration, and a framerate.
- plot_waves(wave1, wave2): Displays the first 500 samples of two waves to visually compare them.
- calculate_correlation(wave1, wave2): Calculates and prints the correlation matrix between two waves and returns the correlation value between wave1 and wave2.

# serial_correlation.py

This file explores the serial correlation of different types of noise (uniform, Gaussian, Brownian, and pink) through the function serial_corr(signal, lag=1), which calculates the serial correlation of a signal with a certain delay (lag). The function test_serial_corr() generates the different types of noise, calculates their serial correlation, and displays the results in a bar chart.
This script highlights how different types of noise have distinct serial correlation characteristics, with Brownian and pink noise typically showing higher serial correlation compared to uniform and Gaussian noise.

# Auto-Correlation.py

This script focuses on the autocorrelation of pink noise, a type of noise that has a power spectral density that decreases with increasing frequency. The main functions are:
- serial_corr(signal, lag=1): Calculates the serial correlation of a signal at a given delay.
- autocorr(signal): Calculates the autocorrelation of a signal for a range of delays and returns the lag and correlation values.
- generate_pink_noise(N, beta=1): Generates pink noise using a filter applied to white noise.

In summary, correlation in DSP is a fundamental tool for analyzing temporal relationships between signals, allowing the identification of similarities, delays and recurring patterns.