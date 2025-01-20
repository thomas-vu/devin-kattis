def probability_of_success(n, c, m, henchmen):
    # Convert probabilities to decimal form
    for i in range(n):
        henchmen[i][1] /= 100.0
    
    # Sort henchmen by bribe cost in ascending order
    henchmen.sort(key=lambda x: x[0])
    
    # Initialize DP array to store the maximum probability of success for each number of henchmen converted
    dp = [0.0] * (c + 1)
    dp[0] = 1.0
    
    for i in range(n):
        for j in range(c, 0, -1):
            if m >= henchmen[i][0]:
                dp[j] = max(dp[j], dp[j - 1] * henchmen[i][1])
    
    return dp[c]

def main():
    test_cases = int(input())
    results = []
    
    for _ in range(test_cases):
        n, c, m = map(int, input().split())
        henchmen = [list(map(int, input().split())) for _ in range(n)]
        result = probability_of_success(n, c, m, henchmen)
        results.append("{:.6f}".format(result))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()