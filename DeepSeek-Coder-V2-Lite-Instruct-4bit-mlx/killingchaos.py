def calculate_chaos(n, passengers, order):
    chaos = 0
    for i in range(n):
        segment_chaos = (passengers[i] + 9) // 10 * 10
        chaos += segment_chaos
    max_chaos = 0
    current_chaos = 0
    for coach in order:
        current_chaos += (passengers[coach - 1] + 9) // 10 * 10
        max_chaos = max(max_chaos, current_chaos)
    return max_chaos

# Read input
n = int(input())
passengers = list(map(int, input().split()))
order = list(map(int, input().split()))

# Calculate and print the result
print(calculate_chaos(n, passengers, order))