# write Fibonacci series less than number
def fib(number):
    """Print a Fibonacci series less than number."""
    f0, f1 = 0, 1
    while f0 < number:
        print(f0, end=' ')
        f0, f1 = f1, f0+f1
    print()

fib(1994)

# return Fibonacci series up to n
def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

result = fib2(2000)

print(result)
