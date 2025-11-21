with open('declaration.txt', 'r') as f:
    contents = f.read().upper()

counters = [0] * 26

print(contents)

for ch in contents:
    if 'A' <= ch <= 'Z':
        counters[ord(ch) - ord('A')] += 1

for letter, count in enumerate(counters):
    print(chr(ord('A') + letter), count)
