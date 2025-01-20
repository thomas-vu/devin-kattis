def encrypt(message):
    values = [ord(c) - ord('a') + 1 if c != ' ' else 0 for c in message]
    encrypted = []
    for i, value in enumerate(values):
        if i == 0:
            encrypted.append(value)
        else:
            encrypted.append((value + encrypted[i-1]) % 27)
    return ''.join([chr(enc + ord('a') - 1) if enc != 0 else ' ' for enc in encrypted])

def decrypt(message):
    values = [ord(c) - ord('a') + 1 if c != ' ' else 0 for c in message]
    decrypted = []
    for i, value in enumerate(values):
        if i == 0:
            decrypted.append(value)
        else:
            prev_val = (values[i-1] if i > 0 else 0)
            decrypted.append((value - prev_val) % 27)
    return ''.join([chr(dec + ord('a') - 1) if dec != 0 else ' ' for dec in decrypted])

def main():
    n = int(input().strip())
    for _ in range(n):
        command, message = input().strip().split(' ', 1)
        if command == 'e':
            print(encrypt(message))
        elif command == 'd':
            print(decrypt(message))

if __name__ == "__main__":
    main()