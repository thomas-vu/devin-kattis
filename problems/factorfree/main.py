import sys
from math import gcd

# Function to check if a number is coprime with all its ancestors
def is_coprime(node, parent):
    if parent == 0:
        return True
    return gcd(node, parent) == 1

# Function to build the factor-free tree from inorder sequence
def build_factor_free_tree(sequence):
    n = len(sequence)
    parent = [0] * (n + 1)
    stack = []
    
    for node in sequence:
        if not is_coprime(node, stack[-1] if stack else 0):
            return "impossible"
        current = len(stack)
        while stack and is_coprime(node, stack[-1]):
            current = len(stack) - 1
            parent[len(stack)] = stack[-1]
            stack.pop()
        stack.append(node)
    
    while len(stack) > 1:
        parent[len(stack)] = stack[-1]
        stack.pop()
    
    return parent[1:]

# Read input
n = int(sys.stdin.readline().strip())
sequence = list(map(int, sys.stdin.readline().strip().split()))

# Build and output the tree or "impossible" if it doesn't exist
result = build_factor_free_tree(sequence)
if result == "impossible":
    print("impossible")
else:
    print(" ".join(map(str, result)))