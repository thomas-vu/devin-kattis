def read_ints():
    return list(map(int, input().split()))

# Read inputs
A, B, E, P = read_ints()
precedence_rules = [tuple(read_ints()) for _ in range(P)]

# Create adjacency list for the precedence graph
adj_list = [[] for _ in range(E)]
for x, y in precedence_rules:
    adj_list[x].append(y)

# Topological sort to find the number of employees that can be possibly promoted for each promotion count
def possible_promotions(promotion_count):
    in_degree = [0] * E
    for x, y in precedence_rules:
        if promotion_count == 0:
            break
        for v in adj_list[y]:
            in_degree[v] += 1
    return sum(in_degree) == E - promotion_count

# Calculate the number of employees that will certainly be promoted and those with no possibility of being promoted for both A and B
certainly_promoted_A = 0
certainly_promoted_B = 0
no_possibility_B = 0
for promotions in range(1, B + 1):
    if possible_promotions(promotions - 1) and not possible_promotions(promotions):
        certainly_promoted_A = promotions
    if possible_promotions(promotions):
        certainly_promoted_B = promotions
    else:
        no_possibility_B = E - promotions

# Output the results
print(certainly_promoted_A)
print(certainly_promoted_B)
print(no_possibility_B)