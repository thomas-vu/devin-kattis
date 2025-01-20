def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    u, k = map(int, data[0].split())
    recipes = {}
    for i in range(1, u + 1):
        dish_name = data[i]
        h = int(data[i + u])
        ingredients = {}
        for j in range(i + 1, i + h + 1):
            ingredient_name, quantity = data[j].split()
            ingredients[ingredient_name] = int(quantity)
        recipes[dish_name] = ingredients
    
    receipts = {}
    for i in range(u + u + 1, len(data), 2):
        n = int(data[i])
        for j in range(i + 1, i + n + 1):
            dish_name, quantity = data[j].split()
            if dish_name in receipts:
                receipts[dish_name] += int(quantity)
            else:
                receipts[dish_name] = int(quantity)
    
    needed_ingredients = {}
    for dish, quantity in receipts.items():
        for ingredient, amount in recipes[dish].items():
            if ingredient in needed_ingredients:
                needed_ingredients[ingredient] += amount * quantity
            else:
                needed_ingredients[ingredient] = amount * quantity
    
    for ingredient, amount in sorted(needed_ingredients.items(), key=lambda x: (x[0].lower())):
        print(f"{ingredient} {amount}")

if __name__ == "__main__":
    main()