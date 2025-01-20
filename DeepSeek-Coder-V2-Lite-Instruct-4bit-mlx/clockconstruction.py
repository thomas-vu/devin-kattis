def min_groups(N, H, W):
    # Helper function to check if a pixel is on or off
    def is_on(pixel):
        return pixel == '*'

    # Generate all possible groups of pixels
    def generate_groups(h, w):
        groups = []
        for i in range(H - h + 1):
            for j in range(W - w + 1):
                group = []
                for k in range(i, i + h):
                    row = ''
                    for l in range(j, j + w):
                        row += clock[k][l]
                    group.append(row)
                groups.append(group)
        return groups

    # Read the clock display
    clock = [input().strip() for _ in range(H)]

    # Generate all possible groups of pixels
    groups = generate_groups(1, 1)
    min_groups_needed = len(groups)

    # Try different group sizes to find the minimum number of groups needed
    for h1 in range(1, H + 1):
        for w1 in range(1, W + 1):
            groups = generate_groups(h1, w1)
            if len(set(''.join(g) for g in groups)) >= N:
                min_groups_needed = min(min_groups_needed, len(groups))

    return min_groups_needed

# Read input
N, H, W = map(int, input().split())
print(min_groups(N, H, W))