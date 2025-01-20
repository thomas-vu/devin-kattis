F, B = map(int, input().split())
front_sprockets = list(map(int, input().split()))
back_sprockets = list(map(int, input().split()))

gears = []
for f in front_sprockets:
    for b in back_sprockets:
        gears.append((f, b))

gears.sort(key=lambda x: (x[0] / x[1], x[0]))

for gear in gears:
    print(f"({gear[0]},{gear[1]})")