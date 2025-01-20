def apply_rules(sequence, rules):
    new_sequence = ""
    for char in sequence:
        if char in rules:
            new_sequence += rules[char]
        else:
            new_sequence += char
    return new_sequence

def generate_tree(rules, sequence, iterations):
    for _ in range(iterations):
        sequence = apply_rules(sequence, rules)
    return sequence

# Read input
n, m = map(int, input().split())
rules = {}
for _ in range(n):
    x, _, y = input().split()
    rules[x] = y
S0 = input()

# Generate the resulting sequence after m iterations
result = generate_tree(rules, S0, m)
print(result)