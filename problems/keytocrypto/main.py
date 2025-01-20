def decrypt_autokey(ciphertext, secret_word):
    key = list(secret_word)
    message = []
    
    for i, char in enumerate(ciphertext):
        shift = ord(key[i]) - ord('A')
        original_char = chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
        message.append(original_char)
        key.append(chr((ord(original_char) - ord('A')) % 26 + ord('A')))
    
    return ''.join(message)

# Read input from stdin
ciphertext = input().strip()
secret_word = input().strip()

# Decrypt the ciphertext and print the original message
original_message = decrypt_autokey(ciphertext, secret_word)
print(original_message)