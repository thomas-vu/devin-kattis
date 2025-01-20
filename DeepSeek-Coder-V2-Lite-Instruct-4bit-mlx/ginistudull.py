def gini_coefficient(incomes):
    n = len(incomes)
    total_sum = sum(incomes)
    numerator = 0.0
    
    for i in range(n):
        for j in range(n):
            numerator += abs(incomes[i] - incomes[j])
    
    gini = numerator / (2 * total_sum * n)
    return gini

# Read input
n = int(input())
incomes = [int(input()) for _ in range(n)]

# Calculate and print the Gini coefficient
gini_index = gini_coefficient(incomes)
print("{:.15f}".format(gini_index))