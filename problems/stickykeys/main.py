def correct_message(s):
    result = []
    for char in s:
        if result and result[-1] == char:
            continue
        else:
            result.append(char)
    return ''.join(result)

# Read input from stdin
s = input().strip()
# Process the message and output the corrected version
print(correct_message(s))