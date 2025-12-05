import random
try:
    r = random.randint(1, 3) # r is 1, 2, or 3
    if r == 1:
        print(int('Fred')) # Try to convert a non-integer
    elif r == 2:
        [][2] = 5  # Non-existent index of the empty list
    else:
        print(3/0) # Try to divide by zero
except ValueError:
    print('Cannot convert integer')
except IndexError as e:
    print('List index is out of range')
    print(e)
except ZeroDivisionError:
    print('Division by zero not allowed')
print('Done')
