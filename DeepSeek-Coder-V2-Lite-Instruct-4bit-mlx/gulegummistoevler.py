def find_shortest_path(instructions):
    position = (0, 0)
    direction = (0, 1)
    visited = {position}
    
    for instruction in instructions:
        if instruction == 'U':
            direction = (-direction[1], direction[0])
        elif instruction == 'D':
            direction = (direction[1], -direction[0])
        elif instruction == 'L':
            direction = (-direction[0], -direction[1])
        elif instruction == 'R':
            direction = (direction[0], -direction[1])
        else:
            for _ in range(int(instruction)):
                position = (position[0] + direction[0], position[1] + direction[1])
                if position in visited:
                    break
                visited.add(position)
    
    # Reconstruct the path to return to start
    path = []
    while position != (0, 0):
        if direction == (0, 1):
            path.append('R')
            position = (position[0] - 1, position[1])
        elif direction == (0, -1):
            path.append('L')
            position = (position[0] + 1, position[1])
        elif direction == (1, 0):
            path.append('U')
            position = (position[0], position[1] - 1)
        elif direction == (-1, 0):
            path.append('D')
            position = (position[0], position[1] + 1)
    
    path.reverse()
    return ['exit'] if len(path) == 1 else [str(len(path))] + path

# Example usage:
instructions = ["2", " < 2", " 2 > 2 > 2", " exit"]
print(" ".join(find_shortest_path(instructions)))