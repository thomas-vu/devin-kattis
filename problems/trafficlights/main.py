def min_time_to_green(n, lights):
    def time_until_next_green(r, g, current_time):
        while current_time >= r + g:
            current_time -= (r + g)
        if current_time < r:
            return r - current_time
        else:
            return 0

    min_cycle = float('inf')
    for r, g in lights:
        min_cycle = min(min_cycle, r + g)

    if min_cycle == 0:
        return -1

    total_time = 0
    for r, g in lights:
        if time_until_next_green(r, g, total_time) != 0:
            return -1
        total_time += time_until_next_green(r, g, total_time)

    return total_time

# Read input from stdin
n = int(input().strip())
lights = [tuple(map(int, input().strip().split())) for _ in range(n)]

# Calculate and print the result
print(min_time_to_green(n, lights))