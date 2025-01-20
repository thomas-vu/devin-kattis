def median_of_three(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    return b

def generate_plan(n, k_list, a_list, b_list):
    plan = []
    for i in range(n):
        choices = [k_list[i], a_list[i], b_list[i]]
        choices.sort()
        plan.append(choices[1])  # Append the median of the three choices
    return plan

# Read input
n = int(input())
k_list = list(map(int, input().split()))
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

# Generate and output the plan
plan = generate_plan(n, k_list, a_list, b_list)
for distance in plan:
    print(distance, end=' ')