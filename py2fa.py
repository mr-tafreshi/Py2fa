# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/py2fa.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(514, 670)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame{\n"
"background-color:#070708;\n"
"border-radius:20px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.TitleLabel = QtWidgets.QLabel(self.frame)
        self.TitleLabel.setGeometry(QtCore.QRect(190, 30, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Telugu UI")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setStyleSheet("color : #abcf29;")
        self.TitleLabel.setObjectName("TitleLabel")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(40, 140, 431, 51))
        self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget.setStyleSheet("background-color : #2f3032; border-radius:20px;")
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(310, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("NotoSansMono Nerd Font")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color : #abcf29;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("NotoSansMono Nerd Font")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color : #abcf29;")
        self.label_3.setObjectName("label_3")
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setGeometry(QtCore.QRect(40, 220, 431, 51))
        self.widget_2.setStyleSheet("background-color : #2f3032; border-radius:20px;")
        self.widget_2.setObjectName("widget_2")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(310, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("NotoSansMono Nerd Font")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color : #abcf29;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("NotoSansMono Nerd Font")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color : #abcf29;")
        self.label_5.setObjectName("label_5")
        self.widget_3 = QtWidgets.QWidget(self.frame)
        self.widget_3.setGeometry(QtCore.QRect(40, 300, 431, 51))
        self.widget_3.setStyleSheet("background-color : #2f3032; border-radius:20px;")
        self.widget_3.setObjectName("widget_3")
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(310, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("NotoSansMono Nerd Font")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color : #abcf29;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily("NotoSansMono Nerd Font")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color : #abcf29;")
        self.label_7.setObjectName("label_7")
        self.widget_4 = QtWidgets.QWidget(self.frame)
        self.widget_4.setGeometry(QtCore.QRect(40, 380, 431, 51))
        self.widget_4.setStyleSheet("background-color : #2f3032; border-radius:20px;")
        self.widget_4.setObjectName("widget_4")
        self.label_8 = QtWidgets.QLabel(self.widget_4)
        self.label_8.setGeometry(QtCore.QRect(310, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("NotoSansMono Nerd Font")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color : #abcf29;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget_4)
        self.label_9.setGeometry(QtCore.QRect(20, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily("NotoSansMono Nerd Font")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color : #abcf29;")
        self.label_9.setObjectName("label_9")
        self.AddButton = QtWidgets.QPushButton(self.frame)
        self.AddButton.setEnabled(True)
        self.AddButton.setGeometry(QtCore.QRect(390, 40, 51, 41))
        self.AddButton.setMouseTracking(False)
        self.AddButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.AddButton.setToolTip("")
        self.AddButton.setAutoFillBackground(False)
        self.AddButton.setStyleSheet("QPushButton{\n"
"background-color: #2f3032;\n"
"color: #abcf29;\n"
"border-radius:5px;\n"
"}\n"
"")
        self.AddButton.setDefault(False)
        self.AddButton.setFlat(False)
        self.AddButton.setObjectName("AddButton")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TitleLabel.setText(_translate("MainWindow", "Py2fa"))
        self.label_2.setText(_translate("MainWindow", "999 301"))
        self.label_3.setText(_translate("MainWindow", "Discord"))
        self.label_4.setText(_translate("MainWindow", "999 301"))
        self.label_5.setText(_translate("MainWindow", "Google"))
        self.label_6.setText(_translate("MainWindow", "999 301"))
        self.label_7.setText(_translate("MainWindow", "Microsoft"))
        self.label_8.setText(_translate("MainWindow", "999 301"))
        self.label_9.setText(_translate("MainWindow", "Instagram"))
        self.AddButton.setText(_translate("MainWindow", "Add"))
