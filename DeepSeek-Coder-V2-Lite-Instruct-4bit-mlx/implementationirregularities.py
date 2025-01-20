import sys
from math import ceil

# Read input from stdin
n = int(input().strip())
t_values = list(map(int, input().strip().split()))
s_values = list(map(int, input().strip().split()))

# Initialize a list to keep track of the time each problem was solved
solved_time = [0] * n
for i in range(n):
    if s_values[i] != -1:
        solved_time[i] = s_values[i]

# Sort problems by the time they were solved
problems = sorted([(solved_time[i], t_values[i]) for i in range(n)])

# Calculate the minimum number of computers used
max_time = 0
computers = 1
for i in range(n):
    if problems[i][0] > max_time:
        max_time = problems[i][0] + problems[i][1]
    else:
        max_time += problems[i][1]
    if i < n - 1 and problems[i + 1][0] > max_time:
        computers += 1
        max_time = problems[i + 1][0] + problems[i + 1][1]

# Output the result
print(computers)