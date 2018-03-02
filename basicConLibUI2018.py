
import os
import functools
import logging
from PySide2 import QtGui, QtCore, QtUiTools, QtWidgets
from shiboken2 import wrapInstance
import pymel.core as pm
import maya.OpenMayaUI as omui 

_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)

import conGenSimplified as conGenAPI
reload(conGenAPI)

"""
to add a new path:
import sys 
sys.path.append( 'palce path here', Ex: 'C:\Users\yourName\Documents/folderName' )
import controllerLibUI as conLibUI
reload(conLibUI)
conLibUI.run()
"""

def getMayaWindow():
    """ Pointer to the Maya main window  
    """

    ptr = omui.MQtUtil.mainWindow()
    if ptr :
        return wrapInstance(long(ptr), QtWidgets.QMainWindow)

win = None


def run():
    """  Builds our UI
    """

    global win
    if win:
        win.close()
    win = CurveControllerLibraryUI(parent=getMayaWindow())
    win.show()


class CurveControllerLibraryUI(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(CurveControllerLibraryUI,self).__init__(parent)


        self.scaleValue = 1.0


        # index color mapping to rgb for Q pix map
        self.colorMapDictionary = {
        0:None,
        1:(0,0,0),
        2:(64,64,64),
        3:(128,128,128),
        4:(155,0,40),
        5:(0,4,96),
        6:(0,0,255),
        7:(0,75,25),
        8:(38,0,67),
        9:(200,0,200),
        10:(138,72,51),
        11:(63,35,31),
        12:(153,38,0),
        13:(255,0,0),
        14:(0,255,0),
        15:(0,65,153),
        16:(255,255,255),
        17:(255,255,0),
        18:(100,220,255),
        19:(67,255,163),
        20:(255,176,176),
        21:(228,172,121),
        22:(255,255,99),
        23:(0,153,84),
        24:(165,108,49),
        25:(158,160,48),
        26:(104,160,48),
        27:(48,161,94),
        28:(48,162,162),
        29:(48,102,160),
        30:(112,48,162),
        31:(162,48,106)
        }

        # top most layout
        self.setCentralWidget(QtWidgets.QWidget(self))        
        self.gridLayout = QtWidgets.QGridLayout()
        

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)

        # label
        self.conLabel = QtWidgets.QLabel('Simple Controller Library')
        self.verticalLayout.addWidget(self.conLabel)


        # conName
        self.conNameLineEdit = QtWidgets.QLineEdit()

        rx = QtCore.QRegExp("[0-9a-zA-Z_]*")
        validator = QtGui.QRegExpValidator(rx, self)

        self.conNameLineEdit.setValidator(validator)
        self.verticalLayout.addWidget(self.conNameLineEdit)

        # save button
        self.saveConbutton = QtWidgets.QPushButton('Save Controller')
        self.verticalLayout.addWidget(self.saveConbutton)

        self.defaultIconImage = os.path.join(conGenAPI.iconFolderPath, 'noIcon.png')
        thePixmap = QtGui.QPixmap(self.defaultIconImage)
        defaultIconScaled = thePixmap.scaledToWidth(400)

        self.imageLabel = QtWidgets.QLabel()
        self.imageLabel.setPixmap(defaultIconScaled)
        self.verticalLayout.addWidget(self.imageLabel)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)

        # color label
        self.colorLabel = QtWidgets.QLabel('Select Controller Color:')
        self.verticalLayout.addWidget(self.colorLabel)

        # colors
        self.buttonGridLayout = QtWidgets.QGridLayout()
        self.buttonGridLayout.setHorizontalSpacing(0)
        self.buttonGridLayout.setVerticalSpacing(0)
        self.buttonGroup = QtWidgets.QButtonGroup()


        buttonNumber = 0
        for i in range(4):
            for j in range(8):
                self.colorButton = QtWidgets.QPushButton("{0}".format(buttonNumber))
                self.colorButton.setMinimumSize(0,0)
                self.colorButton.setMaximumSize(60,60)
                self.colorButton.setCheckable(True)

                if buttonNumber == 0:
                    self.colorButton.setDisabled(True)
                    self.colorButton.setText("")
                else:
                    buttonColor = self.colorMapDictionary.get(buttonNumber)
                    _logger.debug('buttoncolor: {0}'.format(buttonColor))

                    needsDarkerText = [14,16,17,18,19,20,21,22]

                    if buttonNumber in needsDarkerText:
                        textColor = 'black'
                    else:
                        textColor = 'white'


                    self.colorButton.setStyleSheet('QPushButton {background-color: rgb(%d,%d,%d); color: %s;}' % (buttonColor[0],buttonColor[1],buttonColor[2], textColor))

                self.buttonGroup.addButton(self.colorButton)

                # adding buttons to the grid
                self.buttonGridLayout.addWidget(self.colorButton, i,j)

                buttonNumber += 1

        
        self.verticalLayout.addLayout(self.buttonGridLayout)

        # slider chunk
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.scaleLabel = QtWidgets.QLabel('Scale: ')
        self.horizontalLayout.addWidget(self.scaleLabel)
        self.scaleValLineEdit = QtWidgets.QLineEdit('1.0')
        self.horizontalLayout.addWidget(self.scaleValLineEdit)
        self.scaleSlider = QtWidgets.QSlider()
        self.scaleSlider.setMinimum(1)
        self.scaleSlider.setMaximum(100)
        self.scaleSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalLayout.addWidget(self.scaleSlider)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # list widget
        self.conListWidget = QtWidgets.QListWidget()
        self.verticalLayout.addWidget(self.conListWidget)

        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.makeConnections()
        self.setWindowTitle("CONTROLLER LIBRARY")
        self.centralWidget().setLayout(self.gridLayout)
        self.initUiState()
        self.show()
        
    def initUiState(self):
        """ Sets up the initial state of UI
        """

        self.updateListWidget()
        self.scaleSlider.setValue(self.scaleValue)



    def makeConnections(self):
        """ Connect events in UI 
        """

        self.conListWidget.itemDoubleClicked.connect(self.doubleClickedItem)
        self.conListWidget.itemClicked.connect(self.singleClickedItem)
        self.scaleSlider.valueChanged[int].connect(self.sliderEvent)
        self.scaleValLineEdit.editingFinished.connect(self.manualScaleEnteredEvent)
        self.saveConbutton.clicked.connect(self.saveControllerEvent)



    def updateListWidget(self):
        """ Updates the list widget
        """

        # returns sorted list
        conList = conGenAPI.consList()

        # emptying the list widget
        self.conListWidget.clear()

        for con in conList:
            item = QtWidgets.QListWidgetItem(con)
            self.conListWidget.addItem(item)


    def doubleClickedItem(self):
        """ When an item is double clicked
        """

        theListWidget = self.sender()

        curItem = theListWidget.currentItem()
        curItemText = curItem.text() 

        # get color
        currentButton = self.buttonGroup.checkedButton()

        color = int(currentButton.text()) if currentButton else 0


        conGenAPI.generateCon(conName=curItemText, scale = self.scaleValue, color=color)


    def sliderEvent(self,value):
        """ Sets the value of the slider
        """

        floatVal = float(value)/10.0
        self.scaleValLineEdit.setText(str(floatVal))
        self.scaleValue = floatVal




    def manualScaleEnteredEvent(self):
        """ When a manual scale is entered update the slider and scaleValue
        """
        
        tempScale = float(self.scaleValLineEdit.text())

        if tempScale < 0.1:
            self.scaleValue = 0.1
        elif tempScale > 10.0:
            self.scaleValue = 10.0
        else:
            self.scaleValue = tempScale
        
        self.scaleSlider.setValue(self.scaleValue * 10)



    def saveControllerEvent(self):
        """ Saves selected curve
        """

        sel = pm.selected()
        if sel and len(sel) == 1:

            try:
                crvShape = sel[0].getShape()
                if not crvShape.nodeType == 'nurbsCurve':
                    _logger.error("Selected is not a curve")
                else:
                    _logger.debug("selected a curve")

            except:
                _logger.error("error placeholder")

        else:
            _logger.debug("do you have something selected?")



        curveName = self.conNameLineEdit.text()
        if not curveName:
            _logger.error("No valid name entered")


        # save the curve
        conGenAPI.saveCon(con=sel[0], conName = curveName, doScreenGrab=True, debug =True)

        # update the list
        self.updateListWidget()



    def singleClickedItem(self):
        """ When an item is clicked in the list widget
        """


        theListWidget = self.sender()

        curItem = theListWidget.currentItem()
        curItemText = curItem.text() 

        picturePath = os.path.join(conGenAPI.iconFolderPath, '{0}.jpg'.format(curItemText))

        if not os.path.isfile(picturePath):
            picturePath = os.path.join(conGenAPI.iconFolderPath, '{0}.png'.format(curItemText))

        if not os.path.isfile(picturePath):
            picturePath = self.defaultIconImage
        
        newPixmap = QtGui.QPixmap(picturePath)
        scaledPixmap = newPixmap.scaledToWidth(400)

        self.imageLabel.setPixmap(scaledPixmap)
