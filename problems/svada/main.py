T = int(input())
N = int(input())
A_k = [tuple(map(int, input().split())) for _ in range(N)]
M = int(input())
C_k = [tuple(map(int, input().split())) for _ in range(M)]

# Calculate the total coconuts picked by each monkey of the first type
total_coconuts_picked = sum((T // B - 1) for _, B in A_k)
# Calculate the total coconuts opened by each monkey of the second type
total_coconuts_opened = sum((T // D - 1) for _, D in C_k)

# The time when the first type of monkeys arrives is 0 seconds
first_arrival = 0
# The time when the second type of monkeys arrives is when all coconuts are opened
second_arrival = total_coconuts_opened * min(D for _, D in C_k)

# Output the number of seconds between the arrival of the first type and the second type
print(second_arrival - first_arrival)