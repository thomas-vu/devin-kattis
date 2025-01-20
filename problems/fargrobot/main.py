def find_commands(N, sequence):
    best_sequence = ""
    
    def simulate(seq, commands):
        index = 0
        for cmd in commands:
            while seq[index] != cmd:
                index += 1
            index += 1
        return seq[:index]
    
    def generate_commands(seq, n):
        if n == 0:
            return ""
        best_gain = -1
        best_cmd = ""
        for cmd in "RGB":
            gain = len(simulate(seq, best_cmd + cmd)) - len(simulate(seq, best_cmd))
            if gain > best_gain:
                best_gain = gain
                best_cmd = cmd
        return best_cmd + generate_commands(seq, n - 1)
    
    commands = generate_commands(sequence, N)
    return commands

# Read input
N = int(input())
sequence = input()

# Get and print the commands
commands = find_commands(N, sequence)
print(commands)