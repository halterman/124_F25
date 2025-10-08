size = int(input('Please enter table size: '))

for column in range(1, size + 1):
    print(f'{column:3}', end=' ')
print()
for column in range(1, size):
    print('----', end='')
print('---')
for row in range(1, size + 1):
    for column in range(1, size + 1):
        print(f'{row * column:3}', end=' ')
    print()