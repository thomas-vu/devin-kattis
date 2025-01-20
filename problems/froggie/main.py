def simulate_frogger(L, W, lanes):
    moves = {"U": -1, "D": 1, "L": -1, "R": 1}
    directions = {"U": -1, "D": 1, "L": 0, "R": 0}
    car_positions = [[] for _ in range(L)]
    
    # Initialize car positions based on lane directions and speeds
    for i in range(L):
        offset = 0 if (i % 2 == 0) else W - 1
        for j in range(lanes[i][0], W, lanes[i][1]):
            car_positions[i].append((j + offset) % W)
    
    # Process moves for Froggie
    x, y = 0, W - 1
    for move in moves:
        if move == "U": y -= 1
        elif move == "D": y += 1
        elif move == "L": x -= 1
        elif move == "R": x += 1
    
    # Check for collision at each time step
    for t in range(len(moves)):
        # Move cars
        for i in range(L):
            if (i % 2 == 0):  # Right moving lanes
                for j in range(len(car_positions[i])):
                    car_positions[i][j] = (car_positions[i][j] + 1) % W
            else:  # Left moving lanes
                for j in range(len(car_positions[i])):
                    car_positions[i][j] = (car_positions[i][j] - 1) % W
        
        # Check for collision with cars
        if y < L and x in car_positions[y]:
            return "squish"
        
        # Update Froggie's position based on the move
        x += directions[moves[t]]
    
    # Check if Froggie has safely crossed the road
    return "safe" if y == -1 else "squish"

# Main function to read input and output the result
def main():
    while True:
        try:
            L, W = map(int, input().split())
            lanes = []
            for _ in range(L):
                O, I, S = map(int, input().split())
                lanes.append((O, I, S))
            P = int(input().split()[0])
            moves = input()
            
            result = simulate_frogger(L, W, lanes)
            print(result)
        except EOFError:
            break

if __name__ == "__main__":
    main()