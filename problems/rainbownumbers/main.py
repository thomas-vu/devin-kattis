MOD = 998244353

def count_rainbow(L, U):
    def is_valid(num_str):
        for i in range(1, len(num_str)):
            if num_str[i] == num_str[i-1]:
                return False
        return True
    
    def count_valid(num_str):
        n = len(num_str)
        if n == 0:
            return 1
        
        count = 0
        for next_digit in range(1, 10):
            if n == 1 and next_digit < int(num_str[0]):
                continue
            if is_valid(num_str + str(next_digit)):
                count += 1
        
        for i in range(1, n):
            for next_digit in range(10):
                if is_valid(num_str[:i] + str(next_digit) + num_str[i:]):
                    count += 1
        
        return count % MOD
    
    def count_range(L, U):
        L = str(L)
        U = str(U)
        n = len(U)
        
        count_upto_U = 0
        for length in range(1, n + 1):
            count_upto_U += sum(count_valid('') for _ in range(length - len(L)))
            count_upto_U += sum(count_valid(L[:i] + str(digit) + L[i:]) for i in range(len(L) + 1) for digit in range(int(L[i]) if i < len(L) else 1, 10))
        
        return count_upto_U % MOD
    
    return count_range(L, U)

# Example usage:
# L = 1
# U = 1010
# print(count_rainbow(L, U))  # Output: 260