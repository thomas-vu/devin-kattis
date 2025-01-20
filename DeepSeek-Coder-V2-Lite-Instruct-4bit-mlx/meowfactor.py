import math

def meow_factor(n):
    def count_divisions(number, divisor):
        count = 0
        while number % divisor == 0:
            number //= divisor
            count += 1
        return count
    
    meow = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count = count_divisions(n, i)
            if count == 9:
                meow = max(meow, i)
    
    if meow == 1:
        for i in range(int(math.sqrt(n)), 0, -1):
            if n % i == 0:
                count = count_divisions(n, i)
                if count == 9:
                    meow = max(meow, i)
    
    return meow

# Read input
n = int(input().strip())

# Output the meow factor
print(meow_factor(n))