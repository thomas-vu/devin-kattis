def find_words(grid, words):
    h, w = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def dfs(x, y, word, index):
        if index == len(word):
            return True
        if x < 0 or x >= h or y < 0 or y >= w or grid[x][y] != word[index]:
            return False
        temp, grid[x][y] = grid[x][y], '#'
        for dx, dy in directions:
            if dfs(x + dx, y + dy, word, index + 1):
                grid[x][y] = temp
                return True
        grid[x][y] = temp
        return False
    
    count = 0
    for word in words:
        found = False
        for i in range(h):
            for j in range(w):
                if grid[i][j] == word[0] and dfs(i, j, word, 0):
                    count += 1
                    found = True
                    break
            if found:
                break
    return count

h, w = map(int, input().split())
grid = [list(input().strip()) for _ in range(h)]
n = int(input())
words = [input().strip() for _ in range(n)]
print(find_words(grid, words))