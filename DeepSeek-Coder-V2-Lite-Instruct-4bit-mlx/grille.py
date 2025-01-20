def decrypt_message(n, grille, encrypted_message):
    # Check if the grille is valid
    holes = sum(row.count('.') for row in grille)
    if holes != n * n:
        return "invalid grille"
    
    # Extract the message from the grille
    decrypted_message = ""
    for _ in range(4):  # Rotate the grille 3 times (total of 4 rotations)
        for i in range(n):
            for j in range(n):
                if grille[i][j] == '.':
                    decrypted_message += encrypted_message[i * n + j]
        # Rotate the grille 90 degrees clockwise
        grille = [''.join(row[i] for row in reversed(grille)) for i in range(n)]
    
    return decrypted_message

# Read input
n = int(input())
grille = [input() for _ in range(n)]
encrypted_message = input()

# Decrypt the message
result = decrypt_message(n, grille, encrypted_message)
print(result)