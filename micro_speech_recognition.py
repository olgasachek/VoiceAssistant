import speech_recognition as sr
import json


class MicroSpeechRecognition:

    def __init__(self):
        self.recognizer = sr.Recognizer()

        self.mic = sr.Microphone()
        self.s = sr.Microphone.list_working_microphones()

    def get_speech(self):
        with sr.Microphone() as microphone_source:
            recorded_audio = self.recognizer.listen(microphone_source)

        try:
            recognised_text = self.recognizer.recognize_vosk(recorded_audio)
            recognised_text = json.loads(recognised_text)['text']
            return recognised_text
        except sr.UnknownValueError:
            print("Извините, не удалось распознать речь.")
        except sr.RequestError as e:
            print("Ошибка сервиса распознавания речи; {0}".format(e))
