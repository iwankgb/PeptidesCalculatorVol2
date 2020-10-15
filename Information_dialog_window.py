from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame_i(object):

    def setupUi_i(self, Frame, communique):

        Frame.setObjectName("Frame")
        Frame.resize(900, 200)
        Frame.setMinimumSize(QtCore.QSize(900, 200))
        Frame.setMaximumSize(QtCore.QSize(900, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("peptid logo/logo1.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Frame.setWindowIcon(icon)
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(30, 40, 113, 100))
        self.label_4.setMinimumSize(QtCore.QSize(113, 100))
        self.label_4.setMaximumSize(QtCore.QSize(113, 100))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("peptid logo/information.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(180, 35, 700, 95))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(Frame)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 140, 180, 28))

        '''allows to execute by click enter button'''
        self.pushButton_2.setDefault(True)

        self.pushButton_2.setObjectName("pushButton_2")

        self.info_text = communique

        self.retranslateUi_i(Frame, info_text=self.info_text)
        self.pushButton_2.clicked.connect(Frame.close)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi_i(self, Frame, info_text):

        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate(
            "Frame", "PeptideMassCalculator - INFORMATION"))

        info_text_1 = info_text.split(";")[0]
        info_text_2 = info_text.split(";")[1]

        self.label_3.setText(_translate("Frame", "<html>"
                                                 "<head/>"
                                                 "<body>"
                                                 f"<p><span style=\" font-size:10pt;\">{info_text_1}.</span></p>"
                                                 f"<p><span style=\" font-size:10pt;\">{info_text_2}!</span></p>"
                                                 "</body>"
                                                 "</html>"))

        self.pushButton_2.setText(_translate("Frame", "OK"))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame_i()
    ui.setupUi_i(Frame, 'test;test')
    Frame.show()
    sys.exit(app.exec_())
