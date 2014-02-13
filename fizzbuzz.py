"""Creating a user extensible fizzbuzz in which user provide a dict with a key
corresponding to divisor and a value equating the desired string"""


def fizzbuzz(n, divisor_dict):
    result = ''
    for k, v in sorted(divisor_dict.items()):  # create iterable from user dict
        if n % k == 0:
            result.append(v)
    if result == '':
        return n
    return result
