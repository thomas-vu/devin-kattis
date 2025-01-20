def count_welcome_to_code_jam(text):
    target = "welcome to code jam"
    n = len(text)
    m = len(target)
    
    # Create a DP table where dp[i][j] represents the number of ways to form the first i characters of target using the first j characters of text
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base case: there is one way to form an empty sequence from the text
    for j in range(n + 1):
        dp[0][j] = 1
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text[j - 1] == target[i - 1]:
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 1]) % 10000
            else:
                dp[i][j] = dp[i][j - 1]
    
    # The answer is the number of ways to form the entire target sequence using the text
    return dp[m][n]

def main():
    T = int(input())
    for case_number in range(1, T + 1):
        text = input()
        result = count_welcome_to_code_jam(text)
        print("Case #{}: {:04d}".format(case_number, result))

if __name__ == "__main__":
    main()