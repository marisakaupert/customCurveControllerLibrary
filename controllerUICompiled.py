# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Marisa\Documents\cgCircuit/controllerUIDesigner.ui'
#
# Created: Fri May 19 12:38:23 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(658, 719)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.conLabel = QtGui.QLabel(Dialog)
        self.conLabel.setObjectName("conLabel")
        self.verticalLayout.addWidget(self.conLabel)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scaleLabel = QtGui.QLabel(Dialog)
        self.scaleLabel.setObjectName("scaleLabel")
        self.horizontalLayout.addWidget(self.scaleLabel)
        self.scaleValLineEdit = QtGui.QLineEdit(Dialog)
        self.scaleValLineEdit.setObjectName("scaleValLineEdit")
        self.horizontalLayout.addWidget(self.scaleValLineEdit)
        self.scaleSlider = QtGui.QSlider(Dialog)
        self.scaleSlider.setOrientation(QtCore.Qt.Horizontal)
        self.scaleSlider.setObjectName("scaleSlider")
        self.horizontalLayout.addWidget(self.scaleSlider)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.conNameLineEdit = QtGui.QLineEdit(Dialog)
        self.conNameLineEdit.setObjectName("conNameLineEdit")
        self.verticalLayout.addWidget(self.conNameLineEdit)
        self.saveConbutton = QtGui.QPushButton(Dialog)
        self.saveConbutton.setObjectName("saveConbutton")
        self.verticalLayout.addWidget(self.saveConbutton)
        self.conListWidget = QtGui.QListWidget(Dialog)
        self.conListWidget.setObjectName("conListWidget")
        self.verticalLayout.addWidget(self.conListWidget)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.conLabel.setText(QtGui.QApplication.translate("Dialog", "Simple Controller Library", None, QtGui.QApplication.UnicodeUTF8))
        self.scaleLabel.setText(QtGui.QApplication.translate("Dialog", "Scale: ", None, QtGui.QApplication.UnicodeUTF8))
        self.scaleValLineEdit.setText(QtGui.QApplication.translate("Dialog", "1.0", None, QtGui.QApplication.UnicodeUTF8))
        self.saveConbutton.setText(QtGui.QApplication.translate("Dialog", "PushButton", None, QtGui.QApplication.UnicodeUTF8))

