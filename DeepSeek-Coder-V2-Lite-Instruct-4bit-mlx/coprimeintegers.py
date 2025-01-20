from math import gcd

def count_coprime_pairs(a, b, c, d):
    def is_coprime(x, y):
        return gcd(x, y) == 1
    
    count = 0
    for x in range(a, b + 1):
        for y in range(c, d + 1):
            if is_coprime(x, y):
                count += 1
    return count

# Read input
a, b, c, d = map(int, input().split())
# Output the result
print(count_coprime_pairs(a, b, c, d))