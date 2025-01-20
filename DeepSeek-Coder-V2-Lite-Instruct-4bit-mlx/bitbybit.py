def process_instructions(n, instructions):
    register = ['0'] * 32
    
    for i in range(n):
        parts = instructions[i].split()
        op = parts[0]
        
        if op == 'SET':
            bit_index = int(parts[1])
            register[bit_index] = '1'
        elif op == 'CLEAR':
            bit_index = int(parts[1])
            register[bit_index] = '0'
        elif op == 'OR':
            bit_i, bit_j = int(parts[1]), int(parts[2])
            register[bit_i] = '1' if register[bit_i] == '1' or register[bit_j] == '1' else register[bit_i]
        elif op == 'AND':
            bit_i, bit_j = int(parts[1]), int(parts[2])
            register[bit_i] = '1' if register[bit_i] == '1' and register[bit_j] == '1' else register[bit_i]
    
    return ''.join(register)

while True:
    n = int(input())
    if n == 0:
        break
    
    instructions = [input().strip() for _ in range(n)]
    result = process_instructions(n, instructions)
    print(result)