def encrypt_message(n, message):
    # Convert the message to uppercase and remove spaces
    cleaned_message = ''.join(char.upper() for char in message if char != ' ')
    encrypted_text = ''
    
    # Create a list to hold the letters in order for decryption
    decrypted_order = [''] * len(cleaned_message)
    
    # Determine the order of letters for decryption
    index = 0
    while index < len(cleaned_message):
        for i in range(len(decrypted_order)):
            if index < len(cleaned_message):
                decrypted_order[i] = cleaned_message[index]
                index += 1
    
    # Construct the encrypted text based on the decrypted order
    for i in range(len(decrypted_order)):
        encrypted_text += decrypted_order[i]
    
    return encrypted_text

# Read input until zero is encountered
messages = []
while True:
    n = int(input().strip())
    if n == 0:
        break
    message = input().strip()
    messages.append((n, message))

# Encrypt each message and output the results
for n, message in messages:
    encrypted_text = encrypt_message(n, message)
    print(encrypted_text)