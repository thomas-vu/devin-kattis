# Solution in Python 3
registers = [0] * 10
ram = list(map(lambda x: f"{x:03d}", range(1000)))
pc = 0
step_count = 0

while True:
    instruction = ram[pc]
    op_code = int(instruction[:1])
    d = int(instruction[1:2])
    n = int(instruction[2:])
    
    if op_code == 1:
        break
    elif op_code == 2:
        registers[d] = n
    elif op_code == 3:
        registers[d] += n
    elif op_code == 4:
        registers[d] *= n
    elif op_code == 5:
        registers[d] = registers[s]
    elif op_code == 6:
        registers[d] += registers[s]
    elif op_code == 7:
        registers[d] *= registers[s]
    elif op_code == 8:
        registers[d] = int(ram[registers[a]])
    elif op_code == 9:
        ram[registers[a]] = f"{registers[s]:03d}"
    elif op_code == 0:
        if registers[s] != 0:
            pc = registers[d]
            continue
    step_count += 1
    pc += 1

print(step_count)