from calc_remove_unusual_amino import Remove
from PyQt5 import QtCore, QtGui, QtWidgets
from Error_dialog_window import Ui_Frame
from Information_dialog_window import Ui_Frame_i


class Ui_DeleteUnusualAmino(object):
    def setupUi(self, DeleteUnusualAmino):
        DeleteUnusualAmino.setObjectName("DeleteUnusualAmino")
        DeleteUnusualAmino.resize(600, 400)
        DeleteUnusualAmino.setMinimumSize(QtCore.QSize(600, 400))
        DeleteUnusualAmino.setMaximumSize(QtCore.QSize(600, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("peptid logo/logo1.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DeleteUnusualAmino.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(DeleteUnusualAmino)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.frame)
        DeleteUnusualAmino.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DeleteUnusualAmino)
        self.statusbar.setObjectName("statusbar")
        DeleteUnusualAmino.setStatusBar(self.statusbar)

        self.retranslateUi(DeleteUnusualAmino)
        QtCore.QMetaObject.connectSlotsByName(DeleteUnusualAmino)

        self.pushButton.clicked.connect(self.connector1)

    def connector1(self):
        value = self.lineEdit.text()
        value1 = self.lineEdit_2.text()
        value2 = self.lineEdit_3.text()
        call = Remove()

        '''remove unusual amino'''
        comunicate = call.remove_unsual_amino(value, value1, value2)

        '''shows communicate, and choose communicate type "y" information window'''
        if comunicate[-1:] == 'y':
            self.open_info_i(comunicate)
            '''clears data'''
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
            self.lineEdit_3.setText('')
        else:
            self.open_error(comunicate)

    '''open info window'''

    def open_info_i(self, communique):
        self.open = QtWidgets.QFrame()
        self.ui = Ui_Frame_i()
        self.ui.setupUi_i(self.open, communique)
        self.open.show()

    '''open error window'''

    def open_error(self, communique):
        self.open = QtWidgets.QFrame()
        self.ui = Ui_Frame()
        self.ui.setupUi(self.open, communique)
        self.open.show()

    def retranslateUi(self, DeleteUnusualAmino):
        _translate = QtCore.QCoreApplication.translate
        DeleteUnusualAmino.setWindowTitle(_translate(
            "DeleteUnusualAmino", "PeptideMassCalculator - Delete Unusual Amino Acid"))
        self.label_2.setText(_translate("DeleteUnusualAmino", "Amino acid"))
        self.label_3.setText(_translate(
            "DeleteUnusualAmino", "3-letter abbreviation"))
        self.label.setText(_translate(
            "DeleteUnusualAmino", "Molecular weight"))
        self.pushButton.setText(_translate("DeleteUnusualAmino", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeleteUnusualAmino = QtWidgets.QMainWindow()
    ui = Ui_DeleteUnusualAmino()
    ui.setupUi(DeleteUnusualAmino)
    DeleteUnusualAmino.show()
    sys.exit(app.exec_())
