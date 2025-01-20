# Read the inputs
b, n, e = map(int, input().split())
sb, sn, se = map(int, input().split())
c_values = list(map(int, input().split()))

# Sort the kayaks by speed factor in descending order
c_values.sort(reverse=True)

# Initialize the strength arrays for beginners, normal participants, and experienced kayakers
beginners = [sb] * b
normals = [sn] * n
experienced = [se] * e

# Merge the strengths of all participants into one list and sort it in ascending order
strengths = sorted(beginners + normals + experienced)

# Initialize the maximum speed to a very low value
max_speed = -1

# Iterate through all possible distributions of participants in the kayaks
for i in range(len(c_values) + 1):
    for j in range(i, len(c_values) + 1):
        # Calculate the speed for the current distribution of participants in the kayaks
        if i + j == len(strengths):
            left_over = strengths[j:]
            min_speed = float('inf')
            for k in range(0, len(left_over), 2):
                if k + 1 < len(left_over):
                    min_speed = min(min_speed, c_values[i + j - 1] * (left_over[k] + left_over[k + 1]))
                else:
                    min_speed = min(min_speed, c_values[i + j - 1] * (left_over[k] + left_over[k]))
            max_speed = max(max_speed, min_speed)

# Output the maximum speed
print(max_speed)