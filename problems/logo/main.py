import math

def simulate_commands(commands):
    x, y = 0, 0
    angle = 0
    
    for command in commands:
        cmd, value = command.split()
        value = int(value)
        
        if cmd == 'fd':
            x += value * math.cos(math.radians(angle))
            y += value * math.sin(math.radians(angle))
        elif cmd == 'bk':
            x -= value * math.cos(math.radians(angle))
            y -= value * math.sin(math.radians(angle))
        elif cmd == 'lt':
            angle += value
        elif cmd == 'rt':
            angle -= value
    
    return math.sqrt(x**2 + y**2)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    num_cases = int(data[0])
    index = 1
    
    for _ in range(num_cases):
        num_commands = int(data[index])
        commands = data[index+1:index+num_commands+1]
        index += num_commands + 1
        distance = simulate_commands(commands)
        print(f"{int(round(distance))}")

if __name__ == "__main__":
    main()