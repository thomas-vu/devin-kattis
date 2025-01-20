def min_cost(pa, ka, pb, kb, n):
    min_cost = float('inf')
    best_x, best_y = 0, 0
    
    # Check all possible number of trips for Car A (x) and Car B (y)
    for x in range(n // ka + 1):
        for y in range(n // kb + 1):
            if x * ka + y * kb >= n:
                cost = x * pa + y * pb
                if cost < min_cost:
                    min_cost = cost
                    best_x, best_y = x, y
    
    return best_x, best_y, min_cost

# Read input
pa, ka, pb, kb, n = map(int, input().split())
x, y, total_cost = min_cost(pa, ka, pb, kb, n)
print(x, y, total_cost)