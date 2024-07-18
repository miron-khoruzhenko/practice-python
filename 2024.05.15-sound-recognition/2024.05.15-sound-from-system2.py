import pyaudio
import wave

def record_audio(filename, duration=10, sample_rate=44100, chunk_size=1024):
    audio_format = pyaudio.paInt16
    channels = 2

    p = pyaudio.PyAudio()

    # Открыть поток для записи
    stream = p.open(format=audio_format,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    input_device_index=3,
                    frames_per_buffer=chunk_size)

    frames = []

    print("Recording...")
    for i in range(0, int(sample_rate / chunk_size * duration)):
        data = stream.read(chunk_size)
        frames.append(data)
    print("Finished recording.")

    # Остановить и закрыть поток
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Сохранить записанный звук в WAV файл
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(audio_format))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))
    wf.close()

# Записать 10 секунд звука в файл 'output.wav'
record_audio('output.wav', duration=10)
