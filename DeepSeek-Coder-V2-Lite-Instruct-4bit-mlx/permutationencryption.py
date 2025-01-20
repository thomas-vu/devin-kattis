def encrypt_message(key, message):
    key_length = len(key)
    message_length = len(message)
    
    # Determine the number of groups needed to pad the message
    num_groups = (message_length + key_length - 1) // key_length
    
    # Pad the message with spaces if necessary
    padded_message = message.ljust(num_groups * key_length)
    
    encrypted_message = ''
    
    for i in range(num_groups):
        group = padded_message[i * key_length:(i + 1) * key_length]
        encrypted_group = [''] * key_length
        
        for j, char in enumerate(group):
            new_position = key[j] - 1
            encrypted_group[new_position] = char
        
        encrypted_message += ''.join(encrypted_group)
    
    return f"'{encrypted_message}'"

def main():
    while True:
        input_line = input()
        if input_line == '0':
            break
        
        key_length = int(input_line.split()[0])
        key = list(map(int, input().split()))
        message = input()
        
        encrypted_msg = encrypt_message(key, message)
        print(encrypted_msg)

if __name__ == "__main__":
    main()