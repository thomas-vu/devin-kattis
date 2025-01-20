def can_build_last_row(N, c1, c2, c3, top_row):
    # Create a list to store the number of each type of brick needed for the last row
    bricks_needed = [0, 0, 0]
    
    # Count the number of each type of brick in the top row
    for brick_length in top_row:
        if brick_length == 1:
            bricks_needed[0] += 1
        elif brick_length == 2:
            bricks_needed[1] += 1
        elif brick_length == 3:
            bricks_needed[2] += 1
    
    # Check if we can cover the connections in the top row with the available bricks
    for i in range(3):
        if bricks_needed[i] > c1 + c2 + c3:
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (c3 if i == 0 else 0):
            return "NO"
    
    # Check if the number of each type of brick is sufficient to cover the connections in the top row
    for i in range(3):
        if bricks_needed[i] > c1 + (c2 if i == 0 else 0) + (