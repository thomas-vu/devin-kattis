def decrypt_vigenere(encrypted_message, key):
    decrypted_text = []
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        key_char = key[i]
        if i % 2 == 0:
            # Even-indexed characters are shifted forward
            shift = ord(key_char) - ord('A')
            decrypted_char = chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
        else:
            # Odd-indexed characters are shifted backward
            shift = ord(key_char) - ord('A')
            decrypted_char = chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
        decrypted_text.append(decrypted_char)
    return ''.join(decrypted_text)

# Read input from stdin
encrypted_message = input().strip()
key = input().strip()

# Decrypt the message and print the result
decrypted_message = decrypt_vigenere(encrypted_message, key)
print(decrypted_message)