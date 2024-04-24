# DSP Basic Concept - Exercise A1: Python and Sounds

This exercise is part of a course on Audio Signal Processing for Music Applications. It is designed to help you get familiar with basic audio operations using Python. The exercise is divided into four parts:

1. **Reading a wav audio file**: In this part, you are required to complete the function `readAudio(inputFile)` that reads an audio file and returns 10 consecutive samples of the file starting from the 50001th sample. The input to the function is the file name (including the path) and the output should be a numpy array containing 10 samples.

    def readAudio(inputFile):
    """
    Input:
    inputFile: the path to the wav file
    Output:
    The function should return a numpy array that
    contains 10 samples of the audio.
    """
    


2. **Basic operations with audio**: In this part, you are required to complete the function `minMaxAudio(inputFile)` that reads an audio file and returns the minimum and the maximum values of the audio samples in that file. The input to the function is the wav file name (including the path) and the output should be two floating point values returned as a tuple.

    def minMaxAudio(inputFile):
    """
    Input:
    inputFile: file path to the wav file
    Output:
    A tuple of the minimum and the maximum value of the audio
    samples, like: (min_val, max_val)
    """
    


3. **Python array indexing**: In this part, you are required to complete the function `hopSamples(x,M)` that given a numpy array x, the function returns every Mth element in x, starting from the first element. The input arguments to this function are a numpy array x and a positive integer M such that M is less than the number of elements in x. The output of this function should be a numpy array.

    def downsampleAudio(inputFile, M):
    """
    Inputs:
    inputFile: file name of the wav file (including path)
    M: downsampling factor (positive integer)
    """
    

# DFT and IDFT - Exercise

This exercise is part of a course on Audio Signal Processing for Music Applications. It is designed to help you understand some basic concepts in audio signal processing related to the Discrete Fourier Transform (DFT). You will write snippets of code to generate sinusoids, to implement the DFT and to implement the inverse DFT. The exercise is divided into five parts:

1. **Generate a sinusoid**: In this part, you are required to complete the function `genSine(A, f, phi, fs, t)` that generates a real sinusoid given its amplitude A, frequency f (Hz), initial phase phi (radians), sampling rate fs (Hz) and duration t (seconds).

    def genSine(A, f, phi, fs, t):
    """
    Inputs:
    A (float) = amplitude of the sinusoid
    f (float) = frequency of the sinusoid in Hz
    phi (float) = initial phase of the sinusoid in radians
    fs (float) = sampling frequency of the sinusoid in Hz
    t (float) = duration of the sinusoid (is second)
    Output:
    The function should return a numpy array
    x (numpy array) = The generated sinusoid (use np.cos())
    """
    


2. **Generate a complex sinusoid**: In this part, you are required to complete the function `genComplexSine(k, N)` that generates the complex sinusoid that is used in DFT computation of length N (samples), corresponding to the frequency index k.

    def genComplexSine(k, N):
    """
    Inputs:
    k (integer) = frequency index of the complex sinusoid
    of the DFT
    N (integer) = length of complex sinusoid in samples
    Output:
    The function should return a numpy array
    cSine (numpy array) = The generated complex sinusoid
    (length N)
    """
    


3. **Implement the discrete Fourier transform (DFT)**: In this part, you are required to complete the function `DFT(x)` that implements the discrete Fourier transform (DFT). Given a sequence x of length N, the function should return its DFT of length N, its spectrum, with the frequency indexes ranging from 0 to N − 1.
    
    def DFT(x):
    """
    Input:
    x (numpy array) = input sequence of length N
    Output:
    The function should return a numpy array of length N
    X (numpy array) = The N point DFT of the input sequence x
    """
   



4. **Implement the inverse discrete Fourier transform (IDFT)**: In this part, you are required to complete the function `IDFT(X)` that implements the inverse discrete Fourier transform (IDFT). Given a frequency spectrum X of length N, the function should return its IDFT x, also of length N. Assume that the frequency index of the input spectrum ranges from 0 to N − 1.

    def IDFT(X):
    """
    Input:
    X (numpy array) = frequency spectrum (length N)
    Output:
    The function should return a numpy array of length N
    x (numpy array) = The IDFT of the frequency spectrum X
    (length N)
    """
    


# AUDIO_PLOTTING_AND_FILTERING Exercise

The AUDIO_PLOTTING_AND_FILTERING.py script reads an audio file, converts the audio data to a floating point format between -1 and 1, and creates several plots to visualize the audio data in the time and frequency domain. It creates a graph of the audio data in the time domain, a spectrogram of the audio data, and a spectrogram of the magnitude of the audio data.
    
# ClassSinusoid.py 
This file defines a Sinusoid class that represents a sinusoidal signal. The class has methods to evaluate the signal at an array of points in time (evaluate) and to generate a wave by sampling the signal at a certain framerate (make_wave). The file also includes an example of how to create a Sinusoid object, generate a wave from it, and plot the magnitude spectrum of the wave.