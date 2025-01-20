def count_finger_presses(song):
    # Define the fingers needed for each note
    finger_map = {
        'c': [2, 3, 4],
        'd': [2, 3, 4],
        'e': [2, 3, 4],
        'f': [2, 3, 4],
        'g': [2, 3, 4],
        'a': [2, 3],
        'b': [2],
        'C': [3],
        'D': [1, 2, 3, 4],
        'E': [1, 2, 3, 4],
        'F': [1, 2, 3, 4],
        'G': [1, 2, 3, 4],
        'A': [1, 2, 3],
        'B': [1, 2]
    }
    
    # Initialize the presses for each finger to zero
    presses = [0] * 10
    
    # Process each note in the song
    for i, note in enumerate(song):
        if note in finger_map:
            needed_fingers = finger_map[note]
            for finger in range(1, 11):
                if finger in needed_fingers and (i == 0 or finger not in finger_map[song[i-1]]):
                    presses[finger - 1] += 1
    
    return presses

# Read the number of test cases
t = int(input().strip())
for _ in range(t):
    song = input().strip()
    result = count_finger_presses(song)
    print(' '.join(map(str, result)))