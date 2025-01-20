import math

def get_permutation(n, k):
    numbers = list(range(1, n + 1))
    permutation = ''
    k -= 1  # Adjust for zero-based indexing
    
    while n > 0:
        n -= 1
        index = k // math.factorial(n)
        permutation += str(numbers[index])
        numbers.pop(index)
        k %= math.factorial(n)
    
    return permutation

while True:
    try:
        n, k = map(int, input().split())
        print(get_permutation(n, k))
    except EOFError:
        break