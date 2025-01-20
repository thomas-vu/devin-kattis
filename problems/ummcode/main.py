def decode_umm_code(s):
    decoded = ""
    i = 0
    while i < len(s):
        if s[i:i+3] == "umm":
            decoded += chr(97)  # ASCII code for 'a'
            i += 3
        elif s[i:i+4] == "ummm":
            decoded += chr(105)  # ASCII code for 'i'
            i += 4
        elif s[i:i+3] == "mmm":
            decoded += chr(109)  # ASCII code for 'm'
            i += 3
        elif s[i:i+2] == "um":
            decoded += chr(117)  # ASCII code for 'u'
            i += 2
        else:
            i += 1
    return decoded

# Read input from stdin
s = ""
while True:
    line = input()
    s += line
    if line.endswith('\n'):
        break

# Decode the message
decoded_message = decode_umm_code(s)
print(decoded_message)