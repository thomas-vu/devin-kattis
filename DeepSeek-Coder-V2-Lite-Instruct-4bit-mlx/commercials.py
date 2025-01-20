def max_profit(N, P, students):
    # Calculate the total gain if each commercial break is played optimally
    max_gain = 0
    for start in range(N):
        current_sum = 0
        min_students = float('inf')
        for end in range(start, N):
            current_sum += students[end]
            min_students = min(min_students, students[end])
            gain = (end - start + 1) * P - current_sum * min_students
            max_gain = max(max_gain, gain)
    return max_gain

# Read input
N, P = map(int, input().split())
students = list(map(int, input().split()))

# Calculate and print the result
result = max_profit(N, P, students)
print(result)