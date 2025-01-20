def run_length_encode(text):
    encoded = []
    i = 0
    while i < len(text):
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            i += 1
            count += 1
        encoded.append(f"{text[i]}{count}")
        i += 1
    return ''.join(encoded)

def run_length_decode(text):
    decoded = []
    i = 0
    while i < len(text):
        count = ''
        while text[i].isdigit():
            count += text[i]
            i += 1
        decoded.append(text[i] * int(count))
        i += 1
    return ''.join(decoded)

operation = input().strip()
message = input().strip()

if operation == 'E':
    print(run_length_encode(message))
elif operation == 'D':
    print(run_length_decode(message))