def main():
    N = int(input())
    tea_prices = list(map(int, input().split()))
    M = int(input())
    topping_prices = list(map(int, input().split()))
    
    # Read the compatibility lists for each tea type
    compatibilities = []
    for _ in range(N):
        K, *toppings = map(int, input().split())
        compatibilities.append(set(toppings))
    
    X = int(input())
    
    # Calculate the minimum cost for each tea type with its compatible toppings
    min_costs = []
    for i in range(N):
        for j in compatibilities[i]:
            cost = tea_prices[i] + topping_prices[j - 1]
            min_costs.append(cost)
    
    # Sort the costs to find the maximum number of students PVH can invite
    min_costs.sort()
    
    # Buy the cheapest tea and toppings for each student until budget is exhausted
    count = 0
    while X >= min_costs[0]:
        X -= min_costs[count]
        count += 1
        if count == len(min_costs):
            break
    
    print(count)

if __name__ == "__main__":
    main()