def find_missing_number(commands):
    x, y = 0, 0
    angle = 0
    
    for command in commands:
        cmd, arg = command[0], command[1:]
        if cmd == 'fd':
            x += int(arg) if arg != '?' else 0
            y += int(arg[1:]) if arg[0] == '-' else -int(arg[1:])
        elif cmd == 'bk':
            x -= int(arg) if arg != '?' else 0
            y -= int(arg[1:]) if arg[0] == '-' else -int(arg[1:])
        elif cmd == 'lt':
            angle = (angle + int(arg)) % 360
        elif cmd == 'rt':
            angle = (angle - int(arg)) % 360
    
    return x, y, angle

def parse_commands(lines):
    commands = []
    for line in lines:
        parts = line.split()
        commands.append((parts[0], parts[1] if len(parts) > 1 else '?'))
    return commands

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    num_cases = int(data[0])
    index = 1
    
    for _ in range(num_cases):
        num_commands = int(data[index])
        index += 1
        commands = []
        for i in range(num_commands):
            commands.append(data[index])
            index += 1
        
        x, y, angle = find_missing_number(commands)
        
        for i in range(len(commands)):
            if commands[i][1] == '?':
                cmd, arg = commands[i]
                if cmd == 'fd' or cmd == 'bk':
                    arg_value = int(arg[1:]) if arg[0] == '-' else int(arg)
                    commands[i] = (cmd, f'{arg_value if cmd == "fd" else -arg_value}')
                elif cmd == 'lt' or cmd == 'rt':
                    if arg.isdigit():
                        commands[i] = (cmd, f'{360 - angle if cmd == "rt" else angle}')
        
        x_final, y_final, angle_final = find_missing_number(commands)
        print(0 if x_final == 0 and y_final == 0 else int((x_final**2 + y_final**2)**0.5))

if __name__ == "__main__":
    main()