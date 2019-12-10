import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

import hello_pyqt5

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = hello_pyqt5.MainWindow()
    ui.setipUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())