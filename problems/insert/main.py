def count_unique_bst(values):
    def generate_trees(start, end):
        if start > end:
            return [None]
        if start == end:
            return [TreeNode(values[start])]
        
        trees = []
        for i in range(start, end + 1):
            left_subtrees = generate_trees(start, i - 1)
            right_subtrees = generate_trees(i + 1, end)
            
            for left in left_subtrees:
                for right in right_subtrees:
                    root = TreeNode(values[i])
                    root.left = left
                    root.right = right
                    trees.append(root)
        return trees
    
    def TreeNode(value):
        return type('TreeNode', (object,), {'__init__': lambda self: [setattr(self, 'val', value)], 'left': None, 'right': None})()
    
    if not values:
        return 0
    trees = generate_trees(0, len(values) - 1)
    return len(trees)

while True:
    N = int(input())
    if N == 0:
        break
    values = list(map(int, input().split()))
    print(count_unique_bst(values))