def count_divisible_binomial(N, K):
    # Initialize Pascal's triangle
    pascal = [[1] * (i + 1) for i in range(N + 1)]
    
    # Fill Pascal's triangle using the given recursion
    for i in range(2, N + 1):
        for j in range(1, i):
            pascal[i][j] = pascal[i - 1][j] + pascal[i - 1][j - 1]
    
    # Count the number of multiples of K in Pascal's triangle
    count = 0
    for i in range(N + 1):
        for j in range(i + 1):
            if pascal[i][j] % K == 0:
                count += 1
    return count

# Read input
N, K = map(int, input().split())

# Compute and print the result
print(count_divisible_binomial(N, K))