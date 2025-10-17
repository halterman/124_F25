from typing import Callable

ArithFunc = Callable[[float, float], float]

def add(a: float, b: float) -> float:
    """
    Adds the two parameters a and b and returns the result.
    a is a floating point number
    b is a floating point number
    """
    return a + b

def multiply(a: float, b: float) -> float:
    """
    Multiplies the two parameters a and b and returns the result.
    a is a floating point number
    b is a floating point number
    """
    return a * b


def eval(f: ArithFunc, a: float, b: float) -> float:
    """
    Applies the f function to the two parameters a and b 
    and returns the result.
    f is a function that accepts two float parameters a 
      and b and returns the result.
    a is a floating point number
    b is a floating point number
    """
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

