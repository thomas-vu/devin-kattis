def calculate_score(results):
    n = len(results)
    g_wins = 0
    a_wins = 0
    
    # Count wins for Guillaume and Arnar
    for result in results:
        if result == 'G':
            g_wins += 1
        elif result == 'A':
            a_wins += 1
    
    # Calculate the number of matches Guillaume considers valid
    k = min(g_wins, n - g_wins)  # The number of matches Guillaume considers valid
    
    while k > 0:
        if g_wins / (g_wins + a_wins) >= k / (2 * k):
            break
        k -= 1
    
    return f"{g_wins}-{a_wins}"

# Read input
n = int(input())
results = input()

# Calculate and print the score
score = calculate_score(results)
print(score)