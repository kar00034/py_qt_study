from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from mysqlx.protobuf.mysqlx_pb2 import Ok


class LambdaUse(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("lambda_use.ui")
        self.ui.show()
        self.ui.btn_ok.clicked.connect(lambda stat, button=self.ui.btn_ok: self.showLabel(stat, button))
        # self.ui.btn_yes.clicked.connect(lambda stat, button=self.ui.btn_yes: self.showLabel(stat, button))
        self.ui.btn_yes.clicked.connect(
            lambda stat, text=self.ui.btn_yes.text(): self.showLabelText(stat, text))

    def showLabel(self, stat, button):
        text = button.text()
        # QMessageBox.information(self, 'btn_ok', text, QMessageBox, Ok)
        self.ui.lbl_res.setText(text)

    def showLabelText(self, stat, text):
        self.ui.lbl_res.setText(text)

    def showLabel2(self):
        text = self.ui.btn_yes.text()
        QMessageBox.information(self, 'btn_yes', text, QMessageBox, Ok)
        self.ui.lbl_res.setText(text)


if __name__ == "__main__":
    app = QApplication([])
    myapp = LambdaUse()
    app.exec_()
