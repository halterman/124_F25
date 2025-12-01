with open('declaration.txt', 'r') as f:
    contents = f.read().upper()

counters: dict[str, int] = {}

words = contents.split()

for word in words:
    if word not in counters:
        counters[word] = 1
    else:
        counters[word] += 1

for word, count in sorted(counters.items()):
    print(word, count)


# # Sort by keys (that is, the words)
# for word, count in sorted(counters.items()):
#     print(word, count)

# # Sort by values (that is, the counts)
# counts: list[tuple[int, str]] = []
# for word, count in sorted(counters.items()):
#     counts.append((count, word))
# for pair in sorted(counts):
#     print(pair)

