print('i         r1              r2               diff')
print('-----------------------------------------------')
for i in range(20):
    r = 1.0  # First estimate
    while not (-0.00001 < r*r - i < 0.0001):
        # print(f'Inside the loop, r = {r} and i = {i}')
        r = (r + i/r)/2
    
    sq = i**0.5
    print(f'{i}:  {r:12.8}   {sq:12.8}    {r - sq:12.8}')