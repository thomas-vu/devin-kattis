def min_crayons_to_remove(N, K, boxes):
    from collections import defaultdict
    
    color_count = defaultdict(int)
    
    for box in boxes:
        for color in box:
            color_count[color] += 1
    
    min_removals = float('inf')
    
    for box in boxes:
        unique_colors = set(box)
        removals = 0
        for color in box:
            if color_count[color] > 1:
                removals += 1
        min_removals = min(min_removals, removals)
    
    return min_removals

# Read input
N, K = map(int, input().split())
boxes = [input().split() for _ in range(N)]

# Calculate and output the result
print(min_crayons_to_remove(N, K, boxes))