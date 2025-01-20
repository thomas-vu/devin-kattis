def calculate_upvotes_and_downvotes(N, x, y):
    total_users = sum(y)
    if total_users > sum(x):
        return 0  # Not enough parking slots to accommodate all users
    
    upvotes = 0
    downvotes = 0
    for i in range(N):
        if y[i] > x[i]:  # Tier has more users than slots
            upvotes += min(y[i], x[i])  # Assign users to available slots
        elif y[i] < x[i]:  # Tier has more slots than users
            downvotes += y[i]  # Assign all users to this tier's slots
        else:  # Tier has equal number of slots and users
            upvotes += y[i]  # All users can be satisfied
    
    return upvotes - downvotes

# Read input
N = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

# Calculate and output the result
result = calculate_upvotes_and_downvotes(N, x, y)
print(result)