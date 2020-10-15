import re


class Check:

    def check_sequence(self, data_sequence):
        '''check if sequence exist'''
        if len(data_sequence) == 0:
            return 'Please provide sequence'

        '''check if number of bracket is even number'''
        check1 = [search.start()
                  for search in re.finditer("[(|)]", data_sequence)]

        if len(check1) % 2 != 0:
            return 'Please correct sequence;One bracket is missing'

        '''check if non standard amino shortcut length is correct '''
        number = len(check1)

        while number:
            first_index = check1.pop(0)
            second_index = check1.pop(0)
            check2 = second_index - first_index - 1
            if check2 != 3:
                return 'Please correct sequence;Amino acid abbreviation length is incorrect'
            number -= 2
        else:
            return data_sequence


if __name__ == '__main__':
    a = Check()
    a.check_sequence('(aed)l')
