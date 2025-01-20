def max_revenue(k, r, ingredients, recipes):
    max_rev = 0
    for price, recipe in recipes:
        can_make = float('inf')
        for i in range(k):
            if recipe[i] != 0:
                can_make = min(can_make, ingredients[i] // recipe[i])
        rev = can_make * price
        max_rev = max(max_rev, rev)
    return max_rev

# Read input
k, r = map(int, input().split())
ingredients = list(map(int, input().split()))
recipes = [list(map(int, input().split())) for _ in range(r)]

# Process and output the result
print(max_revenue(k, r, ingredients, recipes))