import sys
from bisect import bisect_left, bisect_right

# Read dictionary words
n = int(input())
dictionary = [input().strip() for _ in range(n)]
dictionary.sort()

# Preprocess dictionary to get prefixes count
prefix_counts = {}
for word in dictionary:
    for i in range(1, len(word)):
        prefix = word[:i]
        if prefix not in prefix_counts:
            prefix_counts[prefix] = []
        bisect_left_index = bisect_right(prefix_counts[prefix], word)
        prefix_counts[prefix].insert(bisect_left_index, word)

# Process keystroke sequences
q = int(input())
for _ in range(q):
    sequence = input().strip()
    text = ""
    tab_count = 0
    
    for char in sequence:
        if char == '#':
            tab_count += 1
            prefix = text
            if prefix in prefix_counts:
                words = prefix_counts[prefix]
                if tab_count <= len(words):
                    text = words[tab_count - 1]
                else:
                    tab_count = (tab_count - 1) % len(words) + 1
        else:
            text += char
    
    print(text)