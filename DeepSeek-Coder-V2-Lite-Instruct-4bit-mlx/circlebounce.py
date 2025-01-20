MOD = 1000000007

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def bounce_point(a, b, n):
    # Initial position and direction
    x, y = -1, 0
    dx, dy = a, b
    
    for _ in range(n):
        # Reflect the direction after hitting the wall
        if x * dx + y * dy < 0:
            # Reflect off the wall with slope -dx/dy
            dx, dy = -dx, -dy
        elif x * dx + y * dy > 0:
            # Reflect off the wall with slope -dx/dy
            dx, dy = -dx, -dy
        else:
            # Reflect off the wall with slope dx/dy
            dx, dy = dx, dy
        
        # Update the position
        x += dx
        y += dy
    
    return (x, y)

def main():
    a, b, n = map(int, input().split())
    
    # Get the final position after n bounces
    x, y = bounce_point(a, b, n)
    
    # Normalize the position to rational coordinates
    r = x
    s = y
    
    # Calculate the modular inverse of s with respect to MOD
    sinv = modinv(s, MOD)
    
    # Calculate the result
    result = (r * sinv) % MOD
    
    print(result)

if __name__ == "__main__":
    main()