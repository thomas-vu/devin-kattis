class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, value):
        while index < self.size:
            self.tree[index] += value
            index |= index + 1

    def query(self, index):
        result = 0
        while index >= 0:
            result += self.tree[index]
            index = (index & (index + 1)) - 1
        return result

# Read input
import sys
input = sys.stdin.read
data = input().split()

index = 0
N = int(data[index])
Q = int(data[index + 1])
index += 2

# Initialize Fenwick Tree
fenwick = FenwickTree(N)

# Process queries
for _ in range(Q):
    op = data[index]
    index += 1
    if op == '+':
        i = int(data[index])
        delta = int(data[index + 1])
        index += 2
        fenwick.update(i, delta)
    elif op == '?':
        i = int(data[index])
        index += 1
        print(fenwick.query(i - 1))