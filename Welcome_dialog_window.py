from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrameW(object):
    def setupUiW(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(500, 600)
        Frame.setMinimumSize(QtCore.QSize(500, 600))
        Frame.setMaximumSize(QtCore.QSize(500, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("peptid logo/logo1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Frame.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 451, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("peptid logo/Welcome.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 451, 361))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("peptid logo/logo1.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(400, 500, 80, 80))
        self.pushButton.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton.setMaximumSize(QtCore.QSize(80, 80))
        self.pushButton.setStyleSheet("QPushButton{background: transparent;}")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("peptid logo/ON.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(100, 100))
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Frame)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 500, 80, 80))
        self.pushButton_2.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_2.setMaximumSize(QtCore.QSize(80, 80))
        self.pushButton_2.setStyleSheet("QPushButton{background:transparent;}")
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("peptid logo/Off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Frame)
        self.pushButton.clicked.connect(Frame.close)
        QtCore.QMetaObject.connectSlotsByName(Frame)

        self.pushButton_2.clicked.connect(exit)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "PeptideMassCalculator - Welcome"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_FrameW()
    ui.setupUiW(Frame)
    Frame.show()
    sys.exit(app.exec_())
