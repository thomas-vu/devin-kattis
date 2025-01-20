from math import gcd

def main():
    while True:
        n, d, m = map(int, input().split())
        if n == 0 and d == 0 and m == 0:
            break
        
        moles = []
        for _ in range(m):
            x, y, t = map(int, input().split())
            moles.append((x, y, t))
        
        # Sort moles by time of appearance
        moles.sort(key=lambda x: x[2])
        
        # Initialize DP array to store the maximum score up to each mole
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Process each mole and update the DP array
        for i in range(m):
            x1, y1, _ = moles[i]
            new_dp = [row[:] for row in dp]
            
            for x2 in range(n):
                for y2 in range(n):
                    if (x1, y1) == (x2, y2):
                        new_dp[x2][y2] = max(new_dp[x2][y2], dp[x1][y1] + 1)
                    else:
                        # Check if (x2, y2) is within the allowed distance from (x1, y1)
                        if max(abs(x2 - x1), abs(y2 - y1)) <= d:
                            new_dp[x2][y2] = max(new_dp[x2][y2], dp[x1][y1] + 1)
            
            # Update the DP array with new values
            dp = new_dp
        
        # The maximum score is the maximum value in the DP array after processing all moles
        max_score = 0
        for x in range(n):
            for y in range(n):
                max_score = max(max_score, dp[x][y])
        
        print(max_score)

if __name__ == "__main__":
    main()