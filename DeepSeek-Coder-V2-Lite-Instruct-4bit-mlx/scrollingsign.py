def min_letters_to_display(k, words):
    dp = [0] * (len(words) + 1)
    for i in range(1, len(words) + 1):
        dp[i] = dp[i - 1] + k
        for j in range(i):
            if len(set(words[j:i])) <= k:
                dp[i] = min(dp[i], dp[j] + (k - len(words[j:i])) * (len(words[j:i]) < k))
    return dp[-1]

def main():
    n = int(input())
    for _ in range(n):
        k, w = map(int, input().split())
        words = [input().strip() for _ in range(w)]
        result = min_letters_to_display(k, words)
        print(result)

if __name__ == "__main__":
    main()