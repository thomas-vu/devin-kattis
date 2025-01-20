def generate_tree(N):
    tree = [0] * (2**N - 1)
    
    def fill_tree(start, end, level):
        if start == end:
            tree[start] = 1 << (N - level - 1)
            return
        mid = (start + end) // 2
        fill_tree(start, mid, level + 1)
        fill_tree(mid + 1, end, level + 1)
    
    fill_tree(0, len(tree) - 1, 0)
    return tree

def preorder_traversal(tree, index):
    if index >= len(tree) or tree[index] == 0:
        return []
    result = [tree[index]]
    left_subtree = preorder_traversal(tree, 2 * index + 1)
    right_subtree = preorder_traversal(tree, 2 * index + 2)
    return result + left_subtree + right_subtree

N = int(input())
tree = generate_tree(N)
preorder = preorder_traversal(tree, 0)
print(' '.join(map(str, preorder)))