P = int(input())

# Function to find the number of kids based on the fortune and digit constraints
def find_kids(P):
    results = []
    for kids in range(1, int(P**0.5) + 1):
        if P % kids == 0:
            amount_per_kid = P // kids
            if all(x in ['2', '4'] for x in str(kids)) and all(x in ['2', '4'] for x in str(amount_per_kid)):
                results.append(kids)
            if all(x in ['2', '4'] for x in str(kids)) and all(x in ['2', '4'] for x in str(amount_per_kid)) and kids != amount_per_kid:
                results.append(amount_per_kid)
    return sorted(results)

# Get the number of kids based on the fortune
kids_list = find_kids(P)

# Output the results
for kids in kids_list:
    print(kids)