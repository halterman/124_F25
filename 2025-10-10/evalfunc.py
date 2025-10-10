from typing import Callable


def add(a: float, b: float) -> float:
    return a + b

def multiply(a: float, b: float) -> float:
    return a * b

def eval(f: Callable[[float, float], float], a: float, b: float) -> float:
    return f(a, b)

num1 = float(input('Please enter a number: '))
num2 = float(input('Please enter another number: '))

# Call the add and multiply functions directly
print(f'{num1} plus {num2} equals {add(num1, num2)}')
print(f'{num1} times {num2} equals {multiply(num1, num2)}')

print('--------------------------------------------------')

# Call the add and multiply functions indirectly through the
# eval function
print(f'{num1} plus {num2} equals {eval(add, num1, num2)}')
print(f'{num1} times {num2} equals {eval(multiply, num1, num2)}')
