# write Fibonacci series less than number
def fib(number):
    """Print a Fibonacci series less than number."""
    f0, f1 = 0, 1
    while f0 < number:
        print(f0, end=' ')
        f0, f1 = f1, f0+f1
    print()

fib(1994)

# return Fibonacci series up to number
def fib2(number):
    """Return a list containing the Fibonacci series up to number."""
    result = []
    f0, f1 = 0, 1
    while f0 < number:
        result.append(f0) # result = result + [a]
        f0, f1 = f1, f0+f1
    return result

result = fib2(2000)

print(result)
