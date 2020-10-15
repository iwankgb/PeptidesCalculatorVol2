from Delete_unusual_amino_acid_dialog_window import Ui_DeleteUnusualAmino
from Add_unusual_amino_acid_dialog_window import Ui_AddUnusualAminoAcid
from Welcome_dialog_window import Ui_FrameW
from Error_dialog_window import Ui_Frame
from calc_data_printing import Data_Printer
from calc_sequence_calculator import Sequence
import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1251, 456)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("peptid logo/logo1.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.checkBox_2)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.checkBox)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_2.addWidget(self.comboBox_2, 1, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 3)
        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("color: rgb(0, 0, 255);\n"
                                      "background-color: rgb(170, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.gridLayout.addWidget(self.frame, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1251, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionShow = QtWidgets.QAction(MainWindow)
        self.actionShow.setObjectName("actionShow")
        self.actionShow_Protected_Amino_Acid = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionShow_Protected_Amino_Acid.setFont(font)
        self.actionShow_Protected_Amino_Acid.setObjectName(
            "actionShow_Protected_Amino_Acid")
        self.actionShow_Not_Protected_Amino_Acid = QtWidgets.QAction(
            MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionShow_Not_Protected_Amino_Acid.setFont(font)
        self.actionShow_Not_Protected_Amino_Acid.setObjectName(
            "actionShow_Not_Protected_Amino_Acid")
        self.actionAdd_Custom_Amino_Acid = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionAdd_Custom_Amino_Acid.setFont(font)
        self.actionAdd_Custom_Amino_Acid.setObjectName(
            "actionAdd_Custom_Amino_Acid")
        self.actionExit = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionExit.setFont(font)
        self.actionExit.setObjectName("actionExit")
        self.actionInstruction = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionInstruction.setFont(font)
        self.actionInstruction.setObjectName("actionInstruction")
        self.actionTerminus = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionTerminus.setFont(font)
        self.actionTerminus.setObjectName("actionTerminus")
        self.actionDelete_Unusual_Amino_Acid = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionDelete_Unusual_Amino_Acid.setFont(font)
        self.actionDelete_Unusual_Amino_Acid.setObjectName(
            "actionDelete_Unusual_Amino_Acid")
        self.actionShow_Unusual_Amino_Acid = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionShow_Unusual_Amino_Acid.setFont(font)
        self.actionShow_Unusual_Amino_Acid.setObjectName(
            "actionShow_Unusual_Amino_Acid")
        self.menuMenu.addAction(self.actionShow_Unusual_Amino_Acid)
        self.menuMenu.addAction(self.actionShow_Not_Protected_Amino_Acid)
        self.menuMenu.addAction(self.actionShow_Protected_Amino_Acid)
        self.menuMenu.addAction(self.actionTerminus)
        self.menuMenu.addAction(self.actionAdd_Custom_Amino_Acid)
        self.menuMenu.addAction(self.actionDelete_Unusual_Amino_Acid)
        self.menuMenu.addAction(self.actionInstruction)
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.checkBox_2, self.checkBox)
        MainWindow.setTabOrder(self.checkBox, self.comboBox)
        MainWindow.setTabOrder(self.comboBox, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.comboBox_2)
        MainWindow.setTabOrder(self.comboBox_2, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.lineEdit_2)

        '''connection between interface buttons and functions'''
        self.actionShow_Unusual_Amino_Acid.triggered.connect(
            self.open_data_printer_unusual)
        self.actionShow_Protected_Amino_Acid.triggered.connect(
            self.amino_protected)
        self.actionShow_Not_Protected_Amino_Acid.triggered.connect(
            self.amino_not_protected)
        self.actionTerminus.triggered.connect(self.endings)
        self.actionDelete_Unusual_Amino_Acid.triggered.connect(
            self.open_window_delete)
        self.actionAdd_Custom_Amino_Acid.triggered.connect(
            self.open_window_add)
        self.actionInstruction.triggered.connect(self.help)
        self.actionExit.triggered.connect(MainWindow.close)

        self.pushButton.clicked.connect(self.open_calculation_process)

        '''add items to the combo box'''
        self.n_terminus_list = [
            "Hydrogen",
            "Biotin",
            "Acetyl",
            '5-FAM',
            '5-TAMRA',
            'DABCYL',
            'Fmoc',
            'Pyr',
            'Myr',
            'Z',
            'DOTA',
        ]

        self.c_terminus_list = [
            "Free",
            "Amid",
            'Aldehyde',
            'AFC',
            'CMK',
            'EDANS',
        ]

        self.comboBox.addItems(self.n_terminus_list)
        self.comboBox_2.addItems(self.c_terminus_list)

    def open_calculation_process(self):

        self.lineEdit_3.setText('')  # cleans results
        self.lineEdit_2.setText('')  # cleans results

        if self.checkBox.isChecked() and self.checkBox_2.isChecked():
            return self.open_error('Please choose only one Amino Acid Type')
        if self.checkBox_2.isChecked():
            self.user_choice_1 = "P"
        else:
            if self.checkBox.isChecked():
                self.user_choice_1 = 'N'
            else:
                return self.open_error('Please choose Amino Acid Type')

        '''get ending type'''
        self.n_terminus = self.comboBox.currentText()
        self.c_terminus = self.comboBox_2.currentText()

        '''transforms user choice'''
        self.user_choice = self.user_choice_1 + str("E")

        self.data_input = self.lineEdit.text()  # takes data from LineEdit
        self.counting = Sequence()

        '''sends sequence from lineEdit to calculator'''
        calculation_return = self.counting.enter_sequence(
            self.data_input, self.user_choice, self.n_terminus, self.c_terminus)  # use return multiple values

        if calculation_return[0:6] == 'Please':  # Please - means an error
            return self.open_error(calculation_return)
        else:
            result = calculation_return[0]

            if result == 'Please be informed that sequence is incorrect;Amino acid or unusual amino acid, doesnt exist':
                return self.open_error(result)
            else:
                pep_sequence = calculation_return[1]
                converted_result = str(result)
                convert_pep_sequence = str(pep_sequence)

                # gives result to Interface
                self.lineEdit_3.setText(converted_result)
                # gives sequence to Interface
                self.lineEdit_2.setText(convert_pep_sequence)

    def open_data_printer_unusual(self):

        self.menuMenu.setEnabled(False)  # block menu
        # block "menu show function" in case user uses keyboard shortcut
        self.disables_menu_buttons()
        self.unusualamino = Data_Printer()
        comunicate = self.unusualamino.print_unusual_amino_acid()

        if comunicate != None:  # if file exist returns None if error then returns message
            return self.open_error(comunicate)
        self.enable_menu_buttons()
        self.menuMenu.setEnabled(True)

    def amino_protected(self):
        return self.open_data_printer_protected_and_not('protected')

    def amino_not_protected(self):
        return self.open_data_printer_protected_and_not('notprotected')

    def endings(self):
        return self.open_data_printer_protected_and_not('endings')

    def open_data_printer_protected_and_not(self, type):
        self.menuMenu.setEnabled(False)
        self.disables_menu_buttons()
        self.amino = Data_Printer()
        comunicate = self.amino.print_protected_amino_acid_and_not(type)

        if comunicate != None:  # Returns none when function "print_protected_amino_acid_and_not" has no error, if ico file does not exist it returns error.
            return self.open_error(comunicate)
        self.enable_menu_buttons()
        self.menuMenu.setEnabled(True)

    def open_window_delete(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_DeleteUnusualAmino()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_window_add(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AddUnusualAminoAcid()
        self.ui.setupUi(self.window)
        self.window.show()

    def help(self):

        path = os.getcwd()
        full_path = f'{path}\help text.pdf'
        if os.path.isfile(full_path) == False:
            return self.open_error("Help can't be displayed, because 'help text.pdf' doesn't exist")
        else:
            os.startfile(full_path)

    '''open error window'''

    def open_error(self, communique):
        self.open = QtWidgets.QFrame()
        self.ui = Ui_Frame()
        self.ui.setupUi(self.open, communique)
        self.open.show()
        self.enable_menu_buttons()
        self.menuMenu.setEnabled(True)

    '''disable menu buttons'''

    def disables_menu_buttons(self):
        self.actionShow_Unusual_Amino_Acid.setEnabled(False)
        self.actionShow_Protected_Amino_Acid.setEnabled(False)
        self.actionShow_Not_Protected_Amino_Acid.setEnabled(False)
        self.actionTerminus.setEnabled(False)

    '''enable menu buttons'''

    def enable_menu_buttons(self):
        self.actionShow_Unusual_Amino_Acid.setEnabled(True)
        self.actionShow_Protected_Amino_Acid.setEnabled(True)
        self.actionShow_Not_Protected_Amino_Acid.setEnabled(True)
        self.actionTerminus.setEnabled(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "PeptideMassCalculator"))
        self.label_4.setText(_translate(
            "MainWindow", "Peptide Sequence Check"))
        self.groupBox.setTitle(_translate(
            "MainWindow", "Choose Amino Acid Type"))
        self.checkBox_2.setText(_translate(
            "MainWindow", "Protected Amino Acid"))
        self.checkBox.setText(_translate(
            "MainWindow", "Not Protected Amino Acid"))
        self.label_3.setText(_translate("MainWindow", "C-Terminus"))
        self.label_2.setText(_translate("MainWindow", "Sequence"))
        self.label.setText(_translate("MainWindow", "N-Terminus"))
        self.pushButton.setText(_translate("MainWindow", "CALCULATE"))
        self.label_5.setText(_translate(
            "MainWindow", "Peptide Molecular Weight"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionShow.setText(_translate("MainWindow", "Show"))
        self.actionShow_Protected_Amino_Acid.setText(
            _translate("MainWindow", "Show Protected Amino Acid"))
        self.actionShow_Protected_Amino_Acid.setStatusTip(
            _translate("MainWindow", "Shows protected amino acid table"))
        self.actionShow_Protected_Amino_Acid.setShortcut(
            _translate("MainWindow", "Ctrl+2"))
        self.actionShow_Not_Protected_Amino_Acid.setText(
            _translate("MainWindow", "Show Amino Acid"))
        self.actionShow_Not_Protected_Amino_Acid.setStatusTip(
            _translate("MainWindow", "Shows amino acid table"))
        self.actionShow_Not_Protected_Amino_Acid.setShortcut(
            _translate("MainWindow", "Ctrl+1"))
        self.actionAdd_Custom_Amino_Acid.setText(
            _translate("MainWindow", "Add Unusual Amino Acid"))
        self.actionAdd_Custom_Amino_Acid.setStatusTip(
            _translate("MainWindow", "Add unusual amino acid"))
        self.actionAdd_Custom_Amino_Acid.setShortcut(
            _translate("MainWindow", "Ctrl+A"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit program"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionInstruction.setText(_translate("MainWindow", "Help"))
        self.actionInstruction.setStatusTip(_translate(
            "MainWindow", "Shows Instruction how to use Peptide Mass Calculator"))
        self.actionInstruction.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionTerminus.setText(_translate("MainWindow", "Show Terminus"))
        self.actionTerminus.setToolTip(
            _translate("MainWindow", "Show Terminus"))
        self.actionTerminus.setStatusTip(_translate(
            "MainWindow", "Shows all Terminuses available to choose"))
        self.actionTerminus.setShortcut(_translate("MainWindow", "Ctrl+3"))
        self.actionDelete_Unusual_Amino_Acid.setText(
            _translate("MainWindow", "Delete Unusual Amino Acid"))
        self.actionDelete_Unusual_Amino_Acid.setStatusTip(
            _translate("MainWindow", "Delete unusual amino acid"))
        self.actionDelete_Unusual_Amino_Acid.setShortcut(
            _translate("MainWindow", "Ctrl+D"))
        self.actionShow_Unusual_Amino_Acid.setText(
            _translate("MainWindow", "Show Unusual Amino Acid"))
        self.actionShow_Unusual_Amino_Acid.setStatusTip(
            _translate("MainWindow", "Shows unusual amino acid table"))
        self.actionShow_Unusual_Amino_Acid.setShortcut(
            _translate("MainWindow", "Ctrl+0"))


if __name__ == "__main__":
    import sys

    '''open welcome window'''
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_FrameW()
    ui.setupUiW(Frame)
    Frame.show()
    app.exec()

    '''open interface'''
    app1 = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui1 = Ui_MainWindow()
    ui1.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app1.exec_())
