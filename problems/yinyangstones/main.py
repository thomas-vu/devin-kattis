def can_balance(s):
    n = len(s)
    diff = 0
    
    # Calculate the difference between black and white stones for each position in the circle
    for i in range(n):
        if s[i] == 'B':
            diff += 1
        else:
            diff -= 1
    
    # If the total difference is zero, it means we can balance the stones by picking a sequence
    # where there is exactly one more of one type than the other
    return int(diff == 0)

# Read input from stdin
s = input().strip()
print(can_balance(s))