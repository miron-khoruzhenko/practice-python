import speech_recognition as sr

def recognize_from_microphone():
    # Создаем распознаватель речи
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 0.6
    recognizer.dynamic_energy_threshold = False
    


    # Используем видео в качестве источника звука
    with sr.AudioFile('./captcha.wav') as source:
        print("Скажите что-нибудь...")
        # Настройка видео и подавление шума
        recognizer.adjust_for_ambient_noise(source)
        # Слушаем источник (видео)
        audio_data = recognizer.record(source)
        print("Распознавание...")

        # Используем Google Web Speech API для распознавания речи
        try:
            # Преобразуем аудио в текст
            text = recognizer.recognize_google(audio_data, language="de-DE")
            print("Вы сказали: " + text)
        except sr.UnknownValueError:
            print("Не удалось распознать речь")
        except sr.RequestError as e:
            print(f"Ошибка сервиса; проверьте подключение к интернету: {e}")

if __name__ == "__main__":
    recognize_from_microphone()
