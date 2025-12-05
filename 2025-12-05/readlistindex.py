import random

def make_list() -> list[int]:
    # List will contain up to 10 elements
    n = random.randrange(10)
    result = [0] * n
    for i in range(n):
        result[i] = random.randrange(100)
    return result

if __name__ == '__main__':
    lst = make_list()
    idx = int(input('Please enter position: '))
    # print(lst[idx])
    
    if -len(lst) <= idx <= len(lst):
        print(lst[idx])

