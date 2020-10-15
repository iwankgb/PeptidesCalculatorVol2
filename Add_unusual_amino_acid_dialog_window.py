from calc_add_unusual_amino import Add
from PyQt5 import QtCore, QtGui, QtWidgets
from Error_dialog_window import Ui_Frame
from Information_dialog_window import Ui_Frame_i


class Ui_AddUnusualAminoAcid(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("peptid logo/logo1.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_3, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.lineEdit_4)
        MainWindow.setTabOrder(self.lineEdit_4, self.pushButton)

        self.pushButton.clicked.connect(self.connector1)

    def connector1(self):
        value = self.lineEdit_3.text()
        value2 = self.lineEdit_2.text()
        value3 = self.lineEdit_4.text()
        call = Add()

        '''starts add unusual amino, save and return comunicate'''
        comunicate = call.add_unusual_amino(value, value2, value3)

        ''' shows communicate, and choose communicate type "y" information window '''
        if comunicate[-1:] == 'y':
            self.open_info_i(comunicate)

            '''clears data'''
            self.lineEdit_3.setText('')
            self.lineEdit_2.setText('')
            self.lineEdit_4.setText('')
        else:
            self.open_error(comunicate)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "PeptideMassCalculator - Add Unusual Amino Acid"))
        self.label_2.setText(_translate("MainWindow", "Amino acid"))
        self.label_3.setText(_translate("MainWindow", "3-letter abbreviation"))
        self.label.setText(_translate("MainWindow", "Molecular weight"))
        self.pushButton.setText(_translate("MainWindow", "Save"))

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AddUnusualAminoAcid()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
