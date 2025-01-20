def min_sum_difficulty(N, A):
    A.sort()
    total_sum = 0
    for i in range(N // 2):
        total_sum += A[i] + A[N - i - 1]
    return total_sum

# Read input
N = int(input())
A = list(map(int, input().split()))

# Calculate and output the minimum sum of difficulty level to build the intercities highways
print(min_sum_difficulty(N, A))