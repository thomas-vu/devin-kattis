def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for t in range(T):
        R = int(data[index])
        P = int(data[index + 1])
        D = int(data[index + 2])
        index += 3
        
        ingredients = []
        for r in range(R):
            name = data[index]
            weight = float(data[index + 1])
            percentage = float(data[index + 2])
            ingredients.append((name, weight, percentage))
            index += 3
        
        scaling_factor = D / P
        main_ingredient = next((ing for ing in ingredients if ing[2] == 100.0), None)
        main_weight = main_ingredient[1] * scaling_factor
        
        scaled_ingredients = []
        for ing in ingredients:
            if ing[2] == 100.0:
                continue
            scaled_weight = ing[1] * scaling_factor / 100.0
            scaled_ingredients.append((ing[0], scaled_weight))
        
        results.append(f"Recipe # {t + 1}")
        for name, weight in scaled_ingredients:
            results.append(f"{name} {weight:.1f}")
        results.append("-" * 40)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()