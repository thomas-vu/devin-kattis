def find_victorious_knight(n, knights):
    for i in range(n):
        if all(knights[i][0] <= knights[j][1] for j in range(n) if i != j):
            return i + 1
    return -1

n = int(input())
knights = [tuple(map(int, input().split())) for _ in range(n)]
print(find_victorious_knight(n, knights))