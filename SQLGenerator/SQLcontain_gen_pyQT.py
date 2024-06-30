import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class GoogleSheetsSQLGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Google Sheets SQL Code Generator')
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        self.range_label = QLabel('Table Range (e.g., Sheet1!A1:H10):')
        self.range_input = QLineEdit()
        self.layout.addWidget(self.range_label)
        self.layout.addWidget(self.range_input)

        self.column_label = QLabel('Column to Search (e.g., D):')
        self.column_input = QLineEdit()
        self.layout.addWidget(self.column_label)
        self.layout.addWidget(self.column_input)

        self.value_label = QLabel('Search Value:')
        self.value_input = QLineEdit()
        self.layout.addWidget(self.value_label)
        self.layout.addWidget(self.value_input)

        self.generate_button = QPushButton('Generate SQL Code')
        self.generate_button.clicked.connect(self.generate_sql_code)
        self.layout.addWidget(self.generate_button)

        self.sql_label = QLabel()
        self.layout.addWidget(self.sql_label)

        self.setLayout(self.layout)

    def generate_sql_code(self):
        table_range = self.range_input.text()
        column = self.column_input.text()
        search_value = self.value_input.text()

        sql_code = f"=QUERY({table_range}, \"SELECT * WHERE {column} CONTAINS '{search_value}'\", 0)"
        self.sql_label.setText(sql_code)

def main():
    app = QApplication(sys.argv)
    window = GoogleSheetsSQLGenerator()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
