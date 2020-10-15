import csv


class Remove:

    def remove_unsual_amino(self, value, value1, value2):

        amino_acid_input = value
        letter_abbreviation_input = value1
        molecular_weight = value2

        molecular_weight_str = str(molecular_weight)
        remove_item_list = [amino_acid_input.upper(
        ), letter_abbreviation_input.upper(), molecular_weight_str]

        check_list = []
        check_list_1 = []

        try:
            with open('unusual_amino.csv', newline='') as open_csv:
                reader = csv.reader(open_csv, delimiter=',')
                for row in reader:
                    check_list_1.append(row)
                    if row != remove_item_list:
                        check_list.append(row)

                '''check if given amino exist'''
            if len(check_list) == len(check_list_1):
                return "Given amino acid doesn't exist; So it can't be removed"

        except FileNotFoundError:
            return 'File with unusual amino does not exist.'

        '''save'''
        try:
            with open("unusual_amino.csv", "w", newline="") as unusual:
                write = csv.writer(unusual)
                for amino in check_list:
                    write.writerow(amino)
            return f'Unusual amino acid: {remove_item_list}; Has been removed successfully'
        except PermissionError:
            return "Please close 'unusual_amino.csv' file"
