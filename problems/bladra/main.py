def min_balloons(k, q):
    problem_count = [0] * (k + 1)
    
    for a, b in zip(a_i, b_i):
        problem_count[b] += 1
    
    max_count = max(problem_count)
    min_balloons = sum(1 for count in problem_count if count == max_count)
    
    return min_balloons

# Read input
k, q = map(int, input().split())
a_i = [0] * q
b_i = [0] * q
for i in range(q):
    a_i[i], b_i[i] = map(int, input().split())

# Calculate and print the result
print(min_balloons(k, q))