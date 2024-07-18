import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

print(sd.query_devices())


fs = 48000  # Sample rate
duration = 3  # seconds

# Укажите индекс устройства или его имя здесь
device_name = 'virtual_mic_SystemAudio+Mic-175'

with sd.InputStream(device=device_name, channels=2, samplerate=fs):
    print('Recording...')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    print('Recording finished')
    wav.write('output.wav', fs, myrecording)


#   0 HDA Intel PCH: HDMI 0 (hw:0,3), ALSA (0 in, 8 out)
#    1 hdmi, ALSA (0 in, 8 out)
#    2 pipewire, ALSA (64 in, 64 out)
# *  3 default, ALSA (64 in, 64 out)
#    4 Built-in Audio Analog Stereo, JACK Audio Connection Kit (4 in, 2 out)
#    5 loopback-3613-13, JACK Audio Connection Kit (4 in, 2 out)
#    6 loopback-3613-12, JACK Audio Connection Kit (4 in, 2 out)
#    7 loopback-3613-14, JACK Audio Connection Kit (4 in, 2 out)
#    8 virtual_mic_SystemAudio+Mic, JACK Audio Connection Kit (4 in, 2 out)
#    9 loopback-3613-16, JACK Audio Connection Kit (4 in, 2 out)
#   10 loopback-3613-17, JACK Audio Connection Kit (4 in, 2 out)
#   11 loopback-3613-18, JACK Audio Connection Kit (4 in, 2 out)
#   12 virtual_mic_SystemAudio+Mic-174, JACK Audio Connection Kit (2 in, 0 out)
#   13 Firefox, JACK Audio Connection Kit (2 in, 0 out)
#   14 speech-dispatcher-dummy, JACK Audio Connection Kit (2 in, 0 out)
#   15 virtual1_SystemAudio, JACK Audio Connection Kit (2 in, 2 out)
#   16 virtual2_SystemAudio+Mic, JACK Audio Connection Kit (2 in, 2 out)
#   17 virtual1_SystemAudio-133, JACK Audio Connection Kit (2 in, 2 out)
#   18 virtual2_SystemAudio+Mic-141, JACK Audio Connection Kit (2 in, 2 out)
#   19 virtual_mic_SystemAudio+Mic-175, JACK Audio Connection Kit (2 in, 2 out)