def can_concoct(recipe, used_ingredients):
    cauldron = set()
    for ingredient in recipe:
        if ingredient not in used_ingredients:
            return False
        cauldron.add(ingredient)
    return True

def main():
    N = int(input())
    recipes = []
    
    for _ in range(N):
        line = list(map(int, input().split()))
        M = line[0]
        recipe = line[1:]
        recipes.append(recipe)
    
    used_ingredients = set()
    concocted_count = 0
    
    for recipe in recipes:
        if can_concoct(recipe, used_ingredients):
            for ingredient in recipe:
                used_ingredients.add(ingredient)
            concocted_count += 1
    
    print(concocted_count)

if __name__ == "__main__":
    main()