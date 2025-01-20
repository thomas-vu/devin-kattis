# Define the data structure to store groups and their members
groups = {}

# Read input until EOF
while True:
    try:
        line = input()
        if not line.startswith("group"):
            continue
        
        _, group_name, n = line.split()
        n = int(n)
        members = []
        for _ in range(n):
            member_name = input()
            members.append(member_name)
        groups[group_name] = set(members)
    except EOFError:
        break

# Process selection expressions
while True:
    try:
        line = input()
        if not line:
            continue
        
        tokens = line.split()
        stack = []
        for token in tokens:
            if token == "group":
                group_name = next(tokens)
                stack.append(groups[group_name])
            elif token == "union":
                set2 = stack.pop()
                set1 = stack.pop()
                stack.append(set1.union(set2))
            elif token == "intersection":
                set2 = stack.pop()
                set1 = stack.pop()
                stack.append(set1.intersection(set2))
            elif token == "difference":
                set2 = stack.pop()
                set1 = stack.pop()
                stack.append(set1.difference(set2))
        
        result_set = sorted(stack[0])
        print(" ".join(result_set))
    except EOFError:
        break