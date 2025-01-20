def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_cycle(positions):
    n = len(positions)
    min_period = float('inf')
    min_letter = ''
    
    for i in range(n):
        pi, letters = positions[i]
        for j in range(i + 1, n):
            pj, letters_j = positions[j]
            if letters != letters_j:
                continue
            period = pj - pi
            for k in range(i + 1, j):
                pk, letters_k = positions[k]
                if letters != letters_k:
                    continue
                period_candidate = pk - pi
                if gcd(period, period_candidate) != 1:
                    period = lcm(period, period_candidate)
            if period < min_period:
                min_period = period
                min_letter = letters[0]
            elif period == min_period and pi < positions[positions.index(min_letter)][0]:
                min_period = period
                min_letter = letters[0]
    return min_letter, min_period

def lcm(a, b):
    return a * b // gcd(a, b)

N = int(input())
positions = []
for _ in range(N):
    pi, letters = input().split()
    positions.append((int(pi), letters))

letter, _ = find_cycle(positions)
print(letter)