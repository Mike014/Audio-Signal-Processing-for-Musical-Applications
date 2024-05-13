
from tkinter import N
import numpy as np

#generating a sine wave
#x[n] = A cos(2πfnT + ϕ)
#A is the amplitude of the sine wave
#f is the frequency of the sine wave
#phi is the phase of the sine wave
#fs is the sampling frequency
#t is the time duration

def genSine(A, f, phi, fs, t):
    T = 1.0/fs#sampling interval
    n = np.arange(0, t, T)#time vector
    x = A * np.sin(2 *np.pi * f * n + phi)#sine wave generation
    return x

#generating a complex sine wave
#x[n] = Aej(ωnT +ϕ) = A cos(ωnT + ϕ) + jA sin(ωnT + ϕ)
#x is the array of complex numbers of sine wave
#n is the array of time indices
#A is the amplitude of the sine wave
#ω is the angular frequency of the sine wave
#ϕ is the phase of the sine wave
#fs is the sampling frequency
#t is the time duration

def genComplexSine(k, N):
    n = np.arange(N)#time index
    cSine = np.exp(-1j * 2 * np.pi * k * n / N)#complex sine wave
    return cSine

#implementing the DFT
#X[k] = Σ (x[n]e^(-j2πkn/N)) per n da 0 a N-1
#n is the time index
#k is the frequency index
#N is the length of the DFT

def DFT(x):
    N = len(x)#length of the signal
    X = np.array([np.dot(x, genComplexSine(K, N)) for k in range(N)])#array to store the DFT
    return X

#implementing the IDFT
#x[n] = (1/N) Σ (X[k]e^(j2πkn/N)) for k da 0 a N-1
#n is the time index
#k is the frequency index
#N is the length of the IDFT

def IDFT(X):
    N = len(X)#length of the signal
    x = np.array([np.dot(X, genComplexSine(k, N)) for n in range(N)]) / N#array to store the IDFT
    return x

#Calculating the magnitude of the DFT
#|X[k]|

def genMagSpec(X):
    X = DFT(x)#DFT of the signal
    magX = np.abs(X)#magnitude of the DFT
    return magX