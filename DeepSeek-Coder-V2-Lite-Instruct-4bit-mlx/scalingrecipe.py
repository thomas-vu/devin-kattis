n, x, y = map(int, input().split())
ingredients = [int(input()) for _ in range(n)]
scale_factor = y / x
for ingredient in ingredients:
    print(int(ingredient * scale_factor))