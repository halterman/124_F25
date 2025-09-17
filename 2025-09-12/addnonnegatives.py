# Provide instructions to the user
print('Please enter non-negative integers to add.')
print('End your list with a negative integer.')

# Initialize variables
sum = 0
number = 0
# Get the values from the user
while number >= 0:
    number = int(input('=> '))
    if number >= 0:
        sum += number
# Display the result
print(f'The sum is {sum}')
