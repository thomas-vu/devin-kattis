def solve(rooms, turns):
    n = len(rooms)
    dp_max = [[0] * n for _ in range(turns + 1)]
    dp_min = [[0] * n for _ in range(turns + 1)]
    
    # Initialize DP tables
    for i in range(n):
        dp_max[0][i] = rooms[i][i]
        dp_min[0][i] = rooms[i][i]
    
    # Fill DP tables
    for t in range(1, turns + 1):
        for i in range(n):
            dp_max[t][i] = rooms[i][i]
            dp_min[t][i] = rooms[i][i]
            for j in range(n):
                if i != j:
                    dp_max[t][i] = max(dp_max[t][i], dp_max[t - 1][j] + rooms[i][j])
                    dp_min[t][i] = min(dp_min[t][i], dp_min[t - 1][j] + rooms[i][j])
    
    return dp_max[turns][0], dp_min[turns][0]

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        rooms = [list(map(int, input().split())) for _ in range(n)]
        m = int(input())
        max_win, min_win = solve(rooms, m)
        print(max_win, min_win)

if __name__ == "__main__":
    main()