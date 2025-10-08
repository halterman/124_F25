i = float(input("Please enter number: "))
r = 1  # First estimate
while not (-0.00000001 < r*r - i < 0.0000001):
    print(f'Inside the loop, r = {r} and i = {i}')
    r = (r + i/r)/2

print(f'The square root of {i} is {r}')