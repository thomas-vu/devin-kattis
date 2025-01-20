def count_pythagorean_triples(n):
    triples = set()
    for a in range(1, n):
        for b in range(a, n):
            c = (a**2 + b**2) % n
            if c < a:  # Ensure the condition a <= b and a^2 + b^2 == c^2
                triples.add((a, b, c))
    return len(triples) % n

n = int(input())
print(count_pythagorean_triples(n))