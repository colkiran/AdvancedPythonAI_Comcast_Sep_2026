
from collections import Counter

cars = ['merc', 'bmw', 'audi', 'bmw', 'merc', 'bentley', 'merc']
freq = Counter(cars)
print(freq)

print(freq.most_common(3))
print("-" * 60)

print(dir(freq))