# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 190)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 20, 381, 161))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_name = QtWidgets.QLabel(self.widget)
        self.lbl_name.setObjectName("lbl_name")
        self.gridLayout.addWidget(self.lbl_name, 0, 0, 1, 1)
        self.lbl_width = QtWidgets.QLabel(self.widget)
        self.lbl_width.setObjectName("lbl_width")
        self.gridLayout.addWidget(self.lbl_width, 1, 0, 1, 1)
        self.lbl_height = QtWidgets.QLabel(self.widget)
        self.lbl_height.setObjectName("lbl_height")
        self.gridLayout.addWidget(self.lbl_height, 2, 0, 1, 1)
        self.lbl_color = QtWidgets.QLabel(self.widget)
        self.lbl_color.setObjectName("lbl_color")
        self.gridLayout.addWidget(self.lbl_color, 3, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.le_name = QtWidgets.QLineEdit(self.widget)
        self.le_name.setObjectName("le_name")
        self.verticalLayout_2.addWidget(self.le_name)
        self.spin_width = QtWidgets.QSpinBox(self.widget)
        self.spin_width.setProperty("value", 32)
        self.spin_width.setObjectName("spin_width")
        self.verticalLayout_2.addWidget(self.spin_width)
        self.spin_height = QtWidgets.QSpinBox(self.widget)
        self.spin_height.setProperty("value", 32)
        self.spin_height.setObjectName("spin_height")
        self.verticalLayout_2.addWidget(self.spin_height)
        self.cmb_color = QtWidgets.QComboBox(self.widget)
        self.cmb_color.setObjectName("cmb_color")
        self.verticalLayout_2.addWidget(self.cmb_color)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_ok = QtWidgets.QPushButton(self.widget)
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout_2.addWidget(self.btn_ok)
        self.btn_cancel = QtWidgets.QPushButton(self.widget)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_2.addWidget(self.btn_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "사용자입력폼"))
        self.lbl_name.setText(_translate("Form", "Name:"))
        self.lbl_width.setText(_translate("Form", "Width:"))
        self.lbl_height.setText(_translate("Form", "Height:"))
        self.lbl_color.setText(_translate("Form", "Color depth:"))
        self.le_name.setText(_translate("Form", "Untitled image"))
        self.btn_ok.setText(_translate("Form", "OK"))
        self.btn_cancel.setText(_translate("Form", "Cancel"))

