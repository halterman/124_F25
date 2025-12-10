def process(num: int) -> int: 
    samples = [2*x for x in range(num)] 
    try: 
        first_entry = int(input('Number please: ')) 
        second_entry = int(input('Another please: ')) 
        quotient = first_entry // second_entry 
        result = samples[quotient] 
    except ValueError: 
        return 13 
    except ZeroDivisionError: 
        return 22 
    return result 


def compute(val: int) -> int: 
    extra = 2 
    return process(val + extra) 


def calc(n: int) -> int: 
    try: 
        ans = compute(n - 5) 
    except IndexError: 
        ans = 15 
    return ans


if __name__ == '__main__': 
    print(calc(8)) 