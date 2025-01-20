keyboard = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
def decode_char(c):
    if c in keyboard:
        index = keyboard.index(c) - 1
        return keyboard[index] if index >= 0 else c
    else:
        return c
def decode_line(line):
    return ''.join(decode_char(c) for c in line)
def main():
    while True:
        try:
            line = input()
            print(decode_line(line))
        except EOFError:
            break
if __name__ == "__main__":
    main()