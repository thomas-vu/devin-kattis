def can_move_pile(N, M, K):
    # A pile of size K can be moved if:
    # 1. There are exactly K free cells available to hold the cards temporarily.
    # 2. There are enough empty stacks to place the cards one by one as they are moved from the source stack.
    # 3. The number of free cells and empty stacks combined is at least K, because we need to account for the temporary holding in free cells and empty stacks.
    return K <= N + M

# Read input from stdin
while True:
    try:
        N, M, K = map(int, input().split())
        print("yes" if can_move_pile(N, M, K) else "no")
    except EOFError:
        break