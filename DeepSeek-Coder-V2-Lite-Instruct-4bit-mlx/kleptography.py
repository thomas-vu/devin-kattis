def autokey_decrypt(n, m, keyword, ciphertext):
    # Convert the keyword to a list of integers representing letters
    keyword_list = [ord(c) - ord('a') for c in keyword]
    
    # Initialize the plaintext list with the last n letters of the ciphertext
    plaintext = [ord(c) - ord('a') for c in ciphertext[-n:]]
    
    # Decrypt the rest of the plaintext using the Autokey cipher formula
    for i in range(m - n):
        plaintext.append((ord(ciphertext[i]) - ord('a') - keyword_list[i]) % 26)
    
    # Convert the list of integers back to letters
    plaintext_str = ''.join(chr(p + ord('a')) for p in plaintext)
    
    return plaintext_str

# Read input from stdin
n, m = map(int, input().split())
keyword = input().strip()
ciphertext = input().strip()

# Decrypt and print the plaintext
print(autokey_decrypt(n, m, keyword, ciphertext))