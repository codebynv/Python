# Interleave two lists, keeping remaining values from the longer list.

from itertools import zip_longest

list1 = [1, 3, 5]
list2 = [2, 4, 6, 8, 10]

result = [
    item
    for pair in zip_longest(list1, list2, fillvalue=None)
    for item in pair
    if item is not None
]

print("Interleaved List :", result)
