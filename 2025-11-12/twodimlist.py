
def matrix_print(m: list[list[int]]) -> None:
    for row in m:
        for column in row:
            print(f'{column:4}', end=' ')
        print()
        

m1 = [[1, 2, 3],
      [0, 0, 4],
      [5, 2, 3]]

m2 = [[324,  12,  30, 234],
      [  3,  35, 100,   0],
      [ 25, 217,   3,  88]]

print(m2[1][2])
print(m2[1])

matrix_print(m1) 

matrix_print(m2) 