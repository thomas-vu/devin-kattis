def reconstruct_map(distances):
    n = len(distances)
    roads = []
    
    for i in range(n):
        for j in range(i + 1, n):
            if distances[i][j] == distances[i][0] + distances[0][j]:
                roads.append((i + 1, j + 1))
    
    for road in roads:
        print(road[0], road[1])

# Sample Input 1
n = 4
distances = [
    [0, 1, 1, 2],
    [1, 0, 2, 3],
    [1, 2, 0, 3],
    [2, 3, 3, 0]
]
reconstruct_map(distances)

# Sample Input 2
n = 7
distances = [
    [0, 2, 9, 1, 4, 3, 3],
    [2, 0, 11, 1, 6, 3, 3],
    [9, 11, 0, 10, 5, 12, 12],
    [1, 1, 10, 0, 5, 2, 2],
    [4, 6, 5, 5, 0, 7, 7],
    [3, 3, 12, 2, 7, 0, 4],
    [3, 3, 12, 2, 7, 4, 0]
]
reconstruct_map(distances)