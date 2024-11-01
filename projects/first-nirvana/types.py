# Integer, Floating points

num1 = 123
num2 = 23.32

print(num1 + num2) # 146.32

# Strings

str1 = "Kasir"
str2 = 'Mohammad Jawad'

print(str1, str2) # Kasir Mohammad Jawad

# Convert string to integer

num1 = int("3")
num2 = int('98')

print(num1 + num2) # 101

# Wrong usage

# ValueError: invalid literal for int() with base 10: 'asd'
wrong_usage_1 = int("asd")
# ValueError: invalid literal for int() with base 10: '12asd'
wrong_usage_2 = int("12asd")
# ValueError: invalid literal for int() with base 10: '12.21'
wrong_usage_3 = int("12.21")