def leapfrog_encryption(t, k, text):
    if t == 'E':
        return encrypt(text, k)
    else:
        return decrypt(text, k)

def encrypt(plaintext, key):
    key_values = [ord(c) - ord('a') + 1 for c in key]
    plaintext = ''.join(filter(str.isalpha, plaintext)).lower()
    n = len(plaintext)
    m = len(key)
    ciphertext = [''] * n
    
    # Place letters in positions defined by key values left-to-right
    for i in range(n):
        pos = (i * m) % n
        ciphertext[pos] = plaintext[i]
    
    # Fill in remaining positions using key values right-to-left
    for i in range(n):
        if ciphertext[i] == '':
            pos = (i * m) % n
            while ciphertext[pos] != '':
                pos = (pos + m) % n
            ciphertext[pos] = plaintext[i]
    
    return ''.join(ciphertext)

def decrypt(ciphertext, key):
    key_values = [ord(c) - ord('a') + 1 for c in key]
    n = len(ciphertext)
    m = len(key)
    plaintext = [''] * n
    
    # Place letters in positions defined by key values left-to-right
    for i in range(n):
        pos = (i * m) % n
        plaintext[pos] = ciphertext[i]
    
    # Fill in remaining positions using key values right-to-left
    for i in range(n):
        if plaintext[i] == '':
            pos = (i * m) % n
            while plaintext[pos] != '':
                pos = (pos + m) % n
            plaintext[pos] = ciphertext[i]
    
    return ''.join(plaintext)

# Read input from stdin
import sys
input_lines = sys.stdin.read().splitlines()
t, k = input_lines[0].split()
text = input_lines[1]

# Perform the encryption or decryption and output the result
result = leapfrog_encryption(t, k, text)
print(result)