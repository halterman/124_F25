size = int(input('Please enter table size: '))

for row in range(1, size + 1):
    for column in range(1, size + 1):
        print(f'{row * column:3}', end=' ')
    print()