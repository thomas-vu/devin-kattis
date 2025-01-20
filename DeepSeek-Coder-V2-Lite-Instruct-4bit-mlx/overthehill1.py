def encrypt_text(matrix, plaintext):
    n = len(matrix)
    ciphertext = ""
    
    # Convert plaintext to numbers
    text_to_numbers = [ord(c) - ord('A') if c.isalpha() else (ord(c) - ord('0')) + 26 for c in plaintext]
    
    # Group into vectors and encrypt
    for i in range(0, len(text_to_numbers), n):
        vector = text_to_numbers[i:i+n]
        if len(vector) < n:  # Padding with spaces (value 36)
            vector += [36] * (n - len(vector))
        # Multiply by matrix and convert back to characters
        encrypted_vector = [sum((matrix[j][k] * vector[k]) % 37 for k in range(n)) % 37 for j in range(n)]
        ciphertext += ''.join(chr(c + ord('A') if c < 26 else chr(c - 26 + ord('0')) for c in encrypted_vector)
        
    return ciphertext

# Read input
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
plaintext = input()

# Encrypt and output the ciphertext
ciphertext = encrypt_text(matrix, plaintext)
print(ciphertext)