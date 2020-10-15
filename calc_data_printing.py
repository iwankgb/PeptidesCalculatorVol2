import tkinter as tk
from pandastable import Table
import pandas as pd
import os
import csv


class Data_Printer:

    protectedamino = pd.DataFrame({
        'AMINO ACID NAME': ["Fenyloalanina",	"Prolina",	"Histydyna",	"Arginina",	"Asparagina",	"Kwas Asparaginowy",	"Tryptofan",
                            "Kwas Glutaminowy",	"Metionina",	"Lizyna",	"Cysteina",	"Treonina",	"Seryna",	"Izoleucyna",	"Tyrozyna",
                            "Walina",	"Leucyna",	"Glutamina",	"Alanina",	"Glicyna"],
        '3 LETTER SHORTCUT': ["Phe",	 "Pro",	 "His",	 "Arg",	 "Asn",	 "Asp",	 "Trp",	 "Glu",	 "Met",	 "Lys",	 "Cys",
                              "Thr",	 "Ser",	 "Ile",	 "Tyr",	 "Val",	 "Leu",	 "Gln",	 "Ala",	 "Gly"],
        '1 LETTER SHORTCUT': ["F",	 "P",	 "H",	 "R",	 "N",	 "D",	 "W",	 "E",	 "M",	 "K",	 "C",	 "T",	 "S",	 "I",	 "Y",	 "V",	 "L",	 "Q",	 "A",	 "G"],
        'MOLECULAR WEIGHT': [147.1734,	 97.11508,	 379.4594,	 408.4861,	 356.4228,	 171.1953,	 286.3265,	 185.2219,	 131.1985,	 128.1724,
                             345.4654,	 157.2119,	 143.18533,	 113.1576,	 219.2808,	 99.13103,	 113.1576,	 370.4493,	 71.07793,	 57.05138, ],
    })

    notprotectedamino = pd.DataFrame({
        'AMINO ACID NAME': ["Fenyloalanina",	"Prolina",	"Histydyna",	"Arginina",	"Asparagina",	"Kwas Asparaginowy",	"Tryptofan",	"Kwas Glutaminowy",	"Metionina",
                            "Lizyna",	"Cysteina",	"Treonina",	"Seryna",	"Izoleucyna",	"Tyrozyna",	"Walina",	"Leucyna",	"Glutamina",	"Alanina",	"Glicyna"],
        '3 LETTER SHORTCUT': ["Phe",	 "Pro",	 "His",	 "Arg",	 "Asn",	 "Asp",	 "Trp",	 "Glu",	 "Met",	 "Lys",	 "Cys",
                              "Thr",	 "Ser",	 "Ile",	 "Tyr",	 "Val",	 "Leu",	 "Gln",	 "Ala",	 "Gly"],
        '1 LETTER SHORTCUT': ["F",	 "P",	 "H",	 "R",	 "N",	 "D",	 "W",	 "E",	 "M",	 "K",	 "C",	 "T",	 "S",	 "I",	 "Y",	 "V",	 "L",	 "Q",	 "A",	 "G"],
        'MOLECULAR WEIGHT': [147.1734,	 97.11508,	 137.1394,	 156.1861,	 114.1028,	 115.0873,	 186.2095,	 129.1139,	 131.1985,	 228.2894,
                             103.1454,	 101.1039,	 87.07733,	 113.1576,	 163.1728,	 99.13103,	 113.1576,	 128.1293,	 71.07793,	 57.05138],
    })

    endings = pd.DataFrame({
        'TERMINUS TYPE': ['N-TERMINUS', 'N-TERMINUS', 'N-TERMINUS', 'N-TERMINUS', 'N-TERMINUS', 'N-TERMINUS', 'N-TERMINUS', 'N-TERMINUS', 'N-TERMINUS', 'N-TERMINUS', 'N-TERMINUS',
                          'C-TERMINUS', 'C-TERMINUS', 'C-TERMINUS', 'C-TERMINUS', 'C-TERMINUS', 'C-TERMINUS'],
        'TERMINUS NAME': ["Hydrogen", "Biotin", "Acetyl", "5-FAM", "5-TAMRA", "DABCYL", "Fmoc", "Pyr", "Myr",
                          "Z", "DOTA", "Free", "Amid", "Aldehyde", "AFC", "CMK", "EDANS"],
        'MOLECULAR WEIGHT': [1.00797, 227.3056, 43.04453, 359.3, 413.44, 252.29, 223.24, 112.1, 211.36, 135.13, 387.4, 17.00738,
                             16.0228, 1.01, 228.16, 49.49, 265.33],
    })

    def print_unusual_amino_acid(self):
        '''Check if ico file exist'''
        if self.check_if_ico_exist() == False:
            return f'"logo.ico" file doesnt exist. File has to be added to the directory;{self.ico_path()}'

        '''check if unusual_amino.csv" exist'''
        if self.check_if_data_exist() == False:
            return f'"unusual_amino.csv" doesnt exist. Amino acid has to be added first;{self.data_path()}'

        '''check if unusual_amino.csv is empty - first checked if exist'''
        if self.check_if_unusual_amino_is_empty() == 'True':
            return f'Please note that file "unusual_amino.csv" is empty; Or it contains only one row'
        else:
            '''Sets icon'''
            root = tk.Tk()
            root.title('PeptideMassCalculator')
            root.iconbitmap(self.ico_path())

            frame = tk.Frame(root)
            frame.pack(fill='both', expand=True)
            datatable = Table(frame, showtoolbar=False, showstatusbar=True)
            datatable.show()

            '''shows unusual_amino.csv in the table'''
            datatable.importCSV(filename=self.data_path(), dialog=False)
            root.mainloop()

    def print_protected_amino_acid_and_not(self, type):
        '''Check if ico file exist'''
        if self.check_if_ico_exist() == False:
            return f'"logo.ico" file doesnt exist. File has to be added to the directory;{self.ico_path()}'

        else:

            if type == "protected":
                amino = self.protectedamino
                title = "Protected Amino Acid"
            if type == "notprotected":
                amino = self.notprotectedamino
                title = "Amino Acid"
            if type == "endings":
                amino = self.endings
                title = "Terminus"
            root = tk.Tk()
            root.title(f'PeptideMassCalculator - {title}')
            root.iconbitmap(self.ico_path())
            frame = tk.Frame(root)
            frame.pack(fill='both', expand=True)
            datatable = Table(frame, dataframe=amino, showstatusbar=True)
            datatable.show()
            root.mainloop()

    '''returns path to the program icon'''

    def ico_path(self):
        path = os.getcwd()
        full_path = f'{path}\logo.ico'
        return full_path

    '''returns file path'''

    def data_path(self):
        path = os.getcwd()
        full_path = f'{path}\\unusual_amino.csv'
        return full_path

    '''check if file and icon exist'''

    def check_if_ico_exist(self):
        return os.path.isfile(self.ico_path())

    def check_if_data_exist(self):
        return os.path.isfile(self.data_path())

    '''check if unusual amino file is empty'''

    def check_if_unusual_amino_is_empty(self):
        with open('unusual_amino.csv') as file:
            reader = csv.reader(file)
            line_count = 0
            for row in reader:
                line_count += 1
            if line_count <= 1:
                return 'True'
            else:
                return 'False'


if __name__ == '__main__':
    test = Data_Printer()
    test.print_protected_amino_acid_and_not("protected")
