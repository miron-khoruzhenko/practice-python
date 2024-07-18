import pyaudio
p = pyaudio.PyAudio()
device_index = 6
for device in [p.get_device_info_by_index(i) for i in range(p.get_device_count())]:
  if device['name'] == 'Built-in Audio Analog Stereo':
    print(device)
    break
p.open(format=pyaudio.paInt16, channels=2, rate=48000, input=True, output=False, input_device_index=device_index)
