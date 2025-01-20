def min_moves_to_pair_socks(n, socks):
    # Count the number of each sock type
    sock_count = {}
    for sock in socks:
        if sock not in sock_count:
            sock_count[sock] = 0
        sock_count[sock] += 1
    
    # Check if it's possible to pair all socks
    for count in sock_count.values():
        if count % 2 != 0:
            return "impossible"
    
    # Calculate the minimum number of moves to pair socks
    moves = 0
    original_pile = list(range(1, n + 1))
    auxiliary_pile = []
    
    for i in range(2 * n):
        if socks[i] in original_pile:
            # Move the sock to the auxiliary pile
            auxiliary_pile.append(socks[i])
            original_pile.remove(socks[i])
        else:
            # Move the sock from auxiliary pile to original pile
            original_pile.append(auxiliary_pile.pop())
        # Pair the socks if possible
        while auxiliary_pile and original_pile:
            top_aux = auxiliary_pile[-1]
            top_orig = original_pile[-1]
            if top_aux == top_orig:
                auxiliary_pile.pop()
                original_pile.pop()
                moves += 2
            else:
                break
    
    return moves

# Read input
n = int(input())
socks = list(map(int, input().split()))

# Get the result and print it
result = min_moves_to_pair_socks(n, socks)
if result == "impossible":
    print("impossible")
else:
    print(result)