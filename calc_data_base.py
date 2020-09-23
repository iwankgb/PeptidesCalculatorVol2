import csv

class CalcDataBase:

    def data_base(self, user_choice):

        """amino and endings data base"""
        protectedamino = {"F": 147.1734,
                        "P": 97.11508,
                        "H": 379.4594,
                        "R": 408.4861,
                        "N": 356.4228,
                        "D": 171.1953,
                        "W": 286.3265,
                        "E": 185.2219,
                        "M": 131.1985,
                        "K": 228.2894,
                        "C": 345.4654,
                        "T": 157.2119,
                        "S": 143.18533,
                        "I": 113.1576,
                        "Y": 219.2808,
                        "V": 99.13103,
                        "L": 113.1576,
                        "Q": 370.4493,
                        "A": 71.07793,
                        "G": 57.05138}

        amino = {       "F": 147.1734,
                        "P": 97.11508,
                        "H": 137.1394,
                        "R": 156.1861,
                        "N": 114.1028,
                        "D": 115.0873,
                        "W": 186.2095,
                        "E": 129.1139,
                        "M": 131.1985,
                        "K": 128.1724,
                        "C": 103.1454,
                        "T": 101.1039,
                        "S": 87.07733,
                        "I": 113.1576,
                        "Y": 163.1728,
                        "V": 99.13103,
                        "L": 113.1576,
                        "Q": 128.1293,
                        "A": 71.07793,
                        "G": 57.05138}

        endingsn = {"Hydrogen": 1.00797,
                    "Biotin": 227.3056,
                    "Acetyl": 43.04453,
                    "5-FAM": 359.3,
                    "5-TAMRA": 413.44,
                    "DABCYL": 252.29,
                    "Fmoc": 223.24,
                    "Pyr": 112.1,
                    "Myr": 211.36,
                    "Z": 135.13,
                    "DOTA": 387.4,
                    }

        endingsc = {"Free": 17.00738,
                    "Amid": 16.0228,
                    "Aldehyde": 1.01,
                    "AFC": 228.16,
                    "CMK": 49.49,
                    "EDANS": 265.33,
                    }

        nonstandard = None  # if file with nonstansdard does not exist

        '''amino data base - added by user '''
        try:  # check if file is empty or if exist, if empty - first error is IndexError
            my_list = []
            with open('unusual_amino.csv', newline='') as open_csv:
                reader = csv.reader(open_csv, delimiter=',')
                for row in reader:
                    del row[0]  # removes first element
                    for element in row:  # changes lists into one list
                        my_list.append(element)

                del my_list[0:2] #remove headers


            nonstandard = {my_list[ele]: my_list[ele + 1] for ele in range(0, len(my_list), 2)}  #convertion to a dict

            nonstandard.update((key, float(val)) for key, val in nonstandard.items())
        except (IndexError, FileNotFoundError):
            pass
        test_input = user_choice

        if test_input.upper() == "PE":
            if nonstandard is None:
                protectedamino.update(endingsn)
                protectedamino.update(endingsc)
                return protectedamino
            protectedamino.update(endingsn)
            protectedamino.update(endingsc)
            protectedamino.update(nonstandard)
            return protectedamino

        elif test_input.upper() == "NE":
            if nonstandard is None:
                amino.update(endingsn)
                amino.update(endingsc)
                return amino
            amino.update(endingsn)
            amino.update(endingsc)
            amino.update(nonstandard)
            return amino


if __name__ == '__main__':
    a = CalcDataBase()
    a.data_base()