import numpy as np
from scipy.io import wavfile

def readAudio(InputFile):
    fs, data = wavfile.read(InputFile)
    return data[50000:50010]

def minMaxAudio(inputFile):
    fs, data = wavfile.read(inputFile)
    return (np.min(data), np.max(data))

def hopSamples(x, M):
    if x.ndim == 1:  
        return x[::M]
    elif x.ndim == 2:  
        return x[::M, :]

def downsampleAudio(inputFile, M):
    fs, data = wavfile.read(inputFile)
    downsampled_data = hopSamples(data, M)
    outputFile = inputFile.replace(".wav", "_downsampled.wav")
    wavfile.write(outputFile, fs // M, downsampled_data)
   
