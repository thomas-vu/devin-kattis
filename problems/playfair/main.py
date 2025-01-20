def create_playfair_matrix(key):
    key = key.replace('j', 'i')
    key = key.upper().replace(' ', '')
    matrix = []
    for char in key:
        if char not in matrix:
            matrix.append(char)
    
    for char in range(65, 91):
        if chr(char) not in matrix and chr(char) != 'Q':
            matrix.append(chr(char))
    
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None

def encrypt_pair(matrix, pair):
    if pair[0] == pair[1]:
        return pair[0] + 'X' if pair[1] == 'X' else pair
    
    pos1 = find_position(matrix, pair[0])
    pos2 = find_position(matrix, pair[1])
    
    if pos1[0] == pos2[0]:
        return matrix[pos1[0]][(pos1[1]+1)%5] + matrix[pos2[0]][(pos2[1]+1)%5]
    elif pos1[1] == pos2[1]:
        return matrix[(pos1[0]+1)%5][pos1[1]] + matrix[(pos2[0]+1)%5][pos2[1]]
    else:
        return matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]]

def encrypt_message(matrix, message):
    encrypted = []
    i = 0
    while i < len(message):
        if i+1 == len(message) or message[i] == message[i+1]:
            encrypted.append(encrypt_pair(matrix, [message[i], 'X']))
            i += 1
        else:
            encrypted.append(encrypt_pair(matrix, [message[i], message[i+1]]))
            i += 2
    return ''.join(encrypted)

key = input().replace(' ', '')
message = input().replace(' ', '')
matrix = create_playfair_matrix(key)
encrypted_message = encrypt_message(matrix, message)
print(encrypted_message.upper())