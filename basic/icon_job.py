from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QToolTip, QMainWindow, QVBoxLayout, QHBoxLayout


class MyIcon(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Icon")
        # self.SetWindowIcon(QIcon("img/web.png"))
        self.setGeometry(300, 300, 300, 200)

        # self.statusBar().showMessage('Ready', 3000)
        # self.st1atusBar().clearMessage()

        btn = QPushButton("quit", self)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())

        btn2 = QPushButton("setStatusMessage", self)
        btn2.move(150, 50)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn)
        hbox.addWidget(btn2)
        hbox.addStretch(2)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(QPushButton("test"))
        hbox2.addWidget(QPushButton("test2"))
        hbox2.addStretch(2)

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addStretch(1)

        self.setLayout(vbox)

        #풍선 도움말
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        #종료
        # btn.clicked.connect(QCoreApplication.instance().quit)
        btn.clicked.connect(self.clearStatus)
        # btn2.clicked.connect(self.setStatusMsg)
        self.show()


    def clearStatus(self):
        self.statusBar().clearMessage()

    def setStatusMsg(self):
        self.statusBar().showMessage("set Message")


if __name__ == "__main__":
    app = QApplication([])
    w = MyIcon()
    app.exec_()