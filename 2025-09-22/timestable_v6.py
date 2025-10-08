size = int(input('Please enter table size: '))

print('     ', end='')
for column in range(1, size + 1):
    print(f'{column:3}', end=' ')
print()
print('    +', end='')
for column in range(1, size):
    print('----', end='')
print('---')
for row in range(1, size + 1):
    print(f'{row:3} |', end='')
    for column in range(1, size + 1):
        print(f'{row * column:3}', end=' ')
    print()