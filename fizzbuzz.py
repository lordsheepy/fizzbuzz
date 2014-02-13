#! usr/bin/env python
def fizzbuzz(n, divisor_dict):

    """Creating a user extensible fizzbuzz in which user provide a dict with a
    key corresponding to divisor and a value equating the desired string"""

    result = ''
    for k, v in sorted(divisor_dict.items()):
        if n % k == 0:
            result += v

    if result == '':
        return str(n)

    return result


if __name__ == "__main__":

    num = int(raw_input("What number would you like to evaluate?"))
    input_dict = {}
    more = True

    while more == True:
        divisor = int(raw_input("Please input a divisor: "))
        word = str(raw_input("What word you like to have it print? "))
        input_dict[divisor] = word
        y_or_n = str(raw_input("Would you like to add another divisor?(Y/N) "))
        more = y_or_n.lower() == 'y'

    print fizzbuzz(num, input_dict)
