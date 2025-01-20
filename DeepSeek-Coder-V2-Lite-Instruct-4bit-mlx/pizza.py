def min_delivery_cost(deliveries):
    x, y = len(deliveries[0]), len(deliveries)
    total_costs = []
    
    for i in range(y):
        for j in range(x):
            if deliveries[i][j] > 0:
                costs = []
                for k in range(y):
                    for l in range(x):
                        if deliveries[k][l] > 0:
                            cost = abs(i - k) + abs(j - l) * deliveries[k][l]
                            costs.append(cost)
                total_costs.append(sum(costs))
    
    return min(total_costs) if total_costs else 0

def main():
    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split())
        deliveries = [list(map(int, input().split())) for _ in range(y)]
        result = min_delivery_cost(deliveries)
        print(f"{result} blocks")

if __name__ == "__main__":
    main()