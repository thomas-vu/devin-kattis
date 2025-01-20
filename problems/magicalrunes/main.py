def simulate_runes(s, d):
    n = len(s)
    states = list(s)
    
    for day in range(d):
        new_states = [''] * n
        for i in range(n):
            if i == 0:
                new_states[i] = 'B' if states[i] == 'A' else 'A'
            elif states[i - 1] == 'B':
                new_states[i] = 'A' if states[i] == 'B' else 'B'
            else:
                new_states[i] = states[i]
        states = new_states
    
    return ''.join(states)

# Read input from stdin
input_line = input().strip()
s, d = input_line.split()
d = int(d)

# Output the result
print(simulate_runes(s, d))