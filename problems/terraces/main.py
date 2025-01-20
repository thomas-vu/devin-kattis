def count_water_collectable(garden, x, y):
    water_collected = 0
    for i in range(y):
        for j in range(x):
            if (i == 0 or garden[i-1][j] > garden[i][j]) and \
               (i == y-1 or garden[i+1][j] > garden[i][j]) and \
               (j == 0 or garden[i][j-1] > garden[i][j]) and \
               (j == x-1 or garden[i][j+1] > garden[i][j]):
                water_collected += 1
    return water_collected

x, y = map(int, input().split())
garden = []
for _ in range(y):
    garden.append(list(map(int, input().split())))

print(count_water_collectable(garden, x, y))