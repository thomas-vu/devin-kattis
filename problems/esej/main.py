import random
import string

def generate_essay(A, B):
    words = []
    while len(words) < A:
        word_length = random.randint(1, 15)
        word = ''.join(random.choices(string.ascii_lowercase, k=word_length))
        words.append(word)
    
    essay = ' '.join(words)
    while len(essay.split()) < A or len(essay.split()) > B:
        if len(essay.split()) < A:
            word_length = random.randint(1, 15)
            word = ''.join(random.choices(string.ascii_lowercase, k=word_length))
            essay = ' '.join(words + [word])
        elif len(essay.split()) > B:
            essay = ' '.join(essay.split()[:-1])
    
    return essay

# Read input
A, B = map(int, input().split())

# Generate and print the essay
print(generate_essay(A, B))