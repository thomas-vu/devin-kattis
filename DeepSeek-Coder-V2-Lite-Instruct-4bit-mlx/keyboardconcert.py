def min_switches(n, m, instruments):
    notes = [int(x) for x in input().split()]
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    next_note = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Initialize DP table with the first note for each instrument
    for i in range(1, n + 1):
        dp[i][0] = 0
    
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            for k in range(1, instruments[i - 1][0] + 1):
                if instruments[i - 1][k] == notes[j - 1]:
                    if dp[i][j] > dp[i][j - 1]:
                        dp[i][j] = dp[i][j - 1]
                        next_note[i][j] = i
                else:
                    if dp[i][j] > dp[i - 1][j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                        next_note[i][j] = i
            dp[i][j] += 1
    
    min_switches = float('inf')
    final_instrument = 0
    for i in range(1, n + 1):
        if min_switches > dp[i][m]:
            min_switches = dp[i][m]
            final_instrument = i
    
    current_instrument = next_note[final_instrument][m]
    switches = 0
    for j in range(m, 0, -1):
        if next_note[current_instrument][j] != current_instrument:
            switches += 1
            current_instrument = next_note[current_instrument][j]
    
    return switches

# Read input
n, m = map(int, input().split())
instruments = []
for _ in range(n):
    k_i, *notes_i = map(int, input().split())
    instruments.append(notes_i)
tune = list(map(int, input().split()))

# Output the result
print(min_switches(n, m, instruments))