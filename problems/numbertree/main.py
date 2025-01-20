def calculate_node_label(H, path):
    label = 0
    for i in range(len(path)):
        if path[i] == 'L':
            label = (label << 1) + 1
        else:
            label = (label << 1) + 2
    return (1 << H) - 1 - label

# Read input
H = int(input().strip())
path = input().strip()

# Calculate and output the result
print(calculate_node_label(H, path))