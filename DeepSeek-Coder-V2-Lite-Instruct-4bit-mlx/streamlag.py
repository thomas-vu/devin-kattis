def calculate_total_lag(n, packets):
    current_time = 0
    total_lag = 0
    
    for i in range(n):
        arrival_time, packet_number = packets[i]
        if arrival_time > current_time:
            total_lag += (arrival_time - current_time) * (n - i)
            current_time = arrival_time
        else:
            total_lag += 0
    
    return total_lag

# Read input
n = int(input())
packets = [tuple(map(int, input().split())) for _ in range(n)]

# Calculate and output the total lag
total_lag = calculate_total_lag(n, packets)
print(total_lag)