N = int(input())
ingredients = []
for _ in range(N):
    I, P = input().split()
    P = int(P) if P != '?' else '?'
    ingredients.append((I, P))

L = [0] * N
H = [0] * N

# Determine the possible ranges for each ingredient
for i in range(N):
    if ingredients[i][1] != '?':
        L[i] = H[i] = ingredients[i][1] / (sum(ingredients[j][1] for j in range(N) if ingredients[j][1] != '?') if sum(ingredients[j][1] for j in range(N) if ingredients[j][1] != '?') > 0 else 1)
    else:
        total_known = sum(ingredients[j][1] for j in range(N) if ingredients[j][1] != '?')
        total_unknown = N - sum(ingredients[j][1] != '?' for j in range(N))
        if total_unknown == 0:
            L[i] = H[i] = ingredients[i][1] / (sum(ingredients[j][1] for j in range(N) if ingredients[j][1] != '?') if sum(ingredients[j][1] for j in range(N) if ingredients[j][1] != '?') > 0 else 1)
        elif total_known == 0:
            L[i] = H[i] = 0
        else:
            min_total = (sum(ingredients[j][1] for j in range(N) if ingredients[j][1] != '?') + total_unknown - 1) / (total_unknown if total_unknown > 0 else 1)
            max_total = (sum(ingredients[j][1] for j in range(N) if ingredients[j][1] != '?') + total_unknown - 1) / (total_unknown if total_unknown > 0 else 1)
            L[i] = min_total * (ingredients[i][1] / 100)
            H[i] = max_total * (ingredients[i][1] / 100)

# Output the results
for i in range(N):
    print(ingredients[i][0], int(L[i]), int(H[i]))