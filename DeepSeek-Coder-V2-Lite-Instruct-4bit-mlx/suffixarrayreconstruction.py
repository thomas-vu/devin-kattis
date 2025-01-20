def reconstruct_string(length, suffixes):
    # Create a list to represent the string with placeholders for unknown characters
    string = [''] * length
    
    # Process each suffix
    for pos, suffix in suffixes:
        start = pos - 1
        if '*' in suffix:
            # Replace the '*'' with a placeholder for easy comparison
            index = suffix.index('*')
            end = start + len(suffix) - index
            for i in range(start, end):
                string[i] = '*'
        else:
            for char in suffix:
                string[start] = char
                start += 1
    
    # Check for consistency of the reconstructed string
    for i in range(length):
        if string[i] == '':
            continue
        for pos, suffix in suffixes:
            real_index = pos - 1 + string[pos - 1:].index(string[i])
            if suffix[real_index] != string[i]:
                return "IMPOSSIBLE"
    
    # Construct the final string from the reconstructed list
    result = ''.join(string)
    
    # Replace '*' with the correct character if possible
    for pos, suffix in suffixes:
        start = pos - 1
        index = suffix.index('*')
        end = start + len(suffix) - index
        for i in range(start, end):
            if string[i] == '*':
                for char in set(suffix.replace('*', '')):
                    temp_string = string[:]
                    temp_string[i] = char
                    for pos, suffix in suffixes:
                        real_index = pos - 1 + temp_string[pos - 1:].index(temp_string[i])
                        if suffix[real_index] != temp_string[i]:
                            break
                    else:
                        string[i] = char
                        break
                else:
                    return "IMPOSSIBLE"
    
    return ''.join(string)

def main():
    t = int(input().strip())
    for _ in range(t):
        l, s = map(int, input().strip().split())
        suffixes = []
        for _ in range(s):
            pos, suf = input().strip().split()
            suffixes.append((int(pos), suf))
        result = reconstruct_string(l, suffixes)
        print(result)

if __name__ == "__main__":
    main()