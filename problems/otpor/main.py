import re

def calculate_resistance(resistors, circuit):
    stack = []
    i = 0
    while i < len(circuit):
        if circuit[i] == 'R':
            j = i + 1
            while j < len(circuit) and circuit[j].isdigit():
                j += 1
            resistor_type = int(circuit[i+1:j]) - 1
            stack.append(resistors[resistor_type])
            i = j
        elif circuit[i] == '(':
            stack.append(circuit[i])
            i += 1
        elif circuit[i] == ')':
            elements = []
            while stack[-1] != '(':
                elements.append(stack.pop())
            stack.pop()  # Remove '('
            while elements:
                if elements[-1] == '-':
                    elements.pop()
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a + b)
                elif elements[-1] == '|':
                    elements.pop()
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(1 / (1/a + 1/b))
                else:
                    stack.append(elements.pop())
            i += 1
        elif circuit[i] == '-':
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
            i += 1
        elif circuit[i] == '|':
            b = stack.pop()
            a = stack.pop()
            stack.append(1 / (1/a + 1/b))
            i += 1
        else:
            i += 1
    return stack[0]

# Read input
N = int(input())
resistors = list(map(float, input().split()))
circuit = input()

# Calculate and print the result
result = calculate_resistance(resistors, circuit)
print("{:.5f}".format(result))