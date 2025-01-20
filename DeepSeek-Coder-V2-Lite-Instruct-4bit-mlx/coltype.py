def is_valid(s):
    return all(c in 'EO' for c in s) and s[-1] == 'O' and not any(s[i] == 'O' and s[i+1] == 'O' for i in range(len(s) - 1))

def collatz_sequence_type(s):
    if not is_valid(s):
        return "INVALID"
    
    sequence = []
    for char in s:
        if char == 'E':
            sequence.append('E')
        elif char == 'O':
            if sequence and sequence[-1] == 'E':
                sequence.append('O')
            else:
                return "INVALID"
    
    n = 1
    for char in sequence:
        if char == 'E':
            n *= 2
        elif char == 'O':
            n = (3 * n) + 1
    
    return str(n)

# Read input from stdin
input_line = input().strip()
print(collatz_sequence_type(input_line))