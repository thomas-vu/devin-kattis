def min_ticks_to_complete_level(N, tiles):
    # Define the states and transitions for each Mario form
    forms = {
        'S': {'S': 0, '?': 1, '.': -1},
        '?': {'S': 0, '?': 0, '.': -1},
        '.': {'S': 0, '?': 2, '.': -1}
    }
    
    # Initialize the DP array with infinity (impossibile state)
    dp = [[float('inf')] * 3 for _ in range(N)]
    
    # Base case: starting from the first tile with all forms
    for form in range(3):
        if tiles[0] == '.' or tiles[0] == '?':
            dp[0][form] = 0 if tiles[0] == '.' else 2
    
    # Fill the DP array
    for i in range(1, N):
        for form in range(3):
            for prev_form in range(3):
                if tiles[i] == 'S' and forms[chr(ord('A') + prev_form)][chr(ord('A') + form)] == -1:
                    continue
                ticks = forms[chr(ord('A') + prev_form)][tiles[i]]
                if ticks != -1:
                    dp[i][form] = min(dp[i][form], dp[i-1][prev_form] + ticks)
    
    # Check the final states and return the minimum ticks required
    result = min(dp[-1])
    return -1 if result == float('inf') else result

# Read input
N = int(input())
tiles = input()

# Get the result and print it
result = min_ticks_to_complete_level(N, tiles)
print(result)