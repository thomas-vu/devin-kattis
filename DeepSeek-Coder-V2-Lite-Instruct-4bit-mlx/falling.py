def find_frames(D):
    for n1 in range(int(D**0.5) + 1):
        n2_squared = n1*n1 + D
        n2 = int(n2_squared**0.5)
        if n2*n2 == n2_squared:
            return (n1, n2)
    return "impossible"

# Read input
D = int(input().strip())
result = find_frames(D)
if result == "impossible":
    print("impossible")
else:
    n1, n2 = result
    print(n1, n2)