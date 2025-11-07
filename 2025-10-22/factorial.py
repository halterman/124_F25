
def factorial(n: int) -> int:
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

print(f"factorial(-1) = {factorial(-1)}")
print(f"factorial(0) = {factorial(0)}")
print(f"factorial(1) = {factorial(1)}")
print(f"factorial(2) = {factorial(2)}")
print(f"factorial(3) = {factorial(3)}")
print(f"factorial(4) = {factorial(4)}")
print(f"factorial(5) = {factorial(5)}")
print(f"factorial(6) = {factorial(6)}")

print(f"factorial(10) = {factorial(10)}")
print(f"factorial(100) = {factorial(100)}")