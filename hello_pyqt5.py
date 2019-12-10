import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("hello_pyqt5.ui")
        self.ui.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyApp()
    app.exec_()
