def can_divide_teams(n, coworkers):
    skill_sums = {}
    
    for b, p in coworkers:
        total_skill = b + p
        if total_skill in skill_sums:
            skill_sums[total_skill] += 1
        else:
            skill_sums[total_skill] = 1
    
    for count in skill_sums.values():
        if count % 2 != 0:
            return "impossible"
    return "possible"

n = int(input().strip())
coworkers = [tuple(map(int, input().strip().split())) for _ in range(n)]
print(can_divide_teams(n, coworkers))