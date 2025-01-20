def find_encryption_key(a, b):
    a_str = str(a)
    b_str = str(b)
    n = len(a_str)
    
    exponents = []
    for i in range(n):
        digit_a = int(a_str[i])
        for exp in range(2, 10):  # Check possible exponents from 2 to 9
            if digit_a**exp == int(b_str[i]):
                exponents.append(exp)
                break
    
    return ' '.join(map(str, exponents))

# Read input
a, b = map(int, input().split())

# Output the encryption key
print(find_encryption_key(a, b))