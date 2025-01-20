import math

def T2(n):
    count = 0
    for m in range(n):
        for k in range(m + 1):
            if math.factorial(m) % (math.factorial(k) * math.factorial(m - k)) == 0:
                count += 1
    return count

# Example usage:
n = int(input())
print(T2(n))