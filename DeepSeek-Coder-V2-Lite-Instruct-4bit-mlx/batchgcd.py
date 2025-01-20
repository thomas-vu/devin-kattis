Here's the solution to the problem in Python 3:
```python
import math
from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def batch_gcd(numbers):
    if len(numbers) == 1:
        return "NO" if math.gcd(*numbers) == 1 else "YES"
    
    half = len(numbers) // 2
    left_gcd = batch_gcd(numbers[:half])
    right_gcd = batch_gcd(numbers[half:])
    
    if left_gcd == "YES" or right_gcd == "YES":
        return "YES"
    
    left_numbers = [numbers[i] for i in range(half)]
    right_numbers = [numbers[i + half] for i in range(len(numbers) - half)]
    
    left_prod = reduce(lambda x, y: x * y, left_numbers, 1)
    right_prod = reduce(lambda x, y: x * y, right_numbers, 1)
    
    if gcd(left_prod, right_prod) > 1:
        return "YES"
    else:
        return "NO"

# Read input
n = int(input())
numbers = list(map(int, input().split()))

# Output the result
print("YES" if batch_gcd(numbers) == "YES" else "NO")