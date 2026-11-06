# Count words without treating letter case or punctuation as distinct.

import re
from collections import Counter

sentence = "Python is useful, and Python is readable!"
words = re.findall(r"\b[\w']+\b", sentence.casefold())
frequencies = Counter(words)

for word, count in frequencies.most_common():
    print(f"{word}: {count}")
