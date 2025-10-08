# Client code
from sqrtfunc import my_sqrt

for num in range(1, 26):
    print(f'The square root of {num} is {my_sqrt(num)}')

print('-----------------')

print(my_sqrt(16))
print(my_sqrt(100 - 6*3))