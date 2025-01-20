def translate_to_keypad(message):
    keypad = {
        'a': '2', 'b': '2', 'c': '2',
        'd': '3', 'e': '3', 'f': '3',
        'g': '4', 'h': '4', 'i': '4',
        'j': '5', 'k': '5', 'l': '5',
        'm': '6', 'n': '6', 'o': '6',
        'p': '7', 'q': '7', 'r': '7', 's': '7',
        't': '8', 'u': '8', 'v': '8',
        'w': '9', 'x': '9', 'y': '9', 'z': '9',
        ' ': '0'
    }
    
    sequence = ""
    i = 0
    while i < len(message):
        char = message[i]
        if char in keypad:
            sequence += keypad[char]
            # Check for consecutive characters with the same key
            count = 1
            while i + 1 < len(message) and message[i + 1] == char:
                count += 1
                i += 1
            if count > 1:
                sequence = sequence[:-count] + (keypad[char] * count)
        else:
            sequence += keypad[char]
        i += 1
    return sequence

def main():
    N = int(input())
    for case in range(1, N + 1):
        message = input()
        translated_message = translate_to_keypad(message)
        print(f"Case #{case}: {translated_message}")

if __name__ == "__main__":
    main()