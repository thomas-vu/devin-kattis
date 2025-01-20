def decrypt_message(key, encrypted_message):
    x = int(key[0])
    S = key[1]
    P = key[2]
    
    n = len(S)
    d = int((n ** 1.5 + x) % n)
    
    # Create a mapping from symbols in S to their positions
    symbol_to_position = {symbol: index for index, symbol in enumerate(S)}
    
    # Create a mapping from positions in P to their symbols
    position_to_symbol = {index: symbol for index, symbol in enumerate(P)}
    
    # Decrypt the message
    decrypted_message = []
    for i in range(len(encrypted_message)):
        if i == d:
            # Use the symbol at position d from encrypted message to find the original character
            decrypted_message.append(position_to_symbol[encrypted_message[i]])
        else:
            # Use xor operation to find the original character
            pos_m_j = position_to_symbol[encrypted_message[i]]
            pos_m_jp1 = position_to_symbol[(encrypted_message[(i + 1) % len(encrypted_message)])]
            original_char = S[pos_m_j ^ pos_m_jp1]
            decrypted_message.append(original_char)
    
    return ''.join(decrypted_message)

def main():
    while True:
        x = input().strip()
        if x == '0':
            break
        S = input().strip()
        P = input().strip()
        encrypted_message = [symbol_to_position[c] for c in input().strip()]
        key = (x, S, P)
        decrypted_message = decrypt_message(key, encrypted_message)
        print(decrypted_message)

if __name__ == "__main__":
    main()