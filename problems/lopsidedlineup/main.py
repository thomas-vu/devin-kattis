def max_team_strength_difference(n, c):
    # Split the players into two teams with equal size
    team1 = []
    team2 = []
    
    # Calculate the total strength of all players
    total_strength = sum(sum(row) for row in c)
    
    # Calculate the average strength per player
    avg_strength = total_strength / n
    
    # Distribute players to minimize the difference in team strengths
    for i in range(n):
        if sum(team1) + c[i][i] <= avg_strength:
            team1.append(i)
        else:
            team2.append(i)
    
    # Calculate the strength of each team
    strength_team1 = 0
    strength_team2 = 0
    
    for i in team1:
        for j in team1:
            if i != j:
                strength_team1 += c[i][j]
    
    for i in team2:
        for j in team2:
            if i != j:
                strength_team2 += c[i][j]
    
    # Return the maximum possible difference in strength between two teams
    return abs(strength_team1 - strength_team2)

# Read input
n = int(input())
c = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_team_strength_difference(n, c))