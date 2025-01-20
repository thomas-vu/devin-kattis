import itertools
import string

def generate_word_ladder(n):
    words = list(string.ascii_lowercase) * (n // 26 + 1)[:n]
    for i in range(n):
        for j in range(i + 1, n):
            if sum((a != b) for a, b in zip(words[i], words[j])) == 1:
                words[i], words[j] = words[j], words[i]
    return words[:n]

n = int(input().strip())
word_ladder = generate_word_ladder(n)
for word in word_ladder:
    print(word)