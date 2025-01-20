import re
from collections import defaultdict

def core_word(word):
    return ''.join([c for c in word.lower() if c.isalpha()])

def similar_words(word):
    word = core_word(word)
    similars = set()
    
    def delete_char(w, i):
        return w[:i] + w[i+1:]
    
    def insert_char(w, i, c):
        return w[:i] + c + w[i:]
    
    def replace_char(w, i, c):
        return w[:i] + c + w[i+1:]
    
    def transpose_chars(w, i):
        if i < len(w) - 1:
            return w[:i] + w[i+1] + w[i] + w[i+2:]
        return w
    
    for i in range(len(word)):
        similars.add(core_word(delete_char(word, i)))
        for c in 'abcdefghijklmnopqrstuvwxyz':
            similars.add(core_word(insert_char(word, i, c)))
            if i < len(word) - 1:
                similars.add(core_word(replace_char(word, i, c)))
            similars.add(core_word(transpose_chars(word, i)))
    
    return similars

words = []
while True:
    line = input().strip()
    if line == '***':
        break
    words.extend(line.split())

word_cores = defaultdict(set)
for word in words:
    core = core_word(word)
    if core:
        word_cores[core].add(core_word(word))

similar_candidates = set()
for core, wordset in word_cores.items():
    for other_core in similar_words(core):
        if core != other_core:
            similar_candidates.add((min(core, other_core), max(core, other_core)))

output = []
for (a, b) in sorted(similar_candidates):
    output.append(f"{a}: {b}")

if output:
    for line in output:
        print(line)
else:
    print("***")