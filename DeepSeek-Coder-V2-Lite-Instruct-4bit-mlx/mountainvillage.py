def find_min_difference(matrix, r, c, k):
    def dfs(x, y, visited, min_val, max_val):
        if (x, y) in visited:
            return min_val, max_val
        visited.add((x, y))
        min_val = min(min_val, matrix[x][y])
        max_val = max(max_val, matrix[x][y])
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c:
                min_val, max_val = dfs(nx, ny, visited, min_val, max_val)
        return min_val, max_val
    
    results = []
    for i in range(r):
        for j in range(c):
            visited = set()
            min_val, max_val = dfs(i, j, visited, float('inf'), -float('inf'))
            if len(visited) >= k:
                results.append(max_val - min_val)
    return min(results) if results else 0

def main():
    r, c = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(r)]
    n = int(input())
    queries = [int(input()) for _ in range(n)]
    
    for k in queries:
        print(find_min_difference(matrix, r, c, k))

if __name__ == "__main__":
    main()