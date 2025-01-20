def min_cost(N, B, H, W, prices, beds):
    min_cost = float('inf')
    
    for i in range(H):
        price_per_person = prices[i]
        available_beds = beds[i]
        
        if price_per_person * N <= B:
            for beds_available in available_beds:
                if beds_available >= N:
                    min_cost = min(min_cost, price_per_person * N)
    
    return "stay home" if min_cost > B else min_cost

# Read input
N, B, H, W = map(int, input().split())
prices = []
beds = []

for _ in range(H):
    p = int(input())
    beds_available = list(map(int, input().split()))
    prices.append(p)
    beds.append(beds_available)

# Output the result
print(min_cost(N, B, H, W, prices, beds))