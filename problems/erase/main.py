def verify_deletion(N, original_bits, overwritten_bits):
    for _ in range(N):
        new_bits = ""
        for bit in original_bits:
            if bit == '0':
                new_bits += '1'
            else:
                new_bits += '0'
        original_bits = new_bits
    return "Deletion succeeded" if original_bits == overwritten_bits else "Deletion failed"

# Read input
N = int(input())
original_bits = input()
overwritten_bits = input()

# Output the result
print(verify_deletion(N, original_bits, overwritten_bits))