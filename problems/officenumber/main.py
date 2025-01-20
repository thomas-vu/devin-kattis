def count_ways(n):
    digits = [int(d) for d in str(n)]
    max_exponents = [0] * len(digits)
    
    def count_combinations(index, remaining):
        if index == len(digits):
            return 1 if remaining == 0 else 0
        
        count = 0
        for e in range(max_exponents[index] + 1):
            if remaining - (digits[index] ** e) >= 0:
                count += count_combinations(index + 1, remaining - (digits[index] ** e))
            else:
                break
        return count
    
    # Calculate the maximum possible exponents for each digit
    for i in range(len(digits)):
        max_exponents[i] = int(math.log(n, digits[i]))
    
    return count_combinations(0, n)

import math
n = int(input())
print(count_ways(n))