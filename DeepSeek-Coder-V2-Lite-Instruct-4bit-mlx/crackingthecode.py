def decrypt_letter(decrypted, encrypted):
    mapping = {}
    for d, e in zip(decrypted, encrypted):
        if d not in mapping:
            mapping[d] = e
        elif mapping[d] != e:
            return None  # Conflict in mapping, impossible to decrypt
    return mapping

def decrypt_message(decrypted, encrypted_messages):
    for encrypted in encrypted_messages:
        mapping = decrypt_letter(decrypted, encrypted)
        if mapping is not None:
            return mapping
    return None

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    num_test_cases = int(data[index])
    index += 1
    results = []
    
    for _ in range(num_test_cases):
        n = int(data[index])
        index += 1
        encrypted_messages = [data[index + i] for i in range(n)]
        index += n
        decrypted = data[index]
        index += 1
        encrypted_x = data[index]
        index += 1
        
        mapping = decrypt_message(decrypted, encrypted_messages)
        if mapping is None:
            results.append("IMPOSSIBLE")
            continue
        
        decrypted_x = ""
        for letter in encrypted_x:
            if letter in mapping:
                decrypted_x += mapping[letter]
            else:
                decrypted_x += "?"
        results.append(decrypted_x)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()