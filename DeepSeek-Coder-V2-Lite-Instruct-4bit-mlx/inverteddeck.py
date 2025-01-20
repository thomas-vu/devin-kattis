def can_restore_order(n, rarities):
    # Create a list to track the position of each rarity value
    positions = [0] * (n + 1)
    for i, rarity in enumerate(rarities):
        positions[rarity] = i
    
    # Check for the longest sequence where reversing it would sort the list
    max_len = 0
    start, end = -1, -1
    
    for length in range(1, n + 1):
        if positions[length] < positions[length - 1]:
            continue
        
        # Calculate the end of the subsequence where reversing would sort this segment
        current_end = positions[length]
        while length < n and positions[length + 1] > current_end:
            length += 1
            current_end = positions[length]
        
        # Check if reversing the subsequence from start to end sorts the list
        if length - i + 1 > max_len:
            max_len = length - i + 1
            start, end = i + 1, length + 1
    
    if max_len == n:
        return (start, end)
    else:
        return "impossible"

# Read input
n = int(input())
rarities = list(map(int, input().split()))

# Output the result
result = can_restore_order(n, rarities)
if result == "impossible":
    print("impossible")
else:
    print(*result)