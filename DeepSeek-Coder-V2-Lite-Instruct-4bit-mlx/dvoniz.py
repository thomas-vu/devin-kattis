def longest_interesting_subsequence(N, S, A):
    def is_interesting(start, end, k):
        return sum(A[start:start+k]) <= S and sum(A[end-k+1:end+1]) <= S

    def find_longest(start):
        left = start
        right = N - 1
        while left <= right:
            mid = (left + right) // 2
            if is_interesting(start, mid, (mid - start + 1) // 2):
                left = mid + 1
            else:
                right = mid - 1
        return right - start + 1

    result = []
    for i in range(N):
        if is_interesting(i, i + (N - i) // 2 * 2, (N - i) // 2):
            result.append(find_longest(i))
        else:
            result.append(0)
    return result

# Read input
N, S = map(int, input().split())
A = [int(input()) for _ in range(N)]

# Get the result and print it
result = longest_interesting_subsequence(N, S, A)
for length in result:
    print(length)