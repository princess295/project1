# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\shelt\PycharmProjects\study\project\calc.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.threeButton = QtWidgets.QPushButton(Form)
        self.threeButton.setObjectName("threeButton")
        self.gridLayout.addWidget(self.threeButton, 2, 1, 1, 1)
        self.minusButton = QtWidgets.QPushButton(Form)
        self.minusButton.setObjectName("minusButton")
        self.gridLayout.addWidget(self.minusButton, 1, 0, 1, 1)
        self.delenButton = QtWidgets.QPushButton(Form)
        self.delenButton.setObjectName("delenButton")
        self.gridLayout.addWidget(self.delenButton, 4, 0, 1, 1)
        self.umnButton = QtWidgets.QPushButton(Form)
        self.umnButton.setObjectName("umnButton")
        self.gridLayout.addWidget(self.umnButton, 3, 0, 1, 1)
        self.procentButton = QtWidgets.QPushButton(Form)
        self.procentButton.setObjectName("procentButton")
        self.gridLayout.addWidget(self.procentButton, 2, 0, 1, 1)
        self.plusButton = QtWidgets.QPushButton(Form)
        self.plusButton.setObjectName("plusButton")
        self.gridLayout.addWidget(self.plusButton, 0, 0, 1, 1)
        self.twoButton = QtWidgets.QPushButton(Form)
        self.twoButton.setObjectName("twoButton")
        self.gridLayout.addWidget(self.twoButton, 1, 1, 1, 1)
        self.stepButton = QtWidgets.QPushButton(Form)
        self.stepButton.setObjectName("stepButton")
        self.gridLayout.addWidget(self.stepButton, 5, 0, 1, 1)
        self.ravnoButton = QtWidgets.QPushButton(Form)
        self.ravnoButton.setObjectName("ravnoButton")
        self.gridLayout.addWidget(self.ravnoButton, 6, 0, 1, 1)
        self.oneButton = QtWidgets.QPushButton(Form)
        self.oneButton.setObjectName("oneButton")
        self.gridLayout.addWidget(self.oneButton, 0, 1, 1, 1)
        self.eightButton = QtWidgets.QPushButton(Form)
        self.eightButton.setObjectName("eightButton")
        self.gridLayout.addWidget(self.eightButton, 0, 2, 1, 1)
        self.fourButton = QtWidgets.QPushButton(Form)
        self.fourButton.setObjectName("fourButton")
        self.gridLayout.addWidget(self.fourButton, 3, 1, 1, 1)
        self.fiveButton = QtWidgets.QPushButton(Form)
        self.fiveButton.setObjectName("fiveButton")
        self.gridLayout.addWidget(self.fiveButton, 4, 1, 1, 1)
        self.sixButton = QtWidgets.QPushButton(Form)
        self.sixButton.setObjectName("sixButton")
        self.gridLayout.addWidget(self.sixButton, 5, 1, 1, 1)
        self.sevenButton = QtWidgets.QPushButton(Form)
        self.sevenButton.setObjectName("sevenButton")
        self.gridLayout.addWidget(self.sevenButton, 6, 1, 1, 1)
        self.nineButton = QtWidgets.QPushButton(Form)
        self.nineButton.setObjectName("nineButton")
        self.gridLayout.addWidget(self.nineButton, 1, 2, 1, 1)
        self.zeroButton = QtWidgets.QPushButton(Form)
        self.zeroButton.setObjectName("zeroButton")
        self.gridLayout.addWidget(self.zeroButton, 2, 2, 1, 1)
        self.zzButton = QtWidgets.QPushButton(Form)
        self.zzButton.setObjectName("zzButton")
        self.gridLayout.addWidget(self.zzButton, 3, 2, 1, 1)
        self.clearButton = QtWidgets.QPushButton(Form)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 4, 2, 1, 1)
        self.deleteButton = QtWidgets.QPushButton(Form)
        self.deleteButton.setObjectName("deleteButton")
        self.gridLayout.addWidget(self.deleteButton, 5, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.threeButton.setText(_translate("Form", "3"))
        self.minusButton.setText(_translate("Form", "-"))
        self.delenButton.setText(_translate("Form", "/"))
        self.umnButton.setText(_translate("Form", "*"))
        self.procentButton.setText(_translate("Form", "%"))
        self.plusButton.setText(_translate("Form", "+"))
        self.twoButton.setText(_translate("Form", "2"))
        self.stepButton.setText(_translate("Form", "^"))
        self.ravnoButton.setText(_translate("Form", "="))
        self.oneButton.setText(_translate("Form", "1"))
        self.eightButton.setText(_translate("Form", "8"))
        self.fourButton.setText(_translate("Form", "4"))
        self.fiveButton.setText(_translate("Form", "5"))
        self.sixButton.setText(_translate("Form", "6"))
        self.sevenButton.setText(_translate("Form", "7"))
        self.nineButton.setText(_translate("Form", "9"))
        self.zeroButton.setText(_translate("Form", "0"))
        self.zzButton.setText(_translate("Form", "00"))
        self.clearButton.setText(_translate("Form", "C"))
        self.deleteButton.setText(_translate("Form", "00 -> 0"))

