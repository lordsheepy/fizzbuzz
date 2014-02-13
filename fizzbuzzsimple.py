
def fizzbuzz(n):
    result = n
    if n % 3 == 0:
        result = "Fizz"
        if n % 5 == 0:
            result = 'FizzBuzz'
            return result
    elif n % 5 == 0:
        result = "Buzz"
    return result
