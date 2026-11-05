# Count the frequency of each list element.

from collections import Counter

numbers = [10, 20, 10, 30, 20, 10, 40]
frequency = Counter(numbers)

print("Frequencies =", dict(frequency))
