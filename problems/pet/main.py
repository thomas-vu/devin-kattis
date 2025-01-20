# Read the input data
contestants = []
for _ in range(5):
    contestants.append([int(x) for x in input().split()])

# Calculate the points for each contestant
points = []
for i in range(5):
    total_points = sum(contestants[i])
    points.append((i + 1, total_points))

# Determine the winner
winner = max(points, key=lambda x: x[1])
print(f"{winner[0]} {winner[1]}")