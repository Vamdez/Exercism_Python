import re


class PhoneNumber:
    def __init__(self, number):
        self.number = self.cleans_the_number(number)
        self.validation_exception(self.number)
        self.area_code = self.number[0:3]

    def cleans_the_number(self, number):
        if re.search(r'[a-zA-z]', number):
            raise ValueError("letters not permitted")
        if re.search('[@!?#$%¨&*]', number):
            raise ValueError("punctuation not permitted")
        p = re.compile(r'\D')
        return p.sub('', number)

    def validation_exception(self, number):
        if len(number) < 10:
            raise ValueError("incorrect number of digits")
        if len(number) > 11:
            raise ValueError("more than 11 digits")
        if len(number) == 11:
            if number[0] != '1':
                print('entro')
                raise ValueError("11 digits must start with 1")
            self.number = number[1:]
            number = self.number
        if len(number) == 10:
            if number[0] == '1':
                raise ValueError("area code cannot start with one")
            if number[0] == '0':
                raise ValueError("area code cannot start with zero")
            if number[3] == '1':
                raise ValueError("exchange code cannot start with one")
            if number[3] == '0':
                raise ValueError("exchange code cannot start with zero")

    def pretty(self):
        return f'({self.number[0:3]})-{self.number[3:6]}-{self.number[6:]}'
