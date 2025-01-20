def min_anger(M, N, wishes):
    # Sort the children's wishes in ascending order
    wishes.sort()
    
    total_anger = 0
    excess_candies = M - sum(wishes[:N])
    
    for i in range(N):
        if wishes[i] <= excess_candies:
            continue
        else:
            total_anger += (wishes[i] - excess_candies) ** 2
    
    return total_anger

# Read input
M, N = map(int, input().split())
wishes = [int(input()) for _ in range(N)]

# Calculate and output the minimum sum of children's anger
print(min_anger(M, N, wishes))