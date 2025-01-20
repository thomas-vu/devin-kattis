def min_minutes(N, K, skills):
    skills.sort(reverse=True)
    teams = [skills[i * K:(i + 1) * K] for i in range((N // K))]
    max_team_size = max(len(team) for team in teams)
    
    minutes = 0
    for i in range(max_team_size):
        team_skills = [teams[t][i] for t in range(len(teams)) if i < len(teams[t])]
        minutes = max(minutes, max(team_skills) - min(team_skills))
    
    return minutes

# Read input
N, K = map(int, input().split())
skills = list(map(int, input().split()))

# Calculate and print the result
print(min_minutes(N, K, skills))