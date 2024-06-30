import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QListWidget, QLineEdit, QPushButton


class ToDoListApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List")
        self.setGeometry(100, 100, 300, 400)

        # Create the main layout
        layout = QVBoxLayout()

        # Create the list widget to display tasks
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        # Create the line edit widget to add new tasks
        self.task_input = QLineEdit()
        layout.addWidget(self.task_input)

        # Create the "Add Task" button
        add_button = QPushButton("Add Task")
        add_button.clicked.connect(self.add_task)
        layout.addWidget(add_button)

        # Create the "Delete Task" button
        delete_button = QPushButton("Delete Task")
        delete_button.clicked.connect(self.delete_task)
        layout.addWidget(delete_button)

        # Create the central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def add_task(self):
        task = self.task_input.text()
        if task:
            self.list_widget.addItem(task)
            self.task_input.clear()

    def delete_task(self):
        selected_item = self.list_widget.currentItem()
        if selected_item:
            self.list_widget.takeItem(self.list_widget.row(selected_item))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_app = ToDoListApp()
    todo_app.show()
    sys.exit(app.exec_())
