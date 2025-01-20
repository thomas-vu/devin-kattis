def calculate_probability(target):
    if target <= 5:
        return (target + 1) / 36.0
    
    dp = [[0] * (target + 1) for _ in range(9)]
    dp[0][0] = 1.0
    
    for i in range(1, 9):
        for j in range(target + 1):
            dp[i][j] = sum(dp[i - 1][j - k] * (k / 6.0) for k in range(1, 7))
    
    total_probability = sum(dp[8][target:])
    return total_probability

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    num_cases = int(data[0])
    results = []
    
    for i in range(1, num_cases + 1):
        target = int(data[i])
        prob = calculate_probability(target)
        results.append(prob)
    
    for result in results:
        print("{:.10f}".format(result))

if __name__ == "__main__":
    main()