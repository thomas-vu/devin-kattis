def interpret_brainfuck(program, input_data):
    memory = [0] * 1024
    data_index = 0
    program_index = 0
    input_index = 0
    output = ""
    program_length = len(program)
    input_length = len(input_data)
    bracket_map = {}
    
    # Precompute bracket positions for efficient jumping
    stack = []
    for i, command in enumerate(program):
        if command == '[':
            stack.append(i)
        elif command == ']':
            if stack:
                start = stack.pop()
                bracket_map[start] = i
                bracket_map[i] = start
    
    instructions_count = 0
    
    while program_index < program_length and instructions_count < 50000000:
        command = program[program_index]
        
        if command == '+':
            memory[data_index] = (memory[data_index] + 1) % 256
        elif command == '-':
            memory[data_index] = (memory[data_index] - 1) % 256
        elif command == '>':
            data_index = (data_index + 1) % 1024
        elif command == '<':
            data_index = (data_index - 1) % 1024
        elif command == '.':
            output += chr(memory[data_index])
        elif command == ',':
            if input_index < input_length:
                memory[data_index] = ord(input_data[input_index])
                input_index += 1
            else:
                memory[data_index] = 255
        elif command == '[':
            if memory[data_index] == 0:
                program_index = bracket_map[program_index]
        elif command == ']':
            if memory[data_index] != 0:
                program_index = bracket_map[program_index]
        
        instructions_count += 1
        program_index += 1
    
    if instructions_count >= 50000000:
        return "Loops", program_index, bracket_map[program_index]
    else:
        return "Terminates"

def main():
    t = int(input().strip())
    results = []
    
    for _ in range(t):
        s_m, s_c, s_i = map(int, input().strip().split())
        program = input().strip()
        input_data = input().strip()
        
        result = interpret_brainfuck(program, input_data)
        if result[0] == "Loops":
            print("Loops", result[1], result[2])
        else:
            print(result[0])
    
if __name__ == "__main__":
    main()