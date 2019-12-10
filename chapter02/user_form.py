from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication


class UserForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("user_form.ui")
        self.ui.show()


if __name__ == "__main__":
    app = QApplication([])
    w = UserForm()
    app.exec_()
