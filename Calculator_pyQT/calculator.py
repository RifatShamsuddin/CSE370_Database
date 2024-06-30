import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.input_line = QLineEdit()
        self.layout.addWidget(self.input_line)

        button_grid_1 = QHBoxLayout()
        button_grid_2 = QHBoxLayout()
        button_grid_3 = QHBoxLayout()
        button_grid_4 = QHBoxLayout()
        button_grid_1.addWidget(self.create_button("7"))
        button_grid_1.addWidget(self.create_button("8"))
        button_grid_1.addWidget(self.create_button("9"))
        button_grid_2.addWidget(self.create_button("4"))
        button_grid_2.addWidget(self.create_button("5"))
        button_grid_2.addWidget(self.create_button("6"))
        button_grid_3.addWidget(self.create_button("1"))
        button_grid_3.addWidget(self.create_button("2"))
        button_grid_3.addWidget(self.create_button("3"))
        button_grid_4.addWidget(self.create_button("0"))

        operation_grid = QVBoxLayout()
        operation_grid.addWidget(self.create_button("+"))
        operation_grid.addWidget(self.create_button("-"))
        operation_grid.addWidget(self.create_button("*"))
        operation_grid.addWidget(self.create_button("/"))
        operation_grid.addWidget(self.create_button("="))
        operation_grid.addWidget(self.create_button("C"))

        self.layout.addLayout(button_grid_1)
        self.layout.addLayout(button_grid_2)
        self.layout.addLayout(button_grid_3)
        self.layout.addLayout(button_grid_4)

        self.layout.addLayout(operation_grid)

        self.setLayout(self.layout)

    def create_button(self, text):
        button = QPushButton(text)
        button.clicked.connect(self.on_button_click)
        return button

    def on_button_click(self):
        sender = self.sender()
        current_text = self.input_line.text()
        button_text = sender.text()

        if button_text == "=":
            try:
                result = eval(current_text)
                self.input_line.setText(str(result))
            except Exception as e:
                self.input_line.setText("Error")
        elif button_text == "C":
            self.input_line.clear()
        else:
            new_text = current_text + button_text
            self.input_line.setText(new_text)

def main():
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
