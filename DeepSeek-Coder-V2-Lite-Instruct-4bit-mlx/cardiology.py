def find_stable_location(r, c):
    # The goal is to find the stable location of a card after redeal iterations.
    # We need to simulate the process and find where the card ends up after each iteration.
    
    # Function to simulate one iteration and find the final position of a card
    def simulate(start_col):
        cards = [[0 for _ in range(c)] for __ in range(r)]
        index = 0
        for i in range(r):
            for j in range(c):
                cards[i][j] = index + 1
                index += 1
        
        col_order = [start_col]
        for _ in range(3):
            if start_col == 1:
                col_order.append(2)
                col_order.append(3)
            elif start_col == 2:
                col_order.append(1)
                col_order.append(3)
            else:  # start_col == 3
                col_order.append(1)
                col_order.append(2)
        
        final_cards = [[0 for _ in range(c)] for __ in range(r)]
        pos = 0
        for col in col_order:
            for i in range(r):
                final_cards[i][pos] = cards[i][col - 1]
            pos += 1
        
        # Find the stable position of the card in the final_cards array
        for i in range(r):
            for j in range(c):
                if final_cards[i][j] != 0:
                    return (i + 1, j + 1)
    
    best_p = 2
    min_distance = float('inf')
    max_iterations = 0
    
    for p in range(1, 4):
        i, j = simulate(p)
        distance = abs(i - (r // 2 + 1)) + abs(j - (c // 2 + 1))
        if distance < min_distance:
            min_distance = distance
            best_p = p
            max_iterations = 1
        elif distance == min_distance and p < best_p:
            best_p = p
            max_iterations = 1
        elif distance == min_distance and p == best_p:
            max_iterations = max(max_iterations, i + j)
    
    return f"{best_p} {i} {j} {max_iterations}"

# Read input
r, c = map(int, input().split())
result = find_stable_location(r, c)
print(result)