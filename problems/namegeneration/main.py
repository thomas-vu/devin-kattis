import random
import string

def generate_name():
    vowels = 'aeiou'
    consonants = ''.join(chr(c) for c in range(ord('a'), ord('z') + 1) if chr(c) not in vowels)
    
    def is_valid(name):
        for i in range(len(name) - 2):
            if all(c in vowels for c in name[i:i+3]) or all(c in consonants for c in name[i:i+3]):
                return False
        return True
    
    while True:
        name = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 20)))
        if is_valid(name):
            return name

def generate_names(N):
    names = []
    while len(names) < N:
        name = generate_name()
        if name not in names:
            names.append(name)
    return names

N = int(input().strip())
names = generate_names(N)
for name in names:
    print(name)