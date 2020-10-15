import re
from calc_convert_list import Converter
from calc_distinguish import Distinguish
from calc_check_sequence_correction import Check
from calc_data_base import CalcDataBase


class Sequence:

    def enter_sequence(self, data_input, user_choice, n_terminus, c_terminus):

        data_sequence = data_input

        '''checks if sequence is correct'''
        check_sequence1 = Check()
        checking_result = check_sequence1.check_sequence(data_sequence)
        if checking_result[0:6] == 'Please':  # P - means there is an error
            return checking_result
        else:
            '''mark non standard amino by adding *'''
            mark_non_standard = Distinguish()
            mark_data_sequence = mark_non_standard.distinguish_non_standard(
                data_sequence)

            '''Search for non standard amino - 3 characters'''
            non_standard_amino = re.findall("\((.*?)\)", mark_data_sequence)

            '''Splits sequence by () and remove '' '''
            splited_sequence = re.split("[(|)]", mark_data_sequence)
            for element in splited_sequence:
                if element == '':
                    splited_sequence.remove(element)

            '''Builds list with divided standard and non standard amino'''
            final_list = []
            for element in splited_sequence:
                if element not in non_standard_amino:
                    final_list.append(self.split_sequence(element))
                else:
                    final_list.append(element)

            '''Use converter to prepare final list'''
            converted_list = Converter()
            sequence_list = list(converted_list.list_converter(final_list))
            # returns amino_calculator function and sequence_list
            return self.amino_calculator(sequence_list, user_choice, n_terminus, c_terminus), sequence_list

    def split_sequence(self, string_to_split):
        return [char for char in string_to_split]

    def amino_calculator(self, sequence_list, user_choice, n_terminus, c_terminus):
        '''add endings to sequence_list'''
        if n_terminus != '':
            sequence_list.append(n_terminus)
        if c_terminus != '':
            sequence_list.append(c_terminus)

        base = CalcDataBase()
        amino_data_base = base.data_base(user_choice)
        mass_result = 0
        try:

            for single_amino in sequence_list:
                mass_result += amino_data_base[single_amino]
            result = round(mass_result, 2)
            return result  # returns the result
        except KeyError:
            return "Please be informed that sequence is incorrect;Amino acid or unusual amino acid, doesnt exist"
