import csv
from itertools import chain


class Add:

    def add_unusual_amino(self, value, value1, value2):
        '''Input unusual amino acid'''
        Amino_Acid_Input = str(value)
        Letter_abbreviation_Input = str(value1)
        if Amino_Acid_Input == "" or Letter_abbreviation_Input == "":
            return "Field can't be empty. Please complete all fields"
        if len(Letter_abbreviation_Input) != 3:
            return "Abbreviation has incorrect length"
        try:
            Molecular_weight = float(value2)
        except ValueError:
            return "Weight should be a number"

        '''open file and check if amino already exist'''
        try:
            with open("unusual_amino.csv", newline='') as unusual_amino:
                reader = csv.reader(unusual_amino)
                unusual_amino_data = (list(reader))
                unusual_amino_list = list(
                    chain.from_iterable(unusual_amino_data))
                for amino in unusual_amino_list:
                    if amino == Letter_abbreviation_Input.upper() or amino == Amino_Acid_Input.upper():
                        return "Unusual Amino already exist; Abbreviation is the same as existing one"
        except FileNotFoundError:
            return self.first_time_save(Amino_Acid_Input, Letter_abbreviation_Input, Molecular_weight)

        '''save'''
        unusual_amino = [Amino_Acid_Input.upper(
        ), Letter_abbreviation_Input.upper(), Molecular_weight]
        try:
            with open("unusual_amino.csv", "a", newline="") as unusual:
                write = csv.writer(unusual)
                write.writerow(unusual_amino)

            return f'Unusual amino acid: {unusual_amino}; Has been saved successfully'

        except PermissionError:
            return "Please close 'unusual_amino.csv' file"

    def first_time_save(self, Amino_Acid_Input, Letter_abbreviation_Input, Molecular_weight):
        '''sets headers'''
        unusual_amino = ['AMINO ACID NAME',
                         '3 LETTER SHORTCUT', 'MOLECULAR WEIGHT']
        with open("unusual_amino.csv", "a", newline="") as unusual:
            write = csv.writer(unusual)
            write.writerow(unusual_amino)

        '''save user input'''
        unusual_amino = [Amino_Acid_Input.upper(
        ), Letter_abbreviation_Input.upper(), Molecular_weight]
        with open("unusual_amino.csv", "a", newline="") as unusual:
            write = csv.writer(unusual)
            write.writerow(unusual_amino)

        return f'Unusual amino acid: {unusual_amino}; Has been saved successfully'
