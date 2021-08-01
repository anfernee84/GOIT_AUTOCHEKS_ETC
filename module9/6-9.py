import re

def generator_numbers(string=""):

        splitstr = re.findall('[0-9]+', string)
        for i in splitstr:
            yield i


def sum_profit(string):
    numval = [int(i) for i in generator_numbers(string)]
    return sum(numval)

print(sum_profit("The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."))