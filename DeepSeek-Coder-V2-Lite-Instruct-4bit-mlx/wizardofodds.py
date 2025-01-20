def can_guarantee_win(N, K):
    if K == 0:
        return "You will become a flying monkey!"
    elif K >= int(N).bit_length():
        return "Your wish is granted!"
    else:
        return "You will become a flying monkey!"

# Read input
N, K = map(int, input().split())

# Output the result
print(can_guarantee_win(N, K))