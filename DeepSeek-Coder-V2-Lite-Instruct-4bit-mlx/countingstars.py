def count_stars(bitmap, m, n):
    def dfs(x, y):
        if x < 0 or x >= m or y < 0 or y >= n or bitmap[x][y] != '#':
            return
        bitmap[x][y] = '.'  # Mark as visited
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)

    stars = 0
    for i in range(m):
        for j in range(n):
            if bitmap[i][j] == '#':
                dfs(i, j)
                stars += 1
    return stars

def main():
    case_number = 0
    while True:
        try:
            m, n = map(int, input().split())
            bitmap = [list(input().strip()) for _ in range(m)]
            stars_counted = count_stars(bitmap, m, n)
            case_number += 1
            print(f"Case {case_number}: {stars_counted}")
        except EOFError:
            break

if __name__ == "__main__":
    main()