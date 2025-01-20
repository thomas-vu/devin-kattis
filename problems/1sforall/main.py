def complexity(n):
    if n == 0:
        return 1
    min_complexity = float('inf')
    
    def find_min_complexity(num):
        if num <= 1:
            return len(str(num))
        
        min_ops = float('inf')
        for i in range(1, int(num**0.5)+1):
            if num % i == 0:
                min_ops = min(min_ops, find_min_complexity(i) + find_min_complexity(num // i))
        
        for ops in range(1, len(str(num))+1):
            left = int(str(num)[:ops])
            right = int(str(num)[ops:])
            min_ops = min(min_ops, find_min_complexity(left) + find_min_complexity(right))
        
        return min_ops + 1
    
    for ops in range(1, len(str(n))+1):
        left = int(str(n)[:ops])
        right = int(str(n)[ops:])
        min_complexity = min(min_complexity, find_min_complexity(left) + find_min_complexity(right))
    
    return min_complexity if min_complexity != float('inf') else len(str(n))

# Read input from stdin
import sys
for line in sys.stdin:
    n = int(line.strip())
    print(complexity(n))