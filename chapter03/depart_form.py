from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QAbstractItemView, QHeaderView, QTableWidgetItem, QAction, \
    QMessageBox


def create_table(table=None, data=None):
    table.setHorizontalHeaderLabels(data)
    # row단위 선택
    table.setSelectionBehavior(QAbstractItemView.SelectRows)
    # 수정불가능
    table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    # 균일한 간격으로 재배치
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    return table


class DepartUI(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("dept_form.ui")
        self.ui.show()

        self.table = create_table(table=self.ui.tableWidget, data=("부서번호", "부서명", "위치"))

        # slot/signal
        self.ui.btn_add.clicked.connect(self.add_item)
        self.ui.btn_init.clicked.connect(self.init_item)

        # 마우스 우클릭시 메뉴
        self.set_context_menu(self.table)

        data = [(1, "마케팅", 8), (2, "개발", 10), (3, "인사", 20)]
        self.load_data(data)

    def load_data(self, data):
        for idx, (no, name, floor) in enumerate(data):
            item_no, item_name, item_floor = self.create_item(floor, name, no)
            nextIdx = self.table.rowCount()
            self.table.insertRow(nextIdx)
            self.table.setItem(nextIdx, 0, item_no)
            self.table.setItem(nextIdx, 1, item_name)
            self.table.setItem(nextIdx, 2, item_floor)

    def set_context_menu(self, tv):
        tv.setContextMenuPolicy(Qt.ActionsContextMenu)
        update_action = QAction("수정 (&u)", tv)
        delete_action = QAction("삭제 (&d)", tv)
        tv.addAction(update_action)
        tv.addAction(delete_action)
        update_action.triggered.connect(self.__update)
        delete_action.triggered.connect(self.__delete)

    def __update(self):
        QMessageBox.information(self, 'Update', "확인", QMessageBox.Ok)
        item_no, item_name, item_floor = self.get_item_form_le()
        selectionIdxs = self.table.selectedIndexes()[0]
        self.table.setItem(selectionIdxs.row(), 0, item_no)
        self.table.setItem(selectionIdxs.row(), 1, item_name)
        self.table.setItem(selectionIdxs.row(), 2, item_floor)

    def __delete(self):
        QMessageBox.information(self, 'Delete', "확인", QMessageBox.Ok)
        selectionIdxs = self.table.selectedIndexes()[0]
        print(selectionIdxs.row(), " ", selectionIdxs.column())
        self.table.removeRow(selectionIdxs.row())

    def add_item(self):
        item_no, item_name, item_floor = self.get_item_form_le()
        currentIdx = self.table.rowCount()
        # print(type(currentIdx))
        self.table.insertRow(currentIdx)
        self.table.setItem(currentIdx, 0, item_no)
        self.table.setItem(currentIdx, 1, item_name)
        self.table.setItem(currentIdx, 2, item_floor)
        self.init_item()

    def get_item_form_le(self):
        no = self.ui.le_no.text()
        name = self.ui.le_name.text()
        floor = self.ui.le_floor.text()
        return self.create_item(floor, name, no)

    def create_item(self, floor, name, no):
        item_no = QTableWidgetItem()
        item_no.setTextAlignment(Qt.AlignCenter)
        item_no.setData(Qt.DisplayRole, no)
        item_name = QTableWidgetItem()
        item_name.setTextAlignment(Qt.AlignCenter)
        item_name.setData(Qt.DisplayRole, name)
        item_floor = QTableWidgetItem()
        item_floor.setTextAlignment(Qt.AlignCenter)
        item_floor.setData(Qt.DisplayRole, floor)
        return item_floor, item_name, item_no

    def init_item(self):
        self.ui.le_no.clear()
        self.ui.le_name.clear()
        self.ui.le_floor.clear()


if __name__ == "__main__":
    app = QApplication([])
    w = DepartUI()
    app.exec_()
