n = int(input())
coins = list(map(int, input().split()))
moves = []

# Check if the total number of coins is even
if sum(coins) % 2 != 0:
    print("no")
else:
    # Try to pair coins from different stacks
    for i in range(n):
        for j in range(i + 1, n):
            if coins[i] > 0 and coins[j] > 0:
                moves.append((i + 1, j + 1))
                coins[i] -= 1
                coins[j] -= 1
    # Check if all coins are removed
    if sum(coins) == 0:
        print("yes")
        for move in moves:
            print(move[0], move[1])
    else:
        print("no")