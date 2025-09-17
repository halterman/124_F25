number = float(input("Please enter a number in the range 1...10, inclusive: "))

# print(f"You entered {number}")

if number < 1:
    print("Number too low")
elif number > 10:
    print("Number too high")
else:
    print("Number is in range")