def can_complete_wall(h, w, n, bricks):
    # Sort the bricks in descending order to try to fit them first into the widest layers
    bricks.sort(reverse=True)
    
    # Initialize a list to keep track of the current width used in each layer
    layers = [0] * h
    
    for brick in bricks:
        # Find the first layer where the brick can fit
        placed = False
        for i in range(h):
            if layers[i] + brick <= w:
                layers[i] += brick
                placed = True
                break
        # If the brick cannot be placed in any layer, return NO
        if not placed:
            return "NO"
    # If all layers are completely filled, return YES
    return "YES"

# Read input
h, w, n = map(int, input().split())
bricks = list(map(int, input().split()))

# Check if the wall can be completed
result = can_complete_wall(h, w, n, bricks)
print(result)