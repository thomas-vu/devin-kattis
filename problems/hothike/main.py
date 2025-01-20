def find_best_trip_days(n, temperatures):
    min_max_temp = float('inf')
    best_start_day = 0
    
    for start in range(n - 2):
        end = start + 2
        max_temp_during_trip = max(temperatures[start:end])
        
        if max_temp_during_trip < min_max_temp:
            min_max_temp = max_temp_during_trip
            best_start_day = start + 1
    
    return best_start_day, min_max_temp

# Read input
n = int(input())
temperatures = list(map(int, input().split()))

# Find and output the best trip days
best_start_day, min_max_temp = find_best_trip_days(n, temperatures)
print(best_start_day + 1, min_max_temp)