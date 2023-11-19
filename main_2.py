import json
import speech_recognition as sr
from sentence_transformers  import SentenceTransformer
import numpy as np

class MicroSpeechRecognition:

    def __init__(self):
        self.recognizer = sr.Recognizer()

        self.mic = sr.Microphone()
        self.s = sr.Microphone.list_working_microphones()
        self.commands = ['Пуск жатки', 'Стоп жатки', 'Верхнее положение жатки', 'Нижнее положение жатки', 'Выше жатку', 'Ниже жатку']
        self.recognised_text = ''

    def get_speech(self):
        with sr.Microphone() as microphone_source:
            recorded_audio = self.recognizer.listen(microphone_source)

        try:
            recognised_text = self.recognizer.recognize_vosk(recorded_audio)
            print('raw recognised_text: ', recognised_text)
            self.recognised_text = json.loads(recognised_text)['text']
            return self.recognised_text
        except sr.UnknownValueError:
            print("Извините, не удалось распознать речь.")
        except sr.RequestError as e:
            print("Ошибка сервиса распознавания речи; {0}".format(e))

    def find_command(self):
        model = SentenceTransformer('distilbert-base-nli-mean-tokens')

        embedding_user = model.encode(self.recognised_text)
        for command in self.commands:
          embedding2 = model.encode(command)

          # calculate the cosine similarity between the embeddings
          cosine_similarity = lambda x, y: np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))
          similarity_score = cosine_similarity(embedding_user, embedding2)

          # print the similarity score
          print(f'Для команды "{command}" степень сходства = {similarity_score:.2f}')


if __name__ == '__main__':
    speech_rec = MicroSpeechRecognition()
    recognised_text = speech_rec.get_speech()
    if recognised_text is None:
        recognised_text = 'Распознавание текста не получилось'
    print(recognised_text)
    speech_rec.find_command();
