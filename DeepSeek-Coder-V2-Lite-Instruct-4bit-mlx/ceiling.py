# This problem involves generating unique tree shapes from given sequences of integers and counting them. 
# We can represent the sequence as a preorder traversal of the tree, where each node is represented by its value.
# We can use a dictionary to map the preorder traversals of trees to their counts, since preorder traversal uniquely identifies a tree shape.
# Here's the approach to solve the problem:
# 1. Generate all possible preorder traversals of trees with k nodes (since each prototype has k layers).
# 2. Use a dictionary to count the occurrences of each unique preorder traversal (tree shape).
# 3. Output the number of unique tree shapes found by counting the keys in the dictionary.
from collections import defaultdict
import sys

# Function to generate preorder traversal of the tree for a given sequence
def generate_preorder(seq):
    if not seq:
        return "#"
    root = str(seq[0])
    left_subtree = generate_preorder(seq[1:]) if seq[1:] else "#"
    right_subtree = generate_preorder(seq[2:]) if seq[2:] else "#"
    return root + "," + left_subtree + "," + right_subtree

# Read input
n, k = map(int, sys.stdin.readline().split())
prototypes = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# Generate preorder traversals and count unique shapes
shape_count = defaultdict(int)
for prototype in prototypes:
    preorder = generate_preorder(prototype)
    shape_count[preorder] += 1

# Output the number of unique tree shapes
print(len(shape_count))