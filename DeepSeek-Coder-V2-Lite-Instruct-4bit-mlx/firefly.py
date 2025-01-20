N, H = map(int, input().split())
stalagmites = []
stalactites = []
for _ in range(N):
    obstacle_height = int(input())
    if _ % 2 == 0:
        stalagmites.append(obstacle_height)
    else:
        stalactites.append(obstacle_height)

stalagmites.sort()
stalactites.sort()

def count_obstacles(height):
    global stalagmites, stalactites
    idx_s = len(stalagmites) - 1
    idx_a = len(stalactites) - 1
    count = 0
    while idx_s >= 0 and idx_a >= 0:
        if stalagmites[idx_s] < height and stalactites[idx_a] < height:
            count += 2
            idx_s -= 1
            idx_a -= 1
        elif stalagmites[idx_s] < height:
            count += 1
            idx_s -= 1
        elif stalactites[idx_a] < height:
            count += 1
            idx_a -= 1
        else:
            break
    return count

min_obstacles = float('inf')
levels = []
for height in range(1, H + 1):
    obstacles_at_height = count_obstacles(height)
    if obstacles_at_height < min_obstacles:
        min_obstacles = obstacles_at_height
        levels = [height]
    elif obstacles_at_height == min_obstacles:
        levels.append(height)

print(min_obstacles, len(levels))