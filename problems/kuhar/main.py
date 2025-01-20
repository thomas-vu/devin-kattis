def read_ints():
    return list(map(int, input().split()))

N, M = read_ints()
ingredients = []
for _ in range(N):
    data = read_ints()
    ingredients.append({
        'needed': data[0],
        'available': data[1],
        'small_size': data[2],
        'small_price': data[3],
        'large_size': data[4],
        'large_price': data[5]
    })

max_servings = 0
for i in range(1 << N):
    cost = 0
    servings = float('inf')
    for j in range(N):
        if i & (1 << j):
            needed = ingredients[j]['needed'] - ingredients[j]['available']
            if needed > 0:
                large_packages = min(needed // ingredients[j]['large_size'], (M - cost) // ingredients[j]['large_price'])
                needed -= large_packages * ingredients[j]['large_size']
                cost += large_packages * ingredients[j]['large_price']
                small_packages = min(needed // ingredients[j]['small_size'], (M - cost) // ingredients[j]['small_price'])
                needed -= small_packages * ingredients[j]['small_size']
                cost += small_packages * ingredients[j]['small_price']
            if needed > 0:
                break
        else:
            available = ingredients[j]['available']
            large_packages = min(ingredients[j]['needed'] // ingredients[j]['large_size'], (M - cost) // ingredients[j]['large_price'])
            available -= large_packages * ingredients[j]['large_size']
            cost += large_packages * ingredients[j]['large_price']
            small_packages = min(ingredients[j]['needed'] // ingredients[j]['small_size'], (M - cost) // ingredients[j]['small_price'])
            available -= small_packages * ingredients[j]['small_size']
            cost += small_packages * ingredients[j]['small_price']
            if available < 0:
                break
        servings = min(servings, ingredients[j]['needed'] // (ingredients[j]['available'] + needed))
    else:
        max_servings = max(max_servings, servings)

print(max_servings)