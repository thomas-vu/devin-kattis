def count_good_itineraries(events):
    n = len(events)
    last_occurrences = {}
    dp = [0] * n
    
    # Precompute the last occurrences of each character
    for i in range(n):
        last_occurrences[events[i]] = i
    
    # Compute the number of good itineraries ending at each position
    for i in range(1, n):
        dp[i] = dp[i - 1]
        for prev_char, last_pos in last_occurrences.items():
            if events[i] != prev_char and i - last_pos > 1:
                dp[i] += 1
    
    # Sum up all the good itineraries
    return sum(dp)

# Read input from stdin
events = input().strip()

# Calculate and print the number of good itineraries
print(count_good_itineraries(events))