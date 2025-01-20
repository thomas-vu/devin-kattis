import base64

def main():
    cipher_text = input().strip()
    target = "Per" * (len(cipher_text) // 3)
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    transformations = 0
    
    while cipher_text != target:
        for i in range(len(cipher_text)):
            for char in alphabet:
                temp_text = list(cipher_text)
                temp_text[i] = char
                new_text = ''.join(temp_text)
                if new_text.lower() == target:
                    cipher_text = new_text
                    transformations += 1
                    break
        else:
            continue
        break
    
    print(transformations)

if __name__ == "__main__":
    main()