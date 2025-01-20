def min_gates_to_change(tree, desired_value):
    # Helper function to build the tree from the input
    def build_tree(index):
        if index >= len(tree['values']):
            return tree['values'][index]
        left_child = build_tree(2 * index)
        right_child = build_tree(2 * index + 1)
        return left_child, right_child
    
    # Helper function to calculate the minimum changes needed
    def min_changes(node, value):
        if node is None:
            return float('inf')
        left_val, right_val = node
        if isinstance(left_val, tuple):
            left_val = build_tree(2 * index)
        if isinstance(right_val, tuple):
            right_val = build_tree(2 * index + 1)
        
        if isinstance(left_val, bool) and isinstance(right_val, bool):
            current_value = (left_val and right_val) if tree['gates'][index] == 1 else (left_val or right_val)
            if current_value == value:
                return 0
            else:
                # Change the gate at this node
                if tree['gates'][index] == 1:
                    return min(min_changes(2 * index, value), min_changes(2 * index + 1, value)) + 1
                else:
                    return min(min_changes(2 * index, not value), min_changes(2 * index + 1, not value)) + 1
        else:
            return float('inf')
    
    # Build the tree from the input
    index = 1
    while index < len(tree['values']):
        index *= 2
    
    # Calculate the minimum changes needed
    result = min_changes(index // 2, desired_value)
    return "IMPOSSIBLE" if result == float('inf') else result

# Read input and process each test case
num_cases = int(input())
for case in range(1, num_cases + 1):
    M, V = map(int, input().split())
    gates = []
    values = []
    for _ in range(M - (M + 1) // 2):
        G, C = map(int, input().split())
        gates.append(G)
    for _ in range((M + 1) // 2):
        values.append(int(input()))
    
    tree = {
        'gates': gates,
        'values': values
    }
    
    result = min_gates_to_change(tree, V)
    print(f"Case #{case}: {result}")