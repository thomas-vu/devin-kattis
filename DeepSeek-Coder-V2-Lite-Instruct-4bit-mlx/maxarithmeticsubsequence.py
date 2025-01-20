def solve(n, c, arr):
    if n <= c * (c + 1) // 2:
        return -1
    max_len = 0
    for i in range(n):
        for j in range(i + 1, n):
            diff = arr[j] - arr[i]
            length = 2
            prev_val = arr[j]
            for k in range(j + 1, n):
                if arr[k] - prev_val == diff:
                    length += 1
                    prev_val = arr[k]
            max_len = max(max_len, length)
    return max_len if max_len > c else -1

def main():
    t = int(input())
    for _ in range(t):
        n, c = map(int, input().split())
        arr = list(map(int, input().split()))
        result = solve(n, c, arr)
        print(result)

if __name__ == "__main__":
    main()