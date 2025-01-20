class TreeNode:
    def __init__(self, name):
        self.name = name
        self.parents = []
        self.ancestors = set()

def find_ancestors(node, ancestors):
    for parent in node.parents:
        if parent not in ancestors:
            ancestors.add(parent)
            find_ancestors(parent, ancestors)

def detect_hillbillies_and_paradoxes(family):
    name_to_node = {}
    for parent, child in family:
        if parent not in name_to_node:
            name_to_node[parent] = TreeNode(parent)
        if child not in name_to_node:
            name_to_node[child] = TreeNode(child)
        parent_node, child_node = name_to_node[parent], name_to_node[child]
        parent_node.ancestors.add(parent)
        child_node.parents.append(parent_node)
        find_ancestors(child_node, child_node.ancestors)
    
    hillbillies = set()
    paradoxes = set()
    for node in name_to_node.values():
        if len(set(node.ancestors)) != len(node.ancestors):
            hillbillies.add(node.name)
        if node.name in node.ancestors:
            paradoxes.add(node.name)
    
    return sorted(hillbillies), sorted(paradoxes)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    families = []
    family = []
    for word in data:
        if word == 'done':
            families.append(family)
            family = []
        else:
            parent, child = word.split()
            family.append((parent, child))
    
    for i, family in enumerate(families):
        hillbillies, paradoxes = detect_hillbillies_and_paradoxes(family)
        if hillbillies or paradoxes:
            for hillbilly in hillbillies:
                print(f"{hillbilly} hillbilly")
            for paradox in paradoxes:
                print(f"{paradox} paradox")
            if i < len(families) - 1:
                print()

if __name__ == "__main__":
    main()