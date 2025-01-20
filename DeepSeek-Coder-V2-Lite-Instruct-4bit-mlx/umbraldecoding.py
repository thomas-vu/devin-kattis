def count_points(n, k, safe_points):
    umbra_count = set()
    
    for x, y, b in safe_points:
        for p in range(max(0, x - int((b + abs(y-x)**3)**(1/3)), min(n, x + int((b + abs(y-x)**3)**(1/3)))):
            for q in range(max(0, y - int((b + abs(x-y)**3)**(1/3)), min(n, y + int((b + abs(x-y)**3)**(1/3)))):
                if (p, q) not in umbra_count:
                    umbra_count.add((p, q))
    
    return n**2 - len(umbra_count)

# Read input
n, k = map(int, input().split())
safe_points = [tuple(map(int, input().split())) for _ in range(k)]

# Calculate and output the result
result = count_points(n, k, safe_points)
print(result)