def parse_tree(s):
    i = 0
    def helper():
        nonlocal i
        if s[i] == '(':
            i += 1
            children = []
            while s[i] != ')':
                children.append(helper())
                if s[i] == ',':
                    i += 1
            i += 1
            return children if len(children) > 1 else children[0]
        else:
            label = s[i]
            i += 1
            return label
    return helper()

def same_tree(root1, root2):
    if isinstance(root1, str) and isinstance(root2, str):
        return root1 == root2
    if isinstance(root1, list) and isinstance(root2, list):
        if len(root1) != len(root2):
            return False
        for i in range(len(root1)):
            if not same_tree(root1[i], root2[i]):
                return False
        return True
    return False

def main():
    t = int(input())
    for _ in range(t):
        tree1 = parse_tree(input())
        tree2 = parse_tree(input())
        if same_tree(tree1, tree2):
            print("same")
        else:
            print("different")

main()