from math import gcd
from collections import defaultdict

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def solve(sequence):
    factors_count = defaultdict(int)
    
    # Count the frequency of each factor in the sequence
    for num in sequence:
        temp = num
        i = 2
        while i * i <= temp:
            if temp % i == 0:
                factors_count[i] += 1
                while temp % i == 0:
                    temp //= i
            i += 1
        if temp > 1:
            factors_count[temp] += 1
    
    # Find the maximum possible score and the number of operations needed
    max_score = 1
    ops_count = 0
    
    for num in sequence:
        temp = num
        i = 2
        operations_for_num = float('inf')
        while i * i <= temp:
            if temp % i == 0:
                min_operations = float('inf')
                for x in factors_count:
                    if num % x == 0:
                        min_operations = min(min_operations, factors_count[x])
                if min_operations != float('inf'):
                    operations = 0
                    while num % i == 0:
                        num //= i
                        operations += min_operations
                    while temp % i == 0:
                        temp //= i
                    operations_for_num = min(operations_for_num, operations)
            i += 1
        if temp > 1:
            for x in factors_count:
                if num % x == 0:
                    min_operations = float('inf')
                    while num % temp == 0:
                        num //= temp
                        min_operations = min(min_operations, factors_count[temp])
                    while temp % x == 0:
                        temp //= x
                    operations_for_num = min(operations_for_num, min_operations)
        
        if operations_for_num != float('inf'):
            while num % i == 0:
                num //= i
            while temp > 1:
                for x in factors_count:
                    if temp % x == 0:
                        while temp % x == 0:
                            temp //= x
                i += 1
            if num == 1:
                max_score = gcd(max_score, i)
            else:
                ops_count += operations_for_num
    
    return max_score, ops_count

# Read input
N = int(input())
sequence = list(map(int, input().split()))

# Solve the problem and print the result
max_score, ops_count = solve(sequence)
print(max_score, ops_count)