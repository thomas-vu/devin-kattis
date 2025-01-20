def rotate_string(s, n):
    rotated = ""
    for char in s:
        if char == '_':
            rotated += '_'
        elif char == '.':
            rotated += '.'
        else:
            new_char = chr(((ord(char) - ord('A') + n) % 26) + ord('A'))
            rotated += new_char
    return rotated

def process_string(s, n):
    reversed_str = s[::-1]
    return rotate_string(reversed_str, n)

def main():
    while True:
        line = input()
        if line == "0":
            break
        n, string = int(line.split()[0]), line.split()[1]
        encrypted_string = process_string(string, n)
        print(encrypted_string)

if __name__ == "__main__":
    main()