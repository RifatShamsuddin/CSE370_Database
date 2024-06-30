import sys
from PyQt5.QtWidgets import QApplication
from main import ToDoListApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_app = ToDoListApp()
    todo_app.show()
    sys.exit(app.exec_())