def calculate_problems(A_uniq, A_reuse, B_uniq, B_reuse):
    total_problems = (A_uniq + A_reuse) * (B_uniq + B_reuse)
    return total_problems

# Read input
A_uniq, A_reuse, B_uniq, B_reuse = map(int, input().split())

# Calculate and print the result
result = calculate_problems(A_uniq, A_reuse, B_uniq, B_reuse)
print(result)