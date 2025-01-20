def encrypt_message(number_string, message):
    encrypted = ""
    for char in message:
        num = ord(char) - ord('A') if 'A' <= char <= 'Z' else (ord(char) - ord('a') + 26)
        multiplier = int(number_string[num % len(number_string)])
        new_char_code = (num * multiplier) % 52 + ord('A') if new_char_code <= ord('Z') else (new_char_code - 26 + ord('a'))
        encrypted += chr(new_char_code) if 'A' <= char <= 'Z' else chr(new_char_code + 26)
    return encrypted

def main():
    number_string = input().strip()
    n = int(input().strip())
    messages = [input().strip() for _ in range(n)]
    
    for message in messages:
        print(encrypt_message(number_string, message))

if __name__ == "__main__":
    main()