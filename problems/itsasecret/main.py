def clean_message(msg):
    msg = msg.upper().replace('J', 'I')
    cleaned_msg = ''
    for char in msg:
        if char.isalpha():
            cleaned_msg += char
    return cleaned_msg

def generate_key_table(key):
    key = clean_message(key)
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # I replaces J
    key_table = []
    for char in key:
        if char not in key_table and char != ' ':
            key_table.append(char)
    for char in alphabet:
        if char not in key_table and char != ' ':
            key_table.append(char)
    return [key_table[i:i+5] for i in range(0, 25, 5)]

def find_position(table, char):
    for row in range(5):
        for col in range(5):
            if table[row][col] == char:
                return (row, col)
    return None

def encode_digraph(table, digraph):
    pos1 = find_position(table, digraph[0])
    pos2 = find_position(table, digraph[1])
    
    if not pos1 or not pos2:
        return digraph  # Invalid digraph, just return it as is
    
    row1, col1 = pos1
    row2, col2 = pos2
    
    if row1 == row2:
        new_digraph = (table[row1][(col1 + 1) % 5], table[row2][(col2 + 1) % 5])
    elif col1 == col2:
        new_digraph = (table[(row1 + 1) % 5][col1], table[(row2 + 1) % 5][col2])
    else:
        new_digraph = (table[row1][col2], table[row2][col1])
    
    return ''.join(new_digraph)

def encode_message(key, message):
    table = generate_key_table(key)
    digraphs = []
    i = 0
    while i < len(message):
        if i + 1 == len(message) or message[i] == message[i + 1]:
            digraphs.append(message[i] + 'X')
            i += 1
        else:
            digraphs.append(message[i] + message[i + 1])
            i += 2
    encoded_message = ''
    for digraph in digraphs:
        if digraph[0] == 'X' and digraph[1] == 'X':
            encoded_message += encode_digraph(table, 'XX')
        else:
            encoded_message += encode_digraph(table, digraph)
    return encoded_message

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        key = input().strip()
        messages = [input().strip() for _ in range(n)]
        for message in messages:
            encoded = encode_message(key, clean_message(message))
            print(encoded.upper())
        print()

if __name__ == "__main__":
    main()