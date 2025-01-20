def max_area(stories):
    n = len(stories)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        w_i, h_i, x_i, y_i = stories[i - 1]
        for j in range(i + 1, n + 1):
            w_j, h_j, x_j, y_j = stories[j - 1]
            if not (x_i + w_i <= x_j or x_j + w_j <= x_i or y_i + h_i <= y_j or y_j + h_j <= y_i):
                overlap_w = min(x_i + w_i, x_j + w_j) - max(x_i, x_j)
                overlap_h = min(y_i + h_i, y_j + h_j) - max(y_i, y_j)
                overlap_area = overlap_w * overlap_h
                dp[i][j] = max(dp[i - 1][j - 1] + (w_i * h_i) - overlap_area, dp[i - 1][j], dp[j - 1][i])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[j - 1][i])
    
    return dp[n][n]

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        stories = []
        for _ in range(n):
            w, h, x, y = map(int, input().split())
            stories.append((w, h, x, y))
        print(max_area(stories))

if __name__ == "__main__":
    main()