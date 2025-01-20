def find_restaurant():
    n = int(input())
    restaurants = []
    
    for _ in range(n):
        k = int(input())
        menu = [input().strip() for _ in range(k + 1)]
        restaurant_name = menu[0]
        if "pea soup" in menu and "pancakes" in menu:
            restaurants.append(restaurant_name)
    
    if restaurants:
        return restaurants[0]
    else:
        return "Anywhere is fine I guess"

print(find_restaurant())