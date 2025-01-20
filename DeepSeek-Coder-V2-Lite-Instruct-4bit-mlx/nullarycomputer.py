# Brian Huck's Nullary Core-based Prototype Computer Sorting Program
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Read the initial register values from the problem statement
registers = {
    'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0,
    'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0,
    'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
    'Y': 0, 'Z': 0
}

# Initialize the flag register
flag = False

# Sorting logic
for i in range(24):
    for j in range(i + 1, 24):
        if is_prime(registers[chr(65 + i)]):
            # Move the number from register I to the flag register
            flag = True
            registers[chr(65 + i)] -= 1
            registers[chr(65 + j)] += 1
        if flag:
            break
    if flag:
        # Move the number from the flag register to register J
        registers[chr(65 + i)] -= 1
        registers[chr(65 + j)] += 1
        flag = False

# Output the sorted register values
for i in range(24):
    print(chr(65 + i) + '0' * registers[chr(65 + i)])