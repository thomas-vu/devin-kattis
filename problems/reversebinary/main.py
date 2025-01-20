def reverse_binary(n):
    binary = bin(n)[2:]  # Convert to binary and remove the '0b' prefix
    reversed_binary = binary[::-1]  # Reverse the string
    return int(reversed_binary, 2)  # Convert back to integer from binary

# Read input
N = int(input().strip())

# Output the result
print(reverse_binary(N))