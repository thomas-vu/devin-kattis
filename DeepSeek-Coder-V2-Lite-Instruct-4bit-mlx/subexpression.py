class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        if not self.left and not self.right:
            return str(self.value)
        left_str = str(self.left) if self.left else ''
        right_str = str(self.right) if self.right else ''
        return f'{self.value}({left_str},{right_str})'

def parse(expression):
    if '(' not in expression:
        return Node(expression)
    count = 0
    for i, char in enumerate(expression):
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count == 0 and char == ',':
            left_expr = expression[1:i]
            right_expr = expression[i+1:-1]
            break
    left_node = parse(left_expr)
    right_node = parse(right_expr)
    return Node(expression[0], left_node, right_node)

def min_graph(expr):
    root = parse(expr)
    node_map = {}
    
    def dfs(node):
        if not node:
            return ''
        if node in node_map:
            return str(node_map[node])
        value = node.value
        left_str = dfs(node.left)
        right_str = dfs(node.right)
        new_value = len(node_map) + 1
        node_map[node] = new_value
        if not left_str and not right_str:
            return value
        else:
            left_str = str(dfs(node.left)) if node.left else ''
            right_str = str(dfs(node.right)) if node.right else ''
            return f'{value}({left_str},{right_str})'
    
    return dfs(root)

c = int(input())
for _ in range(c):
    expr = input()
    print(min_graph(expr))