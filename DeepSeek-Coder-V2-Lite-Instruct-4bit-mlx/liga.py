def fill_missing_fields(teams):
    for i in range(len(teams)):
        if teams[i][4] == '?':
            wins = teams[i][0] - (teams[i][1] + teams[i][2] + teams[i][3])
            lost = wins - (teams[i][0] // 2) + (teams[i][1] // 3)
            draw = teams[i][0] - wins - lost
            points = 3 * wins + draw
            teams[i][4] = points
        if teams[i][3] == '?':
            draw = (teams[i][4] - 3 * teams[i][1]) / 2
            lost = (teams[i][0] - draw) // 2
            points = 3 * teams[i][1] + draw
            if points == int(points) and draw == int(draw):
                teams[i][3] = lost
        if teams[i][2] == '?':
            draw = (teams[i][4] - 3 * teams[i][1]) / 2
            lost = (teams[i][0] - draw) // 2
            points = 3 * teams[i][1] + draw
            if points == int(points) and lost == int(lost):
                teams[i][2] = draw
        if teams[i][1] == '?':
            wins = (teams[i][4] - draw) // 3
            lost = (teams[i][0] - wins) // 2
            points = 3 * wins + draw
            if points == int(points) and wins == int(wins):
                teams[i][1] = wins
        if teams[i][0] == '?':
            draw = (teams[i][4] - 3 * teams[i][1]) / 2
            wins = (teams[i][4] - draw) // 3
            lost = (teams[i][0] - wins) // 2
            points = 3 * wins + draw
            if points == int(points) and lost == int(lost):
                teams[i][0] = wins + draw + lost
    return teams

# Read input
N = int(input())
teams = [list(map(int, input().split())) for _ in range(N)]

# Fill missing fields
filled_teams = fill_missing_fields(teams)

# Output the result
for team in filled_teams:
    print(' '.join(map(str, team)))