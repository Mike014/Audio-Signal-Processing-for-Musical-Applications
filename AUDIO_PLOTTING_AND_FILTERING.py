from scipy.io import wavfile
from scipy.signal import butter, freqz, lfilter
import matplotlib.pyplot as plt
import numpy as np

# Define the filter lowpass butter function
def butter_lowpass(cutoff, fs, order):
    nyquist = 0.5 * fs
    cut = cutoff / nyquist
    b, a = butter(order, cut, btype='low')
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

if __name__ == "__main__":
    # Read the audio file
    sr, data = wavfile.read('D:\\Playlist Musica\\01 - Ember (Noisia Remix).wav')

    # Convert the audio data to floating point between -1 and 1
    data = data / (2.**15)

    # cutoff
    cutoff = 2000.0 # desired cutoff frequency of the filter, Hz

    # Create graph of the audio data in the time domain
    plt.axes(xlabel="Time (seconds)", ylabel="Amplitude")
    t = np.linspace(0, len(data)/float(sr), len(data))
    plt.plot(t, data)
    plt.show()

    # Create spectrogram of the audio data
    plt.axes(xlabel="Time (seconds)", ylabel="Frequency (Hz)")
    plt.specgram(data, NFFT=512, Fs=sr, cmap=plt.cm.gist_gray)
    plt.plot()
    plt.show()

    # Create spectogram of magnitude of the audio data
    plt.magnitude_spectrum(data, Fs=sr, scale='dB')
    plt.show()

    # Plot the frequency response for a few different orders.
    for order in [2, 4, 8]:
        b, a = butter_lowpass(cutoff, sr, order)
        w, h = freqz(b, a)
        plt.figure()
        plt.clf()
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Gain')
        plt.grid(True)
        plt.plot((sr*0.5/np.pi)*w, abs(h), label="order = %d" % order)
        plt.legend(loc='best')

    # Filter the signal and plot spectrogram
    filtered = butter_lowpass_filter(data, cutoff, sr, 8)
    plt.figure()
    plt.clf()
    plt.axes(xlabel="Time (seconds)", ylabel="Frequency (Hz)")
    plt.specgram(filtered, NFFT=512, Fs=sr, cmap=plt.cm.gist_gray)
    plt.plot()
    plt.show()

    # Write the filtered audio to a new WAV file
    wavfile.write("filtered_output.wav", sr, filtered)





    



