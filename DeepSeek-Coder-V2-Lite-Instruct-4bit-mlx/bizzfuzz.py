def count_divisible(A, B, C, D):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    def lcm(a, b):
        return a * b // gcd(a, b)
    
    lcm_CD = lcm(C, D)
    count = B // C - (A - 1) // C
    count += B // D - (A - 1) // D
    count -= B // lcm_CD - (A - 1) // lcm_CD
    return count

# Read input from stdin
A, B, C, D = map(int, input().split())
# Output the result
print(count_divisible(A, B, C, D))