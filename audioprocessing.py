import audioread
import array
import wave
import numpy as np
import pydub
from pydub import AudioSegment
import ffmpeg
from playsound import playsound
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
from io import BytesIO
import tempfile
import requests
import numpy as np
import scipy.signal as sg
import pydub
import matplotlib.pyplot as plt
from IPython.display import Audio, display
import scipy
import wave
import numpy
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import filtfilt
import requests
import IPython


# # sound = AudioSegment.from_mp3("/path/to/file.mp3")
# # sound.export("/output/path/file.wav", format="wav")
#
#
# def save_wav_channel(fn, wav, channel):
#     '''
#     Take Wave_read object as an input and save one of its
#     channels into a separate .wav file.
#     '''
#     # Read data
#     nch = wav.getnchannels()
#     depth = wav.getsampwidth()
#     wav.setpos(0)
#     sdata = wav.readframes(wav.getnframes())
#
#     # Extract channel data (24-bit data not supported)
#     typ = { 1: np.uint8, 2: np.uint16, 4: np.uint32 }.get(depth)
#     if not typ:
#         raise ValueError("sample width {} not supported".format(depth))
#     if channel >= nch:
#         raise ValueError("cannot extract channel {} out of {}".format(channel+1, nch))
#     print ("Extracting channel {} out of {} channels, {}-bit depth".format(channel+1, nch, depth*8))
#     data = np.fromstring(sdata, dtype=typ)
#     ch_data = data[channel::nch]
#
#     # Save channel to a separate file
#     outwav = wave.open(fn, 'w')
#     outwav.setparams(wav.getparams())
#     outwav.setnchannels(1)
#     outwav.writeframes(ch_data.tostring())
#     outwav.close()
#
# # wav = wave.open('/Users/kunal/audiofilter/lilnasxpanini.wav')
# # save_wav_channel('ch1.wav', wav, 0)
# # save_wav_channel('ch2.wav', wav, 1)
#
# # playsound('ch1.wav')
# # playsound('ch2.wav')
# #
# # y, sr = librosa.load('/Users/kunal/audiofilter/areyougonnagomyway.wav')
# #
# # # Set the hop length; at 22050 Hz, 512 samples ~= 23ms
# # hop_length = 512
# #
# # # Separate harmonics and percussives into two waveforms
# # y_harmonic, y_percussive = librosa.effects.hpss(y)
# #
# # playsound(y_harmonic)
# #
# # # Beat track on the percussive signal
# # tempo, beat_frames = librosa.beat.beat_track(y=y_percussive,
# #                                              sr=sr)
# #
# # # Compute MFCC features from the raw signal
# # mfcc = librosa.feature.mfcc(y=y, sr=sr, hop_length=hop_length, n_mfcc=13)
# #
# # # And the first-order differences (delta features)
# # mfcc_delta = librosa.feature.delta(mfcc)
# #
# # # Stack and synchronize between beat events
# # # This time, we'll use the mean value (default) instead of median
# # beat_mfcc_delta = librosa.util.sync(np.vstack([mfcc, mfcc_delta]),
# #                                     beat_frames)
# #
# # # Compute chroma features from the harmonic signal
# # chromagram = librosa.feature.chroma_cqt(y=y_harmonic,
# #                                         sr=sr)
# #
# # # Aggregate chroma features between beat events
# # # We'll use the median value of each feature between beat frames
# # beat_chroma = librosa.util.sync(chromagram,
# #                                 beat_frames,
# #                                 aggregate=np.median)
# #
# # # Finally, stack all beat-synchronous features together
# # beat_features = np.vstack([beat_chroma, beat_mfcc_delta])
# #
#
#
# #
# # S_full, phase = librosa.magphase(librosa.stft(y))
# # S_filter = librosa.decompose.nn_filter(S_full,
# #                                        aggregate=np.median,
# #                                        metric='cosine',
# #                                        width=int(librosa.time_to_frames(2, sr=sr)))
# #
# # S_filter = np.minimum(S_full, S_filter)
# #
# #
# # margin_i, margin_v = 2, 10
# # power = 2
# #
# # mask_i = librosa.util.softmask(S_filter,
# #                                margin_i * (S_full - S_filter),
# #                                power=power)
# #
# # mask_v = librosa.util.softmask(S_full - S_filter,
# #                                margin_v * S_filter,
# #                                power=power)
# #
# # # Once we have the masks, simply multiply them with the input spectrum
# # # to separate the components
# #
# # S_foreground = mask_v * S_full
# # S_background = mask_i * S_full
#
#

# read in audio file and get the two mono tracks
song = wave.open('lilnasxpanini.wav', mode=None)
myAudioFile = "/Users/kunal/audiofilter/areyougonnagomyway.wav"

sound_stereo = AudioSegment.from_file(myAudioFile, format="wav")
sound_monoL = sound_stereo.split_to_mono()[0]
sound_monoR = sound_stereo.split_to_mono()[1]

new = sound_monoR.high_pass_filter(70)

# Invert phase of the Right audio file
sound_monoR_inv = sound_monoR.invert_phase()

new = sound_monoR.high_pass_filter(70)

# Merge two L and R_inv files, this cancels out the centers
sound_CentersOut = sound_monoL.overlay(new)

# Export merged audio file
fh = sound_CentersOut.export("myAudioFile_CentersOut.wav", format="wav")


playsound('myAudioFile_CentersOut.wav')