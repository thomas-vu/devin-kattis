# Read the input passwords
pass1 = input()
pass2 = input()

# Initialize a set to store distinct sequences
sequences = set()

# Generate all possible combinations of matching sequences
for i in range(4):
    for j in range(10):
        if str(j) == pass1[i] or str(j) == pass2[i]:
            sequences.add(''.join([str(k) for k in range(10)]))

# Output the number of distinct sequences
print(len(sequences))