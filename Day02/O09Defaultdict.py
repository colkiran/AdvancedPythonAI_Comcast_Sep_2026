
from collections import defaultdict

counts = defaultdict(int)

words = ['apple', 'orange', 'banana', 'apple', 'orange']

for w in words:
    counts[w] += 1

print(counts)
