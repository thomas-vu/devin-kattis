import math

def parse_directions(directions):
    x, y = 0.0, 0.0
    angle = 0.0
    for command in directions:
        if command[0] == 'turn':
            angle += float(command[1])
        elif command[0] == 'walk':
            distance = float(command[1])
            x += distance * math.cos(math.radians(angle))
            y += distance * math.sin(math.radians(angle))
    return (x, y)

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        directions_list = []
        for _ in range(n):
            person_directions = []
            while True:
                command = input().split()
                if command[0] == 'start':
                    break
                person_directions.append(command)
            directions_list.append(person_directions)
        
        total_x, total_y = 0.0, 0.0
        for directions in directions_list:
            x, y = parse_directions(directions)
            total_x += x
            total_y += y
        avg_x, avg_y = total_x / n, total_y / n
        
        max_distance = 0.0
        for directions in directions_list:
            end_x, end_y = parse_directions(directions)
            distance = math.sqrt((end_x - avg_x)**2 + (end_y - avg_y)**2)
            max_distance = max(max_distance, distance)
        
        print("{:.4f} {:.4f} {:.4f}".format(avg_x, avg_y, max_distance))

if __name__ == "__main__":
    main()