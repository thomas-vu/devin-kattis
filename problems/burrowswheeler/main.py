def burrows_wheeler_transform(text):
    n = len(text)
    rotations = []
    
    for i in range(n):
        rotations.append(text[i:] + text[:i])
    
    rotations_sorted = sorted(rotations)
    transform = ''.join([rotation[-1] for rotation in rotations_sorted])
    
    return transform

import sys

for line in sys.stdin:
    if line.strip():  # Check for non-empty lines
        text = line.strip()
        print(burrows_wheeler_transform(text))