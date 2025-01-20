def find_position(A1, m):
    sequence = [A1]
    while True:
        next_value = sequence[-1] + min_diff(sequence)
        if next_value == m:
            return len(sequence) + 1
        sequence.append(next_value)
        if m in sequence:
            return len(sequence)

def min_diff(seq):
    diffs = set()
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            diffs.add(abs(seq[j] - seq[i]))
    smallest_diff = 1
    while smallest_diff in diffs:
        smallest_diff += 1
    return smallest_diff

# Read input
A1, m = map(int, input().split())

# Find and print the result
print(find_position(A1, m))