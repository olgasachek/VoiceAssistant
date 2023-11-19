import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QVBoxLayout, QLabel, QPushButton
from micro_speech_recognition import MicroSpeechRecognition


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Распознование голоса'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 100
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget = MainWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()


class MainWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.push_button = QPushButton('Распознать голос')
        self.push_button.clicked.connect(self.recognise_speech)

        self.recognised_text = 'Текст появится здесь после распознования'
        self.recognized_text_label = QLabel(self)
        self.recognized_text_label.setText(self.recognised_text)

        self.one_more_label = QLabel(self)
        self.one_more_label.setText('Еще одно поле')

        self.layout.addWidget(self.push_button)
        self.layout.addWidget(self.recognized_text_label)
        self.layout.addWidget(self.one_more_label)
        self.setLayout(self.layout)

        self.speech_rec = MicroSpeechRecognition()

    def recognise_speech(self):
        self.recognised_text = self.speech_rec.get_speech()
        if self.recognised_text is None:
            self.recognised_text = 'Распознование текста не получилось'
        self.recognized_text_label.setText(self.recognised_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())
