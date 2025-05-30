# converts audio files to spectrograms
import librosa
import librosa.display
import matplotlib.pyplot as plt

y, sr librosa.load('audio.wav')
spectrogram = librosa.feature.melspectrogram(y, sr=sr)
librosa.display.specshow(librosa.power_to_db(spectrogram, ref=np.max), y_axis='mel', x_axis='time')
plt.colorbar(format='%+2.0f dB')
plt.title('Mel-frequency spectrogram')
plt.show()