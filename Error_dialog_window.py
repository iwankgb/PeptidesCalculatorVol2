from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame, communique):
        Frame.setObjectName("Frame")
        Frame.resize(900, 200)
        Frame.setMinimumSize(QtCore.QSize(900, 200))
        Frame.setMaximumSize(QtCore.QSize(900, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("peptid logo/logo1.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Frame.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(600, 140, 180, 28))

        '''allows to execute by click enter button'''
        self.pushButton.setDefault(True)

        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(30, 40, 113, 100))
        self.label.setMinimumSize(QtCore.QSize(113, 100))
        self.label.setMaximumSize(QtCore.QSize(113, 100))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("peptid logo/Error2.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(180, 35, 700, 95))
        self.label_2.setObjectName("label_2")

        self.error_text = communique

        self.retranslateUi(Frame, error_text=self.error_text)
        self.pushButton.clicked.connect(Frame.close)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame, error_text):

        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate(
            "Frame", "PeptideMassCalculator - ERROR !"))
        self.pushButton.setText(_translate("Frame", "OK"))

        if error_text.find(";") != -1:
            error_text_1 = error_text.split(";")[0]
            error_text_2 = error_text.split(";")[1]

            self.label_2.setText(_translate("Frame", "<html>"
                                                     "<head/>"
                                                     "<body>"
                                                     f"<p><span style=\" font-size:10pt;\">{error_text_1}!</span></p>"
                                                     f"<p><span style=\" font-size:10pt;\">{error_text_2}.</span></p>"
                                                     "</body>"

                                                     "</html>"))

        else:
            error_text_1 = error_text

            self.label_2.setText(_translate("Frame", "<html>"
                                                     "<head/>"
                                                     "<body>"
                                                     f"<p><span style=\" font-size:10pt;\">{error_text_1}!</span></p>"
                                                     "</body>"
                                                     "</html>"))


if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame, 'Test')
    Frame.show()
    app.exec_()
