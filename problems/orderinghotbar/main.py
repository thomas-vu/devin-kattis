def min_moves_to_sort(a):
    n = len(a)
    # Create a list to store the minimum number of moves for each position
    dp = [0] * n
    
    # Calculate the minimum number of moves for each position by considering both ends
    for i in range(n):
        min_moves = float('inf')
        for j in range(i + 1):
            # Move the item to the left end
            moves_left = sum(a[j+1:i+1]) + (i - j - 1) * min(a[j+1:i+1])
            # Move the item to the right end
            moves_right = sum(a[j:i]) + (i - j) * min(a[j:i])
            min_moves = min(min_moves, moves_left, moves_right)
        dp[i] = min_moves
    
    # The result is the minimum number of moves for placing all items in their correct positions
    return sum(dp)

# Read input
n = int(input())
a = list(map(int, input().split()))

# Calculate and print the minimum number of moves
print(min_moves_to_sort(a))