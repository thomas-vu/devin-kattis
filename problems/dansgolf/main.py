def min_lights_to_turn_on(N, M, K, dancing_tiles):
    # Create a grid to mark the tiles with dancers
    dancefloor = [[0] * M for _ in range(N)]
    
    # Mark the tiles with dancers on the dancefloor
    for x, y in dancing_tiles:
        dancefloor[x - 1][y - 1] = 1
    
    # Count the minimum number of lights needed to turn on
    count = 0
    
    # Check each tile with a dancer and decide if a light should be turned on
    for i in range(N):
        for j in range(M):
            if dancefloor[i][j] == 1:
                # Turn on the light at (i, j) and all other lights in its diagonal
                for x in range(N):
                    for y in range(M):
                        if (x - i == y - j) or (x - i == -(y - j)):
                            dancefloor[x][y] = 2
                count += 1
    
    return count

# Read input
N, M, K = map(int, input().split())
dancing_tiles = [tuple(map(int, input().split())) for _ in range(K)]

# Get the result and print it
result = min_lights_to_turn_on(N, M, K, dancing_tiles)
print(result)