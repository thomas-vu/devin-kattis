def solve(s, p, y, j):
    # Spot's age + Puff's age = s + p
    # Puff's age + Yertle's age = p + y
    # Spot's age + Yertle's age = s + y
    # Sum of all ages = sum of Dick's and Jane's age = d + j
    
    # Spot's age + Puff's age + Yertle's age = d + j
    # Spot's age + Puff's age = s + p
    # Puff's age + Yertle's age = p + y
    # Spot's age + Yertle's age = s + y
    
    # Let's solve for Spot's, Puff's, and Yertle's ages
    # Spot's age = s + y - p
    # Puff's age = d + j - (s + y)
    # Yertle's age = d + j - (p + y)
    
    spot_age = s + y - p
    puff_age = d + j - (s + y)
    yertle_age = d + j - (p + y)
    
    return spot_age, puff_age, yertle_age

# Read input lines until EOF
while True:
    try:
        s, p, y, j = map(int, input().split())
        spot_age, puff_age, yertle_age = solve(s, p, y, j)
        print(spot_age, puff_age, yertle_age)
    except EOFError:
        break