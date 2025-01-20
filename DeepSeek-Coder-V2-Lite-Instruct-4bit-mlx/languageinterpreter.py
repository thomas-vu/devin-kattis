n, k = map(int, input().split())
registers = list(map(int, input().split()))
instructions = [input() for _ in range(n)]

for i, instruction in enumerate(instructions):
    parts = instruction.split()
    if parts[0] == 'add':
        x, y, z = map(int, parts[1:])
        registers[x] = (registers[y] + registers[z]) % (1 << 32)
    elif parts[0] == 'addi':
        x, y, c = map(int, parts[1:])
        registers[x] = (registers[y] + c) % (1 << 32)
    elif parts[0] == 'move':
        x, y = map(int, parts[1:])
        registers[x] = registers[y]
    elif parts[0] == 'li':
        x, c = map(int, parts[1:])
        registers[x] = c % (1 << 32)
    elif parts[0] == 'for':
        c = int(parts[1])
        for _ in range(c):
            for sub_instruction in instructions[i+1:]:
                sub_parts = sub_instruction.split()
                if sub_parts[0] == 'add':
                    x, y, z = map(int, sub_parts[1:])
                    registers[x] = (registers[y] + registers[z]) % (1 << 32)
                elif sub_parts[0] == 'addi':
                    x, y, c = map(int, sub_parts[1:])
                    registers[x] = (registers[y] + c) % (1 << 32)
                elif sub_parts[0] == 'move':
                    x, y = map(int, sub_parts[1:])
                    registers[x] = registers[y]
                elif sub_parts[0] == 'li':
                    x, c = map(int, sub_parts[1:])
                    registers[x] = c % (1 << 32)
                elif sub_parts[0] == 'rof':
                    break
    elif parts[0] == 'rof':
        break

print(' '.join(map(str, registers)))