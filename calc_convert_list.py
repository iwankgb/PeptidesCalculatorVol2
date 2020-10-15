class Converter:

    def __init__(self):

        self.converted_list = []

    def list_converter(self, list_to_convert):

        for item in list_to_convert:
            if type(item) == list:
                self.list_converter(item)
            else:
                self.converted_list.append(item)

        '''removed '*' from converted_list'''
        self.converted_final_list = map(
            lambda element: element.strip('*'), self.converted_list)
        return [element.upper() for element in self.converted_final_list]
