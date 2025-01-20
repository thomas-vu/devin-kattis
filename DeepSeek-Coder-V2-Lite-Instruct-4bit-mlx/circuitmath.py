def evaluate_circuit(variables, circuit):
    stack = []
    
    for char in circuit:
        if char.isupper():  # It's an input variable
            stack.append(variables[ord(char) - ord('A')])
        elif char == '*':  # AND gate
            b = stack.pop()
            a = stack.pop()
            stack.append(a and b)
        elif char == '+':  # OR gate
            b = stack.pop()
            a = stack.pop()
            stack.append(a or b)
        elif char == '-':  # NOT gate
            a = stack.pop()
            stack.append(not a)
    
    return 'T' if stack[0] else 'F'

# Read input
n = int(input())
values = list(input().split())
circuit = input()

# Convert truth values to boolean
variables = {chr(i + ord('A')): True if val == 'T' else False for i, val in enumerate(values)}

# Evaluate and print the circuit output
print(evaluate_circuit(variables, circuit))