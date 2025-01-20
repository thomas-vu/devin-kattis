R, C = map(int, input().split())
N = int(input())
seats = [[0] * (C + 2) for _ in range(R + 2)]

for _ in range(N):
    r, c = map(int, input().split())
    seats[r][c] = 1

result = [0] * 9

for i in range(1, R + 1):
    for j in range(1, C + 1):
        if seats[i][j] == 1:
            count = 0
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if x == 0 and y == 0:
                        continue
                    if seats[i + x][j + y] == 1:
                        count += 1
            result[count] += 1

print(' '.join(map(str, result)))