from scipy.io.wavfile import read 
import matplotlib.pyplot as plt

# Read the audio file
input_data = read('D:\\New sfx\\Toms\\Tom_1.wav')  
audio = input_data[1]
# plot the first 1024 samples
plt.plot(audio[0:1024])
# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time (samples)")
# set the title
plt.title("Toms Sample")
# display the plot
plt.show()







