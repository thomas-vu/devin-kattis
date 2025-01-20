n, q = map(int, input().split())
tiles = list(map(int, input().split()))
for _ in range(q):
    s_j, d_j = map(int, input().split())
    pos = s_j - 1
    for _ in range(d_j):
        next_pos = pos + 1
        while next_pos < n and tiles[next_pos] <= tiles[pos]:
            next_pos += 1
        if next_pos == n:
            print("leik lokid")
            break
        pos = next_pos
    else:
        print(pos + 1)