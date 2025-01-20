n, m = map(int, input().split())
schools = [0] * m
for i in range(m):
    schools[i] = int(input())

accepted = [0] * m
capacity_left = n
for school in range(m):
    teams = schools[school]
    while capacity_left > 0 and teams > accepted[school]:
        accepted[school] += 1
        capacity_left -= 1
    if capacity_left == 0:
        break

for accepted_teams in accepted:
    print(accepted_teams)