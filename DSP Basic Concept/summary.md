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
    


# AUDIO_PLOTTING_AND_FILTERING Exercise

The AUDIO_PLOTTING_AND_FILTERING.py script reads an audio file, converts the audio data to a floating point format between -1 and 1, and creates several plots to visualize the audio data in the time and frequency domain. It creates a graph of the audio data in the time domain, a spectrogram of the audio data, and a spectrogram of the magnitude of the audio data.
"Plotting" provides a visual representation of audio data, aiding in the analysis and understanding of the signal, while "filtering" allows for the manipulation of the signal to achieve the desired effect, whether it be cleaning the signal, isolating specific components, or modifying sound characteristics.

    
