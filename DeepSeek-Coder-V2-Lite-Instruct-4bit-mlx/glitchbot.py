def fix_instructions(target, instructions):
    # Define the movements and their effects on direction
    directions = {'north': (0, 1), 'east': (1, 0), 'south': (0, -1), 'west': (-1, 0)}
    turn_left = {'north': 'west', 'east': 'north', 'south': 'east', 'west': 'south'}
    turn_right = {'north': 'east', 'east': 'south', 'south': 'west', 'west': 'north'}
    
    # Initial position and direction
    x, y = 0, 0
    current_direction = 'north'
    
    # Parse the instructions and track position
    for i, instruction in enumerate(instructions):
        if instruction == 'Left':
            current_direction = turn_left[current_direction]
        elif instruction == 'Right':
            current_direction = turn_right[current_direction]
        elif instruction == 'Forward':
            x += directions[current_direction][0]
            y += directions[current_direction][1]
        
        # Check if the current position matches the target destination
        if x == target[0] and y == target[1]:
            return i + 1, 'Forward'
    
    # Check for corrections if the target is not reached by following instructions
    for i in range(len(instructions)):
        original_instruction = instructions[i]
        if original_instruction == 'Left':
            corrected_instruction = 'Right'
        elif original_instruction == 'Right':
            corrected_instruction = 'Left'
        else:
            continue  # Skip checking corrections for Forward instructions
        
        # Try the corrected instruction and check if it reaches the target
        for direction, movement in directions.items():
            x_temp, y_temp = x, y
            if direction == 'north':
                y_temp += movement[1]
            elif direction == 'east':
                x_temp += movement[0]
            elif direction == 'south':
                y_temp -= movement[1]
            elif direction == 'west':
                x_temp -= movement[0]
            
            if x_temp == target[0] and y_temp == target[1]:
                return i + 1, corrected_instruction
    
    # If no correction is found (which should not happen), return a default value
    return -1, 'Forward'  # This line should never be reached in a correct solution

# Main function to read input and output the result
def main():
    target = list(map(int, input().split()))
    n = int(input())
    instructions = [input().strip() for _ in range(n)]
    
    line_number, correction = fix_instructions(target, instructions)
    print(line_number, correction)

if __name__ == "__main__":
    main()