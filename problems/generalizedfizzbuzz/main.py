def fizz_buzz(n, a, b):
    fizz = 0
    buzz = 0
    fizzbuzz = 0
    
    for i in range(1, n + 1):
        if i % a == 0 and i % b == 0:
            fizzbuzz += 1
        elif i % a == 0:
            fizz += 1
        elif i % b == 0:
            buzz += 1
    
    return fizz, buzz, fizzbuzz

# Read input
n, a, b = map(int, input().split())

# Get the results
fizz, buzz, fizzbuzz = fizz_buzz(n, a, b)

# Print the output
print(fizz, buzz, fizzbuzz)