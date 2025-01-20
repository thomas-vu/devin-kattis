def min_moves(n, places):
    target = [i for i in range(1, n + 1)]
    moves = 0
    for i in range(n):
        if places[i] != target[i]:
            moves += 1
    return moves

# Read input
n = int(input())
places = list(map(int, input().split()))

# Calculate and output the result
print(min_moves(n, places))