def max_music(c, n, songs):
    # Sort the songs in descending order to try and fill the CDs optimally
    songs.sort(reverse=True)
    
    # Initialize variables to store the maximum total music that can be stored on two CDs
    max_total = 0
    best_diff = float('inf')
    
    # Iterate through all possible ways to split the songs between two CDs
    for i in range(1, n):
        # Calculate the total music on each CD if we select songs[i:] and songs[:i]
        cd1 = sum(songs[:i])
        cd2 = sum(songs[i:])
        
        # Check if both CDs fit within the capacity limit
        if cd1 <= c and cd2 <= c:
            # Calculate the difference in music between the two CDs
            diff = abs(cd1 - cd2)
            
            # Update the maximum total music and best difference if a better solution is found
            if diff < best_diff or (diff == best_diff and max(cd1, cd2) > max_total):
                best_diff = diff
                max_total = max(cd1, cd2)
    
    # Return the result in the required format
    return f"{max_total} {sum(songs) - max_total}" if max_total != 0 else "No solution"

# Read input from stdin
c, n = map(int, input().split())
songs = list(map(int, input().split()))

# Output the result
print(max_music(c, n, songs))