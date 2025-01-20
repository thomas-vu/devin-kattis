def decrypt_message(encrypted_msg):
    N = len(encrypted_msg)
    for R in range(1, N + 1):
        if N % R == 0:
            C = N // R
            if R <= C:
                matrix = [encrypted_msg[i * C:(i + 1) * C] for i in range(R)]
                decrypted_msg = ''
                for col in range(C):
                    for row in range(R):
                        decrypted_msg += matrix[row][col]
                return decrypted_msg

# Test the function with given examples
print(decrypt_message("bokbok"))  # Sample Output 1
print(decrypt_message("koaskikakosi"))  # Sample Output 2
print(decrypt_message("boudonuimilcbsaibombonisuuladici"))  # Sample Output 3