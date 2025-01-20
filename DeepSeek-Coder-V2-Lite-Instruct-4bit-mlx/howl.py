def generate_valid_howl(fenrir_howl):
    valid_chars = set('AHO')
    result = list(fenrir_howl[0])  # Start with the first character

    for char in fenrir_howl[1:]:
        if char == 'W':
            continue  # Skip adding W's
        elif char == 'H' and result[-1] != 'W':
            result.append(char)  # Add H if the last added char is not W
        elif char == 'O' and (result[-1] != 'H' or result[-2:] != ['A', 'O']):
            result.append(char)  # Add O if the last added char is not H or sequence is not AO
        elif char == 'A' and result[-1] != 'O':
            result.append(char)  # Add A if the last added char is not O
        else:
            continue  # Skip invalid characters or sequences

    return ''.join(result)

# Input
fenrir_howl = input().strip()

# Generate and output the valid howl
valid_howl = generate_valid_howl(fenrir_howl)
print(valid_howl)