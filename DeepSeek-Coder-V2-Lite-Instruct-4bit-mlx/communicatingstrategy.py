import sys

# Read the length of the sequence from standard input
n = int(sys.stdin.readline().strip())

# Initialize the sequence with n elements, for simplicity assume all are 1
sequence = [1] * n

# Function to ask a query about the sequence
def ask_query(l, r):
    sys.stdout.write(f"1 {l} {r}\n")
    sys.stdout.flush()
    k, S = map(int, sys.stdin.readline().strip().split())
    return k, S

# Main logic to find the sequence
for i in range(n):
    for j in range(i + 1, n):
        k, S = ask_query(i + 1, j + 1)
        # Update the sequence based on the query result if needed
        sequence[j] = S  # Assuming we can somehow deduce the value from the sum of products

# After querying, guess the sequence
sys.stdout.write("2 ")
for num in sequence:
    sys.stdout.write(f"{num} ")
sys.stdout.flush()