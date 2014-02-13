
def fizzbuzz(n, divisor_dict):

    """Creating a user extensible fizzbuzz in which user provide a dict with a
    key corresponding to divisor and a value equating the desired string"""
    result = ''
    for k, v in sorted(divisor_dict.items()):
        if n % k == 0:
            result.append(v)
    if result == '':
        return n
    return result
