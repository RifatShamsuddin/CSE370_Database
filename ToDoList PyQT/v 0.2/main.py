import sys
from PyQt5.QtWidgets import QApplication, QCheckBox, QMainWindow, QVBoxLayout, QWidget, QListWidget, QLineEdit, QPushButton, QTextEdit
from datetime import datetime


class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.status = True

    def get_entry(self):
        task_entry = f"{self.name}"
        return task_entry


class ToDoListApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List")
        self.setGeometry(100, 100, 500, 400)

        # Create the main layout
        layout = QVBoxLayout()

        # Create the list widget to display tasks
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        # Create the line edit widget for task name
        self.task_input = QLineEdit()
        layout.addWidget(self.task_input)

        # Create the text edit widget for task description
        self.description_edit = QTextEdit()
        layout.addWidget(self.description_edit)

        # Create the "Add Task" button
        add_button = QPushButton("Add Task")
        add_button.clicked.connect(self.add_task)
        layout.addWidget(add_button)

        # Create the "Delete Task" button
        delete_button = QPushButton("Delete Task")
        delete_button.clicked.connect(self.delete_task)
        layout.addWidget(delete_button)

        # Create the "Save Tasks" button
        save_button = QPushButton("Save Tasks")
        save_button.clicked.connect(self.save_tasks)
        layout.addWidget(save_button)

        # Create the central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Task counter
        self.task_counter = 1
        self.tasks = []

    def add_task(self):
        task_name = self.task_input.text()
        task_description = self.description_edit.toPlainText()
        if task_name:
            task = Task(task_name, task_description)
            self.tasks.append(task)
            task_entry = task.get_entry()
            checkbox = QCheckBox()
            self.list_widget.addItem(task_entry, checkbox)
            self.task_input.clear()
            self.description_edit.clear()
            self.task_counter += 1

    def delete_task(self):
        selected_row = self.list_widget.currentRow()
        if selected_row >= 0:
            self.list_widget.takeItem(selected_row)
            del self.tasks[selected_row]

    def save_tasks(self):
        current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"tasks_{current_date}.txt"
        with open(filename, "w") as file:
            for task in self.tasks:
                task_entry = task.get_entry()
                file.write(task_entry + "\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_app = ToDoListApp()
    todo_app.show()
    sys.exit(app.exec_())
