def solve(n, a, b):
    def generate_sequence(x1, n, a, b):
        sequence = [x1]
        for i in range(1, 2 * n, 2):
            x_i = (a * sequence[i - 1] + b) % 10001
            x_next = (a * x_i + b) % 10001
            sequence.append(x_next)
        return sequence
    
    def find_output(sequence):
        output = []
        for i in range(1, 2 * n, 2):
            output.append(sequence[i])
        return output
    
    def calculate_answer(sequence):
        answer = 0
        for num in sequence:
            answer ^= num
        return answer
    
    sequences = [generate_sequence(x1, n, a, b) for x1 in [n]]
    outputs = [find_output(seq) for seq in sequences]
    answers = [calculate_answer(out) for out in outputs]
    
    return '\n'.join(map(str, answers))

# Read input
T = int(input().strip())
inputs = [int(input().strip()) for _ in range(T)]

# Constants for the sequence generation
a = 16807
b = 28345

# Solve each test case and print the output
for n in inputs:
    result = solve(n, a, b)
    print(result)