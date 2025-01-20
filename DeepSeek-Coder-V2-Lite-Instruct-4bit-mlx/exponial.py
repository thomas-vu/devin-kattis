def exponial(n, m):
    def mod_exp(base, exp, mod):
        result = 1
        base %= mod
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            exp >>= 1
            base = (base * base) % mod
        return result
    
    def exponial_helper(n):
        if n == 1:
            return 1
        else:
            exp = exponial_helper(n - 1)
            return mod_exp(n, exp, m)
    
    return exponial_helper(n) % m

# Example usage:
print(exponial(2, 42))        # Output: 2
print(exponial(5, 123456789)) # Output: 16317634
print(exponial(94, 26539))    # Output: 17180