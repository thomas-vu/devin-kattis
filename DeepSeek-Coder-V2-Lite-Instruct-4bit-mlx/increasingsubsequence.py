def find_longest_increasing_subsequence(arr):
    if not arr:
        return []
    
    n = len(arr)
    dp = [1] * n
    prev = [-1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
    
    max_len = max(dp)
    index = dp.index(max_len)
    
    result = []
    while index != -1:
        result.append(arr[index])
        index = prev[index]
    
    return max_len, list(reversed(result))

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        
        arr = list(map(int, input().split()))
        max_len, subsequence = find_longest_increasing_subsequence(arr)
        print(max_len)

if __name__ == "__main__":
    main()