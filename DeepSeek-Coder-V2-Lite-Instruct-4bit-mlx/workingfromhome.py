import math
m, p, n = map(int, input().split())
workdays = [int(input()) for _ in range(n)]

episodes_watched = 0
current_target = m

for i in range(n):
    if workdays[i] > current_target:
        extra = workdays[i] - current_target
        new_target = math.ceil(current_target - (extra * p / 100))
    else:
        deficit = current_target - workdays[i]
        new_target = math.ceil(current_target + (deficit * p / 100))
    if new_target <= workdays[i]:
        episodes_watched += 1
        current_target = math.ceil(current_target + (workdays[i] - current_target) * p / 100)
    else:
        current_target = new_target

print(episodes_watched)