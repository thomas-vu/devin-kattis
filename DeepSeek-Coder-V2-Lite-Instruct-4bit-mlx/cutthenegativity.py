n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
flights = []

for i in range(n):
    for j in range(i+1, n):
        if costs[i][j] != -1:
            flights.append((i+1, j+1, costs[i][j]))

flights.sort(key=lambda x: (x[0], x[1]))

print(len(flights))
for flight in flights:
    print(*flight)