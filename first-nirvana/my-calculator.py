from enum import Enum

class Command(Enum):
    INIT = -1
    EXIT = 0
    SUM = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4

def is_int(num: int|float) -> None:
    assert type(num) is int, 'Entered number is not integer'

# AFAICT/IMO this is nonsense
def is_float(num: int|float) -> None:
    assert type(num) is float, 'Entered number is not float'

def take_two_number() -> {"num1": float, "num2": float}:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    return { "num1": float(num1), "num2": float(num2) }

def take_number() -> float:
    string_number = input("Enter a number: ")
    string_number = float(string_number)

    return string_number

def sum(
        num1: float,
        num2: float) -> float:
    return num1+num2

def minus(
        num1: float,
        num2: float) -> float:
    return num1-num2

def multiply(
        num1: float,
        num2: float) -> float:
    return num1*num2

def divide(
        num1: float,
        num2: float) -> float:
    return num1/num2

previous_result: float = 0
command: Command = Command.INIT

while command != Command.EXIT:
    command = input("Select command (1.Sum, 2.Minus, 3.multiply, 4.divide, 0.exit): ")
    command = int(command)
    is_int(command)

    if command == Command.EXIT.value:
        break;

    number = take_number()
    
    if command == Command.SUM.value:
        previous_result = sum(previous_result, number)
    elif command == Command.MINUS.value:
        previous_result = minus(previous_result, number)
    elif command == Command.MULTIPLY.value:
        previous_result = multiply(previous_result, number)
    elif command == Command.DIVIDE.value:
        previous_result = divide(previous_result, number)
    else:
        print("Invalid Command!")
        continue;
    
    print("Result: ", previous_result)

"""
    It seems precondition and postcondition is not implemented
    https://pypi.org/project/preconditions/
    https://pypi.org/project/icontract/
    https://pypi.org/project/conditions-py/
"""
# @precondition(lambda num1, num2: is_int(num1) & is_int(num2) )
# @postcondition(lambda returnValue, inputValue: is_int(returnValue))
# def sumInt(
#         num1: int,
#         num2: int) -> int:
#     return num1+num2;