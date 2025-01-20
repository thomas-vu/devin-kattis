N, Y = map(int, input().split())
found_obstacles = set([int(input()) for _ in range(Y)])
all_obstacles = set(range(N))
missing_obstacles = sorted(all_obstacles - found_obstacles)
for obstacle in missing_obstacles:
    print(obstacle)
print("Mario got", len(found_obstacles), "of the dangerous obstacles.")