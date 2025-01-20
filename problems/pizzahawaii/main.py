def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        pizza_names = []
        foreign_ingredients = {}
        native_ingredients = {}
        
        for _ in range(n):
            name = input()
            m = int(input())
            ingredients = input().split()
            pizza_names.append(name)
            foreign_ingredients[name] = ingredients
            native_ingredients[name] = input().split()
        
        all_pairs = set()
        for i in range(len(pizza_names)):
            for j in range(i + 1, len(pizza_names)):
                common_ingredients = set(foreign_ingredients[pizza_names[i]]).intersection(foreign_ingredients[pizza_names[j]])
                for ingredient1 in common_ingredients:
                    for ingredient2 in common_ingredients:
                        if ingredient1 != ingredient2:
                            all_pairs.add((min(ingredient1, ingredient2), max(ingredient1, ingredient2)))
        
        for pair in sorted(all_pairs):
            print("({}, {})".format(*pair), end=' ')
        print()