def count_destroyed_residential(map, L, W):
    destroyed = 0
    for i in range(L):
        for j in range(W):
            if map[i][j] == 'R':
                destroyed += 1
    return destroyed

def godzilla_moves(map, L, W):
    for i in range(L):
        for j in range(W):
            if map[i][j] == 'G':
                # Check North
                for k in range(i-1, -1, -1):
                    if map[k][j] == 'R':
                        map[k][j] = '.'
                        destroyed += 1
                    elif map[k][j] == 'M':
                        break
                # Check East
                for k in range(j+1, W):
                    if map[i][k] == 'R':
                        map[i][k] = '.'
                        destroyed += 1
                    elif map[i][k] == 'M':
                        break
                # Check South
                for k in range(i+1, L):
                    if map[k][j] == 'R':
                        map[k][j] = '.'
                        destroyed += 1
                    elif map[k][j] == 'M':
                        break
                # Check West
                for k in range(j-1, -1, -1):
                    if map[i][k] == 'R':
                        map[i][k] = '.'
                        destroyed += 1
                    elif map[i][k] == 'M':
                        break
    return destroyed

def main():
    T = int(input())
    for _ in range(T):
        L, W = map(int, input().split())
        map_matrix = [list(input().strip()) for _ in range(L)]
        destroyed = 0
        godzilla_moves(map_matrix, L, W)
        print(destroyed)

main()