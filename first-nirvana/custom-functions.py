def calculate_sum(
        num1: int,
        num2: int = 5) -> int:
    return num1+num2

print(calculate_sum(6546, 15)) # 6561
print(calculate_sum(65.46, 15)) # 80.46s

def print_numbers(
        *numbers: list[int]) -> None:
    for number in numbers:
        print(number)

print_numbers(1,54,45,5,4584,8,84)

# Wrong usage

# def calculate_sum(
#         num1: int = 5,
#         num2: int) -> int:
#     return num1+num2

# TypeError: calculate_sum() takes 2 positional arguments but 3 were given
calculate_sum(65, 15, 6)