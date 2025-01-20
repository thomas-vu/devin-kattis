def can_yraglac_make_it_on_time(s, t, n, d, b, c):
    current_time = s
    for i in range(n):
        current_time += d[i]  # Walking time to the bus stop
        next_bus = current_time // c[i] * c[i]  # Time of the next bus
        current_time = max(next_bus, b[i]) + d[i]  # Time to board the bus and walk to the next stop
    current_time += d[n]  # Walking time from the last bus to class
    return "yes" if current_time <= t else "no"

# Read input
s, t, n = map(int, input().split())
d = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

# Output the result
print(can_yraglac_make_it_on_time(s, t, n, d, b, c))