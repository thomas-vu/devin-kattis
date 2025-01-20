import math

# Read input from stdin
g = input().strip()
k = input().strip()
p = float(input().strip())

# Calculate the probability of each character in g and k appearing in s before the game ends
def calculate_probability(g, k, p):
    n = len(g)
    m = len(k)
    
    # Probability that g appears in s before the game ends
    pg = 0.0
    for i in range(n):
        if g[i] == 'H':
            pg += (1 - p) ** i
        else:
            pg += (p) ** i
    
    # Probability that k appears in s before the game ends
    pk = 0.0
    for i in range(m):
        if k[i] == 'H':
            pk += (1 - p) ** i
        else:
            pk += (p) ** i
    
    # Probability that both g and k appear in s before the game ends
    pgk = 0.0
    for i in range(max(n, m)):
        if i < n and g[i] == 'H':
            pgk += (1 - p) ** i
        if i < m and k[i] == 'H':
            pgk += (1 - p) ** i
    
    # Calculate the probability that Gon wins
    return (pg - pgk) / (1 - pgk) if 1 - pgk != 0 else 0.0

# Output the result with appropriate precision
print("{:.15f}".format(calculate_probability(g, k, p)))