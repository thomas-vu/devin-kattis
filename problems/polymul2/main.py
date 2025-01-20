T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    
    # Perform polynomial multiplication
    result_degree = n + m
    result = [0] * (result_degree + 1)
    
    for i in range(n + 1):
        for j in range(m + 1):
            result[i + j] += a[i] * b[j]
    
    # Output the result
    print(result_degree)
    print(' '.join(map(str, result)))