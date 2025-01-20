R, S = map(int, input().split())
garden = [input() for _ in range(R)]
G = int(input())
apples = [tuple(map(int, input().split())) for _ in range(G)]

def squared_distance(r1, s1, r2, s2):
    return (r1 - r2) ** 2 + (s1 - s2) ** 2

for i in range(G):
    r_i, s_i = apples[i]
    min_distance = float('inf')
    for row in range(R):
        for col in range(S):
            if garden[row][col] == 'x':
                distance = squared_distance(r_i, s_i, row + 1, col + 1)
                min_distance = min(min_distance, distance)
    print(min_distance)