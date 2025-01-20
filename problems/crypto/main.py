import math

def count_trailing_zeros(n, base):
    count = 0
    while n % base == 0:
        n //= base
        count += 1
    return count

def find_strongest_key(n):
    min_base = 2
    max_zeros = 0
    strongest_key = 2
    
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            zeros = count_trailing_zeros(n, k)
            if zeros > max_zeros:
                max_zeros = zeros
                strongest_key = k
            elif zeros == max_zeros:
                min_base = min(min_base, k)
    
    if max_zeros == 0:
        return n
    
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            zeros = count_trailing_zeros(n, k)
            if zeros == max_zeros and k < min_base:
                min_base = k
    
    return min_base

n = int(input().strip())
print(find_strongest_key(n))