def can_split_evenly(n, boxes):
    total_sum = sum(boxes)
    if total_sum % 2 != 0:
        return "NO"
    
    target = total_sum // 2
    current_sum = 0
    
    for box in boxes:
        current_sum += box
        if current_sum == target:
            return "YES"
        elif current_sum > target:
            return "NO"
    
    return "NO"

# Read input
n = int(input())
boxes = list(map(int, input().split()))

# Check if it's possible to split the boxes evenly
result = can_split_evenly(n, boxes)
print(result)