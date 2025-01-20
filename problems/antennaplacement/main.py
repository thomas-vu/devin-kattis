def min_antennas(matrix):
    h, w = len(matrix), len(matrix[0])
    dp = [[float('inf')] * w for _ in range(h)]
    
    # Function to check if a position is valid and not covered
    def is_valid(x, y):
        return 0 <= x < h and 0 <= y < w and matrix[x][y] == '*'
    
    # Fill the dp array with minimum antennas needed for each position
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == '*':
                # Directly cover the position with an antenna
                dp[i][j] = 1
                
                # Check the neighboring positions and update the minimum antennas needed
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = i + dx, j + dy
                    if is_valid(nx, ny):
                        dp[i][j] = min(dp[i][j], 1 + min(dp[nx][ny] if dp[nx][ny] != float('inf') else float('inf') for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]))
    
    # The minimum number of antennas needed to cover all points of interest
    min_antennas = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == '*':
                min_antennas = max(min_antennas, dp[i][j])
    
    return min_antennas

def main():
    n = int(input())
    scenarios = []
    for _ in range(n):
        h, w = map(int, input().split())
        matrix = [input() for _ in range(h)]
        scenarios.append(matrix)
    
    for scenario in scenarios:
        print(min_antennas([list(row) for row in scenario]))

if __name__ == "__main__":
    main()