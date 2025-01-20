def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def farey_sequence_length(N):
    count = 0
    for b in range(1, N + 1):
        for a in range(b + 1):
            if gcd(a, b) == 1:
                count += 1
    return count + 1  # Adding the fraction 0/1

P = int(input())
for _ in range(P):
    K, N = map(int, input().split())
    length = farey_sequence_length(N)
    print(f"{K} {length}")