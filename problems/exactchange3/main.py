def min_coins(a, b):
    # Convert the binary strings to integers
    a = int(a, 2)
    b = int(b, 2)
    
    # The minimum number of coins needed to cover any amount between a and b
    k = 0
    
    # Start from the smallest power of 2 that is at least a and go up to b
    i = 1
    while i <= b:
        if (i & a) == i:
            k += 1
        i <<= 1
    
    return k

# Read input from stdin
a = input().strip()
b = input().strip()

# Output the result
print(min_coins(a, b))