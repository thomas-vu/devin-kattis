def max_teams(n, ranks):
    # Sort the competitors by their rank and preferences
    sorted_ranks = sorted([(a, b) for a, b in zip(ranks, range(n))], key=lambda x: (x[0][0], -x[1]))
    
    # Initialize the count of teams and a list to track team formation status
    team_count = 0
    taken = [False] * n
    
    # Iterate through the sorted competitors
    for i in range(n):
        if not taken[i]:
            # Find the next available teammate for the current competitor
            for j in range(i + 1, n):
                if not taken[j] and sorted_ranks[i][0][0] <= sorted_ranks[j][0][0] and sorted_ranks[i][0][1] >= sorted_ranks[j][0][1]:
                    taken[i], taken[j] = True, True  # Mark them as taken for a team
                    team_count += 1
                    break  # Move to the next competitor after forming a team
    
    return team_count

# Read input
n = int(input())
ranks = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_teams(n, ranks))