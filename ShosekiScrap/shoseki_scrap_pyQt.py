import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QVBoxLayout, QWidget

class TextProcessingApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Text Processing App')

        layout = QVBoxLayout()

        self.label = QLabel('Enter Text:', self)
        layout.addWidget(self.label)

        self.input_textbox = QTextEdit(self)
        layout.addWidget(self.input_textbox)
        self.input_textbox.acceptRichText = False  # Set acceptRichText to False

        self.process_button = QPushButton('Process and Save', self)
        layout.addWidget(self.process_button)
        self.process_button.clicked.connect(self.processAndSave)

        self.clear_button = QPushButton('Clear', self)
        layout.addWidget(self.clear_button)
        self.clear_button.clicked.connect(self.clearInput)

        self.result_label = QLabel(self)
        layout.addWidget(self.result_label)

        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def processAndSave(self):
        input_text = self.input_textbox.toPlainText()

        # Read the date range from the input text
        date_range_str, *input_lines = input_text.split('\n')

        # Process the input and append the date range
        output_lines = []
        for line in input_lines:
            line = line.strip()  # Remove leading/trailing whitespaces
            if line:
                line_with_date = f"{date_range_str}\t{line}"
                output_lines.append(line_with_date)

        # Append the processed data to the output text file
        with open('output_text.txt', 'a', encoding='utf-8') as output_file:
            # Add a separator between the last line of previous text and the new data
            if output_lines:
                output_file.write('\n')
            output_file.write('\n'.join(output_lines))

        with open('output_text.txt', 'r', encoding='utf-8') as output_file:
            num_lines = len(output_file.readlines())

        self.result_label.setText(f"Program execution is done.\nNumber of lines in output file: {num_lines}\nLast Date {date_range_str}")

    def clearInput(self):
        self.input_textbox.clear()
        self.result_label.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TextProcessingApp()
    window.show()
    sys.exit(app.exec_())
