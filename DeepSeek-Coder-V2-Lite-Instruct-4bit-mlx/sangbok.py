def min_seconds_to_sing(t, n, song_times):
    # Sort the song times in non-decreasing order
    song_times.sort()
    
    # Initialize a dynamic programming table where dp[i] represents the minimum number of seconds to sing i songs
    dp = [float('inf')] * (t + 1)
    dp[0] = 0
    
    # Use a subset sum approach to fill the DP table
    for song_time in song_times:
        for i in range(t, song_time - 1, -1):
            dp[i] = min(dp[i], dp[i - song_time] + 1)
    
    # Find the maximum number of songs that can be sung within the time limit
    for i in range(t, -1, -1):
        if dp[i] != float('inf'):
            return i

# Read input from stdin
t, n = map(int, input().split())
song_times = list(map(int, input().split()))

# Output the result
print(min_seconds_to_sing(t, n, song_times))