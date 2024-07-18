import speech_recognition as sr

def recognize_from_microphone():
    # Создаем распознаватель речи
    recognizer = sr.Recognizer()

    # Используем микрофон в качестве источника звука
    with sr.Microphone() as source:
        print("Скажите что-нибудь...")
        # Настройка микрофона и подавление шума
        recognizer.adjust_for_ambient_noise(source)
        # Слушаем источник (микрофон)
        audio_data = recognizer.listen(source)
        print("Распознавание...")

        # Используем Google Web Speech API для распознавания речи
        try:
            # Преобразуем аудио в текст
            text = recognizer.recognize_google(audio_data, language="ru-RU")
            print("Вы сказали: " + text)
        except sr.UnknownValueError:
            print("Не удалось распознать речь")
        except sr.RequestError as e:
            print(f"Ошибка сервиса; проверьте подключение к интернету: {e}")

if __name__ == "__main__":
    recognize_from_microphone()
