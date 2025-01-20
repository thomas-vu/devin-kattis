def generate_bit_string(n, c, broken_bits):
    hard_drive = ['1'] * n
    for bit in broken_bits:
        hard_drive[bit - 1] = '0'
    
    bit_changes = 0
    for i in range(n - 1):
        if hard_drive[i] != hard_drive[i + 1]:
            bit_changes += 1
    
    if bit_changes == c:
        return ''.join(hard_drive)
    
    for i in range(n - 1):
        if hard_drive[i] != hard_drive[i + 1]:
            continue
        if hard_drive[i] == '0':
            hard_drive[i] = '1'
        else:
            hard_drive[i + 1] = '0'
        bit_changes += 1
        
        if hard_drive[i] != hard_drive[i + 1]:
            bit_changes += 1
        
        if bit_changes == c:
            return ''.join(hard_drive)
    
    return generate_bit_string(n, c, broken_bits)

# Read input
n, c, b = map(int, input().split())
broken_bits = list(map(int, input().split()))

# Generate and print the bit string
bit_string = generate_bit_string(n, c, broken_bits)
print(bit_string)