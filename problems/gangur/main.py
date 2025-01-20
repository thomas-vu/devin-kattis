def count_passes(hallway):
    passes = 0
    for i in range(len(hallway) - 1):
        if hallway[i] == '>' and hallway[i + 1] == '<':
            passes += 1
    return passes

# Read input from the user
hallway = input().strip()
print(count_passes(hallway))