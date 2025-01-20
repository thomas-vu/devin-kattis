A, B = map(int, input().split())
N = int(input())
floors = [int(input()) for _ in range(N)]

# Sort floors and remove duplicates
floors = sorted(set(floors))

# Initialize the total time to 0 seconds
total_time = 0

# Calculate the number of floors traveled
if A < B:
    for i in range(len(floors) - 1):
        total_time += abs(floors[i] - floors[i + 1]) * 4
    total_time += (B - A) * 4
else:
    for i in range(len(floors) - 1):
        total_time += abs(floors[i] - floors[i + 1]) * 4
    total_time += abs(A - B) * 4

# Add the time for door operations on each floor
total_time += N * 10

print(total_time)