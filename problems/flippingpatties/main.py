def min_cooks(orders):
    orders.sort(key=lambda x: x[1])  # Sort by pickup time
    end_times = []
    
    for d, t in orders:
        placed = False
        for i in range(len(end_times)):
            if end_times[i] + d <= t:  # If the current order can be served by this cook
                end_times[i] = t + d  # Update the end time of this cook
                placed = True
                break
        if not placed:  # If no cook can serve this order, add a new cook
            end_times.append(t + d)
    
    return len(end_times)

# Read input
n = int(input())
orders = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(min_cooks(orders))