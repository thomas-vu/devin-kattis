def mod_base_b(b, p, m):
    # Convert base-10 numbers to base-b integers
    b_p = int(p, b)
    b_m = int(m, b)
    
    # Compute the remainder using Python's built-in division and modulo operations
    result = b_p % b_m
    
    # Convert the result back to base-b string representation
    return format(result, f'0{len(p)}b') if len(format(result, f'0{len(p)}b')) == len(p) else format(result, 'b')

# Read input until a line with 0 is encountered
while True:
    b, p, m = input().split()
    if b == '0':
        break
    print(mod_base_b(int(b), p, int(m)))