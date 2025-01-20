def min_keypresses(target, current, suggestions):
    n = len(target)
    m = len(current)
    
    # Create a DP table where dp[i][j] represents the minimum keypresses to match first i chars of target with first j chars of current
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    # Fill the DP table
    for i in range(n + 1):
        for j in range(m + 1):
            if i > 0 and j > 0:
                # No operation (just typing)
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + (target[i - 1] != current[j - 1]))
            if i > 0:
                # Backspace
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + 2)
            if j > 0:
                # Use a suggestion
                for sug in suggestions:
                    if j <= len(sug):
                        dp[i][j] = min(dp[i][j], dp[i][j - 1] + len(sug) - j + 1)
    
    return dp[n][m]

def main():
    T = int(input())
    for _ in range(T):
        target = input()
        current = input()
        suggestions = [input(), input(), input()]
        result = min_keypresses(target, current, suggestions)
        print(result)

if __name__ == "__main__":
    main()