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
