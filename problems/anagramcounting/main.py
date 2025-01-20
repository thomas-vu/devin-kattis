from math import factorial
from collections import Counter
import sys

def count_anagrams(word):
    counts = Counter(word)
    total_permutations = factorial(len(word))
    for count in counts.values():
        total_permutations //= factorial(count)
    return total_permutations

for word in sys.stdin:
    word = word.strip()
    if not word:
        continue
    print(count_anagrams(word))