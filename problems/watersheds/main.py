def find_basins(map, H, W):
    labels = [[0] * W for _ in range(H)]
    basin_index = 1
    
    def dfs(x, y, label):
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            if labels[cx][cy] == 0:
                labels[cx][cy] = label
                min_neighbor = (cx, cy)
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < H and 0 <= ny < W:
                        if map[nx][ny] < map[min_neighbor[0]][min_neighbor[1]]:
                            min_neighbor = (nx, ny)
                if min_neighbor != (cx, cy):
                    stack.append((min_neighbor[0], min_neighbor[1]))
    
    for i in range(H):
        for j in range(W):
            if labels[i][j] == 0:
                dfs(i, j, basin_index)
                basin_index += 1
    
    return labels

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for t in range(1, T + 1):
        H = int(data[index])
        W = int(data[index + 1])
        map = []
        for i in range(H):
            row = list(map(int, data[index + 2 + i].split()))
            map.append(row)
        index += 2 + H
        
        labels = find_basins(map, H, W)
        result = []
        for i in range(H):
            row_result = []
            for j in range(W):
                row_result.append(chr(ord('a') + labels[i][j] - 1))
            result.append(''.join(row_result))
        results.append(f"Case #{t}:")
        for row in result:
            results[-1] += "\n" + row
    
    for r in results:
        print(r)

main()