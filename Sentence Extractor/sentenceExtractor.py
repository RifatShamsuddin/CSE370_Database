import re
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton


def extract_sentences_with_words(text, words):
    # Regex sentence extractor
    words_pattern = '|'.join(re.escape(word) for word in words)
    sentence_pattern = fr'[A-Za-z0-9\s\-\,\;\:\'\"\(\)\[\]\{\}\!\?]+[\.!\?](?=\s*({words_pattern})\s*[\.!\?]|$)'
    sentences = re.findall(sentence_pattern, text)
    sentences = [sentence.strip() for sentence in sentences]
    return sentences


class SentenceExtractorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Sentence Extractor')
        self.setGeometry(100, 100, 800, 600)

        # Widgets
        self.words_label = QLabel('Enter specified words (comma-separated):')
        self.words_input = QLineEdit()
        self.paragraph_label = QLabel('Enter the paragraph or essay:')
        self.paragraph_input = QTextEdit()
        self.extract_button = QPushButton('Extract Sentences')
        self.extracted_sentences_label = QLabel()

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.words_label)
        layout.addWidget(self.words_input)
        layout.addWidget(self.paragraph_label)
        layout.addWidget(self.paragraph_input)
        layout.addWidget(self.extract_button)
        layout.addWidget(self.extracted_sentences_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Button click event
        self.extract_button.clicked.connect(self.extract_sentences)

    def extract_sentences(self):
        # Get the specified words and the paragraph text
        specified_words = self.words_input.text().split(',')
        paragraph_text = self.paragraph_input.toPlainText()

        # Extract sentences containing the specified words
        extracted_sentences = extract_sentences_with_words(paragraph_text, specified_words)

        # Display the extracted sentences
        if extracted_sentences:
            sentences_text = '\n'.join(extracted_sentences)
            self.extracted_sentences_label.setText(sentences_text)
        else:
            self.extracted_sentences_label.setText('No sentences containing the specified words were found.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SentenceExtractorApp()
    window.show()
    sys.exit(app.exec_())
