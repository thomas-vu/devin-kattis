import sys

def area(a, b, h):
    return ((a + b) * h) / 2

def cost(stones):
    back_porch, gazebo = map(int, sys.stdin.readline().split())
    min_cost = float('inf')
    
    for _ in range(n):
        a, b, h = map(int, sys.stdin.readline().split())
        stones.append((a, b, h))
    
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                a1, b1, h1 = stones[i]
                a2, b2, h2 = stones[j]
                a3, b3, h3 = stones[k]
                
                # Check if the paving stones can be joined correctly
                if (a1 == b2 and a2 == b3) or (a1 == b3 and a3 == b2):
                    total_area = area(a1, b2, h1) + area(a2, b3, h2)
                    cost = total_area * 0.02
                    min_cost = min(min_cost, cost)
    
    return min_cost

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    
    stones = []
    result = cost(stones)
    print("{:.2f}".format(result))