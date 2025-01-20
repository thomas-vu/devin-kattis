import sys

def decode_arithmetic_code(N, D, encoded_message):
    p_A = D / 8
    p_B = 1 - p_A
    
    # Convert the binary representation of the encoded message to a float
    start = 0.0
    end = 1.0
    
    for i in range(N):
        mid = start + (end - start) * p_A
        if encoded_message[0] == '1':
            start = mid
        else:
            end = mid
        encoded_message = encoded_message[1:]
    
    original_message = ''
    while len(encoded_message) > 0:
        mid = start + (end - start) * p_A
        if encoded_message[0] == '1':
            original_message += 'A'
            end = mid
        else:
            original_message += 'B'
            start = mid
        encoded_message = encoded_message[1:]
    
    return original_message

# Read input
N = int(input())
D = int(input())
encoded_message = input()

# Decode the arithmetic code
original_message = decode_arithmetic_code(N, D, encoded_message)

# Output the original message
print(original_message)