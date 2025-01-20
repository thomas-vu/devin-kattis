def find_m_k(n):
    for m in range(1, int(n**0.5) + 1):
        if (n + m*m) % (2*m) == 0:
            k = (n - m*m) // (2*m)
            if k >= 0:
                return m, k
    return "impossible"

n = int(input().strip())
result = find_m_k(n)
if result == "impossible":
    print("impossible")
else:
    m, k = result
    print(m, k)