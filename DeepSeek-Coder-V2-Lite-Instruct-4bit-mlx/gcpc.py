n, m = map(int, input().split())
favorite_team = 1
teams = {i: [0, 0] for i in range(1, n + 1)}
solved_count = 0

for _ in range(m):
    t, p = map(int, input().split())
    teams[t][0] += 1
    teams[t][1] += p

sorted_teams = sorted(teams.items(), key=lambda x: (-x[1][0], x[1][1]))

for i in range(m):
    t, p = map(int, input().split())
    teams[t][0] += 1
    teams[t][1] += p
    rank = 1
    for team, score in sorted_teams:
        if teams[favorite_team] < (score[0], score[1]):
            rank += 1
    print(rank)