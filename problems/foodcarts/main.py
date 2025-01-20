MOD = 10**9 + 7

def count_happy_passengers(n, m, k, passengers, food_carts):
    # Sort the food carts by their range start positions
    food_carts.sort(key=lambda x: (x[0], -x[1]))
    
    # Initialize the number of happy passengers for each car when no food cart is in service
    happy_passengers = [0] * n
    
    # Calculate the number of passengers in cars that can be happy with each food cart in service
    for start, end in food_carts:
        temp = 0
        for i in range(start - 1, end):
            happy_passengers[i] += passengers[i]
    
    # Check if each passenger is happy with at least k food carts in service
    def count_ways(threshold):
        ways = 0
        for i in range(n):
            if happy_passengers[i] >= threshold:
                ways += 1
        return ways
    
    # Binary search to find the number of happy passengers required for k food carts in service
    left, right = 0, sum(passengers) + 1
    while left < right:
        mid = (left + right) // 2
        if count_ways(mid) >= k:
            left = mid + 1
        else:
            right = mid
    
    # Calculate the number of ways to achieve exactly k happy passengers
    threshold = left - 1
    ways = 1
    current_happy = [0] * n
    
    # Use bit manipulation to count the number of ways with food carts in service
    for mask in range(1, 1 << m):
        count = 0
        for i in range(m):
            if mask & (1 << i):
                count += 1
                for j in range(food_carts[i][0] - 1, food_carts[i][1]):
                    current_happy[j] += 1
        if count == count_ways(threshold):
            ways = (ways + 1) % MOD
        for i in range(food_carts[i][0] - 1, food_carts[i][1]):
            current_happy[j] -= 1
    
    return ways

# Read input
n, m, k = map(int, input().split())
passengers = list(map(int, input().split()))
food_carts = [tuple(map(int, input().split())) for _ in range(m)]

# Output the result
print(count_happy_passengers(n, m, k, passengers, food_carts))