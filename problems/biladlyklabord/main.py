def remove_adjacent_duplicates(s):
    result = []
    for char in s:
        if not result or char != result[-1]:
            result.append(char)
    return ''.join(result)

# Read input from standard input
input_line = input().strip()
output_line = remove_adjacent_duplicates(input_line)
print(output_line)