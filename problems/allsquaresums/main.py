def find_squares(n):
    solutions = set()
    limit = int(n ** 0.5) + 1
    
    for x in range(-limit, limit + 1):
        y_squared = n - x**2
        if y_squared >= 0:
            y = int(y_squared**0.5)
            if x**2 + y**2 == n:
                solutions.add((x, y))
    
    return solutions

n = int(input().strip())
solutions = find_squares(n)
print(len(solutions))
for x, y in solutions:
    if x < 0 and y >= 0:
        print(f"({x})^2 + {y}^2 = {n}")
    elif x >= 0 and y < 0:
        print(f"{x}^2 + ({y})^2 = {n}")
    elif x < 0 and y < 0:
        print(f"({x})^2 + ({y})^2 = {n}")
    else:
        print(f"{x}^2 + {y}^2 = {n}")