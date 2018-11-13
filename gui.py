# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'autobot.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(401, 183)
        self.start = QtWidgets.QPushButton(Dialog)
        self.start.setGeometry(QtCore.QRect(230, 150, 75, 23))
        self.start.setObjectName("start")
        self.end = QtWidgets.QPushButton(Dialog)
        self.end.setGeometry(QtCore.QRect(320, 150, 75, 23))
        self.end.setObjectName("end")
        self.sllineedit = QtWidgets.QLineEdit(Dialog)
        self.sllineedit.setGeometry(QtCore.QRect(250, 60, 113, 20))
        self.sllineedit.setObjectName("sllineedit")
        self.tplineedit = QtWidgets.QLineEdit(Dialog)
        self.tplineedit.setGeometry(QtCore.QRect(60, 60, 113, 20))
        self.tplineedit.setObjectName("tplineedit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 60, 31, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(220, 60, 31, 20))
        self.label_2.setObjectName("label_2")
        self.tradeamountlineedit = QtWidgets.QLineEdit(Dialog)
        self.tradeamountlineedit.setGeometry(QtCore.QRect(200, 100, 113, 20))
        self.tradeamountlineedit.setObjectName("tradeamountlineedit")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(110, 100, 81, 20))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 51, 20))
        self.label_3.setObjectName("label_3")
        self.labelbalance = QtWidgets.QLabel(Dialog)
        self.labelbalance.setGeometry(QtCore.QRect(70, 150, 141, 20))
        self.labelbalance.setObjectName("labelbalance")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 71, 20))
        self.label_4.setObjectName("label_4")
        self.file_path_field = QtWidgets.QLineEdit(Dialog)
        self.file_path_field.setGeometry(QtCore.QRect(100, 20, 261, 20))
        self.file_path_field.setObjectName("file_path_field")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.start.setText(_translate("Dialog", "Start"))
        self.end.setText(_translate("Dialog", "End"))
        self.label.setText(_translate("Dialog", "TP %"))
        self.label_2.setText(_translate("Dialog", "SL %"))
        self.label_5.setText(_translate("Dialog", "TRADE AMOUNT"))
        self.label_3.setText(_translate("Dialog", "Balance:"))
        self.labelbalance.setText(_translate("Dialog", "0.0"))
        self.label_4.setText(_translate("Dialog", "Data File Path"))

