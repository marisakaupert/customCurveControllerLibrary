# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Marisa\Documents\cgCircuit/controllerUIDesigner.ui'
#
# Created: Fri May 19 12:38:23 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!


        self.gridLayout = QtGui.QGridLayout()

        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)

        self.conLabel = QtGui.QLabel('Simple Controller Library')

        self.verticalLayout.addWidget(self.conLabel)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)

        self.scaleLabel = QtGui.QLabel('Scale: ')

        self.horizontalLayout.addWidget(self.scaleLabel)
        self.scaleValLineEdit = QtGui.QLineEdit('1.0')

        self.horizontalLayout.addWidget(self.scaleValLineEdit)
        self.scaleSlider = QtGui.QSlider()
        self.scaleSlider.setOrientation(QtCore.Qt.Horizontal)

        self.horizontalLayout.addWidget(self.scaleSlider)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.conNameLineEdit = QtGui.QLineEdit()

        self.verticalLayout.addWidget(self.conNameLineEdit)
        self.saveConbutton = QtGui.QPushButton('Save Controller')

        self.verticalLayout.addWidget(self.saveConbutton)
        self.conListWidget = QtGui.QListWidget()

        self.verticalLayout.addWidget(self.conListWidget)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

  
