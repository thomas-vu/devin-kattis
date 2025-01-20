import math
from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def operate_list(numbers, op):
    if op == 'gcd':
        return [reduce(gcd, numbers)]
    elif op == 'lcm':
        return [reduce(lcm, numbers)]

def solve(numbers):
    N = len(numbers)
    results = []
    
    for i in range(N):
        max_outcome = numbers[0]
        min_outcome = numbers[0]
        
        for j in range(N):
            if i != j:
                temp_numbers = numbers[:]
                temp_numbers[i], temp_numbers[j] = operate(temp_numbers[i], temp_numbers[j], 'gcd' if i < j else 'lcm')
                max_outcome = max(max_outcome, temp_numbers[i])
                min_outcome = min(min_outcome, temp_numbers[i])
        
        results.append((max_outcome, min_outcome))
    
    return results

def operate(x, y, op):
    if op == 'gcd':
        return gcd(x, y)
    elif op == 'lcm':
        return lcm(x, y)

# Main function to read input and output results
def main():
    N = int(input())
    numbers = [tuple(map(int, input().split())) for _ in range(N)]
    
    results = solve(numbers)
    
    for result in results:
        print(*result[0])
        print(*result[1])

if __name__ == "__main__":
    main()