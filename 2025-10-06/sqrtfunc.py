
def my_sqrt(x: float) -> float:
    r = 1  # First estimate
    while not (-0.00000001 < r*r - x < 0.0000001):
        r = (r + x/r)/2
    return r

# Simple test code
if __name__ == '__main__':
    for num in range(1, 26):
        print(f'The square root of {num} is {my_sqrt(num)}')

