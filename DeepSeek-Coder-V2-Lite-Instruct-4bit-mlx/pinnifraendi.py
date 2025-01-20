def calculate_probability(n):
    total_possible = 10**n
    successful_outcomes = 1
    
    # The PIN and the code must be exactly the same, so there's only 1 successful outcome
    probability = successful_outcomes / total_possible
    
    return "{:.12f}".format(probability)

n = int(input().strip())
print(calculate_probability(n))