# write Fibonacci series less than n
def fib(number):
    """Print a Fibonacci series less than number."""
    f0, f1 = 0, 1
    while f0 < number:
        print(f0, end=' ')
        f0, f1 = f1, f0+f1
    print()

print(fib(1994))
