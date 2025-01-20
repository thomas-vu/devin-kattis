def extended_gcd(R, S):
    if R == 0:
        return (0, 1, S)
    else:
        x, y, gcd = extended_gcd(S % R, R)
        return (y - (S // R) * x, x, gcd)

def find_smallest_pair(R, S, Q):
    x, y, gcd = extended_gcd(R, S)
    if Q % gcd != 0:
        return "No solution"
    
    x *= Q // gcd
    y *= Q // gcd
    
    # Ensure A and B are positive
    while x <= 0:
        x += abs(S) // gcd
        y -= abs(R) // gcd
    
    while y <= 0:
        x -= abs(S) // gcd
        y += abs(R) // gcd
    
    return (x, y)

def main():
    T = int(input().strip())
    results = []
    for _ in range(T):
        R, S, Q = map(int, input().strip().split())
        A, B = find_smallest_pair(R, S, Q)
        results.append((A, B))
    
    for A, B in results:
        print(f"{A} {B}")

if __name__ == "__main__":
    main()