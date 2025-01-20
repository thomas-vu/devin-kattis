import math

def find_x(n):
    # Use the Lambert W function to solve for x in x^x = n
    if n <= 0:
        return None
    try:
        x = math.exp(math.log(n) / 2)
    except ValueError:
        return None
    
    # Newton's method to refine the approximation
    while True:
        prev_x = x
        x = x - (x**x - n) / (math.log(x) * x**x)
        if abs(x - prev_x) < 1e-6:
            break
    return x

n = int(input().strip())
x = find_x(n)
if x is not None:
    print("{:.10f}".format(x))
else:
    print("No solution found")