#Creating a user extensible fizzbuzz with a dict approach


def fizzbuzz(n, dict):
    result = ''
    for k, v in sorted(dict.items()):  # create iterable from user dict
        if n % k == 0:
            result.append(v)
    if result == '':
        return n
    return result
