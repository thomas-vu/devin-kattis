def min_explosions(N, S, A, monsters):
    # Sort the monsters by their life points in ascending order
    monsters.sort()
    
    # Initialize the number of explosions needed
    explosions = 0
    
    for monster in monsters:
        # Calculate the remaining life points after an explosion
        remaining_life = monster - S
        
        # If the remaining life points are less than or equal to 0, it means the monster is defeated
        if remaining_life <= 0:
            continue
        
        # Calculate the number of additional explosions needed for this monster
        additional_explosions = (remaining_life + A - 1) // A
        
        # Update the total number of explosions needed
        explosions += additional_explosions
    
    return explosions

# Read input
N, S, A = map(int, input().split())
monsters = list(map(int, input().split()))

# Calculate and print the minimum number of explosions needed
print(min_explosions(N, S, A, monsters))