import speech_recognition as sr

import requests

# headers= {
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0",
#     "Accept": "audio/webm,audio/ogg,audio/wav,audio/*;q=0.9,application/ogg;q=0.7,video/*;q=0.6,*/*;q=0.5",
#     "Accept-Language": "ru,tr-TR;q=0.8,tr;q=0.6,en-US;q=0.4,en;q=0.2",
#     "Range": "bytes=0-",
#     "Sec-Fetch-Dest": "audio",
#     "Sec-Fetch-Mode": "no-cors",
#     "Sec-Fetch-Site": "same-site",
#     "Cookie" : "cookie_consent=accepted; marketing_consent=accepted; personalization_consent=accepted; rest=024dae17b4-4300-45o8VdIpevHM6FqPtHncUpoCZ6uQbLlbsTbF46u6fnPcpaEtlrjYkklfDupnPEQdzKjWo; OAMAuthnHintCookie=0@1715815698"
# }
# res = requests.get('https://rest.arbeitsagentur.de/idaas/id-aas-service/ct/v1/captcha/6C05754F-C526-4D76-88DE-7286F945FE4A?type=audio&languageIso639Code=de', headers=headers)

# print(res.status_code)

# with open('captcha.wav', 'wb') as f:
#     f.write(res.content)


def recognize_from_microphone():
    # Создаем распознаватель речи
    recognizer = sr.Recognizer()
    # recognizer.pause_threshold = 0.5
    recognizer.dynamic_energy_threshold = False
    # recognizer.non_speaking_duration = 0.2
    
    # Используем видео в качестве источника звука
    with sr.AudioFile('./mywav_reduced_noise.wav') as source:
        audio = recognizer.listen(source)
        # Слушаем источник (видео)
        audio_data = recognizer.record(source)
        print("Распознавание...")

        # Используем Google Web Speech API для распознавания речи
        try:
            # Преобразуем аудио в текст
            text = recognizer.recognize_google(audio, language="de-DE").lower()
            print("Вы сказали: " + text)
        except sr.UnknownValueError:
            print("Не удалось распознать речь")
        except sr.RequestError as e:
            print(f"Ошибка сервиса; проверьте подключение к интернету: {e}")

if __name__ == "__main__":
    recognize_from_microphone()
