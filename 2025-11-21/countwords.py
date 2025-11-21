with open('declaration.txt', 'r') as f:
    contents = f.read().upper()

counters: dict[str, int] = {}

words = contents.split()

for word in words:
    if word not in counters:
        counters[word] = 1
    else:
        counters[word] += 1

for word, count in counters.items():
    print(word, count)

