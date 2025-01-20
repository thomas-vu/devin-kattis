def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

n, m, p = map(int, input().split())
judges = [tuple(map(int, input().split())) for _ in range(n)]
tar_repos = [tuple(map(int, input().split())) for _ in range(m)]
feather_storehouses = [tuple(map(int, input().split())) for _ in range(p)]

total_distance = 0
assigned_tar = [False] * m
assigned_feather = [False] * p

for judge in judges:
    min_tar_dist = float('inf')
    tar_repo_idx = -1
    for i in range(m):
        if not assigned_tar[i]:
            dist = distance(*judge, *tar_repos[i])
            if dist < min_tar_dist:
                min_tar_dist = dist
                tar_repo_idx = i
    
    min_feather_dist = float('inf')
    feather_storehouse_idx = -1
    for i in range(p):
        if not assigned_feather[i]:
            dist = distance(*judge, *feather_storehouses[i])
            if dist < min_feather_dist:
                min_feather_dist = dist
                feather_storehouse_idx = i
    
    total_distance += min_tar_dist + min_feather_dist
    assigned_tar[tar_repo_idx] = True
    assigned_feather[feather_storehouse_idx] = True

print("{:.1f}".format(total_distance))