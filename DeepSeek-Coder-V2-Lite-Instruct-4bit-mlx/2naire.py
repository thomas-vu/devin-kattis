def expected_prize(n, t):
    # Dynamic programming approach to calculate the expected prize
    dp = [0.0] * (n + 1)
    dp[0] = 1.0  # Starting prize of $1
    
    for i in range(1, n + 1):
        p = (t + 1 - i) / (1 - i)  # Probability of answering the question
        for j in range(i, -1, -1):
            dp[j] = (dp[j] * (1 - p)) + (dp[j - 1] * p if j > 0 else 0)
    
    expected_prize = sum(dp[i] * (2 ** i) for i in range(n + 1))
    return expected_prize

while True:
    line = input()
    if line == "0 0":
        break
    n, t = map(float, line.split())
    n = int(n)
    result = expected_prize(n, t)
    print("{:.3f}".format(result))