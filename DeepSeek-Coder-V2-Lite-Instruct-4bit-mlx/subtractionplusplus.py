def can_alex_win(n):
    # Create a list to store the results for each number of cobblestones
    dp = [False] * (n + 1)
    
    # Base case: if there are no cobblestones, Alex loses
    dp[0] = False
    
    # Fill the list for each number of cobblestones up to n
    for i in range(1, n + 1):
        # Check all possible moves Alex and Steve can make
        for j in range(1, min(i, 5) + 1):
            # If after the move the other player cannot make a move, this player wins
            if not dp[i - j]:
                dp[i] = True
                break
    
    # Return "YES" if Alex can win, otherwise return "NO"
    return "YES" if dp[n] else "NO"

# Read the input
n = int(input().strip())

# Output the result
print(can_alex_win(n))