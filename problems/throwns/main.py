def main():
    n, k = map(int, input().split())
    commands = list(map(str, input().split()))
    
    egg_position = 0
    history = []
    
    for command in commands:
        if command == 'undo':
            m = int(commands[commands.index(command) + 1])
            for _ in range(m):
                if history:
                    egg_position = history.pop()
        else:
            t = int(command)
            egg_position = (egg_position + t) % n
            history.append(egg_position)
    
    print(egg_position)

if __name__ == "__main__":
    main()