def calculate_result(A, operator, B):
    if operator == '+':
        return A + B
    elif operator == '*':
        return A * B

# Read input from stdin
A = int(input())
operator = input()
B = int(input())

# Calculate and print the result
result = calculate_result(A, operator, B)
print(result)