import sys
from itertools import combinations

# Fast input reading
input = sys.stdin.readline

# Read the number of sequences and the length of each sequence, and the difference count
N, M, K = map(int, input().split())

# Read the sequences
sequences = [input().strip() for _ in range(N)]

# Function to count the number of differences between two sequences
def count_differences(seq1, seq2):
    return sum(c1 != c2 for c1, c2 in zip(seq1, seq2))

# Iterate through each sequence to find the one that differs in exactly K places from all others
for i, seq in enumerate(sequences):
    diff_count = sum(1 for other_seq in sequences if count_differences(seq, other_seq) == K)
    if diff_count == N - 1:
        print(i + 1)
        break