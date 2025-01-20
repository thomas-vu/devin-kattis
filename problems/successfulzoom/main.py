def find_smallest_k(n, numbers):
    for k in range(1, n + 1):
        q = n // k
        is_increasing = True
        for i in range(1, q):
            if numbers[i * k - 1] >= numbers[(i + 1) * k - 1]:
                is_increasing = False
                break
        if is_increasing:
            return k
    return "ABORT!"

# Read input
n = int(input())
numbers = list(map(int, input().split()))

# Output the result
print(find_smallest_k(n, numbers))