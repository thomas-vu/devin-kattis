class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    depth = 0
    while True:
        if value < root.value:
            if root.left is None:
                root.left = TreeNode(value)
                return depth + 1
            else:
                root = root.left
        else:
            if root.right is None:
                root.right = TreeNode(value)
                return depth + 1
            else:
                root = root.right
        depth += 1

n = int(input())
sequence = [int(input()) for _ in range(n)]
root = TreeNode(sequence[0])
counters = []
for i in range(1, n):
    counters.append(insert(root, sequence[i]))
for counter in counters:
    print(counter)