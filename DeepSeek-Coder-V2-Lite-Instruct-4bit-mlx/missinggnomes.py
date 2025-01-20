def find_original_sequence(n, m, subsequence):
    # Create a list to simulate the original sequence of gnomes
    original_sequence = [0] * n
    
    # Create a list to mark the positions of the remaining gnomes
    position_map = [0] * (n + 1)
    
    # Populate the position map with the positions of the remaining gnomes
    for i, gnome in enumerate(subsequence):
        position_map[gnome] = i + 1
    
    # Fill the original sequence based on the position map
    next_gnome = 1
    for i in range(n):
        if position_map[next_gnome] == 0:
            # Find the next gnome that should be in this position
            while position_map[next_gnome] == 0:
                next_gnome += 1
        original_sequence[i] = next_gnome
        position_map[next_gnome] -= 1
    
    return original_sequence

# Read input from stdin
n, m = map(int, input().split())
subsequence = [int(input()) for _ in range(m)]

# Get the original sequence and print it
original_sequence = find_original_sequence(n, m, subsequence)
for gnome in original_sequence:
    print(gnome)